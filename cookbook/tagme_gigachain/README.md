# TagMe Trace

## Описание

**TagMe Trace** — это вспомогательная библиотека для отправки диалогов и описаний функций из приложений на базе LangChain (Gigachain) в сервис TagMe. Пакет предоставляет синхронные и асинхронные HTTP‑клиенты, а также удобные декораторы для автоматического логирования вызовов языковых моделей и передачи их в TagMe для разметки и анализа.

## Основные возможности

- Синхронный (`TagmeIntegrationClientSync`) и асинхронный (`TagmeIntegrationClientAsync`) клиенты для REST API TagMe.
- Декораторы `tagme_trace` и `tagme_trace_async` для автоматической отправки диалогов при вызове языковой модели.
- Поддержка произвольных метаданных, которые передаются вместе с диалогом.
- Утилиты для преобразования разных форматов входных данных LangChain в унифицированный формат TagMe.
- Обработка ошибок отсутствующих функций (`MissingFunctionsError`) с возможностью игнорирования.

## Требования

- Python 3.9+
- Установленные зависимости из `requirements.txt`
- Установленный пакет tagme_gigachain: `pip install ./<path_to_repo>/cookbook/tagme_gigachain`
- Действующий токен доступа к TagMe и адрес сервиса.

## Настройка окружения

Перед использованием установите переменные окружения:

- `TAGME_GIGACHAIN_TOKEN` — токен доступа к TagMe. Если значение не задано, его необходимо передать в конструктор клиента.
- `TAGME_GIGACHAIN_BASE_URL` — базовый URL сервиса TagMe (например, `https://tagme.sberdevices.ru/dev/chatwm/plugin_statistics/trace`). Можно переопределить через аргумент `base_url`.

## Быстрый старт: синхронный клиент

```python
from tagme_gigachain import TagmeIntegrationClientSync, FunctionDef

client = TagmeIntegrationClientSync(ignore_missing_functions=False)

functions = [
    FunctionDef(
        name="weather",
        description="Получение прогноза погоды",
        parameters={"type": "object", "properties": {}},
    )
]
client.send_functions(functions)

response = client.send_dialog({"input": [], "metadata": {"custom_meta": {"source": "demo"}}})
print(response)
```

## Асинхронный пример

```python
import asyncio
from tagme_gigachain import TagmeIntegrationClientAsync

async def main():
    async_client = TagmeIntegrationClientAsync(ignore_missing_functions=True)
    await async_client.send_dialog({"input": [], "metadata": {}})
    await async_client.close()

asyncio.run(main())
```

## Использование декораторов

Декораторы помогают перехватывать вызовы языковых моделей и автоматически отправлять диалог в TagMe.

### Асинхронный декоратор

```python
from langchain_core.messages import AIMessage, HumanMessage
from tagme_gigachain import tagme_trace_async

@tagme_trace_async(metadata={"additional_meta": "example"})
async def run_model(messages):
    return AIMessage(content="Ответ", response_metadata={"finish_reason": "stop"})

result = await run_model([HumanMessage(content="Привет")])
```

### Синхронный декоратор

```python
from langchain_core.messages import AIMessage, HumanMessage
from tagme_gigachain import tagme_trace

@tagme_trace(metadata={"additional_meta": "example"})
def run_model_sync(messages):
    return AIMessage(content="Ответ", response_metadata={})

run_model_sync([HumanMessage(content="Привет")])
```

Оба декоратора принимают дополнительные аргументы:

- `token`, `trust_env`, `ssl`, `ignore_missing_functions`, `base_url` — проксируются в соответствующий клиент.
- `tagme_client` — уже созданный экземпляр клиента (полезно для повторного использования).
- `metadata` — пользовательские метаданные.
- `dialog_transform_fc` — функция, преобразующая входные данные в `DialogData`. По умолчанию используется `form_dialog_data` из `tagme_gigachain.utils`.

## Формирование данных диалога

Функция `form_dialog_data(model_input, model_response, metadata)` приводит разнообразные структуры LangChain (`PromptValue`, списки сообщений, строки, словари) к формату, который ожидает TagMe. Возвращается объект `DialogData` с полями:

- `input` — список сообщений с ролями `system`, `user`, `assistant`, `function`.
- `metadata` — словарь с метаданными вопроса, ответа и пользовательскими значениями.

## Обработка ошибок

Если TagMe не знает описание функции, встреченной в диалоге, сервер возвращает ошибку `FUNCTIONS_NOT_FOUND`. Библиотека выбрасывает исключение `MissingFunctionsError` с перечнем отсутствующих функций. Поведение можно контролировать флагом `ignore_missing_functions` в клиентах и декораторах.

## Тестирование

Проект покрыт автотестами на pytest. Чтобы запустить тесты:

```bash
pytest
```

## Примеры

Jupyter Notebook `examples_tagme_gigachain.ipynb`, демонстрирует интеграцию с LangChain и передачу диалогов в TagMe.

## Логирование

Библиотека использует стандартный модуль `logging`. Чтобы увидеть отладочные сообщения, настройте уровень логирования в приложении:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
