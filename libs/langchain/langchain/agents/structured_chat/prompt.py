# flake8: noqa
<<<<<<< HEAD
PREFIX = """Отвечай человеку как можно более полезно и точно. У тебя есть доступ к следующим инструментам:"""
FORMAT_INSTRUCTIONS = """Используй json-объект для указания инструмента, предоставив ключ действия (имя инструмента) и ключ ввода действия (ввод инструмента).

Допустимые значения "action": "Final Answer" или {tool_names}

Предоставь только ОДНО действие на $JSON_BLOB, как показано:
=======
PREFIX = """Respond to the human as helpfully and accurately as possible. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).

Valid "action" values: "Final Answer" or {tool_names}

Provide only ONE action per $JSON_BLOB, as shown:
>>>>>>> langchan/master

```
{{{{
  "action": $TOOL_NAME,
  "action_input": $INPUT
}}}}
```

<<<<<<< HEAD
Следуй этому формату:

Question: вводимый вопрос для ответа
Thought: учитывай предыдущие и последующие шаги
=======
Follow this format:

Question: input question to answer
Thought: consider previous and subsequent steps
>>>>>>> langchan/master
Action:
```
$JSON_BLOB
```
<<<<<<< HEAD
Observation: результат действия
... (повторяй Thought/Action/Action Input/Observation может повторяться N раз)
Thought: Я знаю, что отвечать
=======
Observation: action result
... (repeat Thought/Action/Observation N times)
Thought: I know what to respond
>>>>>>> langchan/master
Action:
```
{{{{
  "action": "Final Answer",
<<<<<<< HEAD
  "action_input": "Окончательный ответ человеку"
}}}}
```"""
SUFFIX = """Начни! Напоминаю, что ВСЕГДА нужно отвечать действительным json-объектом одного действия. Используй инструменты, если это необходимо. Отвечай напрямую, если это уместно. Формат - Action:```$JSON_BLOB```затем Observation:.
=======
  "action_input": "Final response to human"
}}}}
```"""
SUFFIX = """Begin! Reminder to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly if appropriate. Format is Action:```$JSON_BLOB```then Observation:.
>>>>>>> langchan/master
Thought:"""
