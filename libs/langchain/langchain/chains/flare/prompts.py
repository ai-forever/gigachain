from typing import Tuple

from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import PromptTemplate


class FinishedOutputParser(BaseOutputParser[Tuple[str, bool]]):
    """Output parser that checks if the output is finished."""

    finished_value: str = "FINISHED"
    """Value that indicates the output is finished."""

    def parse(self, text: str) -> Tuple[str, bool]:
        cleaned = text.strip()
        finished = self.finished_value in cleaned
        return cleaned.replace(self.finished_value, ""), finished


PROMPT_TEMPLATE = """\
<<<<<<< HEAD
Ответь на сообщение пользователя, используя любой релевантный контекст. \
Если контекст предоставлен, ты должен основывать свой ответ на этом контексте. \
Как только ты закончишь отвечать, верни FINISHED.

>>> КОНТЕКСТ: {context}
>>> ВВОД ПОЛЬЗОВАТЕЛЯ: {user_input}
>>> ОТВЕТ: {response}\
=======
Respond to the user message using any relevant context. \
If context is provided, you should ground your answer in that context. \
Once you're done responding return FINISHED.

>>> CONTEXT: {context}
>>> USER INPUT: {user_input}
>>> RESPONSE: {response}\
>>>>>>> langchan/master
"""

PROMPT = PromptTemplate(
    template=PROMPT_TEMPLATE,
    input_variables=["user_input", "context", "response"],
)


QUESTION_GENERATOR_PROMPT_TEMPLATE = """\
<<<<<<< HEAD
Учитывая ввод пользователя и существующий частичный ответ в качестве контекста, \
задай вопрос, на который ответом является данный термин/сущность/фраза:

>>> ВВОД ПОЛЬЗОВАТЕЛЯ: {user_input}
>>> СУЩЕСТВУЮЩИЙ ЧАСТИЧНЫЙ ОТВЕТ: {current_response}

Вопрос, на который ответом является термин/сущность/фраза "{uncertain_span}", это:"""
=======
Given a user input and an existing partial response as context, \
ask a question to which the answer is the given term/entity/phrase:

>>> USER INPUT: {user_input}
>>> EXISTING PARTIAL RESPONSE: {current_response}

The question to which the answer is the term/entity/phrase "{uncertain_span}" is:"""
>>>>>>> langchan/master
QUESTION_GENERATOR_PROMPT = PromptTemplate(
    template=QUESTION_GENERATOR_PROMPT_TEMPLATE,
    input_variables=["user_input", "current_response", "uncertain_span"],
)
