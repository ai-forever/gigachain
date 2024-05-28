# ruff: noqa: E501

# fmt: off
template = (
    """
<<<<<<< HEAD
Преобразуй сюжет математической задачи в объект JSON. Не догадывайся о каких-либо частях.
=======
Transform the math story plot into a JSON object. Don't guess at any of the parts.
>>>>>>> langchan/master

{format_instructions}



<<<<<<< HEAD
История: У Бориса в семь раз больше домашних животных, чем у Марсии. У Яна в три раза больше домашних животных, чем у Марсии. У Марсии на два домашних животных больше, чем у Синди.
=======
Story: Boris has seven times the number of pets as Marcia. Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy.
>>>>>>> langchan/master



# JSON:



{{
    "attribute": "pet_count",
    "entities": [
        {{
            "name": "cindy",
            "value": 0,
            "depends_on": [],
            "code": "pass"
        }},
        {{
            "name": "marcia",
            "value": 0,
            "depends_on": ["cindy"],
            "code": "marcia.value = cindy.value + 2"
        }},
        {{
            "name": "boris",
            "value": 0,
            "depends_on": ["marcia"],
            "code": "boris.value = marcia.value * 7"
        }},
        {{
            "name": "jan",
            "value": 0,
            "depends_on": ["marcia"],
            "code": "jan.value = marcia.value * 3"
        }}
    ]
}}




<<<<<<< HEAD
История: Борис отдает 20 процентов своих денег Марсии. Марсия отдает 10
процентов своих денег Синди. Синди отдает 5 процентов своих денег Яну.
=======
Story: Boris gives 20 percent of his money to Marcia. Marcia gives 10
percent of her money to Cindy. Cindy gives 5 percent of her money to Jan.
>>>>>>> langchan/master




# JSON:



{{
    "attribute": "money",
    "entities": [
        {{
            "name": "boris",
            "value": 0,
            "depends_on": [],
            "code": "pass"
        }},
        {{
            "name": "marcia",
            "value": 0,
            "depends_on": ["boris"],
            "code": "
                marcia.value = boris.value * 0.2
                boris.value = boris.value * 0.8
            "
        }},
        {{
            "name": "cindy",
            "value": 0,
            "depends_on": ["marcia"],
            "code": "
                cindy.value = marcia.value * 0.1
                marcia.value = marcia.value * 0.9
            "
        }},
        {{
            "name": "jan",
            "value": 0,
            "depends_on": ["cindy"],
            "code": "
                jan.value = cindy.value * 0.05
                cindy.value = cindy.value * 0.9
            "
        }}
    ]
}}




<<<<<<< HEAD
История: {narrative_input}
=======
Story: {narrative_input}
>>>>>>> langchan/master



# JSON:
""".strip()
    + "\n"
)
# fmt: on
