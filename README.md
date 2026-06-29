# 📄 AI-Powered PDF Chatbot

An intelligent chatbot that enables users to interact with PDF documents using Natural Language Processing (NLP) and Large Language Models (LLMs). Upload one or multiple PDF files, ask questions in plain English, and receive accurate, context-aware responses extracted from your documents.

---

## 🚀 Features

* 📂 **Multi-PDF Support** – Upload and analyze one or multiple PDF documents simultaneously.
* 🤖 **AI-Powered Question Answering** – Ask questions in natural language and receive context-aware answers.
* 📑 **Contextual Retrieval** – Retrieves only the most relevant document sections before generating responses.
* ⚡ **Fast Semantic Search** – Uses vector embeddings for efficient document retrieval.
* 💬 **Interactive Chat Interface** – Simple and intuitive Streamlit-based UI for seamless conversations.
* 🔒 **Session-Based Conversations** – Maintains conversation context for a better user experience.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM:** Google Gemini / Google PaLM *(Update based on the model you're currently using)*
* **Embeddings:** Google Generative AI Embeddings
* **Vector Database:** FAISS
* **PDF Processing:** PyPDF2
* **Framework:** LangChain

---

## ⚙️ How It Works

1. Upload one or more PDF documents.
2. The application extracts text from the PDFs.
3. The extracted content is split into manageable chunks.
4. Text embeddings are generated and stored in a FAISS vector database.
5. When a user asks a question, the chatbot retrieves the most relevant chunks.
6. The LLM generates an accurate answer based on the retrieved context.

---

## 🌐 Live Demo

**Deployment:** https://ai-powered-pdf-interaction-bot-main-3.onrender.com/

---

## 📷 Preview

<img width="1912" height="792" alt="image" src="https://github.com/user-attachments/assets/bf896e72-2924-4d22-bdca-b3ab40e1a4fd" />
<img width="515" height="628" alt="image" src="https://github.com/user-attachments/assets/a5ec1eed-3edf-4ea6-a29e-3a3f803f197a" />
<img width="1652" height="488" alt="image" src="https://github.com/user-attachments/assets/afbe549b-e9dc-490c-9449-fda4754513d5" />


---

## 📌 Future Enhancements

* Conversation history
* PDF summarization
* Citation and source highlighting
* Support for DOCX, PPTX, and TXT files
* Authentication and user accounts
* Voice-based interaction

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub!
