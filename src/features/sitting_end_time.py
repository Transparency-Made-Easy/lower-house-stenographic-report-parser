import re
from datetime import time


def get_sitting_end_time(pages):
    regex = r"\(\s*Koniec\s+posiedzenia\s+o\s+godz\.\s+(\d+)\s+min\s+(\d+)\s*\)"

    for page in reversed(pages):
        if match := re.search(regex, page):
            return time(int(match.group(1)), int(match.group(2)))

    return None
