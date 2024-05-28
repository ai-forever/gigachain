<<<<<<< HEAD
# ruff: noqa: E501

=======
>>>>>>> langchan/master
import json
from textwrap import dedent
from typing import List

from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_experimental.tot.thought import ThoughtValidity


def get_cot_prompt() -> PromptTemplate:
    """Get the prompt for the Chain of Thought (CoT) chain."""

    return PromptTemplate(
        template_format="jinja2",
        input_variables=["problem_description", "thoughts"],
        template=dedent(
            """
<<<<<<< HEAD
            Ты - интеллектуальный агент, который генерирует одну мысль за раз в
            древовидной структуре мыслей.

            ПРОБЛЕМА 
=======
            You are an intelligent agent that is generating one thought at a time in
            a tree of thoughts setting.

            PROBLEM 
>>>>>>> langchan/master
            
            {{problem_description}}
            
            {% if thoughts %}
<<<<<<< HEAD
            МЫСЛИ
=======
            THOUGHTS
>>>>>>> langchan/master
            
            {% for thought in thoughts %}
            {{ thought }}
            {% endfor %}
            {% endif %}
            
<<<<<<< HEAD
            Давайте думать шаг за шагом.
=======
            Let's think step by step.
>>>>>>> langchan/master
            """
        ).strip(),
    )


class JSONListOutputParser(BaseOutputParser):
    """Parse the output of a PROPOSE_PROMPT response."""

    @property
    def _type(self) -> str:
        return "json_list"

    def parse(self, text: str) -> List[str]:
        """Parse the output of an LLM call."""

        json_string = text.split("```json")[1].strip().strip("```").strip()
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return []


def get_propose_prompt() -> PromptTemplate:
    """Get the prompt for the PROPOSE_PROMPT chain."""

    return PromptTemplate(
        template_format="jinja2",
        input_variables=["problem_description", "thoughts", "n"],
        output_parser=JSONListOutputParser(),
        template=dedent(
            """
<<<<<<< HEAD
            Ты - интеллектуальный агент, который генерирует мысли в древовидной
            структуре мыслей.

            Вывод должен быть оформлен в виде фрагмента кода на markdown, отформатированного как JSON-список
            строк, включая ведущие и замыкающие "```json" и "```":

            ```json
            [
                "<мысль-1>",
                "<мысль-2>",
                "<мысль-3>"
            ]
            ```

            ПРОБЛЕМА

            {{ problem_description }}

            {% if thoughts %}
            ВАЛИДНЫЕ МЫСЛИ

            {% for thought in thoughts %}
            {{ thought }}
            {% endfor %}

            Возможные следующие {{ n }} валидные мысли на основе последней валидной мысли:
            {% else %}

            Возможные следующие {{ n }} валидные мысли на основе ПРОБЛЕМЫ:
            {%- endif -%}
        """
=======
                You are an intelligent agent that is generating thoughts in a tree of
                thoughts setting.
                
                The output should be a markdown code snippet formatted as a JSON list of
                strings, including the leading and trailing "```json" and "```":
                
                ```json
                [
                "<thought-1>",
                "<thought-2>",
                "<thought-3>"
                ]
                ```
                
                PROBLEM
                
                {{ problem_description }}
                
                {% if thoughts %}
                VALID THOUGHTS
                
                {% for thought in thoughts %}
                {{ thought }}
                {% endfor %}
                
                Possible next {{ n }} valid thoughts based on the last valid thought:
                {% else %}
                
                Possible next {{ n }} valid thoughts based on the PROBLEM:
                {%- endif -%}
                """
>>>>>>> langchan/master
        ).strip(),
    )


class CheckerOutputParser(BaseOutputParser):
    """Parse and check the output of the language model."""

    def parse(self, text: str) -> ThoughtValidity:
        """Parse the output of the language model."""
        text = text.upper()
        if "INVALID" in text:
            return ThoughtValidity.INVALID
        elif "INTERMEDIATE" in text:
            return ThoughtValidity.VALID_INTERMEDIATE
        elif "VALID" in text:
            return ThoughtValidity.VALID_FINAL
        else:
            return ThoughtValidity.INVALID

    @property
    def _type(self) -> str:
        return "tot_llm_checker_output"


CHECKER_PROMPT = PromptTemplate(
    input_variables=["problem_description", "thoughts"],
    template=dedent(
        """
<<<<<<< HEAD
        Ты - интеллектуальный агент, проверяющий мысли другого интеллектуального агента.

        ПРОБЛЕМА 
        
        {problem_description}

        МЫСЛИ
        
        {thoughts}

        Оцени мысли и ответь одним словом.

        - Ответь ВАЛИДНО, если последняя мысль является валидным окончательным решением проблемы.
        - Ответь НЕВАЛИДНО, если последняя мысль невалидна.
        - Ответь ПРОМЕЖУТОЧНО, если последняя мысль валидна, но не является окончательным 
        решением проблемы.

        Эта цепочка мыслей"""
=======
        You are an intelligent agent, validating thoughts of another intelligent agent.

        PROBLEM 
        
        {problem_description}

        THOUGHTS
        
        {thoughts}

        Evaluate the thoughts and respond with one word.

        - Respond VALID if the last thought is a valid final solution to the
        problem.
        - Respond INVALID if the last thought is invalid.
        - Respond INTERMEDIATE if the last thought is valid but not the final
        solution to the problem.

        This chain of thoughts is"""
>>>>>>> langchan/master
    ).strip(),
    output_parser=CheckerOutputParser(),
)
