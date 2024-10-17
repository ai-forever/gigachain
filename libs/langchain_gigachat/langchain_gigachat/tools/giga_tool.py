import functools
import inspect
import textwrap
from typing import (
    Annotated,
    Any,
    Awaitable,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Type,
    Union,
    get_type_hints,
)

from langchain_core.callbacks import Callbacks
from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.tools import (
    FILTERED_ARGS,
    BaseTool,
    StructuredTool,
    Tool,
    create_schema_from_function,
)
from langchain_core.utils.pydantic import TypeBaseModel
from pydantic import BaseModel
from pydantic.functional_validators import SkipValidation

from langchain_gigachat.utils.function_calling import create_return_schema_from_function

FewShotExamples = Optional[List[Dict[str, Any]]]


class GigaBaseTool(BaseTool):
    """Interface of GigaChat tools with additional properties, that GigaChat supports"""

    return_schema: Annotated[Optional[TypeBaseModel], SkipValidation()] = None
    """Return schema of JSON that function returns"""
    few_shot_examples: FewShotExamples = None
    """Few-shot examples to help the model understand how to use the tool."""


class GigaTool(GigaBaseTool, Tool):
    pass


def _get_type_hints(func: Callable) -> Optional[dict[str, type]]:
    if isinstance(func, functools.partial):
        func = func.func
    try:
        return get_type_hints(func)
    except Exception:
        return None


def _get_runnable_config_param(func: Callable) -> Optional[str]:
    type_hints = _get_type_hints(func)
    if not type_hints:
        return None
    for name, type_ in type_hints.items():
        if type_ is RunnableConfig:
            return name
    return None


def _filter_schema_args(func: Callable) -> list[str]:
    filter_args = list(FILTERED_ARGS)
    if config_param := _get_runnable_config_param(func):
        filter_args.append(config_param)
    return filter_args


class GigaStructuredTool(GigaBaseTool, StructuredTool):
    @classmethod
    def from_function(
        cls,
        func: Optional[Callable] = None,
        coroutine: Optional[Callable[..., Awaitable[Any]]] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        return_direct: bool = False,
        args_schema: Optional[type[BaseModel]] = None,
        infer_schema: bool = True,
        return_schema: Optional[Type[BaseModel]] = None,
        few_shot_examples: Optional[List[Dict[str, Any]]] = None,
        *,
        response_format: Literal["content", "content_and_artifact"] = "content",
        parse_docstring: bool = False,
        error_on_invalid_docstring: bool = False,
        **kwargs: Any,
    ) -> StructuredTool:
        """Create tool from a given function.

        A classmethod that helps to create a tool from a function.

        Args:
            func: The function from which to create a tool.
            coroutine: The async function from which to create a tool.
            name: The name of the tool. Defaults to the function name.
            description: The description of the tool.
                Defaults to the function docstring.
            return_direct: Whether to return the result directly or as a callback.
                Defaults to False.
            args_schema: The schema of the tool's input arguments. Defaults to None.
            infer_schema: Whether to infer the schema from the function's signature.
                Defaults to True.
            return_schema: The return schema of tool output. Defaults to None
            few_shot_examples: Few shot examples of tool usage
            response_format: The tool response format. If "content" then the output of
                the tool is interpreted as the contents of a ToolMessage. If
                "content_and_artifact" then the output is expected to be a two-tuple
                corresponding to the (content, artifact) of a ToolMessage.
                Defaults to "content".
            parse_docstring: if ``infer_schema`` and ``parse_docstring``, will attempt
                to parse parameter descriptions from Google Style function docstrings.
                Defaults to False.
            error_on_invalid_docstring: if ``parse_docstring`` is provided, configure
                whether to raise ValueError on invalid Google Style docstrings.
                Defaults to False.
            kwargs: Additional arguments to pass to the tool
        """

        if func is not None:
            source_function = func
        elif coroutine is not None:
            source_function = coroutine
        else:
            msg = "Function and/or coroutine must be provided"
            raise ValueError(msg)
        name = name or source_function.__name__
        if args_schema is None and infer_schema:
            # schema name is appended within function
            args_schema = create_schema_from_function(
                name,
                source_function,
                parse_docstring=parse_docstring,
                error_on_invalid_docstring=error_on_invalid_docstring,
                filter_args=_filter_schema_args(source_function),
            )
        if return_schema is None and infer_schema:
            # schema name is appended within function
            return_schema = create_return_schema_from_function(source_function)
        description_ = description
        if description is None and not parse_docstring:
            description_ = source_function.__doc__ or None
        if description_ is None and args_schema:
            description_ = args_schema.__doc__ or None
        if description_ is None:
            msg = "Function must have a docstring if description not provided."
            raise ValueError(msg)
        if description is None:
            # Only apply if using the function's docstring
            description_ = textwrap.dedent(description_).strip()

        # Description example:
        # search_api(query: str) - Searches the API for the query.
        description_ = f"{description_.strip()}"
        return cls(
            name=name,
            func=func,
            coroutine=coroutine,
            args_schema=args_schema,  # type: ignore[arg-type]
            description=description_,
            return_direct=return_direct,
            response_format=response_format,
            return_schema=return_schema,
            few_shot_examples=few_shot_examples,
            **kwargs,
        )


def giga_tool(
    *args: Union[str, Callable, Runnable],
    return_direct: bool = False,
    args_schema: Optional[type] = None,
    infer_schema: bool = True,
    response_format: Literal["content", "content_and_artifact"] = "content",
    parse_docstring: bool = False,
    error_on_invalid_docstring: bool = True,
    return_schema: Optional[type] = None,
    few_shot_examples: FewShotExamples = None,
) -> Callable:
    """Make tools out of functions, can be used with or without arguments.

    Args:
        *args: The arguments to the tool.
        return_direct: Whether to return directly from the tool rather
            than continuing the agent loop. Defaults to False.
        args_schema: optional argument schema for user to specify.
            Defaults to None.
        infer_schema: Whether to infer the schema of the arguments from
            the function's signature. This also makes the resultant tool
            accept a dictionary input to its `run()` function.
            Defaults to True.
        response_format: The tool response format. If "content" then the output of
            the tool is interpreted as the contents of a ToolMessage. If
            "content_and_artifact" then the output is expected to be a two-tuple
            corresponding to the (content, artifact) of a ToolMessage.
            Defaults to "content".
        parse_docstring: if ``infer_schema`` and ``parse_docstring``, will attempt to
            parse parameter descriptions from Google Style function docstrings.
            Defaults to False.
        error_on_invalid_docstring: if ``parse_docstring`` is provided, configure
            whether to raise ValueError on invalid Google Style docstrings.
            Defaults to True.
        return_schema: The return schema of tool output. Defaults to None
        few_shot_examples: Few shot examples of tool usage
    """

    def _make_with_name(tool_name: str) -> Callable:
        def _make_tool(dec_func: Union[Callable, Runnable]) -> BaseTool:
            if isinstance(dec_func, Runnable):
                runnable = dec_func

                if runnable.input_schema.model_json_schema().get("type") != "object":
                    msg = "Runnable must have an object schema."
                    raise ValueError(msg)

                async def ainvoke_wrapper(
                    callbacks: Optional[Callbacks] = None, **kwargs: Any
                ) -> Any:
                    return await runnable.ainvoke(kwargs, {"callbacks": callbacks})

                def invoke_wrapper(
                    callbacks: Optional[Callbacks] = None, **kwargs: Any
                ) -> Any:
                    return runnable.invoke(kwargs, {"callbacks": callbacks})

                coroutine = ainvoke_wrapper
                func = invoke_wrapper
                schema: Optional[type[BaseModel]] = runnable.input_schema
                description = repr(runnable)
            elif inspect.iscoroutinefunction(dec_func):
                coroutine = dec_func
                func = None
                schema = args_schema
                description = None
            else:
                coroutine = None
                func = dec_func
                schema = args_schema
                description = None

            if infer_schema or args_schema is not None:
                return GigaStructuredTool.from_function(
                    func,
                    coroutine,
                    name=tool_name,
                    description=description,
                    return_direct=return_direct,
                    args_schema=schema,
                    infer_schema=infer_schema,
                    response_format=response_format,
                    parse_docstring=parse_docstring,
                    error_on_invalid_docstring=error_on_invalid_docstring,
                    return_schema=return_schema,
                    few_shot_examples=few_shot_examples,
                )
            # If someone doesn't want a schema applied, we must treat it as
            # a simple string->string function
            if dec_func.__doc__ is None:
                msg = (
                    "Function must have a docstring if "
                    "description not provided and infer_schema is False."
                )
                raise ValueError(msg)
            return GigaTool(
                name=tool_name,
                func=func,
                description=f"{tool_name} tool",
                return_direct=return_direct,
                coroutine=coroutine,
                response_format=response_format,
                return_schema=return_schema,
                few_shot_examples=few_shot_examples,
            )

        return _make_tool

    if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], Runnable):
        return _make_with_name(args[0])(args[1])
    elif len(args) == 1 and isinstance(args[0], str):
        # if the argument is a string, then we use the string as the tool name
        # Example usage: @tool("search", return_direct=True)
        return _make_with_name(args[0])
    elif len(args) == 1 and callable(args[0]):
        # if the argument is a function, then we use the function name as the tool name
        # Example usage: @tool
        return _make_with_name(args[0].__name__)(args[0])
    elif len(args) == 0:
        # if there are no arguments, then we use the function name as the tool name
        # Example usage: @tool(return_direct=True)
        def _partial(func: Callable[[str], str]) -> BaseTool:
            return _make_with_name(func.__name__)(func)

        return _partial
    else:
        msg = "Too many arguments for tool decorator"
        raise ValueError(msg)
