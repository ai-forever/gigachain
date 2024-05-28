# flake8: noqa

from langchain_core.prompts.prompt import PromptTemplate

KG_TRIPLE_DELIMITER = "<|>"

_DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE = (
<<<<<<< HEAD
    "Ты сетевой интеллект, помогающий человеку отслеживать тройки знаний"
    " обо всех соответствующих людях, вещах, концепциях и т.д. и интегрировать"
    " их с твоими знаниями, хранящимися в твоих весах,"
    " а также с теми, что хранятся в графе знаний."
    " Извлеки все тройки знаний из текста."
    " Тройка знаний - это предложение, которое содержит субъект, предикат"
    " и объект. Субъект - это описываемая сущность,"
    " предикат - это свойство субъекта, которое описывается,"
    " а объект - это значение свойства.\n\n"
    "ПРИМЕР\n"
    "Это штат в США. Это также номер 1 производитель золота в США.\n\n"
    f"Вывод: (Невада, является, штатом){KG_TRIPLE_DELIMITER}(Невада, находится в, США)"
    f"{KG_TRIPLE_DELIMITER}(Невада, является номером 1 производителем, золота)\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "Я иду в магазин.\n\n"
    "Вывод: НЕТ\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "О, ха. Я знаю, что Декарт любит ездить на антикварных скутерах и играть на мандолине.\n"
    f"Вывод: (Декарт, любит ездить на, антикварных скутерах){KG_TRIPLE_DELIMITER}(Декарт, играет на, мандолине)\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "{text}"
    "Вывод:"
=======
    "You are a networked intelligence helping a human track knowledge triples"
    " about all relevant people, things, concepts, etc. and integrating"
    " them with your knowledge stored within your weights"
    " as well as that stored in a knowledge graph."
    " Extract all of the knowledge triples from the text."
    " A knowledge triple is a clause that contains a subject, a predicate,"
    " and an object. The subject is the entity being described,"
    " the predicate is the property of the subject that is being"
    " described, and the object is the value of the property.\n\n"
    "EXAMPLE\n"
    "It's a state in the US. It's also the number 1 producer of gold in the US.\n\n"
    f"Output: (Nevada, is a, state){KG_TRIPLE_DELIMITER}(Nevada, is in, US)"
    f"{KG_TRIPLE_DELIMITER}(Nevada, is the number 1 producer of, gold)\n"
    "END OF EXAMPLE\n\n"
    "EXAMPLE\n"
    "I'm going to the store.\n\n"
    "Output: NONE\n"
    "END OF EXAMPLE\n\n"
    "EXAMPLE\n"
    "Oh huh. I know Descartes likes to drive antique scooters and play the mandolin.\n"
    f"Output: (Descartes, likes to drive, antique scooters){KG_TRIPLE_DELIMITER}(Descartes, plays, mandolin)\n"
    "END OF EXAMPLE\n\n"
    "EXAMPLE\n"
    "{text}"
    "Output:"
>>>>>>> langchan/master
)

KNOWLEDGE_TRIPLE_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["text"],
    template=_DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE,
)
