from datetime import time
import re


def get_session_start(pages):
    for k, page in pages.items():
        start = get_session_start_from_text(page)
        if start is not None:
            return start
    return None


def get_session_start_from_text(text):
    regex = r"(Początek|Wznowienie)\s+posiedzenia\s+o\s+godz\.\s+(\d+)\s+min\s+(\d+)"
    match = re.search(regex, text)

    if not match:
        return None

    hour = int(match.group(2))
    minute = int(match.group(3))
    time_object = time(hour, minute)
    return time_object
