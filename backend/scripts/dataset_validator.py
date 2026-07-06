REQUIRED_FIELDS = [
    "title",
    "category",
    "subcategory",
    "severity",
    "language",
    "text",
    "summary",
    "red_flags",
    "recommended_actions",
    "keywords",
    "source"
]


def validate_record(record):

    # Check required fields
    for field in REQUIRED_FIELDS:

        if field not in record:
            return False

    # Check list fields
    if not isinstance(record["red_flags"], list):
        return False

    if not isinstance(record["recommended_actions"], list):
        return False

    if not isinstance(record["keywords"], list):
        return False

    # Check text fields are not empty
    if not record["title"].strip():
        return False

    if not record["text"].strip():
        return False

    return True