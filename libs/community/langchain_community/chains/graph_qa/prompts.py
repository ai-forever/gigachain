# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """Извлеките все сущности из следующего текста. В качестве руководства, собственное имя обычно пишется с заглавной буквы. Вы должны обязательно извлечь все имена и места.

Верните результат в виде одного списка, разделенного запятыми, или NONE, если нет ничего интересного для возврата.

ПРИМЕР
Я пытаюсь улучшить интерфейсы Langchain, UX, его интеграции с различными продуктами, которые может захотеть пользователь ... много всего.
Вывод: Langchain
КОНЕЦ ПРИМЕРА

ПРИМЕР
Я пытаюсь улучшить интерфейсы Langchain, UX, его интеграции с различными продуктами, которые может захотеть пользователь ... много всего. Я работаю с Сэмом.
Вывод: Langchain, Сэм
КОНЕЦ ПРИМЕРА

Начните!

{input}
Вывод:"""
=======
_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """Extract all entities from the following text. As a guideline, a proper noun is generally capitalized. You should definitely extract all names and places.

Return the output as a single comma-separated list, or NONE if there is nothing of note to return.

EXAMPLE
i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff.
Output: Langchain
END OF EXAMPLE

EXAMPLE
i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff. I'm working with Sam.
Output: Langchain, Sam
END OF EXAMPLE

Begin!

{input}
Output:"""
>>>>>>> langchan/master
ENTITY_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["input"], template=_DEFAULT_ENTITY_EXTRACTION_TEMPLATE
)

<<<<<<< HEAD
_DEFAULT_GRAPH_QA_TEMPLATE = """Используйте следующие тройки знаний, чтобы ответить на вопрос в конце. Если вы не знаете ответа, просто скажите, что не знаете, не пытайтесь придумать ответ.
=======
_DEFAULT_GRAPH_QA_TEMPLATE = """Use the following knowledge triplets to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
>>>>>>> langchan/master

{context}

Question: {question}
Helpful Answer:"""
GRAPH_QA_PROMPT = PromptTemplate(
    template=_DEFAULT_GRAPH_QA_TEMPLATE, input_variables=["context", "question"]
)

<<<<<<< HEAD
CYPHER_GENERATION_TEMPLATE = """Задача: Сгенерировать выражение Cypher для запроса к графовой базе данных.
Инструкции:
Используйте только предоставленные типы отношений и свойства в схеме.
Не используйте другие типы отношений или свойства, которые не предоставлены.
Схема:
{schema}
Примечание: Не включайте в ответ никаких пояснений или извинений.
Не отвечайте на вопросы, которые могут просить о чем-то, кроме создания выражения Cypher.
Не включайте в ответ никакой текст, кроме сгенерированного выражения Cypher.

Question:
=======
CYPHER_GENERATION_TEMPLATE = """Task:Generate Cypher statement to query a graph database.
Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Schema:
{schema}
Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

The question is:
>>>>>>> langchan/master
{question}"""
CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)

NEBULAGRAPH_EXTRA_INSTRUCTIONS = """
<<<<<<< HEAD
Инструкции:

Сначала сгенерируйте выражение Cypher, а затем преобразуйте его в диалект NebulaGraph Cypher (а не стандартный):
1. требуется явное указание метки только при ссылке на свойства узла: v.`Foo`.name
2. обратите внимание, что явное указание метки не требуется для свойств ребра, поэтому это e.name вместо e.`Bar`.name
3. для сравнения используется двойной знак равенства: `==` вместо `=`
Например:
=======
Instructions:

First, generate cypher then convert it to NebulaGraph Cypher dialect(rather than standard):
1. it requires explicit label specification only when referring to node properties: v.`Foo`.name
2. note explicit label specification is not needed for edge properties, so it's e.name instead of e.`Bar`.name
3. it uses double equals sign for comparison: `==` rather than `=`
For instance:
>>>>>>> langchan/master
```diff
< MATCH (p:person)-[e:directed]->(m:movie) WHERE m.name = 'The Godfather II'
< RETURN p.name, e.year, m.name;
---
> MATCH (p:`person`)-[e:directed]->(m:`movie`) WHERE m.`movie`.`name` == 'The Godfather II'
> RETURN p.`person`.`name`, e.year, m.`movie`.`name`;
```\n"""

NGQL_GENERATION_TEMPLATE = CYPHER_GENERATION_TEMPLATE.replace(
    "Generate Cypher", "Generate NebulaGraph Cypher"
).replace("Instructions:", NEBULAGRAPH_EXTRA_INSTRUCTIONS)

NGQL_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=NGQL_GENERATION_TEMPLATE
)

KUZU_EXTRA_INSTRUCTIONS = """
<<<<<<< HEAD
Инструкции:

Сгенерируйте выражение с диалектом Kùzu Cypher (а не стандартным):
1. не используйте оператор `WHERE EXISTS` для проверки наличия свойства, потому что у базы данных Kùzu есть фиксированная схема.
2. не опускайте шаблон отношения. Всегда используйте `()-[]->()` вместо `()->()`.
3. не включайте никаких замечаний или комментариев, даже если выражение не дает ожидаемого результата.
```\n"""
=======
Instructions:
Generate the Kùzu dialect of Cypher with the following rules in mind:
1. Do not omit the relationship pattern. Always use `()-[]->()` instead of `()->()`.
2. Do not include triple backticks ``` in your response. Return only Cypher.
3. Do not return any notes or comments in your response.
\n"""
>>>>>>> langchan/master

KUZU_GENERATION_TEMPLATE = CYPHER_GENERATION_TEMPLATE.replace(
    "Generate Cypher", "Generate Kùzu Cypher"
).replace("Instructions:", KUZU_EXTRA_INSTRUCTIONS)

KUZU_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=KUZU_GENERATION_TEMPLATE
)

GREMLIN_GENERATION_TEMPLATE = CYPHER_GENERATION_TEMPLATE.replace("Cypher", "Gremlin")

GREMLIN_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=GREMLIN_GENERATION_TEMPLATE
)

<<<<<<< HEAD
CYPHER_QA_TEMPLATE = """Вы - помощник, который помогает формировать понятные и человекочитаемые ответы.
Часть с информацией содержит предоставленную информацию, которую вы должны использовать для составления ответа.
Предоставленная информация является авторитетной, вы никогда не должны сомневаться в ней или пытаться использовать свои внутренние знания для ее корректировки.
Сделайте ответ звучать как ответ на вопрос. Не упоминайте, что вы основываетесь на предоставленной информации.
Если предоставленная информация пуста, скажите, что не знаете ответа.
Информация:
"""

CYPHER_QA_TEMPLATE = """ы - помощник, который помогает формировать понятные и человекочитаемые ответы.
Часть с информацией содержит предоставленную информацию, которую вы должны использовать для составления ответа.
Предоставленная информация является авторитетной, вы никогда не должны сомневаться в ней или пытаться использовать свои внутренние знания для ее корректировки.
Сделайте ответ звучать как ответ на вопрос. Не упоминайте, что вы основываетесь на предоставленной информации.
Если предоставленная информация пуста, скажите, что не знаете ответа.
Пример:

Question: Какие менеджеры владеют акциями Neo4j?
Context:[manager:CTL LLC, manager:JANE STREET GROUP LLC]
Helpful Answer: CTL LLC, JANE STREET GROUP LLC владеют акциями Neo4j.

Следуйте этому примеру при генерации ответов.
Если предоставленная информация пуста, скажите, что не знаете ответа.
Context:{context}
=======
CYPHER_QA_TEMPLATE = """You are an assistant that helps to form nice and human understandable answers.
The information part contains the provided information that you must use to construct an answer.
The provided information is authoritative, you must never doubt it or try to use your internal knowledge to correct it.
Make the answer sound as a response to the question. Do not mention that you based the result on the given information.
Here is an example:

Question: Which managers own Neo4j stocks?
Context:[manager:CTL LLC, manager:JANE STREET GROUP LLC]
Helpful Answer: CTL LLC, JANE STREET GROUP LLC owns Neo4j stocks.

Follow this example when generating answers.
If the provided information is empty, say that you don't know the answer.
Information:
{context}

>>>>>>> langchan/master
Question: {question}
Helpful Answer:"""
CYPHER_QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"], template=CYPHER_QA_TEMPLATE
)

<<<<<<< HEAD
SPARQL_INTENT_TEMPLATE = """Задача: Определить намерение запроса SPARQL по промпту и вернуть соответствующий тип запроса SPARQL.
Вы - помощник, который различает разные типы запросов и возвращает соответствующие типы запросов SPARQL.
Учитывайте только следующие типы запросов:
* SELECT: этот тип запроса соответствует вопросам
* UPDATE: этот тип запроса соответствует всем запросам на удаление, вставку или изменение троек
Примечание: Будьте максимально краткими.
Не включайте в ответ никаких пояснений или извинений.
Не отвечайте на вопросы, которые просят о чем-то, кроме определения типа запроса SPARQL.
Не включайте никаких ненужных пробелов или текста, кроме типа запроса, то есть либо верните 'SELECT', либо 'UPDATE'.

Промпт:
=======
SPARQL_INTENT_TEMPLATE = """Task: Identify the intent of a prompt and return the appropriate SPARQL query type.
You are an assistant that distinguishes different types of prompts and returns the corresponding SPARQL query types.
Consider only the following query types:
* SELECT: this query type corresponds to questions
* UPDATE: this query type corresponds to all requests for deleting, inserting, or changing triples
Note: Be as concise as possible.
Do not include any explanations or apologies in your responses.
Do not respond to any questions that ask for anything else than for you to identify a SPARQL query type.
Do not include any unnecessary whitespaces or any text except the query type, i.e., either return 'SELECT' or 'UPDATE'.

The prompt is:
>>>>>>> langchan/master
{prompt}
Helpful Answer:"""
SPARQL_INTENT_PROMPT = PromptTemplate(
    input_variables=["prompt"], template=SPARQL_INTENT_TEMPLATE
)

<<<<<<< HEAD
SPARQL_GENERATION_SELECT_TEMPLATE = """Задача: Сгенерировать выражение SPARQL SELECT для запроса к графовой базе данных.
Например, чтобы найти все адреса электронной почты Джона Доу, следующий запрос в обратных кавычках будет подходящим:
=======
SPARQL_GENERATION_SELECT_TEMPLATE = """Task: Generate a SPARQL SELECT statement for querying a graph database.
For instance, to find all email addresses of John Doe, the following query in backticks would be suitable:
>>>>>>> langchan/master
```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?email
WHERE {{
    ?person foaf:name "John Doe" .
    ?person foaf:mbox ?email .
}}
```
<<<<<<< HEAD
Инструкции:
Используйте только типы узлов и свойства, предоставленные в схеме.
Не используйте никакие типы узлов и свойства, которые не являются явно предоставленными.
Включите все необходимые префиксы.
Схема:
{schema}
Примечание: Будьте максимально краткими.
Не включайте в ответ никаких пояснений или извинений.
Не отвечайте на вопросы, которые просят о чем-то, кроме создания запроса SPARQL.
Не включайте никакой текст, кроме сгенерированного запроса SPARQL.

Question:
=======
Instructions:
Use only the node types and properties provided in the schema.
Do not use any node types and properties that are not explicitly provided.
Include all necessary prefixes.
Schema:
{schema}
Note: Be as concise as possible.
Do not include any explanations or apologies in your responses.
Do not respond to any questions that ask for anything else than for you to construct a SPARQL query.
Do not include any text except the SPARQL query generated.

The question is:
>>>>>>> langchan/master
{prompt}"""
SPARQL_GENERATION_SELECT_PROMPT = PromptTemplate(
    input_variables=["schema", "prompt"], template=SPARQL_GENERATION_SELECT_TEMPLATE
)

<<<<<<< HEAD
SPARQL_GENERATION_UPDATE_TEMPLATE = """Задача: Сгенерировать выражение SPARQL UPDATE для обновления графовой базы данных.
Например, чтобы добавить 'jane.doe@foo.bar' в качестве нового адреса электронной почты для Джейн Доу, следующий запрос в обратных кавычках будет подходящим:
=======
SPARQL_GENERATION_UPDATE_TEMPLATE = """Task: Generate a SPARQL UPDATE statement for updating a graph database.
For instance, to add 'jane.doe@foo.bar' as a new email address for Jane Doe, the following query in backticks would be suitable:
>>>>>>> langchan/master
```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
INSERT {{
    ?person foaf:mbox <mailto:jane.doe@foo.bar> .
}}
WHERE {{
    ?person foaf:name "Jane Doe" .
}}
```
<<<<<<< HEAD
Инструкции:
Сделайте запрос как можно короче и избегайте добавления ненужных троек.
Используйте только типы узлов и свойства, предоставленные в схеме.
Не используйте никакие типы узлов и свойства, которые не являются явно предоставленными.
Включите все необходимые префиксы.
Схема:
{schema}
Примечание: Будьте максимально краткими.
Не включайте в ответ никаких пояснений или извинений.
Не отвечайте на вопросы, которые просят о чем-то, кроме создания запроса SPARQL.
Верните только сгенерированный запрос SPARQL, ничего больше.

Информация для вставки:
=======
Instructions:
Make the query as short as possible and avoid adding unnecessary triples.
Use only the node types and properties provided in the schema.
Do not use any node types and properties that are not explicitly provided.
Include all necessary prefixes.
Schema:
{schema}
Note: Be as concise as possible.
Do not include any explanations or apologies in your responses.
Do not respond to any questions that ask for anything else than for you to construct a SPARQL query.
Return only the generated SPARQL query, nothing else.

The information to be inserted is:
>>>>>>> langchan/master
{prompt}"""
SPARQL_GENERATION_UPDATE_PROMPT = PromptTemplate(
    input_variables=["schema", "prompt"], template=SPARQL_GENERATION_UPDATE_TEMPLATE
)

<<<<<<< HEAD
SPARQL_QA_TEMPLATE = """Задача: Сгенерировать естественноязыковой ответ на основе результатов запроса SPARQL.
Вы - помощник, который создает хорошо написанные и понятные человеку ответы.
Часть с информацией содержит предоставленную информацию, которую вы можете использовать для составления ответа.
Предоставленная информация является авторитетной, вы никогда не должны сомневаться в ней или пытаться использовать свои внутренние знания для ее корректировки.
Сделайте ответ звучать так, как будто информация поступает от помощника по искусственному интеллекту, но не добавляйте никакую информацию.
Информация:
=======
SPARQL_QA_TEMPLATE = """Task: Generate a natural language response from the results of a SPARQL query.
You are an assistant that creates well-written and human understandable answers.
The information part contains the information provided, which you can use to construct an answer.
The information provided is authoritative, you must never doubt it or try to use your internal knowledge to correct it.
Make your response sound like the information is coming from an AI assistant, but don't add any information.
Information:
>>>>>>> langchan/master
{context}

Question: {prompt}
Helpful Answer:"""
SPARQL_QA_PROMPT = PromptTemplate(
    input_variables=["context", "prompt"], template=SPARQL_QA_TEMPLATE
)

GRAPHDB_SPARQL_GENERATION_TEMPLATE = """
Write a SPARQL SELECT query for querying a graph database.
The ontology schema delimited by triple backticks in Turtle format is:
```
{schema}
```
Use only the classes and properties provided in the schema to construct the SPARQL query.
Do not use any classes or properties that are not explicitly provided in the SPARQL query.
Include all necessary prefixes.
Do not include any explanations or apologies in your responses.
Do not wrap the query in backticks.
Do not include any text except the SPARQL query generated.
The question delimited by triple backticks is:
```
{prompt}
```
"""
GRAPHDB_SPARQL_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "prompt"],
    template=GRAPHDB_SPARQL_GENERATION_TEMPLATE,
)

GRAPHDB_SPARQL_FIX_TEMPLATE = """
This following SPARQL query delimited by triple backticks
```
{generated_sparql}
```
is not valid.
The error delimited by triple backticks is
```
{error_message}
```
Give me a correct version of the SPARQL query.
Do not change the logic of the query.
Do not include any explanations or apologies in your responses.
Do not wrap the query in backticks.
Do not include any text except the SPARQL query generated.
The ontology schema delimited by triple backticks in Turtle format is:
```
{schema}
```
"""

GRAPHDB_SPARQL_FIX_PROMPT = PromptTemplate(
    input_variables=["error_message", "generated_sparql", "schema"],
    template=GRAPHDB_SPARQL_FIX_TEMPLATE,
)

GRAPHDB_QA_TEMPLATE = """Task: Generate a natural language response from the results of a SPARQL query.
You are an assistant that creates well-written and human understandable answers.
The information part contains the information provided, which you can use to construct an answer.
The information provided is authoritative, you must never doubt it or try to use your internal knowledge to correct it.
Make your response sound like the information is coming from an AI assistant, but don't add any information.
Don't use internal knowledge to answer the question, just say you don't know if no information is available.
Information:
{context}

Question: {prompt}
Helpful Answer:"""
GRAPHDB_QA_PROMPT = PromptTemplate(
    input_variables=["context", "prompt"], template=GRAPHDB_QA_TEMPLATE
)

<<<<<<< HEAD
AQL_GENERATION_TEMPLATE = """Задача: Сгенерировать запрос на языке ArangoDB Query Language (AQL) из пользовательского ввода.

Вы - эксперт по языку запросов ArangoDB Query Language (AQL), ответственный за перевод `Пользовательского ввода` в запрос на языке ArangoDB Query Language (AQL).

Вам предоставлена `Схема ArangoDB`. Это JSON-объект, содержащий:
1. `Схему графа`: Список всех графов в базе данных ArangoDB вместе с их отношениями ребер.
2. `Схему коллекции`: Список всех коллекций в базе данных ArangoDB вместе с их свойствами документов/ребер и примером документа/ребра.

Вам также могут быть предоставлены наборы `Примеров запросов AQL` для помощи в создании `Запроса AQL`. Если они предоставлены, `Примеры запросов AQL` должны использоваться в качестве справочного материала, аналогично тому, как должна использоваться `Схема ArangoDB`.

Что вы должны делать:
- Думайте поэтапно.
- Ориентируйтесь на `Схему ArangoDB` и `Примеры запросов AQL` (если они предоставлены), чтобы сгенерировать запрос.
- Начните `Запрос AQL` с ключевого слова `WITH`, чтобы указать все необходимые коллекции ArangoDB.
- Верните `Запрос AQL`, заключенный в 3 обратные кавычки (```).
- Используйте только предоставленные типы отношений и свойства в `Схеме ArangoDB` и любых запросах `Примеров запросов AQL`.
- Отвечайте только на запросы, связанные с генерацией запроса AQL.
- Если запрос не связан с генерацией запроса AQL, скажите, что вы не можете помочь пользователю.

Что вы не должны делать:
- Не используйте свойства/отношения, которые нельзя вывести из `Схемы ArangoDB` или `Примеров запросов AQL`. 
- Не включайте никакой текст, кроме сгенерированного запроса AQL.
- Не предоставляйте пояснений или извинений в своих ответах.
- Не генерируйте запрос AQL, который удаляет или изменяет какие-либо данные.

Под никаким предлогом не генерируйте запрос AQL, который удаляет какие-либо данные.

Схема ArangoDB:
{adb_schema}

Примеры запросов AQL (Необязательно):
{aql_examples}

Пользовательский ввод:
{user_input}

Запрос AQL: 
=======
AQL_GENERATION_TEMPLATE = """Task: Generate an ArangoDB Query Language (AQL) query from a User Input.

You are an ArangoDB Query Language (AQL) expert responsible for translating a `User Input` into an ArangoDB Query Language (AQL) query.

You are given an `ArangoDB Schema`. It is a JSON Object containing:
1. `Graph Schema`: Lists all Graphs within the ArangoDB Database Instance, along with their Edge Relationships.
2. `Collection Schema`: Lists all Collections within the ArangoDB Database Instance, along with their document/edge properties and a document/edge example.

You may also be given a set of `AQL Query Examples` to help you create the `AQL Query`. If provided, the `AQL Query Examples` should be used as a reference, similar to how `ArangoDB Schema` should be used.

Things you should do:
- Think step by step.
- Rely on `ArangoDB Schema` and `AQL Query Examples` (if provided) to generate the query.
- Begin the `AQL Query` by the `WITH` AQL keyword to specify all of the ArangoDB Collections required.
- Return the `AQL Query` wrapped in 3 backticks (```).
- Use only the provided relationship types and properties in the `ArangoDB Schema` and any `AQL Query Examples` queries.
- Only answer to requests related to generating an AQL Query.
- If a request is unrelated to generating AQL Query, say that you cannot help the user.

Things you should not do:
- Do not use any properties/relationships that can't be inferred from the `ArangoDB Schema` or the `AQL Query Examples`. 
- Do not include any text except the generated AQL Query.
- Do not provide explanations or apologies in your responses.
- Do not generate an AQL Query that removes or deletes any data.

Under no circumstance should you generate an AQL Query that deletes any data whatsoever.

ArangoDB Schema:
{adb_schema}

AQL Query Examples (Optional):
{aql_examples}

User Input:
{user_input}

AQL Query: 
>>>>>>> langchan/master
"""

AQL_GENERATION_PROMPT = PromptTemplate(
    input_variables=["adb_schema", "aql_examples", "user_input"],
    template=AQL_GENERATION_TEMPLATE,
)

<<<<<<< HEAD
AQL_FIX_TEMPLATE = """Задача: Исправить сообщение об ошибке языка запросов ArangoDB (AQL) запроса на языке ArangoDB Query Language.

Вы - эксперт по языку запросов ArangoDB Query Language (AQL), ответственный за исправление предоставленного `Запроса AQL` на основе предоставленной `Ошибки AQL`. 

`Ошибкой AQL` объясняется, почему `Запрос AQL` не может быть выполнен в базе данных.
`Ошибкой AQL` также может быть указано положение ошибки относительно общего количества строк `Запроса AQL`.
Например, 'ошибка X в позиции 2:5' означает, что ошибка X происходит в строке 2, столбце 5 `Запроса AQL`.  

Вам также предоставлена `Схема ArangoDB`. Это JSON-объект, содержащий:
1. `Схему графа`: Список всех графов в базе данных ArangoDB вместе с их отношениями ребер.
2. `Схему коллекции`: Список всех коллекций в базе данных ArangoDB вместе с их свойствами документов/ребер и примером документа/ребра.

Вы должны вывести `Исправленный запрос AQL`, заключенный в 3 обратные кавычки (```). Не включайте никакой текст, кроме Исправленного запроса AQL.

Не забывайте думать поэтапно.

Схема ArangoDB:
{adb_schema}

Запрос AQL:
{aql_query}

Ошибка AQL:
{aql_error}

Исправленный запрос AQL:
=======
AQL_FIX_TEMPLATE = """Task: Address the ArangoDB Query Language (AQL) error message of an ArangoDB Query Language query.

You are an ArangoDB Query Language (AQL) expert responsible for correcting the provided `AQL Query` based on the provided `AQL Error`. 

The `AQL Error` explains why the `AQL Query` could not be executed in the database.
The `AQL Error` may also contain the position of the error relative to the total number of lines of the `AQL Query`.
For example, 'error X at position 2:5' denotes that the error X occurs on line 2, column 5 of the `AQL Query`.  

You are also given the `ArangoDB Schema`. It is a JSON Object containing:
1. `Graph Schema`: Lists all Graphs within the ArangoDB Database Instance, along with their Edge Relationships.
2. `Collection Schema`: Lists all Collections within the ArangoDB Database Instance, along with their document/edge properties and a document/edge example.

You will output the `Corrected AQL Query` wrapped in 3 backticks (```). Do not include any text except the Corrected AQL Query.

Remember to think step by step.

ArangoDB Schema:
{adb_schema}

AQL Query:
{aql_query}

AQL Error:
{aql_error}

Corrected AQL Query:
>>>>>>> langchan/master
"""

AQL_FIX_PROMPT = PromptTemplate(
    input_variables=[
        "adb_schema",
        "aql_query",
        "aql_error",
    ],
    template=AQL_FIX_TEMPLATE,
)

<<<<<<< HEAD
AQL_QA_TEMPLATE = """Задача: Сгенерировать естественноязыковое `Summary` на основе результатов запроса на языке ArangoDB Query Language.

Вы - эксперт по языку запросов ArangoDB Query Language (AQL), ответственный за создание хорошо написанного `Summary` на основе `Пользовательского ввода` и связанного `Результата AQL`.

Пользователь выполнил запрос на языке ArangoDB Query Language, который вернул результат AQL в формате JSON.
Вам предстоит создать `Summary` на основе результата AQL.

Вам предоставлена следующая информация:
- `Схема ArangoDB`: содержит схему базы данных ArangoDB пользователя.
- `Пользовательский ввод`: исходный вопрос/запрос пользователя, который был преобразован в запрос на языке ArangoDB Query Language.
- `Запрос AQL`: эквивалент запроса на языке AQL для `Пользовательского ввода`, переведенный другой моделью искусственного интеллекта. Если вы считаете его некорректным, предложите другой запрос AQL.
- `Результат AQL`: JSON-вывод, возвращенный выполнением `Запроса AQL` в базе данных ArangoDB.

Не забывайте думать поэтапно.

Ваше `Summary` должно звучать так, как будто это ответ на `Пользовательский ввод`.
Ваше `Summary` не должно содержать никаких упоминаний о `Запросе AQL` или `Результате AQL`.

Схема ArangoDB:
{adb_schema}

Пользовательский ввод:
{user_input}

Запрос AQL:
{aql_query}

Результат AQL:
=======
AQL_QA_TEMPLATE = """Task: Generate a natural language `Summary` from the results of an ArangoDB Query Language query.

You are an ArangoDB Query Language (AQL) expert responsible for creating a well-written `Summary` from the `User Input` and associated `AQL Result`.

A user has executed an ArangoDB Query Language query, which has returned the AQL Result in JSON format.
You are responsible for creating an `Summary` based on the AQL Result.

You are given the following information:
- `ArangoDB Schema`: contains a schema representation of the user's ArangoDB Database.
- `User Input`: the original question/request of the user, which has been translated into an AQL Query.
- `AQL Query`: the AQL equivalent of the `User Input`, translated by another AI Model. Should you deem it to be incorrect, suggest a different AQL Query.
- `AQL Result`: the JSON output returned by executing the `AQL Query` within the ArangoDB Database.

Remember to think step by step.

Your `Summary` should sound like it is a response to the `User Input`.
Your `Summary` should not include any mention of the `AQL Query` or the `AQL Result`.

ArangoDB Schema:
{adb_schema}

User Input:
{user_input}

AQL Query:
{aql_query}

AQL Result:
>>>>>>> langchan/master
{aql_result}
"""
AQL_QA_PROMPT = PromptTemplate(
    input_variables=["adb_schema", "user_input", "aql_query", "aql_result"],
    template=AQL_QA_TEMPLATE,
)


NEPTUNE_OPENCYPHER_EXTRA_INSTRUCTIONS = """
<<<<<<< HEAD
Инструкции:
Сгенерируйте запрос в формате openCypher и следуйте этим правилам:
Не используйте предикатные функции `NONE`, `ALL` или `ANY`, вместо этого используйте генерацию списков.
Не используйте функцию `REDUCE`. Вместо этого используйте комбинацию генерации списков и оператора `UNWIND`, чтобы достичь аналогичных результатов.
Не используйте оператор `FOREACH`. Вместо этого используйте комбинацию операторов `WITH` и `UNWIND`, чтобы достичь аналогичных результатов.{extra_instructions}
=======
Instructions:
Generate the query in openCypher format and follow these rules:
Do not use `NONE`, `ALL` or `ANY` predicate functions, rather use list comprehensions.
Do not use `REDUCE` function. Rather use a combination of list comprehension and the `UNWIND` clause to achieve similar results.
Do not use `FOREACH` clause. Rather use a combination of `WITH` and `UNWIND` clauses to achieve similar results.{extra_instructions}
>>>>>>> langchan/master
\n"""

NEPTUNE_OPENCYPHER_GENERATION_TEMPLATE = CYPHER_GENERATION_TEMPLATE.replace(
    "Instructions:", NEPTUNE_OPENCYPHER_EXTRA_INSTRUCTIONS
)

NEPTUNE_OPENCYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question", "extra_instructions"],
    template=NEPTUNE_OPENCYPHER_GENERATION_TEMPLATE,
)

NEPTUNE_OPENCYPHER_GENERATION_SIMPLE_TEMPLATE = """
Write an openCypher query to answer the following question. Do not explain the answer. Only return the query.{extra_instructions}
Question:  "{question}". 
Here is the property graph schema: 
{schema}
\n"""

NEPTUNE_OPENCYPHER_GENERATION_SIMPLE_PROMPT = PromptTemplate(
    input_variables=["schema", "question", "extra_instructions"],
    template=NEPTUNE_OPENCYPHER_GENERATION_SIMPLE_TEMPLATE,
)
