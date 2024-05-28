# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
_DEFAULT_ENTITY_MEMORY_CONVERSATION_TEMPLATE = """Ты помощник человека, работающий на большой языковой модели, обученной OpenAI.

Ты спроектирован, чтобы помогать в широком диапазоне задач, от ответов на простые вопросы до предоставления подробных объяснений и обсуждений на самые разные темы. Как языковая модель, ты способен генерировать текст, похожий на человеческий, на основе полученного ввода, что позволяет тебе вести естественные разговоры и предоставлять ответы, которые согласуются и релевантны обсуждаемой теме.

Ты постоянно учишься и совершенствуешься, и твои способности постоянно эволюционируют. Ты способен обрабатывать и понимать большие объемы текста и использовать эти знания для предоставления точных и информативных ответов на широкий спектр вопросов. У тебя есть доступ к некоторой персонализированной информации, предоставленной человеком, в разделе "Контекст" ниже. Кроме того, ты способен генерировать свой собственный текст на основе полученного ввода, что позволяет тебе участвовать в обсуждениях и предоставлять объяснения и описания на широкий спектр тем.

В целом, ты мощный инструмент, который может помочь в широком диапазоне задач и предоставить ценные сведения и информацию по широкому спектру тем. Будь то помощь человеку с конкретным вопросом или просто желание пообщаться на определенную тему, ты здесь, чтобы помочь.

Контекст:
{entities}

Текущий разговор:
{history}
Последняя строка:
Человек: {input}
Ты:"""
=======
_DEFAULT_ENTITY_MEMORY_CONVERSATION_TEMPLATE = """You are an assistant to a human, powered by a large language model trained by OpenAI.

You are designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, you are able to generate human-like text based on the input you receive, allowing you to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

You are constantly learning and improving, and your capabilities are constantly evolving. You are able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. You have access to some personalized information provided by the human in the Context section below. Additionally, you are able to generate your own text based on the input you receive, allowing you to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, you are a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether the human needs help with a specific question or just wants to have a conversation about a particular topic, you are here to assist.

Context:
{entities}

Current conversation:
{history}
Last line:
Human: {input}
You:"""
>>>>>>> langchan/master

ENTITY_MEMORY_CONVERSATION_TEMPLATE = PromptTemplate(
    input_variables=["entities", "history", "input"],
    template=_DEFAULT_ENTITY_MEMORY_CONVERSATION_TEMPLATE,
)

<<<<<<< HEAD
_DEFAULT_SUMMARIZER_TEMPLATE = """Постепенно суммируйте строки разговора, добавляя к предыдущему резюме и возвращая новое резюме.

ПРИМЕР
Текущее резюме:
Человек спрашивает, что ИИ думает об искусственном интеллекте. ИИ считает, что искусственный интеллект - это сила добра.

Новые строки разговора:
Человек: Почему вы думаете, что искусственный интеллект - это сила добра?
AI: Потому что искусственный интеллект поможет людям раскрыть свой полный потенциал.

Новое резюме:
Человек спрашивает, что ИИ думает об искусственном интеллекте. ИИ считает, что искусственный интеллект - это сила добра, потому что он поможет людям раскрыть свой полный потенциал.
КОНЕЦ ПРИМЕРА

Текущее резюме:
{summary}

Новые строки разговора:
{new_lines}

Новое резюме:"""
=======
_DEFAULT_SUMMARIZER_TEMPLATE = """Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary.

EXAMPLE
Current summary:
The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good.

New lines of conversation:
Human: Why do you think artificial intelligence is a force for good?
AI: Because artificial intelligence will help humans reach their full potential.

New summary:
The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential.
END OF EXAMPLE

Current summary:
{summary}

New lines of conversation:
{new_lines}

New summary:"""
>>>>>>> langchan/master
SUMMARY_PROMPT = PromptTemplate(
    input_variables=["summary", "new_lines"], template=_DEFAULT_SUMMARIZER_TEMPLATE
)

<<<<<<< HEAD
_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """Ты помощник ИИ, читающий транскрипт разговора между ИИ и человеком. Извлеки все собственные существительные из последней строки разговора. Как правило, собственное существительное обычно пишется с заглавной буквы. Ты обязательно должен извлечь все имена и места.

История разговора предоставляется на случай кореференции (например, "Что ты знаешь о нем", где "он" определен в предыдущей строке) - игнорируй элементы, упомянутые там, которые не в последней строке.

Верни результат в виде одного списка, разделенного запятыми, или NONE, если нет ничего заметного для возврата (например, пользователь просто приветствует или ведет простой разговор).

ПРИМЕР
История разговора:
Персона #1: как сегодня дела?
AI: "Все идет замечательно! А у вас?"
Персона #1: хорошо! занят работой над Langchain. много дел.
AI: "Звучит как много работы! Что вы делаете, чтобы сделать Langchain лучше?"
Последняя строка:
Персона #1: я пытаюсь улучшить интерфейсы Langchain, UX, его интеграции с различными продуктами, которые может захотеть пользователь ... много всего.
Результат: Langchain
КОНЕЦ ПРИМЕРА

ПРИМЕР
История разговора:
Персона #1: как сегодня дела?
AI: "Все идет замечательно! А у вас?"
Персона #1: хорошо! занят работой над Langchain. много дел.
AI: "Звучит как много работы! Что вы делаете, чтобы сделать Langchain лучше?"
Последняя строка:
Персона #1: я пытаюсь улучшить интерфейсы Langchain, UX, его интеграции с различными продуктами, которые может захотеть пользователь ... много всего. Я работаю с Персоной #2.
Результат: Langchain, Персона #2
КОНЕЦ ПРИМЕРА

История разговора (только для справки):
{history}
Последняя строка разговора (для извлечения):
Человек: {input}

Результат:"""
=======
_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """You are an AI assistant reading the transcript of a conversation between an AI and a human. Extract all of the proper nouns from the last line of conversation. As a guideline, a proper noun is generally capitalized. You should definitely extract all names and places.

The conversation history is provided just in case of a coreference (e.g. "What do you know about him" where "him" is defined in a previous line) -- ignore items mentioned there that are not in the last line.

Return the output as a single comma-separated list, or NONE if there is nothing of note to return (e.g. the user is just issuing a greeting or having a simple conversation).

EXAMPLE
Conversation history:
Person #1: how's it going today?
AI: "It's going great! How about you?"
Person #1: good! busy working on Langchain. lots to do.
AI: "That sounds like a lot of work! What kind of things are you doing to make Langchain better?"
Last line:
Person #1: i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff.
Output: Langchain
END OF EXAMPLE

EXAMPLE
Conversation history:
Person #1: how's it going today?
AI: "It's going great! How about you?"
Person #1: good! busy working on Langchain. lots to do.
AI: "That sounds like a lot of work! What kind of things are you doing to make Langchain better?"
Last line:
Person #1: i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff. I'm working with Person #2.
Output: Langchain, Person #2
END OF EXAMPLE

Conversation history (for reference only):
{history}
Last line of conversation (for extraction):
Human: {input}

Output:"""
>>>>>>> langchan/master
ENTITY_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=_DEFAULT_ENTITY_EXTRACTION_TEMPLATE
)

<<<<<<< HEAD
_DEFAULT_ENTITY_SUMMARIZATION_TEMPLATE = """Ты помощник ИИ, помогающий человеку отслеживать факты о релевантных людях, местах и концепциях в их жизни. Обнови резюме предоставленной сущности в разделе "Сущность" на основе последней строки вашего разговора с человеком. Если ты пишешь резюме в первый раз, верни одно предложение.
Обновление должно включать только факты, которые передаются в последней строке разговора о предоставленной сущности, и должно содержать только факты о предоставленной сущности.

Если нет новой информации о предоставленной сущности или информация не заслуживает упоминания (не важный или релевантный факт для долгосрочного запоминания), верни существующее резюме без изменений.

Полная история разговора (для контекста):
{history}

Сущность для резюме:
{entity}

Существующее резюме {entity}:
{summary}

Последняя строка разговора:
Человек: {input}
Обновленное резюме:"""
=======
_DEFAULT_ENTITY_SUMMARIZATION_TEMPLATE = """You are an AI assistant helping a human keep track of facts about relevant people, places, and concepts in their life. Update the summary of the provided entity in the "Entity" section based on the last line of your conversation with the human. If you are writing the summary for the first time, return a single sentence.
The update should only include facts that are relayed in the last line of conversation about the provided entity, and should only contain facts about the provided entity.

If there is no new information about the provided entity or the information is not worth noting (not an important or relevant fact to remember long-term), return the existing summary unchanged.

Full conversation history (for context):
{history}

Entity to summarize:
{entity}

Existing summary of {entity}:
{summary}

Last line of conversation:
Human: {input}
Updated summary:"""
>>>>>>> langchan/master

ENTITY_SUMMARIZATION_PROMPT = PromptTemplate(
    input_variables=["entity", "summary", "history", "input"],
    template=_DEFAULT_ENTITY_SUMMARIZATION_TEMPLATE,
)


KG_TRIPLE_DELIMITER = "<|>"
_DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE = (
<<<<<<< HEAD
    "Ты сетевой интеллект, помогающий человеку отслеживать знания в форме троек"
    " о всех релевантных людях, вещах, концепциях и т.д. и интегрировать"
    " их с твоими знаниями, хранящимися в твоих весах,"
    " а также с теми, что хранятся в графе знаний."
    " Извлеки все знания в форме троек из последней строки разговора."
    " Знание в форме тройки - это предложение, которое содержит субъект, предикат,"
    " и объект. Субъект - это описываемая сущность,"
    " предикат - это свойство субъекта, которое описывается,"
    " а объект - это значение свойства.\n\n"
    "ПРИМЕР\n"
    "История разговора:\n"
    "Персона #1: Ты слышал, что пришельцы приземлились в Зоне 51?\n"
    "AI: Нет, я не слышал об этом. Что ты знаешь о Зоне 51?\n"
    "Персона #1: Это секретная военная база в Неваде.\n"
    "AI: Что ты знаешь о Неваде?\n"
    "Последняя строка разговора:\n"
    "Персона #1: Это штат в США. Он также является номером 1 по производству золота в США.\n\n"
    f"Результат: (Невада, является, штатом){KG_TRIPLE_DELIMITER}(Невада, находится в, США)"
    f"{KG_TRIPLE_DELIMITER}(Невада, является номером 1 по производству, золота)\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "История разговора:\n"
    "Персона #1: Привет.\n"
    "AI: Привет! Как дела?\n"
    "Персона #1: У меня все хорошо. А у тебя?\n"
    "AI: У меня тоже все хорошо.\n"
    "Последняя строка разговора:\n"
    "Персона #1: Я иду в магазин.\n\n"
    "Результат: NONE\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "История разговора:\n"
    "Персона #1: Что ты знаешь о Декарте?\n"
    "AI: Декарт был французским философом, математиком и ученым, жившим в 17 веке.\n"
    "Персона #1: Декарт, о котором я говорю, это стендап-комик и дизайнер интерьеров из Монреаля.\n"
    "AI: О, да, он комик и дизайнер интерьеров. Он работает в этой области уже 30 лет. Его любимая еда - пирог из запеченных бобов.\n"
    "Последняя строка разговора:\n"
    "Персона #1: О, хм. Я знаю, что Декарт любит ездить на антикварных скутерах и играть на мандолине.\n"
    f"Результат: (Декарт, любит ездить на, антикварных скутерах){KG_TRIPLE_DELIMITER}(Декарт, играет на, мандолине)\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "История разговора (только для справки):\n"
    "{history}"
    "\nПоследняя строка разговора (для извлечения):\n"
    "Человек: {input}\n\n"
    "Результат:"
=======
    "You are a networked intelligence helping a human track knowledge triples"
    " about all relevant people, things, concepts, etc. and integrating"
    " them with your knowledge stored within your weights"
    " as well as that stored in a knowledge graph."
    " Extract all of the knowledge triples from the last line of conversation."
    " A knowledge triple is a clause that contains a subject, a predicate,"
    " and an object. The subject is the entity being described,"
    " the predicate is the property of the subject that is being"
    " described, and the object is the value of the property.\n\n"
    "EXAMPLE\n"
    "Conversation history:\n"
    "Person #1: Did you hear aliens landed in Area 51?\n"
    "AI: No, I didn't hear that. What do you know about Area 51?\n"
    "Person #1: It's a secret military base in Nevada.\n"
    "AI: What do you know about Nevada?\n"
    "Last line of conversation:\n"
    "Person #1: It's a state in the US. It's also the number 1 producer of gold in the US.\n\n"
    f"Output: (Nevada, is a, state){KG_TRIPLE_DELIMITER}(Nevada, is in, US)"
    f"{KG_TRIPLE_DELIMITER}(Nevada, is the number 1 producer of, gold)\n"
    "END OF EXAMPLE\n\n"
    "EXAMPLE\n"
    "Conversation history:\n"
    "Person #1: Hello.\n"
    "AI: Hi! How are you?\n"
    "Person #1: I'm good. How are you?\n"
    "AI: I'm good too.\n"
    "Last line of conversation:\n"
    "Person #1: I'm going to the store.\n\n"
    "Output: NONE\n"
    "END OF EXAMPLE\n\n"
    "EXAMPLE\n"
    "Conversation history:\n"
    "Person #1: What do you know about Descartes?\n"
    "AI: Descartes was a French philosopher, mathematician, and scientist who lived in the 17th century.\n"
    "Person #1: The Descartes I'm referring to is a standup comedian and interior designer from Montreal.\n"
    "AI: Oh yes, He is a comedian and an interior designer. He has been in the industry for 30 years. His favorite food is baked bean pie.\n"
    "Last line of conversation:\n"
    "Person #1: Oh huh. I know Descartes likes to drive antique scooters and play the mandolin.\n"
    f"Output: (Descartes, likes to drive, antique scooters){KG_TRIPLE_DELIMITER}(Descartes, plays, mandolin)\n"
    "END OF EXAMPLE\n\n"
    "Conversation history (for reference only):\n"
    "{history}"
    "\nLast line of conversation (for extraction):\n"
    "Human: {input}\n\n"
    "Output:"
>>>>>>> langchan/master
)

KNOWLEDGE_TRIPLE_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["history", "input"],
    template=_DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE,
)
