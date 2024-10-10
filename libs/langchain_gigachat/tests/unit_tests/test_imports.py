from langchain_gigachat import __all__

EXPECTED_ALL = ["GigaChat", "GigaChatEmbeddings"]


def test_all_imports() -> None:
    assert sorted(EXPECTED_ALL) == sorted(__all__)
