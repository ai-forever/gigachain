import collections.abc
import functools
import inspect
import types
import typing
from typing import (
    Annotated,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Type,
    Union,
    cast,
    get_type_hints,
)

from langchain_core.tools import BaseTool, Tool
from langchain_core.utils.function_calling import (
    FunctionDescription,
    is_basemodel_subclass,
)
from langchain_core.utils.json_schema import dereference_refs
from pydantic import BaseModel
from typing_extensions import get_args, get_origin, is_typeddict


class GigaFunctionDescription(FunctionDescription):
    """The parameters of the function."""

    return_parameters: Optional[dict]
    """The result settings of the function."""
    few_shot_examples: Optional[list]
    """The examples of the function."""


SCHEMA_DO_NOT_SUPPORT_MESSAGE = """Incorrect function schema!
{schema}
GigaChat currently do not support these typings: 
Union[X, Y, ...]"""


class IncorrectSchemaException(Exception):
    pass


def gigachat_fix_schema(schema: Any, prev_key: str = "") -> Any:
    """
    GigaChat do not support allOf/anyOf in JSON schema.
    We need to fix this in case of allOf with one object or
    in case with optional parameter.
    In other cases throw exception that we do not support this types of schemas
    """
    if isinstance(schema, dict):
        obj_out: Any = {}
        for k, v in schema.items():
            if k == "title":
                if isinstance(v, dict) and prev_key == "properties" and "title" in v:
                    obj_out[k] = gigachat_fix_schema(v, k)
                else:
                    continue
            if k == "allOf":
                if len(v) > 1:
                    raise IncorrectSchemaException()
                obj = gigachat_fix_schema(v[0], k)
                outer_description = schema.get("description")
                obj_out = {**obj_out, **obj}
                if outer_description:
                    # Внешнее описания приоритетнее внутреннего для ref
                    obj_out["description"] = outer_description
            if k == "anyOf":
                if len(v) > 1:
                    raise IncorrectSchemaException()
            elif isinstance(v, (list, dict)):
                obj_out[k] = gigachat_fix_schema(v, k)
            else:
                obj_out[k] = v
        return obj_out
    elif isinstance(schema, list):
        return [gigachat_fix_schema(el) for el in schema]
    else:
        return schema


def _convert_typed_dict_to_gigachat_function(
    typed_dict: type,
) -> GigaFunctionDescription:
    visited: dict = {}
    from pydantic.v1 import BaseModel

    model = cast(
        type[BaseModel],
        _convert_any_typed_dicts_to_pydantic(typed_dict, visited=visited),
    )
    return convert_pydantic_to_gigachat_function(model)  # type: ignore


_MAX_TYPED_DICT_RECURSION = 25


def _is_optional(field: type) -> bool:
    return typing.get_origin(field) is Union and type(None) in typing.get_args(field)


def _convert_any_typed_dicts_to_pydantic(
    type_: type, *, visited: dict, depth: int = 0
) -> type:
    from pydantic.v1 import Field as Field_v1
    from pydantic.v1 import create_model as create_model_v1

    if type_ in visited:
        return visited[type_]
    elif depth >= _MAX_TYPED_DICT_RECURSION:
        return type_
    elif is_typeddict(type_):
        typed_dict = type_
        docstring = inspect.getdoc(typed_dict)
        annotations_ = typed_dict.__annotations__
        description, arg_descriptions = _parse_google_docstring(
            docstring, list(annotations_)
        )
        fields: dict = {}
        for arg, arg_type in annotations_.items():
            if get_origin(arg_type) is Annotated:
                annotated_args = get_args(arg_type)
                new_arg_type = _convert_any_typed_dicts_to_pydantic(
                    annotated_args[0], depth=depth + 1, visited=visited
                )
                field_kwargs = dict(zip(("default", "description"), annotated_args[1:]))
                if (field_desc := field_kwargs.get("description")) and not isinstance(
                    field_desc, str
                ):
                    msg = (
                        f"Invalid annotation for field {arg}. Third argument to "
                        f"Annotated must be a string description, received value of "
                        f"type {type(field_desc)}."
                    )
                    raise ValueError(msg)
                elif arg_desc := arg_descriptions.get(arg):
                    field_kwargs["description"] = arg_desc
                else:
                    pass
                fields[arg] = (new_arg_type, Field_v1(**field_kwargs))
            else:
                new_arg_type = _convert_any_typed_dicts_to_pydantic(
                    arg_type, depth=depth + 1, visited=visited
                )
                if _is_optional(new_arg_type):
                    field_kwargs = {"default": None}
                else:
                    field_kwargs = {"default": ...}
                if arg_desc := arg_descriptions.get(arg):
                    field_kwargs["description"] = arg_desc
                fields[arg] = (new_arg_type, Field_v1(**field_kwargs))
        model = create_model_v1(typed_dict.__name__, **fields)
        model.__doc__ = description
        visited[typed_dict] = model
        return model
    elif (origin := get_origin(type_)) and (type_args := get_args(type_)):
        subscriptable_origin = _py_38_safe_origin(origin)
        type_args = tuple(
            _convert_any_typed_dicts_to_pydantic(arg, depth=depth + 1, visited=visited)
            for arg in type_args  # type: ignore[index]
        )
        return subscriptable_origin[type_args]  # type: ignore[index]
    else:
        return type_


def _py_38_safe_origin(origin: type) -> type:
    origin_union_type_map: dict[type, Any] = (
        {types.UnionType: Union} if hasattr(types, "UnionType") else {}
    )

    origin_map: dict[type, Any] = {
        dict: dict,
        list: list,
        tuple: tuple,
        set: set,
        collections.abc.Iterable: typing.Iterable,
        collections.abc.Mapping: typing.Mapping,
        collections.abc.Sequence: typing.Sequence,
        collections.abc.MutableMapping: typing.MutableMapping,
        **origin_union_type_map,
    }
    return cast(type, origin_map.get(origin, origin))


def _parse_google_docstring(
    docstring: Optional[str],
    args: list[str],
    *,
    error_on_invalid_docstring: bool = False,
) -> tuple[str, dict]:
    """Parse the function and argument descriptions from the docstring of a function.

    Assumes the function docstring follows Google Python style guide.
    """
    if docstring:
        docstring_blocks = docstring.split("\n\n")
        if error_on_invalid_docstring:
            filtered_annotations = {
                arg for arg in args if arg not in ("run_manager", "callbacks", "return")
            }
            if filtered_annotations and (
                len(docstring_blocks) < 2 or not docstring_blocks[1].startswith("Args:")
            ):
                msg = "Found invalid Google-Style docstring."
                raise ValueError(msg)
        descriptors = []
        args_block = None
        past_descriptors = False
        for block in docstring_blocks:
            if block.startswith("Args:"):
                args_block = block
                break
            elif block.startswith(("Returns:", "Example:")):
                # Don't break in case Args come after
                past_descriptors = True
            elif not past_descriptors:
                descriptors.append(block)
            else:
                continue
        description = " ".join(descriptors)
    else:
        if error_on_invalid_docstring:
            msg = "Found invalid Google-Style docstring."
            raise ValueError(msg)
        description = ""
        args_block = None
    arg_descriptions = {}
    if args_block:
        arg = None
        for line in args_block.split("\n")[1:]:
            if ":" in line:
                arg, desc = line.split(":", maxsplit=1)
                arg_descriptions[arg.strip()] = desc.strip()
            elif arg:
                arg_descriptions[arg.strip()] += " " + line.strip()
    return description, arg_descriptions


def _get_python_function_name(function: Callable) -> str:
    """Get the name of a Python function."""
    return function.__name__


def _model_to_schema(model: Type[BaseModel]) -> dict:
    if hasattr(model, "model_json_schema"):
        # Pydantic 2
        from langchain_gigachat.utils.pydantic_generator import GigaChatJsonSchema

        return model.model_json_schema(schema_generator=GigaChatJsonSchema)
    elif hasattr(model, "schema"):
        return model.schema()  # Pydantic 1
    else:
        msg = "Model must be a Pydantic model."
        raise TypeError(msg)


def _convert_return_schema(
    return_model: Optional[Union[Type[BaseModel], dict[str, Any]]],
) -> Dict[str, Any]:
    if not return_model:
        return {}

    if isinstance(return_model, dict):
        return_schema = return_model
    else:
        return_schema = dereference_refs(_model_to_schema(return_model))

    if "definitions" in return_schema:  # pydantic 1
        return_schema.pop("definitions", None)
    if "$defs" in return_schema:  # pydantic 2
        return_schema.pop("$defs", None)
    if "title" in return_schema:
        return_schema.pop("title", None)

    for key in return_schema["properties"]:
        if "type" not in return_schema["properties"][key]:
            return_schema["properties"][key]["type"] = "object"
        if "description" not in return_schema["properties"][key]:
            return_schema["properties"][key]["description"] = ""

    return return_schema


def format_tool_to_gigachat_function(tool: BaseTool) -> GigaFunctionDescription:
    """Format tool into the GigaChat function API."""
    if not tool.description or tool.description == "":
        raise RuntimeError(
            "Incorrect function or tool description. Description is required."
        )
    tool_schema = tool.args_schema
    if tool.tool_call_schema:
        tool_schema = tool.tool_call_schema

    if hasattr(tool, "return_schema") and tool.return_schema:
        # return_schema = _convert_return_schema(tool.return_schema)
        return_schema = tool.return_schema
    else:
        return_schema = None

    if hasattr(tool, "few_shot_examples") and tool.few_shot_examples:
        few_shot_examples = tool.few_shot_examples
    else:
        few_shot_examples = None

    is_simple_tool = isinstance(tool, Tool) and not tool.args_schema

    if tool_schema and not is_simple_tool:
        return convert_pydantic_to_gigachat_function(
            tool_schema,
            name=tool.name,
            description=tool.description,
            return_model=return_schema,
            few_shot_examples=few_shot_examples,
        )
    else:
        if hasattr(tool, "return_schema") and tool.return_schema:
            return_schema = _convert_return_schema(tool.return_schema)
        else:
            return_schema = None

        return {
            "name": tool.name,
            "description": tool.description,
            "parameters": {"properties": {}, "type": "object"},
            "few_shot_examples": few_shot_examples,
            "return_parameters": return_schema,
        }


def convert_pydantic_to_gigachat_function(
    model: Type[BaseModel],
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    return_model: Optional[Type[BaseModel]] = None,
    few_shot_examples: Optional[List[dict]] = None,
) -> GigaFunctionDescription:
    """Converts a Pydantic model to a function description for the GigaChat API."""
    schema = dereference_refs(_model_to_schema(model))
    if "definitions" in schema:  # pydantic 1
        schema.pop("definitions", None)
    if "$defs" in schema:  # pydantic 2
        schema.pop("$defs", None)
    title = schema.pop("title", None)
    if "properties" in schema:
        for key in schema["properties"]:
            if "type" not in schema["properties"][key]:
                schema["properties"][key]["type"] = "object"
            if "description" not in schema["properties"][key]:
                schema["properties"][key]["description"] = ""

    if return_model:
        return_schema = _convert_return_schema(return_model)
    else:
        return_schema = None

    description = description or schema.get("description", None)
    if not description or description == "":
        raise ValueError(
            "Incorrect function or tool description. Description is required."
        )

    return GigaFunctionDescription(
        name=name or title,
        description=description,
        parameters=schema,
        return_parameters=return_schema,
        few_shot_examples=few_shot_examples,
    )


def _get_type_hints(func: Callable) -> Optional[Dict[str, Type]]:
    if isinstance(func, functools.partial):
        func = func.func
    try:
        return get_type_hints(func)
    except Exception:
        return None


def create_return_schema_from_function(func: Callable) -> Optional[Type[BaseModel]]:
    return_type = get_type_hints(func).get("return", Any)
    if (
        return_type is not str
        and return_type is not int
        and return_type is not float
        and return_type is not None
    ):
        try:
            if isinstance(return_type, type) and is_basemodel_subclass(return_type):
                return return_type
        except TypeError:  # It's normal for testing
            return None

    return None


def convert_python_function_to_gigachat_function(
    function: Callable,
) -> GigaFunctionDescription:
    """Convert a Python function to an GigaChat function-calling API compatible dict.

    Assumes the Python function has type hints and a docstring with a description. If
        the docstring has Google Python style argument descriptions, these will be
        included as well.

    Args:
        function: The Python function to convert.

    Returns:
        The GigaChat function description.
    """
    from langchain_core import tools

    func_name = _get_python_function_name(function)
    model = tools.create_schema_from_function(
        func_name,
        function,
        filter_args=(),
        parse_docstring=True,
        error_on_invalid_docstring=False,
        include_injected=False,
    )
    _return_schema = create_return_schema_from_function(function)
    return convert_pydantic_to_gigachat_function(
        model, name=func_name, return_model=_return_schema, description=model.__doc__
    )


def convert_to_gigachat_function(
    function: Union[Dict[str, Any], Type[BaseModel], Callable, BaseTool, type],
) -> Dict[str, Any]:
    """Convert a raw function/class to an GigaChat function.

    Args:
        function:
            A dictionary, Pydantic BaseModel class, TypedDict class, a LangChain
            Tool object, or a Python function. If a dictionary is passed in, it is
            assumed to already be a valid GigaChat function.

    Returns:
        A dict version of the passed in function which is compatible with the
            GigaChat function-calling API.
    """
    from langchain_core.tools import BaseTool

    if isinstance(function, dict):
        return function
    elif isinstance(function, type) and is_basemodel_subclass(function):
        function = cast(Dict, convert_pydantic_to_gigachat_function(function))
    elif isinstance(function, BaseTool):
        function = cast(Dict, format_tool_to_gigachat_function(function))
    elif is_typeddict(function):
        function = cast(
            dict, _convert_typed_dict_to_gigachat_function(cast(type, function))
        )
    elif callable(function):
        function = cast(Dict, convert_python_function_to_gigachat_function(function))
    else:
        raise ValueError(
            f"Unsupported function type {type(function)}. Functions must be passed in"
            f" as Dict, pydantic.BaseModel, or Callable."
        )
    try:
        return gigachat_fix_schema(function)
    except IncorrectSchemaException:
        raise IncorrectSchemaException(
            SCHEMA_DO_NOT_SUPPORT_MESSAGE.format(schema=function)
        )


def convert_to_gigachat_tool(
    tool: Union[Dict[str, Any], Type[BaseModel], Callable, BaseTool],
) -> Dict[str, Any]:
    """Convert a raw function/class to an GigaChat tool.

    Args:
        tool: Either a dictionary, a pydantic.BaseModel class, Python function, or
            BaseTool. If a dictionary is passed in, it is assumed to already be a valid
            GigaChat tool, GigaChat function,
            or a JSON schema with top-level 'title' and
            'description' keys specified.

    Returns:
        A dict version of the passed in tool which is compatible with the
            GigaChat tool-calling API.
    """
    if isinstance(tool, dict) and tool.get("type") == "function" and "function" in tool:
        return tool
    function = convert_to_gigachat_function(tool)
    return {"type": "function", "function": function}
