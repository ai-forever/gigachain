# flake8: noqa
<<<<<<< HEAD
SYSTEM_MESSAGE_PREFIX = """Ответь на следующие вопросы как можно лучше. У тебя есть следующие инструменты:"""
FORMAT_INSTRUCTIONS = """Использование инструментов происходит путем указания json блока.
В частности, этот json должен иметь ключ `action` (с именем используемого инструмента) и ключ `action_input` (с вводом в инструмент здесь).

Единственные значения, которые должны быть в поле "action", это: {tool_names}

$JSON_BLOB должен содержать только ОДНО действие, НЕ возвращайте список нескольких действий. Вот пример действительного $JSON_BLOB:
=======
SYSTEM_MESSAGE_PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """The way you use the tools is by specifying a json blob.
Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are: {tool_names}

The $JSON_BLOB should only contain a SINGLE action, do NOT return a list of multiple actions. Here is an example of a valid $JSON_BLOB:
>>>>>>> langchan/master

```
{{{{
  "action": $TOOL_NAME,
  "action_input": $INPUT
}}}}
```

<<<<<<< HEAD
ВСЕГДА используй следующий формат:

Question: вопрос, на который ты должен ответить
Thought: ты всегда должен думать, что делать
=======
ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
>>>>>>> langchan/master
Action:
```
$JSON_BLOB
```
<<<<<<< HEAD
Observation: результат действия
... (этот цикл Thought/Action/Action Input/Observation может повторяться N раз)
Thought: теперь я знаю окончательный ответ
Final answer: окончательный ответ на исходный вопрос"""
SYSTEM_MESSAGE_SUFFIX = """Начни! Напоминаю, что всегда нужно использовать точные символы `Final answer` при ответе."""
=======
Observation: the result of the action
... (this Thought/Action/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question"""
SYSTEM_MESSAGE_SUFFIX = """Begin! Reminder to always use the exact characters `Final Answer` when responding."""
>>>>>>> langchan/master
HUMAN_MESSAGE = "{input}\n\n{agent_scratchpad}"
