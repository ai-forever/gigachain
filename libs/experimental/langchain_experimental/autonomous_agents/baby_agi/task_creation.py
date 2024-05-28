from langchain.chains import LLMChain
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import PromptTemplate


class TaskCreationChain(LLMChain):
    """Chain generating tasks."""

    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        task_creation_template = (
<<<<<<< HEAD
            "Ты - AI, создающий задачи,"
            " который использует результат работы исполнительного агента"
            " для создания новых задач с следующей целью: {objective},"
            " Последняя выполненная задача имеет результат: {result}."
            " Этот результат был основан на этом описании задачи: {task_description}."
            " Вот незавершенные задачи: {incomplete_tasks}."
            " Основываясь на результате, создай новые задачи для выполнения"
            " AI системой, которые не пересекаются с незавершенными задачами."
            " Верни задачи в виде массива."
=======
            "You are an task creation AI that uses the result of an execution agent"
            " to create new tasks with the following objective: {objective},"
            " The last completed task has the result: {result}."
            " This result was based on this task description: {task_description}."
            " These are incomplete tasks: {incomplete_tasks}."
            " Based on the result, create new tasks to be completed"
            " by the AI system that do not overlap with incomplete tasks."
            " Return the tasks as an array."
>>>>>>> langchan/master
        )
        prompt = PromptTemplate(
            template=task_creation_template,
            input_variables=[
                "result",
                "task_description",
                "incomplete_tasks",
                "objective",
            ],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
