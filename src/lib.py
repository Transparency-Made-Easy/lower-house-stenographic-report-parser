from src.features.table_of_contents import get_table_of_contents
from src.features.session_date import get_session_date
from src.features.session_start import get_session_start
from src.features.sitting_number import get_sitting_number
from src.features.term import get_term
from src.pdf import get_pages


def report_to_obj(file_path):
    pages = get_pages(file_path)

    obj = {
        "term": get_term(pages[0]),
        "sitting_number": get_sitting_number(pages[0]),
        "session_date": get_session_date(pages[0]),
        "table_of_contents": get_table_of_contents(pages),
        "session_start": get_session_start(pages),
    }

    return obj
