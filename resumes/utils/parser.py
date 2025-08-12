from pdfminer.high_level import extract_text as pdfminer_extract
from pdf2image import convert_from_path
import pytesseract

def extract_text(file_path):
    try:
        text = pdfminer_extract(file_path)
        if text.strip():
            return text
    except Exception:
        pass  # Silence pdfminer failure

    try:
        images = convert_from_path(file_path)
        ocr_text = ''
        for img in images:
            ocr_text += pytesseract.image_to_string(img)
        return ocr_text
    except Exception as e:
        print("❌ OCR failed:", e)
        return ''