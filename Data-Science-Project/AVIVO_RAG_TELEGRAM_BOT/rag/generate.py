import ollama

from rag.retrieve import retrieve
from config import LLM_MODEL

query_cache = {}

def generate_answer(question):


    # Check cache first
    if question in query_cache:
        print("Cache hit")
        return query_cache[question]

    results = retrieve(question)

    context = "\n\n".join(
        [r["content"] for r in results]
    )

    sources = list(
        set(
            [r["source"] for r in results]
        )
    )

    prompt = f"""
            You are AVIVO Knowledge Assistant.

            Use ONLY the provided context.

            Rules:
            - Never use external knowledge.
            - If information is unavailable say:
            'I could not find that information in the knowledge base.'
            - Keep answers concise.
            - Mention the most relevant policy or document when possible.

            Context:
            {context}

            Question:
            {question}

            Answer:
        """

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    # Save in cache
    query_cache[question] = (
        answer,
        results
    )


    #return answer, sources
    return answer, results


if __name__ == "__main__":

    question = input("Ask a question: ")

    answer, sources = generate_answer(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")
    for source in sources:
        print(f"- {source}")