import json
import random

BANKS = [
    "SBI",
    "HDFC",
    "ICICI",
    "Axis Bank",
    "PNB"
]

LINKS = [
    "bit.ly/update",
    "verify-bank.xyz",
    "secureupi.in",
    "bank-update.co"
]

templates = [

    {
        "category": "Banking",

        "severity": "High",

        "template":
        "Dear customer, your {bank} account has been blocked. Click {link} immediately to verify your KYC."
    },

    {
        "category": "UPI",

        "severity": "High",

        "template":
        "Your UPI account requires verification. Visit {link} immediately."
    },

    {
        "category": "Jobs",

        "severity": "Medium",

        "template":
        "Congratulations! You are selected for a work-from-home job. Pay ₹499 registration fee."
    }

]

dataset = []

counter = 1

for template in templates:

    for _ in range(40):

        text = template["template"].format(

            bank=random.choice(BANKS),

            link=random.choice(LINKS)

        )

        dataset.append({

            "id": counter,

            "title": template["category"] + " Scam",

            "category": template["category"],

            "severity": template["severity"],

            "language": "English",

            "text": text,

            "source": "Generated"

        })

        counter += 1

with open("data/generated_examples.json", "w", encoding="utf-8") as f:

    json.dump(dataset, f, indent=4, ensure_ascii=False)

print(f"Generated {len(dataset)} scam examples.")