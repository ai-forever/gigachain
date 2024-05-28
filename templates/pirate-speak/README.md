<<<<<<< HEAD
# pirate-speak

Этот шаблон преобразует пользовательский ввод в пиратский жаргон.

## Настройка среды

Установите переменную среды `OPENAI_API_KEY` для доступа к моделям OpenAI.

## Использование

Чтобы использовать этот пакет, у вас должен быть установлен CLI для GigaChain:

```shell
pip install -U gigachain-cli
```

Чтобы создать новый проект GigaChain и установить этот пакет как единственный, вы можете сделать следующее:

```shell
gigachain app new my-app --package pirate-speak
```

Если вы хотите добавить это в существующий проект, просто выполните:

```shell
gigachain app add pirate-speak
```

И добавьте следующий код в файл `server.py`:
=======

# pirate-speak

This template converts user input into pirate speak.

## Environment Setup

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

## Usage

To use this package, you should first have the LangChain CLI installed:

```shell
pip install -U langchain-cli
```

To create a new LangChain project and install this as the only package, you can do:

```shell
langchain app new my-app --package pirate-speak
```

If you want to add this to an existing project, you can just run:

```shell
langchain app add pirate-speak
```

And add the following code to your `server.py` file:
>>>>>>> langchan/master
```python
from pirate_speak.chain import chain as pirate_speak_chain

add_routes(app, pirate_speak_chain, path="/pirate-speak")
```

<<<<<<< HEAD
(Необязательно) Давайте теперь настроим LangSmith.
LangSmith поможет нам отслеживать, мониторить и отлаживать приложения GigaChain.
LangSmith сейчас находится в частном бета-тестировании, вы можете зарегистрироваться [здесь](https://smith.langchain.com/).
Если у вас нет доступа, вы можете пропустить этот раздел.

```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<ваш-api-ключ>
export LANGCHAIN_PROJECT=<ваш-проект>  # если не указано, по умолчанию используется "default"
```

Если вы находитесь в этой директории, то вы можете напрямую запустить экземпляр GigaServe с помощью:

```shell
gigachain serve
```

Это запустит приложение FastAPI, и сервер будет работать локально по адресу 
[http://localhost:8000](http://localhost:8000)

Мы можем увидеть все шаблоны по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Мы можем получить доступ к площадке для игр по адресу [http://127.0.0.1:8000/pirate-speak/playground](http://127.0.0.1:8000/pirate-speak/playground)  

Мы можем получить доступ к шаблону из кода с помощью:

```python
from gigaserve.client import RemoteRunnable
=======
(Optional) Let's now configure LangSmith. 
LangSmith will help us trace, monitor and debug LangChain applications. 
You can sign up for LangSmith [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

If you are inside this directory, then you can spin up a LangServe instance directly by:

```shell
langchain serve
```

This will start the FastAPI app with a server is running locally at 
[http://localhost:8000](http://localhost:8000)

We can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
We can access the playground at [http://127.0.0.1:8000/pirate-speak/playground](http://127.0.0.1:8000/pirate-speak/playground)  

We can access the template from code with:

```python
from langserve.client import RemoteRunnable
>>>>>>> langchan/master

runnable = RemoteRunnable("http://localhost:8000/pirate-speak")
```
