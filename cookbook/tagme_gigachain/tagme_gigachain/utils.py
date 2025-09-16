"""Utility helpers for reshaping LangChain data structures for TagMe."""

import json
from typing import Any, Dict, List, Optional, Union

from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    FunctionMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)
from langchain_core.prompt_values import PromptValue

from .entities import (
    ChatMessage,
    DialogData,
    FunctionCall,
    FunctionResult,
    RoleType,
)

Metadata = Dict[str, Union[str, int, float, dict, list, None]]

ROLE_ALIASES: Dict[str, RoleType] = {
    "human": "user",
    "ai": "assistant",
    "system": "system",
    "function": "function",
    "tool": "function",
}


def _role_of(msg: BaseMessage) -> RoleType:
    """Return the TagMe role label that corresponds to a LangChain message."""

    msg_type = getattr(msg, "type", None)
    if msg_type:
        return ROLE_ALIASES.get(msg_type, msg_type)  # type: ignore
    if isinstance(msg, HumanMessage):
        return "user"
    if isinstance(msg, AIMessage):
        return "assistant"
    if isinstance(msg, SystemMessage):
        return "system"
    return "user"


def _collect_messages(model_input: LanguageModelInput) -> List[BaseMessage]:
    """Normalize different LangChain input types into a flat list of messages."""

    if isinstance(model_input, PromptValue):
        return model_input.to_messages()
    if isinstance(model_input, BaseMessage):
        return [model_input]
    if isinstance(model_input, (list, tuple)):
        out: List[BaseMessage] = []
        for m in model_input:
            if isinstance(m, BaseMessage):
                out.append(m)
            else:
                out.append(HumanMessage(content=str(m)))
        return out
    if isinstance(model_input, dict):
        msgs = model_input.get("messages")
        if isinstance(msgs, (list, tuple)):
            return [m if isinstance(m, BaseMessage) else HumanMessage(content=str(m)) for m in msgs]
        return [HumanMessage(content=str(model_input))]
    if isinstance(model_input, str):
        return [HumanMessage(content=model_input)]
    return [HumanMessage(content=str(model_input))]


def form_dialog_data(
    model_input: LanguageModelInput,
    model_response: BaseMessage,
    metadata: Optional[Metadata],
) -> DialogData:
    """Create a TagMe payload describing the conversation and metadata."""

    msgs = _collect_messages(model_input)

    input_arr = [_to_chat_message(m) for m in msgs]
    input_arr.append(_to_chat_message(model_response))

    question_meta: Dict[str, Any] = {}
    for m in msgs:
        meta = getattr(m, "response_metadata", None)
        if isinstance(meta, dict):
            question_meta.update(meta)

    response_meta: Dict[str, Any] = {}
    raw_response_meta = getattr(model_response, "response_metadata", None)
    if isinstance(raw_response_meta, dict):
        response_meta.update(raw_response_meta)
    usage_meta = getattr(model_response, "usage_metadata", None)
    if isinstance(usage_meta, dict):
        response_meta.setdefault("usage_metadata", usage_meta)

    dialog_metadata: Dict[str, Union[str, Metadata]] = {
        "question": question_meta,
        "response": response_meta,
    }
    if metadata:
        dialog_metadata["custom_meta"] = metadata

    return DialogData(input=input_arr, metadata=dialog_metadata)


def _to_chat_message(msg: BaseMessage) -> ChatMessage:
    """Convert a LangChain message into the simplified ChatMessage form."""

    content = _stringify_content(getattr(msg, "content", ""))
    function_call = _extract_function_call(msg)
    function_result = _extract_function_result(msg)

    return ChatMessage(
        role=_role_of(msg),
        content=content,
        function_call=function_call,
        function_result=function_result,
    )


def _stringify_content(content: Any) -> str:
    """Convert message content to a string representation."""

    if isinstance(content, str):
        return content
    return str(content)


def _extract_function_call(msg: BaseMessage) -> Optional[FunctionCall]:
    """Pull a function call definition from AI messages when available."""

    additional_kwargs = getattr(msg, "additional_kwargs", {}) or {}
    call_payload = additional_kwargs.get("function_call")
    if isinstance(call_payload, dict):
        return FunctionCall(
            name=str(call_payload.get("name", "")),
            arguments=_coerce_arguments(call_payload.get("arguments")),
        )

    tool_calls = getattr(msg, "tool_calls", None)
    if isinstance(tool_calls, list) and tool_calls:
        tool_call = tool_calls[0]
        if isinstance(tool_call, dict):
            return FunctionCall(
                name=str(tool_call.get("name", "")),
                arguments=_coerce_arguments(tool_call.get("args")),
            )
    return None


def _extract_function_result(msg: BaseMessage) -> Optional[FunctionResult]:
    """Pull a function result payload from tool or function messages."""

    if isinstance(msg, FunctionMessage):
        return FunctionResult(
            name=str(getattr(msg, "name", "")),
            result=_ensure_dict_like(getattr(msg, "content", "")),
        )
    if isinstance(msg, ToolMessage):
        return FunctionResult(
            name=str(getattr(msg, "tool_call_id", "")),
            result=_ensure_dict_like(getattr(msg, "content", "")),
        )
    return None


def _coerce_arguments(raw_args: Any) -> Dict[str, Any]:
    """Normalize function call arguments into a dictionary."""

    if isinstance(raw_args, dict):
        return raw_args
    if isinstance(raw_args, str):
        try:
            parsed = json.loads(raw_args)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            pass
        return {"value": raw_args}
    return {"value": raw_args}


def _ensure_dict_like(value: Any) -> Dict[str, Any]:
    """Convert content payloads into a dictionary form when possible."""

    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            parsed = None
        if isinstance(parsed, dict):
            return parsed
        return {"content": value}
    return {"content": value}
