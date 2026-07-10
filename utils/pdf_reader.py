"""
pdf_reader.py
-----------------------------------
Utility for extracting text from PDF files.

Uses:
1. pdfplumber (Primary)
2. PyPDF2 (Fallback)
"""

import pdfplumber
from PyPDF2 import PdfReader


def read_pdf(file_path):
    """
    Extract text from a PDF file.

    Parameters:
        file_path (str): Path to the uploaded PDF.

    Returns:
        str: Extracted text from all pages.
    """

    extracted_text = ""

    # -------------------------------------------------
    # Try using pdfplumber (Best for medical reports)
    # -------------------------------------------------

    try:
        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

        return extracted_text.strip()

    except Exception as e:

        print("pdfplumber failed:", e)

    # -------------------------------------------------
    # Fallback using PyPDF2
    # -------------------------------------------------

    try:

        reader = PdfReader(file_path)

        for page in reader.pages:

            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

        return extracted_text.strip()

    except Exception as e:

        print("PyPDF2 failed:", e)

        return ""