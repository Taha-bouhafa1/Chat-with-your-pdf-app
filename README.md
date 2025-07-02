# 🤖 Smart Chat with Your Documents

Interact intelligently with PDF documents using this lightweight app built with **LangChain**, **FAISS**, **Streamlit**, and **Groq's LLaMA models**.

---

## Demo

![Screenshot 1](https://github.com/Taha-bouhafa1/Chat-with-your-pdf-app/blob/main/assets/img_1.png)
![Screenshot 2](https://github.com/Taha-bouhafa1/Chat-with-your-pdf-app/blob/main/assets/img_2.png)

---


## Architecture Diagram

![Architecture Diagram](https://github.com/Taha-bouhafa1/Chat-with-your-pdf-app/blob/main/assets/chatbot-pdf-diagr.png)

---

## Features

- Upload and process PDF files  
- Split and embed document text  
- Store and search vectors using FAISS  
- Ask natural language questions  
- Retrieve accurate answers using Groq's LLaMA 3.3 70B model

---

## Tech Stack

- **Frontend**: Streamlit  
- **Vector Store**: FAISS  
- **Embeddings**: Google Generative AI  
- **LLM**: Groq API (LLaMA models)  
- **Framework**: LangChain  

---

## Project Structure

```
chat-with-your-pdf/
├── app/
│   ├── pdf_loader.py         # PDF text extraction
│   ├── vector_store.py       # FAISS vector store setup
│   └── qa_chain.py           # Question-answering logic
├── assets/                   # Demo screenshots
├── main.py                   # Streamlit interface
├── requirements.txt          # Python dependencies
└── .env                      # API keys (not tracked)
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Taha-bouhafa1/Chat-with-your-pdf-app.git
cd Chat-with-your-pdf-app

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the root directory with the following format:

```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

---

## Running the App

```bash
streamlit run main.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## How It Works

1. Upload one or more PDF documents  
2. The text is extracted and chunked  
3. Each chunk is embedded using Google Generative AI  
4. Embeddings are stored in a FAISS vector database  
5. When a question is asked, relevant chunks are retrieved and passed to Groq’s LLaMA model for answering

---

## Example Questions

- Summarize the abstract  
- What are the main contributions of the paper?  
- What method is used in section 2?  
- Who are the authors?  

---

## License

This project is licensed under the MIT License.

---

**Made by Taha Bouhafa**
