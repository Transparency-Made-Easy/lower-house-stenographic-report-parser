import re


def get_speaker_of_the_session(pages) -> (str, [str]):
    for k, page in pages.items():
        speakers = get_speaker_of_the_session_from_text(page)
        if speakers is not None:
            return speakers
    return None, None, []


def get_speaker_of_the_session_from_text(text) -> (str, [str]):
    text = text.replace("\n", " ")

    if not re.search(
        r"\(\s*Na\s+posiedzeniu\s+przewodnicz\w\s+(wice)?marszał.*?\)",
        text,
        re.UNICODE | re.MULTILINE | re.IGNORECASE,
    ):
        return None

    marszalek_senior = re.findall(
        r"Na\s+posiedzeniu\s+przewodnicz\w.*?marszałek\s+senior\s(.+?)\s*?oraz", text
    )
    marszalek_senior = None if not marszalek_senior else marszalek_senior[0].strip()

    marszalek = re.findall(
        r"Na\s+posiedzeniu\s+przewodnicz\w.*marszałek\s+Sejmu\s+(.+?)\s*(\)|oraz)", text
    )

    marszalek = None if not marszalek else marszalek[0][0]

    wicemarszalkowie = re.findall(
        r"(Na\s+posiedzeniu\s+przewodnicz\w.*wicemarszałkowie(?:\s+Sejmu)?\s+((\w+\s+\w+)(,\s+|\s+i\s+|\s*\)))+)",
        text,
    )

    if wicemarszalkowie:
        wicemarszalkowie = wicemarszalkowie[0][0].strip()
        wicemarszalkowie = re.sub(r"\s+", " ", wicemarszalkowie)
        index = re.search(r"\s*wicemarszałkowie(?:\s*Sejmu)?\s*", wicemarszalkowie)
        wicemarszalkowie = wicemarszalkowie[index.end() :].strip()
        wicemarszalkowie = re.sub(r"\s+i\s+", ", ", wicemarszalkowie).strip()
        wicemarszalkowie = wicemarszalkowie.replace(")", "").split(",")
        wicemarszalkowie = [x.strip() for x in wicemarszalkowie]
    else:
        wicemarszalkowie = []

    return marszalek_senior, marszalek, wicemarszalkowie
