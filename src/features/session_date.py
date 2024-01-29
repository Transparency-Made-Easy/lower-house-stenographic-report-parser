from datetime import datetime
import re


def get_session_date(text):
    expression = r"z\s+\d+.\s+posiedzenia\s+Sejmu\s+Rzeczypospolitej\s+Polskiej\s+w\s+dniu\s+(\d+)\s+(\w+)\s+(\d+)\s+r."
    match = re.search(expression, text)
    if match:
        day = int(match.group(1))
        month_str = match.group(2)
        year = int(match.group(3))
        month = month_str_to_u32(month_str)
        return datetime(year, month, day)
    return None


def month_str_to_u32(month_str):
    months = {
        "stycznia": 1,
        "lutego": 2,
        "marca": 3,
        "kwietnia": 4,
        "maja": 5,
        "czerwca": 6,
        "lipca": 7,
        "sierpnia": 8,
        "września": 9,
        "października": 10,
        "listopada": 11,
        "grudnia": 12,
    }
    return months.get(month_str.strip())
