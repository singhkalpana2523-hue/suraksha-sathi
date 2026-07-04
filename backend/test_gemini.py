"""Manual smoke test for text analysis.

This file is not intended to be collected/executed by pytest.
Renamed from a test-style script to avoid CI failures when optional deps
(e.g. `groq`) are not installed.
"""

if __name__ == "__main__":
    from app.providers.groq_provider import analyze_text

    response = analyze_text(
        "Congratulations! Click this link to verify your bank account."
    )

    print(response.model_dump_json(indent=2))

