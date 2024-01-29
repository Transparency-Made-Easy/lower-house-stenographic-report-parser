import re

from src.features.session_start import get_session_start


def get_session_agenda_from_page(text):
    regex = r"(Punkt\s+\d+\.(.|\n)*?\n)(Głosowanie|Poseł)"
    matches = re.findall(regex, text, re.I | re.M)
    return list(map(lambda v: v[0], matches))


def get_session_agenda(pages):
    start, end = get_session_pages_range(pages)

    matches = []
    for i in range(start, end + 1):
        matches.extend(get_session_agenda_from_page(pages[i]))

    return matches


def get_session_pages_range(pages) -> (int, int):
    start = None
    end = None

    for i, page in pages.items():
        if start == None and is_spis_tresci_in_text(page):
            start = i
        if start != None and end == None:
            if get_session_start(page) != None:
                end = i
                break

    return start, end


def is_spis_tresci_in_text(text):
    regex = r"SPIS\s+TREŚCI"
    match = re.search(regex, text)
    return match is not None
