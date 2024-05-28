<<<<<<< HEAD
from typing import Any, Dict, List, Mapping, Optional

from langchain_core.embeddings import Embeddings
from langchain_core.pydantic_v1 import BaseModel, Extra, Field, root_validator
from langchain_core.utils import get_from_dict_or_env

DEFAULT_EMBED_INSTRUCTION = "Represent this input: "
DEFAULT_QUERY_INSTRUCTION = "Represent the question for retrieving similar documents: "


class OctoAIEmbeddings(BaseModel, Embeddings):
    """OctoAI Compute Service embedding models.

    The environment variable ``OCTOAI_API_TOKEN`` should be set
    with your API token, or it can be passed
    as a named parameter to the constructor.
    """

    endpoint_url: Optional[str] = Field(None, description="Endpoint URL to use.")
    model_kwargs: Optional[dict] = Field(
        None, description="Keyword arguments to pass to the model."
    )
    octoai_api_token: Optional[str] = Field(None, description="OCTOAI API Token")
    embed_instruction: str = Field(
        DEFAULT_EMBED_INSTRUCTION,
        description="Instruction to use for embedding documents.",
    )
    query_instruction: str = Field(
        DEFAULT_QUERY_INSTRUCTION, description="Instruction to use for embedding query."
    )

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator(allow_reuse=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Ensure that the API key and python package exist in environment."""
        values["octoai_api_token"] = get_from_dict_or_env(
            values, "octoai_api_token", "OCTOAI_API_TOKEN"
        )
        values["endpoint_url"] = get_from_dict_or_env(
            values, "endpoint_url", "https://text.octoai.run/v1/embeddings"
        )
        return values

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Return the identifying parameters."""
        return {
            "endpoint_url": self.endpoint_url,
            "model_kwargs": self.model_kwargs or {},
        }

    def _compute_embeddings(
        self, texts: List[str], instruction: str
    ) -> List[List[float]]:
        """Compute embeddings using an OctoAI instruct model."""
        from octoai import client

        embedding = []
        embeddings = []
        octoai_client = client.Client(token=self.octoai_api_token)

        for text in texts:
            parameter_payload = {
                "sentence": str([text]),
                "input": str([text]),
                "instruction": str([instruction]),
                "model": "thenlper/gte-large",
                "parameters": self.model_kwargs or {},
            }

            try:
                resp_json = octoai_client.infer(self.endpoint_url, parameter_payload)
                if "embeddings" in resp_json:
                    embedding = resp_json["embeddings"]
                elif "data" in resp_json:
                    json_data = resp_json["data"]
                    for item in json_data:
                        if "embedding" in item:
                            embedding = item["embedding"]

            except Exception as e:
                raise ValueError(f"Error raised by the inference endpoint: {e}") from e

            embeddings.append(embedding)

        return embeddings

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Compute document embeddings using an OctoAI instruct model."""
        texts = list(map(lambda x: x.replace("\n", " "), texts))
        return self._compute_embeddings(texts, self.embed_instruction)

    def embed_query(self, text: str) -> List[float]:
        """Compute query embedding using an OctoAI instruct model."""
        text = text.replace("\n", " ")
        return self._compute_embeddings([text], self.query_instruction)[0]
=======
from typing import Dict

from langchain_core.pydantic_v1 import Field, SecretStr, root_validator
from langchain_core.utils import convert_to_secret_str, get_from_dict_or_env

from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.utils.openai import is_openai_v1

DEFAULT_API_BASE = "https://text.octoai.run/v1/"
DEFAULT_MODEL = "thenlper/gte-large"


class OctoAIEmbeddings(OpenAIEmbeddings):
    """OctoAI Compute Service embedding models.

    See https://octo.ai/ for information about OctoAI.

    To use, you should have the ``openai`` python package installed and the
    environment variable ``OCTOAI_API_TOKEN`` set with your API token.
    Alternatively, you can use the octoai_api_token keyword argument.
    """

    octoai_api_token: SecretStr = Field(default=None)
    """OctoAI Endpoints API keys."""
    endpoint_url: str = Field(default=DEFAULT_API_BASE)
    """Base URL path for API requests."""
    model: str = Field(default=DEFAULT_MODEL)
    """Model name to use."""
    tiktoken_enabled: bool = False
    """Set this to False for non-OpenAI implementations of the embeddings API"""

    @property
    def _llm_type(self) -> str:
        """Return type of embeddings model."""
        return "octoai-embeddings"

    @property
    def lc_secrets(self) -> Dict[str, str]:
        return {"octoai_api_token": "OCTOAI_API_TOKEN"}

    @root_validator()
    def validate_environment(cls, values: dict) -> dict:
        """Validate that api key and python package exists in environment."""
        values["endpoint_url"] = get_from_dict_or_env(
            values,
            "endpoint_url",
            "ENDPOINT_URL",
            default=DEFAULT_API_BASE,
        )
        values["octoai_api_token"] = convert_to_secret_str(
            get_from_dict_or_env(values, "octoai_api_token", "OCTOAI_API_TOKEN")
        )
        values["model"] = get_from_dict_or_env(
            values,
            "model",
            "MODEL",
            default=DEFAULT_MODEL,
        )

        try:
            import openai

            if is_openai_v1():
                client_params = {
                    "api_key": values["octoai_api_token"].get_secret_value(),
                    "base_url": values["endpoint_url"],
                }
                if not values.get("client"):
                    values["client"] = openai.OpenAI(**client_params).embeddings
                if not values.get("async_client"):
                    values["async_client"] = openai.AsyncOpenAI(
                        **client_params
                    ).embeddings
            else:
                values["openai_api_base"] = values["endpoint_url"]
                values["openai_api_key"] = values["octoai_api_token"].get_secret_value()
                values["client"] = openai.Embedding
                values["async_client"] = openai.Embedding

        except ImportError:
            raise ImportError(
                "Could not import openai python package. "
                "Please install it with `pip install openai`."
            )

        return values
>>>>>>> langchan/master
