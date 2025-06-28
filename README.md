# 🤖 Smart Chat with Your Documents

Interact intelligently with your PDF documents using this lightweight app built with **LangChain**, **FAISS**, **Streamlit**, and **Groq's blazing-fast LLaMA models**.

---

## 📸 Demo

![Screenshot 1](https://github.com/Taha-bouhafa1/Chat-with-your-pdf-app/blob/main/assets/img_1.png)
![Screenshot 2](https://github.com/Taha-bouhafa1/Chat-with-your-pdf-app/blob/main/assets/img_2.png)

---

## 🛠️ Features

- 📄 Upload and process PDF files  
- 🧠 Chunk text and generate embeddings  
- 📚 Store vectors with FAISS (fast vector DB)  
- 🔎 Ask natural language questions  
- ⚡ Get fast and accurate answers using **Groq's LLaMA 3.3 70B**

---

## 💻 Tech Stack

- **Frontend**: Streamlit  
- **Vector DB**: FAISS  
- **Embeddings**: Google Generative AI  
- **LLM**: Groq API (LLaMA models)  
- **Frameworks**: LangChain  

---

## 📂 Project Structure

```
chat-with-your-pdf/
├── app/
│   ├── pdf_loader.py         # PDF text extraction
│   ├── vector_store.py       # FAISS vector DB setup
│   └── qa_chain.py           # LLM question-answering chain
├── assets/                   # Screenshots and media
├── main.py                   # Streamlit frontend
├── requirements.txt
└── .env                      # API keys
```

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Taha-bouhafa1/Chat-with-your-pdf-app.git
cd Chat-with-your-pdf-app

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys in a .env file
```

**`.env` file format:**
```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

---

## 🚀 Run the App

```bash
streamlit run main.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧠 How It Works

1. Upload one or more PDFs  
2. Text is extracted and split into chunks  
3. Chunks are embedded using Google Generative AI  
4. Stored into FAISS for similarity search  
5. When you ask a question, the app retrieves relevant chunks and queries the LLaMA model via Groq  

---

## 💬 Example Questions

- "Summarize the abstract."  
- "What are the main contributions of the paper?"  
- "What method is used in section 2?"  
- "Who are the authors?"  

---

## 📌 License

MIT License — feel free to use and modify!

---

**Made by Taha Bouhafa**
