# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
PROMPT_SUFFIX = """Используй только следующие индексы Elasticsearch:
=======
PROMPT_SUFFIX = """Only use the following Elasticsearch indices:
>>>>>>> langchan/master
{indices_info}

Question: {input}
ESQuery:"""

<<<<<<< HEAD
DEFAULT_DSL_TEMPLATE = """Получив входной вопрос, создай синтаксически правильный запрос Elasticsearch для его выполнения. Если пользователь не указывает в своем вопросе конкретное количество примеров, которые он хочет получить, всегда ограничивай свой запрос максимумом {top_k} результатов. Ты можешь упорядочить результаты по релевантной колонке, чтобы вернуть наиболее интересные примеры из базы данных.

Если не указано иное, не запрашивай все колонки из определенного индекса, запрашивай только несколько релевантных колонок, учитывая вопрос.

Обрати внимание, чтобы использовать только имена колонок, которые ты видишь в описании сопоставления. Будь осторожен, чтобы не запрашивать колонки, которые не существуют. Также обрати внимание, какая колонка находится в каком индексе. Верни запрос в виде действительного json.

Используй следующий формат:

Question: Здесь вопрос
ESQuery: Запрос Elasticsearch, отформатированный как json
=======
DEFAULT_DSL_TEMPLATE = """Given an input question, create a syntactically correct Elasticsearch query to run. Unless the user specifies in their question a specific number of examples they wish to obtain, always limit your query to at most {top_k} results. You can order the results by a relevant column to return the most interesting examples in the database.

Unless told to do not query for all the columns from a specific index, only ask for a the few relevant columns given the question.

Pay attention to use only the column names that you can see in the mapping description. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which index. Return the query as valid json.

Use the following format:

Question: Question here
ESQuery: Elasticsearch Query formatted as json
>>>>>>> langchan/master
"""

DSL_PROMPT = PromptTemplate.from_template(DEFAULT_DSL_TEMPLATE + PROMPT_SUFFIX)

<<<<<<< HEAD
DEFAULT_ANSWER_TEMPLATE = """Получив входной вопрос и релевантные данные из базы данных, ответь на вопрос пользователя.

Используй следующий формат:

Question: Здесь вопрос
Данные: Здесь релевантные данные
Answer: Здесь окончательный ответ

Question: {input}
Данные: {data}
=======
DEFAULT_ANSWER_TEMPLATE = """Given an input question and relevant data from a database, answer the user question.

Use the following format:

Question: Question here
Data: Relevant data here
Answer: Final answer here

Question: {input}
Data: {data}
>>>>>>> langchan/master
Answer:"""

ANSWER_PROMPT = PromptTemplate.from_template(DEFAULT_ANSWER_TEMPLATE)
