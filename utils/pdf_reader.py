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
        str | None:
            Extracted text if successful,
            None if PDF cannot be read.
    """

    extracted_text = ""

    # -------------------------------------------------
    # Primary Method - pdfplumber
    # -------------------------------------------------

    try:

        with pdfplumber.open(file_path) as pdf:

            if len(pdf.pages) == 0:
                return None

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

        if extracted_text.strip():
            return extracted_text.strip()

    except Exception as e:

        print(f"[PDF Reader] pdfplumber failed: {e}")

    # -------------------------------------------------
    # Fallback Method - PyPDF2
    # -------------------------------------------------

    extracted_text = ""

    try:

        reader = PdfReader(file_path)

        if len(reader.pages) == 0:
            return None

        for page in reader.pages:

            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

        if extracted_text.strip():
            return extracted_text.strip()

    except Exception as e:

        print(f"[PDF Reader] PyPDF2 failed: {e}")

    # -------------------------------------------------
    # Failed to read PDF
    # -------------------------------------------------

    return None