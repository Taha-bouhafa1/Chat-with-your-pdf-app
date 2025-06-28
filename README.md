# 🧠 Chat With Your PDF

A simple and efficient app to **interact with your PDF documents** using **Local Embeddings + RAG (Retrieval-Augmented Generation)**.

Built with:
- 🧠 `LangChain` for orchestration
- 🔍 `Chroma` for vector search
- 💬 `Gradio` for web UI
- 🔗 `HuggingFace` (MiniLM) for embeddings
- 🤖 (Optional) Groq API for LLM responses

---

## 🚀 Features

- ✅ Upload any PDF and chat with its contents
- ✅ Automatically extracts, chunks, and embeds your document
- ✅ Vector search with ChromaDB
- ✅ Clean and lightweight Gradio UI
- ✅ Local embedding with HuggingFace models (no OpenAI key needed)
- ✅ Easily extendable to use **Groq**, **OpenAI**, or any LLM

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/chat-with-your-pdf.git
cd chat-with-your-pdf

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
## 🧪 Run the App
```
```bash
python main.py
```
Then open: http://localhost:7860
## 📂 Project Structure
chat-with-your-pdf/
│
├── app/
│   ├── pdf_loader.py         # Loads and chunks PDF text
│   ├── vector_store.py       # Embeds and stores text in Chroma
│   ├── qa_chain.py           # Runs LLM over retrieved chunks
│
├── main.py                   # Gradio UI
├── requirements.txt
├── README.md

## 💡 Example Models

| Type             | Model Name                                        |
|------------------|--------------------------------------------------|
| Embedding Model  | `sentence-transformers/all-MiniLM-L6-v2`         |
| Chat Model (LLM) | `meta-llama/llama-4-scout-17b-16e-instruct` (via Groq) |

## 📌 Future Improvements

- Add support for multiple PDFs  
- Chat memory / history  
- File download for summaries  
- Upload `.txt` or `.docx` support  

---

## 🧑‍💻 Author

**Taha Bouhafa**  
Big Data & AI Engineer | NLP & LLM Enthusiast
