"""Tool for the Wikipedia API."""

<<<<<<< HEAD
from typing import Optional

from langchain_core.callbacks import CallbackManagerForToolRun
=======
from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Field
>>>>>>> langchan/master
from langchain_core.tools import BaseTool

from langchain_community.utilities.wikipedia import WikipediaAPIWrapper


<<<<<<< HEAD
=======
class WikipediaQueryInput(BaseModel):
    """Input for the WikipediaQuery tool."""

    query: str = Field(description="query to look up on wikipedia")


>>>>>>> langchan/master
class WikipediaQueryRun(BaseTool):
    """Tool that searches the Wikipedia API."""

    name: str = "wikipedia"
    description: str = (
        "A wrapper around Wikipedia. "
        "Useful for when you need to answer general questions about "
        "people, places, companies, facts, historical events, or other subjects. "
        "Input should be a search query."
    )
    api_wrapper: WikipediaAPIWrapper

<<<<<<< HEAD
=======
    args_schema: Type[BaseModel] = WikipediaQueryInput

>>>>>>> langchan/master
    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Wikipedia tool."""
        return self.api_wrapper.run(query)
