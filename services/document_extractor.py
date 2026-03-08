import pdfplumber
import pytesseract
from PIL import Image
from docx import Document
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file):

    filename = file.filename.lower()

    # read file safely
    contents = file.file.read()
    file_stream = io.BytesIO(contents)

    text = ""

    # -------- PDF --------
    if filename.endswith(".pdf"):

        with pdfplumber.open(file_stream) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        return text

    # -------- IMAGE --------
    elif filename.endswith((".png", ".jpg", ".jpeg")):

        image = Image.open(file_stream)
        text = pytesseract.image_to_string(image)

        return text

    # -------- DOCX --------
    elif filename.endswith(".docx"):

        doc = Document(file_stream)

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    else:
        return ""