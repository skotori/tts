from docx import Document

def do_read(file_path):
    doc = Document(file_path)

    text = ''
    for para in doc.paragraphs:
        text = text + para.text + ' '

    return text
