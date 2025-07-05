# 🧪 **RAG-Lab: A Sample Retrieval-Augmented Generation Playground**

[![Python](https://img.shields.io/badge/python-%3E=3.9-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Overview

**RAG-Lab** is a lightweight, modular playground for experimenting with Retrieval-Augmented Generation (RAG) pipelines. Effortlessly ingest documents, embed them into a vector store, and chat with an LLM enhanced by real-time retrieval. Perfect for prototyping, benchmarking, and learning how RAG works under the hood!

---

## ✨ Key Features

- **Pluggable document loaders & chunkers**
- **Multiple vector store backends** (FAISS & Chroma out of the box)
- **Simple REST & WebSocket chat API**
- **Streamlit-based web UI for chatting and inspection**
- **Docker-first deployment for easy setup**
- **Built-in evaluation harness** for RAG quality checks

---

## 🏗️ Architecture

```mermaid
flowchart TD
    User([User: Web UI / API Client])
    subgraph RAG-Lab
      A[Document Loader] --> B[Text Chunker]
      B --> C[Embedder (OpenAI, etc.)]
      C --> D[Vector Store (FAISS, Chroma)]
      User -->|Query| E[Retriever]
      E --> D
      D --> E
      E --> F[LLM (OpenAI, etc.)]
      F -->|Response| User
      subgraph API & UI
        E
        F
      end
    end
```
*_(Replace with a project-specific diagram as implementation evolves)_*

---

## ⚡ Quick Start

### Prerequisites

- Python >= 3.9 & `pip`
- _(Optional)_ Docker

### 1. Run via Docker (recommended)

```bash
docker run -e OPENAI_API_KEY=sk-... -p 8000:8000 ghcr.io/your-org/rag-lab:latest
```

### 2. Or, Local Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
python main.py
```
_Or for FastAPI:_  
```bash
uvicorn app:app --reload
```

### 3. Access the UI

- Streamlit: [http://localhost:8501](http://localhost:8501)
- API: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📁 Directory Structure

```
rag-lab/
├── app/                 # FastAPI application code
│   ├── api/             # REST/WebSocket endpoints
│   ├── retrieval/       # RAG core logic
│   └── ...
├── ui/                  # Streamlit frontend
├── docs/                # Documentation, diagrams
├── tests/               # Unit & integration tests
├── data/                # Sample docs (excluded from git)
├── requirements.txt
├── Dockerfile
└── README.md
```
*_(Some directories are placeholders; structure may evolve.)_*

---

## ⚙️ Configuration

Configure via `.env` or environment variables:

| Name              | Description                                 | Example                        |
|-------------------|---------------------------------------------|--------------------------------|
| `OPENAI_API_KEY`  | Your OpenAI API key (required for LLM/emb)  | `sk-...`                       |
| `VECTOR_DB_URL`   | Vector DB connection string (if remote)      | `sqlite:///faiss.db`           |
| `EMBEDDING_MODEL` | Embedding model name                        | `text-embedding-ada-002`       |
| `UI_PORT`         | Streamlit UI port                           | `8501`                         |
| `API_PORT`        | FastAPI port                                | `8000`                         |

---

## 🧑‍💻 Example Usage

### Chat via API

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is vector search?", "history": []}'
```
_Response:_
```json
{
  "answer": "Vector search is a technique...",
  "source_docs": ["docs/intro.pdf"]
}
```

### Web UI

![UI Screenshot Placeholder](docs/screenshot.png)
<!-- Replace with an actual UI screenshot -->

---

## 🛠️ Contributing

1. **Fork** this repo
2. **Create a feature branch**  
   `git checkout -b feat/your-feature`
3. **Commit with clear messages**  
   _Style: `feat: Add new retriever backend`_
4. **Push & open a Pull Request**
5. We'll review & collaborate!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements & Inspirations

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [LangChain](https://github.com/langchain-ai/langchain)
- [ChromaDB](https://www.trychroma.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
- And the broader open-source RAG community!