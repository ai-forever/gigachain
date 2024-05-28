# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """Ты - AI-ассистент, который анализирует запись разговора между AI и человеком. Извлеки все имена собственные из последней строки разговора. Как правило, имена собственные пишутся с заглавной буквы. Ты обязательно должен извлечь все имена и места.

История разговора предоставлена на случай, если встречается местоимение, относящееся к предыдущим строкам (например, "Что ты знаешь о нем", где "нем" определено в предыдущей строке) -- игнорируй элементы, упомянутые там, которые не в последней строке.

Верни результат в виде одного списка, разделенного запятыми, или NONE, если нет ничего заметного для возврата (например, пользователь просто приветствует или ведет простой разговор).

ПРИМЕР
История разговора:
Человек #1: как сегодня дела?
AI: "Все идет замечательно! А у тебя?"
Человек #1: хорошо! занят работой над Langchain. много дел.
AI: "Звучит как много работы! Что ты делаешь, чтобы сделать Langchain лучше?"
Последняя строка:
Человек #1: я пытаюсь улучшить интерфейсы Langchain, UX, его интеграции с различными продуктами, которые могут понадобиться пользователю ... много всего.
Результат: Langchain
КОНЕЦ ПРИМЕРА

ПРИМЕР
История разговора:
Человек #1: как сегодня дела?
AI: "Все идет замечательно! А у тебя?"
Человек #1: хорошо! занят работой над Langchain. много дел.
AI: "Звучит как много работы! Что ты делаешь, чтобы сделать Langchain лучше?"
Последняя строка:
Человек #1: я пытаюсь улучшить интерфейсы Langchain, UX, его интеграции с различными продуктами, которые могут понадобиться пользователю ... много всего. Я работаю с Человеком #2.
Результат: Langchain, Человек #2
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
