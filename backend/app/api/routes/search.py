from fastapi import APIRouter
from pydantic import BaseModel
from app.db.chroma_client import collection
from app.services.embedding_service import generate_embedding

router = APIRouter()

class QueryRequest(BaseModel):
    query: str


@router.post("/search")
def search_papers(request: QueryRequest):
    query_embedding = generate_embedding(request.query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return {
        "query": request.query,
        "results": results["documents"]
    }