# flake8: noqa
from langchain.chains.prompt_selector import ConditionalPromptSelector, is_chat_model
from langchain_core.prompts.chat import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.prompts.prompt import PromptTemplate

DEFAULT_REFINE_PROMPT_TMPL = (
<<<<<<< HEAD
    "Оригинальный вопрос звучит так: {question}\n"
    "Мы предоставили существующий ответ: {existing_answer}\n"
    "У нас есть возможность уточнить существующий ответ"
    "(если это необходимо) с некоторым дополнительным контекстом ниже.\n"
    "------------\n"
    "{context_str}\n"
    "------------\n"
    "Учитывая новый контекст, уточни оригинальный ответ, чтобы лучше "
    "ответить на вопрос. "
    "Если контекст не полезен, верни оригинальный ответ."
=======
    "The original question is as follows: {question}\n"
    "We have provided an existing answer: {existing_answer}\n"
    "We have the opportunity to refine the existing answer "
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{context_str}\n"
    "------------\n"
    "Given the new context, refine the original answer to better "
    "answer the question. "
    "If the context isn't useful, return the original answer."
>>>>>>> langchan/master
)
DEFAULT_REFINE_PROMPT = PromptTemplate.from_template(DEFAULT_REFINE_PROMPT_TMPL)

refine_template = (
<<<<<<< HEAD
    "У нас есть возможность уточнить существующий ответ"
    "(если это необходимо) с некоторым дополнительным контекстом ниже.\n"
    "------------\n"
    "{context_str}\n"
    "------------\n"
    "Учитывая новый контекст, уточни оригинальный ответ, чтобы лучше "
    "ответить на вопрос. "
    "Если контекст не полезен, верни оригинальный ответ."
=======
    "We have the opportunity to refine the existing answer "
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{context_str}\n"
    "------------\n"
    "Given the new context, refine the original answer to better "
    "answer the question. "
    "If the context isn't useful, return the original answer."
>>>>>>> langchan/master
)
CHAT_REFINE_PROMPT = ChatPromptTemplate.from_messages(
    [("human", "{question}"), ("ai", "{existing_answer}"), ("human", refine_template)]
)
REFINE_PROMPT_SELECTOR = ConditionalPromptSelector(
    default_prompt=DEFAULT_REFINE_PROMPT,
    conditionals=[(is_chat_model, CHAT_REFINE_PROMPT)],
)


DEFAULT_TEXT_QA_PROMPT_TMPL = (
<<<<<<< HEAD
    "Информация контекста ниже. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Учитывая информацию контекста и отсутствие предварительных знаний, "
    "ответь на вопрос: {question}\n"
=======
    "Context information is below. \n"
    "------------\n"
    "{context_str}\n"
    "------------\n"
    "Given the context information and not prior knowledge, "
    "answer the question: {question}\n"
>>>>>>> langchan/master
)
DEFAULT_TEXT_QA_PROMPT = PromptTemplate.from_template(DEFAULT_TEXT_QA_PROMPT_TMPL)

chat_qa_prompt_template = (
<<<<<<< HEAD
    "Информация контекста ниже. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Учитывая информацию контекста и отсутствие предварительных знаний, "
    "ответь на любые вопросы"
=======
    "Context information is below.\n"
    "------------\n"
    "{context_str}\n"
    "------------\n"
    "Given the context information and not prior knowledge, "
    "answer any questions"
>>>>>>> langchan/master
)
CHAT_QUESTION_PROMPT = ChatPromptTemplate.from_messages(
    [("system", chat_qa_prompt_template), ("human", "{question}")]
)
QUESTION_PROMPT_SELECTOR = ConditionalPromptSelector(
    default_prompt=DEFAULT_TEXT_QA_PROMPT,
    conditionals=[(is_chat_model, CHAT_QUESTION_PROMPT)],
)
