<<<<<<< HEAD
# flake8: noqa
"""Prompt для цепочки роутеров в цепочке вопросов и ответов с множественным извлечением."""

MULTI_RETRIEVAL_ROUTER_TEMPLATE = """\
Учитывая запрос к системе ответов на вопросы, выбери наиболее подходящую систему \
для входных данных. Тебе будут даны имена доступных систем и описание \
для каких вопросов эта система наиболее подходит. Ты также можешь пересмотреть исходный \
запрос, если считаешь, что его изменение в конечном итоге приведет к лучшему ответу.

<< ФОРМАТИРОВАНИЕ >>
Верни фрагмент кода markdown с объектом JSON, отформатированным таким образом:
```json
{{{{
    "destination": string \\ имя системы ответов на вопросы для использования или "DEFAULT"
    "next_inputs": string \\ возможно измененная версия исходного запроса
}}}}
```

ПОМНИ: "destination" ДОЛЖЕН быть одним из указанных ниже имен кандидатов на промпт ИЛИ \
он может быть "DEFAULT", если входные данные не подходят для любого из кандидатов на промпт.
ПОМНИ: "next_inputs" может быть просто исходным запросом, если ты не считаешь, что нужны \
какие-либо изменения.

<< КАНДИДАТЫ НА ПРОМПТ >>
{destinations}

<< ВХОДНЫЕ ДАННЫЕ >>
{{input}}

<< ВЫХОДНЫЕ ДАННЫЕ >>
=======
"""Prompt for the router chain in the multi-retrieval qa chain."""

MULTI_RETRIEVAL_ROUTER_TEMPLATE = """\
Given a query to a question answering system select the system best suited \
for the input. You will be given the names of the available systems and a description \
of what questions the system is best suited for. You may also revise the original \
input if you think that revising it will ultimately lead to a better response.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted to look like:
```json
{{{{
    "destination": string \\ name of the question answering system to use or "DEFAULT"
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

<< OUTPUT >>
>>>>>>> langchan/master
"""
