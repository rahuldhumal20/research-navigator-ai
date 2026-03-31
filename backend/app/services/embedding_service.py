from sentence_transformers import SentenceTransformer
from app.db.chroma_client import collection

# load model (only once)
model = SentenceTransformer('all-MiniLM-L6-v2')


def generate_embedding(text: str):
    return model.encode(text).tolist()


def store_chunks(chunks, filename):
    for i, chunk in enumerate(chunks):
        embedding = generate_embedding(chunk)

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{filename}_{i}"]
        )
        