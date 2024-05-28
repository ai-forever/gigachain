# flake8: noqa
<<<<<<< HEAD
PREFIX = """
Ты бот-ассистент. Ты можешь выбирать какую функцию выполнить и какие параметры ей передать.
Ответь не следующие вопросы как можно лучше. Ты можешь вызвать следующие функции:"""  # noqa: E501
FORMAT_INSTRUCTIONS = """
За один запрос ты можешь выполнить одну функцию
Question: *изначальный вопрос пользователя*

Используй следующий формат:
-----
[Начало цикла]
Thought: Введи здесь Мысль, что ты должен сделать
Action: [название функции, должно быть из списка [{tool_names}]]
Action Input: [параметры для функции]
Observation: Результат выполнения функции
[Конец цикла]
------
Цикл с вопросами может выполняться N раз Thought -> Action -> Action Input -> Observation
Если в результате выполнения функции ты не получил финальный ответ, выполни цикл еще раз
Когда ты знаешь окончательный ответ ты должен написать
-----
Thought: Теперь я знаю окончательный ответ
Final Answer: окончательный ответ на исходный вопрос
-----
"""  # noqa: E501
SUFFIX = """
Question: {input}{agent_scratchpad}
"""
=======
PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question"""
SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""
>>>>>>> langchan/master
