# flake8: noqa
from langchain.output_parsers.regex import RegexParser
from langchain_core.prompts import PromptTemplate

<<<<<<< HEAD
template = """Ты учитель, который составляет вопросы для викторины. 
Исходя из следующего документа, пожалуйста, сформулируй вопрос и ответ, основанные на этом документе.

Пример формата:
<Начало документа>
...
<Конец документа>
ВОПРОС: вопрос здесь
ОТВЕТ: ответ здесь

Эти вопросы должны быть подробными и строго основываться на информации в документе. Начни!

<Начало документа>
{doc}
<Конец документа>"""
=======
template = """You are a teacher coming up with questions to ask on a quiz. 
Given the following document, please generate a question and answer based on that document.

Example Format:
<Begin Document>
...
<End Document>
QUESTION: question here
ANSWER: answer here

These questions should be detailed and be based explicitly on information in the document. Begin!

<Begin Document>
{doc}
<End Document>"""
>>>>>>> langchan/master
PROMPT = PromptTemplate(
    input_variables=["doc"],
    template=template,
)
