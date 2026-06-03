# RAG PDF Chatbot

A simple Retrieval-Augmented Generation (RAG) application built with Streamlit, LangChain, ChromaDB, and Ollama.

## Features

* Upload PDF documents
* Extract text from PDFs
* Generate embeddings using Ollama
* Store embeddings in ChromaDB
* Ask questions about uploaded documents
* Retrieve relevant context and generate answers using Gemma

## Tech Stack

* Streamlit
* LangChain
* ChromaDB
* Ollama
* PyPDF

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Models Used

* gemma4:e2b
* embeddinggemma:latest

## Architecture

PDF → Text Extraction → Chunking → Embeddings → ChromaDB → Retrieval → LLM → Answer
