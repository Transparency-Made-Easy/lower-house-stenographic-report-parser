from pypdf import PdfReader


def get_pages(file_path):
    pages = {}
    with open(file_path, "rb") as file:
        pdf = PdfReader(file)
        for i, page in enumerate(pdf.pages):
            pages[i] = page.extract_text()
    return pages
