import unittest
from src.custom_json import obj2pretty_json
from src.lib import report_to_obj
from datetime import time
from tests.utils import get_file_path_in_same_folder


class SessionReport(unittest.TestCase):
    # TODO: get_table_of_contents is crashing
    def test(self):
        file_path = get_file_path_in_same_folder(__file__, "01_j_ksiazka.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term_number"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["sitting_start_time"], None)
        self.assertEqual(obj["sitting_end_time"], None)
        self.assertEqual(obj["session_date"].isoformat(), "2023-12-12T00:00:00")
        self.assertEqual(obj["session_start_time"], time(10, 13))
        self.assertEqual(obj["session_end_time"], time(23, 4))
        self.assertEqual(
            obj["session_intra_breaks_times"],
            [
                {"start": time(13, 42), "end": time(14, 12)},
                {"start": time(17, 2), "end": time(17, 13)},
                {"start": time(17, 18), "end": time(18, 4)},
                {"start": time(21, 19), "end": time(21, 46)},
                {"start": time(21, 46), "end": time(21, 50)},
                {"start": time(22, 12), "end": time(22, 34)},
            ],
        )
        self.assertEqual(obj["speaker_senior"], None)
        self.assertEqual(obj["speaker"], "Szymon Hołownia")
        self.assertEqual(
            obj["vicespeakers"],
            [
                "Monika Wielichowska",
                "Włodzimierz Czarzasty",
                "Krzysztof Bosak",
                "Piotr Zgorzelski",
                "Dorota Niedziela",
            ],
        )
        # TODO: toc and content j book
        # s
        # elf.assertEqual(
        #     obj["table_of_contents"],
        # )
        # self.assertEqual(
        #     obj["text"],
        # )
