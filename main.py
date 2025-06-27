import gradio as gr
from app.pdf_loader import load_pdf
from app.vector_store import store_and_retrieve_docs
from app.qa_chain import run_llm_chain

retriever = None

def upload_pdf(file):
    global retriever
    chunks = load_pdf(file)
    retriever = store_and_retrieve_docs(chunks)
    return "✅ PDF uploaded and processed. You can now ask your question."

def answer_question(question):
    if not retriever:
        return "❌ Please upload a PDF first."
    return run_llm_chain(question, retriever)

with gr.Blocks() as demo:
    gr.Markdown("# 📄 Chat with your PDF")
    with gr.Row():
        pdf_input = gr.File(label="Upload your PDF", file_types=[".pdf"])
        upload_button = gr.Button("Process PDF")
    output_status = gr.Textbox(label="Status")

    with gr.Row():
        question_input = gr.Textbox(label="Your Question")
        answer_output = gr.Textbox(label="Answer")

    upload_button.click(fn=upload_pdf, inputs=pdf_input, outputs=output_status)
    question_input.submit(fn=answer_question, inputs=question_input, outputs=answer_output)

if __name__ == "__main__":
    demo.launch()
