import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from config import (
    CHROMA_DB_DIR,
    COLLECTION_NAME,
    TOP_K
)

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

collection = client.get_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function
)


def retrieve(query, k=TOP_K):

    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    documents = results["documents"][0]
    metadata = results["metadatas"][0]

    retrieved_chunks = []

    for doc, meta in zip(documents, metadata):

        retrieved_chunks.append(
            {
                "content": doc,
                "source": meta["source"]
            }
        )

    return retrieved_chunks


if __name__ == "__main__":

    query = input("Ask a question: ")

    results = retrieve(query)

    print("\nRetrieved Chunks:\n")

    for idx, result in enumerate(results, start=1):

        print(f"Chunk {idx}")
        print(f"Source: {result['source']}")
        print(result["content"])
        print("-" * 50)