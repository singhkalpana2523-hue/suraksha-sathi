from __future__ import annotations

import os
import pickle
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class RAGConfig:
    vector_store_dir: str
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    # Must match build_vectors.py's metric choice.
    faiss_metric: str = "l2"  # "l2" or "ip"


class RAGService:
    """Vector retrieval service.

    Responsibilities:
    1) Load FAISS index
    2) Load metadata.pkl
    3) Load SentenceTransformer model
    4) Embed incoming query
    5) Search index
    6) Return top_k records with similarity scores

    This module does NOT call Gemini.
    """

    def __init__(self, cfg: RAGConfig):
        self.cfg = cfg

        # Heavy imports after init so module import stays cheap.
        # (Tests may monkeypatch these modules; hence we import via sys.modules.)
        try:
            import faiss  # type: ignore
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "faiss is required to load the FAISS index. Install faiss-cpu (or faiss-gpu) to use RAG."
            ) from e

        try:
            from sentence_transformers import SentenceTransformer  # type: ignore
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "sentence-transformers is required to embed queries. Install it to use RAG."
            ) from e


        index_path = os.path.join(cfg.vector_store_dir, "faiss.index")
        meta_path = os.path.join(cfg.vector_store_dir, "metadata.pkl")

        if not os.path.exists(index_path):
            raise FileNotFoundError(
                f"FAISS index not found at {index_path}. Run build_vectors.py first."
            )
        if not os.path.exists(meta_path):
            raise FileNotFoundError(
                f"metadata.pkl not found at {meta_path}. Run build_vectors.py first."
            )

        self.faiss = faiss
        self.index = faiss.read_index(index_path)

        with open(meta_path, "rb") as f:
            self.metadata: List[Dict[str, Any]] = pickle.load(f)

        self.model = SentenceTransformer(cfg.embedding_model_name)

    def _embed_query(self, query: str):
        # Normalize embeddings when using IP (cosine-like) with normalize_embeddings=True.
        normalize = self.cfg.faiss_metric.lower().strip() == "ip"
        vec = self.model.encode(
            [query],
            show_progress_bar=False,
            normalize_embeddings=normalize,
        )

        # SentenceTransformer returns (1, dim) numpy array
        return vec.astype("float32")

    def _convert_scores(self, distances, *, top_k: int) -> List[float]:
        """Convert FAISS distances to similarity scores.

        For IndexFlatL2: smaller distance => more similar.
        For IndexFlatIP: larger inner product => more similar.

        We'll return a normalized-ish similarity:
        - L2: similarity = 1 / (1 + distance)
        - IP: similarity = inner_product
        """
        import numpy as np

        d = np.asarray(distances).reshape(-1)[:top_k]
        metric = self.cfg.faiss_metric.lower().strip()
        if metric == "ip":
            return d.astype(float).tolist()

        # Default L2
        sim = 1.0 / (1.0 + d)
        return sim.astype(float).tolist()

    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        if not query or not query.strip():
            return []

        qvec = self._embed_query(query)

        # FAISS returns (distances, indices)
        distances, indices = self.index.search(qvec, top_k)

        sims = self._convert_scores(distances[0], top_k=top_k)
        idxs = indices[0]

        results: List[Dict[str, Any]] = []
        for i, idx in enumerate(idxs.tolist()):
            if idx < 0:
                continue
            if idx >= len(self.metadata):
                continue

            rec = dict(self.metadata[idx])
            rec["similarity"] = sims[i] if i < len(sims) else None
            results.append(rec)

        return results


def get_default_rag_service() -> RAGService:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    vector_store_dir = os.path.join(base_dir, "dataset", "vector_store")
    # base_dir points to backend/app, so join gives backend/app/dataset/vector_store
    return RAGService(
        RAGConfig(
            vector_store_dir=vector_store_dir,
            faiss_metric="l2",
        )
    )

