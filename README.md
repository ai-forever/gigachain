[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br />
<div align="center">

  <a href="https://github.com/ai-forever/gigachain">
    <img src="static/img/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">🦜️🔗 GigaChain (GigaChat + LangChain)</h1>

  <p align="center">
    Набор решений для разработки LLM-приложений на русском языке с поддержкой GigaChat
    <br />
    <a href="https://github.com/ai-forever/gigachain/issues">Создать issue</a>
    ·
    <a href="https://developers.sber.ru/docs/ru/gigachat/sdk/overview">Документация GigaChain</a>
  </p>
</div>


![Product Name Screen Shot](/static/img/logo-with-backgroung.png)

---

# О GigaChain

GigaChain – это набор решений для создания приложений с использованием больших языковых моделей (*LLM*).
GigaChain охватывает все этапы разработки от прототипирования и исследования, до запуска в эксплуатацию и поддержки.

В состав GigaChain входят:

* [библиотеки](#создание-агентов-и-разработка-комплексных-llm-приложенийсоз) для создания агентов и разработки комплексных LLM-приложений;
* [SDK](#работа-с-gigachat-api) для работы с моделями GigaChat;
* [утилита](#проксирования-openai-запросов) для проксирования OpenAI-запросов в GigaChat API;

В этом репозитории вы найдете:

* краткое описание всех решений GigaChain;
* инструкции по началу работы([Python](#быстрый-старт-python), [JS/TS](#быстрый-старт-jsts), [Java](#быстрый-старт-java)) с библиотеками для создания агентов и разработки комплексных LLM-приложений;
* ссылки на примеры использования решений.

## Создание агентов и разработка комплексных LLM-приложений

Существуют различные фреймворки и решения, предназначенные для создания агентов и разработки комплексных LLM-приложений, которые используют [работу с функциями](https://developers.sber.ru/docs/ru/gigachat/guides/function-calling) (*инструментами*), реализуют RAG и другие техники.

К таким решениям относятся популярные проекты [LangChain](https://python.langchain.com/docs/introduction/), [LangGraph](https://langchain-ai.github.io/langgraph/) и [LangChain4j](https://docs.langchain4j.dev/).

GigaChain включает интеграционные библиотеки, для работы с этими проектами.

### Партнерские пакеты LangChain для Python и JS/TS

Библиотека `langchain-gigachat` — партнерский пакет популярного open source фреймворка LangChain.
Пакет позволяет использовать все возможности фреймворка и моделей GigaChat, в том числе [создание агентов с помощью LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/). 

Библиотека доступна как для [Python](https://github.com/ai-forever/langchain-gigachat), так и для [JS/TS](https://github.com/ai-forever/langchainjs/tree/main/libs/langchain-gigachat).

**Требования**

Для работы с `langchain-gigachat` вам понадобятся:

* Python версии 3.9 или Node.js версии 16;
* Ключ авторизации для работы с API. О том, как получить ключ авторизации — в [документации GigaChat API](https://developers.sber.ru/docs/ru/gigachat/quickstart/ind-using-api#poluchenie-avtorizatsionnyh-dannyh);
* [Сертификаты НУЦ Минцифры](https://developers.sber.ru/docs/ru/gigachat/certificates).

  Если нужно, вы можете отключить проверку сертификатов. Подробнее — в примерах ниже.

#### Быстрый старт Python

Установите библиотеку с помощью менеджера пакетов pip:

```sh
pip install langchain-gigachat
```

Запустите пример:

```py
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

giga = GigaChat(
    '''
    Ключ авторизации для обмена сообщениями с GigaChat API.
    [Подробнее о получении ключа авторизации](https://developers.sber.ru/docs/ru/gigachat/quickstart/ind-using-api#poluchenie-avtorizatsionnyh-dannyh).
    О других способах авторизации — в [README GigaChat SDK](https://github.com/ai-forever/gigachat#способы-авторизации)
    '''
    credentials="ваш_ключ_авторизации",
    '''
    Необязательный параметр, в котором можно указать версию API. По умолчанию запросы передаются в версию для физических лиц.
    Возможные значения:
    - `GIGACHAT_API_PERS` — версия API для физических лиц;
    - `GIGACHAT_API_B2B` — доступ для ИП и юридических лиц [по предоплате](https://developers.sber.ru/docs/ru/gigachat/api/tariffs#platnye-pakety2);
    - `GIGACHAT_API_CORP` — доступ для ИП и юридических лиц [по схеме pay-as-you-go](https://developers.sber.ru/docs/ru/gigachat/api/tariffs#oplata-pay-as-you-go).
    '''
    scope="GIGACHAT_API_PERS",
    '''
    Необязательный параметр, в котором можно задать [модель GigaChat](https://developers.sber.ru/docs/ru/gigachat/models).
    По умолчанию запросы передаются в модель GigaChat Lite (`model="GigaChat"`).
    '''
    model="GigaChat-2-Max",
    '''
    Необязательный параметр, который включает и отключает [потоковую генерацию токенов](https://developers.sber.ru/docs/ru/gigachat/api/response-token-streaming).
    По умолчанию `False`.
    '''
    streaming=false,
    # Необязательный параметр, с помощью которого можно отключить проверку [сертификатов НУЦ Минцифры](https://developers.sber.ru/docs/ru/gigachat/certificates).
    verify_ssl_certs=False,
)

messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
    )
]

while(True):
    user_input = input("Пользователь: ")
    if user_input == "пока":
      break
    messages.append(HumanMessage(content=user_input))
    res = giga.invoke(messages)
    messages.append(res)
    print("GigaChat: ", res.content)
```

> [!TIP]
> Спросите [чат-бот LangChain](https://chat.langchain.com/), как использовать GigaChat с инструментами фреймворка.
> 
> Исходный код чат-бота — в [репозитории chat-langchain](https://github.com/langchain-ai/chat-langchain).

#### Быстрый старт JS/TS

Установите библиотеку с помощью менеджера пакетов npm:

```sh
npm install --save langchain-gigachat
```

Запустите пример:

```js
import { Agent } from 'node:https';
import { GigaChat } from "langchain-gigachat"
import { HumanMessage, SystemMessage } from "@langchain/core/messages";

const httpsAgent = new Agent({
    // Отключение проверки сертификатов НУЦ Минцифры.
    rejectUnauthorized: false,
});

const giga = new GigaChat({
    /**
     * Ключ авторизации для обмена сообщениями с GigaChat API.
     * [Подробнее о получении ключа авторизации](https://developers.sber.ru/docs/ru/gigachat/quickstart/ind-using-api#poluchenie-avtorizatsionnyh-dannyh).
     * О других способах авторизации — в [README GigaChat SDK](https://github.com/ai-forever/gigachat-js#способы-авторизации)
     */
    credentials: 'ключ_авторизации',
    /**
     * Необязательный параметр, в котором можно указать версию API. По умолчанию запросы передаются в версию для физических лиц.
     * Возможные значения:
     * - `GIGACHAT_API_PERS` — версия API для физических лиц;
     * - `GIGACHAT_API_B2B` — доступ для ИП и юридических лиц [по предоплате](https://developers.sber.ru/docs/ru/gigachat/api/tariffs#platnye-pakety2);
     * - `GIGACHAT_API_CORP` — доступ для ИП и юридических лиц [по схеме pay-as-you-go](https://developers.sber.ru/docs/ru/gigachat/api/tariffs#oplata-pay-as-you-go).
     */
    scope: 'GIGACHAT_API_PERS',
    /**
     * Необязательный параметр, в котором можно задать [модель GigaChat](https://developers.sber.ru/docs/ru/gigachat/models).
     * По умолчанию запросы передаются в модель GigaChat Lite (`model="GigaChat"`).
     */
    model: 'GigaChat-2-Max',
    /**
     * Необязательный параметр, который позволяет задать настройки HTTPS. Эти настройки будут использованы при подключении к серверу API.
     * Вы можете использовать их для отключения проверки [сертификатов НУЦ Минцифры](/https://developers.sber.ru/docs/ru/gigachat/certificates).
     */
    httpsAgent
})

const messages = [
    new SystemMessage("Переведи следующее сообщение на английский"),
    new HumanMessage("Привет!"),
];

const resp = await giga.invoke(messages);

console.log(resp.content);
```

### Интеграционная Java-библиотека для LangChain4j

[Java-библиотека `langchain4j-gigachat`](https://github.com/ai-forever/langchain4j-gigachat) интегрирует модели GigaChat c проектом LangChain4j.

**Требования**

Для работы библиотеки используйте Java версии 17 или выше.

#### Быстрый старт Java

Подключите библиотеку в зависимости своего проекта.

**Gradle**

```kotlin
implementation("chat.giga:langchain4j-gigachat:0.1.4")
```

**Maven**

```xml
<dependency>
    <groupId>chat.giga</groupId>
    <artifactId>langchain4j-gigachat</artifactId>
    <version>0.1.4</version>
</dependency>
```

Запустите пример:

```java
GigaChatChatModel model = GigaChatChatModel.builder()
        .defaultChatRequestParameters(GigaChatChatRequestParameters.builder()
                .modelName(ModelName.GIGA_CHAT_PRO)
                .build())
        .authClient(AuthClient.builder()
                .withOAuth(AuthClientBuilder.OAuthBuilder.builder()
                        .scope(Scope.GIGACHAT_API_PERS)
                        .authKey("<ключ_авторизации>")
                        .build())
                .build())
        .logRequests(true)
        .logResponses(true)
        .build();
```

Подробнее о способах аутентификации — в [README GigaChat SDK](https://github.com/ai-forever/gigachat-java#способы-аутентификации).

## Работа с GigaChat API

В состав GigaChain входят библиотеки SDK, которые представляют собой обертку для [REST API GigaChat](https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/gigachat-api).
Они управляют авторизацией запросов, упрощают отправку сообщений и дают доступ к другим методам API.
Репозиторий каждого SDK содержит инструкцию по началу работы с библиотекой, а также папку с базовыми примерами работы.

SDK доступны на языках программирования:

* [Python](https://github.com/ai-forever/gigachat);

  Примеры работы с SDK в папке [examples](https://github.com/ai-forever/gigachat/blob/main/examples/README.md).

* [JS/TS](https://github.com/ai-forever/gigachat-js);

  Примеры работы с SDK в папке [examples](https://github.com/ai-forever/gigachat-js/blob/master/examples/README.md).

* [Java](https://github.com/ai-forever/gigachat-java).

  Примеры работы с SDK в папке [gigachat-java-example](https://github.com/ai-forever/gigachat-java/blob/main/gigachat-java-example/README.md).

## Проксирование OpenAI-запросов

[Утилита gpt2giga](https://github.com/ai-forever/gpt2giga) — это прокси-сервер, который перенаправляет запросы, отправленные в OpenAI API, в GigaChat API.

Приложения, проверенные на работу с gpt2giga:

* [Aider](https://aider.chat/) — AI-ассистент для написания приложений. Подробнее о запуске и настройке Aider для работы с gpt2giga — в [README](https://github.com/ai-forever/gpt2giga/tree/main/integrations/aider);
* [n8n](https://n8n.io/) — Платформа для создания nocode-агентов.

## Примеры

Примеры демонстрируют как использовать решения GigaChain для разработки агентов, создания RAG, работы с MCP-серверами и решения других задач:

* [Python](/cookbook/README.md);
* [JS/TS](/cookbook/js/README.md);
* [Java](https://github.com/ai-forever/langchain4j-gigachat/tree/main/langchain4j-gigachat-examples).

## Смотрите также

* Документация GigaChat API:
  * [Быстрый страт для физических лиц](https://developers.sber.ru/docs/ru/gigachat/individuals-quickstart);
  * [Быстрый страт для ИП и юридических лиц](https://developers.sber.ru/docs/ru/gigachat/legal-quickstart);
* Документация LangChain:
    * [для Python](https://python.langchain.com/docs/introduction/);
    * [для JS/TS](https://js.langchain.com/docs/introduction/?ref=blog.apify.com);
* Документация LangGraph:
  * [для Python](https://langchain-ai.github.io/langgraph/)
  * [для JS/TS](https://langchain-ai.github.io/langgraphjs/)
* [Документация LangChain4j](https://docs.langchain4j.dev/intro).