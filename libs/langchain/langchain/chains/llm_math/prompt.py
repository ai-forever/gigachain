# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
_PROMPT_TEMPLATE = """Переведи математическую задачу в выражение, которое можно выполнить с помощью библиотеки numexpr в Python. Используй результат выполнения этого кода, чтобы ответить на вопрос.

Question: ${{Вопрос с математической задачей.}}
```text
${{однострочное математическое выражение, решающее задачу}}
```
...numexpr.evaluate(text)...
```output
${{Результат выполнения кода}}
```
Ответ: ${{Ответ}}

Начнем.

Question: Чему равно 37593 * 67?
=======
_PROMPT_TEMPLATE = """Translate a math problem into a expression that can be executed using Python's numexpr library. Use the output of running this code to answer the question.

Question: ${{Question with math problem.}}
```text
${{single line mathematical expression that solves the problem}}
```
...numexpr.evaluate(text)...
```output
${{Output of running the code}}
```
Answer: ${{Answer}}

Begin.

Question: What is 37593 * 67?
>>>>>>> langchan/master
```text
37593 * 67
```
...numexpr.evaluate("37593 * 67")...
```output
2518731
```
<<<<<<< HEAD
Ответ: 2518731
=======
Answer: 2518731
>>>>>>> langchan/master

Question: 37593^(1/5)
```text
37593**(1/5)
```
...numexpr.evaluate("37593**(1/5)")...
```output
8.222831614237718
```
<<<<<<< HEAD
Ответ: 8.222831614237718
=======
Answer: 8.222831614237718
>>>>>>> langchan/master

Question: {question}
"""

PROMPT = PromptTemplate(
    input_variables=["question"],
    template=_PROMPT_TEMPLATE,
)
