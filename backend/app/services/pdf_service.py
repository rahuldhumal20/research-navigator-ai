import os
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.preprocessing import clean_text
from app.utils.chunking import chunk_text
from app.services.embedding_service import store_chunks

UPLOAD_DIR = "data/papers"

# create folder if not exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_pdf(file) -> str:
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path


def process_pdf(file) -> dict:
    file_path = save_pdf(file)

    raw_text = extract_text_from_pdf(file_path)

    cleaned_text = clean_text(raw_text)

    chunks = chunk_text(cleaned_text)

    store_chunks(chunks, file.filename)

    return {
        "filename": file.filename,
        "text_length": len(cleaned_text),
        "total_chunks": len(chunks),
        "sample_chunk": chunks[0] if chunks else "",
        "status": "Stored in ChromaDB"

    }