from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_service import rag_pipeline

router = APIRouter()

class ChatRequest(BaseModel):
    query: str


@router.post("/chat")
def chat(request: ChatRequest):
    result = rag_pipeline(request.query)
    return result