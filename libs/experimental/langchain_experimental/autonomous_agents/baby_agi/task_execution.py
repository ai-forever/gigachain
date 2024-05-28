from langchain.chains import LLMChain
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import PromptTemplate


class TaskExecutionChain(LLMChain):
    """Chain to execute tasks."""

    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        execution_template = (
<<<<<<< HEAD
            "Ты - искусственный интеллект, который"
            " выполняет одну задачу на основе следующей цели: "
            "{objective}."
            "Учти эти ранее выполненные задачи: {context}."
            " Твоя задача: {task}. Ответ:"
=======
            "You are an AI who performs one task based on the following objective: "
            "{objective}."
            "Take into account these previously completed tasks: {context}."
            " Your task: {task}. Response:"
>>>>>>> langchan/master
        )
        prompt = PromptTemplate(
            template=execution_template,
            input_variables=["objective", "context", "task"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
