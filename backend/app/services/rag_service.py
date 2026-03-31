from app.db.chroma_client import collection
from app.services.embedding_service import generate_embedding
from app.services.llm_service import generate_answer


def rag_pipeline(query: str):
    # 1. embed query
    query_embedding = generate_embedding(query)

    # 2. retrieve relevant chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results["documents"][0]

    # 3. build context
    context = " ".join(documents)

    # 4. generate answer
    answer = generate_answer(context, query)

    return {
        "query": query,
        "answer": answer,
        "sources": documents
    }