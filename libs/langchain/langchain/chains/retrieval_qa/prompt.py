# flake8: noqa
from langchain_core.prompts import PromptTemplate

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
