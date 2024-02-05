from datetime import time
import re
from typing import List, Dict


def get_intra_breaks(pages: List[str]) -> List[Dict[str, time]]:
    breaks: List[Dict[str, time]] = []
    for page in pages:
        definite_break = re.search(
            r"\(\s*Przerwa\s+w\s+posiedzeniu\s+od\s+godz\.\s+(\d+)\s+min\s+(\d+)\s+do\s+godz\.\s+(\d+)\s+min\s+(\d+)\s*\)",
            page,
        )

        if definite_break:
            start_hour = int(definite_break.group(1))
            start_minute = int(definite_break.group(2))
            end_hour = int(definite_break.group(3))
            end_minute = int(definite_break.group(4))
            breaks.append(
                {
                    "start": time(start_hour, start_minute),
                    "end": time(end_hour, end_minute),
                }
            )

    return breaks
