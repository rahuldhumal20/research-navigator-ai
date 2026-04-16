from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health,upload, search,chat


app = FastAPI(title="ResearchNavigator AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development (easy fix)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(upload.router)
app.include_router(search.router)
app.include_router(chat.router)


@app.get("/")
def root():
    return {"message": "ResearchNavigator AI Backend Running 🚀"}