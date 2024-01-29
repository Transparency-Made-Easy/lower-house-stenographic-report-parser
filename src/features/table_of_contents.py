import re
from src.custom_json import obj2pretty_json

from src.features.session_start import get_session_start, get_session_start_from_text

SPEAKER_LINE_R = r"\.\s+\.\s*\d+$"


def get_table_of_contents(pages):
    # Almost raw lines
    raw_lines = _get_table_of_contents_lines(pages)
    # print("raw_lines", obj2pretty_json(list(raw_lines)))

    # These lines have added info like is it headerm is it speaker, but have no complex objects inside
    lines_with_tags = _get_lines_with_tags(raw_lines)
    # print("lines_with_tags", obj2pretty_json(lines_with_tags))

    lines_with_complex_info = _get_lines_with_complex_info(lines_with_tags)
    # print("lines_with_complex_info", obj2pretty_json(lines_with_complex_info))

    return lines_with_complex_info


def _get_table_of_contents_lines(pages: dict[int, str]) -> list[str]:
    start, end = _get_table_of_contents_pages_range(pages)
    lines = [_get_table_of_content_lines_from_page(pages[i]) for i in range(start, end)]
    return [line for sublist in lines for line in sublist]


def _get_table_of_contents_pages_range(pages) -> (int, int):
    start = None
    end = None

    for i, page in pages.items():
        if start is None and re.search(r"SPIS\s+TREŚCI", page):
            start = i
        elif (
            start is not None
            and end is None
            and get_session_start_from_text(page) is not None
        ):
            end = i
            break

    return start, end


def _get_table_of_content_lines_from_page(text):
    # print("RAW TEXT", text)
    # Remove last lines with text "Obrady w dniu..." and "1. posiedzenie Sejmu"

    match = re.search(r"SPIS\s+TREŚCI", text)
    if match is not None:
        index = match.start()
        text = text[:index]

    lines = text.split("\n")

    # index = None
    # for i, line in enumerate(lines):
    #     if re.search(r"Przerwa\s+w\s+posiedzeniu", line):
    #         index = i

    # if index is not None:
    #     lines = lines[: index + 1]

    # print("raw_lines", obj2pretty_json(list(lines)))

    # Maybe the page is empty
    if len(lines) == 0:
        return []

    # Last line for some reason can have text "(Przerwa w posiedzeniu)SPIS TREŚCI"
    lines[-1] = re.sub(r"SPIS\s+TREŚCI", "", lines[-1])

    # Remove start and end whitespaces
    lines = [line.strip() for line in lines]

    # Remove empty lines
    lines = [line for line in lines if len(line) > 0]

    # print("lines", obj2pretty_json(lines))
    lines = [_split_line_with_multiple_speakers(line) for line in lines]
    lines = [line for sublist in lines for line in sublist]
    lines = [line for line in lines if len(line) > 0]

    lines = [_split_line_with_speaker_and_header(line) for line in lines]
    lines = [line for sublist in lines for line in sublist]
    lines = [line for line in lines if len(line) > 0]

    lines = [_split_line_with_voting(line) for line in lines]
    lines = [line for sublist in lines for line in sublist]
    lines = [line for line in lines if len(line) > 0]

    lines = [_split_line_with_break_and_resume_at_the_same_line(line) for line in lines]
    lines = [line for sublist in lines for line in sublist]

    lines = [re.sub(r"\s+", " ", line) for line in lines]

    return lines


def _split_line_with_multiple_speakers(line):
    # If this line is not line with speaker, omit it
    if not re.search(SPEAKER_LINE_R, line):
        # print("not speaker", line)
        return [line]

    # print("speaker", line)
    matches = re.findall(r"([-\s+\w+]+(\s+\.\s*)+\d+)+?", line, re.UNICODE)
    # print("matches", matches)
    matches = [match[0] for match in matches]
    return matches


def _split_line_with_speaker_and_header(line):
    # If this line is not line with speaker, omit it
    if not re.search(r"\.\s+\.\s+\d+\w", line):
        return [line]

    matches = re.findall(r"([-\s+\w+]+(\s+\.\s*)+\d+)", line, re.UNICODE)
    speaker = matches[0][0]
    header = line.replace(speaker, "").strip()
    return [speaker, header]


def _split_line_with_break_and_resume_at_the_same_line(line):
    if re.search(r"Przerwa\s+w\s+posiedzeniu", line) and re.search(
        r"Wznowienie\s+obrad", line
    ):
        return [
            "Przerwa w posiedzeniu",
            "Wznowienie obrad",
        ]
    return [line]


def _split_line_with_voting(line):
    # If this line is not line with speaker, omit it
    if not re.search(r"Głosowanie$", line):
        return [line]

    return [line[: -len("Głosowanie")], "Głosowanie"]


def _get_lines_with_tags(lines: list[str]):
    result = []

    index = 0
    while index < len(lines):
        line = lines[index]

        if re.search(r"Przerwa\s+w\s+posiedzeniu", line):
            result.append({"type": "BREAK"})
        elif re.search(r"\s*Wznowienie\s+obrad\s*", line):
            result.append({"type": "RESUME OBRADY"})
        elif re.search(r"\s*Wznowienie\s+posiedzenia\s*", line):
            result.append({"type": "RESUME POSIEDZENIE"})

        elif re.search(SPEAKER_LINE_R, line) and re.search(r"Marszałek\s+Senior", line):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            line = re.sub(r"Marszałek\s+Senior\s*", "", line)
            result.append(
                {"type": "SPEAKER", "position": "Marszałek Senior", "name": line}
            )

        elif re.search(SPEAKER_LINE_R, line) and re.search(r"Marszałek", line):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            line = re.sub(r"Marszałek\s*", "", line)
            result.append(
                {"type": "SPEAKER", "position": "Marszałek", "name": "Marszałek"}
            )

        elif re.search(SPEAKER_LINE_R, line) and re.search(
            r"Poseł\s+Sprawozdawca", line
        ):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            line = re.sub(r"Poseł\s+Sprawozdawca\s*", "", line)
            result.append(
                {"type": "SPEAKER", "position": "Poseł Sprawozdawca", "name": line}
            )

        elif re.search(r"Poseł\s+Sprawozdawca", line) and re.search(
            SPEAKER_LINE_R, lines[index + 1]
        ):
            name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 1])
            result.append(
                {"type": "SPEAKER", "position": "Poseł Sprawozdawca", "name": name}
            )
            index += 2
            continue

        elif re.search(SPEAKER_LINE_R, line) and re.search(r"Sekretarz\s+Poseł", line):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            line = re.sub(r"Sekretarz\s+Poseł\s*", "", line)
            result.append(
                {"type": "SPEAKER", "position": "Sekretarz Poseł", "name": line}
            )

        elif re.search(r"Sekretarz\s+Poseł", line) and re.search(
            SPEAKER_LINE_R, lines[index + 1]
        ):
            name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 1])
            result.append(
                {"type": "SPEAKER", "position": "Sekretarz Poseł", "name": name}
            )
            index += 2
            continue

        elif (
            re.search(r"Sekretarz", line)
            and not re.search(SPEAKER_LINE_R, lines[index + 1])
            and re.search(SPEAKER_LINE_R, lines[index + 2])
        ):
            line_with_name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 2])
            matches = re.findall(
                r"(.*?(ści|ych|sów|cji|ej|ury|rodowiska|ego|Wsi|ogii|yki|drowia))",
                line_with_name,
            )
            end_of_position = matches[0][0].strip() if len(matches) > 0 else ""
            result.append(
                {
                    "type": "SPEAKER",
                    "position": (
                        line.strip()
                        + " "
                        + lines[index + 1].strip()
                        + " "
                        + end_of_position
                    ).strip(),
                    "name": line_with_name.replace(end_of_position, "").strip(),
                }
            )
            index += 3
            continue

        elif (
            re.search(r"Członek", line)
            and not re.search(SPEAKER_LINE_R, lines[index + 1])
            and not re.search(SPEAKER_LINE_R, lines[index + 2])
            and re.search(SPEAKER_LINE_R, lines[index + 3])
        ):
            line_with_name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 3])
            matches = re.findall(
                r"(.*?(ści|ych|sów|cji|ej|ury|rodowiska|ego|Wsi|ogii|yki|drowia|[^\.]\s*\d+))",
                line_with_name,
            )
            end_of_position = matches[0][0].strip() if len(matches) > 0 else ""
            result.append(
                {
                    "type": "SPEAKER",
                    "position": (
                        line.strip()
                        + " "
                        + lines[index + 1].strip()
                        + " "
                        + lines[index + 2].strip()
                        + " "
                        + end_of_position
                    ).strip(),
                    "name": line_with_name.replace(end_of_position, "").strip(),
                }
            )
            index += 4
            continue

        elif re.search(r"Przedstawiciel", line) and re.search(
            SPEAKER_LINE_R, lines[index + 1]
        ):
            line_with_name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 1])
            matches = re.findall(
                r"(.*(ści|ych|sów|cji|ej|ury|rodowiska|ego|Wsi|ogii|yki|drowia))",
                line_with_name,
            )
            end_of_position = matches[0][0].strip() if len(matches) > 0 else ""
            result.append(
                {
                    "type": "SPEAKER",
                    "position": line.strip() + " " + end_of_position,
                    "name": line_with_name.replace(end_of_position, "").strip(),
                }
            )
            index += 2
            continue

        elif (
            re.search(r"Zastępca\s+Przedstawiciela", line)
            and not re.search(SPEAKER_LINE_R, lines[index + 1])
            and re.search(SPEAKER_LINE_R, lines[index + 2])
        ):
            line_with_name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 2])
            matches = re.findall(
                r"(.*?(ści|ych|sów|cji|ej|ury|rodowiska|ego|Wsi|ogii|yki|drowia))",
                line_with_name,
            )
            end_of_position = matches[0][0].strip() if len(matches) > 0 else ""
            result.append(
                {
                    "type": "SPEAKER",
                    "position": (
                        line.strip()
                        + " "
                        + lines[index + 1].strip()
                        + " "
                        + end_of_position
                    ).strip(),
                    "name": line_with_name.replace(end_of_position, "").strip(),
                }
            )
            index += 3
            continue

        elif re.search(r"Zastępca\s+Przedstawiciela", line) and re.search(
            SPEAKER_LINE_R, lines[index + 1]
        ):
            line_with_name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 1])
            matches = re.findall(
                r"(.*?(ści|ych|sów|cji|ej|ury|rodowiska|ego|Wsi|ogii|yki|drowia))",
                line_with_name,
            )
            end_of_position = matches[0][0].strip() if len(matches) > 0 else ""
            result.append(
                {
                    "type": "SPEAKER",
                    "position": line.strip() + " " + end_of_position,
                    "name": line_with_name.replace(end_of_position, "").strip(),
                }
            )
            index += 2
            continue

        elif re.search(SPEAKER_LINE_R, line) and re.search(r"Poseł", line):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            line = re.sub(r"Poseł\s*", "", line)
            result.append({"type": "SPEAKER", "position": "Poseł", "name": line})

        elif re.search(r"Poseł", line) and re.search(SPEAKER_LINE_R, lines[index + 1]):
            first_part_of_name = re.sub(r"\s*Poseł\s*", "", line).strip()
            second_part_of_name = re.sub(
                r"(\s*\.\s*)+\d+", "", lines[index + 1]
            ).strip()
            name = first_part_of_name + " " + second_part_of_name
            result.append(
                {"type": "SPEAKER", "position": "Poseł", "name": name.strip()}
            )
            index += 2
            continue

        elif re.search(r"Minister", line) and re.search(SPEAKER_LINE_R, line):
            this_line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            this_line = this_line.split(" ")
            position = " ".join(this_line[:-2]).strip()
            name = " ".join(this_line[-2:])
            result.append({"type": "SPEAKER", "position": position, "name": name})

        elif (
            re.search(r"Minister", line)
            and re.search(SPEAKER_LINE_R, lines[index + 1])
            and not re.search(r"Poseł", lines[index + 1])
        ):
            line_with_name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 1])
            matches = re.findall(
                r"(.*(ści|ych|sów|cji|ej|ury|rodowiska|ego|Wsi|ogii|yki|drowia))",
                line_with_name,
            )
            end_of_position = matches[0][0].strip() if len(matches) > 0 else ""
            result.append(
                {
                    "type": "SPEAKER",
                    "position": (line.strip() + " " + end_of_position).strip(),
                    "name": line_with_name.replace(end_of_position, "").strip(),
                }
            )
            index += 2
            continue

        elif re.search(SPEAKER_LINE_R, line) and re.search(
            r"Przemów.*Prezydent.+RP", lines[index - 1]
        ):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            result.append({"type": "SPEAKER", "position": "Prezydent RP", "name": line})

        #
        elif re.search(SPEAKER_LINE_R, line) and re.search(
            r"Wystąpienie\s+prezesa\s+Rady\s+Ministrów", lines[index - 1]
        ):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            result.append(
                {"type": "SPEAKER", "position": "Prezes Rady Ministrów", "name": line}
            )

        elif re.search(SPEAKER_LINE_R, line) and re.search(
            r"Przemów.*Marszałk.+Senior", lines[index - 1]
        ):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            result.append(
                {"type": "SPEAKER", "position": "Marszałek Senior", "name": line}
            )

        elif re.search(r"Prezes\s+Rady\s+Ministrów", line) and re.search(
            SPEAKER_LINE_R, lines[index + 1]
        ):
            name = re.sub(r"(\s*\.\s*)+\d+", "", lines[index + 1])
            result.append(
                {"type": "SPEAKER", "position": "Prezes Rady Ministrów", "name": name}
            )
            index += 2
            continue

        elif re.search(SPEAKER_LINE_R, line):
            line = re.sub(r"(\s*\.\s*)+\d+", "", line)
            result.append({"type": "SPEAKER", "position": "", "name": line})

        elif re.search(r"Głosowanie", line):
            result.append({"type": "VOTING"})

        elif re.search(r"Sprawy\s+formalne", line):
            result.append({"type": "HEADER", "text": line})

        elif re.search(r"Punkt\s+\d+\s*\.\s+porządku\s+dziennego", line):
            result.append({"type": "HEADER", "text": line})

        elif len(result) > 0 and result[-1]["type"] == "HEADER":
            result[-1]["text"] += " " + line
        else:
            result.append({"type": "HEADER", "text": line})

        index += 1

    return result


def _get_lines_with_complex_info(lines_with_tags):
    lines_with_complex_info = []

    for item in lines_with_tags:
        if item["type"] == "HEADER":
            name = re.sub(r" - ", "", item["text"])
            lines_with_complex_info.append(
                {"type": item["type"], "name": name, "speakers": []}
            )
        elif item["type"] == "SPEAKER":
            lines_with_complex_info[-1]["speakers"].append(
                {"position": item["position"], "name": item["name"]}
            )
        elif item["type"] == "BREAK":
            lines_with_complex_info.append({"type": "BREAK"})
        elif item["type"] == "RESUME OBRADY":
            lines_with_complex_info.append({"type": "RESUME OBRADY"})
        elif item["type"] == "RESUME POSIEDZENIE":
            lines_with_complex_info.append({"type": "RESUME POSIEDZENIE"})
        elif item["type"] == "VOTING":
            lines_with_complex_info.append({"type": "VOTING", "speakers": []})

    return lines_with_complex_info
