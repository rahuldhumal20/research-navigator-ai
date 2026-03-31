# 🚀 ResearchNavigator AI

AI-powered research paper discovery system using RAG + Knowledge Graphs.

## 🔥 Features
- 📄 Upload research papers (PDF)
- 🧠 Smart chunking & preprocessing
- 🔍 Semantic search using embeddings
- 🤖 RAG-based question answering
- 🦙 Local LLaMA (Ollama) integration

## 🛠️ Tech Stack
- FastAPI (Backend)
- ChromaDB (Vector DB)
- Sentence Transformers (Embeddings)
- Ollama (LLaMA 3)
- React + Vite (Frontend)

## ⚙️ Setup

```bash
git clone <repo-url>
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload