from neo4j_advanced_rag.chain import chain

if __name__ == "__main__":
    original_query = "What is the plot of the Dune?"
<<<<<<< HEAD
    print(  # noqa: T201
=======
    print(
>>>>>>> langchan/master
        chain.invoke(
            {"question": original_query},
            {"configurable": {"strategy": "parent_strategy"}},
        )
    )
