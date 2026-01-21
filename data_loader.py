from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
import ollama

EMBED_MODEL = "qwen3-embedding:8b"  # Ollama embedding model
EMBED_DIM = 4096  # nomic-embed-text output size

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    embeddings = []
    for text in texts:
        response = ollama.embeddings(
            model=EMBED_MODEL,
            prompt=text
        )
        embeddings.append(response["embedding"])
    return embeddings
