# flake8: noqa
from langchain_core.prompts import PromptTemplate

<<<<<<< HEAD
prompt_template = """Напиши краткое резюме следующего:
=======
prompt_template = """Write a concise summary of the following:
>>>>>>> langchan/master


"{text}"


<<<<<<< HEAD
КРАТКОЕ РЕЗЮМЕ:"""
=======
CONCISE SUMMARY:"""
>>>>>>> langchan/master
PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
