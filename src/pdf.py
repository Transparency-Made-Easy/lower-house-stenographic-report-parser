from pypdf import PdfReader
from io import StringIO
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import fitz
from bs4 import BeautifulSoup


def get_pages(file_path):
    pages = {}
    with open(file_path, "rb") as file:
        pdf = PdfReader(file)
        for i, page in enumerate(pdf.pages):
            pages[i] = page.extract_text()
    return pages


def pdf_miner_get_pages(file_path: str):
    # PDFMiner Analyzers
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = "utf-8"
    laparams = LAParams(boxes_flow=None)
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    pages = []
    # Extract text
    pdfFile = open(file_path, "rb")
    for page in PDFPage.get_pages(pdfFile):
        interpreter.process_page(page)
        # sio.flush()
        pages.append(sio.getvalue())
        sio.seek(0)
        sio.truncate(0)

    pdfFile.close()

    # Return text from StringIO
    # text = sio.getvalue()

    # print(text)

    # Freeing Up
    device.close()
    sio.close()

    return pages


def pdf2html(file_path: str):
    doc = fitz.open(file_path)  # open a document
    # out = open("output.txt", "wb")  # create a text output
    for i, page in enumerate(doc):
        if i < 2:
            continue
        html = page.get_text("xhtml").encode("utf8")  # get plain text (is in UTF-8)

        soup = BeautifulSoup(html)
        print(soup.prettify())

        # print(text)
        break
        # out.write(text)  # write text of page
        # out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
    # out.close()


def pdf2text(file_path: str):
    doc = fitz.open(file_path)
    pages = []
    for page in doc:
        pages.append(page.get_text("text"))
    return pages
