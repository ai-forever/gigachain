# flake8: noqa
from langchain_core.prompts import PromptTemplate

SONG_DATA_SOURCE = """\
```json
{{
<<<<<<< HEAD
    "content": "Текст песни",
    "attributes": {{
        "artist": {{
            "type": "string",
            "description": "Имя исполнителя песни"
        }},
        "length": {{
            "type": "integer",
            "description": "Длительность песни в секундах"
        }},
        "genre": {{
            "type": "string",
            "description": "Жанр песни, один из \"pop\", \"rock\" или \"rap\""
=======
    "content": "Lyrics of a song",
    "attributes": {{
        "artist": {{
            "type": "string",
            "description": "Name of the song artist"
        }},
        "length": {{
            "type": "integer",
            "description": "Length of the song in seconds"
        }},
        "genre": {{
            "type": "string",
            "description": "The song genre, one of \"pop\", \"rock\" or \"rap\""
>>>>>>> langchan/master
        }}
    }}
}}
```\
"""

FULL_ANSWER = """\
```json
{{
    "query": "teenager love",
    "filter": "and(or(eq(\\"artist\\", \\"Taylor Swift\\"), eq(\\"artist\\", \\"Katy Perry\\")), lt(\\"length\\", 180), eq(\\"genre\\", \\"pop\\"))"
}}
```\
"""

NO_FILTER_ANSWER = """\
```json
{{
    "query": "",
    "filter": "NO_FILTER"
}}
```\
"""

WITH_LIMIT_ANSWER = """\
```json
{{
    "query": "love",
    "filter": "NO_FILTER",
    "limit": 2
}}
```\
"""

DEFAULT_EXAMPLES = [
    {
        "i": 1,
        "data_source": SONG_DATA_SOURCE,
<<<<<<< HEAD
        "user_query": "Какие песни Тейлор Свифт или Кэти Перри о подростковой любви длительностью менее 3 минут в жанре поп?",
=======
        "user_query": "What are songs by Taylor Swift or Katy Perry about teenage romance under 3 minutes long in the dance pop genre",
>>>>>>> langchan/master
        "structured_request": FULL_ANSWER,
    },
    {
        "i": 2,
        "data_source": SONG_DATA_SOURCE,
<<<<<<< HEAD
        "user_query": "Какие песни не были опубликованы на Spotify",
=======
        "user_query": "What are songs that were not published on Spotify",
>>>>>>> langchan/master
        "structured_request": NO_FILTER_ANSWER,
    },
]

EXAMPLES_WITH_LIMIT = [
    {
        "i": 1,
        "data_source": SONG_DATA_SOURCE,
<<<<<<< HEAD
        "user_query": "Какие песни Тейлор Свифт или Кэти Перри о подростковой любви длительностью менее 3 минут в жанре поп?",
=======
        "user_query": "What are songs by Taylor Swift or Katy Perry about teenage romance under 3 minutes long in the dance pop genre",
>>>>>>> langchan/master
        "structured_request": FULL_ANSWER,
    },
    {
        "i": 2,
        "data_source": SONG_DATA_SOURCE,
<<<<<<< HEAD
        "user_query": "Какие песни не были опубликованы на Spotify",
=======
        "user_query": "What are songs that were not published on Spotify",
>>>>>>> langchan/master
        "structured_request": NO_FILTER_ANSWER,
    },
    {
        "i": 3,
        "data_source": SONG_DATA_SOURCE,
<<<<<<< HEAD
        "user_query": "Какие три песни о любви",
=======
        "user_query": "What are three songs about love",
>>>>>>> langchan/master
        "structured_request": WITH_LIMIT_ANSWER,
    },
]

EXAMPLE_PROMPT_TEMPLATE = """\
<<<<<<< HEAD
<< Пример {i}. >>
Источник данных:
{data_source}

Запрос пользователя:
{user_query}

Структурированный запрос:
=======
<< Example {i}. >>
Data Source:
{data_source}

User Query:
{user_query}

Structured Request:
>>>>>>> langchan/master
{structured_request}
"""

EXAMPLE_PROMPT = PromptTemplate.from_template(EXAMPLE_PROMPT_TEMPLATE)

USER_SPECIFIED_EXAMPLE_PROMPT = PromptTemplate.from_template(
    """\
<< Example {i}. >>
User Query:
{user_query}

Structured Request:
```json
{structured_request}
```
"""
)

DEFAULT_SCHEMA = """\
<<<<<<< HEAD
<< Схема структурированного запроса >>
При ответе используйте фрагмент кода markdown с объектом JSON, отформатированным по следующей схеме:

```json
{{{{
    "query": string \\ текстовая строка для сравнения с содержимым документа
    "filter": string \\ логическое условие для фильтрации документов
}}}}
```

Строка запроса должна содержать только текст, который ожидается в содержимом документов. Любые условия в фильтре не должны упоминаться в запросе.

Логическое условие состоит из одного или нескольких операторов сравнения и логических операций.

Оператор сравнения имеет форму: `comp(attr, val)`:
- `comp` ({allowed_comparators}): оператор сравнения
- `attr` (string):  имя атрибута, к которому применяется сравнение
- `val` (string): значение для сравнения

Логическая операция имеет форму `op(statement1, statement2, ...)`:
- `op` ({allowed_operators}): логический оператор
- `statement1`, `statement2`, ... (операторы сравнения или логические операции): одно или несколько утверждений, к которым применяется операция

Убедитесь, что вы используете только перечисленные выше операторы сравнения и логические операторы и никакие другие.
Убедитесь, что фильтры относятся только к атрибутам, которые существуют в источнике данных.
Убедитесь, что фильтры используют только имена атрибутов с их именами функций, если на них применяются функции.
Убедитесь, что фильтры используют только формат `YYYY-MM-DD` при обработке значений типа данных временной метки.
Убедитесь, что фильтры учитывают описания атрибутов и делают только те сравнения, которые возможны с учетом типа хранимых данных.
Убедитесь, что фильтры используются только по мере необходимости. Если нет фильтров, которые следует применить, верните "NO_FILTER" для значения фильтра.\
=======
<< Structured Request Schema >>
When responding use a markdown code snippet with a JSON object formatted in the following schema:

```json
{{{{
    "query": string \\ text string to compare to document contents
    "filter": string \\ logical condition statement for filtering documents
}}}}
```

The query string should contain only text that is expected to match the contents of documents. Any conditions in the filter should not be mentioned in the query as well.

A logical condition statement is composed of one or more comparison and logical operation statements.

A comparison statement takes the form: `comp(attr, val)`:
- `comp` ({allowed_comparators}): comparator
- `attr` (string):  name of attribute to apply the comparison to
- `val` (string): is the comparison value

A logical operation statement takes the form `op(statement1, statement2, ...)`:
- `op` ({allowed_operators}): logical operator
- `statement1`, `statement2`, ... (comparison statements or logical operation statements): one or more statements to apply the operation to

Make sure that you only use the comparators and logical operators listed above and no others.
Make sure that filters only refer to attributes that exist in the data source.
Make sure that filters only use the attributed names with its function names if there are functions applied on them.
Make sure that filters only use format `YYYY-MM-DD` when handling date data typed values.
Make sure that filters take into account the descriptions of attributes and only make comparisons that are feasible given the type of data being stored.
Make sure that filters are only used as needed. If there are no filters that should be applied return "NO_FILTER" for the filter value.\
>>>>>>> langchan/master
"""
DEFAULT_SCHEMA_PROMPT = PromptTemplate.from_template(DEFAULT_SCHEMA)

SCHEMA_WITH_LIMIT = """\
<<<<<<< HEAD
<< Схема структурированного запроса >>
При ответе используйте фрагмент кода markdown с объектом JSON, отформатированным по следующей схеме:

```json
{{{{
    "query": string \\ текстовая строка для сравнения с содержимым документа
    "filter": string \\ логическое условие для фильтрации документов
    "limit": int \\ количество документов для извлечения
}}}}
```

Строка запроса должна содержать только текст, который ожидается в содержимом документов. Любые условия в фильтре не должны упоминаться в запросе.

Логическое условие состоит из одного или нескольких операторов сравнения и логических операций.

Оператор сравнения имеет форму: `comp(attr, val)`:
- `comp` ({allowed_comparators}): оператор сравнения
- `attr` (string):  имя атрибута, к которому применяется сравнение
- `val` (string): значение для сравнения

Логическая операция имеет форму `op(statement1, statement2, ...)`:
- `op` ({allowed_operators}): логический оператор
- `statement1`, `statement2`, ... (операторы сравнения или логические операции): одно или несколько утверждений, к которым применяется операция

Убедитесь, что вы используете только перечисленные выше операторы сравнения и логические операторы и никакие другие.
Убедитесь, что фильтры относятся только к атрибутам, которые существуют в источнике данных.
Убедитесь, что фильтры используют только имена атрибутов с их именами функций, если на них применяются функции.
Убедитесь, что фильтры используют только формат `YYYY-MM-DD` при обработке значений типа данных временной метки.
Убедитесь, что фильтры учитывают описания атрибутов и делают только те сравнения, которые возможны с учетом типа хранимых данных.
Убедитесь, что фильтры используются только по мере необходимости. Если нет фильтров, которые следует применить, верните "NO_FILTER" для значения фильтра.
Убедитесь, что `limit` всегда является целым числом. Это необязательный параметр, поэтому оставьте его пустым, если он не имеет смысла.
=======
<< Structured Request Schema >>
When responding use a markdown code snippet with a JSON object formatted in the following schema:

```json
{{{{
    "query": string \\ text string to compare to document contents
    "filter": string \\ logical condition statement for filtering documents
    "limit": int \\ the number of documents to retrieve
}}}}
```

The query string should contain only text that is expected to match the contents of documents. Any conditions in the filter should not be mentioned in the query as well.

A logical condition statement is composed of one or more comparison and logical operation statements.

A comparison statement takes the form: `comp(attr, val)`:
- `comp` ({allowed_comparators}): comparator
- `attr` (string):  name of attribute to apply the comparison to
- `val` (string): is the comparison value

A logical operation statement takes the form `op(statement1, statement2, ...)`:
- `op` ({allowed_operators}): logical operator
- `statement1`, `statement2`, ... (comparison statements or logical operation statements): one or more statements to apply the operation to

Make sure that you only use the comparators and logical operators listed above and no others.
Make sure that filters only refer to attributes that exist in the data source.
Make sure that filters only use the attributed names with its function names if there are functions applied on them.
Make sure that filters only use format `YYYY-MM-DD` when handling date data typed values.
Make sure that filters take into account the descriptions of attributes and only make comparisons that are feasible given the type of data being stored.
Make sure that filters are only used as needed. If there are no filters that should be applied return "NO_FILTER" for the filter value.
Make sure the `limit` is always an int value. It is an optional parameter so leave it blank if it does not make sense.
>>>>>>> langchan/master
"""
SCHEMA_WITH_LIMIT_PROMPT = PromptTemplate.from_template(SCHEMA_WITH_LIMIT)

DEFAULT_PREFIX = """\
<<<<<<< HEAD
Твоя задача - структурировать запрос пользователя, чтобы он соответствовал схеме запроса, представленной ниже.
=======
Your goal is to structure the user's query to match the request schema provided below.
>>>>>>> langchan/master

{schema}\
"""

PREFIX_WITH_DATA_SOURCE = (
    DEFAULT_PREFIX
    + """

<< Data Source >>
```json
{{{{
    "content": "{content}",
    "attributes": {attributes}
}}}}
```
"""
)

DEFAULT_SUFFIX = """\
<<<<<<< HEAD
<< Пример {i}. >>
Источник данных:
=======
<< Example {i}. >>
Data Source:
>>>>>>> langchan/master
```json
{{{{
    "content": "{content}",
    "attributes": {attributes}
}}}}
```

<<<<<<< HEAD
Запрос пользователя:
{{query}}

Структурированный запрос:
"""

SUFFIX_WITHOUT_DATA_SOURCE = """\
<< Пример {i}. >>
Запрос пользователя:
{{query}}

Структурированный запрос:
=======
User Query:
{{query}}

Structured Request:
"""

SUFFIX_WITHOUT_DATA_SOURCE = """\
<< Example {i}. >>
User Query:
{{query}}

Structured Request:
>>>>>>> langchan/master
"""
