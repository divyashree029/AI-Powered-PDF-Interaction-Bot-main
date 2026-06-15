import streamlit as st
from PyPDF2 import PdfReader
import cohere
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI


# ==========================
# OPENROUTER CONFIG
# ==========================

import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ==========================
# PDF TEXT EXTRACTION
# ==========================

def get_pdf_text(pdf_docs):

    text = ""

    for pdf in pdf_docs:

        pdf_reader = PdfReader(pdf)

        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


# ==========================
# TEXT CHUNKING
# ==========================

def get_text_chunks(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(text)

    return chunks


# ==========================
# VECTOR STORE
# ==========================

def get_vector_store(text_chunks):

    co = cohere.Client(os.getenv("COHERE_API_KEY"))

    embeddings = []

    for chunk in text_chunks:
        response = co.embed(
            texts=[chunk],
            model="embed-english-v3.0",
            input_type="search_document"
        )
        embeddings.append(response.embeddings[0])

    import faiss
    import numpy as np

    vector_store = FAISS.from_embeddings(
        text_embeddings=list(zip(text_chunks, embeddings)),
        embedding=None
    )

    return vector_store


# ==========================
# LLM CHAIN
# ==========================

def get_conversational_chain(vector_store):

    llm = ChatOpenAI(
        model="google/gemini-2.5-flash",
        openai_api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
        max_tokens=512
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(
            search_kwargs={"k": 1}
        ),
        memory=memory
    )

    return conversation_chain


# ==========================
# USER QUERY
# ==========================

def user_input(user_question):

    response = st.session_state.conversation(
        {"question": user_question}
    )

    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):

        if i % 2 == 0:
            st.write("🧑 Human:", message.content)

        else:
            st.write("🤖 Bot:", message.content)


# ==========================
# MAIN APP
# ==========================

def main():

    st.set_page_config(
        page_title="PDF ChatBot",
        page_icon="📄"
    )

    st.header("📄 Chat With Your PDF")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    user_question = st.text_input(
        "Ask a question about your PDF"
    )

    if user_question:

        if st.session_state.conversation is None:

            st.error(
                "Please upload and process a PDF first."
            )

        else:

            user_input(user_question)

    with st.sidebar:

        st.title("Settings")

        pdf_docs = st.file_uploader(
            "Upload PDF files",
            accept_multiple_files=True
        )

        if st.button("Process"):

            if not pdf_docs:

                st.warning(
                    "Please upload at least one PDF."
                )

                return

            with st.spinner("Processing PDF..."):

                raw_text = get_pdf_text(pdf_docs)

                text_chunks = get_text_chunks(raw_text)

                st.write(
                    f"Chunks created: {len(text_chunks)}"
                )

                vector_store = get_vector_store(
                    text_chunks
                )

                st.session_state.conversation = (
                    get_conversational_chain(
                        vector_store
                    )
                )

                st.success(
                    "PDF processed successfully!"
                )


if __name__ == "__main__":
    main()