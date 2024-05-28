# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
NAIVE_FIX = """Инструкции:
--------------
{instructions}
--------------
Завершение:
=======
NAIVE_FIX = """Instructions:
--------------
{instructions}
--------------
Completion:
>>>>>>> langchan/master
--------------
{completion}
--------------

<<<<<<< HEAD
Вышеуказанное Завершение не удовлетворяет ограничениям, указанным в Инструкциях.
Ошибка:
=======
Above, the Completion did not satisfy the constraints given in the Instructions.
Error:
>>>>>>> langchan/master
--------------
{error}
--------------

<<<<<<< HEAD
Пожалуйста, попробуй ещё раз. Отвечай только так, чтобы это удовлетворяло ограничениям, изложенным в Инструкциях:"""
=======
Please try again. Please only respond with an answer that satisfies the constraints laid out in the Instructions:"""
>>>>>>> langchan/master


NAIVE_FIX_PROMPT = PromptTemplate.from_template(NAIVE_FIX)
