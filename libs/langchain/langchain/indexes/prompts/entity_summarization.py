# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
_DEFAULT_ENTITY_SUMMARIZATION_TEMPLATE = """Ты - AI-ассистент, помогающий человеку отслеживать факты о релевантных людях, местах и концепциях в их жизни. Обнови резюме предоставленной сущности в разделе "Сущность" на основе последней строки твоего разговора с человеком. Если ты пишешь резюме в первый раз, верни одно предложение.
Обновление должно включать только факты, которые передаются в последней строке разговора о предоставленной сущности, и должно содержать только факты о предоставленной сущности.

Если нет новой информации о предоставленной сущности или информация не стоит отмечать (не важный или релевантный факт для долгосрочного запоминания), верни существующее резюме без изменений.

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
