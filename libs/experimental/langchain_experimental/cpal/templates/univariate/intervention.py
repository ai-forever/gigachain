# ruff: noqa: E501

# fmt: off
template = (
    """
<<<<<<< HEAD
Преобразуй гипотетическое условие whatif в JSON. Не догадывайся о каких-либо частях. Напиши NONE, если не уверен.
=======
Transform the hypothetical whatif statement into JSON. Don't guess at any of the parts. Write NONE if you are unsure.
>>>>>>> langchan/master

{format_instructions}



<<<<<<< HEAD
statement: если бы у Синди было 4 питомца
=======
statement: if cindy's pet count was 4
>>>>>>> langchan/master




# JSON:



{{
    "entity_settings" : [
        {{ "name": "cindy", "attribute": "pet_count", "value": "4" }}
    ]
}}





<<<<<<< HEAD
statement: Допустим, у Бориса десять долларов, а у Билла 20 долларов.
=======
statement: Let's say boris has ten dollars and Bill has 20 dollars.
>>>>>>> langchan/master




# JSON:


{{
    "entity_settings" : [
        {{ "name": "boris", "attribute": "dollars", "value": "10" }},
        {{ "name": "bill", "attribute": "dollars", "value": "20" }}
    ]
}}





Statement: {narrative_input}




# JSON:
""".strip()
    + "\n\n\n"
)
# fmt: on
