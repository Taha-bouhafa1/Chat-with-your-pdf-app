import os
from langchain_groq import ChatGroq
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def run_llm_chain(question, retriever):
    groq_api_key = os.getenv("GROQ_API_KEY")
    print("Using GROQ_API_KEY:", groq_api_key is not None)

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt_template = """
    Answer the question as detailed as possible from the provided context. 
    If answer is not in context, say 'answer not available in context'.

    Context: {context}
    Question: {question}
    Answer:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    qa_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

    docs = retriever.get_relevant_documents(question)

    response = qa_chain({"input_documents": docs, "question": question}, return_only_outputs=True)
    return response["output_text"]
