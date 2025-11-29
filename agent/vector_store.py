from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import os

class VectorStore:
    def __init__(self, persist_dir="vector_db"):
        self.persist_dir = persist_dir

        # Load free local embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Setup Chroma with NEW client system
        self.client = chromadb.PersistentClient(path=persist_dir)

        self.collection = self.client.get_or_create_collection(
            name="resume_jd_collection",
            metadata={"hnsw:space": "cosine"}
        )

    def embed_text(self, text):
        """Generate embedding using local model"""
        embedding = self.model.encode(text).tolist()
        return embedding

    def add(self, doc_id, text, metadata):
        embedding = self.embed_text(text)

        self.collection.add(
            ids=[doc_id],
            embeddings=[embedding],
            documents=[text],
            metadatas=[metadata]
        )

    def search(self, query, k=5):
        embedding = self.embed_text(query)

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )

        return results
