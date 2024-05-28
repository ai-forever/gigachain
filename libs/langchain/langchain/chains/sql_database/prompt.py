# flake8: noqa
from langchain_core.output_parsers.list import CommaSeparatedListOutputParser
from langchain_core.prompts.prompt import PromptTemplate


<<<<<<< HEAD
PROMPT_SUFFIX = """Используйте только следующие таблицы:
=======
PROMPT_SUFFIX = """Only use the following tables:
>>>>>>> langchan/master
{table_info}

Question: {input}"""

<<<<<<< HEAD
_DEFAULT_TEMPLATE = """По заданному вопросу сначала создайте синтаксически правильный запрос на {dialect}, затем просмотрите результаты запроса и верните ответ. Если пользователь не указывает конкретное количество примеров, которые он хочет получить, всегда ограничивайте свой запрос не более чем {top_k} результатами. Вы можете упорядочить результаты по соответствующему столбцу, чтобы вернуть наиболее интересные примеры в базе данных.

Никогда не запрашивайте все столбцы из конкретной таблицы, запрашивайте только несколько необходимых столбцов, исходя из вопроса.

Обратите внимание, что используются только имена столбцов, которые вы видите в описании схемы. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer. Unless the user specifies in his question a specific number of examples he wishes to obtain, always limit your query to at most {top_k} results. You can order the results by a relevant column to return the most interesting examples in the database.

Never query for all the columns from a specific table, only ask for a the few relevant columns given the question.

Pay attention to use only the column names that you can see in the schema description. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "dialect", "top_k"],
    template=_DEFAULT_TEMPLATE + PROMPT_SUFFIX,
)


<<<<<<< HEAD
_DECIDER_TEMPLATE = """По заданному вопросу и списку потенциальных таблиц выведите список имен таблиц, разделенных запятыми, которые могут понадобиться для ответа на этот вопрос.

Question: {query}

Имена таблиц: {table_names}

Соответствующие имена таблиц:"""
=======
_DECIDER_TEMPLATE = """Given the below input question and list of potential tables, output a comma separated list of the table names that may be necessary to answer this question.

Question: {query}

Table Names: {table_names}

Relevant Table Names:"""
>>>>>>> langchan/master
DECIDER_PROMPT = PromptTemplate(
    input_variables=["query", "table_names"],
    template=_DECIDER_TEMPLATE,
    output_parser=CommaSeparatedListOutputParser(),
)

<<<<<<< HEAD
_cratedb_prompt = """Вы являетесь экспертом по CrateDB. По заданному вопросу сначала создайте синтаксически правильный запрос CrateDB для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в CrateDB. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в двойные кавычки (") для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию CURRENT_DATE.

Regenerate

Use the following format:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_cratedb_prompt = """You are a CrateDB expert. Given an input question, first create a syntactically correct CrateDB query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per CrateDB. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURRENT_DATE function to get the current date, if the question involves "today". 

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

CRATEDB_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_cratedb_prompt + PROMPT_SUFFIX,
)

<<<<<<< HEAD
_duckdb_prompt = """Вы являетесь экспертом по DuckDB. По заданному вопросу сначала создайте синтаксически правильный запрос DuckDB для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в DuckDB. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в двойные кавычки (") для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию today.

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ

"""

CRATEDB_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_cratedb_prompt + PROMPT_SUFFIX,
)

_duckdb_prompt = """Вы являетесь экспертом по DuckDB. По заданному вопросу сначала создайте синтаксически правильный запрос DuckDB для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в DuckDB. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в двойные кавычки (") для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию today.

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_duckdb_prompt = """You are a DuckDB expert. Given an input question, first create a syntactically correct DuckDB query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per DuckDB. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use today() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

DUCKDB_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_duckdb_prompt + PROMPT_SUFFIX,
)

<<<<<<< HEAD
_googlesql_prompt = """Вы являетесь экспертом по GoogleSQL. По заданному вопросу сначала создайте синтаксически правильный запрос GoogleSQL для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в GoogleSQL. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в обратные кавычки (`) для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию CURRENT_DATE().

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_googlesql_prompt = """You are a GoogleSQL expert. Given an input question, first create a syntactically correct GoogleSQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per GoogleSQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURRENT_DATE() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

GOOGLESQL_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_googlesql_prompt + PROMPT_SUFFIX,
)


<<<<<<< HEAD
_mssql_prompt = """Вы являетесь экспертом по MS SQL. По заданному вопросу сначала создайте синтаксически правильный запрос MS SQL для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово TOP, как в MS SQL. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в квадратные скобки ([]) для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию CAST(GETDATE() as date).

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_mssql_prompt = """You are an MS SQL expert. Given an input question, first create a syntactically correct MS SQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the TOP clause as per MS SQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in square brackets ([]) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CAST(GETDATE() as date) function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

MSSQL_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_mssql_prompt + PROMPT_SUFFIX,
)


<<<<<<< HEAD
_mysql_prompt = """Вы являетесь экспертом по MySQL. По заданному вопросу сначала создайте синтаксически правильный запрос MySQL для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в MySQL. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в обратные кавычки (`) для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию CURDATE().

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURDATE() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

MYSQL_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_mysql_prompt + PROMPT_SUFFIX,
)


<<<<<<< HEAD
_mariadb_prompt = """Вы являетесь экспертом по MariaDB. По заданному вопросу сначала создайте синтаксически правильный запрос MariaDB для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в MariaDB. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в обратные кавычки (`) для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию CURDATE().

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_mariadb_prompt = """You are a MariaDB expert. Given an input question, first create a syntactically correct MariaDB query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MariaDB. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURDATE() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

MARIADB_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_mariadb_prompt + PROMPT_SUFFIX,
)


<<<<<<< HEAD
_oracle_prompt = """Вы являетесь экспертом по Oracle SQL. По заданному вопросу сначала создайте синтаксически правильный запрос Oracle SQL для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово FETCH FIRST n ROWS ONLY, как в Oracle SQL. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в двойные кавычки (") для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию TRUNC(SYSDATE).

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_oracle_prompt = """You are an Oracle SQL expert. Given an input question, first create a syntactically correct Oracle SQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the FETCH FIRST n ROWS ONLY clause as per Oracle SQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use TRUNC(SYSDATE) function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

ORACLE_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_oracle_prompt + PROMPT_SUFFIX,
)


<<<<<<< HEAD
_postgres_prompt = """Вы являетесь экспертом по PostgreSQL. По заданному вопросу сначала создайте синтаксически правильный запрос PostgreSQL для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в PostgreSQL. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в двойные кавычки (") для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию CURRENT_DATE.

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_postgres_prompt = """You are a PostgreSQL expert. Given an input question, first create a syntactically correct PostgreSQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per PostgreSQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURRENT_DATE function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

POSTGRES_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_postgres_prompt + PROMPT_SUFFIX,
)


<<<<<<< HEAD
_sqlite_prompt = """Вы являетесь экспертом по SQLite. По заданному вопросу сначала создайте синтаксически правильный запрос SQLite для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в SQLite. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в двойные кавычки (") для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию date('now').

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_sqlite_prompt = """You are a SQLite expert. Given an input question, first create a syntactically correct SQLite query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per SQLite. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use date('now') function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
>>>>>>> langchan/master

"""

SQLITE_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_sqlite_prompt + PROMPT_SUFFIX,
)

<<<<<<< HEAD
_clickhouse_prompt = """Вы являетесь экспертом по ClickHouse. По заданному вопросу сначала создайте синтаксически правильный запрос ClickHouse для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в ClickHouse. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в двойные кавычки (") для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию today().

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_clickhouse_prompt = """You are a ClickHouse expert. Given an input question, first create a syntactically correct Clic query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per ClickHouse. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use today() function to get the current date, if the question involves "today".

Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"
>>>>>>> langchan/master

"""

CLICKHOUSE_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_clickhouse_prompt + PROMPT_SUFFIX,
)

<<<<<<< HEAD
_prestodb_prompt = """Вы являетесь экспертом по PrestoDB. По заданному вопросу сначала создайте синтаксически правильный запрос PrestoDB для выполнения, затем просмотрите результаты запроса и верните ответ на входной вопрос.
Если пользователь не указывает в вопросе конкретное количество примеров для получения, запрашивайте не более {top_k} результатов, используя ключевое слово LIMIT, как в PrestoDB. Вы можете упорядочить результаты, чтобы вернуть наиболее информативные данные в базе данных.
Никогда не запрашивайте все столбцы из таблицы. Вы должны запрашивать только те столбцы, которые необходимы для ответа на вопрос. Оберните каждое имя столбца в двойные кавычки (") для обозначения их как ограниченных идентификаторов.
Обратите внимание, что используются только имена столбцов, которые вы видите в таблицах ниже. Будьте внимательны, чтобы не запрашивать столбцы, которых не существует. Также обратите внимание, какой столбец находится в какой таблице.
Обратите внимание, что для получения текущей даты, если вопрос связан с "сегодня", используйте функцию current_date.

Используйте следующий формат:

Question: Вопрос
SQLQuery: SQL-запрос для выполнения
SQLResult: Разультат выполнения запроса
Answer: Итоговый ответ
=======
_prestodb_prompt = """You are a PrestoDB expert. Given an input question, first create a syntactically correct PrestoDB query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per PrestoDB. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use current_date function to get the current date, if the question involves "today".

Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"
>>>>>>> langchan/master

"""

PRESTODB_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_prestodb_prompt + PROMPT_SUFFIX,
)


SQL_PROMPTS = {
    "crate": CRATEDB_PROMPT,
    "duckdb": DUCKDB_PROMPT,
    "googlesql": GOOGLESQL_PROMPT,
    "mssql": MSSQL_PROMPT,
    "mysql": MYSQL_PROMPT,
    "mariadb": MARIADB_PROMPT,
    "oracle": ORACLE_PROMPT,
    "postgresql": POSTGRES_PROMPT,
    "sqlite": SQLITE_PROMPT,
    "clickhouse": CLICKHOUSE_PROMPT,
    "prestodb": PRESTODB_PROMPT,
}
