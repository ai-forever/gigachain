<br />
<div align="center">

  <a href="https://github.com/ai-forever/gigachain">
    <img src="static/img/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">🦜️🔗 GigaChain (GigaChat + LangChain)</h1>

  <p align="center">
    Набор решений для разработки LLM-приложений и мультиагентых систем на русском языке с поддержкой GigaChat, LangChain, LangGraph, LangChain4j.
    <br />
    <a href="https://github.com/ai-forever/gigachain/issues">Создать issue</a>
    ·
    <a href="https://developers.sber.ru/docs/ru/gigachat/sdk/overview">Документация GigaChain</a>
  </p>
</div>


![Product Name Screen Shot](/static/img/logo-with-backgroung.png)

---

# О GigaChain

GigaChain – это набор решений для создания приложений с использованием больших языковых моделей (*LLM*). GigaChain охватывает все этапы разработки от прототипирования и исследования, до запуска в эксплуатацию и поддержки.

Для работы вам понадобится [ключ авторизации для доступа к GigaChat API](https://developers.sber.ru/docs/ru/gigachat/quickstart/ind-using-api#poluchenie-avtorizatsionnyh-dannyh).

## LLM-фреймворки

В состав GigaChain входят библиотеки для интеграции с популярными LLM-фреймворками LangChain/LangGraph и LangChain4j.
Они позволяют использовать модели GigaChat со всеми возможностями и инфраструктурой, которую предоставляют фреймворки для разработки комплексных LLM-приложений, использующих RAG, AI-агентов и мультиагентные системы.

Библиотеки доступны на Python, JS/TS и Java.

### Python

[![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain-gigachat?style=flat-round)](https://pypistats.org/packages/langchain-gigachat)
[![GitHub star chart](https://img.shields.io/github/stars/ai-forever/langchain-gigachat?style=flat-round)](https://www.star-history.com/#ai-forever/langchain-gigachat)

Интеграционная библиотека [`langchain-gigachat`](https://github.com/ai-forever/langchain-gigachat) для работы с фреймворками LangChain и LangGraph. 

Начало работы:

* [Быстрый старт](https://github.com/ai-forever/langchain-gigachat);
* [Сборник примеров](/cookbook/README.md).

Смотрите также:

* [Документация LangChain для Python](https://python.langchain.com/docs/introduction/);
* [Документация LangGraph для Python](https://langchain-ai.github.io/langgraph/);
* [Чат-бот по документации LangChain](https://chat.langchain.com).
  
  Исходный код чат-бота (python) — в [репозитории chat-langchain](https://github.com/langchain-ai/chat-langchain).

### JS/TS

![npm](https://img.shields.io/npm/dm/langchain-gigachat)
[![GitHub star chart](https://img.shields.io/github/stars/ai-forever/langchainjs?style=flat-round)](https://www.star-history.com/#ai-forever/langchainjs)



Интеграционная библиотека [`langchain-gigachat`](https://github.com/ai-forever/langchainjs) для работы с JS-версиями фреймворков LangChainJS и LangGraphJS.

Начало работы:

* [Быстрый старт](https://github.com/ai-forever/langchain-gigachat);
* [Сборник примеров](/cookbook/js/README.md).

Смотрите также: 

* [Документация LangChainJS](https://js.langchain.com/docs/introduction/);
* [Документация LangGraphJS](https://langchain-ai.github.io/langgraphjs/);
* Исходный код [чат-бота по документации LangChain на JS](https://github.com/langchain-ai/chat-langchainjs).

### Java

[![GitHub star chart](https://img.shields.io/github/stars/ai-forever/langchain4j-gigachat?style=flat-round)](https://www.star-history.com/#ai-forever/langchain4j-gigachat)

Библиотека [`langchain4j-gigachat`](https://github.com/ai-forever/langchain4j-gigachat) для работы с фреймворком LangChain4j.

Начало работы:

* [Быстрый старт](https://github.com/ai-forever/langchain-gigachat);
* [Сборник примеров](https://github.com/ai-forever/langchain4j-gigachat/tree/main/langchain4j-gigachat-examples).


## SDK для работы с моделями GigaChat

Библиотеки-обертки для работы с [REST API GigaChat](https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/gigachat-api).
Они управляют авторизацией запросов, упрощают отправку сообщений и дают доступ к другим методам API.

SDK доступны на языках:

* Python [![GitHub Downloads (all assets, all releases)](https://img.shields.io/pypi/dm/gigachat?style=flat-square?style=flat-round)](https://pypistats.org/packages/gigachat)
[![GitHub Repo stars](https://img.shields.io/github/stars/ai-forever/gigachat?style=flat-round)](https://star-history.com/#ai-forever/gigachat)

  * [Быстрый старт](https://github.com/ai-forever/gigachat/tree/main?tab=readme-ov-file#о-gigachat);
  * [Примеры](https://github.com/ai-forever/gigachat/tree/main/examples#примеры-работы-с-gigachat).

* JS/TS ![GitHub Downloads (all assets, all releases)](https://img.shields.io/npm/dm/gigachat?style=flat-square?style=flat-round)
[![GitHub Repo stars](https://img.shields.io/github/stars/ai-forever/gigachat-js?style=flat-round)](https://star-history.com/#ai-forever/gigachat-js)

  * [Быстрый старт](https://github.com/ai-forever/gigachat-js?tab=readme-ov-file#gigachat-sdk-typescriptjavascript-%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0);
  * [Примеры](https://github.com/ai-forever/gigachat-java/blob/main/gigachat-java-example/README.md#примеры-работы-с-библиотекой-gigachat).

* Java [![GitHub Repo stars](https://img.shields.io/github/stars/ai-forever/gigachat-java?style=flat-round)](https://star-history.com/#ai-forever/gigachat-java):

  * [Быстрый старт](https://github.com/ai-forever/gigachat-java?tab=readme-ov-file#gigachat-java-sdk);
  * [Примеры](https://github.com/ai-forever/gigachat-js/tree/master/examples#примеры-работы-с-gigachat).

## Утилиты и MCP-сервера

### GPT2GIGA

[![GitHub Downloads (all assets, all releases)](https://img.shields.io/pypi/dm/gpt2giga?style=flat-square?style=flat-round)](https://pypistats.org/packages/gpt2giga)
[![GitHub Repo stars](https://img.shields.io/github/stars/ai-forever/gpt2giga?style=flat-round)](https://star-history.com/#ai-forever/gpt2giga)

[Утилита gpt2giga](https://github.com/ai-forever/gpt2giga) — это прокси-сервер, который перенаправляет запросы, отправленные в OpenAI API, в GigaChat API.

Приложения, проверенные на работу с gpt2giga:

* [Aider](https://aider.chat/) — AI-ассистент для написания приложений. Подробнее о запуске и настройке Aider для работы с gpt2giga — в [README](https://github.com/ai-forever/gpt2giga/tree/main/integrations/aider);
* [n8n](https://n8n.io/) — Платформа для создания nocode-агентов.

### MCP-сервера

Model Context Protocol (или MCP) — открытый протокол, который унифицирует обмен контекстом между приложением и LLM. Другими словами, использование MCP упрощает подключение больших языковых моделей к различным функциям (*инструментам*) и источникам данных.

Подробнее о протоколе — в [официальной документации](https://modelcontextprotocol.io/introduction).

Список MCP-серверов, предоставляющих инструменты для работы с GigaChat и другими сервисами Сбера:

* [Think MCP](https://github.com/ai-forever/think-mcp) — предоставляет инструмент для реализации размышлений («think») при работе с агентами;
* [MCP Giga Checker](https://github.com/ai-forever/mcp_giga_checker) — предоставляет инструмент для проверки переданного текста на наличие содержимого, сгенерированного с помощью нейросетевых моделей.
* [MCP Voice Salute](https://github.com/ai-forever/mcp_voice_salute) — предоставляет инструменты для работы с [API сервиса синтеза и распознавания речи SaluteSpeech](https://developers.sber.ru/docs/ru/salutespeech/overview);
* [MCP Kandinsky](https://github.com/ai-forever/mcp_kandinsky) — предоставляет инструмент для генерации изображений с помощью нейросети Kandinsky.
