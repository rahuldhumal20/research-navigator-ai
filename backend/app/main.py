from fastapi import FastAPI
from app.api.routes import health,upload, search,chat



app = FastAPI(title="ResearchNavigator AI")

app.include_router(health.router)
app.include_router(upload.router)
app.include_router(search.router)
app.include_router(chat.router)


@app.get("/")
def root():
    return {"message": "ResearchNavigator AI Backend Running 🚀"}