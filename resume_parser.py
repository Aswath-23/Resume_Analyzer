import pdfplumber


def pdf_to_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def txt_to_text(file):
    return file.read().decode("utf-8", errors="ignore").strip()


def get_text(uploaded_file):
    filename = uploaded_file.name.lower()
    if filename.endswith(".pdf"):
        return pdf_to_text(uploaded_file)
    elif filename.endswith(".txt"):
        return txt_to_text(uploaded_file)
    return ""
