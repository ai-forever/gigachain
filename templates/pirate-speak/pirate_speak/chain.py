from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Translate user input into pirate speak",
        ),
        MessagesPlaceholder("chat_history"),
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
