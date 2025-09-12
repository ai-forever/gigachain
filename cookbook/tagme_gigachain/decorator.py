import logging
from functools import wraps
from typing import Any, Awaitable, Callable, Optional

from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import BaseMessage

from .client import TagmeIntegrationClientAsync, TagmeIntegrationClientSync
from .types import Metadata, MissingFunctionsError
from .utils import form_dialog_data


def tagme_trace_async(
    *args: Any,
    token: Optional[str] = None,
    metadata: Optional[Metadata] = None,
    tagme_client: Optional[TagmeIntegrationClientAsync] = None,
    **kwargs: Any,
) -> Callable[
    [Callable[[LanguageModelInput], Awaitable[BaseMessage]]],
    Callable[[LanguageModelInput], Awaitable[BaseMessage]],
]:
    if tagme_client is None:
        tagme_client = TagmeIntegrationClientAsync(token, *args, **kwargs)

    def decorator(
        fn: Callable[[LanguageModelInput], Awaitable[BaseMessage]],
    ) -> Callable[[LanguageModelInput], Awaitable[BaseMessage]]:
        @wraps(fn)
        async def wrapper(model_input: LanguageModelInput) -> BaseMessage:
            model_response: BaseMessage = await fn(model_input)

            try:
                data = form_dialog_data(model_input, model_response, metadata)
                await tagme_client.send_dialog(data)
                logging.debug("Диалог успешно отправлен на разметку в TagMe")
            except MissingFunctionsError as e:
                logging.error("Описание некоторых функций не найдены: %s", ", ".join(e.missing))
                raise
            except Exception:  # pylint: disable=broad-except
                pass

            return model_response

        return wrapper

    return decorator


def tagme_trace(
    *args: Any,
    token: Optional[str] = None,
    metadata: Optional[Metadata] = None,
    tagme_client: Optional[TagmeIntegrationClientSync] = None,
    **kwargs: Any,
) -> Callable[
    [Callable[[LanguageModelInput], BaseMessage]],
    Callable[[LanguageModelInput], BaseMessage],
]:
    if tagme_client is None:
        tagme_client = TagmeIntegrationClientSync(token, *args, **kwargs)

    def decorator(
        fn: Callable[[LanguageModelInput], BaseMessage],
    ) -> Callable[[LanguageModelInput], BaseMessage]:
        @wraps(fn)
        def wrapper(model_input: LanguageModelInput) -> BaseMessage:
            model_response: BaseMessage = fn(model_input)

            try:
                data = form_dialog_data(model_input, model_response, metadata)
                tagme_client.send_dialog(data)
                logging.debug("Диалог успешно отправлен на разметку в TagMe")
            except MissingFunctionsError as e:
                logging.error("Описание некоторых функций не найдены: %s", ", ".join(e.missing))
                raise
            except Exception:  # pylint: disable=broad-except
                pass

            return model_response

        return wrapper

    return decorator
