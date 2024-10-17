# mypy: disable-error-code="annotation-unchecked"
from typing import Annotated as ExtensionsAnnotated
from typing import Any, Callable, Literal, Optional, Union

import pytest
from pydantic import BaseModel as BaseModelV2Maybe  #  pydantic: ignore
from pydantic import Field as FieldV2Maybe  #  pydantic: ignore
from typing_extensions import TypedDict as ExtensionsTypedDict

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

        arg1: int = Field(..., description="foo")
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'")

    return dummy_function


@pytest.fixture()
def annotated_function() -> Callable:
    def dummy_function(
        arg1: ExtensionsAnnotated[int, "foo"],
        arg2: ExtensionsAnnotated[Literal["bar", "baz"], "one of 'bar', 'baz'"],
    ) -> None:
        """dummy function"""

    return dummy_function


@pytest.fixture()
def function() -> Callable:
    def dummy_function(arg1: int, arg2: Literal["bar", "baz"]) -> None:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """

    return dummy_function


@pytest.fixture()
def runnable() -> Runnable:
    class Args(ExtensionsTypedDict):
        arg1: ExtensionsAnnotated[int, "foo"]
        arg2: ExtensionsAnnotated[Literal["bar", "baz"], "one of 'bar', 'baz'"]

    def dummy_function(input_dict: Args) -> None:
        pass

    return RunnableLambda(dummy_function)


@pytest.fixture()
def dummy_tool() -> BaseTool:
    class Schema(BaseModel):
        arg1: int = Field(..., description="foo")
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
        arg1: int = Field(..., description="foo")
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

        arg1: int = Field(..., description="foo")
        arg2: Literal["bar", "baz"] = Field(..., description="one of 'bar', 'baz'")

    return dummy_function


@pytest.fixture()
def dummy_pydantic_v2() -> type[BaseModelV2Maybe]:
    class dummy_function(BaseModelV2Maybe):  # noqa: N801
        """dummy function"""

        arg1: int = FieldV2Maybe(..., description="foo")
        arg2: Literal["bar", "baz"] = FieldV2Maybe(
            ..., description="one of 'bar', 'baz'"
        )

    return dummy_function


@pytest.fixture()
def json_schema() -> dict:
    return {
        "title": "dummy_function",
        "description": "dummy function",
        "return_parameters": None,
        "few_shot_examples": None,
        "properties": {
            "description": "dummy function",
            "arg1": {"description": "foo", "type": "integer"},
            "arg2": {
                "description": "one of 'bar', 'baz'",
                "enum": ["bar", "baz"],
                "type": "string",
            },
        },
        "required": ["arg1", "arg2"],
    }


class Dummy:
    def dummy_function(self, arg1: int, arg2: Literal["bar", "baz"]) -> None:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """


class DummyWithClassMethod:
    @classmethod
    def dummy_function(cls, arg1: int, arg2: Literal["bar", "baz"]) -> None:
        """dummy function

        Args:
            arg1: foo
            arg2: one of 'bar', 'baz'
        """


def test_convert_to_gigachat_function(
    pydantic: type[BaseModel],
    function: Callable,
    dummy_structured_tool: StructuredTool,
    dummy_tool: BaseTool,
    json_schema: dict,
    annotated_function: Callable,
    dummy_pydantic: type[BaseModel],
    runnable: Runnable,
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
            "required": ["arg1", "arg2"],
        },
    }

    for fn in (
        pydantic,
        function,
        dummy_structured_tool,
        dummy_tool,
        expected,
        Dummy.dummy_function,
        DummyWithClassMethod.dummy_function,
        annotated_function,
        dummy_pydantic,
    ):
        actual = convert_to_gigachat_function(fn)  # type: ignore
        assert actual == expected

    # Test runnables
    actual = convert_to_gigachat_function(
        runnable.as_tool(description="dummy function")
    )
    parameters = {
        "type": "object",
        "description": "dummy function",
        "properties": {
            "arg1": {"type": "integer", "description": ""},
            "arg2": {"enum": ["bar", "baz"], "type": "string", "description": ""},
        },
        "required": ["arg1", "arg2"],
    }
    runnable_expected = expected.copy()
    runnable_expected["parameters"] = parameters
    assert actual == runnable_expected

    # Test simple Tool
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


def test_convert_to_openai_function_no_args() -> None:
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
