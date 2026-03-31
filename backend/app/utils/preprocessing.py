import re

def clean_text(text: str) -> str:
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # remove special characters (optional)
    text = re.sub(r'[^\w\s.,]', '', text)

    return text.strip()