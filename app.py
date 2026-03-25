import streamlit as st

st.title("AI Document Chatbot 📄")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    text = uploaded_file.read().decode("latin-1", errors="ignore")
    
    st.subheader("Document Content Preview:")
    st.write(text[:1000])

    query = st.text_input("Ask something about the document:")

    if query:
        st.write("This is a basic demo response. Integrate OpenAI for real answers.")
