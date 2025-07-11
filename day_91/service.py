import fitz

def get_text_from_pdf(file_path)->str:
    doc = fitz.open(file_path)

    text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        text += page.get_text()

    doc.close()

    return text