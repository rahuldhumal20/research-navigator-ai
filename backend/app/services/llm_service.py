import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(context: str, query: str) -> str:
    prompt = f"""
You are a research assistant.

Use the context below to answer the question clearly.

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    return data["response"]