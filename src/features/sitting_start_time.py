from datetime import time
import re


def get_sitting_start_time(pages: [str]):
    regex = r"Początek\s+posiedzenia\s+o\s+godz\.\s+(\d+)\s+min\s+(\d+)"

    for page in pages:
        if match := re.search(regex, page):
            hour = int(match.group(1))
            minute = int(match.group(2))
            return time(hour, minute)

    return None
