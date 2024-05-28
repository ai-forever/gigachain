# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

_CREATE_DRAFT_ANSWER_TEMPLATE = """{question}\n\n"""
CREATE_DRAFT_ANSWER_PROMPT = PromptTemplate(
    input_variables=["question"], template=_CREATE_DRAFT_ANSWER_TEMPLATE
)

<<<<<<< HEAD
_LIST_ASSERTIONS_TEMPLATE = """Вот утверждение:
{statement}
Составь список предположений, которые ты сделал, формулируя вышеуказанное утверждение.\n\n"""
=======
_LIST_ASSERTIONS_TEMPLATE = """Here is a statement:
{statement}
Make a bullet point list of the assumptions you made when producing the above statement.\n\n"""
>>>>>>> langchan/master
LIST_ASSERTIONS_PROMPT = PromptTemplate(
    input_variables=["statement"], template=_LIST_ASSERTIONS_TEMPLATE
)

<<<<<<< HEAD
_CHECK_ASSERTIONS_TEMPLATE = """Вот список утверждений:
{assertions}
Для каждого утверждения определи, верно оно или нет. Если оно неверно, объясни почему.\n\n"""
=======
_CHECK_ASSERTIONS_TEMPLATE = """Here is a bullet point list of assertions:
{assertions}
For each assertion, determine whether it is true or false. If it is false, explain why.\n\n"""
>>>>>>> langchan/master
CHECK_ASSERTIONS_PROMPT = PromptTemplate(
    input_variables=["assertions"], template=_CHECK_ASSERTIONS_TEMPLATE
)

_REVISED_ANSWER_TEMPLATE = """{checked_assertions}

<<<<<<< HEAD
Question: Учитывая вышеуказанные утверждения и проверки, как бы ты ответил на вопрос '{question}'?

Ответ:"""
=======
Question: In light of the above assertions and checks, how would you answer the question '{question}'?

Answer:"""
>>>>>>> langchan/master
REVISED_ANSWER_PROMPT = PromptTemplate(
    input_variables=["checked_assertions", "question"],
    template=_REVISED_ANSWER_TEMPLATE,
)
