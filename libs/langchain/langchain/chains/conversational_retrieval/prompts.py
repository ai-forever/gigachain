# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
_template = """Посмотри на историю чата:
{chat_history}
Пользователь задал вопрос {question}
Перепиши вопрос пользователя, заменив в нем местоимения на значения из контекста. Если в вопросе ничего не нужно менять, то просто перепиши его."""  # noqa: E501
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

prompt_template = """Используй следующие части контекста, чтобы ответить на вопрос в конце. Если ты не знаешь ответа, просто скажи, что не знаешь, не пытайся придумать ответ.
=======
_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
>>>>>>> langchan/master

{context}

Question: {question}
<<<<<<< HEAD
Полезный ответ:"""  # noqa: E501
=======
Helpful Answer:"""
>>>>>>> langchan/master
QA_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
