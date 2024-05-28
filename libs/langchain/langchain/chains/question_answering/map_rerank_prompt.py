# flake8: noqa
from langchain.output_parsers.regex import RegexParser
from langchain_core.prompts import PromptTemplate

output_parser = RegexParser(
    regex=r"(.*?)\nScore: (\d*)",
    output_keys=["answer", "score"],
)

<<<<<<< HEAD
prompt_template = """Используй следующие части контекста, чтобы ответить на вопрос в конце. Если ты не знаешь ответа, просто скажи, что не знаешь, не пытайся придумать ответ.

В дополнение к ответу, также верни оценку того, насколько полно он отвечает на вопрос пользователя. Это должно быть в следующем формате:

Question: [вопрос здесь]
Полезный ответ: [ответ здесь]
Оценка: [оценка от 0 до 100]

Как определить оценку:
- Чем выше, тем лучше ответ
- Лучше отвечает полностью на заданный вопрос, с достаточным уровнем детализации
- Если ты не знаешь ответа на основе контекста, то это должна быть оценка 0
- Не будь чересчур уверенным!

Пример #1

Контекст:
---------
Яблоки красные
---------
Вопрос: какого цвета яблоки?
Полезный ответ: красные
Оценка: 100

Пример #2

Контекст:
---------
была ночь, и свидетель забыл свои очки. он не был уверен, была ли это спортивная машина или внедорожник
---------
Вопрос: какого типа была машина?
Полезный ответ: спортивная машина или внедорожник
Оценка: 60

Пример #3

Контекст:
---------
Груши бывают красные или оранжевые
---------
Question: какого цвета яблоки?
Полезный ответ: Этот документ не отвечает на вопрос
Оценка: 0

Начнем!

Контекст:
=======
prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

In addition to giving an answer, also return a score of how fully it answered the user's question. This should be in the following format:

Question: [question here]
Helpful Answer: [answer here]
Score: [score between 0 and 100]

How to determine the score:
- Higher is a better answer
- Better responds fully to the asked question, with sufficient level of detail
- If you do not know the answer based on the context, that should be a score of 0
- Don't be overconfident!

Example #1

Context:
---------
Apples are red
---------
Question: what color are apples?
Helpful Answer: red
Score: 100

Example #2

Context:
---------
it was night and the witness forgot his glasses. he was not sure if it was a sports car or an suv
---------
Question: what type was the car?
Helpful Answer: a sports car or an suv
Score: 60

Example #3

Context:
---------
Pears are either red or orange
---------
Question: what color are apples?
Helpful Answer: This document does not answer the question
Score: 0

Begin!

Context:
>>>>>>> langchan/master
---------
{context}
---------
Question: {question}
<<<<<<< HEAD
Полезный ответ:"""
=======
Helpful Answer:"""
>>>>>>> langchan/master
PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
    output_parser=output_parser,
)
