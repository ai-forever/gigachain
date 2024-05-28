"""Prompt for trajectory evaluation chain."""
<<<<<<< HEAD

=======
>>>>>>> langchan/master
# flake8: noqa
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)


<<<<<<< HEAD
EVAL_TEMPLATE = """Языковая модель AI получила доступ к следующему набору инструментов, чтобы помочь ответить на вопрос пользователя.

Инструменты, предоставленные модели AI:
=======
EVAL_TEMPLATE = """An AI language model has been given access to the following set of tools to help answer a user's question.

The tools given to the AI model are:
>>>>>>> langchan/master
[TOOL_DESCRIPTIONS]
{tool_descriptions}
[END_TOOL_DESCRIPTIONS]

<<<<<<< HEAD
Вопрос, который человек задал модели AI:
=======
The question the human asked the AI model was:
>>>>>>> langchan/master
[QUESTION]
{question}
[END_QUESTION]{reference}

<<<<<<< HEAD
Языковая модель AI решила использовать следующий набор инструментов для ответа на вопрос:
=======
The AI language model decided to use the following set of tools to answer the question:
>>>>>>> langchan/master
[AGENT_TRAJECTORY]
{agent_trajectory}
[END_AGENT_TRAJECTORY]

<<<<<<< HEAD
Окончательный ответ языковой модели AI на вопрос был:
=======
The AI language model's final answer to the question was:
>>>>>>> langchan/master
[RESPONSE]
{answer}
[END_RESPONSE]

<<<<<<< HEAD
Давай проведем подробную оценку ответа языковой модели AI шаг за шагом.

Мы учитываем следующие критерии перед тем, как дать оценку от 1 до 5:

i. Полезен ли окончательный ответ?
ii. Использует ли AI логическую последовательность инструментов для ответа на вопрос?
iii. Использует ли модель языка AI инструменты полезным образом?
iv. Использует ли модель языка AI слишком много шагов для ответа на вопрос?
v. Используются ли подходящие инструменты для ответа на вопрос?"""

EXAMPLE_INPUT = """Языковая модель AI получила доступ к следующему набору инструментов, чтобы помочь ответить на вопрос пользователя.

Инструменты, предоставленные модели AI:
[TOOL_DESCRIPTIONS]
Инструмент 1:
Название: Поиск
Описание: полезно, когда нужно задать вопрос с поиском

Инструмент 2:
Название: Поиск
Описание: полезно, когда нужно задать вопрос с поиском

Инструмент 3:
Название: Калькулятор
Описание: полезно для выполнения расчетов

Инструмент 4:
Название: Поиск в Интернете (SerpAPI)
Описание: полезно, когда нужно ответить на вопросы о текущих событиях
[END_TOOL_DESCRIPTIONS]

Вопрос, который человек задал модели AI: Если положить Статую Свободы вдоль, сколько раз она протянется через Соединенные Штаты?

Языковая модель AI решила использовать следующий набор инструментов для ответа на вопрос:
[AGENT_TRAJECTORY]
Шаг 1:
Используемый инструмент: Поиск в Интернете (SerpAPI)
Ввод инструмента: Если положить Статую Свободы вдоль, сколько раз она протянется через Соединенные Штаты?
Выход инструмента: Статуя Свободы была подарена Соединенным Штатам Францией в знак дружбы между двумя странами. Она была воздвигнута на американском проекте ...
[END_AGENT_TRAJECTORY]

[RESPONSE]
Окончательный ответ языковой модели AI на вопрос был: Есть разные способы измерить длину Соединенных Штатов, но если мы используем расстояние между Статуей Свободы и самой западной точкой континентальных Соединенных Штатов (мыс Алава, Вашингтон), которое составляет примерно 2,857 миль (4,596 км), и предположим, что Статуя Свободы имеет высоту 305 футов (93 метра), то статуя протянется через Соединенные Штаты примерно 17,5 раз, если положить ее вдоль.
[END_RESPONSE]

Давай проведем подробную оценку ответа языковой модели AI шаг за шагом.

Мы учитываем следующие критерии перед тем, как дать оценку от 1 до 5:

i. Полезен ли окончательный ответ?
ii. Использует ли AI логическую последовательность инструментов для ответа на вопрос?
iii. Использует ли модель языка AI инструменты полезным образом?
iv. Использует ли модель языка AI слишком много шагов для ответа на вопрос?
v. Используются ли подходящие инструменты для ответа на вопрос?"""

EXAMPLE_OUTPUT = """Во-первых, давайте оценим окончательный ответ. Окончательный ответ использует хорошее обоснование, но неверен. 2,857 деленное на 305 не равно 17,5.\
Модель должна была использовать калькулятор, чтобы выяснить это. Во-вторых, использует ли модель логическую последовательность инструментов для ответа на вопрос?\
Способ использования поиска моделью не полезен. Модель должна была использовать инструмент поиска, чтобы узнать ширину США или высоту статуи.\
Модель не использовала инструмент калькулятора и дала неверный ответ. Поисковый API должен использоваться для текущих событий или конкретных вопросов.\
Инструменты не использовались полезным образом. Модель не использовала слишком много шагов для ответа на вопрос.\
Модель не использовала подходящие инструменты для ответа на вопрос.\
    
Оценка: Учитывая хорошее обоснование в окончательном ответе, но в остальном слабую работу, мы даем модели оценку 2.

Оценка: 2"""
=======
Let's to do a detailed evaluation of the AI language model's answer step by step.

We consider the following criteria before giving a score from 1 to 5:

i. Is the final answer helpful?
ii. Does the AI language use a logical sequence of tools to answer the question?
iii. Does the AI language model use the tools in a helpful way?
iv. Does the AI language model use too many steps to answer the question?
v. Are the appropriate tools used to answer the question?"""

EXAMPLE_INPUT = """An AI language model has been given access to the following set of tools to help answer a user's question.

The tools given to the AI model are:
[TOOL_DESCRIPTIONS]
Tool 1:
Name: Search
Description: useful for when you need to ask with search

Tool 2:
Name: Lookup
Description: useful for when you need to ask with lookup

Tool 3:
Name: Calculator
Description: useful for doing calculations

Tool 4:
Name: Search the Web (SerpAPI)
Description: useful for when you need to answer questions about current events
[END_TOOL_DESCRIPTIONS]

The question the human asked the AI model was: If laid the Statue of Liberty end to end, how many times would it stretch across the United States?

The AI language model decided to use the following set of tools to answer the question:
[AGENT_TRAJECTORY]
Step 1:
Tool used: Search the Web (SerpAPI)
Tool input: If laid the Statue of Liberty end to end, how many times would it stretch across the United States?
Tool output: The Statue of Liberty was given to the United States by France, as a symbol of the two countries' friendship. It was erected atop an American-designed ...
[END_AGENT_TRAJECTORY]

[RESPONSE]
The AI language model's final answer to the question was: There are different ways to measure the length of the United States, but if we use the distance between the Statue of Liberty and the westernmost point of the contiguous United States (Cape Alava, Washington), which is approximately 2,857 miles (4,596 km), and assume that the Statue of Liberty is 305 feet (93 meters) tall, then the statue would stretch across the United States approximately 17.5 times if laid end to end.
[END_RESPONSE]

Let's to do a detailed evaluation of the AI language model's answer step by step.

We consider the following criteria before giving a score from 1 to 5:

i. Is the final answer helpful?
ii. Does the AI language use a logical sequence of tools to answer the question?
iii. Does the AI language model use the tools in a helpful way?
iv. Does the AI language model use too many steps to answer the question?
v. Are the appropriate tools used to answer the question?"""

EXAMPLE_OUTPUT = """First, let's evaluate the final answer. The final uses good reasoning but is wrong. 2,857 divided by 305 is not 17.5.\
The model should have used the calculator to figure this out. Second does the model use a logical sequence of tools to answer the question?\
The way model uses the search is not helpful. The model should have used the search tool to figure the width of the US or the height of the statue.\
The model didn't use the calculator tool and gave an incorrect answer. The search API should be used for current events or specific questions.\
The tools were not used in a helpful way. The model did not use too many steps to answer the question.\
The model did not use the appropriate tools to answer the question.\
    
Judgment: Given the good reasoning in the final answer but otherwise poor performance, we give the model a score of 2.

Score: 2"""
>>>>>>> langchan/master

EVAL_CHAT_PROMPT = ChatPromptTemplate.from_messages(
    messages=[
        SystemMessage(
<<<<<<< HEAD
            content="Ты полезный помощник, который оценивает языковые модели."
=======
            content="You are a helpful assistant that evaluates language models."
>>>>>>> langchan/master
        ),
        HumanMessage(content=EXAMPLE_INPUT),
        AIMessage(content=EXAMPLE_OUTPUT),
        HumanMessagePromptTemplate.from_template(EVAL_TEMPLATE),
    ]
)


<<<<<<< HEAD
TOOL_FREE_EVAL_TEMPLATE = """Языковая модель AI получила доступ к набору инструментов, чтобы помочь ответить на вопрос пользователя.

Вопрос, который человек задал модели AI:
=======
TOOL_FREE_EVAL_TEMPLATE = """An AI language model has been given access to a set of tools to help answer a user's question.

The question the human asked the AI model was:
>>>>>>> langchan/master
[QUESTION]
{question}
[END_QUESTION]{reference}

<<<<<<< HEAD
Языковая модель AI решила использовать следующий набор инструментов для ответа на вопрос:
=======
The AI language model decided to use the following set of tools to answer the question:
>>>>>>> langchan/master
[AGENT_TRAJECTORY]
{agent_trajectory}
[END_AGENT_TRAJECTORY]

<<<<<<< HEAD
Окончательный ответ языковой модели AI на вопрос был:
=======
The AI language model's final answer to the question was:
>>>>>>> langchan/master
[RESPONSE]
{answer}
[END_RESPONSE]

<<<<<<< HEAD
Давай проведем подробную оценку ответа языковой модели AI шаг за шагом.

Мы учитываем следующие критерии перед тем, как дать оценку от 1 до 5:

i. Полезен ли окончательный ответ?
ii. Использует ли AI логическую последовательность инструментов для ответа на вопрос?
iii. Использует ли модель языка AI инструменты полезным образом?
iv. Использует ли модель языка AI слишком много шагов для ответа на вопрос?
v. Используются ли подходящие инструменты для ответа на вопрос?"""
=======
Let's to do a detailed evaluation of the AI language model's answer step by step.

We consider the following criteria before giving a score from 1 to 5:

i. Is the final answer helpful?
ii. Does the AI language use a logical sequence of tools to answer the question?
iii. Does the AI language model use the tools in a helpful way?
iv. Does the AI language model use too many steps to answer the question?
v. Are the appropriate tools used to answer the question?"""
>>>>>>> langchan/master


TOOL_FREE_EVAL_CHAT_PROMPT = ChatPromptTemplate.from_messages(
    messages=[
        SystemMessage(
<<<<<<< HEAD
            content="Ты полезный помощник, который оценивает языковые модели."
=======
            content="You are a helpful assistant that evaluates language models."
>>>>>>> langchan/master
        ),
        HumanMessage(content=EXAMPLE_INPUT),
        AIMessage(content=EXAMPLE_OUTPUT),
        HumanMessagePromptTemplate.from_template(TOOL_FREE_EVAL_TEMPLATE),
    ]
)
