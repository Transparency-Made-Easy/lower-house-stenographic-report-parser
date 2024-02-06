import re

from src.custom_json import obj2pretty_json


def get_sitting_agenda(pages_list):
    start, end = get_sitting_agenda_pages_range(pages_list)

    if start is None or end is None:
        return None

    pages = [page.strip() for page in pages_list[start : end + 1]]
    items = []

    for page in pages:
        page = re.sub(
            r"[\s\n]*Obecni[\s\n]+posłowie[\s\n]+według[\s\n]+załączonej[\s\n]+do[\s\n]+protokołu[\s\n]+listy obecności[\s\n]*",
            "",
            page,
        )
        page = re.sub(r"[\s\n]*Porządek\s+dzienny[\s\n]*", "", page)
        page = re.sub(
            r"[\s\n]*\d+\.[\s\n]+posiedzenia[\s\n]+Sejmu[\s\n]+Rzeczypospolitej[\s\n]+Polskiej[\s\n]+w[\s\n]+dniach.*?\d{4}[\s\n]+r\.[\s\n]*",
            "",
            page,
            flags=re.DOTALL,
        )

        for line in page.split("\n"):
            line = line.strip()
            if re.search(r"^\d+\.", line) and (
                len(items) == 0 or items[-1].endswith(".")
            ):
                items.append(line)
            else:
                if items[-1].endswith("-"):
                    items[-1] = items[-1][:-1]
                    items[-1] += line
                else:
                    items[-1] += " " + line

    result = []

    for item in items:
        new_item = {}

        number = re.search(r"^\d+\.", item)
        number = number.group(0)
        new_item["number"] = int(number.replace(".", ""))

        item = re.sub(r"^\d+\.", "", item).strip()

        legislative_documents = re.search(
            r"\(druki?\s+nr\s+.*?\)+", item, flags=re.IGNORECASE
        )
        legislative_documents = (
            legislative_documents.group(0) if legislative_documents else None
        )

        if legislative_documents:
            item = re.sub(
                r"\s*\(?" + legislative_documents + r"\)?\s*", "", item
            ).strip()
            legislative_documents = re.sub(r"\s+", " ", legislative_documents)
            legislative_documents = re.sub(
                r"\(druki?\s+nr\s+", "", legislative_documents
            )
            legislative_documents = re.sub(r"\)+", "", legislative_documents)
            legislative_documents = re.sub(r"(\s+i\s+)", ", ", legislative_documents)
            legislative_documents = legislative_documents.split(", ")

        new_item["legislative_documents"] = (
            legislative_documents if legislative_documents else []
        )
        new_item["content"] = re.sub(r"\.+$", ".", item)
        result.append(new_item)

    return result


def get_sitting_agenda_pages_range(pages_list):
    start = None
    end = None

    i = len(pages_list) - 1
    while i >= 0:
        if end is None and re.search(
            r"Obecni\s+posłowie\s+według\s+załączonej\s+do\s+protokołu\s+listy\s+obecności",
            pages_list[i],
        ):
            end = i

        if end is not None and re.search(r"Porządek\s+dzienny", pages_list[i]):
            start = i
            break

        i -= 1

    return start, end
