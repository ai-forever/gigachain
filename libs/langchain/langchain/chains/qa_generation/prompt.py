# flake8: noqa
from langchain.chains.prompt_selector import ConditionalPromptSelector, is_chat_model
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
templ1 = """Ты умный помощник, созданный для помощи учителям старших классов в создании вопросов для проверки понимания прочитанного.
Получив текст, ты должен придумать пару вопрос-ответ, которую можно использовать для проверки способностей ученика к пониманию прочитанного.
При создании этой пары вопрос-ответ, ты должен ответить в следующем формате:
=======
templ1 = """You are a smart assistant designed to help high school teachers come up with reading comprehension questions.
Given a piece of text, you must come up with a question and answer pair that can be used to test a student's reading comprehension abilities.
When coming up with this question/answer pair, you must respond in the following format:
>>>>>>> langchan/master
```
{{
    "question": "$YOUR_QUESTION_HERE",
    "answer": "$THE_ANSWER_HERE"
}}
```

<<<<<<< HEAD
Все, что находится между ``` должно быть валидным json.
"""
templ2 = """Пожалуйста, придумай пару вопрос-ответ в указанном формате JSON для следующего текста:
=======
Everything between the ``` must be valid json.
"""
templ2 = """Please come up with a question/answer pair, in the specified JSON format, for the following text:
>>>>>>> langchan/master
----------------
{text}"""
CHAT_PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(templ1),
        HumanMessagePromptTemplate.from_template(templ2),
    ]
)
<<<<<<< HEAD
templ = """Ты умный помощник, созданный для помощи учителям старших классов в создании вопросов для проверки понимания прочитанного.
Получив текст, ты должен придумать пару вопрос-ответ, которую можно использовать для проверки способностей ученика к пониманию прочитанного.
При создании этой пары вопрос-ответ, ты должен ответить в следующем формате:
=======
templ = """You are a smart assistant designed to help high school teachers come up with reading comprehension questions.
Given a piece of text, you must come up with a question and answer pair that can be used to test a student's reading comprehension abilities.
When coming up with this question/answer pair, you must respond in the following format:
>>>>>>> langchan/master
```
{{
    "question": "$YOUR_QUESTION_HERE",
    "answer": "$THE_ANSWER_HERE"
}}
```

<<<<<<< HEAD
Все, что находится между ``` должно быть валидным json.

Пожалуйста, придумай пару вопрос-ответ в указанном формате JSON для следующего текста:
=======
Everything between the ``` must be valid json.

Please come up with a question/answer pair, in the specified JSON format, for the following text:
>>>>>>> langchan/master
----------------
{text}"""
PROMPT = PromptTemplate.from_template(templ)

PROMPT_SELECTOR = ConditionalPromptSelector(
    default_prompt=PROMPT, conditionals=[(is_chat_model, CHAT_PROMPT)]
)
