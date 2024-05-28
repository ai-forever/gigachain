from rag_self_query import chain

if __name__ == "__main__":
    questions = [
        "What is the nasa sales team?",
        "What is our work from home policy?",
        "Does the company own my personal project?",
        "How does compensation work?",
    ]

    response = chain.invoke(
        {
            "question": questions[0],
            "chat_history": [],
        }
    )
<<<<<<< HEAD
    print(response)  # noqa: T201
=======
    print(response)
>>>>>>> langchan/master

    follow_up_question = "What are their objectives?"

    response = chain.invoke(
        {
            "question": follow_up_question,
            "chat_history": [
                "What is the nasa sales team?",
                "The sales team of NASA consists of Laura Martinez, the Area "
                "Vice-President of North America, and Gary Johnson, the Area "
                "Vice-President of South America. (Sales Organization Overview)",
            ],
        }
    )

<<<<<<< HEAD
    print(response)  # noqa: T201
=======
    print(response)
>>>>>>> langchan/master
