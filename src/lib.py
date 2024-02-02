import re
from src.features.breaks import get_breaks
from src.features.content import get_content_text
from src.features.speaker import get_speaker_of_the_session
from src.features.table_of_contents import get_table_of_contents
from src.features.session_date import get_session_date
from src.features.session_start import get_session_start
from src.features.sitting_number import get_sitting_number
from src.features.term import get_term
from src.pdf import get_pages, pdf2text


def report_to_obj(file_path):
    pages = get_pages(file_path)
    pages2 = pdf2text(file_path)

    speakers = get_speaker_of_the_session(pages)
    table_of_contents = get_table_of_contents(pages, speakers[1])

    # TODO: Extract this logic
    header_names = list(
        set(
            [
                re.sub(
                    r"Punkt\s+\d+.\s+porządku\s+dziennego:\s*", "", item["name"]
                ).strip()
                for item in table_of_contents
                if item["type"] == "HEADER"
            ]
        )
    )

    obj = {
        "term": get_term(pages[0]),
        "sitting_number": get_sitting_number(pages[0]),
        "session_date": get_session_date(pages[0]),
        "session_start": get_session_start(pages),
        "speaker_senior": speakers[0],
        "speaker": speakers[1],
        "vicespeakers": speakers[2],
        "breaks": get_breaks(pages2),
        "table_of_contents": table_of_contents,
        "text": get_content_text(pages2, header_names),
    }

    return obj
