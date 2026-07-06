import json
import faiss
import numpy as np

from app.services.embedding_service import create_embedding

# Load dataset
with open("data/scam_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

documents = []
embeddings = []

for item in data:

    document = f"""
Title: {item.get("title", "")}

Category: {item.get("category", "")}

Subcategory: {item.get("subcategory", "")}

Severity: {item.get("severity", "")}

Summary:
{item.get("summary", "")}

Text:
{item.get("text", "")}

Red Flags:
{", ".join(item.get("red_flags", []))}

Recommended Actions:
{", ".join(item.get("recommended_actions", []))}

Keywords:
{", ".join(item.get("keywords", []))}

Source:
{item.get("source", "")}
"""

    embedding = create_embedding(document)

    embeddings.append(embedding)
    documents.append(item)

# Convert embeddings to NumPy array
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "vectorstore/faiss.index")

# Save metadata
with open("vectorstore/documents.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=4, ensure_ascii=False)

print(f"Indexed {len(documents)} scam records successfully!")