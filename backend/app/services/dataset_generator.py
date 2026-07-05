import json

from app.providers.gemini_provider import GeminiProvider
from app.utils.dataset_validator import validate_record

provider = GeminiProvider()

MAX_RETRIES = 3


def generate_dataset():

    # Load categories
    with open(
        "data/categories.json",
        "r",
        encoding="utf-8"
    ) as f:
        categories = json.load(f)

    dataset = []
    counter = 1

    # Generate data category by category
    for category in categories:

        print(f"\nGenerating dataset for: {category}")

        records = None

        # Retry if Gemini fails
        for attempt in range(MAX_RETRIES):

            try:
                records = provider.generate_dataset(
                    category=category,
                    count=5
                )
                break

            except Exception as e:
                print(
                    f"Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}"
                )

        # Skip category if all retries fail
        if records is None:
            print(f"Skipping {category}")
            continue

        valid_records = []

        # Validate records
        for record in records:

            if validate_record(record):

                record["id"] = counter

                counter += 1

                valid_records.append(record)

        print(f"Valid records: {len(valid_records)}")

        # Add to final dataset
        dataset.extend(valid_records)

        # Save after every category
        with open(
            "data/generated_examples.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                dataset,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"Saved {len(dataset)} records so far."
        )

    print("\nDataset generation completed!")
    print(f"Total records generated: {len(dataset)}")