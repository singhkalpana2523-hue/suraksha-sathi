import os
import sys
import pickle
import json

import pytest

# Ensure `app` package is importable when running pytest from repo root
BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)



@pytest.fixture()
def tmp_vector_store(tmp_path):
    """Create a tiny, deterministic vector store for RAG tests.

    We intentionally avoid requiring faiss + sentence-transformers in CI by
    mocking the RAG internals.
    """

    # Create metadata.pkl
    metadata = [
        {
            "title": "Lottery Scam",
            "category": "Fraud",
            "summary": "You won a lottery—pay a fee.",
            "source": "test",
            "red_flags": [],
            "recommended_actions": [],
            "keywords": [],
        },
        {
            "title": "Digital Arrest Scam",
            "category": "Fraud",
            "summary": "Police claim arrest and demand payment.",
            "source": "test",
            "red_flags": [],
            "recommended_actions": [],
            "keywords": [],
        },
        {
            "title": "KYC Scam",
            "category": "Bank Fraud",
            "summary": "Update KYC to avoid account blocking.",
            "source": "test",
            "red_flags": [],
            "recommended_actions": [],
            "keywords": [],
        },
        {
            "title": "QR Code Scam",
            "category": "UPI",
            "summary": "Scan QR to receive money.",
            "source": "test",
            "red_flags": [],
            "recommended_actions": [],
            "keywords": [],
        },
    ]

    vector_store_dir = tmp_path / "vector_store"
    vector_store_dir.mkdir(parents=True, exist_ok=True)

    meta_path = vector_store_dir / "metadata.pkl"
    with open(meta_path, "wb") as f:
        pickle.dump(metadata, f)

    # Create a dummy faiss.index file placeholder (not used in mock)
    (vector_store_dir / "faiss.index").write_bytes(b"dummy")

    return str(vector_store_dir), metadata


def test_rag_service_search_returns_top_k(monkeypatch, tmp_vector_store):
    vector_store_dir, metadata = tmp_vector_store

    from app.services.rag_service import RAGConfig, RAGService

    # Patch faiss + SentenceTransformer usage inside RAGService.__init__
    class FakeIndex:
        def search(self, qvec, top_k):
            # Always return indices [3, 1, 2] for k=3
            import numpy as np

            # distances shape: (1, top_k)
            distances = np.array([[0.1, 0.2, 0.3]], dtype="float32")
            indices = np.array([[3, 1, 2]], dtype="int64")
            return distances, indices

    class FakeModel:
        def encode(self, texts, show_progress_bar=False, normalize_embeddings=False):
            import numpy as np

            # return a dummy embedding vector
            return np.zeros((1, 384), dtype="float32")

    def fake_read_index(self, index_path):
        return FakeIndex()

    # Monkeypatch modules imported in __init__
    import app.services.rag_service as rag_module

    monkeypatch.setattr(rag_module, "os", rag_module.os)

    # Replace faiss.read_index
    class FakeFaiss:
        def read_index(self, _path):
            return FakeIndex()

    monkeypatch.setattr(rag_module, "faiss", FakeFaiss(), raising=False)
    monkeypatch.setattr(rag_module, "SentenceTransformer", lambda *_args, **_kwargs: FakeModel(), raising=False)

    # Instantiate service, but ensure faiss import succeeds by injecting into sys.modules
    import types

    fake_faiss_module = types.SimpleNamespace(read_index=lambda _path: FakeIndex())
    monkeypatch.setitem(sys.modules, "faiss", fake_faiss_module)

    # Also ensure sentence_transformers import succeeds
    fake_st_module = types.SimpleNamespace(
        SentenceTransformer=lambda *_args, **_kwargs: FakeModel()
    )
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_st_module)

    service = RAGService(
        RAGConfig(
            vector_store_dir=vector_store_dir,
            embedding_model_name="sentence-transformers/all-MiniLM-L6-v2",
            faiss_metric="l2",
        )
    )


    # If patching above didn't override, ensure model/index are set:
    service.index = FakeIndex()
    service.model = FakeModel()

    results = service.search("scan qr to receive money", top_k=3)

    assert len(results) == 3
    assert results[0]["title"] == "QR Code Scam"
    assert results[1]["title"] == "Digital Arrest Scam"
    assert results[2]["title"] == "KYC Scam"
    assert "similarity" in results[0]


def test_rag_service_handles_empty_query(monkeypatch, tmp_vector_store):
    vector_store_dir, _metadata = tmp_vector_store
    from app.services.rag_service import RAGConfig, RAGService

    # Minimal monkeypatching to avoid heavy deps
    import app.services.rag_service as rag_module

    class FakeFaiss:
        def read_index(self, _path):
            class DummyIndex:
                def search(self, qvec, top_k):
                    raise AssertionError("should not be called")

            return DummyIndex()

    class FakeModel:
        def encode(self, *args, **kwargs):
            raise AssertionError("should not be called")

    # Make `import faiss` and `from sentence_transformers import SentenceTransformer` succeed
    import types

    fake_faiss_module = types.SimpleNamespace(read_index=lambda _path: FakeFaiss().read_index(_path))
    monkeypatch.setitem(sys.modules, "faiss", fake_faiss_module)

    fake_st_module = types.SimpleNamespace(
        SentenceTransformer=lambda *_args, **_kwargs: FakeModel()
    )
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_st_module)

    monkeypatch.setattr(rag_module, "faiss", FakeFaiss(), raising=False)
    monkeypatch.setattr(rag_module, "SentenceTransformer", lambda *_args, **_kwargs: FakeModel(), raising=False)

    service = RAGService(RAGConfig(vector_store_dir=vector_store_dir))

    service.index = FakeFaiss().read_index("dummy")
    service.model = FakeModel()

    results = service.search("   ", top_k=5)
    assert results == []

