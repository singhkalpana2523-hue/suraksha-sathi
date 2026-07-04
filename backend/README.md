# suraksha-sathi

## Module: Scam Dataset → Embeddings → FAISS → Retrieval (RAG)

This backend provides semantic retrieval of the most similar scam records from the dataset.

### Pipeline
1. **Dataset records** are stored/managed in JSON.
2. **`scripts/build_vectors.py`** generates:
   - `app/dataset/vector_store/faiss.index`
   - `app/dataset/vector_store/metadata.pkl`
3. **`app/services/rag_service.py`** loads the FAISS index + metadata into memory and exposes:
   - `RAGService.search(query: str, top_k: int = 5)`

The retrieval layer **does not** call Gemini/Groq and **does not** analyze scams. It only returns the best matching records with similarity scores.

### Retrieval output shape
Returns a list like:

```json
[
  {
    "title": "KYC Scam",
    "category": "Bank Fraud",
    "summary": "...",
    "source": "...",
    "similarity": 0.96
  }
]
```

### Key implementation details
- Embedding model name used is exactly:
  - `sentence-transformers/all-MiniLM-L6-v2`
- FAISS metric must match `scripts/build_vectors.py` (`l2` or `ip`).

### Running retrieval tests
From `suraksha-sathi/backend`:

```bash
pip install pytest
pytest -q
```

Notes:
- `test_rag_service.py` uses monkeypatching so it can run without requiring FAISS/SentenceTransformer at test time.

