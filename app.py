
import streamlit as st
from PyPDF2 import PdfReader

st.title("AI Document Chatbot 📄🤖")

pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf:
    pdf_reader = PdfReader(pdf)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Preview:")
    st.write(text[:1000])

    query = st.text_input("Ask a question:")

    if query:
        if query.lower() in text.lower():
            st.write("Answer found in document.")
        else:
            st.write("Basic demo: integrate AI for better answers.")
