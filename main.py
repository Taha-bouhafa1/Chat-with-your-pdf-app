import os
from dotenv import load_dotenv
import streamlit as st
from app.pdf_loader import load_pdf
from app.vector_store import store_and_retrieve_docs
from app.qa_chain import run_llm_chain

load_dotenv()

st.set_page_config(
    page_title="📚 AI-Powered PDF Assistant",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    /* Background gradient */
    .reportview-container {
        background: linear-gradient(135deg, #fdf6f0, #f5efe6);
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Title style */
    .title {
        font-size: 3rem;
        font-weight: 700;
        color: #4b3f72;
        margin-bottom: 0.2em;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        text-shadow: 1px 1px 2px #a3a1c1;
    }

    /* Subtitle */
    .subtitle {
        font-size: 1.2rem;
        font-weight: 400;
        color: #7b6f94;
        margin-bottom: 2rem;
        text-align: center;
        font-style: italic;
    }

    /* Button styling */
    div.stButton > button:first-child {
        background: #4b3f72;
        color: white;
        font-weight: 600;
        border-radius: 12px;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background: #6a5ea8;
        color: #f0f0f0;
    }

    /* Input box styling */
    input[type="text"] {
        border-radius: 10px !important;
        border: 2px solid #4b3f72 !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background: #e6e1f7;
        border-radius: 15px;
        padding: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    st.markdown('<h1 class="title">🤖 Smart Chat with Your Documents </h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Upload your PDFs and ask questions easily!</p>', unsafe_allow_html=True)

    if "retriever" not in st.session_state:
        st.session_state["retriever"] = None

    with st.sidebar:
        st.header("📥 Upload PDF Files")
        uploaded_files = st.file_uploader(
            "Choose one or more PDFs", accept_multiple_files=True, type=["pdf"]
        )
        st.markdown(
            """
            ---
            <small>
            ⚠️ Please upload your PDF files and click **Process PDFs**.<br>
            💡 After processing, you can ask questions in the main panel.<br>
            🔐 Your files stay private and are not uploaded anywhere.
            </small>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Process PDFs"):
            if uploaded_files:
                with st.spinner("⏳ Processing PDFs..."):
                    chunks = load_pdf(uploaded_files)
                    st.session_state["retriever"] = store_and_retrieve_docs(chunks)
                st.success("✅ PDFs processed! Ask your questions below.")
            else:
                st.warning("⚠️ Please upload PDF files first.")

    st.markdown("### 💬 Ask your question:")
    question = st.text_input("", placeholder="Type your question here and press Enter...")

    if question:
        if st.session_state["retriever"] is not None:
            with st.spinner("🤖 Generating answer..."):
                answer = run_llm_chain(question, st.session_state["retriever"])
                st.markdown(f"<div style='border-left: 4px solid #4b3f72; padding-left: 15px; margin-top: 15px; font-size: 1.1rem; background:#f3f1f7; border-radius: 10px;'>{answer}</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please process PDF(s) first from the sidebar.")

if __name__ == "__main__":
    main()
