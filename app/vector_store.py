from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def store_and_retrieve_docs(documents):

    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectordb=Chroma.from_documents(documents=documents,embedding=embedding)
    retriever=vectordb.retriever()
    return retriever