import re
from datetime import time


def get_session_end_time(pages: [str]):
    regex = r"\(\s*(Koniec\s+posiedzenia|Przerwa\s+w\s+posiedzeniu)\s+o\s+godz\.\s+(\d+)\s+min\s+(\d+)\s*\)"

    for page in reversed(pages):
        if match := re.search(regex, page):
            hour = int(match.group(2))
            minute = int(match.group(3))
            return time(hour, minute)

    return None
