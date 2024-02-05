import re

from src.custom_json import obj2pretty_json


def get_session_not_delivered_speeches(pages_list):
    start, end = get_session_not_delivered_speeches_pages_range(pages_list)

    if start is None or end is None:
        return []

    result = []

    for page in pages_list[start : end + 1]:
        page = remove_headers_and_footers(page)
        page = merge_consecutive_brackets(page)
        lines = [line.strip() for line in page.split("\n")]

        i = 0
        while i < len(lines):
            if re.search(r"Oświadczenia\s+poselskie", lines[i]):
                result.append(
                    {"type": "HEADER", "name": "Oświadczenia poselskie", "speakers": []}
                )
            elif re.search(r"^\s*Poseł\s+", lines[i]) and re.search(
                r"^(Koalicyjny)?\s*Klub", lines[i + 1]
            ):
                position = "Poseł"
                speaker = re.sub(r"^\s*Poseł\s+", "", lines[i]).strip()
                parliamentary_group = lines[i + 1]
                content = ""

                result[-1]["speakers"].append(
                    {
                        "position": position,
                        "speaker": speaker,
                        "parliamentary_group": parliamentary_group,
                        "content": content,
                    }
                )
                i += 2
                continue
            else:
                if (
                    len(result) > 0
                    and len(result[-1]["speakers"])
                    and result[-1]["speakers"][-1]["content"].endswith("-")
                ):
                    result[-1]["speakers"][-1]["content"] = result[-1]["speakers"][-1][
                        "content"
                    ][:-1]
                    result[-1]["speakers"][-1]["content"] += lines[i]
                else:
                    result[-1]["speakers"][-1]["content"] += " " + lines[i]
                result[-1]["speakers"][-1]["content"] = re.sub(
                    r"\s+", " ", result[-1]["speakers"][-1]["content"]
                ).strip()

            i += 1

    return result


def get_session_not_delivered_speeches_pages_range(pages_list):
    start = None
    end = None

    i = len(pages_list) - 1
    while i >= 0:
        if end is None and re.search(
            r"TŁOCZONO\s+Z\s+POLECENIA\s+MARSZAŁKA\s+SEJMU\s+RZECZYPOSPOLITEJ\s+POLSKIEJ",
            pages_list[i],
        ):
            end = i

        if (
            start is None
            and re.search(r"Załącznik", pages_list[i])
            and re.search(r"Teksty\s+wystąpień\s+niewygłoszonych", pages_list[i])
        ):
            start = i
            break

        i -= 1

    return start, end


def remove_headers_and_footers(page):
    # page = re.sub(r"^Oświadczenia\s+poselskie\s*\n?\s*", "", page.strip())
    page = re.sub(r"^\s*\d+\s*\n", "", page)
    page = re.sub(r"^Spis\s+treści\s*\n", "", page)
    # page = re.sub(r"^Oświadczenia\s+poselskie\s*\n?\s*", "", page.strip())
    page = re.sub(
        r"\s*\n?\s*TŁOCZONO\s+Z\s+POLECENIA\s+MARSZAŁKA\s+SEJMU\s+RZECZYPOSPOLITEJ\s+POLSKIEJ(.|\n)*?$",
        "",
        page,
    )
    page = re.sub(r"\s*\n?\s*Załącznik\s*$", "", page)
    page = re.sub(r"\s*\n?\s*Teksty\s+wystąpień\s+niewygłoszonych\s*$", "", page)
    return page


def merge_consecutive_brackets(text):
    # Variables to keep track of the current state and store processed text
    new_text = ""
    bracket_text = ""
    inside_bracket = False

    lines = text.split("\n")

    for line in lines:
        clean_line = line.strip()
        # Check if the current line contains the start of bracketed text
        if "(" in clean_line:
            inside_bracket = True
            bracket_text += " " + clean_line if bracket_text else clean_line
        # If we are inside brackets, append the line to bracket_text
        elif inside_bracket:
            # Directly append if the line continues with a hyphen or starts with lowercase (indicating continuation)
            if clean_line.endswith("-") or (
                clean_line[0].islower() and not clean_line.endswith(")")
            ):
                bracket_text += clean_line
            else:
                bracket_text += " " + clean_line
        else:
            # Add non-bracketed lines directly to new_text
            new_text += line + "\n"

        # Check if the line contains the closing bracket and process accordingly
        if ")" in clean_line and inside_bracket:
            # Normalize the space within the brackets and remove hyphens at line breaks
            bracket_text = re.sub(
                r"- ", "", bracket_text
            )  # Handle hyphenated words correctly
            bracket_text = re.sub(r"\s+", " ", bracket_text)  # Normalize spaces
            new_text += bracket_text + "\n"
            bracket_text = ""
            inside_bracket = False

    # Ensure any remaining text is added to the output
    if bracket_text:
        # This handles the case where text may remain in the buffer
        new_text += bracket_text

    return new_text.strip()
