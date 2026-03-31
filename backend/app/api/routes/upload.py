from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import process_pdf

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    result = process_pdf(file)
    return {
        "message": "PDF uploaded successfully",
        "data": result
    }