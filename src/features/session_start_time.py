from datetime import time
import re


def get_session_start_time(pages: [str]):
    for page in pages:
        start_time = find_session_start_time(page)
        if start_time:
            return start_time
    return None


def find_session_start_time(page: str):
    regex = r"(Początek|Wznowienie)\s+posiedzenia\s+o\s+godz\.\s+(\d+)\s+min\s+(\d+)"
    match = re.search(regex, page)
    if match:
        hour = int(match.group(2))
        minute = int(match.group(3))
        return time(hour, minute)
    return None
