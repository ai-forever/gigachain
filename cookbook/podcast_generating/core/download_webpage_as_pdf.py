#!/usr/bin/env python3
"""
Script to download web pages and convert them to PDF format.
Supports multiple methods: weasyprint (recommended) and pdfkit (alternative).
"""

import pdfkit
from pathlib import Path
from urllib.parse import urlparse


def download_webpage_as_pdf_pdfkit(url, output_filename=None, output_dir=".", verbose: bool = False):
    """
    Download a web page and convert it to PDF using pdfkit
    
    Args:
        url (str): The URL of the web page to download
        output_filename (str): Optional output filename. If None, will use domain name
        output_dir (str): Directory to save the PDF file
    
    Returns:
        str: Path to the generated PDF file
    """
    try:
        # Generate output filename if not provided
        if output_filename is None:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc.replace('.', '_')
            path = parsed_url.path.strip('/').replace('/', '_')
            if not path:
                path = "index"
            output_filename = f"{domain}_{path}.pdf"
        
        # Ensure the filename ends with .pdf
        if not output_filename.endswith('.pdf'):
            output_filename += '.pdf'
        
        # Create output directory if it doesn't exist
        output_path = Path(output_dir) / output_filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Configure pdfkit options
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None,
            'quiet': ''
        }
        
        print(f"Converting {url} to PDF: {output_path}")
        pdfkit.from_url(url, str(output_path), options=options)
        
        print(f"Successfully created PDF: {output_path}")
        return str(output_path)
        
    except Exception as e:
        print(f"Error: {e}")
        return None