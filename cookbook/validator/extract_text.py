import logging

from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def extract_text_with_pdfminer(pdf_path: str) -> str:
    """
    Extract text from PDF using pdfminer.six (slower but handles complex layouts better)

    Args:
        pdf_path: Path to PDF file

    Returns:
        Extracted text or None if extraction fails
    """
    try:
        laparams = LAParams(
            line_overlap=0.5,
            char_margin=2.0,
            line_margin=0.5,
            word_margin=0.1,
            boxes_flow=0.5,
            detect_vertical=True
        )
        return extract_text(pdf_path, laparams=laparams)
    except Exception as e:
        logger.error("Error extracting text from PDF: %s", e)
        return None
