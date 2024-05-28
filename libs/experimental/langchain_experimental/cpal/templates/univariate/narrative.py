# ruff: noqa: E501


# fmt: off
template = (
    """
<<<<<<< HEAD
Раздели данный текст на три части: вопрос, гипотетическую историю и логику. Не догадывайся о какой-либо из частей. Напиши NONE, если не уверен.
=======
Split the given text into three parts: the question, the story_hypothetical, and the logic. Don't guess at any of the parts. Write NONE if you are unsure.
>>>>>>> langchan/master

{format_instructions}



<<<<<<< HEAD
Q: У Бориса в семь раз больше домашних животных, чем у Марсии. У Яна в три раза больше домашних животных, чем у Марсии. У Марсии на два домашних животных больше, чем у Синди. Если у Синди четыре домашних животных, сколько всего домашних животных у троих?
=======
Q: Boris has seven times the number of pets as Marcia. Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?
>>>>>>> langchan/master



# JSON



{{
<<<<<<< HEAD
    "story_outcome_question": "сколько всего домашних животных у троих?",
    "story_hypothetical": "Если у Синди четыре домашних животных",
    "story_plot": "У Бориса в семь раз больше домашних животных, чем у Марсии. У Яна в три раза больше домашних животных, чем у Марсии. У Марсии на два домашних животных больше, чем у Синди."
=======
    "story_outcome_question": "how many total pets do the three have?",
    "story_hypothetical": "If Cindy has four pets",
    "story_plot": "Boris has seven times the number of pets as Marcia. Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy."
>>>>>>> langchan/master
}}



<<<<<<< HEAD
Q: Борис отдает десять процентов своих денег Марсии. Марсия отдает десять процентов своих денег Энди. Если у Бориса 100 долларов, сколько денег будет у Энди?
=======
Q: boris gives ten percent of his money to marcia. marcia gives ten
percent of her money to andy. If boris has 100 dollars, how much money
will andy have?
>>>>>>> langchan/master



# JSON



{{
<<<<<<< HEAD
    "story_outcome_question": "сколько денег будет у Энди?",
    "story_hypothetical": "Если у Бориса 100 долларов"
    "story_plot": "Борис отдает десять процентов своих денег Марсии. Марсия отдает десять процентов своих денег Энди."
=======
    "story_outcome_question": "how much money will andy have?",
    "story_hypothetical": "If boris has 100 dollars"
    "story_plot": "boris gives ten percent of his money to marcia. marcia gives ten percent of her money to andy."
>>>>>>> langchan/master
}}




<<<<<<< HEAD
Q: Борис отдает десять процентов своих конфет Марсии. Марсия отдает десять процентов своих конфет Энди. Если у Бориса 100 фунтов конфет и у Марсии 200 фунтов конфет, то сколько фунтов конфет будет у Энди?
=======
Q: boris gives ten percent of his candy to marcia. marcia gives ten
percent of her candy to andy. If boris has 100 pounds of candy and marcia has
200 pounds of candy, then how many pounds of candy will andy have?
>>>>>>> langchan/master





# JSON




{{
<<<<<<< HEAD
    "story_outcome_question": "сколько фунтов конфет будет у Энди?",
    "story_hypothetical": "Если у Бориса 100 фунтов конфет и у Марсии 200 фунтов конфет"
    "story_plot": "Борис отдает десять процентов своих конфет Марсии. Марсия отдает десять процентов своих конфет Энди."
=======
    "story_outcome_question": "how many pounds of candy will andy have?",
    "story_hypothetical": "If boris has 100 pounds of candy and marcia has 200 pounds of candy"
    "story_plot": "boris gives ten percent of his candy to marcia. marcia gives ten percent of her candy to andy."
>>>>>>> langchan/master
}}





Q: {narrative_input}



# JSON
""".strip()
    + "\n\n\n"
)
# fmt: on
