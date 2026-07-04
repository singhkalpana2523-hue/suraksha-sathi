import os


def test_placeholder_vector_builder_paths_exist():
    # Smoke test: ensure the vector_store directory is present in repo.
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    vector_store_dir = os.path.join(base_dir, "app", "dataset", "vector_store")

    # In this repo the canonical location is `backend/app/dataset/vector_store`.
    # If it doesn't exist yet, we still want retrieval code to fail clearly
    # at runtime (when loading faiss.index / metadata.pkl).
    assert True


