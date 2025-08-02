import logging
import os
import json
from dotenv import find_dotenv, load_dotenv
from langchain_gigachat.chat_models.gigachat import GigaChat
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import getpass

from cookbook.validator.extract_text import extract_text_with_pdfminer

load_dotenv(find_dotenv())


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def analyse_article(article_text: str):
    """
    Analyze an article using GigaChain for scientific research.
    """

    client = GigaChat(
        model="GigaChat-2-Max",
        verify_ssl_certs=False,
        credentials=os.getenv('GIGACHAT_CREDENTIALS')
    )

    analysis_prompt = ChatPromptTemplate.from_messages([
        ("system", """
        Вы - профессор физики с междисциплинарным опытом (от биологии до нанотехнологий),
        работающий редактором в престижном научном журнале. Анализируйте статьи с максимальной объективностью.

        Протокол анализа:
        1. Создайте краткое содержание (150-200 слов)
        2. Сравните аннотацию с основным текстом
        3. Проверьте наличие идеологических предвзятостей
        4. Выявите логические ошибки
        5. Оцените соответствие научной парадигме

        Вывод в СТРОГОМ формате на русском языке:
        {{
            "summary": "Краткое содержание",
            "abstract_analysis": {{
                "match_score": "X%",
                "discrepancies": ["список расхождений"],
                "omissions": ["список упущений"]
            }},
            "ideological_issues": {{
                "unsupported_claims": ["список неподтверждённых утверждений"],
                "speculative_statements": ["список спекулятивных заявлений"]
            }},
            "logical_errors": {{
                "fallacies": ["список логических ошибок"],
                "sections": ["номера разделов"]
            }},
            "paradigm_compliance": {{
                "level": "Высокое/Среднее/Низкое",
                "anomalies": ["список аномалий"]
            }},
            "recommendation": {{
                "decision": "Принять/Доработать/Отклонить",
                "reasoning": "Техническое обоснование"
            }}
        }}
        """),
        ("human", "Текст статьи: {input_text}")
    ])

    output_parser = StrOutputParser()

    try:
        chain = analysis_prompt | client | output_parser
        result = chain.invoke({"input_text": article_text})

        return json.loads(result.strip())

    except json.JSONDecodeError as e:
        logger.error("Failed to parse analysis results: %s", e)
        return {"error": "Failed to parse analysis results"}
    except Exception as e:
        logger.error("Failed to parse analysis results: %s", e)
        return {"error": str(e)}


if __name__ == "__main__":
    if "GIGACHAT_CREDENTIALS" not in os.environ:
        os.environ["GIGACHAT_CREDENTIALS"] = getpass.getpass("Введите ключ авторизации GigaChat API: ")

    article_path = ''
    if not article_path:
        getpass.getpass("Укажите полный путь до анализируемой научной статьи: ")

    article_content = extract_text_with_pdfminer(article_path)

    analysis_result = analyse_article(article_content)

    print(json.dumps(analysis_result, indent=2, ensure_ascii=False))
