# ruff: noqa: E501


# fmt: off
template = (
    """
<<<<<<< HEAD
Преобразуй narrative_input в SQL выражение. Если ты не уверен, то не угадывай, вместо этого добавь llm_error_msg, который объясняет, почему ты не уверен.
=======
Transform the narrative_input into an SQL expression. If you are
unsure, then do not guess, instead add a llm_error_msg that explains why you are unsure.
>>>>>>> langchan/master


{format_instructions}


<<<<<<< HEAD
narrative_input: сколько денег у Бориса будет?
=======
narrative_input: how much money will boris have?
>>>>>>> langchan/master


# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "сколько денег у Бориса будет?",
=======
        "narrative_input": "how much money will boris have?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT name, value FROM df WHERE name = 'boris'"
    }}



<<<<<<< HEAD
narrative_input: Сколько денег у Теда?
=======
narrative_input: How much money does ted have?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "Сколько денег у Теда?",
=======
        "narrative_input": "How much money does ted have?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT name, value FROM df WHERE name = 'ted'"
    }}



<<<<<<< HEAD
narrative_input: какова сумма количества питомцев у всех людей?
=======
narrative_input: what is the sum of pet count for all the people?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "какова сумма количества питомцев у всех людей?",
=======
        "narrative_input": "what is the sum of pet count for all the people?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT SUM(value) FROM df"
    }}




<<<<<<< HEAD
narrative_input: каково среднее количество питомцев у всех людей?
=======
narrative_input: what's the average of the pet counts for all the people?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "каково среднее количество питомцев у всех людей?",
=======
        "narrative_input": "what's the average of the pet counts for all the people?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT AVG(value) FROM df"
    }}




<<<<<<< HEAD
narrative_input: какое максимальное количество питомцев у всех людей?
=======
narrative_input: what's the maximum of the pet counts for all the people?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "какое максимальное количество питомцев у всех людей?",
=======
        "narrative_input": "what's the maximum of the pet counts for all the people?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT MAX(value) FROM df"
    }}




<<<<<<< HEAD
narrative_input: какое минимальное количество питомцев у всех людей?
=======
narrative_input: what's the minimum of the pet counts for all the people?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "какое минимальное количество питомцев у всех людей?",
=======
        "narrative_input": "what's the minimum of the pet counts for all the people?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT MIN(value) FROM df"
    }}




<<<<<<< HEAD
narrative_input: сколько людей имеют больше 10 питомцев?
=======
narrative_input: what's the number of people with pet counts greater than 10?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "сколько людей имеют больше 10 питомцев?",
=======
        "narrative_input": "what's the number of people with pet counts greater than 10?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT COUNT(*) FROM df WHERE value > 10"
    }}




<<<<<<< HEAD
narrative_input: сколько питомцев у Бориса?
=======
narrative_input: what's the pet count for boris?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "сколько питомцев у Бориса?",
=======
        "narrative_input": "what's the pet count for boris?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT name, value FROM df WHERE name = 'boris'"
    }}




<<<<<<< HEAD
narrative_input: сколько питомцев у Синди и Марсии?
=======
narrative_input: what's the pet count for cindy and marcia?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "сколько питомцев у Синди и Марсии?",
=======
        "narrative_input": "what's the pet count for cindy and marcia?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT name, value FROM df WHERE name IN ('cindy', 'marcia')"
    }}




<<<<<<< HEAD
narrative_input: какова общая сумма питомцев у Синди и Марсии?
=======
narrative_input: what's the total pet count for cindy and marcia?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "какова общая сумма питомцев у Синди и Марсии?",
=======
        "narrative_input": "what's the total pet count for cindy and marcia?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT SUM(value) FROM df WHERE name IN ('cindy', 'marcia')"
    }}




<<<<<<< HEAD
narrative_input: какова общая сумма питомцев у ТЕД?
=======
narrative_input: what's the total pet count for TED?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "какова общая сумма питомцев у ТЕД?",
=======
        "narrative_input": "what's the total pet count for TED?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT SUM(value) FROM df WHERE name = 'TED'"
    }}





<<<<<<< HEAD
narrative_input: какова общая сумма долларов у ТЕД и Синди?
=======
narrative_input: what's the total dollar count for TED and cindy?
>>>>>>> langchan/master



# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "какова общая сумма долларов у ТЕД и Синди?",
=======
        "narrative_input": "what's the total dollar count for TED and cindy?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT SUM(value) FROM df WHERE name IN ('TED', 'cindy')"
    }}




<<<<<<< HEAD
narrative_input: какова общая сумма питомцев у ТЕД и Синди?
=======
narrative_input: what's the total pet count for TED and cindy?
>>>>>>> langchan/master




# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "какова общая сумма питомцев у ТЕД и Синди?",
=======
        "narrative_input": "what's the total pet count for TED and cindy?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT SUM(value) FROM df WHERE name IN ('TED', 'cindy')"
    }}




<<<<<<< HEAD
narrative_input: что лучше для ТЕД и Синди?
=======
narrative_input: what's the best for TED and cindy?
>>>>>>> langchan/master




# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "что лучше для ТЕД и Синди?",
        "llm_error_msg": "неоднозначный narrative_input, не уверен, что значит 'лучше'",
=======
        "narrative_input": "what's the best for TED and cindy?",
        "llm_error_msg": "ambiguous narrative_input, not sure what 'best' means",
>>>>>>> langchan/master
        "expression": ""
    }}




<<<<<<< HEAD
narrative_input: какова стоимость?
=======
narrative_input: what's the value?
>>>>>>> langchan/master




# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "какова стоимость?",
        "llm_error_msg": "неоднозначный narrative_input, не уверен, о каком объекте идет речь",
=======
        "narrative_input": "what's the value?",
        "llm_error_msg": "ambiguous narrative_input, not sure what entity is being asked about",
>>>>>>> langchan/master
        "expression": ""
    }}






<<<<<<< HEAD
narrative_input: сколько всего питомцев у троих?
=======
narrative_input: how many total pets do the three have?
>>>>>>> langchan/master





# JSON:

    {{
<<<<<<< HEAD
        "narrative_input": "сколько всего питомцев у троих?",
=======
        "narrative_input": "how many total pets do the three have?",
>>>>>>> langchan/master
        "llm_error_msg": "",
        "expression": "SELECT SUM(value) FROM df"
    }}






narrative_input: {narrative_input}




# JSON:
""".strip()
    + "\n\n\n"
)
# fmt: on
