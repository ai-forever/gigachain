#!/usr/bin/env python3
"""
Standalone PDF Text Extractor

A simple tool to extract text from PDF files using PyMuPDF (fitz).
Outputs as plain text.

Usage:
    python pdf_text_extractor.py <pdf_file> [output_file]
    
Examples:
    python pdf_text_extractor.py document.pdf
    python pdf_text_extractor.py document.pdf output.txt
"""

from pathlib import Path
import logging
import fitz  # PyMuPDF


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def extract_text(pdf_path: Path) -> str:
    """Extract text using PyMuPDF."""
    text_parts = []
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        try:
            page = doc.load_page(page_num)
            page_text = page.get_text()
            if page_text.strip():
                text_parts.append(page_text)
        except Exception as e:
            logger.warning(f"Failed to extract text from page {page_num + 1}: {e}")
    
    doc.close()
    return "\n\n".join(text_parts)
