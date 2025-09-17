"""Decorators that trace LangChain model calls and forward them to TagMe."""

import logging
from functools import wraps
from typing import Any, Awaitable, Callable, Optional

from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import BaseMessage

from .client import TagmeIntegrationClientAsync, TagmeIntegrationClientSync
from .entities import DialogData, DialogTransformFunction, Metadata, MissingFunctionsError
from .utils import form_dialog_data

logger = logging.getLogger(__name__)


def tagme_trace_async(
    *args: Any,
    token: Optional[str] = None,
    metadata: Optional[Metadata] = None,
    tagme_client: Optional[TagmeIntegrationClientAsync] = None,
    dialog_transform_fc: DialogTransformFunction = form_dialog_data,
    **kwargs: Any,
) -> Callable[
    [Callable[[LanguageModelInput], Awaitable[BaseMessage]]],
    Callable[[LanguageModelInput], Awaitable[BaseMessage]],
]:
    """Wrap an async LangChain call and push dialog data to TagMe.

    Args:
        *args (Any): Positional arguments forwarded to the async client constructor.
        token (Optional[str]): Explicit API token if not loaded from the environment.
        metadata (Optional[Metadata]): Custom metadata merged into the TagMe payload.
        tagme_client (Optional[TagmeIntegrationClientAsync]): Pre-configured client instance override.
        dialog_transform_fc (DialogTransformFunction): Callable that prepares a ``DialogData`` structure.
        **kwargs (Any): Keyword arguments forwarded to the async client constructor.
    """

    if tagme_client is None:
        tagme_client = TagmeIntegrationClientAsync(token, *args, **kwargs)

    def decorator(
        fn: Callable[[LanguageModelInput], Awaitable[BaseMessage]],
    ) -> Callable[[LanguageModelInput], Awaitable[BaseMessage]]:
        @wraps(fn)
        async def wrapper(model_input: LanguageModelInput) -> BaseMessage:
            model_response: BaseMessage = await fn(model_input)

            try:
                data: DialogData = dialog_transform_fc(model_input, model_response, metadata)
                await tagme_client.send_dialog(data)
                logger.debug("Dialog successfully submitted to TagMe for annotation")
            except MissingFunctionsError as e:
                logger.error("Descriptions for some functions are missing: %s", ", ".join(e.missing))
                raise

            return model_response

        return wrapper

    return decorator


def tagme_trace(
    *args: Any,
    token: Optional[str] = None,
    metadata: Optional[Metadata] = None,
    tagme_client: Optional[TagmeIntegrationClientSync] = None,
    dialog_transform_fc: DialogTransformFunction = form_dialog_data,
    **kwargs: Any,
) -> Callable[
    [Callable[[LanguageModelInput], BaseMessage]],
    Callable[[LanguageModelInput], BaseMessage],
]:
    """Wrap a sync LangChain call and push dialog data to TagMe.

    Args:
        *args (Any): Positional arguments forwarded to the sync client constructor.
        token (Optional[str]): Explicit API token if not loaded from the environment.
        metadata (Optional[Metadata]): Custom metadata merged into the TagMe payload.
        tagme_client (Optional[TagmeIntegrationClientSync]): Pre-configured client instance override.
        dialog_transform_fc (DialogTransformFunction): Callable that prepares a ``DialogData`` structure.
        **kwargs (Any): Keyword arguments forwarded to the sync client constructor.
    """

    if tagme_client is None:
        tagme_client = TagmeIntegrationClientSync(token, *args, **kwargs)

    def decorator(
        fn: Callable[[LanguageModelInput], BaseMessage],
    ) -> Callable[[LanguageModelInput], BaseMessage]:
        @wraps(fn)
        def wrapper(model_input: LanguageModelInput) -> BaseMessage:
            model_response: BaseMessage = fn(model_input)

            try:
                data: DialogData = dialog_transform_fc(model_input, model_response, metadata)
                tagme_client.send_dialog(data)
                logger.debug("Dialog successfully submitted to TagMe for annotation")
            except MissingFunctionsError as e:
                logger.error("Descriptions for some functions are missing: %s", ", ".join(e.missing))
                raise

            return model_response

        return wrapper

    return decorator
