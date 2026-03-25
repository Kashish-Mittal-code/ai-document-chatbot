import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

st.title("AI Document Chatbot (RAG) 📄🤖")

# Upload PDF
pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf:
    pdf_reader = PdfReader(pdf)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    # Split text
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)

    # Create embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # Ask question
    query = st.text_input("Ask a question about your document:")

    if query:
        docs = knowledge_base.similarity_search(query)
        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=query)

        st.write("Answer:")
        st.write(response)
