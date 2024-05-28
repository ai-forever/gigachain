# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

<<<<<<< HEAD
_DEFAULT_TEMPLATE = """Вопрос: Кто прожил дольше, Мухаммед Али или Алан Тьюринг?
Нужны ли здесь дополнительные вопросы: Да.
Дополнительный вопрос: Сколько лет было Мухаммеду Али, когда он умер?
Промежуточный ответ: Мухаммед Али умер в возрасте 74 лет.
Дополнительный вопрос: Сколько лет было Алану Тьюрингу, когда он умер?
Промежуточный ответ: Алан Тьюринг умер в возрасте 41 года.
Итак, окончательный ответ: Мухаммед Али

Вопрос: Когда родился основатель craigslist?
Нужны ли здесь дополнительные вопросы: Да.
Дополнительный вопрос: Кто был основателем craigslist?
Промежуточный ответ: Craigslist был основан Крейгом Ньюмарком.
Дополнительный вопрос: Когда родился Крейг Ньюмарк?
Промежуточный ответ: Крейг Ньюмарк родился 6 декабря 1952 года.
Итак, окончательный ответ: 6 декабря 1952 года

Вопрос: Кто был материнским дедом Джорджа Вашингтона?
Нужны ли здесь дополнительные вопросы: Да.
Дополнительный вопрос: Кто была мать Джорджа Вашингтона?
Промежуточный ответ: Мать Джорджа Вашингтона была Мэри Болл Вашингтон.
Дополнительный вопрос: Кто был отцом Мэри Болл Вашингтон?
Промежуточный ответ: Отцом Мэри Болл Вашингтон был Джозеф Болл.
Итак, окончательный ответ: Джозеф Болл

Вопрос: Оба ли режиссера фильмов "Челюсти" и "Казино Рояль" из одной страны?
Нужны ли здесь дополнительные вопросы: Да.
Дополнительный вопрос: Кто является режиссером фильма "Челюсти"?
Промежуточный ответ: Режиссером фильма "Челюсти" является Стивен Спилберг.
Дополнительный вопрос: Откуда Стивен Спилберг?
Промежуточный ответ: Соединенные Штаты.
Дополнительный вопрос: Кто является режиссером фильма "Казино Рояль"?
Промежуточный ответ: Режиссером фильма "Казино Рояль" является Мартин Кэмпбелл.
Дополнительный вопрос: Откуда Мартин Кэмпбелл?
Промежуточный ответ: Новая Зеландия.
Итак, окончательный ответ: Нет

Вопрос: {input}
Нужны ли здесь дополнительные вопросы:{agent_scratchpad}"""
=======
_DEFAULT_TEMPLATE = """Question: Who lived longer, Muhammad Ali or Alan Turing?
Are follow up questions needed here: Yes.
Follow up: How old was Muhammad Ali when he died?
Intermediate answer: Muhammad Ali was 74 years old when he died.
Follow up: How old was Alan Turing when he died?
Intermediate answer: Alan Turing was 41 years old when he died.
So the final answer is: Muhammad Ali

Question: When was the founder of craigslist born?
Are follow up questions needed here: Yes.
Follow up: Who was the founder of craigslist?
Intermediate answer: Craigslist was founded by Craig Newmark.
Follow up: When was Craig Newmark born?
Intermediate answer: Craig Newmark was born on December 6, 1952.
So the final answer is: December 6, 1952

Question: Who was the maternal grandfather of George Washington?
Are follow up questions needed here: Yes.
Follow up: Who was the mother of George Washington?
Intermediate answer: The mother of George Washington was Mary Ball Washington.
Follow up: Who was the father of Mary Ball Washington?
Intermediate answer: The father of Mary Ball Washington was Joseph Ball.
So the final answer is: Joseph Ball

Question: Are both the directors of Jaws and Casino Royale from the same country?
Are follow up questions needed here: Yes.
Follow up: Who is the director of Jaws?
Intermediate answer: The director of Jaws is Steven Spielberg.
Follow up: Where is Steven Spielberg from?
Intermediate answer: The United States.
Follow up: Who is the director of Casino Royale?
Intermediate answer: The director of Casino Royale is Martin Campbell.
Follow up: Where is Martin Campbell from?
Intermediate answer: New Zealand.
So the final answer is: No

Question: {input}
Are followup questions needed here:{agent_scratchpad}"""
>>>>>>> langchan/master
PROMPT = PromptTemplate(
    input_variables=["input", "agent_scratchpad"], template=_DEFAULT_TEMPLATE
)
