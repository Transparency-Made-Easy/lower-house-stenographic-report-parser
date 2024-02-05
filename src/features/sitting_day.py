import re


def get_sitting_day(pages_list: [str]) -> str:
    pattern = r"\(\s*(.+?)\s+dzień\s+obrad\s*\)"
    match = re.search(pattern, pages_list[0])

    if match:
        day_number = word_to_number(match.group(1))
        return day_number

    return None


def word_to_number(word: str) -> int:
    word = word.strip().lower()

    numbers = {
        "pierwszy": 1,
        "drugi": 2,
        "trzeci": 3,
        "czwarty": 4,
        "piąty": 5,
        "szósty": 6,
        "siódmy": 7,
        "ósmy": 8,
        "dziewiąty": 9,
        "dziesiąty": 10,
        "jedenasty": 11,
        "dwunasty": 12,
        "trzynasty": 13,
        "czternasty": 14,
        "piętnasty": 15,
        "szesnasty": 16,
        "siedemnasty": 17,
        "osiemnasty": 18,
        "dziewiętnasty": 19,
        "dwudziesty": 20,
        "dwudziesty pierwszy": 21,
        "dwudziesty drugi": 22,
        "dwudziesty trzeci": 23,
        "dwudziesty czwarty": 24,
        "dwudziesty piąty": 25,
        "dwudziesty szósty": 26,
        "dwudziesty siódmy": 27,
        "dwudziesty ósmy": 28,
        "dwudziesty dziewiąty": 29,
        "trzydziesty": 30,
    }

    return numbers.get(word, None)
