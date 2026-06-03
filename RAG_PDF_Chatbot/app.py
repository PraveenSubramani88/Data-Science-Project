import streamlit as st
from pypdf import PdfReader
import uuid
import shutil
import os
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Configuration & Constants
DB_PATH = "C:/_BigDataCourses/_2026/_Project/VectorDatabase/chroma_db"
COLLECTION_NAME = "pdf_rag_collection"

# 2. Initialize Models
llm = OllamaLLM(model="gemma4:e2b")
embeddings = OllamaEmbeddings(model="embeddinggemma:latest")

# 3. Initialize Vector Store
vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=DB_PATH
)

# 4. Session State Management
if "processed" not in st.session_state:
    st.session_state.processed = False

# UI Layout
st.title("RAG PDF Chatbot")

# Sidebar button to safely reset database dimensions if needed
with st.sidebar:
    if st.button("Reset Vector Database"):
        if os.path.exists(DB_PATH):
            shutil.rmtree(DB_PATH) # Deletes physical files to clear dimension lock
            st.success("Database cleared! Restart Streamlit now.")
            st.rerun()

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# 5. PDF PROCESSING (Runs once per file upload)
if uploaded_file is not None and not st.session_state.processed:
    with st.spinner("Processing PDF and generating embeddings..."):
        try:
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted
            
            # Chunking
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
            chunks = splitter.split_text(text)

            # Store in ChromaDB
            ids = [str(uuid.uuid4()) for _ in chunks]
            vector_store.add_texts(texts=chunks, ids=ids)

            st.session_state.processed = True
            st.success(f"Successfully processed {len(chunks)} chunks!")
            st.rerun() # Refresh page to show the QA interface

        except Exception as e:
            st.error(f"Error processing PDF: {e}")

# 6. QUESTION & ANSWERING (Kept outside the file uploader block)
if st.session_state.processed:
    st.write("---")
    query = st.text_input("Ask a question about the document:")

    if query:
        with st.spinner("Searching document and thinking..."):
            # Retrieval
            retriever = vector_store.as_retriever(search_kwargs={"k": 4})
            docs = retriever.invoke(query)

            context = "\n\n".join([doc.page_content for doc in docs])

            # Prompt Construction
            prompt = f"""
            You are a PDF assistant.

            Use ONLY the provided context.
            If the answer is not found, say:
            "I could not find that in the document."

            Context:
            {context}

            Question:
            {query}

            Answer:
            """

            # Generation
            response = llm.invoke(prompt)

            # UI Display
            st.write("### Answer")
            st.info(response)

            with st.expander("See Retrieved Context Chunks"):
                st.write(context)
