from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def load_pdf(files):
    full_text = ""
    for pdf in files:  # Accept multiple files
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n\n"

    # Split text into bigger chunks (try 5000 tokens)
    splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=200)
    chunks = splitter.split_text(full_text)

    return [Document(page_content=chunk) for chunk in chunks]
