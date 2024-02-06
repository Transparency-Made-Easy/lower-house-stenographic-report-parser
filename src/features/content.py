import re

from src.custom_json import obj2pretty_json


def get_content_text(pages, table_of_contents):
    header_names = get_header_names(table_of_contents)

    start, end = get_content_page_range(pages)
    text = []

    for i in range(start, end + 1):
        page = pages[i]
        page = re.sub(
            r"\(\s*Początek\s+posiedzenia\s+o\s+godz\.\s+12\s+min\s+07\s*\)", "", page
        )
        page = page.strip()
        page = merge_consecutive_colon(page)

        if i == start:
            match = re.search(r"(Wicemarszałek|Marszałek).*?:", page)
            page = page[match.start() :]

        page = page.strip()

        if len(text) > 0:
            speaker = text[-1]["speaker"]
            regex = re.escape(speaker).replace(r"\ ", r"(\s+|\n+)+")
            match = re.search(regex + "$", page)
            if match:
                page = page[: match.start()].strip()

        def remove_session_number(page):
            expr = r"(\d+)?\.\s+posiedzenie\s+Sejmu\s+w\s+dniu\s+\d+\s+\w+\s+\d+\s+r\."
            page = re.sub("^" + expr, "", page.strip(), flags=re.IGNORECASE).strip()
            page = re.sub(expr + "$", "", page, flags=re.IGNORECASE).strip()
            return page

        def remove_header(page: str, header_names: [str]) -> str:
            expr = "(" + "|".join([name for name in header_names]) + r")\s*\.?\s*"
            page = re.sub(
                "^" + expr, "", page.strip(), flags=re.IGNORECASE | re.DOTALL
            ).strip()
            page = re.sub(expr + "$", "", page, flags=re.IGNORECASE | re.DOTALL).strip()
            return page

        page = remove_session_number(page)
        page = re.sub(r"^\d+", "", page).strip()
        page = remove_session_number(page)
        page = remove_header(page, header_names)
        page = re.sub(r"^\d+", "", page).strip()
        page = remove_session_number(page)
        page = remove_header(page, header_names)
        page = re.sub(r"^\d+", "", page).strip()
        page = remove_header(page, header_names)
        page = re.sub(r"^;.*?;", "", page).strip()
        page = remove_header(page, header_names)
        page = re.sub(r"^\s*(–|-)\s*głosowanie", "", page).strip()
        page = re.sub(r"^\.", "", page).strip()
        page = remove_header(page, header_names)
        page = re.sub(
            r"\*\s*\)\s*Teksty\s+wystąpień\s+niewygłoszonych\s+w\s+załączniku\s*",
            "",
            page,
        ).strip()
        page = re.sub(r"^\s*poselskie\s*\n?\s*", "", page)
        page = re.sub(r"^\s*\d+\s*\n?\s*", "", page)
        page = re.sub(r"\s*\)[\s\n]*\.$", ")", page).strip()
        page = re.sub(r"\.+$", ".", page).strip()
        page = remove_header(page, header_names)

        page = "\n".join(
            [line.strip() for line in page.split("\n") if len(line.strip()) > 0]
        )

        # print(page)
        # print("--------------------------------------------------")

        lines = [line.strip() for line in page.split("\n")]
        i = 0
        while i < len(lines):
            line = lines[i]

            if (
                not re.search(r"^Prezydium", line)
                and not re.search(r"art\.\s*\d+", line)
                and (
                    not re.search(r":\s*(-|—)", line)
                    and (i + 1 >= len(lines) or not re.search(r"^(-|—)", lines[i + 1]))
                )
                and (re.search(r"^[A-Z].*:$", line) or re.search(r"^Poseł.*:", line))
            ):
                index = line.find(":")
                speaker = line[:index]
                rest = line[index + 1 :].strip()
                text.append({"speaker": speaker, "content": rest + " "})

            elif (
                re.search(
                    r"^(Sekretarz\s+Poseł|Prezes\s+Rady\s+Ministrów|Minister|Sekretarz\s+Stanu)",
                    line,
                )
                and i + 1 < len(lines)
                and re.search(r":$", lines[i + 1])
            ):
                next_line = lines[i + 1]
                index = next_line.find(":")
                speaker = next_line[:index]
                rest = next_line[index + 1 :].strip()
                text.append({"speaker": line + " " + speaker, "content": rest + " "})
                i += 2
                continue

            elif (
                re.search(r"^Sekretarz", line)
                and i + 1 < len(lines)
                and not re.search(r":$", lines[i + 1])
                and i + 2 < len(lines)
                and re.search(r":$", lines[i + 2])
            ):
                n1_line = lines[i + 1]
                n2_line = lines[i + 2]
                index = n2_line.find(":")
                speaker2 = n2_line[:index]
                rest = n2_line[index + 1 :].strip()
                text.append(
                    {
                        "speaker": line + " " + n1_line + " " + speaker2,
                        "content": rest + " ",
                    }
                )
                i += 3
                continue

            else:
                if text[-1]["content"].strip().endswith("-"):
                    text[-1]["content"] = re.sub(
                        r"\s*-$", "", text[-1]["content"].strip()
                    )
                    line = re.sub(r"^\s+", "", line)
                text[-1]["content"] += line + " "

            i += 1

    # exit()

    speakers = [item["speaker"].strip() for item in text]
    regex = r"(" + "|".join(speakers) + r")$"

    new_result = []
    for item in text:
        item["content"] = re.sub(r"\s+", " ", item["content"].strip())
        item["speaker"] = re.sub(r"\s+", " ", item["speaker"].strip())
        item["content"] = re.sub(regex, "", item["content"]).strip()

        item["content"] = re.sub(
            r"\(Przerwa\s+w\s+posiedzeniu\s+od?\s+godz\.\s+\d+\s+min\s+\d+.*?\)",
            "",
            item["content"],
        ).strip()

        item["content"] = re.sub(
            r"\(\s*Koniec\s+posiedzenia\s+o\s+godz\.\s+\d+\s+min\s+\d+\s*\)",
            "",
            item["content"],
        ).strip()

        item["content"] = re.sub(
            r"\(Wznowienie\s+posiedzenia\s+o\s+godz\.\s+\d+\s+min\s+\d+\s*\)",
            "",
            item["content"],
        ).strip()

        item["content"] = re.sub(
            r"\(Przewodnictwo\s+w\s+obradach\s+obejmuje.*?\)",
            "",
            item["content"],
        ).strip()

        item["content"] = re.sub(
            r"(\s*(–|-)\s*)?głosowanie$",
            "",
            item["content"],
        ).strip()

        index = re.search(
            r"TŁOCZONO\s+Z\s+POLECENIA\s+MARSZAŁKA\s+SEJMU\s+RZECZYPOSPOLITEJ\s+POLSKIEJ\s+KANCELARIA\s+SEJMU",
            item["content"],
        )
        if index:
            item["content"] = item["content"][: index.start()].strip()

        new_result.append(item)

    # exit()

    # print(obj2pretty_json(new_result))
    return new_result


def get_header_names(table_of_contents):
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
    header_names.append("SPIS TREŚCI")
    header_names.append("Porządek dzienny")
    header_names = [item.replace(" ", r"[\s\n]+") for item in header_names]
    return header_names

    # print(obj2pretty_json(text))
    #     page = merge_blocks(page)
    #     # print("PAGE: ", page)

    #     if i == start:
    #         match = re.search(r"(Wicemarszałek|Marszałek).*?:", page)
    #         page = page[match.start() :]
    #     else:
    #         # page = "\n\n".join(page.split("\n\n")[2:])
    #         blocks = page.split("\n\n")[2:]
    #         if not blocks[0].strip().endswith(":"):
    #             page = "\n\n".join(blocks[1:])
    #         else:
    #             page = "\n\n".join(blocks)

    #     blocks = page.split("\n\n")
    #     for block in blocks:
    #         block = block.strip()
    #         if re.search(r"^\w.*:$", block):
    #             speaker = re.sub(r":$", "", block)
    #             text.append({"speaker": speaker, "content": ""})
    #         else:
    #             text[-1]["content"] += block + " "

    # result = []

    # for item in text:
    #     item["content"] = re.sub(r"\s+", " ", item["content"].strip())
    #     item["speaker"] = re.sub(r"\s+", " ", item["speaker"].strip())
    #     result.append(item)

    # return result


def get_content_page_range(pages):
    start = None
    end = None

    for i, page in enumerate(pages):
        if start is None and re.search(
            r"\(\s*(Początek|Wznowienie)\s+posiedzenia\s+o\s+godz\s*\.\s+\d+\s+min\s+\d+\s*\)",
            page,
        ):
            start = i

        if start is not None and (
            re.search(r"Teksty\s+wystąpień\s+niewygłoszonych", page)
            and re.search(r"Załącznik", page)
        ):
            end = i - 1
            break

        if start is not None and (
            re.search(
                r"Porządek\s+dzienny",
                page,
            )
            and re.search(r"posiedzenia\s+Sejmu\s+Rzeczypospolitej\s+Polskiej", page)
        ):
            end = i - 1
            break

        if start is not None and (
            re.search(
                r"TŁOCZONO\s+Z\s+POLECENIA\s+MARSZAŁKA\s+SEJMU\s+RZECZYPOSPOLITEJ\s+POLSKIEJ",
                page,
            )
        ):
            end = i
            break

    return start, end


def get_content_from_page(text):
    new_text = merge_consecutive_brackets(text)
    new_text = merge_consecutive_colon(new_text)
    new_text = merge_blocks(new_text)

    return new_text


def merge_consecutive_brackets(text):
    new_text = ""
    bracket_text = ""

    lines = text.split("\n")

    for i, line in enumerate(lines):
        line = line.strip()
        if (
            line.startswith("(") and (i > 0 and lines[i - 1] == "")
            # and (i + 1 < len(lines) and lines[i + 1] == "")
        ):
            bracket_text += line
        elif bracket_text:
            if bracket_text.endswith("-"):
                if line != "":
                    bracket_text = re.sub(r"\s*-$", "", bracket_text)
                    bracket_text += re.sub(r"^\s+", "", line)
            else:
                bracket_text += " " + line

            if line.endswith(")"):
                new_text += re.sub(r"\s+", " ", bracket_text) + "\n"
                bracket_text = ""
        else:
            new_text += line + "\n"

    return new_text


def merge_consecutive_colon(text):
    new_text = ""
    # colon_text = ""

    lines = text.split("\n")[::-1]

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if (
            line.endswith(":")
            # and (i > 0 and lines[i - 1] == "")
            and (i + 1 < len(lines) and re.search(r"Prezydent", lines[i + 1]))
        ):
            speaker = lines[i + 1] + "" + line
            new_text = speaker + "\n" + new_text
            i += 2
            continue
        else:
            new_text = line + "\n" + new_text
            i += 1

    return new_text


def merge_blocks(text):
    new_text = ""
    blocks = text.split("\n\n")

    for block in blocks:
        block = block.strip()
        lines = block.split("\n")
        new_block = ""
        for i, line in enumerate(lines):
            line = line.strip()
            if i == 0:
                new_block += line
            elif line == "":
                new_block += ""
            else:
                if new_block.endswith("-"):
                    new_block = re.sub(r"\s*-$", "", new_block)
                    new_block += re.sub(r"^\s+", "", line)
                else:
                    new_block += " " + line
        new_text += re.sub(r"\s+", " ", new_block) + "\n\n"

    return new_text
