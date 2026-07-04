from __future__ import annotations

import json
import os
import pickle
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple


@dataclass
class VectorBuildConfig:
    merged_dataset_path: str
    vector_store_dir: str
    # SentenceTransformer model
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    # FAISS metric: "l2" or "ip"
    faiss_metric: str = "l2"


def _read_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _prepare_search_text(record: Dict[str, Any]) -> str:
    # Combine important fields for better retrieval
    title = record.get("title", "")
    summary = record.get("summary", "")
    text = record.get("text", "")
    category = record.get("category", "")
    subcategory = record.get("subcategory", "")
    keywords = record.get("keywords", [])

    kw_text = ""
    if isinstance(keywords, list):
        kw_text = ", ".join([str(k) for k in keywords if k is not None])
    elif keywords is not None:
        kw_text = str(keywords)

    # Include a light structured format
    parts = [
        f"Title: {title}",
        f"Summary: {summary}",
        f"Category: {category}",
        f"Subcategory: {subcategory}",
        f"Keywords: {kw_text}",
        "Text:",
        text,
    ]
    return "\n".join([p for p in parts if p is not None])


def _select_faiss_index(d: int, metric: str):
    import faiss

    metric = metric.lower().strip()
    if metric == "ip":
        return faiss.IndexFlatIP(d)
    # default l2
    return faiss.IndexFlatL2(d)


def build_vectors(cfg: VectorBuildConfig) -> Dict[str, Any]:
    # Import heavy deps inside function
    from sentence_transformers import SentenceTransformer
    import numpy as np

    import faiss

    os.makedirs(cfg.vector_store_dir, exist_ok=True)

    raw = _read_json(cfg.merged_dataset_path)
    if isinstance(raw, dict) and "records" in raw:
        records = raw["records"]
    elif isinstance(raw, list):
        records = raw
    else:
        raise ValueError("Merged dataset must be a list of records or {\"records\": [...]}.")

    if not records:
        raise ValueError("No records found in merged dataset.")

    # Metadata we keep alongside FAISS vectors
    metadata: List[Dict[str, Any]] = []
    texts: List[str] = []

    for r in records:
        if not isinstance(r, dict):
            continue
        texts.append(_prepare_search_text(r))
        metadata.append(
            {
                "id": r.get("id"),
                "title": r.get("title"),
                "category": r.get("category"),
                "subcategory": r.get("subcategory"),
                "summary": r.get("summary"),
                "source": r.get("source"),
                "severity": r.get("severity"),
                "red_flags": r.get("red_flags", []),
                "recommended_actions": r.get("recommended_actions", []),
                "keywords": r.get("keywords", []),
            }
        )

    model = SentenceTransformer(cfg.embedding_model_name)

    # Compute embeddings
    # For IP we typically use normalized embeddings to approximate cosine similarity.
    embeddings = model.encode(texts, show_progress_bar=True, normalize_embeddings=(cfg.faiss_metric.lower() == "ip"))

    vectors = np.array(embeddings, dtype="float32")
    if vectors.ndim != 2:
        raise ValueError("Embeddings must be a 2D array.")

    d = vectors.shape[1]

    index = _select_faiss_index(d=d, metric=cfg.faiss_metric)
    index.add(vectors)

    faiss_index_path = os.path.join(cfg.vector_store_dir, "faiss.index")
    metadata_path = os.path.join(cfg.vector_store_dir, "metadata.pkl")

    faiss.write_index(index, faiss_index_path)

    with open(metadata_path, "wb") as f:
        pickle.dump(metadata, f)

    # Basic verification output
    out = {
        "records": len(metadata),
        "embedding_dim": d,
        "vector_store_dir": cfg.vector_store_dir,
        "faiss_index": faiss_index_path,
        "metadata_pkl": metadata_path,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    cfg = VectorBuildConfig(
        merged_dataset_path=os.path.join(
            base_dir, "app", "dataset", "processed", "scam_dataset.json"
        ),
        vector_store_dir=os.path.join(base_dir, "app", "dataset", "vector_store"),
    )

    build_vectors(cfg)

