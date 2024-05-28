"""Test BigdlLLM"""
<<<<<<< HEAD

=======
import os

import pytest
>>>>>>> langchan/master
from langchain_core.outputs import LLMResult

from langchain_community.llms.bigdl_llm import BigdlLLM

<<<<<<< HEAD

def test_call() -> None:
    """Test valid call to bigdl-llm."""
    llm = BigdlLLM.from_model_id(
        model_id="lmsys/vicuna-7b-v1.5",
        model_kwargs={"temperature": 0, "max_length": 16, "trust_remote_code": True},
    )
    output = llm("Hello!")
    assert isinstance(output, str)


def test_generate() -> None:
    """Test valid call to bigdl-llm."""
    llm = BigdlLLM.from_model_id(
        model_id="lmsys/vicuna-7b-v1.5",
=======
model_ids_to_test = os.getenv("TEST_BIGDLLLM_MODEL_IDS") or ""
skip_if_no_model_ids = pytest.mark.skipif(
    not model_ids_to_test,
    reason="TEST_BIGDLLLM_MODEL_IDS environment variable not set.",
)
model_ids_to_test = [model_id.strip() for model_id in model_ids_to_test.split(",")]  # type: ignore


@skip_if_no_model_ids
@pytest.mark.parametrize(
    "model_id",
    model_ids_to_test,
)
def test_call(model_id: str) -> None:
    """Test valid call to bigdl-llm."""
    llm = BigdlLLM.from_model_id(
        model_id=model_id,
        model_kwargs={"temperature": 0, "max_length": 16, "trust_remote_code": True},
    )
    output = llm.invoke("Hello!")
    assert isinstance(output, str)


@skip_if_no_model_ids
@pytest.mark.parametrize(
    "model_id",
    model_ids_to_test,
)
def test_generate(model_id: str) -> None:
    """Test valid call to bigdl-llm."""
    llm = BigdlLLM.from_model_id(
        model_id=model_id,
>>>>>>> langchan/master
        model_kwargs={"temperature": 0, "max_length": 16, "trust_remote_code": True},
    )
    output = llm.generate(["Hello!"])
    assert isinstance(output, LLMResult)
    assert isinstance(output.generations, list)
