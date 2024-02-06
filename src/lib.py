from src.features.sitting_agenda import get_sitting_agenda
from src.features.session_not_delivered_speeches import (
    get_session_not_delivered_speeches,
)
from src.features.sitting_day import get_sitting_day
from src.features.sitting_end_time import get_sitting_end_time
from src.features.sitting_start_time import get_sitting_start_time
from src.features.session_end_time import get_session_end_time
from src.features.session_intra_breaks import get_intra_breaks
from src.features.content import get_content_text
from src.features.speaker import get_speaker_of_the_session
from src.features.table_of_contents import get_table_of_contents
from src.features.session_date import get_session_date
from src.features.session_start_time import get_session_start_time
from src.features.sitting_number import get_sitting_number
from src.features.term import get_term
from src.pdf import get_pages, pdf2text


def parse_session_report(file_path):
    pages_dict = get_pages(file_path)
    pages_list = pdf2text(file_path)

    not_delivered_speeches = get_session_not_delivered_speeches(pages_list)

    speakers = get_speaker_of_the_session(pages_dict)
    table_of_contents = get_table_of_contents(pages_dict, speakers[1])

    obj = {
        "term_number": get_term(pages_dict[0]),
        "sitting_number": get_sitting_number(pages_dict[0]),
        "sitting_day": get_sitting_day(pages_list),
        "sitting_start_time": get_sitting_start_time(pages_list),
        "sitting_end_time": get_sitting_end_time(pages_list),
        "sitting_agenda": get_sitting_agenda(pages_list),
        "session_date": get_session_date(pages_dict[0]),
        "session_start_time": get_session_start_time(pages_list),
        "session_end_time": get_session_end_time(pages_list),
        "session_intra_breaks_times": get_intra_breaks(pages_list),
        "speaker_senior": speakers[0],
        "speaker": speakers[1],
        "vicespeakers": speakers[2],
        "table_of_contents": table_of_contents,
        "content": get_content_text(pages_list, table_of_contents),
        "session_not_delivered_speeches": not_delivered_speeches,
    }

    return obj


def parse_sitting_reports(session_reports):
    keys = [
        "sitting_day",
        "session_date",
        "session_start_time",
        "session_end_time",
        "session_intra_breaks_times",
        "speaker_senior",
        "speaker",
        "vicespeakers",
        "table_of_contents",
        "content",
        "session_not_delivered_speeches",
    ]

    purged_session_reports = [
        {key: report[key] for key in keys} for report in session_reports
    ]

    obj = {
        "term_number": session_reports[0]["term_number"],
        "sitting_number": session_reports[0]["sitting_number"],
        "sitting_start_date": session_reports[0]["session_date"],
        "sitting_start_time": session_reports[0]["sitting_start_time"],
        "sitting_end_date": session_reports[-1]["session_date"],
        "sitting_end_time": session_reports[-1]["sitting_end_time"],
        "sitting_agenda": session_reports[-1]["sitting_agenda"],
        "session_reports": purged_session_reports,
    }

    return obj
