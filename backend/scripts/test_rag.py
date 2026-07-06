from app.services.rag_service import RAGService

rag = RAGService()

query = "My SBI account is blocked. Update KYC immediately."

results = rag.search(query)

for r in results:

    print("=" * 50)

    print(r["title"])

    print(r["category"])

    print(r["similarity"])

    print(r["text"])