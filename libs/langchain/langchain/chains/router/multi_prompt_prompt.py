<<<<<<< HEAD
# flake8: noqa
"""Запрос для роутера в цепочке множественных запросов."""

MULTI_PROMPT_ROUTER_TEMPLATE = """\
Учитывая исходный текстовый ввод в языковую модель, выбери наиболее подходящий запрос для \
ввода. Тебе будут даны имена доступных запросов и описание того, для чего лучше всего подходит \
запрос. Ты также можешь пересмотреть исходный ввод, если считаешь, что его изменение в конечном итоге \
приведет к лучшему ответу от языковой модели.

<< ФОРМАТИРОВАНИЕ >>
Верни фрагмент кода в markdown с объектом JSON, отформатированным таким образом:
```json
{{{{
    "destination": string \\ имя используемого запроса или "DEFAULT"
    "next_inputs": string \\ возможно измененная версия исходного ввода
}}}}
```

ПОМНИ: "destination" ДОЛЖЕН быть одним из имен кандидатов на запрос, указанных ниже, ИЛИ \
он может быть "DEFAULT", если ввод не очень подходит для любого из кандидатов на запрос.
ПОМНИ: "next_inputs" может быть просто исходным вводом, если ты не думаешь, что \
необходимы какие-либо изменения.

<< КАНДИДАТЫ НА ЗАПРОСЫ >>
{destinations}

<< ВВОД >>
{{input}}

<< ВЫВОД (должен включать ```json в начале ответа) >>
=======
"""Prompt for the router chain in the multi-prompt chain."""

MULTI_PROMPT_ROUTER_TEMPLATE = """\
Given a raw text input to a language model select the model prompt best suited for \
the input. You will be given the names of the available prompts and a description of \
what the prompt is best suited for. You may also revise the original input if you \
think that revising it will ultimately lead to a better response from the language \
model.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted to look like:
```json
{{{{
    "destination": string \\ name of the prompt to use or "DEFAULT"
    "next_inputs": string \\ a potentially modified version of the original input
}}}}
```

REMEMBER: "destination" MUST be one of the candidate prompt names specified below OR \
it can be "DEFAULT" if the input is not well suited for any of the candidate prompts.
REMEMBER: "next_inputs" can just be the original input if you don't think any \
modifications are needed.

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{{input}}

<< OUTPUT (must include ```json at the start of the response) >>
<< OUTPUT (must end with ```) >>
>>>>>>> langchan/master
"""
