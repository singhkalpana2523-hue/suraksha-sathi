from app.services.rag_service import retrieve_similar

query = "Your bank account will be blocked."

results = retrieve_similar(query)

for r in results:
    print(r["title"])