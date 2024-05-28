import re

from langchain.chains import LLMChain
from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

from langchain_experimental.plan_and_execute.planners.base import LLMPlanner
from langchain_experimental.plan_and_execute.schema import (
    Plan,
    PlanOutputParser,
    Step,
)

SYSTEM_PROMPT = (
<<<<<<< HEAD
    "Давай сначала поймем проблему и разработаем план для ее решения."
    " Пожалуйста, выведи план, начиная с заголовка 'План:', "
    "а затем следуя нумерованным шагам. "
    "План должен содержать минимальное количество шагов, "
    "необходимых для точного выполнения задачи. Если задача представляет собой вопрос, "
    "то последним шагом почти всегда должно быть 'Учитывая приведенные выше шаги, "
    "пожалуйста, ответь на исходный вопрос пользователя'. "
    "В конце своего плана скажи '<END_OF_PLAN>'"
=======
    "Let's first understand the problem and devise a plan to solve the problem."
    " Please output the plan starting with the header 'Plan:' "
    "and then followed by a numbered list of steps. "
    "Please make the plan the minimum number of steps required "
    "to accurately complete the task. If the task is a question, "
    "the final step should almost always be 'Given the above steps taken, "
    "please respond to the users original question'. "
    "At the end of your plan, say '<END_OF_PLAN>'"
>>>>>>> langchan/master
)


class PlanningOutputParser(PlanOutputParser):
<<<<<<< HEAD
    """Парсер выходных данных планирования."""
=======
    """Planning output parser."""
>>>>>>> langchan/master

    def parse(self, text: str) -> Plan:
        steps = [Step(value=v) for v in re.split("\n\s*\d+\. ", text)[1:]]
        return Plan(steps=steps)


def load_chat_planner(
    llm: BaseLanguageModel, system_prompt: str = SYSTEM_PROMPT
) -> LLMPlanner:
    """
<<<<<<< HEAD
    Загрузить планировщик чата.

    Args:
        llm: Языковая модель.
        system_prompt: Системный запрос.
=======
    Load a chat planner.

    Args:
        llm: Language model.
        system_prompt: System prompt.
>>>>>>> langchan/master

    Returns:
        LLMPlanner
    """
    prompt_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            HumanMessagePromptTemplate.from_template("{input}"),
        ]
    )
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)
    return LLMPlanner(
        llm_chain=llm_chain,
        output_parser=PlanningOutputParser(),
        stop=["<END_OF_PLAN>"],
    )
