from transformers import pipeline

# load once
generator = pipeline("text-generation", model="distilgpt2")


def generate_answer(context: str, query: str) -> str:
    prompt = f"""
    You are a research assistant.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    result = generator(prompt, max_length=300, num_return_sequences=1)

    return result[0]["generated_text"]