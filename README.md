# RAG Application using Ollama & LlamaIndex

A **local Retrieval-Augmented Generation (RAG) system** that allows users to query PDF documents using natural language.  
The system extracts content from PDFs, chunks and embeds the text using **Ollama-hosted embedding models**, and enables intelligent question answering over the documents using an LLM.

This project is fully **local**, does not rely on paid APIs, and demonstrates a practical GenAI workflow used in real-world applications.

---

## 🚀 Features

- 📄 Load and process PDF documents
- ✂️ Intelligent text chunking for better retrieval
- 🧠 Semantic embeddings using **Ollama**
- 🔍 Context-aware retrieval using **LlamaIndex**
- 💬 Natural language question answering
- 🏠 Runs completely **offline / locally**

---

## 🛠️ Tech Stack

- **Python**
- **Ollama** (local LLM & embeddings)
- **LlamaIndex**
- **PDFReader**
- **SentenceSplitter**
- **dotenv**

---

## 🧠 Architecture Overview

1. PDF documents are loaded and parsed
2. Text is split into overlapping chunks
3. Chunks are converted into vector embeddings using Ollama
4. Relevant chunks are retrieved based on user queries
5. An LLM generates answers using retrieved context

---

## 📦 Supported Models

### Embedding Models
- `nomic-embed-text`
- `mxbai-embed-large`

### LLMs
- `llama3`
- `mistral`

