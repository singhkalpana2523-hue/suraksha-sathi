from app.providers.groq_provider import analyze_text

response = analyze_text(
    "Congratulations! Click this link to verify your bank account."
)

print(response.model_dump_json(indent=2))