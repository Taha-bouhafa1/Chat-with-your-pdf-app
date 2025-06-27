import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def load_pdf(file_path):
    print("[DEBUG] Opening PDF:", file_path)
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    print("[DEBUG] Total text length:", len(full_text))

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(full_text)
    print("[DEBUG] Total chunks:", len(chunks))

    return [Document(page_content=chunk) for chunk in chunks]
