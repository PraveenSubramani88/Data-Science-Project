import os
import uuid
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


# -----------------------------
# Configuration
# -----------------------------
DOCS_DIR = "docs"
CHROMA_DB_DIR = "chroma_db"
COLLECTION_NAME = "knowledge_base"

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function
)


# -----------------------------
# Text Chunking
# -----------------------------
def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


# -----------------------------
# Read Markdown Files
# -----------------------------
def load_documents():
    documents = []

    for file_path in Path(DOCS_DIR).glob("*.md"):

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append(
            {
                "source": file_path.name,
                "content": text
            }
        )

    return documents


# -----------------------------
# Store in Chroma
# -----------------------------
def ingest_documents():

    docs = load_documents()

    total_chunks = 0

    for doc in docs:

        chunks = chunk_text(doc["content"])

        ids = []
        documents = []
        metadatas = []

        for chunk in chunks:

            ids.append(str(uuid.uuid4()))

            documents.append(chunk)

            metadatas.append(
                {
                    "source": doc["source"]
                }
            )

        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

        total_chunks += len(chunks)

    print(f"Successfully indexed {total_chunks} chunks.")


if __name__ == "__main__":
    ingest_documents()