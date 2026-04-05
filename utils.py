import re
import pdfplumber


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\+\#]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize(text):
    return set(text.split())


def extract_jd_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def extract_jd_text(jd_input):
    if hasattr(jd_input, "read"):
        return jd_input.read().decode("utf-8", errors="ignore").strip()
    return jd_input.strip()
