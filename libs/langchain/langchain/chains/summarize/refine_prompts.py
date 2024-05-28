from langchain_core.prompts import PromptTemplate

<<<<<<< HEAD
REFINE_PROMPT_TMPL = (
    "Твоя задача - создать окончательное резюме\n"
    "Мы предоставили существующее резюме до определенного момента: {existing_answer}\n"
    "У нас есть возможность улучшить существующее резюме"
    "(только если это необходимо) с некоторым дополнительным контекстом ниже.\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "Учитывая новый контекст, улучши оригинальное резюме\n"
    "Если контекст не полезен, верни оригинальное резюме."
)
REFINE_PROMPT = PromptTemplate(
    input_variables=["existing_answer", "text"],
    template=REFINE_PROMPT_TMPL,
)


prompt_template = """Напиши краткое резюме следующего:
=======
REFINE_PROMPT_TMPL = """\
Your job is to produce a final summary.
We have provided an existing summary up to a certain point: {existing_answer}
We have the opportunity to refine the existing summary (only if needed) with some more context below.
------------
{text}
------------
Given the new context, refine the original summary.
If the context isn't useful, return the original summary.\
"""  # noqa: E501
REFINE_PROMPT = PromptTemplate.from_template(REFINE_PROMPT_TMPL)


prompt_template = """Write a concise summary of the following:
>>>>>>> langchan/master


"{text}"


<<<<<<< HEAD
КРАТКОЕ РЕЗЮМЕ:"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
=======
CONCISE SUMMARY:"""
PROMPT = PromptTemplate.from_template(prompt_template)
>>>>>>> langchan/master
