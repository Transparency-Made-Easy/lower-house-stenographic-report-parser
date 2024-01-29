# from src.custom_json import obj2pretty_json
# from src.lib import (
#     get_term,
#     get_session_agenda,
#     get_pages,
#     get_session_date,
#     get_sitting_number,
#     get_session_start,
# )

# FILE = r"C:\Users\Kestivvi\Desktop\pdfReader\03_ksiazka.pdf"


from src.pdf import get_pages
from src.features.table_of_contents import (
    _get_table_of_content_lines_from_page,
    _split_line_with_multiple_speakers,
)


def main():
    # # text = get_text(FILE)
    pages = get_pages(
        r"C:\Users\Kestivvi\Desktop\s3jm_project\pdfParser\files\01_a_ksiazka.pdf"
    )

    # print(pages[4])

    # obj = {
    #     "term": get_term(pages[0]),
    #     "seating_number": get_sitting_number(pages[0]),
    #     "session_date": get_session_date(pages[0]),
    #     "session_agenda": get_session_agenda(pages[2]),
    #     "session_start": get_session_start(pages[4]),
    # }

    # print(obj2pretty_json(obj))

    # x = _get_lines_from_page(pages[2])
    y = _split_line_with_multiple_speakers(
        # "Marszałek . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35"
        "Poseł Urszula Pasławska . . . . . . . . . . . . . . . . 104Poseł Daria Gosek-Popiołek  . . . . . . . . . . . . . 105"
    )

    print(y)


if __name__ == "__main__":
    main()
