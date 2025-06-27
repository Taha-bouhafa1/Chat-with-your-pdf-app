from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

def run_llm_chain(question, retriever):
    llm = ChatOpenAI(
        model_name="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0
    )
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    answer = qa_chain.run(question)
    return answer
