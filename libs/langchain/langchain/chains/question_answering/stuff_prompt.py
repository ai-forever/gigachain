# flake8: noqa
from langchain.chains.prompt_selector import ConditionalPromptSelector, is_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

<<<<<<< HEAD
prompt_template = """Используй следующие части контекста, чтобы ответить на вопрос в конце. Если ты не знаешь ответа, просто скажи, что не знаешь, не пытайся придумать ответ.
=======
prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
>>>>>>> langchan/master

{context}

Question: {question}
<<<<<<< HEAD
Полезный ответ:"""
=======
Helpful Answer:"""
>>>>>>> langchan/master
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

<<<<<<< HEAD
system_template = """Используй следующие части контекста, чтобы ответить на вопрос пользователя. 
Если ты не знаешь ответа, просто скажи, что не знаешь, не пытайся придумать ответ.
=======
system_template = """Use the following pieces of context to answer the user's question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
>>>>>>> langchan/master
----------------
{context}"""
messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}"),
]
CHAT_PROMPT = ChatPromptTemplate.from_messages(messages)


PROMPT_SELECTOR = ConditionalPromptSelector(
    default_prompt=PROMPT, conditionals=[(is_chat_model, CHAT_PROMPT)]
)
