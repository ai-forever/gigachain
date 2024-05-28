from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant who speaks like a pirate",
        ),
        ("human", "{text}"),
    ]
)
_model = ChatOpenAI()

# if you update this, you MUST also update ../pyproject.toml
<<<<<<< HEAD
# with the new `tool.gigaserve.export_attr`
=======
# with the new `tool.langserve.export_attr`
>>>>>>> langchan/master
chain = _prompt | _model
