
# AVIVO RAG Telegram Bot

## Overview

AVIVO RAG Telegram Bot is a lightweight Retrieval-Augmented Generation (RAG) application that answers user questions using a local knowledge base.

The system retrieves relevant document chunks from a vector database and uses a local Large Language Model (LLM) to generate grounded responses. The bot is accessible through Telegram and also includes an optional Gradio interface for local testing and debugging.

---

## Features

* Telegram Bot Interface
* Gradio Debug UI (Optional)
* Retrieval-Augmented Generation (RAG)
* ChromaDB Vector Database
* Local Embeddings
* Local LLM Inference
* Source Attribution
* Query Caching
* Conversation Memory (Last 3 Interactions)
* Hallucination Guardrails

---

## System Architecture

### Query Flow

```text
User
  ↓
Telegram Bot (/ask)
  ↓
Query Processing
  ↓
ChromaDB Retrieval
  ↓
Top-K Relevant Chunks
  ↓
Prompt Construction
  ↓
Llama 3.2 (Ollama)
  ↓
Generated Answer
  ↓
Telegram Response
```

### Document Ingestion Flow

```text
Markdown Documents
        ↓
Text Chunking
        ↓
Embeddings (all-MiniLM-L6-v2)
        ↓
ChromaDB
```

---

## Models and Technologies Used

| Component              | Technology          |
| ---------------------- | ------------------- |
| Bot Framework          | python-telegram-bot |
| Vector Database        | ChromaDB            |
| Embedding Model        | all-MiniLM-L6-v2    |
| LLM                    | llama3.2            |
| LLM Runtime            | Ollama              |
| Environment Management | Conda               |
| Optional UI            | Gradio              |

### Why These Models?

#### all-MiniLM-L6-v2

* Lightweight and fast
* Good semantic search performance
* Small memory footprint
* Well suited for local RAG systems

#### llama3.2

* Runs locally through Ollama
* No external API costs
* Privacy-friendly
* Good balance between speed and response quality

#### ChromaDB

* Lightweight vector database
* Persistent local storage
* Easy setup for small-scale RAG applications

---

## Project Structure

```text
AVIVO_RAG/
│
├── app.py
├── gradio_app.py
├── config.py
├── requirements.txt
├── .env.example
│
├── docs/
│   ├── company_policy.md
│   └── faq.md
│
├── chroma_db/
│
└── rag/
    ├── __init__.py
    ├── ingest.py
    ├── retrieve.py
    └── generate.py
```

---

## Installation

### 1. Create Environment

```bash
conda create -n AVIVO_env python=3.11 -y
conda activate AVIVO_env
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

---

## Ollama Setup

Install Ollama and pull the required model:

```bash
ollama pull llama3.2
```

Verify the model:

```bash
ollama list
```

---

## Ingest Documents

Whenever documents are added or modified in the `docs/` folder, rebuild the vector database:

```bash
python rag/ingest.py
```

---

## Run the Telegram Bot

```bash
python app.py
```

The bot will start polling Telegram messages.

---

## Optional Gradio UI

For local testing without Telegram:

```bash
python gradio_app.py
```

Open:

```text
http://127.0.0.1:7860
```

---

## Telegram Commands

### Help

```text
/help
```

### Ask a Question

```text
/ask How many annual leave days do employees get?
```

### Example Response

```text
📌 Answer

Employees receive 25 days annual leave.

📚 Sources

• company_policy.md
```

---

## RAG Pipeline

### Step 1: Document Ingestion

* Load Markdown files
* Split into chunks
* Generate embeddings
* Store in ChromaDB

### Step 2: Retrieval

* User submits a question
* Generate query embedding
* Retrieve top matching document chunks

### Step 3: Generation

* Build prompt using retrieved context
* Send prompt to llama3.2
* Generate grounded answer
* Return answer with source attribution

---

## Efficiency Features

### Query Cache

Previously answered questions are stored in memory to avoid repeated retrieval and LLM calls.

### Conversation Memory

The system stores the last three interactions per user, enabling future conversational enhancements.

### Local Inference

Both retrieval and generation run locally, reducing latency and eliminating API costs.

---

## Hallucination Prevention

The prompt includes guardrails that instruct the LLM to:

* Use only retrieved context
* Avoid external knowledge
* Avoid generating unsupported facts
* Return a fallback response when information is unavailable

Example:

```text
I could not find that information in the knowledge base.
```

---

## Future Improvements

* Redis-based caching
* Hybrid Search (Keyword + Vector Search)
* Incremental document re-indexing
* Multi-modal support (image + text)
* Docker deployment
* Conversational RAG with persistent memory

---

## Author

Praveen Subramani

Built as part of a GenAI / RAG bot assignment demonstrating Retrieval-Augmented Generation, vector search, local LLM inference, and Telegram integration.

 

---

📌 Feel free to fork, contribute, or reach out for collaboration. Let's build together! 💪🚀
>>>>>>> d1332240345cd34fd1e3f84e6da601b41f0999c6
