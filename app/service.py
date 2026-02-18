import re


def evaluate_status():
    return "red"


def process_data(data):
    return {
        "processed": True,
        **data
    }


def validate_email(email):
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
