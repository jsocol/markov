import re


END_OF_TEXT = '\0'


def normalize_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    return text
