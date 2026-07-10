"""
image_reader.py
---------------------------------------
Extract text from medical report images
using EasyOCR.
"""

import easyocr


def read_image(image_path):
    """
    Extract text from an image.

    Parameters:
        image_path (str): Path to image.

    Returns:
        str: Extracted text.
    """

    try:

        # Create OCR Reader
        reader = easyocr.Reader(['en'], gpu=False)

        # Read text
        results = reader.readtext(image_path)

        extracted_text = ""

        for result in results:
            extracted_text += result[1] + "\n"

        return extracted_text.strip()

    except Exception as e:

        print("EasyOCR Error:", e)

        return ""