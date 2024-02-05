from datetime import time
import re
from typing import List, Dict


def get_intra_breaks(pages: List[str]) -> List[Dict[str, time]]:
    breaks: List[Dict[str, time]] = []
    for page in pages:
        definite_breaks = re.findall(
            r"\(\s*Przerwa\s+w\s+posiedzeniu\s+od\s+godz\.\s+(\d+)\s+min\s+(\d+)\s+do\s+godz\.\s+(\d+)\s+min\s+(\d+)\s*\)",
            page,
        )

        for definite_break in definite_breaks:
            start_hour = int(definite_break[0])
            start_minute = int(definite_break[1])
            end_hour = int(definite_break[2])
            end_minute = int(definite_break[3])
            breaks.append(
                {
                    "start": time(start_hour, start_minute),
                    "end": time(end_hour, end_minute),
                }
            )

    return list(sorted(breaks, key=lambda x: x["start"]))
