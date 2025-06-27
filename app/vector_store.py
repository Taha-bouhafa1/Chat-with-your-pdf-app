import os
import time
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def store_and_retrieve_docs(documents):
    try:
        print("[DEBUG] Starting embedding and vector store")

        # ✅ Force CPU and disable normalization for speed
        embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": False}
        )
        print("[DEBUG] Embedding model loaded")

        # ✅ Setup Chroma persist dir
        persist_dir = os.path.join(os.getcwd(), "chroma_langchain_db")
        print("[DEBUG] Persist dir:", persist_dir)

        # ✅ Create Chroma vector store object
        vectordb = Chroma(
            collection_name="pdf_collection",
            embedding_function=embedding,
            persist_directory=persist_dir,
        )
        print("[DEBUG] Vector store object created")

        # ✅ Extract text content from LangChain Document objects
        texts = [doc.page_content for doc in documents if doc.page_content.strip()]
        print("[DEBUG] Total texts to add:", len(texts))

        # ✅ Manual embedding test
        start = time.time()
        print("[DEBUG] Starting embedding manually...")

        batch_size = 10
        vectors = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            print(f"[DEBUG] Embedding batch {i} to {i + len(batch)}...")
            batch_vectors = embedding.embed_documents(batch)
            vectors.extend(batch_vectors)

        print(f"[DEBUG] Got total {len(vectors)} vectors in {round(time.time() - start, 2)}s")

        # ✅ Now add texts to Chroma (embedding will be reused)
        vectordb.add_texts(texts)
        print("[DEBUG] Texts added to Chroma")

        retriever = vectordb.as_retriever()
        print("[DEBUG] Retriever ready")

        return retriever

    except Exception as e:
        print("[❌ ERROR in vector_store]", str(e))
        raise e
