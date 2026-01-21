from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

COLLECTION = "docs"
EMBED_DIM = 4096

class QdrantStorage:
    def __init__(self, url="http://localhost:6333"):
        self.client = QdrantClient(url=url)
        self.collection = COLLECTION

        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(
                    size=EMBED_DIM,
                    distance=Distance.COSINE
                ),
            )

    def upsert(self, ids, vectors, payloads):
        points = [
            PointStruct(
                id=ids[i],
                vector=vectors[i],
                payload=payloads[i]
            )
            for i in range(len(ids))
        ]

        self.client.upsert(
            collection_name=self.collection,
            points=points
        )

    def search(self, query_vector, top_k=5):
        response = self.client.query_points(
            collection_name=self.collection,
            query=query_vector,
            limit=top_k,
            with_payload=True
        )

        # 🔥 THIS IS THE IMPORTANT PART
        points = response.points if hasattr(response, "points") else response

        contexts = []
        sources = set()

        for p in points:
            # Support tuple + ScoredPoint
            if isinstance(p, tuple):
                payload = p[2] if len(p) > 2 else {}
            else:
                payload = p.payload or {}

            if payload and "text" in payload:
                contexts.append(payload["text"])
                sources.add(payload.get("source", ""))

        return {
            "contexts": contexts,
            "sources": list(sources)
        }


# ✅ SINGLE GLOBAL INSTANCE
store = QdrantStorage()
