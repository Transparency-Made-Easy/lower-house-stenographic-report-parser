import re


def get_term(text):
    match = re.search(r"Kadencja (\S)", text)
    return match.group(1) if match else None
