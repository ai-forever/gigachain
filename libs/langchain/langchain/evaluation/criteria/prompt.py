# flake8: noqa
# Credit to https://github.com/openai/evals/tree/main

from langchain_core.prompts import PromptTemplate

<<<<<<< HEAD
template = """Ты оцениваешь представленный ответ на заданную задачу или ввод на основе набора критериев. Вот данные:
[НАЧАЛО ДАННЫХ]
***
[Ввод]: {input}
***
[Ответ]: {output}
***
[Критерии]: {criteria}
***
[КОНЕЦ ДАННЫХ]
Соответствует ли ответ критериям? Сначала пошагово изложи свои рассуждения по каждому критерию, чтобы убедиться, что твой вывод верен. Избегай простого утверждения правильных ответов с самого начала. Затем напечатай только одну букву "Y" или "N" (без кавычек или знаков препинания) на отдельной строке, соответствующую правильному ответу о том, соответствует ли ответ всем критериям. В конце повтори просто букву еще раз саму по себе на новой строке."""
=======
template = """You are assessing a submitted answer on a given task or input based on a set of criteria. Here is the data:
[BEGIN DATA]
***
[Input]: {input}
***
[Submission]: {output}
***
[Criteria]: {criteria}
***
[END DATA]
Does the submission meet the Criteria? First, write out in a step by step manner your reasoning about each criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the outset. Then print only the single character "Y" or "N" (without quotes or punctuation) on its own line corresponding to the correct answer of whether the submission meets all criteria. At the end, repeat just the letter again by itself on a new line."""
>>>>>>> langchan/master

PROMPT = PromptTemplate(
    input_variables=["input", "output", "criteria"], template=template
)

<<<<<<< HEAD
template = """Ты оцениваешь представленный ответ на заданную задачу или ввод на основе набора критериев. Вот данные:
[НАЧАЛО ДАННЫХ]
***
[Ввод]: {input}
***
[Ответ]: {output}
***
[Критерии]: {criteria}
***
[Справка]: {reference}
***
[КОНЕЦ ДАННЫХ]
Соответствует ли ответ критериям? Сначала пошагово изложи свои рассуждения по каждому критерию, чтобы убедиться, что твой вывод верен. Избегай простого утверждения правильных ответов с самого начала. Затем напечатай только одну букву "Y" или "N" (без кавычек или знаков препинания) на отдельной строке, соответствующую правильному ответу о том, соответствует ли ответ всем критериям. В конце повтори просто букву еще раз саму по себе на новой строке."""
=======
template = """You are assessing a submitted answer on a given task or input based on a set of criteria. Here is the data:
[BEGIN DATA]
***
[Input]: {input}
***
[Submission]: {output}
***
[Criteria]: {criteria}
***
[Reference]: {reference}
***
[END DATA]
Does the submission meet the Criteria? First, write out in a step by step manner your reasoning about each criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the outset. Then print only the single character "Y" or "N" (without quotes or punctuation) on its own line corresponding to the correct answer of whether the submission meets all criteria. At the end, repeat just the letter again by itself on a new line."""
>>>>>>> langchan/master

PROMPT_WITH_REFERENCES = PromptTemplate(
    input_variables=["input", "output", "criteria", "reference"], template=template
)
