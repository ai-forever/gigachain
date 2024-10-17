import copy
from types import GenericAlias
from typing import Any, Dict, List, Type, Union

from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import BaseGenerationOutputParser
from langchain_core.outputs import ChatGeneration, Generation
from pydantic import BaseModel, model_validator


class OutputFunctionsParser(BaseGenerationOutputParser[Any]):
    """Parse an output that is one of sets of values."""

    args_only: bool = True
    """Whether to only return the arguments to the function call."""

    def parse_result(self, result: List[Generation], *, partial: bool = False) -> Any:
        generation = result[0]
        if not isinstance(generation, ChatGeneration):
            raise OutputParserException(
                "This output parser can only be used with a chat generation."
            )
        message = generation.message
        try:
            func_call = copy.deepcopy(message.additional_kwargs["function_call"])
        except KeyError as exc:
            raise OutputParserException(
                f"Could not parse function call: {exc}"
            ) from exc

        if self.args_only:
            return func_call["arguments"]
        return func_call


class PydanticOutputFunctionsParser(OutputFunctionsParser):
    """Parse an output as a pydantic object."""

    pydantic_schema: Union[Type[BaseModel], Dict[str, Type[BaseModel]]]
    """The pydantic schema to parse the output with.

    If multiple schemas are provided, then the function name will be used to
    determine which schema to use.
    """

    @model_validator(mode="before")
    @classmethod
    def validate_schema(cls, values: dict) -> Any:
        """Validate the pydantic schema.

        Args:
            values: The values to validate.

        Returns:
            The validated values.

        Raises:
            ValueError: If the schema is not a pydantic schema.
        """
        schema = values["pydantic_schema"]
        if "args_only" not in values:
            values["args_only"] = (
                isinstance(schema, type)
                and not isinstance(schema, GenericAlias)
                and issubclass(schema, BaseModel)
            )
        elif values["args_only"] and isinstance(schema, dict):
            msg = (
                "If multiple pydantic schemas are provided then args_only should be"
                " False."
            )
            raise ValueError(msg)
        return values

    def parse_result(self, result: list[Generation], *, partial: bool = False) -> Any:
        """Parse the result of an LLM call to a JSON object.

        Args:
            result: The result of the LLM call.
            partial: Whether to parse partial JSON objects. Default is False.

        Returns:
            The parsed JSON object.
        """
        _result = super().parse_result(result)
        if self.args_only:
            if hasattr(self.pydantic_schema, "model_validate"):
                pydantic_args = self.pydantic_schema.model_validate(_result)
            else:
                pydantic_args = self.pydantic_schema.parse_obj(_result)  # type: ignore
        else:
            fn_name = _result["name"]
            _args = _result["arguments"]
            if isinstance(self.pydantic_schema, dict):
                pydantic_schema = self.pydantic_schema[fn_name]
            else:
                pydantic_schema = self.pydantic_schema
            if hasattr(pydantic_schema, "model_validate"):
                pydantic_args = pydantic_schema.model_validate(_args)  # type: ignore
            else:
                pydantic_args = pydantic_schema.parse_obj(_args)  # type: ignore
        return pydantic_args


class PydanticAttrOutputFunctionsParser(PydanticOutputFunctionsParser):
    """Parse an output as an attribute of a pydantic object."""

    attr_name: str
    """The name of the attribute to return."""

    def parse_result(self, result: List[Generation], *, partial: bool = False) -> Any:
        result = super().parse_result(result)
        return getattr(result, self.attr_name)
