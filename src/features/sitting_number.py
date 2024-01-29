import re


def get_sitting_number(text):
    expression = r"z\s+(\d+).\s+posiedzenia\s+Sejmu\s+Rzeczypospolitej\s+Polskiej"
    match = re.search(expression, text)
    return match.group(1) if match else None
