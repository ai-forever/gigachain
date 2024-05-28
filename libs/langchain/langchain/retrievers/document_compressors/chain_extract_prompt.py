# flake8: noqa
<<<<<<< HEAD
prompt_template = """Учитывая следующий вопрос и контекст, извлеките любую часть контекста *КАК ЕСТЬ*, которая имеет отношение к ответу на вопрос. Если ни одна часть контекста не имеет отношения, верните {no_output_str}. 

Помните, *НЕ РЕДАКТИРУЙТЕ* извлеченные части контекста.

> Вопрос: {{question}}
> Контекст:
>>>
{{context}}
>>>
Извлеченные релевантные части:"""
=======
prompt_template = """Given the following question and context, extract any part of the context *AS IS* that is relevant to answer the question. If none of the context is relevant return {no_output_str}. 

Remember, *DO NOT* edit the extracted parts of the context.

> Question: {{question}}
> Context:
>>>
{{context}}
>>>
Extracted relevant parts:"""
>>>>>>> langchan/master
