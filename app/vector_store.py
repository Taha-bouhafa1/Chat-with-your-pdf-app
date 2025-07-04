import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def store_and_retrieve_docs(documents):
    texts = [doc.page_content for doc in documents if doc.page_content.strip()]
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vector_store = FAISS.from_texts(texts, embeddings)

    persist_dir = os.path.join(os.getcwd(), "faiss_index")
    vector_store.save_local(persist_dir)

    retriever = FAISS.load_local(persist_dir, embeddings, allow_dangerous_deserialization=True).as_retriever()
    return retriever
