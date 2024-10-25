# mypy: disable-error-code="annotation-unchecked"
from typing import Annotated as ExtensionsAnnotated
from typing import Any, Callable, List, Literal, Optional, Union
from typing import TypedDict as TypingTypedDict

import pytest
from pydantic import BaseModel as BaseModelV2Maybe  # pydantic: ignore
from pydantic import Field as FieldV2Maybe  # pydantic: ignore
from typing_extensions import TypedDict as ExtensionsTypedDict

from langchain_gigachat.tools.giga_tool import FewShotExamples, GigaBaseTool, giga_tool

try:
    from typing import Annotated as TypingAnnotated  # type: ignore[attr-defined]
except ImportError:
    TypingAnnotated = ExtensionsAnnotated

from langchain_core.runnables import Runnable, RunnableLambda
from langchain_core.tools import BaseTool, StructuredTool, Tool, tool
from pydantic import BaseModel, Field

from langchain_gigachat.utils.function_calling import (
    IncorrectSchemaException,
    convert_to_gigachat_function,
)


@pytest.fixture()
def pydantic() -> type[BaseModel]:
    class dummy_function(BaseModel):  # noqa: N801
        """dummy function"""

        arg1: Optional[int] = Field(..., description="foo")
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'")

    return dummy_function


@pytest.fixture()
def annotated_function() -> Callable:
    def dummy_function(
        arg1: ExtensionsAnnotated[Optional[int], "foo"],
        arg2: ExtensionsAnnotated[Literal["bar", "baz"], "one of 'bar', 'baz'"],
    ) -> None:
        """dummy function"""

    return dummy_function


@pytest.fixture()
def function() -> Callable:
    def dummy_function(arg1: Optional[int], arg2: Literal["bar", "baz"]) -> None:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """

    return dummy_function


@pytest.fixture()
def runnable() -> Runnable:
    class Args(ExtensionsTypedDict):
        arg1: ExtensionsAnnotated[Optional[int], "foo"]
        arg2: ExtensionsAnnotated[Literal["bar", "baz"], "one of 'bar', 'baz'"]

    def dummy_function(input_dict: Args) -> None:
        pass

    return RunnableLambda(dummy_function)


@pytest.fixture()
def dummy_tool() -> BaseTool:
    class Schema(BaseModel):
        arg1: Optional[int] = Field(..., description="foo")
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'")

    class DummyFunction(BaseTool):
        args_schema: type[BaseModel] = Schema
        name: str = "dummy_function"
        description: str = "dummy function"

        def _run(self, *args: Any, **kwargs: Any) -> Any:
            pass

    return DummyFunction()


@pytest.fixture()
def dummy_structured_tool() -> StructuredTool:
    class Schema(BaseModel):
        arg1: Optional[int] = Field(..., description="foo")
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'")

    return StructuredTool.from_function(
        lambda x: None,
        name="dummy_function",
        description="dummy function",
        args_schema=Schema,
    )


@pytest.fixture()
def dummy_pydantic() -> type[BaseModel]:
    class dummy_function(BaseModel):  # noqa: N801
        """dummy function"""

        arg1: Optional[int] = Field(..., description="foo")
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'")

    return dummy_function


@pytest.fixture()
def dummy_pydantic_v2() -> type[BaseModelV2Maybe]:
    class dummy_function(BaseModelV2Maybe):  # noqa: N801
        """dummy function"""

        arg1: Optional[int] = FieldV2Maybe(..., description="foo")
        arg2: Literal["bar", "baz"] = FieldV2Maybe(
            ..., description="one of 'bar', 'baz'"
        )

    return dummy_function


@pytest.fixture()
def dummy_typing_typed_dict() -> type:
    class dummy_function(TypingTypedDict):  # noqa: N801
        """dummy function"""

        arg1: TypingAnnotated[Optional[int], None, "foo"]  # noqa: F821
        arg2: TypingAnnotated[Literal["bar", "baz"], ..., "one of 'bar', 'baz'"]  # noqa: F722

    return dummy_function


@pytest.fixture()
def dummy_typing_typed_dict_docstring() -> type:
    class dummy_function(TypingTypedDict):  # noqa: N801
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """

        arg1: Optional[int]
        arg2: Literal["bar", "baz"]

    return dummy_function


@pytest.fixture()
def dummy_extensions_typed_dict() -> type:
    class dummy_function(ExtensionsTypedDict):  # noqa: N801
        """dummy function"""

        arg1: ExtensionsAnnotated[int, None, "foo"]
        arg2: ExtensionsAnnotated[Literal["bar", "baz"], ..., "one of 'bar', 'baz'"]

    return dummy_function


@pytest.fixture()
def dummy_extensions_typed_dict_docstring() -> type:
    class dummy_function(ExtensionsTypedDict):  # noqa: N801
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """

        arg1: Optional[int]
        arg2: Literal["bar", "baz"]

    return dummy_function


@pytest.fixture()
def json_schema() -> dict:
    return {
        "name": "dummy_function",
        "description": "dummy function",
        "return_parameters": None,
        "few_shot_examples": None,
        "parameters": {
            "type": "object",
            "description": "dummy function",
            "properties": {
                "arg1": {"description": "foo", "type": "integer"},
                "arg2": {
                    "description": "one of 'bar', 'baz'",
                    "enum": ["bar", "baz"],
                    "type": "string",
                },
            },
            "required": ["arg2"],
        },
    }


class Dummy:
    def dummy_function(self, arg1: Optional[int], arg2: Literal["bar", "baz"]) -> None:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """


class DummyWithClassMethod:
    @classmethod
    def dummy_function(cls, arg1: Optional[int], arg2: Literal["bar", "baz"]) -> None:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """


@pytest.fixture()
def function_with_title_parameters() -> type[BaseModel]:
    class Resource(BaseModel):
        """
        Represents a resource. Give it a good title and a short description.
        """

        url: str
        title: str
        description: str

    class ExtractResources(BaseModel):
        """
        Extract the 3-5 most relevant resources from a search result.
        """

        resources: TypingAnnotated[List[Resource], Field(description="массив ресурсов")]

    return ExtractResources


@pytest.mark.parametrize(
    "func",
    [
        "pydantic",
        "function",
        "dummy_structured_tool",
        "dummy_tool",
        "dummy_typing_typed_dict",
        "dummy_typing_typed_dict_docstring",
        "dummy_extensions_typed_dict",
        "dummy_extensions_typed_dict_docstring",
        "annotated_function",
        "dummy_pydantic",
        "json_schema",
        Dummy.dummy_function,
        DummyWithClassMethod.dummy_function,
    ],
)
def test_convert_to_gigachat_function(
    func: Any, request: pytest.FixtureRequest
) -> None:
    expected = {
        "name": "dummy_function",
        "description": "dummy function",
        "return_parameters": None,
        "few_shot_examples": None,
        "parameters": {
            "type": "object",
            "description": "dummy function",
            "properties": {
                "arg1": {"description": "foo", "type": "integer"},
                "arg2": {
                    "description": "one of 'bar', 'baz'",
                    "enum": ["bar", "baz"],
                    "type": "string",
                },
            },
            "required": ["arg2"],
        },
    }
    if isinstance(func, str):
        func = request.getfixturevalue(func)

    actual = convert_to_gigachat_function(func)  # type: ignore
    assert actual == expected


def test_runnable(runnable: Runnable) -> None:
    expected = {
        "name": "dummy_function",
        "description": "dummy function",
        "return_parameters": None,
        "few_shot_examples": None,
        "parameters": {
            "type": "object",
            "description": "dummy function",
            "properties": {
                "arg1": {"type": "integer", "description": ""},
                "arg2": {"enum": ["bar", "baz"], "type": "string", "description": ""},
            },
            "required": ["arg2"],
        },
    }
    actual = convert_to_gigachat_function(
        runnable.as_tool(description="dummy function")
    )
    assert actual == expected


def test_simple_tool() -> None:
    def my_function(input_string: str) -> str:  # type: ignore
        pass

    tool = Tool(name="dummy_function", func=my_function, description="test description")
    actual = convert_to_gigachat_function(tool)
    expected = {
        "name": "dummy_function",
        "description": "test description",
        "return_parameters": None,
        "few_shot_examples": None,
        "parameters": {"properties": {}, "type": "object"},
    }
    assert actual == expected


@pytest.mark.xfail(reason="Direct pydantic v2 models not yet supported")
def test_convert_to_openai_function_nested_v2() -> None:
    class NestedV2(BaseModelV2Maybe):
        nested_v2_arg1: int = FieldV2Maybe(..., description="foo")
        nested_v2_arg2: Literal["bar", "baz"] = FieldV2Maybe(
            ..., description="one of 'bar', 'baz'"
        )

    def my_function(arg1: NestedV2) -> None:
        """dummy function"""

    convert_to_gigachat_function(my_function)


def test_convert_to_gigachat_function_nested() -> None:
    class Nested(BaseModel):
        nested_arg1: int = Field(..., description="foo")
        nested_arg2: Literal["bar", "baz"] = Field(
            ..., description="one of 'bar', 'baz'"
        )

    def my_function(arg1: Nested) -> None:
        """dummy function"""

    expected = {
        "name": "my_function",
        "description": "dummy function",
        "parameters": {
            "type": "object",
            "description": "dummy function",
            "properties": {
                "arg1": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "nested_arg1": {"type": "integer", "description": "foo"},
                        "nested_arg2": {
                            "type": "string",
                            "enum": ["bar", "baz"],
                            "description": "one of 'bar', 'baz'",
                        },
                    },
                    "required": ["nested_arg1", "nested_arg2"],
                }
            },
            "required": ["arg1"],
        },
        "return_parameters": None,
        "few_shot_examples": None,
    }

    actual = convert_to_gigachat_function(my_function)
    assert actual == expected


@pytest.mark.xfail(
    reason="Pydantic converts Optional[str] to str in .model_json_schema()"
)
def test_function_optional_param() -> None:
    @tool
    def func5(a: Optional[str], b: str, c: Optional[list[Optional[str]]]) -> None:
        """A test function"""

    func = convert_to_gigachat_function(func5)
    req = func["parameters"]["required"]
    assert set(req) == {"b"}


def test_function_no_params() -> None:
    def nullary_function() -> None:
        """nullary function"""

    func = convert_to_gigachat_function(nullary_function)
    req = func["parameters"].get("required")
    assert not req


def test_convert_union_fail() -> None:
    @tool
    def magic_function(input: Union[int, float]) -> str:  # type: ignore
        """Compute a magic function."""

    with pytest.raises(IncorrectSchemaException):
        convert_to_gigachat_function(magic_function)


def test_function_with_title_parameters(
    function_with_title_parameters: type[BaseModel],
) -> None:
    expected = {
        "name": "ExtractResources",
        "description": "Extract the 3-5 most relevant resources from a search result.",
        "parameters": {
            "description": "Extract the 3-5 most relevant resources from a search result.",  # noqa
            # noqa
            "properties": {
                "resources": {
                    "description": "массив ресурсов",
                    "items": {
                        "description": "Represents a resource. Give it a good title and a short description.",  # noqa
                        # noqa
                        "properties": {
                            "url": {"type": "string"},
                            "title": {"type": "string"},
                            "description": {"type": "string"},
                        },
                        "required": ["url", "title", "description"],
                        "type": "object",
                    },
                    "type": "array",
                }
            },
            "required": ["resources"],
            "type": "object",
        },
        "return_parameters": None,
        "few_shot_examples": None,
    }
    actual = convert_to_gigachat_function(function_with_title_parameters)
    assert actual == expected


def test_convert_to_function_no_args() -> None:
    @tool
    def empty_tool() -> str:
        """No args"""
        return "foo"

    actual = convert_to_gigachat_function(empty_tool)
    assert actual == {
        "name": "empty_tool",
        "description": "No args",
        "few_shot_examples": None,
        "return_parameters": None,
        "parameters": {"description": "No args", "properties": {}, "type": "object"},
    }


# Test for return parameters and few shot examples


class ReturnParameters(BaseModel):
    """dummy function"""

    arg1: Optional[int] = Field(..., description="foo")
    arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'")


@pytest.fixture()
def annotated_function_return_parameters() -> Callable:
    def dummy_function(  # type: ignore
        arg1: ExtensionsAnnotated[int, "foo"],
        arg2: ExtensionsAnnotated[Literal["bar", "baz"], "one of 'bar', 'baz'"],
    ) -> ReturnParameters:
        """dummy function"""

    return dummy_function


@pytest.fixture()
def function_return_parameters() -> Callable:
    def dummy_function(  # type: ignore
        arg1: int, arg2: Literal["bar", "baz"]
    ) -> ReturnParameters:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """

    return dummy_function


@pytest.fixture()
def dummy_return_parameters_with_fews_tool() -> GigaBaseTool:
    class Schema(BaseModel):
        arg1: int = Field(..., description="foo")
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'")

    class DummyFunction(GigaBaseTool):
        args_schema: type[BaseModel] = Schema
        name: str = "dummy_function"
        description: str = "dummy function"
        return_schema: type[BaseModel] = ReturnParameters
        few_shot_examples: FewShotExamples = [
            {"arg1": 1, "arg2": "bar"},
            {"arg1": 2, "arg2": "baz"},
        ]

        def _run(self, *args: Any, **kwargs: Any) -> Any:
            pass

    return DummyFunction()


@pytest.fixture()
def dummy_return_parameters_with_fews_decorator() -> Callable:
    @giga_tool(
        few_shot_examples=[{"arg1": 1, "arg2": "bar"}, {"arg1": 2, "arg2": "baz"}]
    )
    def dummy_function(  # type: ignore
        arg1: Optional[int] = Field(..., description="foo"),
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'"),
    ) -> ReturnParameters:
        """dummy function"""
        pass

    return dummy_function


@pytest.fixture()
def dummy_return_parameters_through_arg_with_fews_decorator() -> Callable:
    @giga_tool(
        few_shot_examples=[{"arg1": 1, "arg2": "bar"}, {"arg1": 2, "arg2": "baz"}],
        return_schema=ReturnParameters,
    )
    def dummy_function(
        arg1: Optional[int] = Field(..., description="foo"),
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'"),
    ) -> None:
        """dummy function"""
        pass

    return dummy_function


@pytest.fixture()
def json_schema_return_parameters_with_fews() -> dict:
    return {
        "name": "dummy_function",
        "description": "dummy function",
        "return_parameters": {
            "type": "object",
            "description": "dummy function",
            "properties": {
                "arg1": {"description": "foo", "type": "integer"},
                "arg2": {
                    "description": "one of 'bar', 'baz'",
                    "enum": ["bar", "baz"],
                    "type": "string",
                },
            },
            "required": ["arg2"],
        },
        "few_shot_examples": [{"arg1": 1, "arg2": "bar"}, {"arg1": 2, "arg2": "baz"}],
        "parameters": {
            "type": "object",
            "description": "dummy function",
            "properties": {
                "arg1": {"description": "foo", "type": "integer"},
                "arg2": {
                    "description": "one of 'bar', 'baz'",
                    "enum": ["bar", "baz"],
                    "type": "string",
                },
            },
            "required": ["arg2"],
        },
    }


class DummyReturnParameters:
    def dummy_function(  # type: ignore
        self, arg1: Optional[int], arg2: Literal["bar", "baz"]
    ) -> ReturnParameters:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """


class DummyReturnParametersWithClassMethod:
    @classmethod
    def dummy_function(  # type: ignore
        cls, arg1: Optional[int], arg2: Literal["bar", "baz"]
    ) -> ReturnParameters:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """


@pytest.mark.parametrize(
    "func",
    [
        "annotated_function_return_parameters",
        "function_return_parameters",
        "dummy_return_parameters_with_fews_tool",
        "dummy_return_parameters_with_fews_decorator",
        "dummy_return_parameters_through_arg_with_fews_decorator",
        "json_schema_return_parameters_with_fews",
        DummyReturnParameters.dummy_function,
        DummyReturnParametersWithClassMethod.dummy_function,
    ],
)
def test_function_with_return_parameters(
    func: Any, request: pytest.FixtureRequest
) -> None:
    return_params_expected = {
        "type": "object",
        "description": "dummy function",
        "properties": {
            "arg1": {"description": "foo", "type": "integer"},
            "arg2": {
                "description": "one of 'bar', 'baz'",
                "enum": ["bar", "baz"],
                "type": "string",
            },
        },
        "required": ["arg2"],
    }
    if isinstance(func, str):
        func = request.getfixturevalue(func)

    actual_func = convert_to_gigachat_function(func)
    assert actual_func["return_parameters"] == return_params_expected


@pytest.mark.parametrize(
    "func",
    [
        "dummy_return_parameters_with_fews_tool",
        "dummy_return_parameters_with_fews_decorator",
        "dummy_return_parameters_through_arg_with_fews_decorator",
        "json_schema_return_parameters_with_fews",
    ],
)
def test_function_with_few_shots(func: Any, request: pytest.FixtureRequest) -> None:
    few_shots_expected = [{"arg1": 1, "arg2": "bar"}, {"arg1": 2, "arg2": "baz"}]
    if isinstance(func, str):
        func = request.getfixturevalue(func)

    actual_func = convert_to_gigachat_function(func)
    assert actual_func["few_shot_examples"] == few_shots_expected
