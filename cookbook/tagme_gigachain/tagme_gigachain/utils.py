"""Utility helpers for reshaping LangChain data structures for TagMe."""

from typing import Dict, List, Optional, Union

from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_core.prompt_values import PromptValue

from tagme_gigachain.entities import ChatMessage, DialogData, RoleType

Metadata = Dict[str, Union[str, int, float, dict, list, None]]


def _role_of(msg: BaseMessage) -> RoleType:
    """Return the TagMe role label that corresponds to a LangChain message."""

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

    input_arr = [ChatMessage(role=_role_of(m), content=str(m.content)) for m in msgs]
    input_arr.append(ChatMessage(role="assistant", content=str(model_response.content)))

    question_meta: Dict = {}
    for m in msgs:
        meta = getattr(m, "response_metadata", None)
        if isinstance(meta, dict):
            question_meta.update(meta)

    response_meta = getattr(model_response, "response_metadata", {})
    response_meta.update(getattr(model_response, "usage_metadata", {}))

    dialog_metadata: Dict[str, Union[str, Metadata]] = {
        "question": question_meta,
        "response": response_meta,
    }
    if metadata:
        dialog_metadata["custom_meta"] = metadata

    return DialogData(input=input_arr, metadata=dialog_metadata)
