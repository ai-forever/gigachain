# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
API_URL_PROMPT_TEMPLATE = """Тебе дана следующая документация API:
{api_docs}
Используя эту документацию, сформируй полный URL API для ответа на вопрос пользователя.
Тебе следует построить URL API так, чтобы получить ответ, который будет как можно короче, но при этом содержать необходимую информацию для ответа на вопрос. Обрати внимание на то, чтобы исключить все ненужные данные в вызове API.

Question:{question}
URL API:"""
=======
API_URL_PROMPT_TEMPLATE = """You are given the below API Documentation:
{api_docs}
Using this documentation, generate the full API url to call for answering the user question.
You should build the API url in order to get a response that is as short as possible, while still getting the necessary information to answer the question. Pay attention to deliberately exclude any unnecessary pieces of data in the API call.

Question:{question}
API url:"""
>>>>>>> langchan/master

API_URL_PROMPT = PromptTemplate(
    input_variables=[
        "api_docs",
        "question",
    ],
    template=API_URL_PROMPT_TEMPLATE,
)

API_RESPONSE_PROMPT_TEMPLATE = (
    API_URL_PROMPT_TEMPLATE
    + """ {api_url}

<<<<<<< HEAD
Вот ответ от API:

{api_response}

Суммируй этот ответ, чтобы ответить на исходный вопрос.

Сумма:"""
=======
Here is the response from the API:

{api_response}

Summarize this response to answer the original question.

Summary:"""
>>>>>>> langchan/master
)

API_RESPONSE_PROMPT = PromptTemplate(
    input_variables=["api_docs", "question", "api_url", "api_response"],
    template=API_RESPONSE_PROMPT_TEMPLATE,
)
