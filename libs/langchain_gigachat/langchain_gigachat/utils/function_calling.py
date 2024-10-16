import functools
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Type,
    Union,
    cast,
    get_type_hints,
)

from langchain_core.output_parsers import BaseGenerationOutputParser, BaseOutputParser
from langchain_core.prompts import BasePromptTemplate
from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool, Tool
from langchain_core.utils.function_calling import (
    FunctionDescription,
    is_basemodel_subclass,
)
from langchain_core.utils.json_schema import dereference_refs
from pydantic import BaseModel

from langchain_gigachat.output_parsers.gigachat_functions import (
    PydanticAttrOutputFunctionsParser,
    PydanticOutputFunctionsParser,
)


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


def gigachat_fix_schema(schema: Any) -> Any:
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
                continue
            if k == "allOf":
                if len(v) > 1:
                    raise IncorrectSchemaException()
                obj = gigachat_fix_schema(v[0])
                outer_description = schema.get("description")
                obj_out = {**obj_out, **obj}
                if outer_description:
                    # Внешнее описания приоритетнее внутреннего для ref
                    obj_out["description"] = outer_description
            if k == "anyOf":
                if len(v) > 1:
                    raise IncorrectSchemaException()
            elif isinstance(v, (list, dict)):
                obj_out[k] = gigachat_fix_schema(v)
            else:
                obj_out[k] = v
        return obj_out
    elif isinstance(schema, list):
        return [gigachat_fix_schema(el) for el in schema]
    else:
        return schema


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
    function: Union[Dict[str, Any], Type[BaseModel], Callable, BaseTool],
) -> Dict[str, Any]:
    """Convert a raw function/class to an GigaChat function.

    Args:
        function: Either a dictionary, a pydantic.BaseModel class, or a Python function.
            If a dictionary is passed in, it is assumed to already be a valid GigaChat
            function.

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


def create_gigachat_fn_runnable(
    functions: Sequence[Type[BaseModel]],
    llm: Runnable,
    prompt: Optional[BasePromptTemplate] = None,
    *,
    enforce_single_function_usage: bool = True,
    output_parser: Optional[Union[BaseOutputParser, BaseGenerationOutputParser]] = None,
    **llm_kwargs: Any,
) -> Runnable:
    """Create a runnable sequence that uses GigaChat functions."""
    if not functions:
        raise ValueError("Need to pass in at least one function. Received zero.")
    g_functions = [convert_to_gigachat_function(f) for f in functions]
    llm_kwargs_: Dict[str, Any] = {"functions": g_functions, **llm_kwargs}
    if len(g_functions) == 1 and enforce_single_function_usage:
        llm_kwargs_["function_call"] = {"name": g_functions[0]["name"]}
    output_parser = output_parser or get_gigachat_output_parser(functions)
    if prompt:
        return prompt | llm.bind(**llm_kwargs_) | output_parser
    else:
        return llm.bind(**llm_kwargs_) | output_parser


def create_structured_output_runnable(
    output_schema: Union[Type[BaseModel]],
    llm: Runnable,
    prompt: Optional[BasePromptTemplate] = None,
    *,
    output_parser: Optional[Union[BaseOutputParser, BaseGenerationOutputParser]] = None,
    enforce_function_usage: bool = True,
    **kwargs: Any,
) -> Runnable:
    """Create a runnable for extracting structured outputs."""
    # for backwards compatibility
    force_function_usage = kwargs.get(
        "enforce_single_function_usage", enforce_function_usage
    )

    return _create_gigachat_functions_structured_output_runnable(
        output_schema,
        llm,
        prompt=prompt,
        output_parser=output_parser,
        enforce_single_function_usage=force_function_usage,
        **kwargs,  # llm-specific kwargs
    )


def get_gigachat_output_parser(
    functions: Sequence[Type[BaseModel]],
) -> Union[BaseOutputParser, BaseGenerationOutputParser]:
    """Get the appropriate function output parser given the user functions.

    Args:
        functions: Sequence where element is a dictionary, a pydantic.BaseModel class,
            or a Python function. If a dictionary is passed in, it is assumed to
            already be a valid GigaChat function.

    Returns:
        A PydanticOutputFunctionsParser if functions are Pydantic classes, otherwise
            a JsonOutputFunctionsParser. If there's only one function and it is
            not a Pydantic class, then the output parser will automatically extract
            only the function arguments and not the function name.
    """
    if len(functions) > 1:
        pydantic_schema: Union[Dict, Type[BaseModel]] = {
            convert_to_gigachat_function(fn)["name"]: fn for fn in functions
        }
    else:
        pydantic_schema = functions[0]
    output_parser: Union[BaseOutputParser, BaseGenerationOutputParser] = (
        PydanticOutputFunctionsParser(pydantic_schema=pydantic_schema)
    )
    return output_parser


def _create_gigachat_functions_structured_output_runnable(
    output_schema: Union[Type[BaseModel]],
    llm: Runnable,
    prompt: Optional[BasePromptTemplate] = None,
    *,
    output_parser: Optional[Union[BaseOutputParser, BaseGenerationOutputParser]] = None,
    **llm_kwargs: Any,
) -> Runnable:
    class _OutputFormatter(BaseModel):
        """Output formatter. Всегда используй чтобы выдать ответ"""  # noqa: E501

        output: output_schema  # type: ignore

    function = _OutputFormatter
    output_parser = output_parser or PydanticAttrOutputFunctionsParser(
        pydantic_schema=_OutputFormatter, attr_name="output"
    )
    return create_gigachat_fn_runnable(
        [function], llm, prompt=prompt, output_parser=output_parser, **llm_kwargs
    )
