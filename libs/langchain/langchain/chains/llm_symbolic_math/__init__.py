def __getattr__(name: str = "") -> None:
    """Raise an error on import since is deprecated."""
    raise AttributeError(
        "This module has been moved to langchain-experimental. "
        "For more details: https://github.com/langchain-ai/langchain/discussions/11352."
<<<<<<< HEAD
        "To access this code, install it with `pip install gigachain-experimental`."
=======
        "To access this code, install it with `pip install langchain-experimental`."
>>>>>>> langchan/master
        "`from langchain_experimental.llm_symbolic_math.base "
        "import LLMSymbolicMathChain`"
    )
