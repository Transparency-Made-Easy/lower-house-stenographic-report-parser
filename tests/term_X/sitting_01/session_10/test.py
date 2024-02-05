import unittest
from src.custom_json import obj2pretty_json
from src.lib import report_to_obj
from datetime import time
from tests.utils import get_file_path_in_same_folder


class SessionReport(unittest.TestCase):
    def test(self):
        file_path = get_file_path_in_same_folder(__file__, "01_j_ksiazka.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))
        # exit()

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
                {"start": time(18, 13), "end": time(18, 52)},
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
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Antoni Macierewicz"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 38. porządku dziennego: Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                    "speakers": [
                        {"position": "Prezes Rady Ministrów", "name": "Donald Tusk"},
                        {"position": "Poseł", "name": "Mariusz Błaszczak"},
                        {"position": "Poseł", "name": "Małgorzata Gromadzka"},
                        {"position": "Poseł", "name": "Patryk Jaskulski"},
                        {"position": "Poseł", "name": "Michał Kobosko"},
                        {"position": "Poseł", "name": "Władysław Kosiniak-Kamysz"},
                        {"position": "Poseł", "name": "Anna Maria Żukowska"},
                        {"position": "Poseł", "name": "Krzysztof Bosak"},
                        {"position": "Poseł", "name": "Marek Jakubiak"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY", "speakers": []},
                {
                    "type": "HEADER",
                    "name": "Punkt 38. porządku dziennego (cd.)",
                    "speakers": [
                        {"position": "Poseł", "name": "Marcin Porzucek"},
                        {"position": "Poseł", "name": "Cezary Tomczyk"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Urszula Pasławska"},
                        {"position": "Poseł", "name": "Arkadiusz Sikora"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Marek Jakubiak"},
                        {"position": "Poseł", "name": "Barbara Bartuś"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Adam Gomoła"},
                        {"position": "Poseł", "name": "Stefan Krajewski"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Konrad Berkowicz"},
                        {"position": "Poseł", "name": "Jarosław Sachajko"},
                        {"position": "Poseł", "name": "Dariusz Matecki"},
                        {"position": "Poseł", "name": "Maciej Wróbel"},
                        {"position": "Poseł", "name": "Agnieszka Maria Kłopotek"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Grzegorz Adam Płaczek"},
                        {"position": "Poseł", "name": "Łukasz Kmita"},
                        {"position": "Poseł", "name": "Kamil Wnuk"},
                        {"position": "Poseł", "name": "Wiesław Różyński"},
                        {"position": "Poseł", "name": "Tomasz Trela"},
                        {"position": "Poseł", "name": "Ryszard Wilk"},
                        {"position": "Poseł", "name": "Anna Krupka"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Rafał Kasprzyk"},
                        {"position": "Poseł", "name": "Urszula Nowogórska"},
                        {"position": "Poseł", "name": "Joanna Scheuring-Wielgus"},
                        {"position": "Poseł", "name": "Bartłomiej Pejo"},
                        {"position": "Poseł", "name": "Paweł Szefernaker"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Piotr Paweł Strach"},
                        {"position": "Poseł", "name": "Władysław Bartoszewski"},
                        {"position": "Poseł", "name": "Anita Kucharska-Dziedzic"},
                        {"position": "Poseł", "name": "Witold Tumanowicz"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Piotr Adamowicz"},
                        {"position": "Poseł", "name": "Łukasz Osmalak"},
                        {"position": "Poseł", "name": "Adam Dziedzic"},
                        {"position": "Poseł", "name": "Krzysztof Śmiszek"},
                        {"position": "Poseł", "name": "Andrzej Tomasz Zapałowski"},
                        {"position": "Poseł", "name": "Władysław Dajczak"},
                        {"position": "Poseł", "name": "Marta Golbik"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Mirosław Adam Orliński"},
                        {"position": "Poseł", "name": "Marcin Kulasek"},
                        {"position": "Poseł", "name": "Roman Fritz"},
                        {"position": "Poseł", "name": "Bartosz Józef Kownacki"},
                        {"position": "Poseł", "name": "Krzysztof Habura"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Michał Pyrzyk"},
                        {"position": "Poseł", "name": "Katarzyna Ueberhan"},
                        {"position": "Poseł", "name": "Przemysław Wipler"},
                        {"position": "Poseł", "name": "Paweł Rychlik"},
                        {"position": "Poseł", "name": "Agnieszka Pomaska"},
                        {"position": "Poseł", "name": "Barbara Oliwiecka"},
                        {"position": "Poseł", "name": "Magdalena Sroka"},
                        {"position": "Poseł", "name": "Paulina Matysiak"},
                        {"position": "Poseł", "name": "Michał Wawer"},
                        {"position": "Poseł", "name": "Zbigniew Krzysztof Kuźmiuk"},
                        {"position": "Poseł", "name": "Elżbieta Gapińska"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Marek Sawicki"},
                        {"position": "Poseł", "name": "Marcelina Zawisza"},
                        {"position": "Poseł", "name": "Krzysztof Mulawa"},
                        {"position": "Poseł", "name": "Jarosław Zieliński"},
                        {"position": "Poseł", "name": "Maria Małgorzata Janyska"},
                        {"position": "Poseł", "name": "Ewa Schädler"},
                        {"position": "Poseł", "name": "Mirosław Maliszewski"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Włodzimierz Skalik"},
                        {"position": "Poseł", "name": "Daniel Milewski"},
                        {"position": "Poseł", "name": "Krystyna Sibińska"},
                        {"position": "Poseł", "name": "Marcin Przydacz"},
                        {"position": "Poseł", "name": "Ewa Szymanowska"},
                        {"position": "Poseł", "name": "Ireneusz Raś"},
                        {"position": "Poseł", "name": "Ireneusz Zyska"},
                        {"position": "Poseł", "name": "Paweł Śliz"},
                        {"position": "Poseł", "name": "Paweł Hreniak"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Jarosław Rzepa"},
                        {"position": "Poseł", "name": "Ewa Leniart"},
                        {"position": "Poseł", "name": "Danuta Jazłowiecka"},
                        {"position": "Poseł", "name": "Adam Luboński"},
                        {"position": "Poseł", "name": "Andrzej Grzyb"},
                        {"position": "Poseł", "name": "Waldemar Andzel"},
                        {"position": "Poseł", "name": "Katarzyna Kierzek-Koperska"},
                        {"position": "Poseł", "name": "Sławomir Ćwik"},
                        {"position": "Poseł", "name": "Tadeusz Samborski"},
                        {"position": "Poseł", "name": "Kazimierz Gwiazdowski"},
                        {"position": "Poseł", "name": "Marcin Bosacki"},
                        {"position": "Poseł", "name": "Jacek Tomczak"},
                        {"position": "Poseł", "name": "Agata Wojtyszek"},
                        {"position": "Poseł", "name": "Tomasz Zimoch"},
                        {"position": "Poseł", "name": "Zbigniew Ziejewski"},
                        {"position": "Poseł", "name": "Bartłomiej Dorywalski"},
                        {"position": "Poseł", "name": "Iwona Hartwich"},
                        {"position": "Poseł", "name": "Anna Gembicka"},
                        {"position": "Poseł", "name": "Mariusz Witczak"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Robert Telus"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 38. porządku dziennego (cd.)",
                    "speakers": [
                        {"position": "Poseł", "name": "Monika Wielichowska"},
                        {"position": "Poseł", "name": "Jacek Osuch"},
                        {"position": "Poseł", "name": "Piotr Borys"},
                        {"position": "Poseł", "name": "Ryszard Terlecki"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Jarosław Sellin"},
                        {"position": "Poseł", "name": "Agnieszka Górska"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Zbigniew Dolata"},
                        {"position": "Poseł", "name": "Jacek Karnowski"},
                        {"position": "Poseł", "name": "Piotr Kaleta"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Janusz Kowalski"},
                        {"position": "Poseł", "name": "Anna Wojciechowska"},
                        {"position": "Poseł", "name": "Krzysztof Szczucki"},
                        {"position": "Poseł", "name": "Bartosz Zawieja"},
                        {"position": "Poseł", "name": "Anna Dąbrowska-Banaszek"},
                        {"position": "Poseł", "name": "Piotr Kandyba"},
                        {"position": "Poseł", "name": "Marcin Horała"},
                        {"position": "Poseł", "name": "Marek Krząkała"},
                        {"position": "Poseł", "name": "Norbert Jakub Kaczmarczyk"},
                        {"position": "Poseł", "name": "Artur Daniel Gierada"},
                        {"position": "Poseł", "name": "Jacek Bogucki"},
                        {"position": "Poseł", "name": "Agnieszka Hanajczyk"},
                        {"position": "Poseł", "name": "Teresa Pamuła"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY", "speakers": []},
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Piotr Gliński"},
                        {"position": "Poseł", "name": "Grzegorz Puda"},
                        {"position": "Poseł", "name": "Jacek Ozdoba"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY", "speakers": []},
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Monika Wielichowska"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Krzysztof Gawkowski"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY", "speakers": []},
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Anna Maria Żukowska"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Radosław Fogiel"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 38. porządku dziennego (cd.)",
                    "speakers": [
                        {"position": "Poseł", "name": "Andrzej Gawron"},
                        {"position": "Poseł", "name": "Czesław Hoc"},
                        {"position": "Poseł", "name": "Adam Andruszkiewicz"},
                        {"position": "Poseł", "name": "Anita Czerwińska"},
                        {"position": "Poseł", "name": "Paweł Sałek"},
                        {"position": "Poseł", "name": "Mariusz Krystian"},
                        {"position": "Poseł", "name": "Anna Ewa Cicholska"},
                        {"position": "Poseł", "name": "Joanna Borowiak"},
                        {"position": "Poseł", "name": "Przemysław Drabek"},
                        {"position": "Poseł", "name": "Marlena Magdalena Maląg"},
                        {"position": "Poseł", "name": "Marcin Grabowski"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Michał Moskal"},
                        {"position": "Poseł", "name": "Dariusz Stefaniuk"},
                        {"position": "Poseł", "name": "Piotr Uściński"},
                        {"position": "Poseł", "name": "Jerzy Polaczek"},
                        {"position": "Poseł", "name": "Marcin Romanowski"},
                        {"position": "Poseł", "name": "Antoni Macierewicz"},
                        {"position": "Poseł", "name": "Elżbieta Witek"},
                        {"position": "Poseł", "name": "Mirosława Stachowiak-Różecka"},
                        {"position": "Poseł", "name": "Marek Ast"},
                        {"position": "Poseł", "name": "Artur Chojecki"},
                        {"position": "Poseł", "name": "Janusz Cieszyński"},
                        {"position": "Poseł", "name": "Paweł Szrot"},
                        {"position": "Poseł", "name": "Małgorzata Golińska"},
                        {"position": "Poseł", "name": "Robert Telus"},
                        {"position": "Poseł", "name": "Krzysztof Ciecióra"},
                        {"position": "Poseł", "name": "Jan Mosiński"},
                        {"position": "Poseł", "name": "Jan Warzecha"},
                        {"position": "Poseł", "name": "Grzegorz Lorek"},
                        {"position": "Poseł", "name": "Kacper Płażyński"},
                        {"position": "Poseł", "name": "Piotr Müller"},
                        {"position": "Poseł", "name": "Kazimierz Smoliński"},
                        {"position": "Poseł", "name": "Andrzej Adamczyk"},
                        {"position": "Poseł", "name": "Maria Koc"},
                        {"position": "Poseł", "name": "Sebastian Kaleta"},
                        {"position": "Poseł", "name": "Katarzyna Czochara"},
                        {"position": "Poseł", "name": "Józefa Szczurek-Żelazko"},
                        {"position": "Poseł", "name": "Jarosław Wiesław Wieczorek"},
                        {"position": "Poseł", "name": "Paweł Jabłoński"},
                        {"position": "Poseł", "name": "Piotr Polak"},
                        {"position": "Poseł", "name": "Maciej Małecki"},
                        {"position": "Poseł", "name": "Marek Wesoły"},
                        {"position": "Poseł", "name": "Kamil Bortniczuk"},
                        {"position": "Poseł", "name": "Katarzyna Sójka"},
                        {"position": "Poseł", "name": "Andrzej Śliwka"},
                        {"position": "Poseł", "name": "Ryszard Bartosik"},
                        {"position": "Poseł", "name": "Henryk Kowalczyk"},
                        {"position": "Poseł", "name": "Jacek Ozdoba"},
                        {"position": "Poseł", "name": "Arkadiusz Mularczyk"},
                        {"position": "Poseł", "name": "Marek Suski"},
                        {"position": "Poseł", "name": "Elżbieta Duda"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Kazimierz Bogusław Choma"},
                        {"position": "Poseł", "name": "Witold Wojciech Czarnecki"},
                        {"position": "Poseł", "name": "Waldemar Buda"},
                        {"position": "Poseł", "name": "Dominika Chorosińska"},
                        {"position": "Poseł", "name": "Jan Krzysztof Ardanowski"},
                        {"position": "Poseł", "name": "Agnieszka Anna Soin"},
                        {"position": "Poseł", "name": "Władysław Kurowski"},
                        {"position": "Poseł", "name": "Patryk Wicher"},
                        {"position": "Poseł", "name": "Dorota Arciszewska-Mielewczyk"},
                        {"position": "Poseł", "name": "Fryderyk Sylwester Kapinos"},
                        {"position": "Poseł", "name": "Anna Kwiecień"},
                        {"position": "Poseł", "name": "Robert Gontarz"},
                        {"position": "Poseł", "name": "Marek Matuszewski"},
                        {"position": "Poseł", "name": "Zbigniew Hoffmann"},
                        {"position": "Poseł", "name": "Andrzej Kryj"},
                        {"position": "Poseł", "name": "Marzena Anna Machałek"},
                        {"position": "Poseł", "name": "Dariusz Piontkowski"},
                        {"position": "Poseł", "name": "Tadeusz Woźniak"},
                        {"position": "Poseł", "name": "Edward Siarka"},
                        {"position": "Poseł", "name": "Maria Kurowska"},
                        {"position": "Poseł", "name": "Jerzy Materna"},
                        {"position": "Poseł", "name": "Artur Szałabawka"},
                        {"position": "Poseł", "name": "Sylwester Tułajew"},
                        {"position": "Poseł", "name": "Lidia Burzyńska"},
                        {"position": "Poseł", "name": "Michał Wójcik"},
                        {"position": "Poseł", "name": "Aleksander Mikołaj Mrówczyński"},
                        {"position": "Poseł", "name": "Bartłomiej Wróblewski"},
                        {"position": "Poseł", "name": "Rafał Weber"},
                        {"position": "Poseł", "name": "Antoni Macierewicz"},
                        {"position": "Prezes Rady Ministrów", "name": "Donald Tusk"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Paweł Jabłoński"}],
                },
                {"type": "BREAK"},
                {
                    "type": "RESUME OBRADY",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY", "speakers": []},
                {
                    "type": "HEADER",
                    "name": "Punkt 38. porządku dziennego: Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 40. porządku dziennego: Wybór składu osobowego Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 42. porządku dziennego: Sprawozdanie Komisji Cyfryzacji, Innowacyjności i Nowoczesnych Technologii o poselskim projekcie ustawy o zmianie ustawy o doręczeniach elektronicznych",
                    "speakers": [
                        {"position": "Poseł Sprawozdawca", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Janusz Cieszyński"},
                        {"position": "Poseł", "name": "Grzegorz Bernard Napieralski"},
                        {"position": "Poseł", "name": "Paweł Śliz"},
                        {"position": "Poseł", "name": "Adam Dziedzic"},
                        {"position": "Poseł", "name": "Adrian Zandberg"},
                        {"position": "Poseł", "name": "Bartłomiej Pejo"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY", "speakers": []},
                {
                    "type": "HEADER",
                    "name": "Oświadczenia",
                    "speakers": [
                        {"position": "Poseł", "name": "Szymon Giżyński"},
                        {"position": "Poseł", "name": "Paulina Matysiak"},
                        {"position": "Poseł", "name": "Fryderyk Sylwester Kapinos"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Renata Urszula Rak"},
                        {"position": "Poseł", "name": "Adrian Witczak"},
                        {"position": "Poseł", "name": "Norbert Jakub Kaczmarczyk"},
                        {"position": "Poseł", "name": "Mariusz Krystian"},
                        {"position": "Poseł", "name": "Marcin Romanowski"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Dariusz Matecki"},
                        {"position": "Poseł", "name": "Dorota Marek"},
                        {"position": "Poseł", "name": "Karolina Pawliczak"},
                        {"position": "Poseł", "name": "Łukasz Ściebiorowski"},
                        {"position": "Poseł", "name": "Tadeusz Samborski"},
                        {"position": "Poseł", "name": "Andrzej Grzyb"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Iwona Małgorzata Krawczyk"},
                        {"position": "Poseł", "name": "Włodzimierz Skalik"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Waldemar Andzel"},
                    ],
                },
                {"type": "BREAK"},
                {
                    "type": "HEADER",
                    "name": "Załącznik – Teksty wystąpień niewygłoszonych",
                    "speakers": [
                        {"position": "Poseł", "name": "Barbara Bartuś"},
                        {"position": "Poseł", "name": "Fryderyk Sylwester Kapinos"},
                        {"position": "Poseł", "name": "Grzegorz Lorek"},
                        {"position": "Poseł", "name": "Agnieszka Soin"},
                    ],
                },
            ],
        )
        self.assertEqual(
            obj["content"],
            [
                {
                    "speaker": "Marszałek",
                    "content": "Szanowni Państwo! Opóźniam trochę wznowienie posiedzenia, dlatego że widzę, jak długa kolejka posłów chcących zapisać się do pytań po exposé ustawiła się tutaj. Dam jeszcze na to kilka minut, bo nie chciałbym, żebyście państwo dezorganizowali tu pracę. Jak już powitam gości, poproszę o to, żebyście zajęli miejsca i wrócili później. Lista posłów zgłoszonych do pytań nie będzie zamknięta aż do momentu, kiedy skończą się oświadczenia w imieniu klubów i kół, tak że pewnie to jeszcze potrwa jakieś 2, 3 godziny. Na pewno każdy będzie mógł się zapisać do zadania pytania. Pytania dzisiaj nie są w żaden sposób limitowane. (Wypowiedź poza mikrofonem) Jeszcze raz, bo nie słyszę. (Wypowiedź poza mikrofonem) Czasowo będą limitowane, absolutnie, tak jak zawsze. (Głos z sali: Sprzeciw!) Słyszę sprzeciw. Zaraz będziemy głosować. Spokojnie, kochani państwo, wszystko po kolei. (Chwila przerwy) Szanowni Państwo! Za 4 minuty zaczynamy posiedzenie. Bardzo państwa proszę o rozważenie możliwości zapisania się do pytań w późniejszym terminie. Zgłoszenia na pewno będą otwarte jeszcze przez ponad 2 godziny – w czasie trwania exposé i wystąpień klubowych. Ze względu na szacownych gości, którzy nam dzisiaj towarzyszą, nie będę opóźniał rozpoczęcia posiedzenia bardziej niż do godz. 10.15. (Chwila przerwy) Wznawiam posiedzenie. Szanowni Państwo! Witam marszałka Senatu Rzeczypospolitej Polskiej panią Małgorzatę Kidawa-Błońską. (Oklaski) Serdecznie witam pana prezesa Rady Ministrów Donalda Tuska. (Oklaski) Witam obecnych na galerii byłych prezydentów Rzeczypospolitej Polskiej pana Lecha Wałęsę i pana Aleksandra Kwaśniewskiego. (Oklaski) Witam byłych marszałków Sejmu i Senatu oraz byłych premierów. (Oklaski) Witam bardzo licznie przybyły korpus dyplomatyczny. (Oklaski) Witam przedstawicieli Kościołów i związków wyznaniowych. (Oklaski) Witam wszystkich przedstawicieli organów i instytucji państwowych. Witam przedstawicieli wojska i służb mundurowych. (Oklaski) Witam także przedstawicieli samorządu terytorialnego, których też widzę na galerii. Cieszę się, że z nami dzisiaj, w tym uroczystym dniu, jesteście. (Oklaski) Witam wszystkich przybyłych gości. Na sekretarzy dzisiejszych obrad powołuję posłów Pawła Bliźniuka oraz Aleksandrę Karolinę Wiśniewską. Protokół i listę mówców prowadzić będzie poseł Aleksandra Karolina Wiśniewska. (Wypowiedź poza mikrofonem) Dziękuję serdecznie. Odwzajemniam się państwu miłym powitaniem. Sejm, w trybie art. 154 ust. 3 konstytucji, wybrał pana Donalda Tuska na prezesa Rady Ministrów. Prezes Rady Ministrów pan Donald Tusk zgłosił gotowość przedstawienia programu działania Rady Ministrów oraz proponowanego przez niego składu Rady Ministrów. W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o ten właśnie punkt. Prezydium Sejmu proponuje, aby Sejm w dyskusji nad tym punktem porządku dziennego wysłuchał 10-minutowych oświadczeń w imieniu klubów i 5-minutowego oświadczenia w imieniu koła. Jeżeli nie usłyszę sprzeciwu, będę uważał, że Sejm tę propozycję przyjął. Sprzeciwu nie słyszę. Wnioski formalne zgłoszono dwa. Jako pierwszy pan poseł Grzegorz Braun z Konfederacji, a później pan poseł Antoni Macierewicz z Prawa i Sprawiedliwości. (Oklaski)",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Szczęść Boże! Wysoka Izbo! Panie Marszałku! Kiedy zamykał pan wczorajszy dzień ciągle jeszcze 1. posiedzenia Sejmu X kadencji, z tego miejsca bez trybu pan prezes, premier, naczelnik Kaczyński wygłosił zdanie, które nie miało charakteru ocennego. On stwierdzał fakt: Donald Tusk agentem niemieckim. Rozumiem, że pan premier, prezes, naczelnik, w swoim czasie szef komitetu bezpieki rządu własnej kreacji nie dopełnił obowiązków, a może przekroczył uprawnienia. Być może wszedł w posiadanie informacji, do których nie miał prawa docierać, a być może nie dopełnił obowiązków, ponieważ, jak rozumiem, nie uruchomił żadnych procedur, które by doprowadziły do zbadania (Dzwonek) i przykładnego napiętnowania przypadku zdrady narodowej. Panowie Kamiński, Wąsik et consortes również… (Głos z sali: Czas.) Sprawa jest ważna, panie marszałku.",
                },
                {"speaker": "Marszałek", "content": "Tak, panie pośle, ale…"},
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "…najwyraźniej nie dopełnili obowiązków. Z tego miejsca padały już podobne zdania… (Głos z sali: A w jakiej sprawie ten wniosek formalny?) …i powinni byli siedzieć – albo Milczanowski, albo Oleksy, albo Morawiecki, albo pan redaktor Szymowski.",
                },
                {"speaker": "Marszałek", "content": "Panie pośle, proszę o konkluzję."},
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Ktoś powinien wreszcie siedzieć. To nie jest sprawa…",
                },
                {"speaker": "Marszałek", "content": "Panie pośle…"},
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "To nie jest sprawa, panie marszałku, jak był pan łaskaw to dziś podsumować, prywatnego chamstwa i braku zdolności do przestrzegania norm współżycia społecznego. (Głos z sali: Ha, ha, ha!) (Poseł Barbara Bartuś: I kto to mówi?) Proszę nie sprowadzać tego na tory prywatnego konfliktu dwóch zgryźliwych tetryków. Mówmy o sprawach… (Marszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie) …państwa w sposób… (Poruszenie na sali)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, przekroczył pan czas dwukrotnie. Naprawdę nie mogę dłużej tego tolerować. Serdecznie panu posłowi dziękuję. (Poseł Grzegorz Braun: Pytam: Kto będzie siedział? Kto będzie siedział?) (Głos z sali: Ty będziesz siedział.) (Głos z sali: Siadaj!) Dowiemy się w swoim czasie. Na razie proszę, żeby to pan usiadł. (Oklaski) A teraz zapraszam pana posła Antoniego Macierewicza. (Wypowiedź poza mikrofonem) Siedzi, ale nie w tym sensie siedzi. (Głos z sali: Będzie internowany.) Proszę o spokój, panie pośle.",
                },
                {
                    "speaker": "Poseł Antoni Macierewicz",
                    "content": "Panie Marszałku! Wysoka Izbo! Szanowni Państwo! Dzisiaj spotykamy się 12 grudnia, dzień przed rocznicą zbrodni stanu wojennego. Bardzo proszę Wysoką Izbę o uczczenie pamięci tych, którzy zostali zamordowani przez przestępców partii komunistycznej, tych, którzy współpracowali z partią komunistyczną, doprowadzając do tego, że Polacy zostali zamordowani, że milion Polaków zostało wyrzuconych z Polski, że dziesiątki tysięcy znalazło się w więzieniach, że Polska była niszczona tak, by jej nie było. Bardzo proszę o minutę ciszy. (Zebrani wstają, chwila ciszy) (Głos z sali: Wieczny odpoczynek racz im dać, Panie…) (Posłowie: …a światłość wiekuista niechaj im świeci.) (Głos z sali: Niech odpoczywają w pokoju wiecznym.) (Posłowie: Amen.) Dziękuję bardzo.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję serdecznie, panie pośle, za tę ważną inicjatywę. Przystępujemy do rozpatrzenia punktu 38. porządku dziennego: Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów (druk nr 96). Bardzo proszę o zabranie głosu prezesa Rady Ministrów pana Donalda Tuska. Bardzo proszę, panie premierze. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 659",
                    # TODO: "Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 659" should not be included
                },
                {
                    "speaker": "Prezes Rady Ministrów Donald Tusk",
                    "content": "Panie Marszałku! Panie Posłanki! Panowie Posłowie! Czcigodni Goście! 16 lat temu miałem zaszczyt wygłosić pierwsze exposé w roli premiera rządu Rzeczypospolitej. Jedno zapamiętałem. To były lekcje i wyciągnąłem z nich wnioski. Chciałem wtedy powiedzieć o wszystkim. Byłem premierem debiutantem i mówiłem ponad 3 godziny. Dostałem z domu telefon z taką przestrogą: mówiłeś wtedy 3 godziny i to, co zapamiętali Polacy, to to, że mówiłeś 3 godziny. W związku z tym dzisiaj pozwolicie państwo, że skupię się na sprawach najpoważniejszych. Jestem przekonany, że ten podniosły moment, bo takim jest przecież ten dzień, wymaga poważnej narracji. Za nami bardzo brutalna i spektakularna kampania wyborcza. Polska polityka od kilku ładnych lat zatraciła powagę debaty publicznej. Mimo okoliczności zewnętrznych i wewnętrznych, dramatów, jakie dotknęły w tych latach i nasz naród, i cały świat – pandemia, wojna, kryzys migracyjny – mimo wszystko trudno nam było, i mówię to o nas wszystkich, czasami wydobyć z siebie ton powagi i takiej pełnej odpowiedzialności, która spoczywa na nas wszystkich w tych jakże trudnych czasach. Wczoraj miałem okazję, i dziękuję za zrozumienie państwa, podziękować moim najbliższym, ale dzisiaj moje wystąpienie chciałbym rozpocząć od podziękowań tym wszystkim, którzy przez te lata nie zwątpili w to, że Polska może być lepsza (Oklaski), że Polska może być, bo na to zasługuje, najlepszym miejscem na ziemi. Chciałbym podziękować Polsce. Ja jestem bardzo dumny z mojego kraju, z Polek i Polaków, także za to, że – wiecie, tak jak już bywało w naszej historii – w kluczowej chwili potrafiliśmy się nadzwyczajnie zmobilizować, wszyscy, i doprowadzić do tego, niektórzy twierdzili: niemożliwego, przełomu. Dzięki wam ta kluczowa chwila stała się w jakimś sensie momentem dziejowym. Jestem przekonany, że 15 października dołączy do symbolicznych dat w naszym polskim kalendarzu, tych tragicznych – przed chwilą czciliśmy pamięć ofiar jednej z tych tragicznych chwil w naszej historii – i tych pięknych. Myślę, że 15 października przejdzie do historii jako dzień, nie pierwszy raz, pokojowego buntu, buntu na rzecz wolności i demokracji, trochę podobnie jak 31 sierpnia 1980 r. czy 4 czerwca, kiedy odzyskiwaliśmy… (Poseł Antoni Macierewicz: Jak obaliliście rząd Olszewskiego.) …niepodległość, wolność po zwycięstwie „Solidarności”. (Poseł Antoni Macierewicz: Ty właśnie to robiłeś.) Wyborcy wyłonili w głosowaniu nową rządową koalicję, którą będziemy – właściwie to się zaczęło już wczoraj – jeśli państwo pozwolicie, nazywać od dzisiaj koalicją 15 października. (Oklaski) To, co zdarzyło się tego dnia, to jednak rzecz dużo poważniejsza niż zmiana rządu, niż zmiana koalicji rządowej. 15 października był zwieńczeniem procesu obywatelskiego i narodowego odrodzenia, którego byliśmy uczestnikami, niektórzy świadkami, a niektórzy przeciwnikami. O tych ostatnich, pozwólcie, nie będę dziś wiele mówił. Naszą przyszłość chcemy przecież budować na naszych nadziejach, na naszych marzeniach i oczekiwaniach, które okazały się silniejsze od zwątpienia i apatii, a przede wszystkim silniejsze od zła, które rozpleniło się w polskim życiu publicznym w ostatnich latach. (Oklaski) Mam wielką osobistą satysfakcję, że w drobnej mierze pomogłem w tym przebudzeniu, w nazwaniu rzeczy po imieniu, bo tak naprawdę ten ruch 15 października narodził się właśnie od mówienia prawdy, bez ogródek i bez zafałszowań. (Głos z sali: Kłamstwa, nie prawda.) (Głos z sali: Osiem gwiazdek.) Ten ruch narodził się na długo przed moim powrotem do polskiej polityki dzięki tym wszystkim, którzy podnosili głos, czasem krzyk, od pierwszych dni rządów ustępującej ekipy. (Oklaski) Składam tym wszystkim Polkom i Polakom hołd, tak z głębi serca. Jestem przekonany, że dzisiejszy dzień to jest konsekwencja tego, że niektóre i niektórzy z was odważyli się wyjść na ulice, niektórzy odważyli się stanąć samotnie gdzieś w powiatowym mieście pod budynkiem sądu, wtedy kiedy wszyscy jakby czuli, że coś złego zaczyna się dziać z naszą ojczyzną, ale nie wszyscy znaleźli w sobie determinację czy odwagę, żeby dać temu świadectwo. Dokładnie tego dnia miał miejsce pierwszy marsz Komitetu Obrony Demokracji. Chciałbym podziękować tym wszystkim, którzy zarówno w Komitecie Obrony Demokracji, jak i w innych ruchach społecznych, organizacjach, licznych, czasami kilkuosobowych, dawali właśnie świadectwo odwagi i świadectwo takiej autentycznej, tak absolutnie bezinteresownej miłości do ojczyzny (Oklaski) i poszanowania dla państwa i prawa. Pozwólcie, że przeczytam teraz coś, co w jakimś sensie mogłoby zastąpić to moje dzisiejsze exposé. Niewiele zmieniłbym w tym tekście, który być może umknął już naszej uwadze, pamięci, a bardzo mi zależy, żebyśmy przypomnieli sobie i tego człowieka, i słowa, jakie napisał, zanim odszedł. To był manifest. Ja go przeczytam w całości właśnie dlatego, że jestem przekonany, że większość z państwa tu, w polskim Sejmie, podobnie jak większość Polek i Polaków, chyba mogłaby się pod tym podpisać. Napisał to człowiek, który był zupełnie sam tego dnia: Protestuję przeciwko ograniczaniu przez władzę wolności obywatelskich. Protestuję przeciwko łamaniu przez rządzących zasad demokracji, w szczególności przeciwko zniszczeniu, w praktyce, Trybunału Konstytucyjnego i niszczeniu systemu niezależnych sądów. Protestuję przeciwko łamaniu przez władzę prawa, w szczególności Konstytucji Rzeczypospolitej Polskiej. Protestuję przeciwko temu, aby ci, którzy są za to odpowiedzialni, podejmowali jakiekolwiek działania w kiePrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 660 runku zmian w obecnej konstytucji – najpierw niech przestrzegają tej, która obecnie obowiązuje. Protestuję przeciwko takiemu sprawowaniu władzy, że osoby na najwyższych stanowiskach w państwie realizują polecenia wydawane przez bliżej nieokreślone centrum decyzyjne, nieponoszące za swoje decyzje odpowiedzialności. Protestuję przeciwko takiej pracy w Sejmie, kiedy ustawy tworzone są w pośpiechu, bez dyskusji i odpowiednich konsultacji, często po nocach, a potem muszą być od razu poprawiane. (Głos z sali: Wiatraki.) Protestuję przeciwko marginalizowaniu roli Polski na arenie międzynarodowej i ośmieszaniu naszego kraju. Protestuję przeciwko niszczeniu przyrody, szczególnie przez tych, którzy mają ją chronić, i innych obszarów cennych przyrodniczo. Protestuję przeciwko dzieleniu społeczeństwa, umacnianiu i pogłębianiu tych podziałów. W szczególności protestuję przeciwko budowaniu „religii smoleńskiej” i na tym tle dzieleniu ludzi. Protestuję przeciwko seansom nienawiści, przeciwko językowi nienawiści i ksenofobii wprowadzanej przez władzę do debaty publicznej. Protestuję przeciwko obsadzaniu wszystkich możliwych do obsadzenia stanowisk swoimi ludźmi, którzy w większości nie mają odpowiednich kwalifikacji. Protestuję przeciwko pomniejszaniu dokonań, obrzucaniu błotem i niszczeniu autorytetów takich ludzi jak Lech Wałęsa czy byli prezesi Trybunału Konstytucyjnego. Protestuję przeciwko nadmiernej centralizacji państwa i zmianom prawa dotyczącego samorządów i organizacji pozarządowych zgodnie z doraźnymi potrzebami politycznymi rządzącej partii. Protestuję przeciwko wrogiemu stosunkowi władzy do imigrantów oraz przeciw dyskryminacji różnych grup mniejszościowych: kobiet, osób homoseksualnych, muzułmanów i innych. Protestuję przeciwko całkowitemu ubezwłasnowolnieniu telewizji publicznej i niemal całego radia i zrobieniu z nich tub propagandowych władzy. Protestuję przeciwko wykorzystaniu służb specjalnych, Policji i prokuratury do realizacji swoich własnych, partyjnych lub prywatnych, celów. Protestuję przeciwko nieprzemyślanej, nieskonsultowanej i nieprzygotowanej reformie oświaty. Protestuję przeciwko ignorowaniu ogromnych potrzeb służby zdrowia. To jest 15 protestów. Ten, który to napisał, a było to, wiecie, 6 lat temu… Już 6 lat temu ktoś tak precyzyjnie – może to nie jest piękny literacki tekst – nazwał lęki, niepokoje, złość, jakie rodziły się w polskich sercach, chociaż ci, którzy głośno o tym mówili, mieli prawo wówczas czuć się samotni. Ten człowiek zakończył ten spis protestów słowami: Przede wszystkim wzywam, aby przebudzili się ci, którzy popierają PiS – nawet jeśli podobają się wam postulaty PiS-u, to weźcie pod uwagę, że nie każdy sposób ich realizacji jest dopuszczalny. Realizujcie swoje pomysły w ramach demokratycznego państwa prawa, a nie w taki sposób jak obecnie. Tych, którzy nie popierają PiS-u, bo polityka jest im obojętna albo mają inne preferencje, wzywam do działania – nie wystarczy czekać na to, co czas przyniesie, nie wystarczy wyrażać niezadowolenia w gronie znajomych, trzeba działać. (Głos z sali: J…ć PiS.) A form możliwości jest naprawdę dużo. Proszę was jednak, pamiętajcie, że wyborcy PiS to także nasze matki, nasi bracia, sąsiedzi, przyjaciele i koledzy. Nie chodzi o to, żeby toczyć z nimi wojnę – być może tego właśnie chciałby PiS – ani nawrócić ich, bo to naiwne, ale o to, aby swoje poglądy realizowali zgodnie z prawem i zasadami demokracji. (Wypowiedź poza mikrofonem) Ja, zwykły, szary człowiek, taki jak wy, wzywam was wszystkich: nie czekajcie dłużej. Piotr Szczęsny, szary człowiek, spłonął jesienią 2017 r. (Poseł Iwona Ewa Arent: Za to odpowiadacie.) 2017 roku… (Głos z sali: Rozpłacze się.) Nie, panie pośle, nie rozpłaczę się. (Poruszenie na sali) Chcę powiedzieć, że wszystkie zdania…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Proszę państwa, naprawdę… Przepraszam, panie premierze. Nie musicie się państwo zgadzać z poglądami tego człowieka, ale bardzo proszę o szacunek dla majestatu śmierci. (Poseł Henryk Kowalczyk: To jest wzywanie…) To jest obywatel Rzeczypospolitej Polskiej (Poruszenie na sali), który wyraził swoją opinię i przypieczętował ją swoim życiem. Szacunku trochę, drodzy państwo. (Oklaski) Bardzo proszę, panie premierze.",
                },
                {
                    "speaker": "Prezes Rady Ministrów Donald Tusk",
                    "content": "Jestem poruszony, czytając te słowa, i też trochę poruszony, słysząc okrzyki niezadowolenia, bo nie jest tak łatwo powiedzieć słowa nacechowane szacunkiem i w jakimś sensie miłością do tych, którzy mają inne poglądy w dniu, w którym decyduje się na tak tragiczny w swojej formie protest. Na tej sali, drodzy państwo, także tu, wśród nas, są posłanki i posłowie, którzy również doświadczyli tragedii. (Poseł Piotr Gliński: Zabicie Rosiaka.) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 661 Nie chcę, żeby ten dzień był pod znakiem wspomnień dramatycznych, tragicznych i smutnych, ale nie mogę nie wspomnieć mojego przyjaciela, prezydenta mojego miasta Pawła Adamowicza. (Oklaski) Nie mogę i nie chcę wyrzucić z pamięci tego symbolicznego momentu, w którym wzywał do solidarności, gdy mówił o Gdańsku jako o mieście szczodrym, hojnym, i było to w dniu, kiedy Polacy od wielu lat łączą się w takiej autentycznej solidarności na rzecz słabszych, na rzecz chorych. (Poseł Henryk Kowalczyk: O Rosiaku nie zapomnieć…) Chcę, żebyśmy pamiętali o wszystkich, bez wyjątku, ofiarach przemocy, pogardy, nienawiści, konfliktu po to, aby dzień 15 października, być może dzień, w którym udzielicie wotum zaufania nowej Radzie Ministrów, był początkiem odrodzenia. Odrodzenia tego ducha autentycznej solidarności i poszanowania praw wspólnoty, w której ludzie się różnią. Przecież mieliśmy, mamy i będziemy mieli różne poglądy na wiele spraw, ale chcemy być wspólnotą i temu przede wszystkim będzie służyła praca nowego rządu. Na czym ma polegać ta wspólnota? Dlaczego mamy dzisiaj taki problem z powiedzeniem o sobie, że jesteśmy wspólnotą? Dlaczego te lata były nacechowane coraz gorętszym konfliktem politycznym, emocjami? Nie tylko w tej Izbie, bo, jak wiecie, to jest tu akurat coś naturalnego, bo po to się zbieramy w polskim Sejmie, w polskim Senacie, żeby się spierać. Ale przecież istotą demokracji, istotą państwa, gdzie żyją wolni obywatele, jest to, żeby spierać się, toczyć tę wojnę na górze, tu, w Sejmie, w parlamencie, po to, żeby uchronić własny naród, własne rodziny, Polki i Polaków od takiej nieustannej wojny politycznej tam, na dole, wśród zwykłych ludzi, w naszych domach. To nie są puste słowa. Przecież wszyscy cierpimy z tego powodu, bez wyjątku. (Oklaski) Będę prosił was wszystkich, żebyście pomyśleli o tych republikańskich fundamentach, ramach, które pozwalają budować wspólnotę polityczną i wspólnotę narodową. Jesteśmy tak różni, mamy tak różne poglądy, różne korzenie, przywiązani jesteśmy czasami do różnych tradycji, wierzymy w Boga lub gdzie indziej szukamy inspiracji do bycia dobrym – przecież tak, to jest to bogactwo, to jest nasz naród. Każdy jest wart szacunku i respektu. Każdy jest wart swoich praw. To, co naprawdę buduje wspólnotę, to są rządy prawa, to jest konstytucja, to są zasady demokracji, to jest bezpieczna granica i bezpieczne terytorium, to są te sprawy, o które nie powinniśmy się w żadnym wypadku kłócić i spierać. One są czymś, co musimy respektować bez wyjątku, po to, żeby móc się różnić w innych sprawach (Oklaski), żeby móc się różnić bezpiecznie, z szacunkiem. Pamiętam słowa naszego papieża, kiedy prosił, żeby nie budować mu pomników i żeby raczej słuchać tego, co mówi. Różni ludzie różnie oceniają dziedzictwo Jana Pawła II. (Głos z sali: Świętego.) Ja mam jak najlepsze wspomnienia, także z moich osobistych spotkań. Pamiętam te słowa, które wygłosił w Sopocie, w moim Sopocie, i które są chyba takim oczywistym mottem albo powinny być oczywistym mottem dla nas wszystkich, niezależnie od tego, z której strony sali siedzimy. To były słowa o tym, że nie ma solidarności bez miłości. (Oklaski) Ja wiem, że bardzo często, kiedy słowo „miłość” pojawia się w politycznych wystąpieniach, manifestach, budzi czasami uśmiech, drwinę. Wiecie co? Ja tego nie rozumiem. Co jest w tym dziwnego? Przecież ta miłość… Nie mówimy tylko o relacjach między ludźmi, przecież jakże często mówimy o miłości do ojczyzny. (Poseł Bożena Borys-Szopa: Osiem gwiazdek.) Ja kocham moją ojczyznę, Polskę, bez pamięci. Nie wyobrażam sobie polityki bez miłości. (Oklaski) To było już po odzyskaniu niepodległości, ale wcześniej też w moim Gdańsku, na Zaspie, Jan Paweł II mówił o tym, czym jest solidarność. I dedykuję te słowa tym wszystkim – a jest nas tutaj jeszcze całkiem liczna grupa – którzy współtworzyli „Solidarność”. Pamiętam te słowa. One nie do końca chyba przez wszystkich zostały zrozumiane. We mnie też się coś buntowało, to był czas walki. A papież powiedział, że solidarność to nigdy jeden przeciw drugiemu, że solidarność to zawsze jeden z drugim. (Oklaski) I chciałbym, szczególnie że przywołana tu została data jednego z dramatycznych polskich konfliktów, żebyśmy wyciągali z tych słów wnioski głębokie, autentyczne i prawdziwe. Jeśli chcemy odbudować wspólnotę narodową, jeśli chcemy naprawdę doczekać odrodzenia naszej polskiej wspólnoty, to musimy – nie mamy wyjścia, nie ma alternatywy – szanować reguły, jakie ustalamy dla nas wszystkich, z konstytucją na czele, z prawem. Ale musimy też rozumieć, że lekcja „Solidarności” to jest lekcja zdolności pokonywania różnic między ludźmi i budowania na co dzień tej wspólnoty, która pozwala się różnić, ale też pozwala wspólnie działać i wspólnie nieść odpowiedzialność za własną ojczyznę. Mówię tutaj o szczególnej roli prawa, praworządności i rządów prawa. Nie ma naprawdę nic ważniejszego dla nowoczesnego narodu jak zestaw praw, obowiązków uznawanych za wspólne bez wyjątku. Ktoś mógłby pomyśleć, że słowa, które przeczytam, to jedno zdanie mógł wygłosić ktoś, nie wiem, z Wolnych Sądów, ktoś z protestujących w czasie, kiedy demontowano Trybunał Konstytucyjny. One brzmią bardzo nowocześnie, tak jakby właśnie ktoś rok temu je powiedział: Nie dojdziemy do wolności przez łamanie prawa, ale przez jego przestrzeganie. To powiedział Romuald Traugutt w trakcie powstania styczniowego. Nawet wtedy, w takiej sytuacji przywódca powstania nie miał wątpliwości, że przestrzeganie prawa, że uznanie jakichś reguł za wspólne, reguł, których nie można przekraczać, to jest podstawa wolności, a w konsekwencji podstawa autentycznej wspólnoty. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 662 Dlatego o tym mówię, bo dzisiaj mam zaszczyt jako wczoraj wybrany przez Sejm, desygnowany prezes Rady Ministrów, koordynować na szczeblu rządowym prace koalicji 15 października i chcę wam, drodzy, pokazać istotę tego fenomenu, jaki budujemy w tej chwili: politycznego, pozytywnego fenomenu, który naprawdę pokazuje, że wspólnota jest możliwa. (Głos z sali: Czekamy na pokazanie.) I poszanowanie wspólnych reguł jest możliwe, nawet jeśli się ludzie między sobą różnią. Powstała koalicja partii bardzo różnych, mających poglądy na wiele spraw naprawdę odmienne, bo to jest ludzkie i to jest naturalne. I ta koalicja mówi o sobie, że jest koalicją 15 października… (Poseł Bożena Borys-Szopa: Nie, ośmiu gwiazdek.) …bo zgodziliśmy się co do fundamentów, które są przecież do zaakceptowania przez was wszystkich. Dzisiaj żyjemy w takim momencie historycznym, gdy chyba nikt nie może mieć wątpliwości, co jest naszym głównym zadaniem, jakie są nasze naczelne cele. Nie możemy udawać, że żyjemy w świecie, który pozwala na niekończące się kłótnie i swary. Żyjemy w miejscu i w czasie, które bezwzględnie wymagają odbudowy politycznej wspólnoty, wspólnego działania. Na świecie robi się naprawdę niebezpiecznie. Nie będę musiał państwa przekonywać, że naród podzielony, naród skłócony, z władzą, która na konflikcie buduje swoją pozycję, naród, w którym różne grupy uznają za nieważne reguły przyjęte czy to w konstytucji, czy w innych przepisach prawa – że taki naród narażony będzie wielokrotnie bardziej na ryzyka związane z konfliktami, które targają dzisiaj światem i naszym regionem. Jeśli pozostaniemy tak podzieleni, jak to było przez ostatnie lata, jeśli będziemy podzieleni na dwie nieprzystające połówki, to tak jakby było nas dwa razy mniej, tak jakby Polska była dwa razy mniejsza. Wiecie dobrze, że to wyzwanie, jakie przed nami stoi, wymaga pełnej koncentracji sił i dobrej woli. Slogan, że siła jest w jedności, dzisiaj nie jest sloganem. To jest pierwsze polityczne przykazanie. I chcę wam powiedzieć, że dla mojego rządu, dla naszego rządu, też dla waszego rządu, bo to będzie rząd Rzeczypospolitej… (Głos z sali: Ooo…) …rzeczą absolutnie kluczową jest ustalenie na nowo fundamentów, które możemy uznać za wspólne. Powiem parę słów, mam nadzieję, oczywistych. (Poseł Bożena Borys-Szopa: O programie.) Po pierwsze, wojna u naszych granic. Chyba nie muszę nikogo przekonywać, jak ważna jest trwałość naszych sojuszy, jak ważna jest silna pozycja Polski szanowanej na świecie i w Europie, Polski właśnie zjednoczonej w obliczu tego zagrożenia, jak ważne jest powtórzenie jako naszego narodowego wspólnego dogmatu, że Polska jest i będzie kluczowym, silnym, suwerennym ogniwem Sojuszu Północnoatlantyckiego (Oklaski), że Polska będzie lojalnym, stabilnym, pewnym swoich racji, pewnym swojej siły i znaczenia sojusznikiem Stanów Zjednoczonych (Oklaski), że Polska odzyska pozycję lidera Unii Europejskiej (Oklaski), że Polska będzie budowała swoją siłę, swoją pozycję, na jaką zasługuje – bo nie ma w tym słowa przesady – pozycję lidera w Unii Europejskiej przez współpracę i przez szanowanie tej większej wspólnoty, jaką jest dzisiaj Europa. Jesteśmy tym silniejsi, jesteśmy tym bardziej suwerenni, im silniejsza jest nie tylko Polska, ale także Wspólnota Europejska. (Oklaski) (Poseł Antoni Macierewicz: Zwłaszcza Niemcy.) Apeluję tu do wszystkich, żeby uznali to też za jeden z tych fundamentów, które powinny łączyć Polki i Polaków. Wydaje mi się, i chyba to nie jest przesadne ryzyko, jeśli powiem, że jednym z powodów zwycięstwa 15 października nowej koalicji było pragnienie Polek i Polaków, żeby Polska wróciła na należne miejsce w Europie. Wszyscy czuliśmy, że coś nie gra, że coś się psuje, że każdy – a przecież wśród rządzących było wielu takich – kto podważa pozycję Polski w Unii Europejskiej, każdy, kto zaczyna uprawiać ten polityczny i geopolityczny hazard… (Poseł Marek Suski: Co robiliście…) …każdy, kto obstawia absolutnie koszmarną grę na izolację, na samotność, tak naprawdę – nie chcę używać dzisiaj za mocnych słów, bo przecież ktoś z tej strony by od razu krzyknął: zdrada stanu… Ale wiecie, coś w tym jest. Każdy, kto naraża dzisiaj Polskę na bycie obok, bycie poza, bycie sam na sam z tym, co się dzieje wokół naszych granic, naraża nie tylko fundamentalne interesy Rzeczypospolitej, ale naraża na wielkie ryzyko byt naszej ojczyzny. (Oklaski) Proszę wszystkich, abyśmy przestali udawać, że zagrożeniem dla Polski są nasi przyjaciele i sojusznicy z Paktu Północnoatlantyckiego i Unii Europejskiej. To jest naprawdę gra ryzykowna, żeby nie powiedzieć: szalona. Mamy dzisiaj Rosję atakującą Ukrainę, mamy wszyscy poczucie, że tam jest daleko od rozstrzygnięcia. Chyba wszyscy wiemy, co by się stało, gdyby Rosja zatriumfowała w tym konflikcie. Chyba w tej sytuacji, w tym kontekście nie możemy udawać i nikt na tej sali nie ma prawa udawać, że nie zna wysokości tej stawki. I każdy na tej sali, każdy, kto skończył szkołę podstawową, podstawowy kurs historii, musi wiedzieć, że samotna Polska to jest Polska narażona na największe ryzyka. Wzywam wszystkich tutaj bez wyjątku, żebyście rozpoczęli współpracę z nowym rządem nad osadzeniem Polski na mocnych podstawach w tej wspólnocie, która jest naszą wspólnotą, i żebyście pomogli temu rządowi i mnie osobiście w odbudowaniu pozycji Polski po to, żeby to Polska decydowała, jak ma wyglądać Unia Europejska. (Oklaski) (Głos z sali: Reset…) My naprawdę to zrobimy. Mogę państwa uspokoić. Żadne manewry, żadne próby gier, żadne próby zmian traktatów, które są wbrew naszym interesom – to nie wchodzi w rachubę. Ja nie wiem… tzn. tak obserwowałem wasze wysiłki albo i zaniechania w Unii EuroPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 663 pejskiej, w całej polityce zagranicznej i chcę wam powiedzieć, że naprawdę mnie nikt nie ogra w Unii Europejskiej. (Oklaski) (Głos z sali: Ha, ha, ha!) (Głos z sali: Dobry żart.) (Poseł Antoni Macierewicz: Nie, nie, ale podawałeś marynarkę bardzo uprzejmie.) Chcę wam powiedzieć, że koalicja 15 października dobrze wie, że Polska nie ma żadnego powodu i polscy politycy nie powinni mieć żadnego powodu, żeby czuć kompleksy wobec kogokolwiek w Europie. (Oklaski) To nerwowe szamotanie się, obrażanie wszystkich wkoło, szukanie wrogów tam, gdzie mamy przyjaciół… (Poseł Marek Suski: Szczególnie u Putina…) …to osłabianie, czasami kompromitowanie samych siebie – to wszystko mogło nas kosztować o wiele, wiele więcej niż jakieś zwykłe reputacyjne straty w dyplomacji. I dlatego ja wam gwarantuję, nowa koalicja rządowa gwarantuje, że wrócimy na miejsce Polsce należne. Tak się stanie. (Oklaski) W wystąpieniu takim jak to dzisiejsze musimy mówić głośno i stanowczo i też jednym głosem o Ukrainie. Słuchajcie, to też jest sprawa, która musi nas połączyć, bo widzimy dzisiaj prezydenta Zełenskiego, który próbuje na nowo przekonać świat do tego, o co tak naprawdę idzie gra, że wojna, atak Rosji na Ukrainę to jest atak na nas wszystkich. Będziemy – i liczę tutaj na współpracę wszystkich sił politycznych – głośno i zdecydowanie domagać się pełnej mobilizacji wolnego świata, świata Zachodu na rzecz pomocy Ukrainie w tej wojnie. (Oklaski) Nie ma dla takiego myślenia żadnej alternatywy. Ja już nie mogę słuchać czasami niektórych polityków europejskich, z innych państw Zachodu, którzy mówią coś o zmęczeniu sytuacją na Ukrainie. Oni są zmęczeni. (Głos z sali: Kto?) Oni mówią w twarz prezydentowi Zełeńskiemu, że już nie mają siły, że są wyczerpani. (Poseł Antoni Macierewicz: On się Scholz nazywa.) Chcę powiedzieć, że zadaniem Polski, zadaniem nowego rządu, ale też zadaniem nas wszystkich jest głośno, stanowczo domagać się od całej wspólnoty Zachodu pełnej determinacji w pomocy Ukrainie w tej wojnie. Będę to robił od pierwszego dnia. (Oklaski) Chcę też powiedzieć, że pełne zaangażowanie Polski na rzecz Ukrainy w tym okrutnym konflikcie z agresorem rosyjskim nie może oznaczać braku serdecznej, życzliwej asertywności wtedy, kiedy chodzi o polskie interesy, o interesy polskich przedsiębiorców, kierowców, rolników polskiego państwa. (Oklaski) To naprawdę nie jest takie trudne pomagać naszemu sojusznikowi, bratu, zaprzyjaźnionej z nami dzisiaj i toczącej śmiertelny bój Ukrainie. Nie jest tak trudno umieć widzieć te dwie sprawy w sposób precyzyjny. Tak więc pełne polskie zaangażowanie na rzecz walczącej Ukrainy. A Polaków nikt nie musi uczyć solidarności – na tym zupełnie elementarnym poziomie byliśmy świadkami, uczestnikami niebywałego zrywu, polskiej kolejnej solidarności wtedy, kiedy pomagaliśmy rodzinom ukraińskim, które musiały uciekać przed wojną. Równocześnie – tutaj też liczę na współpracę wszystkich bez wyjątku – będziemy bardzo precyzyjnie i, jeśli będzie trzeba, także w sposób twardy pilnować polskich interesów w relacji z każdym sąsiadem. (Poseł Antoni Macierewicz: Z niemieckim też, tak?) Z każdym sąsiadem. Z każdym sąsiadem Polski, który chce wspólnie z nami dalej budować i wzmacniać wolny świat (Oklaski), oparty na wartościach, o które dzisiaj Ukraina walczy. Niech to będzie też takie memento, bo wydaje mi się, że do niektórych to nie dotarło, o co tak naprawdę toczy się tam wojna. Tak jakbyście zapomnieli, niektórzy z was… (Głos z sali: Którzy?) (Głos z sali: Kto zapomniał?) …że Ukraińcy podjęli ten niezwykły wysiłek na rzecz integracji Ukrainy z resztą Europy, że ten bój tak naprawdę zaczął się wtedy na Majdanie, a jego celem było przystąpienie Ukrainy do Unii Europejskiej. (Głos z sali: No i co tam Sikorski...) Dobrze pamiętacie, z jakim zachwytem nasi przyjaciele na Ukrainie mówili: o, Polska, wam się udało, to jest taka wspaniała lekcja dla nas. Chcieli nas we wszystkim naśladować (Oklaski), widząc, co znaczą umiejętne, solidarne, łączące cały naród działania na rzecz integracji z całym światem wolności, z całym światem Zachodu. Dzisiaj Ukraina krwawi także dlatego, że Ukraińcy i Ukrainki zamarzyli o tym, żeby Ukraina była taka jak inne państwa Zachodu: praworządna, demokratyczna, żeby była takim państwem, gdzie przestrzega się praw człowieka, praw mniejszości. To jest ich marzenie. Oni za to dzisiaj przelewają krew. To też jest powód naszego zaangażowania, bo zauważcie – i to jest właściwie istota politycznego dylematu – jak niebezpieczną tendencję mamy dzisiaj na świecie. Prawie wszyscy bez wyjątku polityczni przywódcy w Europie i na świecie, którzy wyrzekają się tradycyjnych, republikańskich, europejskich wartości politycznych, czyli demokracji, rządów prawa, niezależności mediów i wolności słowa itd., jakimś dziwnym zbiegiem okoliczności politycy, którzy atakują fundamenty cywilizacji politycznej Zachodu, są równocześnie antyukraińscy. Chcę, żeby dotarło do wszystkich tutaj to, co świat chyba widzi – zresztą są naprawdę fajne reakcje prawie we wszystkich stolicach Zachodu na tę zmianę w Polsce. One wynikają też z przekonania, że tylko zjednoczony Zachód, w tym Europa zjednoczona wokół wartości, o których przed chwilą mówiłem, tylko taki Zachód może pomóc Ukrainie wygrać tę wojnę. Bo ta wojna toczy się w imię właśnie tych wartości. (Oklaski) (Poseł Bożena Borys-Szopa: A co mówił Sikorski?) Dlatego w polskiej polityce będzie także bardzo wyraźna asertywność wobec tych państw i polityków, którzy odwrócili się nie tylko od tych wartości, ale dzisiaj także narażają Ukrainę na ryzyko porażki. (Poseł Grzegorz Braun: A to jest exposé premiera jakiego rządu: Polski czy Ukrainy?) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 664 Nie będę wymieniał tych nazwisk i nazw tych państw, bo za kilkadziesiąt godzin będę jechał m.in. do Brukseli z nadzieją, uzasadnioną nadzieją, że znajdziemy sposoby – inaczej niż było do tej pory – aby przekonywać naszych kiedyś tradycyjnych sojuszników do jednoznacznej postawy na rzecz wolności, na rzecz republikańskich wartości i na rzecz obrony Ukrainy przed rosyjską agresją. (Oklaski) Mówię o potrzebie wspólnoty dlatego – skoro wiemy to z naszego własnego doświadczenia – że kiedy dzieją się tak straszne rzeczy jak dzisiaj w Ukrainie, to tylko wspólnota może podołać takim wyzwaniom. Ale przecież mamy inne wyzwania. Migracja. Naprawdę można szanować innego człowieka, można szanować inne religie, można szanować inne rasy i równocześnie mieć świadomość, jak wielkim zagrożeniem dla Europy i dla całego świata są te turbulencje, jak wielkie jest zagrożenie niekontrolowaną wędrówką ludów spowodowaną konfliktami, wojną, biedą, głodem czy zmianami klimatycznymi. (Głos z sali: Nieodpowiedzialnością elit.) Ja będę proponował – i to będzie także chyba widoczna zmiana w porównaniu z ostatnimi latami – żebyśmy umieli bardzo precyzyjnie odróżnić narzędzia, metody działania, które są należne wspólnocie narodowej, które służą umacnianiu suwerenności państwowej Polski, od narzędzi, z których też musimy umieć korzystać na rzecz wspólnoty europejskiej czy wspólnoty globalnej. Chciałbym, żeby to wreszcie dotarło do wszystkich obecnych w tej Izbie, że… (Głos z sali: Że zgodzicie się.) …z kryzysem migracyjnym czy z katastrofą klimatyczną nie poradzi sobie pojedyncze państwo. (Głos z sali: Ilu ściągniecie?) Stany Zjednoczone sobie nie są w stanie poradzić z presją migracyjną. To jednak jest trochę większe państwo niż Polska. Chcę, żeby Polska umiała wziąć współodpowiedzialność za ochronę europejskich granic i za ochronę europejskiego terytorium. (Oklaski) W programie mojego rządu nie będzie miejsca na handel wizami… (Oklaski) (Poseł Bożena Borys-Szopa: Bo przypłyną.) …nie będzie tolerancji dla pozornych działań. Polska wschodnia granica będzie granicą szczelną. (Oklaski) Polskie służby, polska administracja, my wszyscy, także tutaj, w tej Izbie, będziemy skutecznie dbali o to, aby polskie i siłą rzeczy europejskie terytorium oraz polskie i europejskie granice były skutecznie chronione. Można to robić naprawdę skutecznie i równocześnie z poszanowaniem dla innych ludzi. (Oklaski) Można ochronić polską granicę i równocześnie być ludzkim. (Oklaski) Nie będziemy dłużej się wstydzić za to, że setki tysięcy ludzi korzystają ze skorumpowanego systemu zorganizowanego przez poprzednią ekipę i ta rzeka ludzi w sposób niekontrolowany, nie wiadomo kto, nie wiadomo kiedy… (Głos z sali: Kłamstwo!) …wlewała się do Polski i do Unii Europejskiej. Nie będzie tego więcej. Wyjaśnimy każdy szczegół tej sprawy. I nie chodzi tu tylko o komisję śledczą. Ona jest nam bardzo potrzebna do tego, żebyśmy wyśledzili każdy element tej sprawy, także po to, aby uniknąć fali nielegalnej emigracji. To jest nasza odpowiedzialność dzisiaj. Polska ma być bezpieczna i osiągniemy ten ideał bezpiecznego państwa. Polska może być naprawdę najbezpieczniejszym miejscem na ziemi. (Oklaski) (Głosy z sali: Jest, jest.) To nie jest fikcja. Naprawdę może być najbezpieczniejszym miejscem na ziemi, tylko musimy spełnić – i my spełnimy – tych kilka warunków. (Głos z sali: Tego nie będzie pod waszym rządem.) A więc, tak jak mówiłem, Polska nie będzie samotna, Polska będzie liderem i częścią wspólnoty europejskiej, Polska będzie niezwykle intensywnie współpracowała ze wszystkimi sojusznikami i Polska będzie strzegła swoich granic. I nikt w Polsce nie będzie handlował wizami z nikim na świecie. (Oklaski) (Głos z sali: Jakieś konkrety?) Program przyszłego rządu, jeśli od Wysokiej Izby otrzymamy wotum zaufania… (Głos z sali: Nareszcie.) Pani poseł mówi: nareszcie. Wy znacie ten program. (Głos z sali: Już 45 minut czekamy.) Ten program pisali Polacy, ten program napisali Polacy, z którymi spotykaliśmy się przez ostatnie 2 lata. (Oklaski) I to jest program do bólu konkretny. (Poseł Antoni Macierewicz: Osiem gwiazdek.) Chcę państwu powiedzieć – i mówię to z wielką satysfakcją – że wtedy, kiedy wy te 2 miesiące marnowaliście w sposób, szczerze powiem, bezwstydny, bo marnowaliście, nie tylko nic nie robiąc przez te 2 miesiące i zwlekając z przekazaniem władzy tym, którzy zyskali zaufanie Polek i Polaków… Wy te 2 miesiące wykorzystaliście do tego – nie chcę używać za mocnych słów, ale czytaliście pewnie sami o tym, co robią wasze koleżanki i wasi koledzy w ministerstwach – żeby zabezpieczyć materialnie siebie i swoich partyjnych kolegów, partyjne koleżanki. (Głos z sali: Kłamstwo!) Lista tego, co robiliście przez lata i przez ostatnie 2 miesiące, jest naprawdę imponująca i ona będzie publicznie znana. (Oklaski) My za kilkadziesiąt godzin uzyskamy wreszcie dostęp też do dokumentacji, do informacji, jak wygląda naprawdę budżet, gdzie są ukryte pieniądze, gdzie i dlaczego zniknęły pieniądze. (Głos z sali: Ha, ha, ha!) (Głos z sali: Zakopane.) My w ciągu kilkudziesięciu godzin przedstawimy Polkom i Polakom precyzyjną informację, jakie są źródła decyzji dotyczących przyszłości bezpieczeństwa energetycznego, np. tzw. małych elektrowni jądrowych. Słuchajcie, ja o tym już mówiłem publicznie, ale kiedy pytacie o konkrety, to wyobraźcie sobie, jak dużo Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 665 konkretów musimy wyjaśnić, jeśli tu, w tej Izbie, usłyszeliśmy o tym skandalu. To będzie jeden z pierwszych konkretów. Patrzę na pana ministra Mariusza Kamińskiego. Nawet się nie spodziewałem, że w moim exposé powiem, że jestem wdzięczny panu ministrowi Kamińskiemu. Sprawdzamy bardzo dokładnie już tę sprawę, panie ministrze. Nie spodziewałem się, że będziemy świadkami konfliktu na szczytach władzy, że w ostatniej chwili minister rządu, nie rządu – nie wiem, jak nazwać ten 2-tygodniowy eksperyment pana Morawieckiego – podejmie decyzję wbrew jednoznacznej opinii Agencji Bezpieczeństwa Wewnętrznego w sprawie, która dotyczy przyszłości energetyki polskiej, bezpieczeństwa energetycznego, naszej relacji z sojusznikami, być może korupcji na dużą skalę. Przecież to jest tylko jeden z przykładów, ale jakże dotkliwych, pokazujących, że oprócz 100 konkretów, oprócz programów pozostałych trzech partii koalicyjnych w koalicji 15 października my będziemy musieli bardzo konkretnie zająć się czyszczeniem. To nie jest wcale przyjemny obowiązek, ale my bez tego nie ruszymy, bez wyczyszczenia tej stajni Augiasza (Oklaski), którą zostawiają po sobie ci z was, którzy bez poszanowania procedur, bez poszanowania prawa… (Oklaski) (Poseł Waldemar Buda: Godzina minęła.) (Głos z sali: Co to jest?) (Głos z sali: Zejdź.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Proszę zejść z mównicy, panie pośle.",
                },
                {
                    "speaker": "Prezes Rady Ministrów Donald Tusk",
                    "content": "…bez poszanowania dobrych obyczajów… Wiecie, czym m.in będzie. się różnił ten rząd od poprzedniego? Słuchaliśmy wczoraj wystąpienia pana Mateusza Morawieckiego. Wygłaszał swoje exposé. Ani on nie wierzył w ani jedno zdanie, które wtedy wypowiadał, ani nikt z was nie wierzył, że to jest exposé przyszłego rządu. (Oklaski) Chciałbym, żebyście przypomnieli sobie, jak zachowywała się w czasie tego wystąpienia ta strona sali. Wysłuchaliśmy tego exposé, tych słów, które de facto pozbawione były znaczenia i treści. Wysłuchaliśmy tych słów z szacunkiem i respektem. (Głos z sali: Krzywonos.) (Głos z sali: Spokój.) Oczekuję tego także od państwa. To jest szansa dla nas wszystkich. Weźcie z tego przykład. (Oklaski) To dotyczy też filozofii nowego rządu. Będziemy się różnić, ale będziemy was szanować. Będziemy was szanować nawet wtedy, kiedy będziecie robili wszystko, żeby nie dało się was szanować. Będziemy bardzo cierpliwi. (Oklaski) Kiedy mówię m.in. o 100 konkretach, to wiecie, że jest to powód do wielkiej satysfakcji nie tylko koalicji 15 października. Mówię o 100 konkretach Koalicji Obywatelskiej, ale jak wiecie, umowa koalicyjna przewiduje syntezę programów partii, które tworzą koalicję. Myśmy zaczęli pracę wtedy, kiedy wy przez 2 miesiące robiliście to, co dzisiaj przynosi wam wstyd. Obserwowała to cała Polska. Ludzie nie wierzyli własnym oczom, kiedy widzieli, że można tak doić własną ojczyznę w ostatnich dniach sprawowania władzy. (Oklaski) My wtedy przygotowywaliśmy plany dotyczące realizacji tych projektów i innych projektów zawartych w umowie koalicyjnej. (Głos z sali: Ustawę wiatrakową.) Jeszcze nie ma naszego rządu… (Głos z sali: Ale są wiatraki.) Jeszcze nie ma naszego rządu, a już jest in vitro. (Oklaski) (Głos z sali: Wiatraki tak klaszczą…) Patrzę na was i nie mogę zrozumieć, nie mogę uwierzyć, że mogliście kompletnie odstąpić od działania, od służby jako państwo w czasie protestu na granicy polsko-ukraińskiej. Zostawiliście to kompletnie bez… Słuchajcie, przecież kontrola granic i pilnowanie interesów własnych przedsiębiorców to istota działania państwa, a wyście nie przypilnowali interesów polskich przedsiębiorców, polskich kierowców i odstąpiliście od pilnowania granicy – granicy z Ukrainą w czasie wojny. (Oklaski) To jest symboliczna chwila, więc chcę wam powiedzieć, że nie w ramach 100 konkretów czy umowy koalicyjnej koalicji 15 października, ale ze zwykłej przyzwoitości przyszli ministrowie tego rządu siedzieli ze mną całymi godzinami po nocach i szukali sposobów na jak najszybsze rozwiązanie problemu na granicy polsko-ukraińskiej. (Głos z sali: Jak Paulina Hennig-Kloska.) Szukaliśmy sposobów na to, żeby jak najszybciej uwzględnić potrzeby polskich kierowców i równocześnie natychmiast odblokować granice walczącej Ukrainy, która czeka na transporty jadące tą zablokowaną autostradą, i znaleźliśmy je. (Oklaski) Nie czekaliśmy na dzisiejsze głosowanie. (Głos z sali: Jakie to sposoby?) Rozmawiałem bardzo długo ze wszystkimi kandydatkami i kandydatami na ministrów o tym, jak realizować takie projekty i one będą zrealizowane natychmiast. Chodzi o kasowy PIT, wtajemniczanie… (Głos z sali: Wiatraki.) (Poseł Antoni Macierewicz: A co z wiatrakami?) Wiatraki wreszcie będą alternatywnym źródłem energii w Polsce. (Oklaski) (Poseł Antoni Macierewicz: Zniszczy pan rolnictwo.) Chcę wam powiedzieć, że nie czekaliśmy na to głosowanie, żeby pracować, żeby zabezpieczyć w przyszłym budżecie państwa środki. Wiecie, z wielką łatwością zaczęliście podejmować w ostatnich dniach decyzje opiewające na grube miliardy złotych, ale zuPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 666 pełnie nie pomyśleliście o tym, jak zabezpieczyć finanse. Otóż mam dobra informację: koalicja 15 października ma już gotowe projekty i plan działania. Chcemy natychmiast wprowadzić takie postulaty jak np. kasowy PIT, w wyniku czego przedsiębiorcy zapłacą podatek dochodowy dopiero po otrzymaniu środków z tytułu zapłaconej faktury, a nie z tytułu samej faktury. Czekali na to przez lata. (Oklaski) Wprowadzimy też ten wymarzony przez nich urlop. Mówię o mikroprzedsiębiorcach, mówię o setkach tysięcy ludzi harujących jak woły za nieduże pieniądze, pilnujących własnej firmy jak rodziny, żeby przetrwała w tych trudnych czasach. Ten urlop dla przedsiębiorców to jest też kwestia godności, to nie tylko jest kwestia finansowa. Chodzi o odstąpienie od płacenia składki wtedy, kiedy po prostu mała firma, działalność gospodarcza akurat nie jest aktywna, bo ci przedsiębiorcy też mają prawo do wypoczynku. (Oklaski) Ograniczymy natychmiast czas kontroli mikroprzedsiębiorców. Wiecie dobrze, że wróciły czasy… Jeśli ktoś ma do czynienia z ludźmi ciężko pracującymi na swoim, to dobrze wie, jak ciężko im jest przetrwać w gąszczu nieuzasadnionych, niekończących się, mnożących się bez umiarkowania kontroli. Pytacie o konkrety. (Głos z sali: 100.) Tak, są zapisane, są znane. Nie muszę czytać ani 100 konkretów, ani innych elementów programu rządowego innych partii politycznych. Cała Polska zna te konkrety. (Oklaski) Polska nas będzie z tego rozliczała. Nie boję się tego. W imieniu całego przyszłego rządu mogę wam powiedzieć: nie obawiamy się żadnej z tych obietnic – zostaną zrealizowane. (Oklaski) (Głos z sali: Ale my się boimy.) (Poseł Antoni Macierewicz: A 60 tys. kiedy?) Powiedzieliśmy… Pamiętacie państwo, jak odchodząca ekipa straszyła Polki i Polaków: o, przyjdą nowi, wszystko zabiorą. To były pierwsze działania – powtarzam – nadal rządu przed głosowaniem, a więc kandydatów na ministrów. Siedzieliśmy także przez długie godziny, żeby ta obietnica stała się gwarancją. Nic, co było dane przez lata, nic, co jest uprawnieniem polskich obywateli i obywatelek, nie zostanie zabrane. (Oklaski) Ale przecież to nie wystarczy. Wynagrodzenia dla nauczycieli wzrosną o 30% (Oklaski) i ten wzrost będzie od 1 stycznia – tak jak obiecaliśmy. Wynagrodzenia dla całej sfery budżetowej wzrosną o 20% (Oklaski) – tak jak obiecaliśmy. Tak jak obiecaliśmy, wprowadzimy natychmiast drugą w ciągu roku waloryzację rent i emerytur wtedy, kiedy inflacja będzie przekraczała 5%. (Oklaski) Śmialiście się z babciowego – będzie babciowe w tym roku. (Oklaski) W ramach programu „Aktywna mama” każdej mamie, każdej rodzinie, wszystkim rodzicom, którzy potrzebują tej pomocy, na opiekę nad swoim maleństwem wypłacimy 1500 zł miesięcznie. (Oklaski) (Głos z sali: Brawo!) Ja podaję tylko przykłady tych rzeczy, które ruszą natychmiast, które już ruszyły, mimo że blokowaliście tak długo, jak się dało, powstanie nowego rządu. Nie czekaliśmy naprawdę ani chwili. Dlaczego używam tych przykładów? Bo równocześnie będziemy prowadzili odpowiedzialną politykę fiskalną i zadbamy o stabilność finansową państwa. (Oklaski) Wiecie co? Przemawia przeze mnie też moje doświadczenie, ale także doświadczenie 8-letnich rządów PiS-u. Liczę tu na zaangażowanie i pomoc wszystkich bez wyjątku w tej Izbie, żebyśmy – to nie jest jakaś wielka magia, ale to wymaga też wzajemnego zrozumienia – znaleźli takie metody i ich używali, zgodnie z którymi będziemy dawali ludziom pomoc tam, gdzie ona będzie potrzebna. Będziemy wspierali każdą Polkę, każdego Polaka, tych, którzy chcą pracować, albo tych, którzy nie mogą i potrzebują pomocy, i równocześnie będziemy pilnowali odpowiedzialnej polityki finansowej. (Oklaski) Między innymi dlatego wprowadzimy radę fiskalną, ludzi neutralnych, którzy będą opiniowali wydatki w taki sposób, aby nasza możliwie szczodra, hojna polityka społeczna nie zagrażała w żaden sposób stabilności finansowej państwa. Polska stanie się modelowym państwem w całej Unii Europejskiej, godzącym jedną i drugą potrzebę, a więc dobrobytu obywateli i pewności, stabilności państwa. (Oklaski) (Poseł Piotr Kaleta: Władek, chyba nie jest dobrze.) Będziecie państwo zadawali dzisiaj bardzo liczne pytania. Chcę powiedzieć, że… (Głos z sali: Nie odpowiem.) …odpowiem na każde z tych pytań. Kto pamięta moje poprzednie kadencje w roli premiera, powinien pamiętać, że odpowiadałem tu, w tej Izbie, na każde pytania. I państwo otrzymacie odpowiedź na każde pytanie dotyczące programu koalicji 15 października, programów poszczególnych partii, tempa, czasu, w jakim będziemy w stanie to zrobić. Nie musicie się obawiać. Cieszę się, to znaczy bardzo martwi mnie obyczajowość niektórych kolegów tutaj i sposób ich zachowania na sali, ale cieszę się, że państwo tak wnikliwie przeczytali te 100 konkretów i że zobaczyliście… (Oklaski) I tak mi się też, wiecie, fajnie na sercu robi, że oglądacie to biało-czerwone serce (Oklaski), bo polskie serce jest biało-czerwone. Ten symbol naprawdę ma dla nas wielkie znaczenie (Oklaski) i oznacza autentyczną empatię tego rządu wobec wszystkich, którzy będą tej empatii potrzebowali. (Poseł Piotr Gliński: Ośmiu gwiazdek nie było. Niech pan coś powie na ten temat.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle Gliński, Gwiazdka już niedługo. Pan cały czas o tych ośmiu gwiazdkach – jedna wystarczy, niebawem. (Oklaski) (Głos z sali: Osiem gwiazdek.) Nie może się doczekać Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 667",
                },
                {
                    "speaker": "Prezes Rady Ministrów Donald Tusk",
                    "content": "Nie wiem, czy państwo zauważyli, ale ja ciągle słyszę z tamtej strony okrzyki: osiem gwiazdek. Ja nie wiem, czy państwo lubicie ten… (Głos z sali: Taco Hemingwaya.) Nawet mi do głowy nie przyszło. Wy macie z tym jakieś dziwne skojarzenia, a mi nawet do głowy nie przyszło, żeby o tym pomyśleć. (Oklaski) (Głos z sali: Niech jeszcze pośpiewają.) (Głos z sali: Notoryczny kłamca.) Szanowny Panie Marszałku! Jestem świadomy i państwo też jesteście tego świadomi, że w najbliższej perspektywie zdarzą się różne trudne sytuacje – przy naszej granicy, być może w niektórych państwach, od których będzie zależało także nasze bezpieczeństwo. Chcę bardzo mocno podkreślić, że musimy się przygotować na tyle, na ile to możliwe, na tyle, na ile to w naszej mocy, abyśmy samodzielnie potrafili zadbać o nasze bezpieczeństwo, w tym bezpieczeństwo militarne. (Głos z sali: Na linii Wisły?) Zacznę prezentację osób, które będą wchodziły w skład naszego rządu, od pana wicepremiera Władysława Kosiniaka-Kamysza, pierwszego wicepremiera. (Oklaski) Jak państwo wiecie, pan Władysław Kosiniak-Kamysz będzie nie tylko pierwszym wicepremierem, ale także ministrem obrony narodowej. Zależy nam bardzo na tym, aby na czele tego resortu stał pełnowymiarowy polityk, młody, a niezwykle doświadczony i… (Poseł Antoni Macierewicz: Pełnowymiarowy, no gratulacje.) Mam nadzieję, że państwo także doceniacie niezwykle pozytywną rolę pana Władysława Kosiniaka-Kamysza i jego partii w tym przełomie 15 października. Bardzo chciałem, panie prezesie, panu podziękować (Oklaski) za niezwykłe doświadczenie wzajemnej lojalności i takiej ludzkiej solidarności. Przy okazji pozwoli pan, że to pan będzie przykładem czy ilustracją tego, do czego przywiązujemy wszyscy wielką wagę w naszej koalicji. My się nie pokłócimy. (Głos z sali: Oczywiście…) Przez 4 lata będziemy działać solidarnie, z wzajemnym szacunkiem i też – mogę tak dzisiaj chyba też powiedzieć o wszystkich liderach partii tworzących koalicję 15 października – z wzajemną sympatią, a może… (Poseł Piotr Kaleta: Miłością.) …z przyjaźnią i z przekonaniem, że razem można zrobić więcej. I zobaczycie, że ta koalicja, w skład której wchodzą cztery partie i jeszcze różne inne środowiska, bo przecież sama Koalicja Obywatelska to jest kilka środowisk z własnymi pomysłami, ambicjami, szanuje wspólne fundamenty, o których mówiłem. Będziemy razem z panem prezesem Władysławem Kosiniakiem-Kamyszem, z panem Włodzimierzem Czarzastym i oczywiście z panem marszałkiem Hołownią czuwali nad tym, żeby ta koalicja współpracowała harmonijnie, solidarnie. A te nadzieje, które gdzieś się tam pojawiały w kuluarach, że ta kadencja potrwa krócej, to są płonne nadzieje. (Oklaski) Naoglądaliśmy się władzy, gdzie interesy osobiste, osobiste ambicje uniemożliwiały zajęcie się poważnymi problemami. Zajmowaliście się przez długie miesiące i lata głównie sobą. (Głos z sali: Nie kłam.) Chcę powiedzieć, że nasza koalicja, chociaż tak różnorodna, ale właśnie dowodząca, że możliwa jest wspólnota polityczna przy różnych poglądach, da przykład wyjątkowej solidarności, lojalności i odpowiedzialności. Zobaczycie to za 4 lata, przyznacie mi rację. (Oklaski) (Głos z sali: Nudzi…) Nadzór cywilny nad polskim wojskiem to jest dzisiaj coś naprawdę kluczowego. Ten nadzór to przede wszystkim konsekwentne uzbrajanie polskiej armii z poszanowaniem tych wszystkich zobowiązań i kontraktów zawartych przez naszych poprzedników. Oczywiście wykluczam sytuacje, w których okazałoby się, że jakiekolwiek działania miałyby charakter korupcyjny. Mam nadzieję, że sprawa ujawniona przez pana Kamińskiego nie jest czymś powszechnym i nie dotyczy kwestii kontraktów zbrojeniowych. Taką mam nadzieję. Dlatego z przekonaniem, w imieniu także pana Władysława Kosiniaka-Kamysza, mogę powiedzieć, że polska armia będzie dobrze uzbrojona (Oklaski), także przy pomocy naszych sojuszników. Drugim wicepremierem w naszym rządzie będzie pan Krzysztof Gawkowski, wicepremier i minister odpowiedzialny za cyfryzację. (Oklaski) (Poseł Piotr Kaleta: Jeszcze masz czas.) Nie muszę nikogo przekonywać, jakim wyzwaniem jest dzisiaj… (Poseł Piotr Kaleta: Nasza oferta jest jeszcze aktualna.) Cyfryzacja to jest skrótowe hasło. Co znaczy dla naszego bezpieczeństwa, dla pozycji Polski w świecie rozwój najnowocześniejszych technologii? Co znaczy bezpieczeństwo w tej sferze, cyberbezpieczeństwo? Sami widzicie, jak wielkie znaczenie dzisiaj, choćby w czasie wojny rosyjsko-ukraińskiej, mają te najnowocześniejsze technologie także na placu boju. A więc obaj wicepremierzy będą w dużej mierze współodpowiedzialni za to, aby nasza armia i nasze najszerzej pojęte bezpieczeństwo były zbudowane na nowoczesnych, innowacyjnych, bardzo stabilnych fundamentach. Pana Radosława Sikorskiego nie muszę przedstawiać. (Oklaski) (Głos z sali: Nie.) (Poseł Piotr Kaleta: Thank you.) (Głos z sali: Spasibo.) Nie będę przedstawiał jego życiorysu, bo pewnie bym zawstydził tutaj kilku bohaterów aktywnych w ostatnim dniu rewolucji. (Wesołość na sali) Znamy takich Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 668",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Szanowni państwo, proszę powściągnąć swój entuzjazm.",
                },
                {
                    "speaker": "Prezes Rady Ministrów Donald Tusk",
                    "content": "Będziemy wspólnie z Radosławem Sikorskim dbali, tak jak o tym już wspomniałem, o pozycję na arenie międzynarodowej i o efektywną pracę na rzecz Ukrainy w jej wojnie z Rosją. Chcę też powiedzieć, że już przygotowujemy wizyty, z których będą płynęły bardzo konkretne wnioski. Ja po Brukseli… Też chcę was uspokoić, bo wiem, że były jakieś niepokoje i lęki – to też dotyczy naszego programu i prezentowanych w czasie kampanii moich 100 konkretów. Tak, przywiozę z Brukseli te upragnione, te wyczekiwane przez polskich przedsiębiorców, polskie samorządy miliardy euro. (Oklaski) (Poseł Piotr Kaleta: Z zamrażarki.) Władysław Bartoszewski kiedyś powiedział, nie wiem, czy państwo pamiętacie, że warto być przyzwoitym, chociaż nie zawsze się to opłaca. I być może opłaca się być nieprzyzwoitym, ale nie warto. (Oklaski) (Głos z sali: Widać po panu.) Chcę wam powiedzieć, że wrócę z Brukseli z tymi załatwionymi pieniędzmi. (Poruszenie na sali) I wiecie, co powiem Polkom i Polakom? Powiem, że udało się w ciągu pierwszych kilku dni naszych rządów być przyzwoitym i że to się nam wszystkim opłaciło. (Oklaski) Po powrocie z Brukseli udam się następnego dnia do Tallina na spotkanie z premierami Litwy, Łotwy i Estonii. Tematy oczywiste: wojna, bezpieczna granica. Będziemy wzmacniali współpracę z państwami, które podzielają nasze poglądy w tej sprawie, a więc nie tylko z naszymi sąsiadami z Litwy, Łotwy i Estonii, ale oczywiście także z Finlandią, Szwecją, a z poza Unii – również z Norwegią, szczególnie na odcinku północno-wschodnim presja nielegalnej imigracji organizowanej przez Putina i Łukaszenkę jest tak bardzo dotkliwa. Będziemy chcieli odegrać niezwykle intensywną rolę jednego z liderów nowoczesnej obrony polskiej granicy i ochrony polskiej granicy wspólnie z naszymi przyjaciółmi ze stolic, które wymieniłem. (Oklaski) Tu duże zadanie dla kolejnego kandydata na ministra – pana Marcina Kierwińskiego. (Oklaski) Będzie sprawował urząd ministra spraw wewnętrznych i administracji. (Poseł Piotr Kaleta: Najprzystojniejszy.) Przez ostatnie dni ciężko pracowaliśmy nad sposobami zabezpieczenia sytuacji na granicy polsko-ukraińskiej w związku z protestem i blokadą. I zobaczycie państwo, że szybko znajdziemy dobre rozwiązanie tego klinczu, dobre dla wszystkich: dla naszych kierowców, dla państwa polskiego i dla Ukrainy. (Oklaski) Ministrem sprawiedliwości będzie pan prof. Adam Bodnar (Oklaski), dzisiaj senator. Nie muszę, jestem przekonany, nikomu tłumaczyć, jak ważny to będzie resort, jak wielka praca przed nami wszystkimi i przed ministrem Bodnarem, bo my musimy tu naprawdę odbudować coś, co zostało zrujnowane, czyli państwo prawa ze wszystkimi tego instytucjonalnymi aspektami. Też spędziliśmy wiele, wiele godzin z panem Adamem Bodnarem nad tym, w jaki sposób szybko i bezwzględnie przywrócić rządy prawa w Polsce. Chcę powiedzieć – usłyszałem te słowa i chcę je powtórzyć tutaj przed państwem – że będziemy szukali sprawiedliwości, będziemy egzekwować sprawiedliwość wobec tych wszystkich, którzy zgwałcili przepisy polskiego prawa, konstytucję, którzy kradli. (Poseł Antoni Macierewicz: Słusznie, konwencja chicagowska.) Słyszałem taki gwar, takie głosy także tutaj, w Sejmie, że koalicja 15 października szuka zemsty, odwetu. Słuchajcie, czy wyobrażacie sobie sytuację, że, nie wiem, sąd skazuje złodzieja, a on mówi: no jak, dlaczego skazujecie mnie, przecież to jest odwet, to jest zemsta? Chcę powiedzieć, że pan prof. Adam Bodnar zostaje ministrem sprawiedliwości m.in. dlatego, że będziemy szukali zgodnie z prawem, zgodnie z konstytucją takich sposobów działania, które bardzo szybko pokażą, że korupcja nie będzie bezkarna (Oklaski), że nadużywanie władzy nie będzie bezkarne, że niszczenie polskich instytucji nie będzie bezkarne. (Gwar na sali) (Głos z sali: Z celi do Brukseli.) Wiecie państwo, dlaczego – i to jest jeden z konkretów, które, wydawałoby się, był nie do uzyskania ze względu na sytuację ustawową, mówię tu o niezależnej prokuraturze – pan prof. Adam Bodnar dostał ode mnie propozycję objęcia funkcji ministra sprawiedliwości i prokuratora generalnego? Ponieważ nie należy do żadnej partii, ponieważ jest niezależny z natury. (Oklaski) (Głos z sali: Ha, ha, ha!) (Poseł Grzegorz Braun: Do ukraińskiej, do ukraińskiej należy.) Wy zlikwidowaliście, zlikwidowaliście niezależną prokuraturę. My ją przywracamy, mimo że ustawowo uniemożliwiliście to. I pan prof. Adam Bodnar będzie gwarantem tego, że prokuratura generalna, chociaż w rękach ministra w związku z waszą ustawą, będzie naprawdę prokuraturą niezależną (Oklaski), niezależną także od partii rządzących dzisiaj w kraju. Ale umówiliśmy się, że będzie także działała w sposób szybki i tam, gdzie to jest właściwe i uzasadnione, bezwzględnie. (Poseł Krzysztof Bosak: Z kim się umówiliście?) Pan Andrzej Domański będzie odpowiadał za państwowe finanse. (Oklaski) Jest jednym z kluczowych autorów programu 100 konkretów, pracował także nad programem całej koalicji 15 października i będzie tą personalną też gwarancją, że to wszystko, co jest tu zapisane, to wszystko, co prezentowaliśmy przed Polkami i Polakami, będzie miało także solidne zabezpieczenie finansowe, a równocześnie państwo polskie nie będzie narażone na turbulencje fiPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 669 nansowe. Z całą pewnością będziemy, nie szukając oszczędności w kieszeniach Polaków, nie robiąc niczego kosztem polskich rodzin, skutecznie zabezpieczali potrzeby finansowe państwa i, proszę być spokojnym, będziemy także utrzymywali to wszystko w ryzach elementarnej odpowiedzialności i finansowego zdrowego rozsądku. Pan Andrzej Domański jest tego gwarancją. Pani Agnieszka Buczyńska będzie odpowiadała za szeroko pojęte społeczeństwo obywatelskie. (Oklaski) W Gdańsku odpowiadała przy panu prezydencie Pawle Adamowiczu za wolontariat, za tych wszystkich ludzi dobrej woli, którzy szukali wsparcia organizacyjnego, za organizacje pozarządowe. To jest jeden z najważniejszych, konkretnych już dzisiaj nie postulatów, tylko punktów programu rządowego: to jest odbudowa tej zdrowej, przyjaznej relacji między władzą centralną a organizacjami pozarządowymi. Społeczeństwo obywatelskie wraca razem z nami, z koalicją 15 października, do rzeczywistości, do naszego życia publicznego. (Oklaski) Jestem z tego bardzo dumny. Dlatego też tymi sprawami będzie zajmowała się pani minister – członek rady ministrów. Bardzo zależy mi na tym, aby ranga organizacji pozarządowych i wolontariatu była najwyższa z możliwych. Tutaj muszę wspomnieć także o powrocie do Polski samorządnej. (Oklaski) Niszczyliście samorząd terytorialny na różne sposoby: poprzez centralizację, poprzez rozdawanie pieniędzy po uważaniu. (Głos z sali: Kłamstwo!) (Głos z sali: Kłamiesz!) Wiecie, ja mam teczkę z raportami z setek polskich gmin, dziesiątków powiatów i wielu województw o tym, jak niesprawiedliwie, jak partyjnie, jak stronniczo dysponowaliście m.in. środkami… (Oklaski) (Głos z sali:Kłamstwo!) (Głos z sali: Każda gmina dostawała pieniądze.) …jak uczyniliście wszystko, na szczęście prawie wszystko, żeby odbudować model władzy centralistycznej. W ogóle wyrzuciliście, chcieliście wyrzucić na śmietnik historii ideę prawdziwego samorządu, gdzie ludzie w swoim miejscu zamieszkania autonomicznie decydują o swoim życiu, a władza centralna jest od tego, żeby pomagać, żeby ułatwiać, a nie narzucać własną wolę. Bogu dzięki, dzisiejsza koalicja rządowa będzie dzieliła się odpowiedzialnością, środkami, decyzjami, władzą z samorządem terytorialnym każdego szczebla. (Oklaski) Pan Borys Budka będzie odpowiadał za aktywa państwowe. (Oklaski) (Poseł Piotr Kaleta: Czyli Orlen tak? Orlen to jest…) Myślę, że nie muszę tego tłumaczyć, chociaż to jest smutne, że naszą pracę, jeśli chodzi o spółki Skarbu Państwa, musi rozpocząć polityk, który był ministrem sprawiedliwości. Nie będę tego tłumaczył w szczegółach, bo nie chcę państwa deprymować. (Oklaski) Minister Borys Budka przygotowuje już w tej chwili – czytałem fragmenty – obszerny raport, na podstawie którego przeprowadzimy błyskawiczny audyt i przedstawimy obraz tego, co działo się w spółkach Skarbu Państwa. Niestety aktywa państwowe… W sumie to piękne dwa słowa: Skarb Państwa, a stały się pod waszymi rządami symbolem nepotyzmu i partyjnego rozdawnictwa. (Oklaski) Jednym z pierwszych zadań pana ministra Borysa Budki będzie przywrócenie elementarnej przyzwoitości w zarządzaniu aktywami państwowymi i koordynowaniu ich. Obiecaliśmy na Śląsku… (Głos z sali: Nie będziemy strzelać.) …że tam będzie polskie ministerstwo przemysłu. Jestem absolutnie przekonany, i powtórzę to przed Wysoką Izbą, że Śląsk – nie tylko, ale głównie Śląsk – może stać się znowu przemysłowym sercem nie tylko Polski, ale Europy, nowoczesnym, nieobarczonym złymi zaszłościami. Pani prof. Marzena Czarnecka, wybitna specjalistka m.in. od kwestii energetycznych, kobieta stamtąd, będzie odpowiedzialna za konstrukcję tego ministerstwa – tak szybko, jak to możliwe. To ministerstwo będzie koordynowało działania na rzecz Śląska, także na rzecz sprawnego wykorzystania tych funduszy w sprawiedliwej transformacji. (Poseł Iwona Ewa Arent: Co dla Warmii i Mazur?) Śląsk – także Konin i okolice, wiele miejsc w Polsce, ale przede wszystkim Śląsk – czeka na pieniądze, na decyzje, na tę nowoczesną wizję. I pani prof. Marzena Czarnecka będzie m.in. za te projekty odpowiadała. (Oklaski) Pani Agnieszka Dziemianowicz-Bąk, jeśli Wysoka Izba tak zdecyduje, będzie powołana na urząd ministra rodziny, pracy i polityki społecznej. (Oklaski) W czasie naszego spotkania – bo także z panią minister zdążyliśmy już parę ładnych godzin przepracować – prosiła o zmianę, która jest symboliczna, ale będzie miała praktyczne konsekwencje, mianowicie aby przywrócić słowo: praca w nazwie tego ministerstwa. (Głos z sali: Dokładnie.) I powiedziała zdanie, które jest bardzo bliskie memu sercu i całej koalicji 15 października: ludzie, Polki, Polacy, którzy pracują, muszą mieć dowody, że państwo szanuje przede wszystkim ich wysiłek. (Oklaski) Ludzie, którzy ciężko pracują, będą naprawdę wiedzieli, że to ma sens, że to jest kwestia ich szans na dobrobyt, kwestia finansowa, ale też godnościowa. Bardzo dziękuję pani Agnieszce Dziemianowicz-Bąk za ten na razie symboliczny, ale od jutra też praktyczny aspekt działania tego ministerstwa. Nie będę dzisiaj państwu mówił o tym, o czym mówiliśmy miesiącami, tygodniami, o czym już była mowa w nowej Izbie po wyborach, czyli o tych wszystkich kwestiach społecznych na skrzyżowaniu kilku resortów, które dotyczą praw kobiet, kwestii aborcji. Dobrze wiemy i nie ukrywamy tego, że wiele spraw będzie jeszcze przedmiotem debaty. Będziemy uczciwie rozmawiać o tym, jak przywrócić… Pani minister Dziemianowicz-Bąk, ale także inne panie ministry, o których za chwilę powiem, będą współpracoPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 670 wały, żeby niezależnie od tego, co ustawowo będzie możliwe – bo wiemy dobrze, w jakich realiach politycznych jesteśmy, a opracowaliśmy już wstępny program – każda polska kobieta natychmiast odczuła zasadniczą różnicę, także w kwestii traktowania macierzyństwa, także w kwestii rozumienia kobiet w ciąży, przyszłych matek i tego bardzo bolesnego dzisiaj w Polsce problemu, jakim jest prawo do legalnej i bezpiecznej aborcji w sytuacji, która tego wymaga. (Poseł Grzegorz Braun: Dla kogo bezpiecznej?) Chcę państwu powiedzieć, że niezależnie od sporów politycznych, które będą obecne w tej Izbie, które będą dotyczyły tych kwestii, od pierwszego dnia przystąpimy do konkretnych, precyzyjnych działań. (Poseł Krzysztof Bosak: Prawo do życia.) (Poseł Grzegorz Braun: Dzieciobójcy.) Niezależnie od tego, czy to będzie prokuratura, czy to będzie szpital, czy to będzie szkoła, przystąpimy do działań, dzięki którym kobiety natychmiast odczują radykalną poprawę, jeśli chodzi o ich prawa, o ich godność, o ich zdrowie, o ich bezpieczeństwo. (Oklaski) (Poseł Krzysztof Bosak: Co z kobietami, które są pro-life?) Wszystkie polskie kobiety niezależnie od własnych poglądów na te sprawy odczują poprawę, wszystkie. (Głos z sali: A dzieci?) Nie, słuchajcie, kochani, chcecie mi mówić o dzieciach, jak się opiekować dziećmi czy wnukami? (Głos z sali: Ha, ha, ha!) Jeśli będziecie chcieli się czegoś dowiedzieć, to służę własnym doświadczeniem. (Oklaski) (Poseł Grzegorz Braun: Trzymajcie się z dala od naszych dzieci.) Pan Jan Grabiec będzie kierował pracami kancelarii. (Oklaski) To jeden z moich najbliższych współpracowników. Zadba o to, żeby nasze działania były sprawnie koordynowane, żebyśmy nie musieli się już nigdy więcej wstydzić za legislacyjne niechlujstwo, za zły obieg dokumentów. (Poseł Antoni Macierewicz: Wstydzicie się, tak? To dobrze.) No tak, panie pośle, przez ostatnie lata wszyscy mieliśmy bardzo dużo powodów do wstydu za to, jak pracuje administracja państwowa pod rządami PiS-u. (Oklaski) Rolą pana ministra Grabca będzie naprawa tej sytuacji. (Poseł Antoni Macierewicz: To my się wstydzimy za wasze działania.) A teraz przedstawię państwa ulubienicę, panią minister Paulinę Hennig-Kloskę. (Oklaski) Będzie prowadziła prace Ministerstwa Klimatu i Środowiska. Przeszła już bardzo poważny test, więc możecie się państwo spodziewać, sprawdziliście to już w boju, że jest bardzo dzielną kobietą, odporną na ataki, kompetentną. (Gwar na sali) (Głos z sali: Dla lobbystów…) (Głos z sali: Niemcy sprawdzili.) (Głos z sali: Uuu…) Ci wszyscy, którzy czekają dzisiaj w Polsce na odnawialne źródła energii, na wiatraki, tak, na ochronę środowiska, ci wszyscy, którzy czekają… (Głos z sali: Na jarmarkach.) (Poseł Piotr Kaleta: A co ma Kloska do wiatraka?)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Przepraszam bardzo, panie premierze. Niektórzy z państwa reagują na słowo: wiatraki tak jak pewien literacki bohater, który miał dużo do czynienia z wiatrakami. (Głos z sali: Ooo…) Wiatraki są w Polsce potrzebne. Dajcie premierowi spokojnie skończyć wypowiedź, dobrze? Panie pośle Dolata, cenię pańskie poczucie humoru, ale bardzo proszę o to, żebyśmy w spokoju wysłuchali tego wystąpienia. Dziękuję.",
                },
                {
                    "speaker": "Prezes Rady Ministrów Donald Tusk",
                    "content": "Nie muszę chyba nikogo przekonywać, użyłem już tego terminu: stajnia Augiasza, że w ochronie środowiska mamy tu prawie dosłownie do czynienia z czymś takim. Polska nie będzie śmietniskiem Europy. (Oklaski) (Głos z sali: Ooo…) Nie będzie więcej tych hańbiących obrazów, tych nieustannie płonących legalnych czy nielegalnych wysypisk, składowisk. Ten czarny obraz, ten tragiczny obraz zatrutej Odry, ten dramatyczny obraz lasów, które znikały na naszych oczach, jakby całe wyrąbane knieje wyjeżdżały do Chin – to się skończyło. (Głos z sali: Ty jesteś za to odpowiedzialny.) Skończyła się ta partyjna prywatyzacja Lasów Państwowych. (Oklaski) Straszyliście Polaków prywatyzacją Lasów Państwowych. Cała Polska zobaczyła, co zrobiliście. To jest jedno z naszych największych dóbr, przecież nie chodzi o jakieś ideologiczne konstrukcje. Słuchajcie, przecież to jest nasze święte dobro. Wiecie, przecież dobrze wiecie, że współczesne wojny będą się toczyły m.in. o dostęp do wody. Być może nie ma dzisiaj bardziej wartościowego zasobu, bardziej strategicznego zasobu niż czysta woda. Mówimy tu i o retencji, i o problemie zatrutych polskich rzek. Lasy, środowisko naturalne – przecież to są rzeczy, z których chcemy być dumni. Chcę, żeby polskie rodziny, Polki i Polacy znowu zobaczyli, jak wygląda prawdziwy las. Las to nie jest gospodarka drewnem. (Oklaski) (Głos z sali: Ha, ha, ha!) Las to nasz święty zasób narodowy. Będziemy go znowu chronić tak, jak na to zasługuje. Będziemy mieli okazję współpracować z tymi wszystkimi leśnikami, to przygniatająca większość, strażnikami ochrony przyrody, którzy pracowali w parkach narodowych. To jest cała rzesza ludzi, którzy kochają lasy Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 671 i rozumieją mądrą gospodarkę leśną. Zobaczycie, że to jest możliwe. Nie będzie już tak, że polski przedsiębiorca kupuje drewno w Niemczech, w Austrii, w Szwecji, bo polskie drewno z bliżej nieznanych powodów wyjeżdża hurtowo do Chin. Polski przedsiębiorca zobaczy, że można chronić lasy, a równocześnie polskie drewno może być dostępne na rynku i może być tańsze niż szwedzkie. Nie wiem, jak wam się to udało, to jest cud na ziemi, ale wyrąbaliście najwięcej drzew w historii, a polskie drewno jest najdroższe w historii. Jak to jest możliwe? (Poseł Anna Kwiecień: I mamy najwięcej lasów.) Nie tylko wyrżnęliście polskie lasy, ale także niemalże zarżnęliście dumę polskiego przemysłu, jaką był polski przemysł wykorzystujący drewno. Bardzo się cieszę, że będziemy współpracowali z panią Pauliną Hennig-Kloską także w tej sprawie. (Oklaski) Ministerstwo Rozwoju i Technologii – pan Krzysztof Hetman. (Oklaski) Znamy się wiele lat. Jest dla mnie rzeczą niezwykle ważną, że potrafi łączyć w sobie kompetencje właściwe nie tylko dla tego resortu – kiedyś był to w jakiejś części resort gospodarki – ale też jest politykiem, który rozumie znaczenie funduszy europejskich, który umie, jak mało kto w Polsce, jak mało kto w Europie, pracować nad rozsądnym, najbardziej efektywnym zdobywaniem środków europejskich i dysponowaniem nimi na rzecz polskiej gospodarki. Mieliśmy już okazję rozmawiać o tym, co musimy zrobić w pierwszych dniach, także jeśli chodzi o promocję polskiego eksportu, jak odbudować służby – nie tak jak ta zabawa w Brukseli za grube miliony założona przez was – jak naprawdę zbudować profesjonalne służby, które będą promowały polską produkcję na całym świecie. Bardzo się cieszę, panie Krzysztofie, że będziemy mogli dzielić się tutaj własnymi kompetencjami. Pan Dariusz Klimczak, urząd ministra infrastruktury. (Oklaski) Od wielu dni pracuje już nasz zespół, który powołaliśmy ad hoc w celu rozwiązania kryzysu na przejściach granicznych z Ukrainą. Rozmawialiśmy także o przyszłości CPK. Chcę państwu powiedzieć, że żadna inwestycja w Polsce nie będzie inwestycją, która doprowadza do tragedii, która doprowadza do rozpaczy polskie rodziny. (Oklaski) Chcę zapewnić jeszcze raz tych wszystkich, którzy czuli się terroryzowani przez ostatnie miesiące… Byłem w tych miejscach. Nie wiem, dlaczego się uśmiechacie. Pojedźcie do nich. Byłem u nich. Oni płakali. Nie rozumiem waszych uśmiechów w tej sprawie. Wiecie, co dzisiaj czują ludzie, którzy od wielu, wielu miesięcy słyszą, że może zostaną wywłaszczeni, a jak im się nie podoba, to może zostaną wywłaszczeni przemocą? Policja przyjeżdża i demonstruje siłę. (Głos z sali: Wiatraki.) Słuchajcie, to są dziesiątki, setki opowieści ludzi z różnych miejsc w kraju. Odwiedziłem setki miejscowości przez te 2 lata. Prawie wszędzie, gdzie byłem w Polsce, spotykałem ludzi ze łzami w oczach mówiących: Oni chcą nas wywłaszczyć. Nie mówią kiedy, nie mówią za ile, nie mówią tak naprawdę po co. To się skończy, w ogóle o tym zapomnijcie. O tym też mówiłem wiele razy, spotykając się z ludźmi. Myśmy naprawdę zrobili największy plac budowy w Polsce. Inwestycje, kiedy byłem premierem, to były największe inwestycje w historii Polski i w historii Europy. (Wesołość na sali, oklaski) Możecie krzyczeć. Słuchajcie, mijam czasami na autostradach i drogach szybkiego ruchu wasze kolumny na kogutach. Jeździcie tam dlatego, że udało nam się zbudować te autostrady i te drogi szybkiego ruchu. (Oklaski) (Poseł Sławomir Nitras: Lotniska, stadiony.) I stadiony, i modernizacja linii kolejowych. Czy słyszeliście chociaż o jednym proteście wywłaszczonych? (Głosy z sali: Tak!) Tak? A ja nie. A byłem premierem i – wyobraźcie sobie – podejmowałem decyzje w tej kwestii. Nie było protestów. (Oklaski) Wszyscy otrzymali należną satysfakcję. (Gwar na sali, dzwonek) Chcę wam powiedzieć, że niezależnie od tego, jakie decyzje inwestycyjne podejmiemy, ludzie w Polsce nie będą z tego powodu więcej płakać. Przyszłość CPK rozstrzygnie się w sposób transparentny. Pan minister Klimczak, a także pełnomocnik rządu do spraw CPK w sposób otwarty, czytelny, bez jakichś dziwnych sytuacji, które od samego początku towarzyszą temu projektowi, na oczach wszystkich Polek i Polaków zdecydują o tym, jaka będzie przyszłość CPK. Będą uczestniczyli w tym procesie wybitni i bezstronni eksperci. To projekt, który w sposób najbardziej racjonalny będzie służył Polsce, nie chorym ambicjom jakiegoś polityka, który chciał sobie zbudować kolejny pomnik, tylko Polsce, Polkom i Polakom – tak jak im służą i będą służyły w przyszłości polskie regionalne lotniska, które budowaliśmy tak intensywnie i które dzisiaj pozwalają Polkom i Polakom latać ze swojego miasta wszędzie, na cały świat. (Oklaski) (Poseł Antoni Macierewicz: No oczywiście w Berlinie jest właściwe lotnisko.) Prawa kobiet i równość to rzeczy, które wymagają dzisiaj ministry, ministra – każdy mówi, jak chce, u nas nie ma tu dogmatu. Ministrą w tej przestrzeni będzie pani Katarzyna Kotula. (Oklaski) Długo o tym rozmawialiśmy. Chcę wam powiedzieć, że jej energia, jej empatia, jej doświadczenie osobiste, życiowe mówią mi, że będziemy mieli, szczególnie… Nie tylko polskie kobiety, bo mówimy tu o równości, a deficyt równości dotyczył wielu, wielu grup społecznych w Polsce. Ten deficyt równości będziemy wspólnie z panią ministrą eliminować. Chcę państwu powiedzieć, że nie ma przypadku w tym, że będzie ministrą konstytucyjną (Oklaski), bo nie ma dla mnie ważniejszej sprawy niż prawa kobiet i równość obywateli wobec prawa, równość obywateli niezależnie od ich statusu społecznego, wyznania, orientacji seksualnej etc. Pani Izabela Leszczyna będzie sprawowała urząd ministra zdrowia. (Oklaski) Wiecie państwo, moje Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 672 doświadczenie, nie tylko moje, mówi, że kluczową sprawą w skutecznej ochronie zdrowia jest oczywiście mądre, zdecydowane dysponowanie finansami publicznymi. Wielu z was sądziło, że przyszła pani minister Izabela Leszczyna będzie odpowiedzialna za finanse. Ale jak państwo wiecie, finanse, pieniądze publiczne, które są i będą w jeszcze większym stopniu zaangażowane w ochronę zdrowia, są jak budżet średniego państwa w Europie i wymagają nadzwyczajnych kompetencji, ale też empatii i zrozumienia. Nikt lepiej się do tej trudnej przecież roli, niektórzy uważali, że straceńczej… A ja wam powiem, że kiedy pani poseł Izabela Leszczyna powiedziała: tak, biorę to na swoje barki, od razu wiedziałem, że to nie jest misja straceńcza i że dzięki pani poseł Leszczynie damy radę. (Oklaski) Ludzie w Polsce zobaczą, że można naprawdę mądrze, skutecznie wykorzystywać te gigantyczne środki finansowe, jakie powinny służyć skutecznie ochronie zdrowia i wszystkim pacjentkom i pacjentom. Pani Barbara Nowacka będzie pełniła funkcję ministra, ministry edukacji. (Oklaski) Tak, w programie koalicji rządowej i także w 100 konkretach znajdziecie… Nie będę państwa zanudzał odczytywaniem wszystkich projektów, które będą wdrażane od pierwszego dnia przez panią minister Nowacką. Powiem szczerze, że tak naprawdę wystarczy chyba zamknąć na chwilę oczy i przypomnieć sobie: pan minister Czarnek, pani minister Nowacka. I chyba wszystko jasne, prawda? (Oklaski) (Głos z sali: Ha, ha, ha!) Tutaj miła niespodzianka dla tej części sali. Ministrem sportu będzie pan poseł Sławomir Nitras. (Oklaski) (Poseł Piotr Kaleta: Walka z dopingiem. Gruba kreska.) Też trudne zadanie. Słyszeliśmy o ambitnym planie promowania idei igrzysk olimpijskich w Polsce. Pomysł bardzo ambitny, muszę powiedzieć, taki bardzo perspektywiczny. Nie będziemy w tej kwestii marudzić, panie pośle, prawda? Będziemy realnie i intensywnie oceniać nasze szanse, możliwości. Kto wie? Być może doczekamy. Nie za pańskiej kadencji i na pewno nie za mojej, ale niewykluczone, że także te marzenia się spełnią. Chociaż przyszły minister pan Nitras będzie miał jedno oczywiste zadanie przed sobą – rewitalizację tego sportu podstawowego. (Oklaski) Trochę zmarnowaliście ten kapitalny system orlików. Pan minister Sławomir Nitras i jego ekipa odbudują to wszystko, co zostało zmarnowane. I zobaczycie, że nasze dzieci, dziewczyny, chłopcy ze szkół podstawowych, ze szkół średnich, znowu dziesiątkami tysięcy będą uczestniczyły w turniejach piłkarskich, w innych zawodach sportowych w każdej polskiej gminie. Znowu zapali się to światło wieczorem i nawet późnym wieczorem nasze dzieciaki będą mogły uprawiać sport. (Oklaski) Panie Ministrze! Duże wyzwanie. (Gwar na sali)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Szanowni państwo, to jest minister sportu, a to nie jest Żyleta, panie pośle Ozdoba i panie pośle Matecki. (Głos z sali: Ha, ha, ha!) Będziemy budowali stadiony, tam będzie dla was dużo miejsca. Teraz jesteśmy w Sejmie. Rozumiem ekscytację, każdy kocha i ceni pana posła Nitrasa. Ale to później, dobrze? Trochę spokojniej. Dziękuję bardzo. Panie pośle Ozdoba, widzę, że pan się męczy, ale może by pan nas nie męczył. Dziękuję.",
                },
                {
                    "speaker": "Prezes Rady Ministrów Donald Tusk",
                    "content": "Panie marszałku, nie wydaje mi się, aby pan minister Ozdoba kiedykolwiek zaryzykował pójście na Żyletę, szczerze powiedziawszy. (Wesołość na sali, oklaski) (Głos z sali: Pan się wybierze?) Ja się nie wybieram, nie, nie. Pani Marzena Okła-Drewnowicz będzie odpowiadała za politykę senioralną. Będziemy budowali w Polsce system. Jestem przekonany – na podstawie materiałów, jakie razem studiowaliśmy w ostatnich dniach – że zbudujemy najnowocześniejszy, najambitniejszy system opieki, aktywnej opieki nad naszymi seniorami w Europie. (Oklaski) Jesteśmy do tego gotowi. Będziemy pracowali interdyscyplinarnie z innymi resortami. Dla mnie główną gwarancją jest to, co do tej pory w tej sprawie robiła. Podkreślam to naprawdę kapitalne skrzyżowanie kompetencji i empatii pani poseł. Jestem dumny, że będziemy w tej sprawie razem współpracowali. I będzie to z korzyścią dla wszystkich, także dla polskiej gospodarki. To jest bardzo wielowymiarowy projekt. Jego symbolem będzie bon senioralny, ale tak naprawdę jest to niezwykle przemyślana, nowoczesna, kapitalna idea. Nasi seniorzy i seniorki bardzo szybko odczują naprawdę radykalną poprawę, jeśli chodzi o ten stosunek państwa do ludzi starszych w Polsce. Pani Katarzyna Pełczyńska-Nałęcz (Oklaski) będzie ministrą funduszy i polityki regionalnej. Nie mogę na nią spojrzeć, bo nie jest posłanką. Jest pani minister? A, jest. (Oklaski) Jestem naprawdę bardzo usatysfakcjonowany, że będziemy razem pracowali w sprawach funduszy i polityki regionalnej. Poznaliśmy się dobrze, kiedy razem pracowaliśmy w moim rządzie. Pani minister ma wiele kompetencji. Jej doświadczenie międzynarodowe w zarządzaniu tym urzędem także będzie bardzo przydatne. Wiem od pana marszałka Szymona Hołowni, jak długą drogę pani ministra przeszła i jak bardzo kompetentna jest także w tych kwestiach, za które będzie odpowiadała w Ministerstwie Funduszy i Polityki Regionalnej. To będzie naprawdę bardzo silny element tego nowego rządu Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 673 Pan Czesław Siekierski – nie muszę nikomu przedstawiać – przyszły minister rolnictwa. (Oklaski) Mogę powiedzieć, że w jakimś sensie jest kwintesencją polskiego ruchu ludowego, to człowiek doświadczony, a ciągle pełen energii. Jestem przekonany, że naprawdę polskie rolnictwo będzie miało w osobie pana ministra kogoś bardzo kompetentnego. Do pomocy, panie ministrze, będzie pan miał w swoim ministerstwie Michała Kołodziejczaka. (Poruszenie na sali, oklaski) (Głos z sali: Ooo…) To będzie… Dziękuję za słowa uznania ze strony koleżanek i kolegów z PiS-u. Już państwo chyba widzicie oczami wyobraźni tę nadzwyczajną synergię. (Oklaski) (Głos z sali: Tak.) To jest naprawdę bardzo obiecujący duet. Z całą pewnością polscy rolnicy, mieszkanki i mieszkańcy polskiej wsi, ale przede wszystkim rolniczki i rolnicy zobaczą, co to naprawdę znaczy… (Głos z sali: Oj, zobaczą.) …twarda, kompetentna, zdecydowana walka o ich interesy. (Oklaski) I nie ma w tym przypadku. Pan poseł Kołodziejczak był pierwszym, który podniósł krzyk, kiedy przez waszą nieudolność polscy rolnicy zamarli ze strachu, kiedy zaczęła się wlewać ta niekontrolowana fala produktów z Ukrainy. Nie ma sensu obwiniać za to Ukraińców, bo to wy odpowiadacie za to. (Oklaski) Gdyby tam byli Siekierski i Kołodziejczak, nie byłoby tych dziwnych, naprawdę czasami bardzo podejrzanych sytuacji na naszej granicy. Te złote żniwa dla niektórych, którzy pod waszym protektoratem dorobili się na tym, właśnie się kończą. (Oklaski) Mój bliski współpracownik, były wicepremier, minister obrony narodowej w poprzednim moim rządzie będzie koordynował służby specjalne w Polsce – pan Tomasz Siemoniak. (Oklaski) Jak patrzę tutaj na osoby, które odpowiadały za służby specjalne w Polsce w ostatnich latach, to mogę powiedzieć, że bardzo się cieszę, że będę współpracował z człowiekiem odpowiedzialnym, racjonalnym, poważnym… (Poseł Antoni Macierewicz: Kompetentnym.) …kompetentnym… (Poseł Antoni Macierewicz: Bardzo, niesłychanie.) …patriotą – tak jest – powiem jednym słowem: normalnym. (Oklaski) (Głos z sali: Ha, ha, ha!) To jest naprawdę dla mnie… Bardzo, bardzo, bardzo się cieszę, panie premierze, że będziemy znowu współpracowali w jednym rządzie. Wiemy dobrze, ile pan ma tam roboty przed sobą. Nieprzypadkowo umówiliśmy się z panem prezydentem Andrzejem Dudą, że jutrzejsze zaprzysiężenie odbędzie się wcześnie, też po to, abym przed wyjazdem do Brukseli zdążył jeszcze nie tylko z ministrami udać się do naszych nowych miejsc pracy, ale także porozmawiać w gronie Kolegium do Spraw Służb Specjalnych o decyzjach, które chcemy podjąć i podejmiemy natychmiast. (Oklaski) Natura tych spraw wymaga dyskrecji, ale spodziewajcie się państwo decyzji masywnych, szybkich i jednoznacznych. Pan minister Bartłomiej Sienkiewicz będzie kierował Ministerstwem Kultury i Dziedzictwa Narodowego. (Oklaski) (Poseł Piotr Kaleta: A kto do pomocy?) Wiecie co? Tak szczerze powiedziawszy, pewnie nie musiałbym tłumaczyć, dlaczego od dziedzictwa narodowego będzie prawnuk Henryka Sienkiewicza, ale przecież nie ta koligacja decyduje o tym, że pan minister Bartłomiej Sienkiewicz będzie zajmował się porządkami. Tak nam wszystkim niestety to się w Polsce kojarzy – to, co się działo, szczególnie w ostatnich czasach, z publicznymi pieniędzmi, które miały trafiać do polskiej kultury – że tak naprawdę mieliśmy do czynienia z ministerstwem antykultury. Jestem pewny, że pan Bartłomiej Sienkiewicz, nie tylko z racji tego, że jest autorem książek… (Głos z sali: Spalonej budki.) …jest człowiekiem kultury. (Poruszenie na sali) Ale ma też doświadczenie, jeśli chodzi o decyzje najtwardsze. I dobrze państwo wiecie, że lepszego człowieka na uporządkowanie sytuacji… (Głos z sali: Nie macie.) …m.in. w sferze mediów publicznych (Oklaski), mediów publicznych, które zniszczyliście… Będzie odpowiedzialny za przywrócenie tych mediów Polkom i Polakom. Bardzo szybko okaże się, że media publiczne służące Polkom i Polakom to nie jest jakiś miraż, to nie jest coś niemożliwego. Tak jak zobaczycie, że wymiar sprawiedliwości może być neutralny, nie partyjny, służący Polsce, a nie partii rządzącej, tak zobaczycie, i pewnie oczom nie uwierzycie, że telewizja publiczna może służyć Polsce, a nie partii rządzącej. (Oklaski) I tak będzie. (Głos z sali: Tak jak TVN?) W sprawach polityki europejskiej pomagać będzie mi minister do spraw Unii Europejskiej pan Adam Szłapka. (Oklaski) (Głos z sali: Chełmoński.) Lider Nowoczesnej i, wydaje mi się, że nie powiem niczego zaskakującego, człowiek naprawdę nowoczesny. My dzisiaj potrzebujemy Polski nowoczesnej, Polski, która będzie imponowała (Gwar na sali, dzwonek) całej Europie nowoczesnością, i pan Adam Szłapka podjął się zadania. To niełatwe zadanie pracować ze mną w sprawach europejskich, ale nie będę się wymądrzał, panie ministrze, będziemy wspólnie duetem, który ciężko będzie pracował nad naszymi interesami w Unii Europejskiej. (Oklaski) Członkiem Rady Ministrów będzie także pan Maciej Berek, odpowiedzialny za cały proces legislacji, osoba niezwykle doświadczona, chociaż ciągle młoda. (Oklaski) Też nie jest posłem, więc nie widzę go tutaj na sali, ale pewnie jest, tak, jest, na galerii. Miałem okazję i zaszczyt pracować z ówczesnym panem ministrem Berkiem i muszę powiedzieć, że jest w Polsce jednym z najwybitniejszych specjalistów też od czyPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 674 stości i transparentności procesu legislacyjnego. Mogę państwu to przyrzec, że inicjatywy legislacyjne polskiego rządu od dnia, w którym zaczniemy sprawować nasze urzędy, to będą procesy przejrzyste do bólu, logiczne, racjonalne, także dzięki doświadczeniu i kompetencjom pana ministra Macieja Berka. (Oklaski) Wiem, że to exposé jest nietypowe, tak jak nietypowa jest sytuacja, w której się znaleźliśmy. Jak wiecie, to jest pierwszy raz w historii polskiego parlamentu, kiedy to Sejm desygnował kandydata na premiera rządu. Jutro, jak sądzę, dzięki decyzji tej Izby będę miał zaszczyt ślubować przed panem prezydentem rotę ślubowania… (Wypowiedź poza mikrofonem) O, dziękuję, rzeczywiście. Nie wiem, co się stało… (Głos z sali: Ooo…) (Głos z sali: Już wpadka.) Już wiem, co się stało. Tak jest, oczywiście, wpadka. Pan minister Dariusz Wieczorek. (Oklaski) Panie Ministrze! Przez tę moją drobną wpadkę wszyscy na tej sali bardziej zapamiętają tę prezentację (Oklaski), więc proszę to potraktować jako niewymuszony przywilej. Stanie pan na czele urzędu ministra nauki. Jak państwo wiecie, to było oczekiwanie… Długo się nad tym zastanawiałem, bo nie było moją intencją tworzenie nowych ministerstw, ale tutaj sygnały były absolutnie jednoznaczne i płynęły z obu środowisk, tj. i edukacji, i ze strony środowisk akademickich, że te dwie części do siebie w codziennej praktyce rządzenia nie przystają. I dlatego zdecydowaliśmy się na odtworzenie Ministerstwa Nauki i Szkolnictwa Wyższego. Pan Dariusz Wieczorek będzie tę funkcję sprawował. Wiem, że dobrał sobie także znakomitych współpracowników. Myślę, że będziemy świadkami nie tylko szybkiej rekonstrukcji tego ministerstwa. Jedną z pierwszych decyzji, wracam do konkretów, będzie oczywiście także podwyżka płac, jeśli chodzi o nauczycieli akademickich (Oklaski), również na to długo czekali, też jesteśmy już z tym gotowi, analogicznie do podwyżki płac dla nauczycieli. W ogóle to jest taki fajny dzień, kiedy mogę powiedzieć… Mówiliśmy o podwyżkach dla nauczycieli, o tej 30-procentowej, i ktoś mógł pomyśleć, że nauczyciele przedszkolni, przepraszam za kolokwializm, się nie załapią. Ta podwyżka dotyczy też polskich przedszkoli (Oklaski) i jakby z drugiej strony, gdy patrzeć na wiek – także nauczycieli akademickich. Panie Ministrze! To znaczy na razie: Panie Pośle! Jestem pewien, że będzie pan też tego pilnował. (Poseł Piotr Kaleta: Jeszcze Ryśkowi jakieś ministerstwo. Spraw zbytecznych.) To nietypowe exposé wynika z nietypowej sytuacji i bezprecedensowej sytuacji. Chciałem jeszcze raz Wysokiej Izbie podziękować za wczorajszy wybór. Konstytucja właściwie nie przewiduje exposé ministra wybranego w tym drugim kroku. Bardzo zależało mi na tempie. Wiecie dlaczego. Wiecie, jak ważne są dni i godziny. Prawdopodobnie zobaczymy się w Brukseli z prezydentem Zełeńskim. Ukraina liczy dzisiaj godziny i dni, bo czeka na kolejne wsparcie. (Głos z sali: Wreszcie.) Polska czeka na miliardy funduszy europejskich. (Głos z sali: Na wiatraki.) Polska też czeka na szybkie sygnały o współpracy z innymi państwami graniczącymi z Rosją, bo moją ambicją jest poprowadzenie w imieniu Polski polityki europejskiej na rzecz ochrony granicy. Granic ze wszystkich stron Europy, tak aby zagrożenie nielegalną migracją nie było tak dotkliwe jak w tej chwili. To nietypowe exposé chciałbym zakończyć czymś, co jest też nietypowe w naszej historii. I to jest już ostatni akcent. Jest to coś niebywałego, być może państwo wczoraj przeczytali tę skromną PAP-owską notatkę. To jest kilkuzdaniowy raport z ostatnich badań CBOS-u, rządowej, więc w jakimś sensie wciąż w dyspozycji ustępującej władzy, pracowni badań społecznych. CBOS wczoraj opublikował raport z badań sprzed kilku dni. Najwięcej Polaków w 30-letniej historii badań CBOS… 30-letniej, bo dokładnie od 1992 r. to badanie jest prowadzone. Najwięcej Polaków uważa, że zwykli ludzie mają wpływ na sprawy kraju. Sądzi tak teraz, po wyborach 15 października… Sądzi tak teraz, po wyborach 15… (Gwar na sali) Zaraz powiem coś o waszych rządach, bo CBOS o tym też mówi. (Oklaski) (Głos z sali: Ha, ha, ha!) Jakbyście państwo dali mi dokończyć tylko to jedno zdanie, to od razu by się wyjaśniło, co było za waszych rządów, więc powtórzę: sądzi tak teraz, po 15 października, 54% obywateli. (Oklaski) (Głos z sali: 120%.) A w poprzednim badaniu, z lutego 2020 r… Kto rządził? Przypomnijcie. (Głos z sali: PiS.) Takie poczucie wpływu miało 26% obywateli. (Oklaski) (Głos z sali: Brawo!) (Głos z sali: Ha, ha, ha!) Chcę państwu powiedzieć, że 2 lata temu narodził się ruch 15 października. (Poruszenie na sali) Tak, 2 lata temu, 2 lata temu. I wystarczyły 2 lata, nastąpił 15 października i ilość obywateli, którzy poczuli, że mają wpływ na losy swojej ojczyzny, zbadanych przez waszą pracownię – waszą pracownię – wzrosła z 26% do 54%. (Poseł Joanna Lichocka: Po naszych rządach.) Rozumiecie? Dwa razy więcej, dwa razy więcej w ciągu tak krótkiego czasu. (Oklaski) (Głos z sali: Brawo!) (Głos z sali: Są inne sondaże.) Czytam dalej raport CBOS-u: Brak wpływu na sprawy kraju deklaruje obecnie 41%, a poprzednio, w 2022 r. – 71% Polaków. Komentarz pracowni: Ostatnie wybory nie tylko przyciągnęły do urn rekordową rzeszę głosujących, ale umocniły, a właściwie na nowo ukonstytuowały w Polakach poczucie Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 675 obywatelskiej podmiotowości (Oklaski), czyli przekonanie o sile pojedynczego głosu i możliwości wpływania na rzeczywistość polityczną za pośrednictwem aktu wyborczego. (Głos z sali: Niedługo się przekonają.) Zmiana w opiniach Polaków jest rewolucyjna, bowiem do tej pory, odkąd prowadzono to badanie, czyli od 1992 r., wśród Polaków w mniejszym lub większym stopniu dominowało przekonanie, że zwykli obywatele nie mają żadnego realnego wpływu na ogólnokrajową politykę. Po 15 października większość Polaków, nawet nie odzyskało, tyko po raz pierwszy uwierzyło, że ma realny wpływ na losy swojej, naszej ojczyzny. (Oklaski) Kochani, nie zmarnujmy tego, to jest dla nas wielkie zobowiązanie. Nie będzie to exposé, ale będę składał Polkom i Polakom takie sprawozdania od serca każdego miesiąca. Wiecie, że jednym z elementów tego odrodzenia wiary we własną sprawczość wśród Polek i Polaków były te spotkania: 4 czerwca – 0,5 mln i 1 października – 1 mln ludzi na ulicach Warszawy. (Głos z sali: Jaki milion?) Tysiące, tysiące ludzi na spotkaniach, w których miałem przywilej, honor uczestniczyć. (Oklaski) (Poseł Marek Suski: Milion to było gwiazdek.) To jest też zobowiązanie. I chciałbym tutaj się zobowiązać, że każdego miesiąca gdzieś w Polsce w sposób otwarty, publiczny, czy przyjdzie 10 tys. ludzi, czy pięć osób, znajdę na to czas, aby wyspowiadać się w imieniu mojego rządu z tego, co zrobiliśmy, z tego, co się udało (Oklaski), gdzie jest kłopot. Uczciwie i prawdziwie będziemy każdego miesiąca takie sprawozdawcze exposé Polakom składali. Bo nie możemy, nie mamy prawa zmarnować tego wielkiego odrodzenia, bo 15 października nastąpiło wielkie Polaków odrodzenie. Szczęśliwej Polski już czas. Dziękuję. (Oklaski) (Część posłów wstaje i skanduje: Donald Tusk! Donald Tusk! Donald Tusk!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie premierze. W nawiązaniu do tego, co pan mówił, że coś się w Polsce zmieniło, chciałbym powiedzieć, że wczorajsze obrady Sejmu w Internecie oglądało ponad 4 mln obywateli. (Oklaski) To jest realna zmiana, drodzy państwo. Ludzie naprawdę interesują się demokracją i tym, co tutaj robimy, patrzą nam na ręce, chcą wiedzieć więcej. Chciałbym z tego miejsca serdecznie pozdrowić wszystkich tych, którzy dzisiaj oglądają naszą pracę tutaj, w tej Izbie. Nagrodźmy ich gorącymi oklaskami, ich wszystkich, niezależnie od tego, jakie mają poglądy. (Oklaski) Społeczeństwo obywatelskie odradza się na naszych oczach, a parlament rządzi się swoimi prawami. Sejm ustalił, że w dyskusji nad tym punktem porządku dziennego wysłucha 10-minutowych oświadczeń w imieniu klubów i 5-minutowego oświadczania w imieniu koła. Otwieram dyskusję klubową. Jako pierwszy głos zabierze w imieniu Klubu Parlamentarnego Prawo i Sprawiedliwości pan poseł Mariusz Błaszczak. (Oklaski) Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Mariusz Błaszczak",
                    "content": "Panie Marszałku! Wysoki Sejmie! Przed chwilą usłyszeliśmy bardzo ostre przemówienie… (Głos z sali: Ooo…) …w którym podtrzymane zostały wszystkie te kłamstwa głoszone z tej strony sali przez lata. Zaś wykorzystywanie listu samobójcy, by uzasadnić swoją politykę, to najpodlejsze, co można zrobić. (Oklaski) Wynoszenie aktu samobójstwa popełnionego w takich okolicznościach do czynu bohaterskiego to najniższe zagranie, jakie można sobie wyobrazić. Mówiłem o tym wczoraj. Pan nie ma skrupułów, ale też jest pan nieuczciwy, bo gdyby pan miał odrobinę uczciwości w sobie, to zacytowałby pan list, jaki napisał do pana człowiek, który podpalił się przed kancelarią w 2011 r., kiedy pan był premierem. (Oklaski) Przypomnę Wysokiej Izbie treść tego listu: Szanowny Panie Premierze! Piszę do pana już po raz kolejny, jako obywatel tego „chorego kraju”, jako ojciec trójki małoletnich dzieci, któremu pan i pana urzędnicy zniszczyli całe dotychczasowe życie. Piszę do pana już po raz ostatni, gdyż nie wierzę, że odniesie to jakikolwiek skutek. Chcę jednak, aby pan wiedział, że liczyłem na to, że nie jest pan kłamcą i hipokrytą, ale normalnym człowiekiem szanującym prawo, a przede wszystkim ojcem kochającym swoją rodzinę. Widzę jednak, że rządza władzy zniszczyła w panu wszelkie wartości i ludzkie cechy, którymi tak się pan chwalił w trakcie kolejnych kampanii wyborczych. To jest fragment listu, który zostawił obywatel Rzeczypospolitej Polskiej panu przed aktem samospalenia w 2011 r. (Poruszenie na sali) To pan nakręcił spiralę nienawiści. Przypomnę moherowe berety. To pan wyhodował Palikota, symbol hejtu i pogardy. Mogę jeszcze wymieniać tu wiele, wiele innych przykładów właśnie takiego postępowania, niegodnego postępowania. (Oklaski) Miłosierdzie niech pan zostawi Bogu. Sam pan głosi nienawiść i okrucieństwo. (Poseł Krystyna Skowrońska: Błaszczak, przestań.) Wysoki Sejmie! Ileż to nasłuchaliśmy się w ostatnich miesiącach o polityce miłości, o uśmiechniętej, przyjaznej Polsce, którą gwarantuje koalicja właśnie czego? Koalicja zemsty i chaosu albo koalicja 13 grudnia. Wpięliście sobie w klapy marynarek serca i udajecie piewców pokoju. Mowa jest królową, jak mawiał Hegel, ale mawiał też, że drogą ducha do wolności są dzieje. A historia z ostatnich lat pokazuje, że pan Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 676 o polityce pojednania tylko mówi. Nie zdobywacie władzy dzięki polityce miłości, tylko polityce ośmiu gwiazdek. (Oklaski) Doprowadziliście do niespotykanej nigdy wcześniej w naszych dziejach wulgaryzacji polityki. (Oklaski) (Głos z sali: Tak jest.) Ośmieliliście lumperię, która co miesiąc zakłóca uroczystości upamiętniające ofiary tragedii smoleńskiej. Wręcz dopingujecie tych ludzi, którzy co miesiąc dokonują okrucieństw. Przypominam: w katastrofie smoleńskiej zginęły także wasze koleżanki i wasi koledzy z ław sejmowych, wasi przyjaciele. Dla was nie ma świętości. Politycy Prawa i Sprawiedliwości przez 8 lat doświadczali niesamowitej agresji z waszej strony, włącznie z groźbami pobicia. To już nie jest przemysł pogardy, to jest konglomerat nienawiści. (Poseł Jakub Rutnicki: TVP.) Ku uciesze waszych psychofanów urządzaliście konkurs na to, kto posunie się dalej, kto przekroczy kolejną granicę. A tych granic jest coraz mniej. Przyjdzie wam kiedyś za to zapłacić. Obiecuję to. (Oklaski) Szanowni Państwo! Wysoki Sejmie! Zwróćcie uwagę, jak bardzo różniło się wczorajsze exposé premiera Mateusza Morawieckiego od tego, które przed chwilą usłyszeliśmy. Wczoraj zaprezentowano konkretny plan, wizję tego, jak bronić suwerenności Polski, jak zadbać o jej dalszy harmonijny rozwój i jak zwiększyć bezpieczeństwo Polski i Polaków (Oklaski), jak sprostać wyzwaniom, które stawia przed nami współczesna geopolityka. Najważniejszą i zasadniczą różnicą pomiędzy exposé premiera Morawieckiego a tym, co usłyszeliśmy z ust Donalda Tuska, jest wiarygodność. Za każdym razem, jak za mównicą stawał premier z Prawa i Sprawiedliwości, mogliśmy być pewni, że nie rzuca słów na wiatr, że to, do czego się zobowiązuje, zostanie dotrzymane. Donald Tusk wcześniej wygłaszał exposé dwukrotnie. Za każdym razem były to puste słowa, za którymi nie szedł żaden konkret. Tym razem było podobnie. Przypominam panu, że rządzenie to nie teatr emocji, tylko ciężka praca na rzecz obywateli. (Oklaski) Urząd to zaszczyt, Polska to miłość. Tą piękną dewizą Mateusz Morawiecki skwitował swoje wczorajsze exposé. (Oklaski) Dla Donalda Tuska polskość to nienormalność, a Sejm Rzeczypospolitej jest miejscem czego? Cierpienia. (Poseł Krystyna Skowrońska: Kłamiesz.) Prawo i Sprawiedliwość zawsze przedstawiało konkretny program, który był konsekwentnie realizowany. Dzięki temu, że trzymaliśmy się naszego planu, mamy teraz najniższe bezrobocie w historii, wyższe wynagrodzenia (Oklaski), a poziomem życia zrównujemy się z państwami Zachodu Europy. Mamy silną i nowoczesną armię, zdolną odstraszyć przeciwnika. Mamy jeden z lepiej rozwiniętych w Europie systemów pomocy społecznej. Staliśmy się europejskim liderem w likwidowaniu luki VAT, a polska gospodarka urosła o 1/3. To nie jest już takie państwo, jakie zostawił pan w 2014 r. Tu już nie zarabia się 7 zł za godzinę, a szczytem marzeń nie jest bilet w jedną stronę do Londynu. A pan, zamiast przedstawić konkretny program, znowu mami Polaków sloganami pozbawionymi jakiejkolwiek wartości merytorycznej. Przedstawił pan bajkową rzeczywistość. Gdzie jest 100 konkretów, o których mówił pan w kampanii? Gdzie ten cudowny plan, który miał być zrealizowany w ciągu 100 dni? Zasłanianie się koalicyjną arytmetyką i koniecznością szukania kompromisów nie zwalnia pana z realizacji umowy zawartej z wyborcami, To nie jest szacunek dla Polaków, to jest ich lekceważenie. O nie, Polacy są mądrzy i nie dadzą się wam drugi raz oszukać. (Oklaski) Wysoki Sejmie! Koalicja zemsty i chaosu za chwilę zapewne stanie się faktem. Chciałbym więc, aby Donald Tusk wyjaśnił kilka sprzeczności, jakie pojawiły się w narracji jego koalicjantów. Co z naszą polityką migracyjną? W kampanii mieliśmy zwrot o 180 stopni, jeśli chodzi o podejście PO do obrony granicy polsko-białoruskiej. Najpierw Donald Tusk nazywał nielegalnych migrantów atakujących naszych żołnierzy i funkcjonariuszy biednymi ludźmi, którzy szukają swojego miejsca na ziemi. A politycy PO mówili o tym, że mur na granicy trzeba rozebrać. Dziś można odnieść wrażenie, że Marcin Kierwiński, który jest szykowany na ministra spraw wewnętrznych, przebierze się za komandosa i osobiście będzie wyłapywał tych, którzy szturmują naszą granicę. W tym samym czasie marszałek Hołownia mówi o konieczności stworzenia systemu, który zaopiekuje się nielegalnymi migrantami. To jak w końcu jest? Bronimy granicy czy wpuszczamy wszystkich i później sprawdzimy, kto to jest? (Oklaski) Drugie pytanie. Prawo i Sprawiedliwość zadbało o polskie rodziny i wprowadziło program 800+. Przypominam o tym, bo parę dni temu nazywaliście ten program waszym konkretem i przekonywaliście, że nic, co dane, nie będzie odebrane. Tymczasem nie dalej jak we wrześniu marszałek Hołownia mówił, że trzeba rozważyć wycofanie programu. To co z tym 800+? Dogadaliście się już? Policzył pan głosy? (Oklaski) (Głos z sali: Brawo!) Trzecie pytanie. Planowane nowe traktaty unijne odbierają naszą suwerenność. To niezwykle ważna sprawa. Przez wiele lat mówiliście, że nie ma innej drogi niż pełniejsza integracja europejska. Jednak kilka tygodni temu część z waszych europarlamentarzystów zagłosowała przeciw ich przyjmowaniu, a część – również ci, którzy pojechali do Brukseli z listy PO – opowiedziała się za ich przyjęciem. Czy to była zasłona dymna? Jakie jest wasze prawdziwe stanowisko w tej sprawie? Wysoki Sejmie! Pozwólcie państwo, że przypomnę, w jakim stanie Donald Tusk zostawiał Polskę przed ucieczką do Brukseli. Według badania opinii społecznej z listopada 2013 r. niemal połowa Polaków nie widziała w działalności premiera żadnych plusów. Krytykowało jego rząd aż 81% ankietowanych. A czy mieli do tego podstawy? Oczywiście. Rządom DonalPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 677 da Tuska nie udało się poprawić sytuacji na rynku pracy. Było rekordowe bezrobocie – ponad 2 mln zarejestrowanych bez pracy. Dodatkowo dochodziła emigracja zarobkowa – nawet 3 mln młodych ludzi wyjechało za granicę w poszukiwaniu godnych zarobków. Politykę fiskalną rządu PO–PSL cechowała regularność w podwyżkach – podniesiono (Dzwonek) stawki VAT, stawkę rentową i akcyzę na niektóre produkty. Zamrożono progi PIT oraz i tak śmiesznie niską kwotę wolną od podatku. O waszym podejściu do bezpieczeństwa mówiłem bardzo wiele, ale przypomnę – to za rządów Donalda Tuska zlikwidowano ponad 600 jednostek organizacyjnych Wojska Polskiego, zahamowano modernizację techniczną i ograniczono liczbę żołnierzy. Mieliście tylko zawiesić pobór, a de facto zawiesiliście rozwój Wojska Polskiego. To tylko skrócony obraz tego, co zafundowaliście Polakom w latach 2007–2015. Tym razem będzie podobnie. Już słychać z ust polityków PO, że brakuje pieniędzy na realizację waszych obietnic. Jak to jest, że jak my rządzimy, to pieniądze zawsze są, a wystarczy, że wy dorwiecie się do władzy, to zaczyna ich brakować? (Oklaski) (Głos z sali: Brawo!) To dlatego tak wam się spieszy do likwidacji wolnych mediów. Zależy wam na tym, żeby Polacy z Telewizji Polskiej i z Polskiego Radia nie dowiedzieli się o skali waszej ignorancji oraz o tym, że nie zamierzacie realizować swoich obietnic. Nie ustaniemy w obronie wolnych mediów narodowych i wszystkiego, co polskie (Oklaski), bo chcieliście też zlikwidować Polskie Linie Lotnicze i Lasy Państwowe. Wysoki Sejmie! Wiecie, dlaczego Donald Tusk tak spieszy się jutro na spotkanie z niemiecką polityk Ursulą von der Leyen, przewodniczącą Komisji Europejskiej? (Głos z sali: Czas minął.) Po to aby zameldować: Jawohl, zadanie wykonane. (Oklaski) (Głos z sali: Wstyd.) (Poseł Cezary Tomczyk: Kompromitacja.) Panie Marszałku! Wysoka Izbo! Jutro będzie 13 grudnia. To kolejny czarny dzień w historii naszej ojczyzny, bo wybór Donalda Tuska na premiera to najgorsze, co mogło spotkać Polskę. (Poseł Borys Budka: Was.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Ma pan jeszcze 10 sekund, panie pośle.",
                },
                {
                    "speaker": "Poseł Mariusz Błaszczak",
                    "content": "Klub Parlamentarny Prawo i Sprawiedliwość będzie głosował przeciwko udzieleniu wotum zaufania Donaldowi Tuskowi. (Głos z sali: Kompromitacja.) Prawo i Sprawiedliwość zawsze będzie pilnować Polski. Będziemy bronić Polski przed koalicją zemsty i chaosu. Dziękuję. (Głos z sali: Brawo!) (Część posłów wstaje, długotrwałe oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Z kronikarskiego obowiązku wspomnę tylko, panie pośle, że zanim premier Tusk spotka się z Ursulą von der Leyen, spotka się też z prezydentem Andrzejem Dudą, który zaprosił go wczoraj na to spotkanie. W imieniu klubu Koalicji Obywatelskiej głos zabierze pani poseł Małgorzata Gromadzka z Koalicji Obywatelskiej, jak już wspomniałem. (Oklaski) A później pan poseł Patryk Jaskulski. Bardzo proszę, pani poseł.",
                },
                {
                    "speaker": "Poseł Małgorzata Gromadzka",
                    "content": "Szanowny Panie Marszałku! Szanowne Panie Posłanki i Panowie Posłowie! Czcigodni Goście! Dzisiaj już jest przepięknie, dzisiaj jest już normalnie, szanowni państwo. (Oklaski) (Głos z sali: Brawo!) I dla przeciwwagi, panie pośle Błaszczak. To moja pierwsza kadencja jako posła Rzeczypospolitej Polskiej. Reprezentuję Lubelszczyznę. Pochodzę z małej wsi Korchów Drugi w powiecie biłgorajskim. Jestem rolniczką, społeczniczką, katoliczką, przedsiębiorczynią, samorządowcem, ale przede wszystkim jestem matką czwórki dzieci. (Oklaski) (Głos z sali: Brawo!) A teraz ważna misja przede mną, ponieważ zostałam posłanką. Dzisiejszy dzień, powołanie rządu pana premiera Donalda Tuska, to dla mnie symbol prawdziwej, realnej zmiany. Żebyście zrozumieli, jak wielkiej, jak długo przeze mnie i przez wszystkich wyczekiwanej, powiem wam kilka słów o moim miejscu zamieszkania. Mieszkam na Lubelszczyźnie, gdzie Prawo i Sprawiedliwość ma ok. 80% poparcia, szczególnie w małych miejscowościach. Na Lubelszczyźnie PiS sprawuje władzę niemalże w każdym samorządzie. Ja natomiast należę do Platformy Obywatelskiej od 2010 r. (Oklaski) (Głos z sali: Brawo!) Od 2015 r., szanowni państwo, trudno w to uwierzyć, ale uprawianie polityki stało się sianiem nienawiści i podziału wśród obywateli. Ja niejednokrotnie byłam szykanowana. Pomijano mnie przy różnych imprezach lokalnych. Nawet wyrzucono mnie z pocztu sztandarowego w szkole moich dzieci ze względu na moją przynależność partyjną, ponieważ wizytować tam miał minister Czarnek i osoby, które fotografowały się ze mną, musiały liczyć się z tym, że mogą na drugi dzień stracić pracę Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów W trakcie kampanii wyborczej przemierzyłam cały okręg nr 7, tzw. chełmski. Byłam na targowiskach, ryneczkach, w sklepikach. Ludzie często odwracali się na widok serduszka, które miałam przyklejone, część rzucała w moim kierunku inwektywy, ale część, szanowni państwo, zaczynała rozmawiać. Ludzie pokazywali, że granica została przekroczona. Ludzie po prostu przestawali się bać. Zapraszali mnie do swoich domów, mieszkań. Żałowali, że nie jestem z PiS-u, bo według nich byłabym idealną kandydatką na tym terenie i wtedy mogliby na mnie oddać swój głos. A jednak zaryzykowali, zagłosowali na mnie i na Koalicję Obywatelską. (Oklaski) (Głos z sali: Brawo!) Dlaczego? Bo tak jak ja mieli dosyć propagandy i marnotrawienia publicznych pieniędzy. I nie pomogły tutaj, szanowni państwo, trefne czeki przywiezione na tekturkach przez ministrów. Panie Marszałku! Wysoka Izbo! Czym jest dla mnie Polska? Polska to zbiór małych ojczyzn, takich jak ta moja mała miejscowość. Bo w takiej małej wsi w powiecie biłgorajskim w województwie lubelskim jak na dłoni widać, jak działają samorządy, jak działają instytucje i czy granica państwa jest bezpieczna. Tam, gdzie mieszkam, ogromnym problemem jest konflikt w Ukrainie i wojna hybrydowa z Białorusią. Wielu z nas, pomagając Ukraińcom po wybuchu wojny, widziało na własne oczy, co tam się działo. To tutaj przedostawały się bojowe helikoptery. To tutaj, pod Hrubieszowem, wybuchła rakieta. Całe szczęście, że ta pod Bydgoszczą nie wybuchła, bo okazała się niewypałem. Zresztą, to jest trafne określenie 8 lat rządów Zjednoczonej Prawicy. (Oklaski) Dlatego rząd Donalda Tuska ma ogromną pracę do wykonania. To przede wszystkim dbałość o bezpieczeństwo, szczególnie bezpieczeństwo Polski Wschodniej. W takich małych wsiach, w takich małych miejscowościach ludzie mają dosyć wiecznej walki między sobą, podsycania przez agresywne, partyjne media, których w żaden sposób nie można nazwać mediami publicznymi. Mamy dość życia w poczuciu zagrożenia. W takich małych miejscowościach kobiety mają dosyć tego, że państwo i Kościół wtrącają się w ich życie. Ja mam trzy córki i chciałabym, żeby w przyszłości miały prawo same o sobie decydować. Kobiety zmobilizowały się w tej kampanii jak nigdy wcześniej, bo nie mogły już dłużej czekać. Mówiono, że rząd PiS obalą kobiety, i tak się stało. (Oklaski) I wiecie co? Rząd Donalda Tuska kobiety będą współtworzyć. Walczymy o prawa kobiet dla siebie, dla naszych przyjaciółek, dla naszych córek, dla naszych sióstr. Nasze ministry będą reprezentantkami tych wszystkich kobiet, które poszły do lokali wyborczych pokazać swoją siłę. Rząd Donalda Tuska gwarantuje, że sytuacja kobiet w Polsce się poprawi. Jestem debiutantką w Sejmie, reprezentuję nowe pokolenie Polek i Polaków. Nasi wyborcy tym niesamowitym zrywem frekwencyjnym pokazali, że chcą innej Polski niż ta dotychczas tworzona przez rząd Zjednoczonej Prawicy. To my, nowe pokolenie, którego młodość przypadła na czasy rządów PiS, chcemy Polski takiej, jak opisuje Donald Tusk. Chcemy po prostu Polski normalnej. (Oklaski) Chcemy państwa demokratycznego, w którym przestrzega się przepisów prawa i honoruje zasadę trójpodziału władzy. Chcemy godnych warunków rozwoju osobistego, zawodowego i rodzinnego. Chcemy państwa zdecentralizowanego, gdzie podstawą będzie samorząd terytorialny. Chcemy państwa, które bierze czynny udział w kształtowaniu polityki zagranicznej z Unią Europejską, NATO i z innymi organizacjami międzynarodowymi. Rząd Donalda Tuska to wielka szansa dla nas, Polek i Polaków. To jest gwarant, szansa na pojednanie: zamiast siania nienawiści – szansa na przestrzeganie praworządności, zamiast grabieży – szansa na zasypanie podziałów i nowe otwarcie. Polki i Polacy oddali na nas swoje głosy w wyborach. W rządzeniu będziemy zatem ich głosem, szanowni państwo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, pani poseł. Pan poseł Patryk Jaskulski. Zostały panu 3 minuty 40 sekund. (Głos z sali: 2 minuty, jak pan Błaszczak miał.) Dostanie pan minutę więcej, bez problemu, jeżeli nie skończy pan myśli. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Patryk Jaskulski",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Nie przyszedłem tutaj pieszo ze Szczecina, chociaż mógłbym, bo żeby stanąć tu dziś, w tym miejscu, na tej mównicy, w trakcie kampanii wyborczej przeszedłem ponad 1 mln kroków. Rozmawiałem z każdym wyborcą napotkanym na swojej drodze (Oklaski), rozmawiałem zwłaszcza z tymi, którzy mówili mi: polityka mnie nie interesuje, polityka mnie nie dotyczy, polityka nic nie zmieni, mój głos nic nie da. Czyżby? Kiedy narzekali na korki i złą komunikację w Szczecinie, wyjaśniałem, że właśnie na to wpływ ma polityka. Kiedy pomstowali na drożyznę, wskazywałem na politykę. Kiedy obawiali się kontroli i zamkniętych granic, mówiłem: tak, to też jest polityka. Jako były radny dobrze wiem, że wielka polityka ma przełożenie na wszystkie sprawy – także te małe, codzienne, zwykłe – i właśnie dlatego tutaj jestem. Panie Marszałku! Wysoka Izbo! To dla mnie symboliczny moment. Jako jeden z najmłodszych posłów Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 679 i sejmowy debiutant mam zaszczyt przemawiać po exposé nowego premiera Polski pana Donalda Tuska. (Oklaski) To znamienne, że pierwszy projekt, który zdążył już przyjąć ten Sejm, to inicjatywa obywatelska, pod którą podpisało się 0,5 mln Polaków, która przywraca refundację in vitro z budżetu państwa. To znamienne, bo kończymy ze złymi praktykami poprzedników, budując prawdziwie obywatelski Sejm, otwarty na obywateli, inicjatywy społeczne i dziennikarzy. Sejm, który już nigdy nie będzie smutnym bunkrem strzegącym władców przed demokracją. (Oklaski) Moje pokolenie to ludzie, dla których otwarte granice to oczywistość, dla których możliwość podróżowania czy studiowania w Europie to normalna sprawa. Praworządność, troska o środowisko naturalne, prawa kobiet, demokracja – wszystko to dla nas jest po prostu zwyczajne. Zwyczajne, bo urodziliśmy się z tym. Dlatego chociaż z każdej strony słyszałem, że trudno zmobilizować młodych ludzi, żeby poszli na wybory, wierzyłem, że spotkamy się właśnie tam, przy urnie. Wierzyłem, że młodzi ludzie się zaangażują, i do tego ich namawiałem. Wszyscy tutaj, po tej stronie sali, namawialiśmy, mówiliśmy, żeby w to uwierzyli. I wiecie co? Młodzi nie zawiedli. Widzieliśmy to wszyscy, gdy stali na mrozie do godz. 3 w nocy w kolejce do lokalu wyborczego na wrocławskim Jagodnie. Uwierzyli, że zmiana jest możliwa. W kampanii od młodych usłyszałem, że oni już nie kupują tego, co przekazuje Telewizja Polska. Widzą, że rzeczywistość jest inna niż ta, o której im się mówi, że są niezrozumiani, pomijani, a klimat życia w Polsce sprawia, iż coraz ciężej oddychać pełną piersią, chociaż nie mam tutaj na myśli jakości powietrza, która faktycznie jest jedną z najgorszych w Europie. Trzeba to podkreślić, że dla mojego pokolenia walka o klimat, o środowisko naturalne, o dobrostan zwierząt, o czyste powietrze, o zaprzestanie wycinki lasów czy czystość rzek to sprawy szalenie istotne, a Donald Tusk wie, jak to zmienić. Jest jednym z nielicznych polityków, którzy potrafią rozmawiać o kwestiach zmian klimatycznych i metodach radzenia sobie z nimi. To jest ta troska o przyszłość, której nie widziałem przez 8 lat z tej strony sali, dlatego tu jestem i dlatego popieram rząd Donalda Tuska. Panie Marszałku! Wysoka Izbo! Pokazaliśmy, czego chcemy, a chcemy nowoczesnego, europejskiego, demokratycznego rządu, który przestrzega konstytucji, prawa i ustaw, rządu, którego nie musimy się wstydzić wszyscy, bo jest kalką tego (Dzwonek) z Budapesztu czy Ankary. Chcemy nowoczesnej edukacji, wolności w sieci i wolności osobistej. I wiecie co? Rząd, który za chwilę powołamy, nam to wszystko gwarantuje. (Oklaski) Ostatnie zdanie. To rząd, który stworzyli liderzy trzech demokratycznych partii. Nie mam wątpliwości, że będzie on rządem dialogu, a nie monologu. Wreszcie będziemy o polityce rozmawiać na argumenty, a nie na wyzwiska. Ten rząd to nadzieja na normalność, na Polskę, która jest demokratyczna, Polskę, która będzie domem wszystkich Polaków, a nie tych, którzy mają tę jedną jedyną, właściwą legitymację partyjną. Ten rząd Polsce po prostu się należy. To nasz rząd i z przyjemnością za nim zagłosuję, panie premierze. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. W imieniu klubu Polska 2050 – Trzecia Droga głos zabierze pan poseł Michał Kobosko. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Michał Kobosko",
                    "content": "Szanowny Panie Marszałku! Szanowny Panie Premierze! Wysoka Izbo! 4 lata temu Szymon Hołownia zgromadził wokół siebie kilkunastoosobowe wówczas grono osób przerażonych kierunkiem, w którym zmierzała Rzeczpospolita. Pazerność i buta rządów środowiska Jarosława Kaczyńskiego, coraz silniej skłócone społeczeństwo, zabójstwo prezydenta Pawła Adamowicza. To z tej potrzeby zmiany narodziła się najpierw kampania Szymona Hołowni na prezydenta, a potem ruch i partia Polska 2050. Od samego początku naszych działań w przestrzeni publicznej szliśmy z kilkoma fundamentalnymi dla naszego środowiska postulatami. Pozwólcie państwo, że w dniu powstania rządu koalicyjnego, w dniu powstania koalicji 15 października, w dniu, w którym do rządu na istotne dla nas programowo stanowiska wchodzą trzy silne kobiety z Polski 2050, tutaj te nasze postulaty przypomnę. Pierwszy to: dość partyjniactwa. Partyjniactwo było jednym z największych grzechów mrocznej epoki rządów PiS. Partyjniactwo w prokuraturze, partyjniactwo w spółkach Skarbu Państwa, partyjniactwo w mediach publicznych, partyjniactwo na wszystkich szczeblach instytucji publicznych. Nie kompetencje, nie merytoryka. My mówiliśmy i mówimy temu: dość. Drugi postulat to: Kościół i władza na swoje miejsce. Relacje między państwem a kościołami i związkami wyznaniowymi, zwłaszcza Kościołem katolickim, wymagają uporządkowania. Ten proces musi przebiegać z poszanowaniem wrażliwości osób wierzących oraz tych, które nie chcą być związane z żadnym kościołem lub związkiem wyznaniowym. Naszym wielkim celem jest budowanie państwa bezstronnego światopoglądowo. Trzeci postulat to: Polska na pokolenia, a nie na kadencję. Chcemy budować Polskę demokratyczną, zieloną, różnorodną, solidarną i gospodarną, zmieniać kraj na pokolenia, a nie – jak dotąd – na jedną kadencję. To nie tylko hasło, to przede wszystkim Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 680 nasz sposób działania. Chcemy, by polityka była o ludziach i o rozwiązywaniu ich codziennych problemów, tak aby zostawić naszym dzieciom silniejszą i sprawiedliwszą ojczyznę. Czwarty postulat brzmiał 4 lata temu: prezydent różnych Polaków. Jak ważny to był postulat, widzimy także dziś, gdy tak wielu z nas ma nieprzyjemne poczucie, że prezydent reprezentuje interesy tylko jednej połowy. Dziś jednak przeformułujemy ten postulat, by brzmiał on: rząd różnych Polaków. Chcę to powiedzieć bardzo wyraźnie: to będzie rząd także wyborców Prawa i Sprawiedliwości. Polska została podzielona i skłócona i czas to zakończyć. Będziemy dbać o interesy wszystkich. Dziś mamy wreszcie szansę, by wprowadzić nasze marzenia w czyn, aby zapewnić, że przez te 4 lata nasze wartości się nie zmieniły. Dość partyjniactwa, Kościół i władza na swoje miejsce, Polska na pokolenia, a nie na kadencję oraz rząd różnych Polaków. To są nasze obietnice, nasza filozofia polityczna, nasze cele. Każdego dnia będziemy wprowadzać te postulaty w życie. Szanowny Panie Marszałku! Wysoka Izbo! 15 października Polki i Polacy nam zaufali. Zaufali siłom opozycji demokratycznej, które w tych wyborach zyskały największe poparcie. Zaufali Trzeciej Drodze, sojuszowi wyborczemu Polski 2050 Szymona Hołowni i Polskiego Stronnictwa Ludowego. Dziś ukonstytuował się rząd pod przewodnictwem naszego sojusznika w tych celach Donalda Tuska. W imieniu ruchu i partii Polska 2050 obiecuję, że od dziś będziemy ciężką pracą budować właśnie taką Polskę – Polskę demokratyczną, zieloną, różnorodną, solidarną i gospodarną, Polskę dla naszych dzieci. Dziś zaczynamy pisać nowy rozdział w historii Polski, rozdział pełen nadziei, odwagi i niewzruszonej wiary w lepsze jutro dla wszystkich nas – kraj silny, zjednoczony i pełen szacunku dla każdego obywatela i dla każdej obywatelki. W rządzie Donalda Tuska znajdą się trzy reprezentantki Polski 2050. Obejmą trzy sfery, które dla nas, dla naszego środowiska politycznego i dla naszych wyborców są szczególnie ważne. Po pierwsze, kwestie dotyczące klimatu, środowiska i transformacji energetycznej. To kwestie kluczowe dla naszego życia. Potrzebujemy czystego powietrza, a nie smogu, który zatruwa co roku zimą największe polskie miasta. Potrzebujemy budować rezerwuar wody pitnej, bo pod tym względem jesteśmy w ogonie Europy. Potrzebujemy przygotować się na przetrwanie w warunkach postępujących zmian klimatycznych, coraz wyższych temperatur, coraz bardziej nieprzewidywalnej pogody, coraz wyższych poziomów mórz, w tym także Bałtyku. By realizować te wszystkie działania, potrzebujemy coraz więcej energii elektrycznej, energii czystej i taniej, energii produkowanej dzięki odnawialnym źródłom energii, energii ze słońca, wiatru, wody, biomasy. Tym nowym źródłom energii musi towarzyszyć jako zasilenie i jako stabilizator także energetyka jądrowa. Również na tym polu jesteśmy ogromnie zapóźnieni. Fundusze unijne. To pole szczególne. Jeszcze przez pewien czas, ale przecież nie na zawsze, Polska pozostanie beneficjentem unijnych miliardów. Będziemy o wiele więcej uzyskiwać, niż wpłacać do wspólnego unijnego budżetu. Musimy dobrze i mądrze wykorzystać ten czas i te fundusze. Po pierwsze, musimy odblokować środki, które Polsce się należą, a z których z winy rządu PiS nie mogliśmy w ostatnich latach korzystać. Dobrze wydane pieniądze unijne to pieniądze, które pójdą na przyspieszenie transformacji naszego kraju, zielonej przemiany, przyspieszenie cyfryzacji, inwestycji w żłobki i w ochronę zdrowia. To te dziedziny, które dziś wymagają istotnego i szybkiego dofinansowania. Dobrze wydane fundusze unijne to też zmniejszenie dysproporcji rozwojowych między regionami naszego kraju. Tak jak mówiliśmy w kampanii wyborczej, twoje miejsce zamieszkania, twój kod pocztowy nie mogą determinować twojego życia, twoich szans i twojej przyszłości. Nie można zatem dyskryminować osób z mniejszych ośrodków i mniej zamożnych rodzin. Wreszcie społeczeństwo obywatelskie. Jesteśmy ogromnie wdzięczni sektorowi pozarządowemu, dziesiątkom mniejszych i większych organizacji, ruchów obywatelskich, które przez te 8 lat pielęgnowały naszą demokrację, walczyły o jej obronę, przypominały i mobilizowały nas, polityków, do starań o przywrócenie podstawowych zasad funkcjonowania państwa prawa, wartości demokratycznych, trójpodziału władzy, Konstytucji Rzeczypospolitej Polskiej. Silne społeczeństwo obywatelskie, to silne społeczeństwo, silny naród, silne państwo. Polska 2050, która powstała i rozwijała się jako ruch obywatelski, jako sprawna organizacja pozarządowa, jako wolontariat, ponosi szczególną odpowiedzialność za rozwój i wspieranie sektora pozarządowego. I tym także zajmiemy się w koalicyjnym rządzie. Panie Premierze! Bardzo dziękuję za to exposé, za wspomnienie o tragicznie zmarłym Piotrze Szczęsnym, za tak ważne słowa o naszej wspólnocie, wspólnocie narodowej, o sile tej wspólnoty i o konieczności przeciwstawiania się próbom osłabiania, rozbijania tej wspólnoty. Dziękuję za jednoznaczne słowa dotyczące Ukrainy i naszego wspólnego obowiązku wspierania Ukrainy, kiedy Ukraińcy walczą o ich wolność i o naszą wolność. Dziękuję za słowa o pozycji Polski w Unii Europejskiej, w NATO, o pozycji Polski na świecie. Musimy tę pozycję przywrócić, musimy tę pozycję zbudować dzisiaj, by osiągnęła taki poziom, z którego wszyscy będziemy zadowoleni i którym będziemy usatysfakcjonowani. Panie Premierze! Jesteśmy gotowi do ciężkiej pracy i do dobrej współpracy z naszymi partnerami w koalicji Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 681 15 października dla dobra Polek i Polaków, dla dobra Polski. Klub Parlamentarny Polska 2050 – Trzecia Droga z wielkim przekonaniem poprze wniosek o wotum zaufania dla Rady Ministrów kierowanej przez Donalda Tuska. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. W imieniu klubu Polskie Stronnictwo Ludowe – Trzecia Droga głos zabierze poseł Władysław Kosiniak-Kamysz. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Władysław Kosiniak-Kamysz",
                    "content": "Wielce Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! Szanowni Państwo! Koalicja 15 października to koalicja wartości i konkretów. To jest też emanacja tego, co pan premier Tusk powiedział w swoim exposé. Zaczął od wartości, od tej wartości podstawowej, wartości nadrzędnej, wartości bezwzględnie koniecznej do zapewnienia Polsce bezpieczeństwa, czyli rzeczy, do której jesteśmy powołani jako politycy, parlamentarzyści, za chwilę jako rząd – wspólnoty. Chodzi o wspólnotę narodową, która jest zawsze jedynym, podstawowym i niezbędnym gwarantem bezpieczeństwa. To wiemy z naszej historii, trudnej i bolesnej, i z naszej wiktorii, wspaniałej i godnej. Nie będzie o tę wspólnotę łatwo. Słyszymy bezwstydne słowa, oskarżające, mówiące, że hejt, że nienawiść to jest z tej strony. Mówią to ci, którzy przez ostatnie 8 lat stworzyli fabrykę hejtu i nienawiści działającą od świtu do nocy w mediach publicznych. (Oklaski) To jest okrutne. My to rozumiemy, to jest wasza frustracja wynikająca z tego, że się nie możecie pogodzić z wyrokiem suwerena, z decyzją wyborczą. My będziemy, powiem wam, niestrudzeni w tym, żeby łączyć i budować mosty porozumienia, żeby odbudować wspólnotę narodową również dla waszego bezpieczeństwa, dla bezpieczeństwa naszych wszystkich wyborców, wszystkich obywateli Rzeczypospolitej Polskiej. To jest nasza obietnica, to jest nasze przyrzeczenie, to jest właśnie koalicja 15 października, koalicja wartości i konkretów. Ludowcy w tej koalicji. Trzecia Droga, PSL – szliśmy do tych wyborów pod różnymi hasłami. Szliśmy pod hasłami właśnie odbudowania wspólnoty, hasłami związanymi z gospodarką, z przedsiębiorczością, z aktywnością, ze wsią i rolnictwem. W czterech słowach mogę ująć te obszary odpowiedzialności: żywią i bronią, gospodarują i budują. To będzie sfera odpowiedzialności Polskiego Stronnictwa Ludowego w rządzie, jeśli chodzi o działy administracji. Rolnictwo i wieś, i Czesław Siekierski zaprezentowany przez pana premiera jako minister odpowiedzialny za tę sferę. Tu jest wielkie wyzwanie, bo ceny płodów rolnych, opłacalność w rolnictwie są na najniższym od lat poziomie. Ceny zboża, żniwa, które już za nami, były takie jak 20 lat temu, ale ceny produkcji – wielokrotnie wyższe. Skrócenie łańcucha dostaw żywności. Opłacalność produkcji rolnej. Ziemia dla polskich rolników, a nie wyprzedaż polskiej ziemi – to będzie nasze hasło i to będzie nasz punkt programowy. (Oklaski) 30-dniowy termin płatności. Budowa portu zbożowego. Zabezpieczenie interesów polskiej gospodarki, w tym polskich rolników. One nie stoją naprzeciw pomocy Ukrainie, tylko one wymagają, tak jak powiedział pan premier, realnego dialogu, rozmowy i jasnego stawiania swoich spraw. Dla nas nasza gospodarka, nasze bezpieczeństwo ekonomiczne, bezpieczeństwo ekonomiczne rodzin żyjących z uprawy i hodowli, są niezwykle ważne. My z tych korzeni wyrastamy i o tych korzeniach pamiętamy. Fundusz stabilizacji dochodów rolniczych, który wpisaliśmy do umowy koalicyjnej. Zwiększenie opłacalności i promocja polskiej żywności za granicą. To są konkrety, które będziemy realizować w obszarze bezpieczeństwa żywności, która jest skarbem narodowym, która jest najlepszą marką i którą możemy promować na całym świecie, nie: sprzedawać polskie bezpieczeństwo za granicą, tylko promować i sprzedawać najlepszą polską żywność. (Oklaski) Gospodarka. Krzysztof Hetman to proponowany minister rozwoju i technologii. Przedsiębiorcy przynieśli Polsce zmianę, przynieśli Polsce zwycięstwo. Przez wiele lat obrażano ich, nawyzywano ich drobnymi cwaniaczkami. W imieniu Polskiego Stronnictwa Ludowego – Trzeciej Drogi, a myślę, że również w imieniu nas wszystkich, chcę podziękować polskim przedsiębiorcom, chcę podziękować rodzinnym firmom, mikro- i małym przedsiębiorcom, tym, którzy prowadzą jednoosobową działalność gospodarczą. Dla niektórych byliście przez ostatnie 8 lat drobnymi cwaniaczkami. Dla nas jesteście bohaterami, jesteście solą naszej ziemi. (Oklaski) Będziemy o was dbać, będziemy dbać o dialog społeczny, będziemy dbać o to, żeby dialog z pracodawcami i z pracownikami, z organizacjami pracodawców i ze związkami zawodowymi – ze wszystkimi, a nie z jedną organizacją – był realny. Dialog społeczny zostanie w Polsce odtworzony. Sładki na ZUS i wakacje od ZUS-u to jest jedna z naszych propozycji programowych. (Głos z sali: Dobrowolne.) Chorobowe wypłacane od pierwszego dnia przez ZUS, a nie przez pracodawcę, to jeden z konkretów z umowy koalicyjnej, którą zawarliśmy. (Oklaski) Postawienie na odnawialne źródła energii, kasowy PIT to konkrety, które za chwilę będą realizowane. To jest sfera naszej odpowiedzialności i fundament. Praca była upokarzana, praca była niedoceniana, praca Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 682 była źle wynagradzana. Praca w Polsce musi się opłacać (Oklaski) i praca w Polsce będzie się opłacać. Ci, którzy pracują, którzy dają coś z siebie, będą otrzymywać więcej. Nie zapomnimy oczywiście o tych, którzy potrzebują wsparcia i pomocy, o tych, którym jest trudno, np. o osobach z niepełnosprawnością. To jest takie nasze wspólnotowe wartościowe zobowiązanie. Sprawa infrastruktury, sprawa transportu to sprawa istoty funkcjonowania państwa. Chodzi o dostęp do dóbr, do cywilizacji, do rozwoju, do możliwości kształcenia, do lekarza, do opieki medycznej. To sprawa jakości życia i polityki spójności. Dariusz Klimczak to nasz kandydat na ministra infrastruktury zaprezentowany przez pana premiera Tuska. Drogi lokalne, przywrócenie połączeń, rozwój w pierwszej kolejności transportu autobusowego, kolejowego, żeby ktoś, kto ma 80, 90 lat, mógł nawet z najmniejszej miejscowości dojechać do miejscowości gminnej, do miejscowości powiatowej do lekarza, do apteki, do sklepu, do tego wszystkiego, co mu gwarantuje i musi zabezpieczać państwo. Chodzi o rozwój zarówno tej najbardziej potrzebnej, najbliższej infrastruktury, jak i tej wielkiej infrastruktury, która umożliwia nam funkcjonowanie. Wody Polskie, dbanie o żeglugę w każdym ujęciu, dbanie o gospodarkę morską, gospodarkę związaną z wykorzystywaniem i szanowaniem, zabezpieczeniem przeciwpowodziowym – to jest nasze wielkie zadanie. Obrona. To dla mnie niezwykły zaszczyt i wielka odpowiedzialność. Obrona narodowa, Ministerstwo Obrony Narodowej, bezpieczeństwo państwa polskiego. W obliczu wszystkich zagrożeń, tego, co dzieje się na świecie, w tej rzeczywistości, która tak niezwykle doświadczyła naszych sąsiadów, zapewnienie tego wszystkiego, co jest fundamentem suwerennego, niepodległego państwa, czyli jego bezpieczeństwa, ochrony granic, nienaruszalności terytorialnej, będzie dla nas najwyższym nakazem. To jest nasze ogromne zobowiązanie. Wspólnota narodowa jako numer jeden, wzmocnienie w sojuszach Unii Europejskiej i NATO, zmodernizowana, dobrze zorganizowana i zarządzana armia. (Oklaski) Przed chwilą pan przewodniczący Błaszczak mówił, że minister Kierwiński będzie się przebierał za komandosa. Będzie zupełnie odwrotnie. (Oklaski) Koniec ubierania się w mundury, bo mundury są dla żołnierzy, dla funkcjonariuszy. Dla polityków jest zupełnie inny strój, ten, w którym tu występujemy. To wy się przebieraliście. Koniec przebierańców. (Oklaski) (Głos z sali: Brawo!) Wszystko będzie poukładane – cywilny nadzór nad armią, rola Wojska Polskiego i dowódców Wojska Polskiego. Wszystko będzie poukładane. Ja wiem, że porządek niektórych drażni, denerwuje, ale będzie porządek i będzie bezpieczeństwo. To jest nasza gwarancja, to są nasze konkrety, to jest nasze zobowiązanie. Mówiliśmy o państwie, które działa w oparciu o pewną staranność, o hasło: silna Polska bez zamordyzmu. To jest sprawa do osiągnięcia, ona jest tak naprawdę na wyciągnięcie ręki. Może istnieć państwo, które gwarantuje bezpieczeństwo, ale w żaden sposób nie jest zamordystyczne. Patriotyzm bez zadęcia i duma z naszej historii, tradycji, ale też ten patriotyzm codzienny, nie tylko od święta, i postęp bez szaleństwa – te trzy rzeczy są naszym udziałem i te trzy rzeczy nim będą. To jest nasza gwarancja, to jest nasze zobowiązanie. (Oklaski) Pozwólcie na koniec też na osobiste słowa. Przez 8 lat zabierałem głos przy okazji każdego exposé. od 8 lat jestem prezesem Polskiego Stronnictwa Ludowego. (Dzwonek) Wielu dążyło do tego, żeby najstarszej partii w Polsce nie było, żeby ją z politycznego życia wymazać. W ostatnim czasie w kampanii wyborczej wiele osób z jednej i z drugiej strony do tego dążyło i wieszczyło, że tak się stanie. Dziękuję wszystkim naszym wyborcom, dziękuję historii i pokoleniom ruchu ludowego (Oklaski), że daliście mi ogromną siłę, że mogę dzisiaj prezentować naszych kandydatów, wspólnie ich przedstawiać i być w rządzie, brać odpowiedzialność za wielką sferę. Oczywiście nie stało by się to bez moich najbliższych, którzy zawsze wierzyli, trwali i byli, bez Paulinki, Zosi i Różyczki, bez moich rodziców (Oklaski), mojej siostry, moich najbliższych. Bardzo wam dziękuję. Dziękuję tym wszystkim, którzy w całej Polsce w nas wierzą, którzy wierzą, że koalicja 15 października, koalicja wartości i konkretów uniesie ciężar odpowiedzialności, zbuduje silną, bezpieczną i dostatnią Polskę. Tak zrobimy i tak będzie. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Głos zabierze teraz pani Anna Maria Żukowska jako reprezentanta klubu Lewicy. Bardzo proszę, pani posłanko.",
                },
                {
                    "speaker": "Poseł Anna Maria Żukowska",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! W ostatnich wyborach zagłosowała rekordowa liczba Polek i Polaków. Na ugrupowania tworzące przyszły rząd oddano 11,6 mln głosów. To ogromne zobowiązanie, zaufanie, a także odpowiedzialność. To jest rząd, na który większość Polek i Polaków czekała 8 lat, niektórzy czekali 18 lat, ale są i tacy, którzy na taki rząd czekali całe życie, jak moja córka. Nie pamiętają świadomie innych rządów niż te, które zafundował im Jarosław Kaczyński. Wyrosło całe pokolenie, które nie znało innego premiera niż premier Morawiecki. Nie znało też innej demokracji niż ta zdeformowana, w której z tylnego siedzenia rządził epizodyczny premier Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 683 Ale te czasy się skończyły. Wyborcy zdecydowali. Wśród nich jest wiele kobiet, młodych kobiet. To szczególnie one nie pamiętają innego rządu niż ten PiS-owski rząd, który wypowiedział wojnę im i ich prawom. Dzięki wam, dziewczyny, wspólnie wygraliśmy wybory. Dziękujemy wam. To wielkie zobowiązanie. (Oklaski) Lewica podjęła to zobowiązanie. Będzie strażnikiem praw kobiet. To zadanie nowej minister do spraw równości Katarzyny Kotuli i minister pracy Agnieszki Dziemianowicz-Bąk, ale też każdego ministra i wiceministra, każdej ministry i wiceministry z rekomendacji Lewicy w tym rządzie. To rząd nadziei na zmianę w polityce europejskiej, w praworządności, w prawach człowieka. Niektóre nadzieje spełnią się szybko, tak jest w sprawie in vitro. Niektóre będą spełnione za chwilę. Z realizacją innych będziemy musieli poczekać do 2025 r., do wyborów prezydenckich, ale w tej kadencji żaden temat nie zostanie uznany za temat zastępczy czy, uwaga, nietykalny ze względu na tzw. światopogląd. My, posłanki Lewicy, złożyłyśmy już dwa projekty ustaw dotyczących prawa do przerywania ciąży i będziemy namawiać koleżanki i kolegów z koalicji rządowej do ich poparcia. Dekryminalizacja pomocy w aborcji oraz legalizacja przerywania ciąży to nie jest światopogląd, to po prostu prawa kobiet. Nowa Lewica wchodzi do tego rządu, aby być gwarantem właśnie m.in. praw kobiet, budowy mieszkań na wynajem, usług publicznych, neutralności światopoglądowej państwa, ochrony praw pracowniczych, renty wdowiej, czystego powietrza, sprawiedliwej transformacji energetycznej, transportu publicznego czy ochrony praw mniejszości. Nieprzypadkowo mam dzisiaj ze sobą to tęczowe serce. Serce jest ostatnio dosyć cenionym symbolem na tej sali. Bardzo dziękuję naszym negocjatorom, Darkowi i Marcelinie, bo to im udało się wywalczyć szereg postulatów z naszego programu wyborczego i wpisać je do umowy koalicyjnej. To dzięki nam, dzięki Lewicy znalazły się one w programie rządzenia nowej Rady Ministrów. Chciałam przez chwilę opowiedzieć o tych postulatach. Po pierwsze, nastąpi przywrócenie porządku prawnego, odpolitycznienie Sądu Najwyższego i Krajowej Rady Sądownictwa. Po drugie, nastąpi uznanie tzw. wyroku Trybunału Konstytucyjnego w sprawie aborcji za nieistniejący. Wiem, że to dopiero pierwszy krok, ale od czegoś trzeba zacząć. Jak już mówiłam, my, Lewica, na tym nie poprzestaniemy. Po trzecie, opieka psychologiczna dla uczniów w każdej szkole. Temat jest bardzo poważny i Lewica go przypilnuje. Pamiętacie okrągły stół w sprawie psychiatrii dziecięcej, który tutaj, w Sejmie zorganizowała Paulina Piechna-Więckiewicz? Następny zorganizuje już w Ministerstwie Edukacji Narodowej jako podsekretarz stanu. Paulina zrobi wszystko, by pomóc dzieciom i młodzieży w kryzysie zdrowia psychicznego. Musimy reagować i pomóc im natychmiast. Po czwarte, macierzyństwo i ojcostwo. In vitro to za mało. Aby w Polsce rodziło się więcej dzieci, należy zagwarantować przyszłym rodzicom poczucie bezpieczeństwa. Kobietom należy zagwarantować pełny dostęp do bezpłatnych badań prenatalnych i do znieczulenia przy porodzie. Należy znormalizować urlopy tacierzyńskie dla mężczyzn. Po piąte, będziemy budować nowe żłobki, aby rodzice mogli spokojnie wrócić do pracy, zostawiając dzieci pod dobrą opieką i nie wydając na to ogromnych pieniędzy. Będziemy również tworzyć nowe przedszkola, aby wyrównywać szanse edukacyjne dzieci. Po szóste, już niebawem nastąpi nowelizacja Kodeksu karnego tak, aby mowa nienawiści ze względu na orientację czy tożsamość psychoseksualną lub płeć była ścigana z urzędu. Każdy, kto jak prezydent Andrzej Duda powie, że LGBT to nie ludzie, ale ideologia, będzie musiał odpowiedzieć za swoje słowa. (Głos z sali: Nie powiedział tak, pani poseł. Dlaczego pani…) Po siódme, rząd będzie aktywnie działał na rzecz likwidacji luki płacowej. Państwowa Inspekcja Pracy dostanie nowe kompetencje, takie kompetencje, które pozwolą jej skutecznie stać na straży praw pracowniczych i nareszcie je egzekwować oraz ucywilizować obecnie uśmieciowiony rynek pracy. Po ósme, rząd będzie prowadził politykę mieszkaniową zakładającą wsparcie budowy mieszkań na wynajem – także dzięki pieniądzom z KPO, które wywalczyliśmy, które odblokujemy. Po dziewiąte, zgadzamy się w koalicji co do rozwoju transportu publicznego i zintegrowanego systemu biletowego. Po dziesiąte, poprawimy sytuację seniorów po śmierci współmałżonka. Obywatelski projekt ustawy w sprawie renty wdowiej przygotowany przez mojego kolegę Arkadiusza Iwaniaka został złożony w Sejmie i będzie dalej procedowany. Po jedenaste, nowy rząd wie, że alimenty to nie prezenty, dlatego poprawimy skuteczność egzekucji alimentów. Po dwunaste, podwyżki dla nauczycieli i pracowników służby publicznej, w tym administracji, sądów i prokuratury. O podwyżki dla nauczycieli akademickich zadba nowy minister nauki Dariusz Wieczorek. Po trzynaste, przywrócimy prawa nabyte emerytów mundurowych. (Głos z sali: Uuu…) Tak, razem z nimi złożyliśmy ćwierć miliona podpisów pod projektem obywatelskim dotyczącym tych praw i dzisiaj o tym nie zapominamy. Będziemy budować nowoczesny miks energetyczny, który zapewni Polkom i Polakom tani prąd i czyste powietrze. Zwiększymy obszar objęty ochroną w parkach narodowych. Będziemy dbać o zielone płuca Polski. Odpartyjnimy media publiczne Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 684 Po siedemnaste, nowoczesny patriotyzm. Pamięć i prawda historyczna. To dzięki lewicy, dzięki zmarłemu tydzień temu byłemu przewodniczącemu Polskiej Partii Socjalistycznej Bogusławowi Gorskiemu i jego interwencji udało się nie wymazać z kart polskiej historii i tym samym z planów obchodów stulecia niepodległości Polski jednego z ojców polskiej niepodległości, marszałka Ignacego Daszyńskiego. To zamierzał zrobić rząd PiS. (Głos z sali: Pani poseł, to jest nieprawda.) Prawda, dokładnie prawda. Odpartyjnimy kulturę i zagwarantujemy wolność artystyczną. Artyści dostaną dostęp do systemu ubezpieczeń społecznych i skończymy z artystyczną biedą. Będziemy wspierać samorządność. Skończymy z polityką głodzenia samorządów i wręczania im na pocieszenie tekturowych czeków. Wreszcie, po dwudzieste… Wprawdzie nie udało się wpisać do umowy koalicyjnej ani związków partnerskich, ani równości małżeńskiej, niemniej właśnie dzisiaj Europejski Trybunał Praw Człowieka podjął historyczną decyzję w sprawie Polski i praw związków jednopłciowych. Uznał, że Polska narusza art. 8 europejskiej konwencji praw człowieka poprzez brak zapewnienia możliwości uznania i ochrony związków osób tej samej płci. I ja mówię tutaj, na tej sali: miłość w końcu wygra. (Oklaski) Członkowie i członkinie rządu z rekomendacji Nowej Lewicy każdego dnia będą kierować się wartościami, które są wspólne dla naszych wyborczyń i wyborców. To wolność, równość i sprawiedliwość społeczna. Wysyłamy do rządu silną ekipę Lewicy. Wicepremier Krzysztof Gawkowski będzie odpowiadać za cyfryzację, Agnieszka Dziemianowicz-Bąk – za pracę i rodzinę oraz politykę społeczną, Dariusz Wieczorek – za naukę, Katarzyna Kotula – za równość, za pomoc grupom defaworyzowanym. Dariusz Wieczorek jako minister do spraw nauki i szkolnictwa wyższego będzie dbał o to, aby akademik był prawem, a nie towarem. Kojarzycie okupację Jowity w Poznaniu? To akademik UAM. Studenci i studentki muszą obecnie walczyć o to, aby mieć gdzie mieszkać w rozsądnej cenie. Kochani i kochane, możecie i będziecie mieć nasze wsparcie. Krzysztof Gawkowski będzie pilnował, aby przestępcy nie wykradali waszych danych cyfrowych, a wielkie korporacje nie zarabiały na naruszeniach waszej prywatności. Agnieszka Dziemianowicz-Bąk będzie normalizować rynek pracy, likwidować jego patologie. (Dzwonek) Znacie te ogłoszenia o prace, w których jest wspomniana praca na pełen etat? Tylko że nie jest oferowany żaden etat, a umowa zlecenia. A jako benefity są wymieniane normalne, kodeksowe prawa, które mają być czymś dodatkowym. No właśnie. Agnieszka z tym skończy. Zadba także o wprowadzenie asystencji osobistej dla osób z niepełnosprawnościami. Katarzyna Kotula będzie stała na straży równości. Będzie pilnować praw kobiet, mniejszości, osób z niepełnosprawnościami. Będzie walczyć z dyskryminacją. Znacie Kaśkę, ona się nigdy nie poddaje. Lewica to wartości. I właśnie z tych powodów, o których mówiłam, z powodu uznania i wpisania do umowy koalicyjnej naszych postulatów poprzemy rząd pana premiera Donalda Tuska. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Głos zabierze pan poseł Krzysztof Bosak w imieniu klubu Konfederacji. Bardzo proszę, panie marszałku. (Poseł Grzegorz Braun: Wreszcie głos rozsądku.)",
                },
                {
                    "speaker": "Poseł Krzysztof Bosak",
                    "content": "Panie Marszałku! Wysoki Sejmie! Zapowiadaliśmy przez całą kampanię wyborczą, że nie poprzemy ani rządu Mateusza Morawieckiego, ani rządu Donalda Tuska. Słowa dotrzymujemy. Już w tym exposé mamy wyjaśnienie, jasną listę dowodów, dlaczego tego nie zrobimy. Otóż to było przede wszystkim exposé z naszej perspektywy niezwykle podobne do wystąpień polityków PiS-u. Oni prezentują pewien specyficzny rodzaj mesjanizmu. Uważają, że tylko oni są w stanie uratować Polskę, oni nie są od tego, żeby normalnie rządzić, oni są od tego, żeby definiować zasady, definiować wartości, wszystkim coś tłumaczyć. Dziś pan przyszedł i zaprezentował to samo, tylko w innej odsłonie. Okazuje się, że większości ze swojego dwugodzinnego przemówienia nie poświęcił pan na przedstawienie planu rządzenia, na przedstawienie tego, co będziecie się starali zrobić, osiągnąć, na złożenie choćby ogólnych obietnic, tak jak zrobił to pan w 2007 r. Byłem jednym z analityków, którzy liczyli wówczas pańskie obietnice. Było ich ponad 200. Przemawiał pan wtedy 3 godziny. Dziś przez 2 godziny złożył pan zaledwie kilkanaście obietnic, niektóre wariantowe, na zasadzie: przeanalizujemy, zobaczymy, będziemy audytować, nie wiadomo. My nie oczekujemy od rządu żadnego nowego mesjanizmu. Tu nie potrzeba ratować republiki. Tu nie potrzeba uczyć społeczeństwa, czym jest demokracja. Tu potrzeba dobrego rządzenia, którego PiS nie potrafił dostarczyć, i widzimy, że jesteście na dobrej drodze, żeby wpaść w dokładnie te same koleiny. Z 2 godzin przez ponad godzinę słyszeliśmy ogólniki, patos, granie na emocjach, nawet odwoływanie się do samobójstw, podczas gdy przed kancelarią premiera, kiedy pan był premierem, też spalił się człowiek, też z powodu frustracji i różnych problemów Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 685 Kiedy pan rządził, przedsiębiorcy nawet wdzierali się siłą na posiedzenia komisji, by protestować przeciwko temu, że byli niszczeni przez złe prawo, które nie gwarantowało ich praw, mimo że pracowali dla państwa. Być może byliśmy jedynym państwem w Europie, w którym ktoś, robiąc kontrakty dla rządu, doprowadzał swoją firmę do bankructwa, bo takie warunki dawało państwo. Czy PiS to zmienił? Nie do końca. Dziś także można wykonywać rządowe przetargi i być doprowadzonym do bankructwa w wyniku braku zapłaty. Sam mam kontakt z przedsiębiorcami, którzy nie mogli się w waszym rządzie wystarać o zapłatę za wykonane roboty. Tymczasem mieliśmy ogólniki, patos, granie na emocjach, mnóstwo ogólnych zapowiedzi o charakterze ideologicznym. Przyjmujemy do wiadomości to, że jesteście koalicją lewicy, progresywnych liberałów pomieszanych z socjalistami i postchadekami, ludowców i obywatelskich polityków od Polski 2050. Przyjmujemy to do wiadomości, natomiast nie musicie edukować reszty społeczeństwa na swoją modłę. Nie zapowiadajcie tego, nikt na to nie czeka. Czekamy jako Polacy, czekamy jako politycy Konfederacji – opozycji wobec was, twardej, merytorycznej, normalnej opozycji, którą będziecie w nas mieli – czekamy, że pokażecie, że da się rządzić normalnie. Czy to pokażecie? Wasze przemówienie niestety tego nie zapowiada (Oklaski) i nasze doświadczenia z wami tego nie zapowiadają. Dlaczego? Pan, panie premierze, wczoraj i dzisiaj prezentował się tu jako nieledwie ofiara totalitaryzmu, podczas gdy pan jest jednym z beneficjentów systemu III RP, który od początku do końca ten system budował. Panie premierze, pan nie jest ofiarą totalitaryzmu. Pan doskonale w polskiej polityce się odnalazł i w niej funkcjonuje. Ludzie, którzy mogą się ustawiać w roli ofiar, to ludzie, którzy, kiedy pan był premierem, siedzieli np. w areszcie wydobywczym po 2 lata, bo pan i pańscy ministrowie wpadliście na pomysł wojny z kibicami. (Głos z sali: 4 lata.) To ludzie, którzy byli zatrzymywani na marszach niepodległości (Oklaski), a następnie skazywani przed sądami – chodziłem na sale sądowe i patrzyłem, jak to się odbywa – na podstawie fałszywych zeznań funkcjonariuszy Policji, bez żadnych dowodów, nawet kiedy nagrania wideo potwierdzały, że ktoś był niewinny. Ja organizowałem przeciwko pańskiemu rządowi manifestacje po aferze taśmowej. Zostałem zatrzymany na ul. Szucha wraz z innym byłym posłem, Robertem Winnickim, przez Policję i następnie przy mnie za waszej władzy policjanci bezczelnie pisali fałszywe notatki, że rzekomo ich zaatakowałem, podczas gdy nagrania wideo tego nie potwierdzały. Przed sądem te zarzuty upadły, ale wcześniej Policja kontrolowana przez pańskich ministrów utrudniała moim adwokatom kontakt ze mną i ustalenie, kiedy znajdę się na sali sądowej. Tak wyglądała praworządność w waszym wypadku. (Oklaski) Może pan się tłumaczyć, że pan o tym nie wiedział. Może pan się tłumaczyć, że to nie była pana odpowiedzialność, tylko kogoś innego, że później pan wyjechał i w ogóle był zarobiony, miał ważne obowiązki w Brukseli. (Głos z sali: Ha, ha, ha!) Może pan się tak tłumaczyć. Natomiast to są fakty. Dlatego z naszej perspektywy zapowiedź tego, że wy będziecie teraz tutaj fundować praworządność, rządy prawa, naprawiać sądy, prokuratury itd., to są czcze zapowiedzi. Wyście przez 8 lat ćwiczyli swoje porządki w wymiarze sprawiedliwości i to, co mieliśmy, to mieliśmy nadużycia ze strony służb specjalnych, mieliśmy nadużywanie środków przymusu bezpośredniego przez Policję, brak szacunku dla wolności zgromadzeń. Sytuacja na ulicach uspokoiła się, kiedy oddaliście władzę. (Głos z sali: Tak było.) W momencie, gdy zdawaliście władzę, odbył się pierwszy spokojny Marsz Niepodległości. (Głos z sali: Tak jest!) Pamięta to pan, panie premierze? (Oklaski) Czy z Brukseli już pan tego nie widział, a pani Kopacz, która była wtedy premierem, nie przekazała tych informacji? (Głos z sali: To z miłości.) Piękne słowa o miłości, pojednaniu, solidarności, ale panu jest trudno wygłosić jedno przemówienie, w którym co 10 minut nie sączy pan jakichś jadowitych aluzji. (Oklaski) Ci ludzie, którzy tu siedzą, mają bardzo poważne wady. Naszym zdaniem oni rządzili fatalnie. Uważamy, że powinni być odsunięci od władzy i bardzo dobrze, trochę higieny politycznej w Polsce się przyda. Trzeba was z tych urzędów pousuwać, może wrócicie do kontaktu z rzeczywistością, zamiast uważać się za mesjaszy naszego narodu. (Oklaski) Natomiast wy w tę rolę nie wchodźcie, bo wejdziecie w te same co i wcześniej koleiny. Bez konkretów w pańskim przemówieniu: o cyfryzacji, o budownictwie, mieszkaniach, o energetyce. Dlaczego mamy najwyższe ceny energii? Bo wspólnie, PiS i Platforma, ustalaliście takie reguły i w takie wprowadziliście nas w Unii Europejskiej, że płacimy horrendalne certyfikaty za to, jaką mamy energetykę. (Oklaski) (Poseł Grzegorz Braun: Tak jest!) Zręby pod to kładł nie pański rząd, tylko Jarosław Kaczyński, który negocjował traktat lizboński, który negocjował i akceptował systemy ETS. Pan to twórczo rozwinął. Pana były doradca Mateusz Morawiecki zradykalizował to, na co pan się zgodził. Nie różnicie się tak bardzo, jakbyście chcieli to przedstawić społeczeństwu. (Oklaski) Rozwijaliście te same polityki – i wy, i wy. Nikt z was nie wetował kluczowych rzeczy, najważniejszych dla Unii Europejskiej Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 686 Pan dzisiaj zapowiada proeuropejskość, powrót do głównego nurtu w Europie itd. Znamy te hasła. Wiemy mniej więcej, z czym one się wiążą. Znów będziecie się na wszystko zgadzać, żeby siedzieć przy tzw. głównym stole, podczas gdy Niemcy i Francuzi publikują już raporty o Europie wielu prędkości i stawiają nam wymagania, że mamy się w kolejnych dziedzinach wyrzec prawa weta, żeby zrobić to, co wy chcecie, czyli integrować Ukrainę z Unią Europejską. A jak wiemy, Ukraina ma sprzeczne z nami interesy w obszarze przewozowym i w obszarze rolniczym. Dziś pan zapowiada, że jest pan tego świadomy i już pan spędził kilka nocy nad rozmowami na ten temat. Ale jak pan chce te sprzeczności usunąć, pan nie powiedział. Pan już jest premierem, już pan ponosi odpowiedzialność – a dziś w nocy mieliśmy atak Policji na protestujących. Pan się w ogóle do tego nie odniósł. (Oklaski) (Głos z sali: Hańba!) Zakładam, że pan o tym słyszał, że pan o tym wiedział. Jeżeli pan się do tego nie odniósł w sposób krytyczny, jeżeli pan nie przedstawia, że to odpowiedzialność Mateusza Morawieckiego, który ustawił Policję w ten sposób, żeby zrobiła z protestującymi porządek w momencie przejściowym, to znaczy, że pan się z tym zgadza. Jeżeli inaczej, proszę wyjść i powiedzieć, jakie widzi pan rozwiązania. Postulaty protestujących to powrót do systemu zezwoleń, kiedy i ukraiński, i polski sektor transportowy się rozwijał. Pan nawet prawidłowej frazeologii dziś nie użył. Mówi pan o kierowcach. To nie kierowcy. Problemem dotyczy branży przewozowej. Kierowcy to tylko element całego systemu transportowego, przewozowego. O czym jeszcze nie powiedział pan konkretów? Budownictwo, energetyka. Zdrowie – hmm… Powiedział pan tyle, że jest dużo pieniędzy. Problem w obszarze zdrowia jest zgoła inny niż taki, że jest tam za dużo pieniędzy. Podatki – niczego się nie dowiedzieliśmy poza tym, że będzie kasowy PIT. Edukacja – niczego poza tym, że będą 30-procentowe podwyżki od stycznia we wszystkich szkołach, na uniwersytetach oraz przedszkolach i równowaga finansów publicznych jednocześnie. Czekamy niecierpliwie, żeby w styczniu zrecenzować, jak idzie wam realizacja tych postulatów. Ja, szczerze mówiąc, kompletnie w to nie wierzę. No, ale zobaczymy. Już pan naskładał w 2007 r. 200 obietnic, później obliczyliśmy, ile zostało zrealizowanych. Zdecydowana mniejszość. Infrastruktura i transport – po tych wszystkich nocach narad i analiz pan premier i pańskie otoczenie nie wiecie, czy chcecie budować CPK, nie wiecie, czy chcecie budować elektrownię atomową, nie wiecie, co z małymi reaktorami atomowymi? (Głos z sali: Słabo.) Z całym szacunkiem, ale już jest moment rządzenia. To już jest czas, kiedy jednak powinniście te rzeczy wiedzieć. Powinniście te rzeczy wiedzieć albo chociaż zakreślić termin na podjęcie decyzji. Ile będą teraz trwały analizy? Mam nadzieję, że nie 8 lat. Niepokojąco brzmią pańskie i innych polityków waszego obozu zapowiedzi dotyczące tego, że będziecie być może wstrzymywać… W Niemczech są już bardzo rozbudzone nadzieje, że może nie powstanie port kontenerowy, że może nie będzie regulacji Odry do żeglowności, że może nie będzie CPK. To nie są rzeczy, których Polska potrzebuje: żeby wstrzymać wszystkie strategiczne inwestycje pod pretekstem rozszerzania systemu socjalnego. Teraz będziecie rywalizować z PiS-em o seniorów. A gdzie było słowo o młodych ludziach? A gdzie było słowo o ludziach w średnim wieku? (Poseł Grzegorz Braun: Nie było.) Będziemy w tej chwili budować najlepszą politykę senioralną na świecie, a jako naród wymieramy. (Dzwonek) Pan nie powiedział słowa o tym, jak pan widzi politykę migracyjną w kontekście niżu demograficznego, tylko że pan będzie z państwami bałtyckimi chronił granicę. Z całym szacunkiem, ale tam, gdzie państwa bałtyckie chcą z nami współpracować, ta współpraca już jest. Pan nie musi jechać w tej sprawie do Tallina. My potrzebujemy jasnej wizji polityki migracyjnej. Pańscy politycy, którzy są pod pańską komendą, dezorganizowali pracę Straży Granicznej, obrażali funkcjonariuszy. Z pana strony nie padło słowo potępienia tych praktyk. (Oklaski) (Poseł Grzegorz Braun: Tak było.) Podsumowuję, bo czas się kończy. Nie wiemy, w jaki sposób chce pan zabezpieczyć polską pozycję w Unii Europejskiej. Na stole jest wyrzeczenie się prawa weta. Poprzednio przy traktacie lizbońskim wy i PiS popieraliście wyrzeczenie się prawa weta przez Polskę w różnych dziedzinach. (Poseł Grzegorz Braun: Hańba!) Nie wiemy, w jaki sposób chce pan walczyć z zadłużeniem Polski. PiS udaje, że nie podniósł zadłużenia, podniósł je bardzo znacznie. Ale i wy to robiliście, przecież ministra Rostowskiego za to krytykowaliśmy. My nie chcemy w rządzie wpływów lewicy, którą pan obsadza na kluczowych stanowiskach, odpowiedzialnych za pracę, za edukację, za rodzinę. To kuriozalne decyzje jak na byłego polityka centroprawicy, ciągle przez jakieś nieporozumienie należącego do partii chadeckiej czy może postchadeckiej. Nie chcemy poprawności politycznej, nie chcemy ograniczenia wolności wypowiedzi, które pan próbował wprowadzić, kiedy poprzednio był pan premierem. Testował pan to. Nie znalazła się większość. Oby i w tym Sejmie się nie znalazła. Nie chcemy uczenia nas wartości, bo swoje wartości mamy i znamy. Nie chcemy uczenia nas europejskości. Nie chcemy centralizmu w Unii Europejskiej. Nie chcemy etatyzmu i socjalizmu. Będziemy dla was twardą opozycją, która broni wolności, niepodległości, tradycji, patriotyzmu, umiaru i rozsądku. Taką opozycję w nas będziecie mieli Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 687 Jeśli coś wam wyjdzie, nie zawahamy się tego zauważyć, bo nie jesteśmy ideologicznie nastawieni, że ma się wam nie udać. Nie chcemy sekciarskiego konfliktu PiS-u i Platformy. (Oklaski) Chcemy Polski normalnej, w której rządzi się dobrze. Pańskie exposé w tej chwili krytykujemy, bo pańskie exposé było skupione na sekciarskim sporze PiS-u i Platformy, a nie na planie dobrego rządzenia. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!) (Głos z sali: Precz z sektami…)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Bezcenne wsparcie kolegów. Dziękuję, panie marszałku, panie pośle. Pan Marek Jakubiak z koła Kukiz’15 jako ostatni. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Marek Jakubiak",
                    "content": "Panie Marszałku! Wysoka Izbo! Ciężko się tu stoi, tak zaorane to pole.",
                },
                {"speaker": "Marszałek", "content": "Gdzie?"},
                {
                    "speaker": "Poseł Marek Jakubiak",
                    "content": "Tutaj taka orka przed chwilą była, szczególnie wypowiedzi premiera Tuska. Szanowni Państwo! Powiem tak, to podsumowanie całego tego exposé: przebrał się diabeł w ornat i na mszę ogonem dzwoni. A powiem, że tak z przyzwoitości należałoby powiedzieć o sprawie kibiców, o której Krzysztof przed chwilą mówił. Chyba nie znam polityka tej rangi w Polsce, który by tak jaskrawie walczył z polskimi kibicami. Ja bym nie poruszał sprawy Żylety, Legii, bo musiałbym cytować, co śpiewali wtedy na pański temat. To chyba taki żart z pańskiej strony. Co do drewna, proszę państwa, i Lasów Państwowych. Oczywiście, że ja przyznaję panu rację. Panie premierze, Lasy Państwowe to jest nasz dobrostan, to jest potęga, może trochę mniejsza niż w innych państwach, ale jednak lasy to taka podstawa. Ale to pański rząd sprowadził tutaj jednego z największych szwedzkich producentów mebli, umiejscowił go na terenie Rzeczypospolitej, chociaż nie chciano go nigdzie indziej na świecie. To pan zbudował największy tartak w Polsce, którego w historii Rzeczypospolitej nie było. To wszystko było za pańskiej kadencji, więc jakąś dwoistość postawy wyczuwam w takich stwierdzeniach, że będziemy dbali o lasy. Sprowadzi pan następną Ikeę? Nie wiem. Cały czas nie mogę się z tym pogodzić, że państwo Polskę pokazujecie w takim micie politycznym jako taki jakiś ciemnogród, jakiś zaścianek Europy, że tu trzeba wszystko naprawiać, że tu jest wszystko źle, teraz będzie znacznie lepiej. Wiecie państwo, nie tylko my słuchamy tego Sejmu. Nas słuchają również ludzie za granicą oraz inwestorzy. Ja bym prosił jednak stronę, która przejmuje rządy, aby trochę bardziej roztropnie traktowała takie wypowiedzi, bowiem tylko w Warszawie, proszę państwa – a propos tego szowinizmu, nacjonalizmu itd. – w 2023 r. kupiono 3,5 tys. mieszkań. I to kupili cudzoziemcy. Oni w nas bowiem widzą zupełnie coś innego, niż państwo widzą. Oni tu widzą bezpieczeństwo, oni tu widzą czystość, uśmiechniętych ludzi i przynajmniej tę opowieść na przyszłość. To widzą cudzoziemcy. Łącznie w Polsce sprzedano cudzoziemcom ok. 14 tys. mieszkań. Cytuję za branżą turystyczną. Tylko w 2023 r. branża turystyczna zanotowała 88-procentowy wzrost sprzedaży. To są również wycieczki do Polski. Jesteśmy jednym z większych odkryć światowych jako państwo nieodkryte, warte zobaczenia, bo tej całej, że tak powiem, kulturowości Zachodu tu jeszcze na szczęście nie ma. Polska przeżywa wielką metamorfozę. To widzą wyraźnie państwa zachodnie. Dbamy o nasze bezpieczeństwo. Wydaje się, że tutaj kontynuacja polityki byłaby wskazana. Jeden z waszych polityków powiedział kiedyś, że Polska to jest – aż trudno mi się to cytuje, bo mi się to po prostu w głowie nie mieści – brzydka panna na wydaniu, i to w dodatku bez posagu. Chcę zapytać, ponieważ widzę te same twarze w rządzie, te stare twarze, czy poważnie tak postrzegacie swoją ojczyznę. Brzydka panna na wydaniu bez posagu? To ja muszę powiedzieć, że tu się absolutnie różnimy, bowiem Polska jest najpiękniejszą kobietą na świecie – zdolną, silną, inteligentną. Jest wyjątkowa, bo jest nasza. (Oklaski) Proszę państwa, nie ma drugiej takiej kobiety na świecie, o którą walczyłyby i za którą oddawały życie miliony Polaków, po to właśnie, żeby istniała. Polska to jest nasze dobro, to jest nasza matka i to jest nasza ojczyzna. Zdaje się, że tu wszyscy powinniśmy się z tym zgadzać, jest tylko kwestia tego, jak do tego dojdziemy. Ja rozumiem, że państwo odczuwacie w tej chwili euforię po dokonaniu dość trudnego porozumienia, które nastało po decyzji większości głosujących, natomiast nie zgadzam się z tym, żebyście atakowali Narodowy Bank Polski tylko dlatego, że żeście sobie coś ubzdurali, że on jest polityczny. Pytam: A za waszych czasów Narodowy Bank Polski oczywiście nie był upolityczniony, był bez wpływów politycznych? Narodowy Bank Polski, o dziwo, w historii polskiej zgromadził coś, czego do tej pory nie było, rezerwy walutowe i rezerwy złota. (Oklaski) Otóż mamy 360 t złota (Dzwonek), mamy 180 mld dolarów. Zachowujecie się jak Butch Cassidy, który zobaczył złoto Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 688 w banku, z którym trzeba po prostu, nie wiem, coś zrobić. Orlen – drugi problem. Proszę państwa, już mi tu pika, bo ja mam mniej czasu niż inni. Natomiast ja chcę powiedzieć, że wstydzilibyście się, naprawdę. Orlen to jest gigantyczne przedsiębiorstwo, które urosło w ciągu kilku lat i którego zazdrości nam połowa świata. I jeżeli teraz chcielibyście cokolwiek powiedzieć, to ja wam podam chociaż trochę wyników. Za waszych czasów, w ciągu 8 lat Orlen przyniósł dywidendę w postaci 2,8 mld, dziś, po 7 latach – 14 mld. (Głos z sali: Kosztem ludzi.) Dziś zatrudnia 65 tys. ludzi, a za waszych czasów zatrudniał tylko 19. To jest kwestia patrzenia na rzeczywistość. (Oklaski) (Głos z sali: Kogo zatrudnili?)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, proszę do konkluzji.",
                },
                {
                    "speaker": "Poseł Marek Jakubiak",
                    "content": "Przepraszam, przepraszam. Chciałbym się też odnieść do prowokacji, której pan wczoraj z premedytacją dokonał. Powiem, że nie zgadzam się na granie emocjami, tylko chciałbym, żeby polityka była dla dobra wspólnego, a nie na zasadzie: jeden przeciwko drugiemu. Wczoraj dokonał pan tu całkiem niepotrzebnej prowokacji i powiem, że jako dojrzały człowiek wyraźnie ją widziałem i odnotowałem. Dlatego o tym mówię. Pokazywanie palcem człowieka i mówienie w kontekście pełnej wiedzy, że zaraz zareaguje, bo chodzi o śmierć bliźniaka, jest taką trochę – powiem – słabą niegodziwością. (Oklaski) Ale cóż, widać tak musiało być.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, przekroczył pan czas w sposób znaczny. Bardzo proszę. (Poseł Sławomir Nitras: I nie tylko czas, nie tylko czas przekroczył.)",
                },
                {"speaker": "Poseł Marek Jakubiak", "content": "To mogę?"},
                {
                    "speaker": "Marszałek",
                    "content": "To konkluzja i dziękuję, bo naprawdę nie mieliśmy już…",
                },
                {
                    "speaker": "Poseł Marek Jakubiak",
                    "content": "Nie chcę tutaj nikogo obrażać. Polska jest jedna, demokratyczne wybory są jedne i z nimi się nie polemizuje. Ja mam ambiwalentny stosunek do polityków. Dla mnie istotą rzeczy jest działanie dla dobra Rzeczypospolitej. Dlatego też, panie premierze, my co prawda wstrzymamy się, ale czekamy na to, żeby pan jako premier działał dla dobra wspólnego, wyciągając wnioski z błędów, które do tej pory były popełniane. Życzymy powodzenia.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Drodzy państwo, proszę o chwilę uwagi, bo podam ważne dla nas wszystkich informacje natury formalnej. Zamykam w tej chwili listę posłów zgłoszonych do pytań. Posłów zgłoszonych do pytań jest ponad 250, dokładnie 254. To cieszy, że dzisiejsze… (Głos z sali: I posłanek.) I posłanek. …exposé budzi tak potężne zainteresowanie. Wczoraj to zainteresowanie było nieco mniejsze. A to, drodzy państwo, oznacza, że będziemy procedować w sposób następujący: ja za chwilę ogłoszę 15-minutową przerwę, tak żebyśmy mogli na moment odsapnąć, i o godz. 13.55 zacznie się seria pytań. Ponieważ tych pytań zostało zgłoszonych tyle, czas na każde pytanie to będzie minuta. Będziemy… Panie pośle Dolata, wiem, że pan chce 30 sekund. Będzie minuta. Ludzie są ciekawi… (Głos z sali: 2 minuty, panie marszałku.) Ciekawość to jest… Pytali mnie pańscy koledzy, czy będzie 30 sekund. Będzie minuta, będzie tak, jak było wczoraj, żeby nikt nie zarzucił, że są nierówne zasady. Natomiast uprzedzam, że będziemy z koleżankami i kolegami restrykcyjnie pilnować czasu i w razie jego przekroczenia wyłączać mikrofon, z szacunku dla nas wszystkich. (Poruszenie na sali) To oznacza, że głosowanie, po odpowiedzi pana premiera, nad składem Rady Ministrów może wydarzyć się, panie pośle Kuźmiuk, najwcześniej ok. godz. 19. I bardzo proszę państwa, żebyście byli gotowi na tę godz. 19 ze swoją gotowością do głosowania. Może być później. Dzisiejsze obrady Sejmu skończymy prawdopodobnie około godz. 23 lub nawet około północy, dlatego że głosowanie nad składem Rady Ministrów, jak wiecie, nie wyczerpuje porządku obrad. (Głos z sali: Nocą?) Chcieliście państwo pytać, korzystać ze swoich przywilejów. Przywileje mają też swoje skutki. Drodzy państwo, ogłaszam przerwę do godz. 13.55.  Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 689",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Wysoka Izbo! Wznawiam obrady. Do tego punktu do pytań zapisało się 253 posłanek i posłów. Lista została zamknięta. Zapraszam pana posła Marcina Porzucka, Prawo i Sprawiedliwość. (Oklaski) Ma pan 1 minutę. (Głos z sali: Brawo, Marcin!)",
                },
                {
                    "speaker": "Poseł Marcin Porzucek",
                    "content": "Pani Marszałek! Wysoka Izbo! Podejmę proste decyzje, które obniżą ceny paliw do 5 zł za 1 l – to są pańskie słowa sprzed kilku miesięcy. Mówił pan, że jest proste rozwiązanie, aby to osiągnąć. Chciałbym zapytać w imieniu polskich kierowców, kiedy będziemy płacić po 5 zł za 1 l paliwa i jakie narzędzia zamierza pan zastosować. Przypomnę także, że politycy Platformy Obywatelskiej straszyli Polaków w czasie kampanii wyborczej, że przed świętami ceny paliw sięgną 8 zł za 1 l. Jak wiemy, kompletnie to się nie sprawdziło. Nasz czempion narodowy – Orlen doskonale radzi sobie w całym regionie Europy Środkowo-Wschodniej, doskonale się rozwija, a my wszyscy jesteśmy jego współwłaścicielami. Mam wielką nadzieję, że odpowie pan na to pytanie. Drugie pytanie dotyczy waszego kandydata, sejmowego kandydata Platformy Obywatelskiej, do Rady Polityki Pieniężnej sprzed roku. Wybraliście kandydata, pana Borowskiego, bankowca z Credit Agricole, który chwalił w 2021 r. (Dzwonek) politykę NBP i Radę Polityki Pieniężnej, jeżeli chodzi o stopy procentowe. Dlaczego wybraliście…",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Dziękuję.",
                },
                {
                    "speaker": "Poseł Marcin Porzucek",
                    "content": "…rekomendowaliście kandydata, który chwalił pana Glapińskiego? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję, panie pośle. Zapraszam pana posła Cezarego Tomczyka, Koalicja Obywatelska. Ma pan 1 minutę.",
                },
                {
                    "speaker": "Poseł Cezary Tomczyk",
                    "content": "Pani Marszałek! Wysoka Izbo! Tutaj niedawno pan Marek Suski zwrócił się z takim przesłaniem: Trzymajcie się za portfele. Wydaje mi się, że to jest przesłanie skierowane przede wszystkim do polityków PiS-u, bo jak patrzę na to, co się działo po tej stronie sali przez te lata – żona posła Sobolewskiego – pięć rad nadzorczych, mąż Jadwigi Emilewicz – Orlen wspominany tutaj przed chwilą, brat poseł Golińskiej – Energa, córka Cymańskiego – Energa – to to był po prostu łup, dla was Polska to był łup. Wy sobie nie potraficie tego wyobrazić, że dzisiaj zaczyna się zupełnie inny standard, że to jest taka podstawowa różnica, że dla was wejście do rządu, dla was wejście do polityki to był po prostu podział łupów. I nagle pojawia się człowiek, który rezygnuje z funkcji europejskiej, ważnej funkcji europejskiej, po to żeby walczyć o polskie sprawy tutaj. I to jest moment wyjątkowy, moment historyczny. I cieszę się, że wszyscy możemy w tym uczestniczyć, również wy. Myślę, że wiele z tego, posłowie PiS-u, wyniesiecie dla siebie. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję, szczególnie za dyscyplinę. Zapraszam panią posłankę Izabelę Bodnar, Polska 2050 – Trzecia Droga. Zapraszam.",
                },
                {
                    "speaker": "Poseł Izabela Bodnar",
                    "content": "Szanowna Pani Marszałkini! Wysoka Izbo! Od 8 lat o tej chwili marzyłam… (Oklaski) (Głos z sali: Ooo…) …każdego dnia ja, marzyły dziesiątki moich przyjaciół, miliony polskich obywateli marzyliśmy o tej chwili. Jestem dzisiaj posłanką m.in. dlatego, że marzenia mi po prostu nie wystarczały. Przecieraliśmy oczy przez te lata, patrząc jak coraz zuchwalej władza depcze demokratyczne wartości, dewastuje praworządność, konstytucję, zawłaszcza media, sączy jad propagandy, kłamstwo próbuje nazywać prawdą, złodziejstwo działaniem w literze prawa. Z biegiem czasu na naszych przerażonych oczach władza poczynała sobie coraz śmielej, przekraczając kolejne granice, zawłaszczyła trybunał, prokuraturę, służby, przypuściła ataki na wolne sądy, zagarniała nasze wolności obywatelskie, prześladowała ludzi niestandardowych, inwigilowała nas jak w Orwellu. Zastanawialiśmy się, jak to jest możliwe. Raptem trzy dekady (Dzwonek) od zrzucenia sowieckiego jarzma, 100 lat od odzyskania niepodległości w Polsce – dlaczego Polsce przytrafia się kolejny tak dramatyczny chichot historii?",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję, pani poseł Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 690",
                },
                {"speaker": "Poseł Izabela Bodnar", "content": ""},
                {
                    "speaker": "Panie premierze, demokratyczny rządzie, Polsko",
                    "content": "Go! (Oklaski) (Głosy z sali: Go!) (Głos z sali: Brawo!) (Głos z sali: Bis!)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Pani poseł, bardzo dziękuję. Zapraszam panią poseł Urszulę Pasławską, Polskie Stronnictwo Ludowe – Trzecia Droga. Ma pani minutę.",
                },
                {
                    "speaker": "Poseł Urszula Pasławska",
                    "content": "Szanowna Pani Marszałek! Panie Premierze! Wysoka Izbo! Dzisiaj zmieniamy bieg ze wstecznego na ten najbardziej przyspieszający do przodu. I bardzo ważne jest to, aby w tych naszych ambitnych celach zadbać również o zrównoważony rozwój. Dlatego mam pierwsze pytanie dotyczące samorządów, które zostały przez państwa wykluczone z możliwości pozyskiwania środków publicznych. Takim przykładem jest moje województwo, piękne województwo warmińsko-mazurskie, i Olsztyn, gdzie na siedem naborów do tzw. Polskiego Ładu w pięciu ostatnich Olsztyn otrzymał równiutkie zero. Jak wyrównać te straty, jak wyrównać te możliwości, które zostały stracone? (Poseł Barbara Bartuś: A składał wnioski?) I drugie pytanie dotyczące Lasów Państwowych. Dla nas jako Polskiego Stronnictwa Ludowego, jako Trzeciej Drogi Lasy Państwowe są bardzo istotne. Przygotowaliśmy pakt dla Lasów Państwowych, który zakłada nie tylko odpolitycznienie, nie tylko zmianę systemu zarządzania poprzez politykę włączającą (Dzwonek) społeczeństwo, ale również przywrócenie godności munduru leśnika.",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję.",
                },
                {
                    "speaker": "Poseł Urszula Pasławska",
                    "content": "Jakie jest pana stanowisko, panie premierze, w tej sprawie? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję, pani poseł. Zapraszam pana posła Arkadiusza Sikorę, Lewica. Minuta.",
                },
                {
                    "speaker": "Poseł Arkadiusz Sikora",
                    "content": "Pani Marszałkini! Wysoka Izbo! Panie Premierze! Podczas prezentowanego przez pana exposé podkreślił pan, jak ważna jest przyszłość nie tylko nasza, ale także naszych dzieci i wnuków. Podkreślił pan również ważne dla naszego rządu priorytety: przyroda i dbałość o nią. Niestety nasi poprzednicy z Prawa i Sprawiedliwości zrobili sobie kosztem zdrowia naszego i naszych dzieci niezły biznes. Widać to dobrze na Dolnym Śląsku. W ciągu ostatnich lat do Polski napłynęło kilkadziesiąt tysięcy ton toksycznych odpadów, które są składowane nie tylko na Dolnym Śląsku, ale w całym kraju. Dzisiaj takich nielegalnych toksycznych wysypisk śmieci w Polsce jest ok. 500. Samorządy nie dają sobie rady z uprzątnięciem tego. I wydaje mi się, że jedną z podstawowych i bardzo szybkich decyzji powinno być właśnie przeznaczenie (Dzwonek) czy stworzenie specjalnego funduszu, który pozwoli samorządom wspólnie z rządem te nielegalne wysypiska śmieci uprzątnąć.",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Arkadiusz Sikora",
                    "content": "Bardzo o to proszę i będę temu kibicował. Dziękuję. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Zapraszam pana posła Grzegorza Brauna, Konfederacja.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Panie Premierze! Obiecał pan odpowiedzieć na każde z pytań, które padną dziś z tej mównicy. Pytanie brzmi, czy złożył pan już zawiadomienie o możliwości popełnienia przestępstwa przez Jarosława Kaczyńskiego, przestępstwa, które mogłoby polegać na niedopełnieniu obowiązków bądź przekroczeniu uprawnień. Jeśli Kaczyński wiedział, a nie powiedział wcześniej, to przestępstwo, to Kodeks karny, prawda. Dlatego że jeśli osoba urzędująca, notabene, tak jak i pani marszałek w tej chwili urzęduje, więc z urzędu posiada wiedzę, że w tej sali miota się takie straszne oskarżenia o zdradę stanu, służenie obcemu państwu… Więc teraz, jeśli pan, panie premierze, wie, że Kaczyński wiedział, nie powiedział, to czy pan już złożył? Nie ukrywam, że moją intencją jest doprowadzenie tutaj do repliki finału „Policji” Mrożka, gdzie to Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 691 policja sama się wyaresztowała. Mam nadzieję, że PiS zamknie (Dzwonek) PO, a PO zamknie PiS i wtedy będziemy mieli spokój. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję, panie pośle. Marek Jakubiak, Kukiz’15. Zapraszam.",
                },
                {
                    "speaker": "Poseł Marek Jakubiak",
                    "content": "Pani Marszałek! Wysoka Izbo! Pragnę sprostować, powstało jakieś nieporozumienie. Oczywiście nie poprzemy pańskiego rządu. (Oklaski) (Głos z sali: Brawo!) To jest po pierwsze. Po drugie, chciałem zapytać, ponieważ co piąty pracownik w Polsce to pracownik strefy budżetowej, a podwyżki, które pan chce zrobić, są pomiędzy 30% a 20%… Chciałem zapytać pana, czy będzie to dotyczyło również żołnierzy, policjantów, strażaków itd., lekarzy i całej strefy budżetowej z urzędnikami włącznie. A po trzecie, chcę zadać również pytanie o pańskie obietnice z 2007 r. dotyczące mieszanej ordynacji wyborczej, likwidacji JOW-ów i tego wszystkiego, co pan wtedy obiecywał, a dziś jest większość konstytucyjna i można tego dokonać, to czy pan to zrobi? Dziękuję uprzejmie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Dziękuję. Zapraszam panią poseł Barbarę Bartuś, Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Barbara Bartuś",
                    "content": "Dziękuję. Pani Marszałek! Wysoka Izbo! Panie Premierze! Polacy oczekiwali na to dzisiejsze exposé, i to nie tylko ci Polacy, którzy pochodzą spod ośmiu gwiazdek, ale też Polacy, którzy patrzą z obawą w przyszłość, na to, co nas czeka pod pańskimi rządami. Co prawda powiedział pan, że nic, co zostało dane, nie zostanie zabrane: rozumiemy wszyscy, że trzynaste, czternaste emerytury, 500+, kapitał opiekuńczy, 300+. Nie zostanie odebrane to, co zostało już Polakom wypłacone dzięki decyzjom rządu Prawa i Sprawiedliwości. Ale chcemy zapytać o przyszłość, bo w tym długim exposé, co prawda już nie 3 godziny, ale 2 godziny, tak naprawdę nie było żadnych konkretów. Mówił pan jedynie o podwyżkach dla nauczycieli 30%, 20% dla całej budżetówki. Nie wiem też, czy zaliczyć do tego ZUS. To też osoby, które oczekują podwyżki, a jednocześnie pan mówił, że nie ma pieniędzy. Więc komu zabierzecie (Dzwonek), żeby dać tym osobom podwyżki? No i kluczowe pytanie: Co z kwotą wolną od podatku? Miało być 100 dni i 60 tys. kwoty wolnej od podatku. Pytam, co z kwotą wolną od podatku. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Dziękuję, pani poseł. Jarosław Wałęsa, Koalicja Obywatelska. Czas – 1 minuta.",
                },
                {
                    "speaker": "Poseł Jarosław Wałęsa",
                    "content": "Pani Marszałek! Panie Premierze! Uważam, że ma pan przed sobą tyle pracy, że nie potrzebuje pan wujka dobra rada. Ale jest jedna rzecz, która jest pomijana, ale jest fundamentalna. Korpus Służby Cywilnej. To jest jedna z pierwszych rzeczy, którą oni zniszczyli. Już w styczniu 2016 r. znieśli konkursy i obniżyli standardy. I wydaje mi się, że powinniśmy do tego wrócić. Jeszcze jest jedna rzecz, o której trzeba przypominać. Pamięta pan, jak w 2007 r. wchodził pan ze swoimi ministrami do ministerstw? Co pan zastał po nich? Spaloną ziemię. Obawiam się, że teraz będzie jeszcze gorzej. Dlatego, panie premierze, chciałem panu coś przekazać. Nosiłem ten znaczek całą uprzednią kadencję. Jest na nim wizerunek mojego ojca i napis: konstytucja. To był mój wskaźnik, do którego powinniśmy dążyć. (Dzwonek) I mam nadzieję, że będzie pan też o tym pamiętał w swojej pracy, żebyśmy nie byli tacy jak oni. Przestrzegajmy prawa, przestrzegajmy konstytucji. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję. Zapraszam pana posła Adama Gomołę, Polska 2050 – Trzecia Droga. Ma pan 1 minutę.",
                },
                {
                    "speaker": "Poseł Adam Gomoła",
                    "content": "Szanowna Pani Marszałek! Wysoki Sejmie! Panie Premierze! Bardzo ciepło przyjąłem pana wczorajszą dedykację dla dwóch pana dziadków, którzy doświadczyli prześladowań za swoją polskość. Może też dlatego, że tak się składa, że i moja rodzina, mój prapradziadek Jan Gomoła i jego siedmiu synów spędzili Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 692 całą wojnę w Buchenwaldzie. I to właśnie dlatego też w kampanii spływały do mnie pytania, dlaczego mimo krzywdy, której doznała moja rodzina od Niemców, tak twardo stoję w obronie interesów polskich obywateli mniejszości niemieckiej. Dlatego będę gorąco apelował do pana premiera o zakończenie tej jedynej na skalę całej Europy prawnej dyskryminacji mniejszości narodowej, jaka ma miejsce w Polsce, i zmazanie tej hańby, którą okrył poprzedni rząd, wprowadzając taki system do polskiego prawa, a także – myślę, że się zgodzimy – o uznanie tożsamości śląskiej, narodowości, największej (Dzwonek) mniejszości w Polsce, która według ostatniego spisu powszechnego liczy ponad 0,5 mln osób. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję, panie pośle. Zapraszam pana posła Stefana Krajewskiego, Polskie Stronnictwo Ludowe – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Stefan Krajewski",
                    "content": "Pani Marszałek! Panie Premierze! Wysoka Izbo! Jestem mieszkańcem województwa podlaskiego. My mamy swoje białe złoto: mleko, produkcja mleka, najlepiej zorganizowane zakłady mleczarskie w Polsce, ale i w Europie. To są nasze perełki. I ostatni kryzys na rynku mleka spowodował, że wiele gospodarstw miało trudności z utrzymaniem, ze spłatą kredytów, ale też zakłady odczuwają ten kryzys. Więc moje pytanie brzmi: Czy jest realna szansa, by urealnić ceny w skupie interwencyjnym? Chodzi o interwencję ogólnie na rynku europejskim, bo pewnie wszyscy się będą mierzyć z tym problemem, kiedy przyjdzie kolejna fala kryzysu, a taka może się pojawić. Tutaj trzeba też działania ze strony Polski, ze strony polskiego rządu. (Dzwonek) Myślę, że jest to w interesie wszystkich rolników w całej Polsce, ale też w interesie konsumentów. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję. Zapraszam pana posła Tadeusza Tomaszewskiego, klub Lewica. 1 minuta, panie pośle.",
                },
                {
                    "speaker": "Poseł Tadeusz Tomaszewski",
                    "content": "Pani Marszałek! Wysoki Sejmie! Szanowny Panie Premierze! Lewica wnosi do koalicji 15 października program „Bezpieczny senior”. O dwóch elementach tego programu mówił pan w swoim exposé: po pierwsze, o nowym podejściu do polityki senioralnej, po drugie, o waloryzacji w przypadku przekroczenia 5% inflacji dwa razy do roku. Chciałbym również zapytać o elementy dotyczące tzw. emerytury wdowiej, o kwestię podniesienia wysokości zasiłku pogrzebowego, bo wiem, że na jednym ze spotkań pan premier już o tym mówił. Po trzecie, jest kwestia dotycząca tzw. emerytur stażowych. W całym systemie emerytalnym – ZUS podaje – na marzec tego roku funkcjonuje, szanowni państwo, 365 tys. osób, które pobierają kilkusetzłotowe, kilkunastozłotowe emerytury, tzw. śmieciowe. (Dzwonek) Myślę, że pański rząd będzie musiał się z tym zmierzyć, bo w najbliższym czasie będzie to dotyczyło 600 tys. osób. Dziękuję.",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję. Zapraszam pana posła Konrada Berkowicza, Konfederacja.",
                },
                {
                    "speaker": "Poseł Konrad Berkowicz",
                    "content": "Panie Premierze! Pan powiedział w ogólnym exposé, że trzeba przywrócić zasady, które są wspólne nam wszystkim, wszystkim Polakom. Powiedział pan o państwie prawa, o demokratyzmie. Myślę, że kto jak kto, ale pan doskonale sobie zdaje sprawę, że państwo prawa musi być ufundowane na konkretnym systemie wartości. Trzeba wybrać wartości, które są na kursie kolizyjnym ze sobą. Mamy albo państwo prawa wolności, jak u Kanta, u Jeffersona, Stanisława Lema, i mamy państwo prawa równości, jak u Jana Jakuba Rousseau. A więc albo mamy państwo prawa, gdzie jest równość, ale wobec prawa i wolność jednostki, a więc w efekcie naturalne nierówności między ludźmi, albo mamy państwo prawa, gdzie jest siłowo zaprowadzana równość między ludźmi, niwelowana nierówność. Wiem, że pan chce zadowolić wszystkich. Nawet kiedyś się pan za Kołakowskim określił mianem liberalnego konserwatysty socjalisty. Ale trzeba wybrać. Pytam, czy jest pan po stronie wolności, czy egalitaryzmu i socjalizmu. (Dzwonek) Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Bardzo dziękuję. Zapraszam pana posła Jarosława Sachajkę, Kukiz’15.",
                },
                {
                    "speaker": "Poseł Jarosław Sachajko",
                    "content": "Pani Marszałek! Panie Premierze! Wysoka Izbo! W 2021 r. Paweł Kukiz zrealizował pańską obietnicę Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 693 sprzed 16 lat. Jest już w polskim porządku prawnym ustawa antykorupcyjna, która zabrania posłom pracować w spółkach Skarbu Państwa. Przez lata media donosiły o zatrudnianiu rodzin w spółkach Skarbu Państwa, gazety publikowały długie listy nazwisk rodzin posłów, gdy pan rządził w latach 2007–2014. Również dzisiaj poseł Cezary Tomczyk wymieniał nazwiska rodzin posłów w państwowych spółkach. Jest to gangrena, która toczy Polskę od ponad 30 lat. Chciałbym zapytać pana premiera, czy uzupełni pan ustawę antykorupcyjną o zakaz zatrudniania rodzin posłów w spółkach Skarbu Państwa, czy jednak skorzysta pan z tego narzędzia, aby tuczyć rodziny polityków, i hasło: rodzina na państwowym dalej będzie istniało. Dziękuję.",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Dziękuję. Dariusz Matecki, Prawo i Sprawiedliwość. (Głos z sali: Uuu…) (Poseł Jakub Rutnicki: PiS-owski hejter.) Zapraszam.",
                },
                {
                    "speaker": "Poseł Dariusz Matecki",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Może niech poseł Kołodziejczak krzyknie do nich, żeby byli cicho. (Głos z sali: Uuu…) (Poseł Bartosz Arłukowicz: Musisz pamiętać, co robiłeś. Hejter.) Sytuacja taka: trzeba zlikwidować WOT, bo one nie służą naszemu społeczeństwu. Nie widzimy efektów ich działań. Kto to powiedział? Władysław Kosiniak-Kamysz. Kto w wywiadzie dla Polsatu nazwał żołnierzy Wojsk Obrony Terytorialnej parawojskiem? Pan. Prywatna armia Macierewicza. Znów będę bilbordem, trudno. Tak wyglądały wasze słowa: mięso armatnie, ORMO – tak nazywani byli żołnierze Wojsk Obrony Terytorialnej. Pytanie: Co zamierza pan zrobić z Wojskami Obrony Terytorialnej? W jaki sposób mają być rozwijane? I pytanie o Lasy Państwowe. W ogóle szczytem jest to, że pan wypowiadał się na temat Lasów Państwowych. Proszę pokazać jedną umowę na sprzedaż przez Lasy Państwowe (Dzwonek) drewna do Chin, bo bardzo często w kampanii wyborczej posługiwał się pan tym kłamstwem. (Oklaski) (Głos z sali: Pośrednicy zarobili.)",
                },
                {
                    "speaker": "Wicemarszałek Monika Wielichowska",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam pana posła Macieja Wróbla, Koalicja Obywatelska.",
                },
                {
                    "speaker": "Poseł Maciej Wróbel",
                    "content": "Szanowna Pani Marszałek! Panie Premierze! Wysoka Izbo! Przemawiać po pośle Mateckim, który ze słowem „prawda” nie ma nic wspólnego… Słowo „prawda” to jest to słowo, które właściwie określa wystąpienie pana premiera Donalda Tuska. Prawdę państwu dzisiaj powiem. Kiedy w 2016 r. byłem dziennikarzem Telewizji Polskiej, to dostałem wyraźną instrukcję, kogo promować, a na kogo trzeba coś znaleźć. Odszedłem z Telewizji Polskiej i obiecałem sobie jedno: że doprowadzę do sytuacji, w której media publiczne nie będą niczyim politycznym łupem. Bardzo się cieszę, panie premierze, że pan dzisiaj o mediach publicznych w bardzo wyraźnych słowach powiedział. (Oklaski) A ja Wysoką Izbę zostawię ze słowami Andrzeja Poczobuta, polskiego dziennikarza więzionego w białoruskim łagrze, który mawiał: nie mamy wpływu na to, w jakich czasach żyjemy, ale mamy wpływ na to, jak żyjemy w tych czasach. Wiwat koalicja 15 października! (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dzień dobry państwu. Będę prowadził dalej obrady. Bardzo miło. Pani poseł Maja Ewa Nowak, Polska 2050 – Trzecia Droga. Nie ma. Pani poseł Agnieszka Maria Kłopotek, PSL – Trzecia Droga. Zapraszam serdecznie.",
                },
                {
                    "speaker": "Poseł Agnieszka Maria Kłopotek",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! W moim programie wyborczym mówiłam o wzmocnieniu pozycji samorządów jako o bardzo ważnym elemencie. Jako samorządowczyni 9 lat działałam w samorządzie województwa i było dla mnie bardzo ważne, żeby ten temat poruszać. Rządy Prawa i Sprawiedliwości przez 8 lat odbierały po kolei kompetencje samorządom, powodując to, że zmniejszały się dochody własne samorządów, które z dużym trudem radzą sobie w tej chwili ze spinaniem budżetów. I dlatego na przykładzie jednej gminy chcę pokazać, ja wygląda sytuacja z oświatą. W gminie Warlubie, gdzie mój mąż jest wójtem, budżet gminy to 42 mln zł, dochody własne – 14 mln. Koszty oświaty ogółem to 19 mln zł. 45% to są koszty oświaty, w tym wynagrodzenia 11 mln, a subwencja wynosi tylko 7 mln zł. W związku z tym Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 694 gmina musi dopłacać rok w rok kilka milionów złotych do oświaty. (Głos z sali: Nie dopłacać, bo to zadanie własne.) Moje pytanie jest takie, panie premierze: Co pan zrobi, aby zasypać lukę oświatową? Dziękuję.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani posłanka Wanda Nowicka, klub parlamentarny Lewicy. Bardzo proszę, pani posłanko.",
                },
                {
                    "speaker": "Poseł Wanda Nowicka",
                    "content": "Szanowny Panie Marszałku! Szanowny Panie Premierze! Wysoka Izbo! Koalicja 15 października wygrała przede wszystkim dzięki głosom kobiet. Kobiety poszły do wyborów, ponieważ mają ogromne potrzeby, ale też i ogromne oczekiwania, dlatego tak bardzo się cieszę, że w rządzie pana premiera jest reaktywowany urząd do spraw równości kobiet i mężczyzn, a nasza koleżanka klubowa Katarzyna Kotula na pewno będzie pracowała dzień i noc i na pewno zrobi maksymalnie to, co można. Ale jednocześnie chciałabym zapytać pana, panie premierze… Polki, poza tym, że mają wielkie potrzeby, też są bardzo wykwalifikowane, bardzo wykształcone, natomiast ich reprezentacja na wysokich stanowiskach w rozmaitych instytucjach rządowych, podległych rozmaitym (Dzwonek) instytucjom jest bardzo ograniczona albo nie ma ich na kluczowych stanowiskach. Dlatego też pytam pana premiera: Czy można liczyć na to, że np. w instytucjach podległych rządowi, wśród wojewodów, w spółkach Skarbu Państwa, w telewizji publicznej znajdą się kobiety na kierowniczych stanowiskach, a nie wyłącznie na stanowiskach do roboty. Dziękuję bardzo.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, pani posłanko. Pan poseł Grzegorz Adam Płaczek, Konfederacja. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Grzegorz Adam Płaczek",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Szanowny Panie Premierze! 2 lata lockdownu w Polsce to 2 lata bezprawia, deptania praw obywatelskich i nierozliczonych afer. To 2 lata niedziałającego systemu ochrony zdrowia, okres niszczenia polskich firm i nieprzejrzystych zakupów respiratorów, maseczek i szczepionek. To wreszcie gigantyczny wzrost zadłużenia państwa, m.in. w efekcie nieprzejrzystego finansowania szpitali tymczasowych, nielogicznego wypłacania tarcz osłonowych i tworzenia funduszy pozabudżetowych. Konfederacja przygotowała projekt uchwały powołującej komisję śledczą do spraw COVID-19 w celu zbadania i rozliczenia wszystkich nieprawidłowości związanych z okresem pandemii. Kilka dni temu na tej sali osobiście wyraził pan wolę do poparcia tej inicjatywy. W związku z powyższym proszę o informację, czy obecnie już jako premier podtrzymuje pan chęć podpisania projektu uchwały i tym samym poprze pan wraz z Koalicją Obywatelską inicjatywę powołania komisji śledczej do spraw COVID-19. (Dzwonek) Pytanie jest istotne, bowiem projekt uchwały Konfederacji leży na biurku pana klubu i czeka od kilku dni na 28 podpisów, których nam brakuje. Kopię uchwały składam na pana ręce. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Łukasz Kmita, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Łukasz Kmita",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! W regionie, skąd pochodzę, dotychczasowe pana rządy, czyli lata 2007–2014, kojarzą się z biedą, likwidacją, rezygnacją, bezrobociem, upokarzaniem ludzi i głodnymi dziećmi. Ale dotychczasowym symbolem rządów Platformy Obywatelskiej była także wielka, niespotykana nigdy dotąd prywatyzacja – tak naprawdę wyprzedaż majątku narodowego. Gdy Platforma Obywatelska w koalicji z PSL w 2007 r. przejmowała stery w kraju, państwo miało udziały w 1343 przedsiębiorstwach państwowych. Gdy oddawaliście władzę, było ich zaledwie 393. To oznacza, że przez dwie kadencje rząd Platformy Obywatelskiej sprzedał aż 950 spółek. (Dzwonek) Przypominam, że NIK bardzo krytycznie oceniał sposób prywatyzacji. Po pierwszych wycenach spółek zlecano kolejne…",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle.",
                },
                {
                    "speaker": "Poseł Łukasz Kmita",
                    "content": "….które wskazywały na coraz niższą wartość majątku Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 695",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Bardzo proszę, pan poseł Kamil Wnuk, Polska 2050.",
                },
                {
                    "speaker": "Poseł Łukasz Kmita",
                    "content": "I teraz pytanie. (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Panie pośle, nie słychać pana. Minął czas. (Oklaski) (Poseł Monika Wielichowska: Czas minął.) Pan poseł Kamil Wnuk, Polska 2050 – Trzecia Droga. Zapraszam uprzejmie.",
                },
                {
                    "speaker": "Poseł Kamil Wnuk",
                    "content": "Panie Marszałku! Wysoka Izbo! Szanowni Obywatele! Nigdy nie zapominajmy, że małe grupy ludzi zdeterminowanych do wprowadzenia zmian mogą rzeczywiście zmienić cały świat. Słowa te przypominają nam, że każdy z nas, działając indywidualnie, jest w stanie wywrzeć ogromny wpływ na świat, jednak kiedy połączymy indywidualne wysiłki, będziemy działać razem, możemy przekraczać nasze najśmielsze oczekiwania. Pokolenie 15 października pokazało nam, że jest to możliwe. Pozytywne zmiany mogą wpływać na praktycznie wszystkie aspekty naszego życia. Mogą prowadzić do tworzenia bardziej równego i sprawiedliwego społeczeństwa, mogą wpływać na zdrowie publiczne, mogą wpływać na ochronę środowiska naturalnego, ale nie zapominajmy o sprawach najważniejszych, o relacjach międzyludzkich. Pozytywne zmiany mogą tworzyć atmosferę wzajemnego szacunku, zrozumienia, prowadzić do budowania spójnego społeczeństwa i znoszenia podziałów pomiędzy ludźmi. Dlatego, drodzy państwo, niech pozytywne zmiany staną się naszym wspólnym celem i motorem do działania. (Dzwonek) Razem możemy zbudować lepszą przyszłość dla nas wszystkich. Pan prezes Rady Ministrów wspólnie z nowymi ministrami, takimi jak Paulina Hennig-Kloska, Katarzyna Pełczyńska-Nałęcz, Agnieszka Buczyńska wykonają prace dla Polek, Polaków, dla pokolenia 15 października. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Bardzo proszę, pan poseł Wiesław Różyński, PSL – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Wiesław Różyński",
                    "content": "Szanowny Panie Marszałku! Szanowny Panie Premierze! Ja, podobnie jak pan, nie wątpię, że Polska może być lepsza. Mamy też oczekiwania. Od wczoraj co prawda jesteśmy bardziej radośni, bo dokonała się dobra zmiana. Skończyły się czasy, które dewastowały nasze samorządy, ale i nasz kraj, obszary naszego życia prywatnego, zawodowego i ogólnospołecznego. Odchodząca wczoraj władza dokonała wielu zniszczeń. Jednak jako były samorządowiec z ponad 20-letnim doświadczeniem chcę powiedzieć z tego miejsca: Zajmiemy się tym, co zepsute. Przywróćmy podmiotowość i niezależność samorządom, wyrównajmy straty, które poniosły nasze małe ojczyzny, przywróćmy im szacunek, wolność, ale i równocześnie finanse. (Dzwonek) Zadbajmy o dialog i zbudujmy na nowo zaufanie do polskich przedsiębiorców, stwórzmy dla nich przyjazny system podatkowy i regulacyjny.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle.",
                },
                {
                    "speaker": "Poseł Wiesław Różyński",
                    "content": "I w końcu – bo pochodzę z regionu rolniczego – trzeba przywrócić godność rolnikom z polskiej ziemi. Musimy bronić interesów naszych gospodarzy. To nasz obowiązek.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, dziękuję panu bardzo. Pan poseł Tomasz Trela, klub parlamentarny Lewica. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Tomasz Trela",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! 15 października wydarzyła się rzecz wyjątkowa. Blisko 12 mln Polek i Polaków powiedziało „dość” dla rządu Prawa i Sprawiedliwości, „tak” dla nowej, demokratycznej większości. Ja się bardzo cieszę, że pan premier Donald Tusk dzisiaj powiedział o tych kilku ważnych, istotnych konkretach: 30% podwyżki dla nauczycieli, 20% dla sfery budżetowej, druga waloryzacja rent i emerytur w przypadku inflacji 5-procentowej. Ale jeszcze bardziej cieszę się, że po tych 952 dniach, dniach hańby, 952 dniach bez pieniędzy z Krajowego Planu Odbudowy, pan premier Donald Tusk dzisiaj bardzo wyraźnie i bardzo jednoznacznie Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 696 powiedział: Jadę do Brukseli załatwić pieniądze dla Polski, dla przedsiębiorców, dla samorządów, dla obywateli. Panie premierze, dziękuję, trzymam kciuki, bo za to trzymają kciuki wszyscy nasi obywatele. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Ryszard Wilk, Konfederacja.",
                },
                {
                    "speaker": "Poseł Ryszard Wilk",
                    "content": "Dzień dobry. Szanowny Panie Marszałku! Wysoka Izbo! Szanowny Panie Premierze! Z wielkim zainteresowaniem wsłuchiwałem się w pana exposé, doszukując się tam konkretów dotyczących tego, jak będzie się zmieniać sytuacja ekonomiczna Polaków, która jest kiepska. Ostatnio w tej Izbie dyskutowaliśmy np. na temat dopłat z budżetu do cen prądu, do in vitro czy do kredytów i te rzeczy mają wspólny mianownik, czyli biedę. Polacy ubożeją w zastraszającym tempie, a ubożeją dlatego, że PiS wprowadził paskudny mechanizm polegający na tym, że rabuje się Polaków ceną, rabuje się ich podatkami, rabuje się ich parapodatkami, opłatami, a w końcu poprzez spółki Skarbu Państwa, później wydając im resztę w postaci zasiłków. Moje pytanie jest takie: Czy pana rząd ma zamiar kontynuować tę paskudną praktykę, czy może trochę zdejmie obciążenia fiskalne z Polaków, pozwalając im samodzielnie decydować, na co będą wydawać swoje ciężko zarobione pieniądze? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani poseł Anna Krupka, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Anna Krupka",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Mówił pan o mojej dziedzinie – sporcie, aktywności na orlikach. Za pana rządów jedynym turniejem, który odbywał się na orlikach, był turniej orlika o puchar Donalda Tuska. Obiecuje pan program rewitalizacji orlików. My go już wprowadziliśmy, działa od wielu lat, przeznaczyliśmy na niego znaczące środki. Ale orliki mają jedną wadę: nie mają dachu, więc zimą czy w czasie deszczu są bezużyteczne. Dlatego stworzyliśmy program „Olimpia”, program budowy hal przyszkolnych z zadaszeniem o lekkiej konstrukcji. Przeznaczyliśmy na ten cel ponad 1113 mln zł, dzięki czemu w Polsce powstaną 552 takie hale. (Poseł Donald Tusk: A ile powstało?) Jakie konkrety pana rząd zamierza wprowadzić w obszarze sportu? Bo frazesy już znamy. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pani posłanka Klaudia Jachira, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Klaudia Jachira",
                    "content": "Panie Marszałku! Wysoka Izbo! Według PiS-u wszystko, co działo się złego w Polsce, było winą Tuska. Wy nie ponosiliście żadnej odpowiedzialności za swoje nieudolne rządy. Ale przegraliście nie z winy Tuska, tylko dlatego, że Polki i Polacy pokazali wam czerwoną kartkę. A ja czekałam na tę chwilę 8 lat i wierzę, że będę mogła żyć na powrót w normalnym, fajnym kraju. W kraju, gdzie testament szarego człowieka zostanie wypełniony – panie premierze, dziękuję, że on dziś wybrzmiał z tej mównicy. W kraju, gdzie nie od razu wszystko będzie idealnie, bo jest wiele do posprzątania po tych szkodnikach i poprzednikach, ale będziemy zmierzać znów w dobrym kierunku silnej Europy, praw człowieka, w tym kobiet, w stronę zielonych wartości, czyli ochrony środowiska i klimatu. Wierzę, że pogodzimy się z sąsiadami (Dzwonek), że media publiczne będą objaśniać i informować, a ludzie na ulicy będą się częściej uśmiechać. I to wszystko to będzie zasługa koalicji 15 października i zasługa, a nie wina, premiera Donalda Tuska. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Rafał Kasprzyk, Polska 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Rafał Kasprzyk",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! Nawiązuję do słów mojej koleżanki. Tak, wczoraj i dzisiaj ziszcza się marzenie Polaków i nadzieja wyrażona najważniejszym sondażem opinii publicznej 15 października przy urnach. Tworzymy historię i jesteśmy z tego powodu szczęśliwi. Nie mamy planety B – to stwierdzenie faktu. A katastrofa ekologiczna, klimatyczna to efekt naszego rabunkowego zarządzania zasobami naturalnymi. Harwestery wycinają nasze drzewa, nasze lasy, o czym pan Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 697 premier mówił, w ciągu kilku minut. Jako Polska 2050 wnosiliśmy i wnosimy o powiększenie obszaru parków narodowych, a także o objęcie 20% najcenniejszych obszarów leśnych całkowitym zakazem wycinki drzew. Panie premierze, czy będzie pan dalej wspierał naszą ambitną politykę klimatyczną w tym zakresie, aby zapewnić naszym wnukom i dzieciom czyste powietrze, zdrową żywność i dobre życie? (Dzwonek) I czy dołoży pan wszelkich starań, aby przywrócić narodowi obszar wyłączony z granic Świętokrzyskiego Parku Narodowego wbrew ustawie o ochronie przyrody? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pani poseł Urszula Nowogórska, PSL – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Urszula Nowogórska",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! Jestem w okręgu nr 14, czyli Limanowa, Sącz, Gorlice, Nowy Targ, Zakopane. Piękne rejony Polski, gdzie mieszkają życzliwi, pracowici ludzie, ale potrzebujemy otwarcia komunikacyjnego. Dlatego, panie premierze, moje pytanie to zarazem prośba. Potrzebujemy obwodnicy Limanowej, potrzebujemy otwarcia komunikacyjnego na drodze nr 28, która jest zablokowana w Kasinie Wielkiej. Potrzebujemy sądeczanki, kontynuacji linii Piekiełko – Podłęże, sprawnej komunikacji na Podhalu. To są dla nas najważniejsze cele, żeby Polakom u nas, w Małopolsce, żyło się bezpiecznie, sprawnie i żeby mieli równe szanse na rozwój i wzmocnienie potencjałów lokalnych. Bardzo dziękuję. (Oklaski) (Głos z sali: Wszystko było w exposé Mateusza Morawieckiego.)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani posłanka Joanna Scheuring-Wielgus, klub parlamentarny Lewicy. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Joanna Scheuring-Wielgus",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Słuchając pana exposé dzisiaj, zapisałam sobie dwa słowa, które – uważam – są dla mnie kluczowe: wspólnota, budowanie wspólnoty – i cieszę się, że to pana exposé właśnie w tym duchu dzisiaj było – ale też poprawa jakości życia Polek i Polaków. Uważam, że to jest ważne. I nie zważając na to, co mówi prawa strona, ten styl mówienia do ludzi i dla ludzi uważam za taki bardzo budujący. Wiele osób zadających pytanie, jak zauważyłam, kiedy słuchałam tutaj, mówiło: jestem z regionu, jestem z miasta. Ja jestem z Torunia, z miasta, które jest miastem Kopernika, pierników, Lindy, Szapołowskiej, Organka, Republiki. Mówię o tym, ponieważ mam nadzieję, że jako koalicja październikowa zakręcimy kurek dla pewnego prezesa, który z Torunia bardzo dużą kasę czerpał przez ostatnie 8 lat. Mówię o tym też dlatego, że w trakcie kampanii wyborczej zarówno moja formacja (Dzwonek), jak i państwa formacja mówiły dużo o świeckim państwie. Tu nie chodzi o rewolucję, ale chodzi o to, żeby pochylić się nad tym, żeby oddzielić państwo od Kościoła i zrobić to naprawdę dobrze. Mam nadzieję, że to się wydarzy. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Bartłomiej Pejo, Konfederacja.",
                },
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "Panie Marszałku! Szanowny Panie Premierze! Jedną z najbardziej gnębionych grup społecznych w ostatnim czasie stali się polscy kierowcy. Wysokie ceny paliw, absurdalne stawki mandatów, podatki na auta spalinowe i strefy wykluczenia transportowego w miastach. To pana partia poparła projekt ustawy o elektromobilności, który pozwolił prezydentowi z pana partii, panu prezydentowi Rafałowi Trzaskowskiemu, wprowadzić strefę czystego transportu w Warszawie. Pytam zatem w imieniu milionów kierowców, co zamierza pan premier dla nich zrobić. Czy zmotoryzowani w dalszym ciągu będą wypychani z miast i uderzani kolejnymi opłatami, ci najmniej zamożni, których nie stać na modne, nowe elektryki? Czy kierowcy będą mogli w końcu swobodnie, sprawnie i bezpiecznie poruszać się po polskich drogach, dojeżdżać do pracy i dowozić swoje pociechy do szkół? Mam dla pana pierwszy konkret do rozwiązania. Od stycznia na stacjach paliw pojawi się nowe paliwo E10 (Dzwonek) zamiast znanej dziewięćdziesiątki piątki. To paliwo nie jest kompatybilne ze starszymi autami spalinowymi.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 698",
                },
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "To uderzenie w miliony Polaków. Proszę odpowiedzieć, co pan w tej kwestii jest w stanie zrobić, czy ewentualnie pan premier jest w stanie przedłużyć okres obowiązywania na kolejne lata, żeby nie obowiązywało to od roku 2024, jak zaproponowano… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) (Głos z sali: Tak jest.)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Panie pośle, panie pośle, dziękuję serdecznie. Pan Paweł Szefernaker, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Paweł Szefernaker",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Demokracja polega m.in. na tym, że co jakiś czas następuje zmiana władzy. W demokratycznych wyborach 15 października Prawo i Sprawiedliwość zdobyło najwięcej głosów. 7 640 854 osoby zagłosowały na Prawo i Sprawiedliwość. Każdy z tych głosów wynikał z konkretnych powodów. Chcę zadeklarować, że będziemy stali na straży każdej sprawy, jaka była ważna dla Polaków, którzy oddali głos na PiS. Chcę tutaj jasno zadeklarować: będziemy pracowitą i skuteczną opozycją, nie przegapimy żadnego waszego kłamstwa, z każdej obietnicy będziemy was rozliczać. W parlamencie reprezentuję województwo zachodniopomorskie, które dzięki rządom Prawa i Sprawiedliwości jest dziś jednym wielkim placem budowy. Wiele rozpoczętych inwestycji w Szczecinie, Koszalinie, w innych, mniejszych miejscowościach popegeerowskich. Będziemy opozycją, która (Dzwonek) będzie pilnowała, aby pana rząd dokończył każdą tę inwestycję. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Michał Szczerba, Koalicja Obywatelska.",
                },
                {
                    "speaker": "Poseł Michał Szczerba",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Wszyscy w różnych formatach w zgromadzeniach parlamentarnych walczymy o dobrą opinię o Polsce. Zależy nam na rzetelności życia publicznego, uczciwości i wysokich standardach. Afera wizowa była jedną z najbardziej bezczelnych, bo zniszczyła wizerunek kraju, bo podała w wątpliwość sprawczość państwa i podważyła zaufanie sojuszników, a obietnica PiS-u o bezpieczeństwie granic okazała się fałszem i pozorem, potwierdziła, że państwo i instytucje nie tylko nie działają, ale też są w totalnym rozkładzie. Państwo zdradziło i zwróciło się przeciwko własnym obywatelom. To zdrada obywateli i ich bezpieczeństwa. Jedynym kryterium weryfikacji stała się łapówka. Jednocześnie forsowano regulacje, by scentralizować decyzje wizowe w rękach ministra i jego centrum. Ta sprawa musi być wyjaśniona i rozliczona (Dzwonek), a społeczeństwo musi poznać prawdę, jak bardzo państwo PiS zawiodło. Instrumentem do wyjaśnienia tego procederu, zorganizowanego procederu zdegenerowanych ludzi władzy, może być komisja śledcza. Władza, nie reagując, świadomie przyzwalała na jego rozwój.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję.",
                },
                {
                    "speaker": "Poseł Michał Szczerba",
                    "content": "Panie Premierze! Krótkie pytanie: Jaka jest rola komisji śledczych w zakresie stworzenia również instrumentów i standardów bezpieczeństwa na przyszłość? Bardzo dziękuję. (Poseł Łukasz Kmita: Panie marszałku, to jest jakiś skandal.)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję, dziękuję panie pośle. Proszę pana, skandalem to było to, co robił poprzedni marszałek Sejmu Ryszard Terlecki… (Poseł Łukasz Kmita: Nie wiem, jestem pierwszą kadencję. Niech pan nie idzie w tę stronę.) …który zresztą tutaj siedzi. (Poseł Łukasz Kmita: Wszystkich należy traktować tak samo.) W związku z tym, ponieważ wszystkich należy traktować tak samo, niech pan zajmie miejsce. (Oklaski) (Poseł Łukasz Kmita: Oczywiście, zwracam panu marszałkowi uwagę.) Pan poseł Piotr Paweł Strach, Polska 2050. Proszę pana, za zwrócenie uwagi panu serdecznie dziękuję. I serdecznie pana pozdrawiam. (Poseł Łukasz Kmita: Również, również.) Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Piotr Paweł Strach",
                    "content": "Panie Marszałku! Panie Premierze! Wiemy, jak w poprzedniej kadencji PiS traktował samorządy. Znamy tę politykę papierowych czeków. Chciałbym prosić nowego premiera, nowy rząd o to, aby docenił ambitne samorządy. Jednym z takich ambitnych samorządów jest Częstochowa. (Głos z sali: A które nie są ambitne?) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 699 Jest w nim duży problem dotyczący stadionu. Chciałbym, aby nowy rząd wsparł Częstochowę w rozbudowie dotychczasowego miejskiego stadionu dla Rakowa Częstochowy. Chodzi o to, żeby nie było tak, że mecze w ramach Ligi Mistrzów czy europejskich pucharów nie mogą się odbyć w macierzystym mieście klubu. Drugim takim ambitnym miastem są Gliwice. Miasto chce wybudować olbrzymi szpital dla prawie 300 tys. ludzi. Chodzi o szpital przy ul. Kujawskiej w Gliwicach. Również proszę o to, aby przyszły rząd wsparł Gliwice w tym ambitnym zadaniu. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Władysław Bartoszewski, PSL – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Władysław Bartoszewski",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! Po brutalnej agresji Rosji na Ukrainę zmieniła się zupełnie sytuacja geopolityczna. Dzięki temu nieszczęściu Polska uzyskała szansę jedną na pokolenie. Chodzi o naszą rolę na wschodniej flance NATO, fantastyczne zachowanie naszego społeczeństwa podczas kryzysu uchodźców, w którym 5 mln uchodźców przeszło przez naszą granicę i zostało zaopiekowanych. Ta szansa została kompletnie zmarnowana przez rząd Prawa i Sprawiedliwości, rząd Mateusza Morawieckiego, który reagował w sposób wyłącznie pasywny, krytycznie podchodził do Unii Europejskiej i niczego nie proponował. Moje pytanie: W jakich obszarach przewiduje pan premier inicjatywy Polski w Unii Europejskiej? Chodzi o to, żeby Unia dyskutowała o naszych projektach i naszych propozycjach, a nie o to, żebyśmy reagowali negatywnie i wyłącznie krytycznie na to, co proponują nam inni. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani posłanka Anita Kucharska-Dziedzic, klub parlamentarny Lewica. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Anita Kucharska-Dziedzic",
                    "content": "Panie Marszałku! Panie Premierze! Ja z ogromną prośbą i apelem. Od 1 października Unia Europejska jest stroną konwencji stambulskiej. Zostało nam kilka tygodni na przygotowanie unijnej dyrektywy przeciwprzemocowej, która ma implementować owo prawo konwencyjne do prawa unijnego. Polska pod wodzą Morawieckiego i Ziobry sprzeciwiła się tej dyrektywie, zwłaszcza art. 5, który implementuje art. 36 konwencji stambulskiej. Chodzi o zmianę definicji zgwałcenia blokowaną przez parlament IX kadencji. Apeluję i bardzo proszę pana premiera o wycofanie tego sprzeciwu, zwłaszcza że zostało nam ledwie kilka tygodni na wycofanie tego sprzeciwu. Mam nadzieję, że w tej, w X kadencji zmienimy w polskim parlamencie definicję zgwałcenia. Projekt przygotowany przez (Dzwonek) mecenas Wawrowską z Koalicji Obywatelskiej i złożony przeze mnie i klub Lewicy leży nadal w polskim parlamencie. Dziękuję ślicznie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Witold Tumanowicz, Konfederacja. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Witold Tumanowicz",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Który to już raz Polacy muszą słuchać pana exposé? Znamy te rządy, a Polacy poznali zapach gazu, poznali pałkę, poznali kopniaki policyjne, poznali także swąd palonej budki. Powiedział pan, że ma pan sposoby na rozwiązanie problemów na granicy. Mam nadzieję, że to nie jest właśnie Policja, że to nie są pałki i gaz, bo właśnie w tym momencie te protesty są pacyfikowane. To polscy obywatele i polski interes powinny być dla nas priorytetem, a nie ci ludzie, których trzeba spacyfikować. Premier Ukrainy gratulował panu i liczył na nowy rozdział w relacjach polsko-ukraińskich. Teraz jest bardzo jasne pytanie: Czy można być bardziej spolegliwym wobec Ukrainy niż był PiS? Mam nadzieję, że pan nie będzie chciał ich pobić. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Myślę, że pan premier Donald Tusk nie będzie chciał nikogo pobić. Zbigniew Bogucki – pan poseł z Klubu Parlamentarnego Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Zbigniew Bogucki",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoki Sejmie! Panie premierze, patrzę panu prosto w oczy i zadaję panu takie pytanie. Najprawdopodobniej jeszcze dzisiaj zostanie wybrany pana rząd w demokratycznej procedurze, zgodnie z konstytucją, a pan wiele razy w tej kampanii, również wcześniej, okłamywał Polaków, okłamywał naród, że w Polsce nie Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 700 ma demokracji. Czy w tym kontekście pan wstydzi się tych słów? Czy pan za te słowa przeprosi? Druga kwestia, związana z pana exposé. W tym exposé moim zdaniem w sposób niegodny przywołał pan tragedie konkretnych ludzi. Wykorzystał je pan politycznie. Ale zapomniał pan o jednej tragedii, o tragedii działacza Prawa i Sprawiedliwości, który został zamordowany właśnie w akcie takiej nienawiści politycznej. A teraz w sprawie mojego Pomorza Zachodniego i mojego kochanego Szczecina. Zachodnia obwodnica Szczecina. Kiedy pan był premierem, pana minister, pan Nowak, mówił, że nie mam miejsca w planach budowy dróg krajowych i autostrad dla tej trakcji. Pana doradca, pan Bielecki (Dzwonek), mówił, że to lokalna fanaberia. Czy pan będzie kontynuował tę inwestycję, którą my rozpoczęliśmy? Co z portem instalacyjnym? Co z portem kontenerowym w Świnoujściu? Co z Odrzańską Drogą Wodną? Co z drogą S10?",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie.",
                },
                {
                    "speaker": "Poseł Zbigniew Bogucki",
                    "content": "Te wszystkie projekty rozpoczęliśmy. Czy pan je będzie kontynuował? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Wie pan, panie pośle, miałem taką pokusę, żeby przedłużyć panu wypowiedź, ale ponieważ koleżanki i koledzy z pana klubu prosili, żebym pilnował czasu, to dlatego skróciłem. (Poseł Zbigniew Bogucki: A ja się zmieściłem, panie marszałku.) No nie, nie zmieścił się pan, bo było 15 sekund dłużej. Pan poseł Piotr Adamowicz, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Piotr Adamowicz",
                    "content": "Dziękuję. Panie Marszałku! Panie Premierze! Pytanie o politykę historyczną pańskiego gabinetu. Po 2015 r. obóz PiS zdecydowanie zintensyfikował politykę historyczną, którą należy zdefiniować jako pisanie historii na nowo. Pisanie historii na nowo to nie tylko apologia żołnierzy wyklętych, wieńce na grobach żołnierzy Brygady Świętokrzyskiej czy osławiony podręcznik do HiT-u. To również setki milionów pompowanych w przeróżne słuszne historycznie projekty. Miało w tym ważny udział Ministerstwo Kultury i Dziedzictwa Narodowego. Nie mamy tu czasu na szczegółowe wyliczenia, dlatego przywołam dwa przykłady polityki historycznej à la PiS z pańskiego, panie premierze, i mego Gdańska: przejęcie Muzeum II Wojny Światowej, zmiana wystawy stałej, wreszcie nacjonalizacja należącej do miasta części Westerplatte. Skoro nie dało się przejąć Europejskiego Centrum Solidarności, to w 2018 r. obcięto dotację dla ECS o 3 mln zł, a następnie wraz z zaprzyjaźnioną (Dzwonek) z PiS-em „Solidarnością” utworzono Instytut Dziedzictwa Solidarności, na który z pieniędzy podatników ministerstwo przeznaczyło ponad 9 mln zł. Dziękuję uprzejmie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Łukasz Osmalak, Polska 2050 – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Łukasz Osmalak",
                    "content": "Panie Marszałku! Wysoka Izbo! Szanowni Obywatele! Panie Premierze! Dzisiaj mamy dobry dzień. Mamy dobry dzień dlatego, że po 8 latach rządów, można by powiedzieć: po 8 latach psucia Polski, nadchodzi ten moment, kiedy w końcu zaczniemy naprawiać. Jak wszyscy dobrze wiemy, naprawianie nigdy nie jest proste. Zawsze jest to proces w mniejszym czy większym stopniu skomplikowany. Ale my wiemy, że musimy to zrobić, dlatego że robimy to dla naszych dzieci i wnuków. My nie będziemy traktować Polski jak dojnej krowy, dlatego że zdajemy sobie sprawę z tego, że to nie Polska i nie obywatele są dla nas, tylko to my jesteśmy dla Polski i dla obywateli. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Adam Dziedzic, PSL – Trzecia Droga. Jest pan poseł? Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Adam Dziedzic",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Bardzo się cieszę, że doczekałem takiego dnia, w którym – albo od którego, jak mniemam – skończy się wreszcie ograniczenie autonomii samorządów, że polski bałagan, bo na pewno nie ład, który został wprowadzony za PiS-u i praktycznie rozwalił finanse samorządów, wreszcie się zakończy, że zakończy się wreszcie nakazowo rozdzielcze przekazywanie środków finansowych do tych samorządów, które z wami tylko chciały współpracować i które PiS… (Głos z sali: Nieprawda!) Oczywiście tak było. (Głos z sali: Kłamiesz!) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 701 Spokojnie, spokojnie. Myślę, że będziemy to mogli wreszcie kiedyś zobaczyć. Bardzo dziękuję. Panie Premierze! Miałbym prośbę dla Podkarpacia. Na Podkarpaciu ma powstać uniwersytecki szpital kliniczny, olbrzymia inwestycja, 17 klinik, gdzie samorząd gminy Świlcza przekazał nieodpłatnie prawie 40 ha gruntu pod tę inwestycję. Liczę, że to powinno ruszyć (Dzwonek) pełną parą. Bardzo proszę też o to, aby wykluczenie komunikacyjne z tych ostatnich kilku lat rządów PiS wreszcie się zakończyło dla mieszkańców. To ważne, żeby Polki i Polacy mieli jak dojechać do szkoły czy do miejsca pracy. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Krzysztof Śmiszek, klub parlamentarny Lewica.",
                },
                {
                    "speaker": "Poseł Krzysztof Śmiszek",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! Ostatnie lata to nie tylko czas rozwalania praworządności w Polsce. To również rozwalenie i upolitycznienie Trybunału Konstytucyjnego, rozwalenie Krajowej Rady Sądownictwa, upolitycznienie Sądu Najwyższego, przynajmniej jego części, a także upolitycznienie prokuratury. Tej pracy będzie całe mnóstwo. Ale trzeba pamiętać jeszcze o jednym. Prawo i Sprawiedliwość z języka nienawiści, pogardy, rasizmu, homofobii, ksenofobii uczyniło sobie narzędzie robienia polityki. Jednym z największych i najważniejszych zadań nowego rządu powinno być wyeliminowanie języka pogardy z przestrzeni publicznej. W umowie koalicyjnej mamy zapis mówiący o tym, że w tym zakresie będzie potrzeba znowelizowania Kodeksu karnego. Dzisiaj także bardzo ważny dzień, bo Europejski Trybunał Praw Człowieka wydał bardzo ważne orzeczenie. Uznano, że Polska poprzez brak jakiejkolwiek ustawy legalizującej pożycie par jednopłciowych łamie prawa człowieka. Tych (Dzwonek) zadań przed nowym rządem jest bardzo, bardzo wiele. Ostatnie 8 lat było czasem pogardy. Niech najbliższe 4 lata będą czasem praw i wolności obywatelskich. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Andrzej Tomasz Zapałowski, Konfederacja. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Andrzej Tomasz Zapałowski",
                    "content": "Panie Marszałku! Panie Premierze! Powiedział pan, że będzie pan chciał koordynować ochronę granic w Europie i że ochrona granic na Wschodzie będzie szczelna. Panie Premierze! Moje pytanie: Kim pan chce to zrobić? W początkowym okresie kryzysu białoruskiego użyto 1/3 wojsk lądowych operacyjnych i terytorialnych. W razie masowej imigracji z Bliskiego Wschodu – 500 km granicy z Ukrainą, 500 km granicy ze Słowacją. W tej chwili mamy 60% wypełnionych etatów wojsk operacyjnych, a Wojska Obrony Terytorialnej to zaledwie trzydzieści parę tysięcy żołnierzy, na których nałożono gorset prawny wojsk operacyjnych. Są one skonstruowane na wzór wojsk wewnętrznych. Nie jest to absolutnie do wykonania, żeby coś takiego się stało. Dlatego, panie premierze, spytam jeszcze o jedną rzecz. Państwa koalicjant, Lewica, chce otwartych (Dzwonek) granic i przyjmowania wszystkich: Co pan z tym zrobi? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Myślę, że nie wczytał się pan dokładnie w program Lewicy w tej sprawie. Ale po posiedzeniu bardzo chętnie pana poinformuję, panie pośle. (Poseł Andrzej Tomasz Zapałowski: Poproszę, chętnie przeczytam.) Pan poseł Władysław Dajczak, Klub Parlamentarny Prawo i Sprawiedliwość. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Władysław Dajczak",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Panie premierze, rozpoczynając swoje dzisiejsze exposé, powiedział pan, że pana pierwsze exposé wygłoszone 8 lat temu zapamiętano z tego, że trwało 3 godziny. Dzisiejsze zostanie zapamiętane z tego, że trwało trochę krócej, bo niespełna 2,5 godziny. Mało konkretów, półprawdy, kłamstwa i zaklinanie rzeczywistości. Dużo też pan mówił o konkretach i o wiarygodności. Chcę panu zacytować zdanie z pana wystąpienia na jednym z wieców wyborczych: W ciągu pierwszych 100 dni przeprowadzimy zmianę absolutnie zasadniczą. Każdy emeryt, każda emerytka, którzy mają emeryturę do 5 tys. zł, nie będą płacili podatku. Każdy tydzień zwłoki jest niebezpieczny dla ich życia. I panie premierze, pan mówi teraz, że w ciągu tych 100 dni nie uda się tego przeprowadzić, bo rok podatkowy. Jest przy panu przyszły minister finansów. Odpowiedzcie tym 5 mln, kilku milionom emerytów, kiedy to zostanie wykonane, skoro jest pan wiarygodny i powiedział pan też, że takie deklaracje składają tylko ludzie wiarygodni. Czekamy (Dzwonek) na pana wiarygodność. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani poseł Marta Golbik, Koalicja Obywatelska Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 702",
                },
                {
                    "speaker": "Poseł Marta Golbik",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Panie Premierze! Lata rządów PiS-u to nie tylko dewastacja wszystkich instytucji państwowych, ale też dewastacja młodych ludzi na polu emocjonalnym, to lęk, niepokój, niepewność, obawa o przyszłość, lęk przed systemem szkolnictwa, to emocje, które towarzyszyły najmłodszym, które niewątpliwe odcisnęły swoje piętno na długie lata. To także telewizja publiczna, wypowiedzi polityków, szczucie, stygmatyzowanie, również przez ministra edukacji, który miał pomagać tym młodym ludziom. Poza tym wszystkim PiS przez te lata oszukiwał zarówno dzieci w kryzysach psychicznych, jak i ich rodziców. Psychiatria zupełnie nie była finansowana i leżała odłogiem, była w ostatnim kręgu zainteresowania młodych ludzi. W końcu PiS zlikwidował telefon alarmowy (Dzwonek) dla najmłodszych: 116 111. Moje pytanie brzmi: Czy rząd pana premiera przywróci finansowanie telefonu zaufania dla dzieci i młodzieży? Czy zadba o zdrowie psychiczne najmłodszych? Bardzo dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Marcin Skonieczka, Polska 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Marcin Skonieczka",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Jest 11 590 090 powodów, dla których większość posłanek i posłów na tej sali poprze dzisiaj wniosek premiera Donalda Tuska o wybór Rady Ministrów. Jest tyle powodów, bo tyle Polek i Polaków zagłosowało na trzy komitety, które zadeklarowały, że wspólnie utworzą demokratyczny rząd. Każda z tych osób, które głosowały, miała konkretny powód i konkretną nadzieję, że po wyborach coś się zmieni. Naszym najważniejszym zadaniem na dziś i na kolejne 4 lata jest udowodnienie, że nie zawiedziemy tego zaufania. Wzięliśmy na siebie wielką odpowiedzialność i jestem przekonany, ze uda nam się ją udźwignąć. Dzięki naszej wspólnej pracy Polska stanie się prawdziwą wspólnotą, wspólnotą ludzi zdrowych, szczęśliwych, różnych, ale dbających o dobro wspólne, ludzi, którzy myślą o przyszłości, o następnych pokoleniach i (Dzwonek) potrafią rozwiązywać nawet najtrudniejsze problemy. Tego wszystkiego nam życzę. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Mirosław Adam Orliński, PSL – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Mirosław Adam Orliński",
                    "content": "Szanowny Panie Marszałku! Szanowny Panie Premierze! Wysoka Izbo! Bardzo się cieszę, że pan premier Donald Tusk w swoim exposé nawiązał do Centralnego Portu Komunikacyjnego, do inwestycji, która u mnie, w części mojego powiatu, powiatu sochaczewskiego, była od 2017 r. ogłaszana jako największa inwestycja, która ma być zbawieniem dla mieszkańców, a tak naprawdę nikt z tymi mieszkańcami nigdy o tym nie rozmawiał. Kiedy w 2017 r., już wtedy byłem radnym sejmiku, spotykałem się z tymi mieszkańcami, przyjechał pan Wild, który wtedy był ministrem, a teraz jest prezesem spółki CPK. Mówił, że to lotnisko musi powstać. To brak argumentacji, brak rozmów ze społeczeństwem. Te prace bardzo przyspieszyły w ostatnim czasie, tak jak pan premier wspominał. Te spotkania z mieszkańcami pokazały, że kilka spółek, nawet te tworzone przez CPK, można powiedzieć, robiło to w niesprawiedliwy sposób, w sposób niegodny. Chodzi o podchody, zastraszanie mieszkańców, żeby wywłaszczyć te tereny. Warto zaznaczyć, że są to najlepsze (Dzwonek) tereny rolnicze w Rzeczypospolitej Polskiej. Panie Premierze! Mam nadzieję, że ten pełnomocnik, który będzie zajmował się sprawami CPK, dokona zatrzymania i wyjaśni te wszystkie sprawy. Apeluję także o wzmocnienie samorządów i samorządu terytorialnego. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Marcin Kulasek, Koalicyjny Klub Parlamentarny Lewicy. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Marcin Kulasek",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! W Polsce brakuje 1 mln mieszkań na rynku wtórnym i 1 mln mieszkań na rynku pierwotnym. 60% Polaków w wieku 25–29 lat mieszka ze swoimi rodzicami. Przez 8 lat PiS nie wybudował akademików. Studenci są w wyjątkowo trudnej sytuacji. Obecnie ok. 66% Polaków nie ma zdolności kredytowej, a najem mieszkań na rynku prywatnym bardzo często pochłania ponad 50% dochodów. Rynek nie rozwiązał problemu mieszkaniowego. Z każdym rokiem coraz mniejsza liczba rodzin będzie mogła liczyć na rozwiązania rynkowe, dlatego obok rozwiązań, które wspierają rodziny, które chcą i mogą zdecydować się na kredyt hipoteczny, potrzebne są też działania wspierające budownictwo na wynajem. Panie Premierze! Wierzę, że taka będzie polityka nowego rządu, bo łączy nas przekonanie, że zarówno mieszkanie, jak i akademik są prawem, a nie tylko towarem. To nasze zobowiązanie wobec wyborców. (Dzwonek) Nie pytam, bo jestem przekonany, że wywiążemy się z tego zobowiązania. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 703",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Roman Fritz, Konfederacja. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Roman Fritz",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! Nie ma osoby poselskiej. Panie premierze, nie ma czegoś takiego jak bezpieczna aborcja. O czym pan mówił? Dla kogo to dzieciobójstwo ma niby być bezpieczne? Dla mordowanego dziecka? Kolejne pytanie dotyczy ministra Bodnara. W czerwcu 2017 r. jako rzecznik praw obywatelskich powiedział, że naród polski uczestniczył w realizowaniu Holokaustu, a w październiku 2021 r. porównał Polaków do zwierząt i prosił, żeby Niemcy uaktywnili działania przeciwko Polsce. Czy ktoś taki ma moralne kompetencje do sprawowania urzędu ministra sprawiedliwości? Kolejne pytanie dotyczy podatku VAT. Dziś mija 10 lat od wprowadzenia przez pana rząd podwyżek do 23% na 2 lata. Kiedy pan to obniży? Mam kolejne pytanie: Czy serio wierzy pan w te wierutne bzdury pseudoreligii marksizmu i klimatyzmu? Mam prośbę – porzućmy łamańce językowe, słowo: ministra (Dzwonek) nie istnieje. Z panem Bogiem. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pozdrawiam pana serdecznie w imieniu niejednej ministry przyszłego rządu. (Oklaski) Pan poseł Bartosz Józef Kownacki, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Bartosz Józef Kownacki",
                    "content": "Dziękuję. Panie Premierze Koalicji Ośmiu Gwiazdek! Pana partyjny kolega, poseł Suski, kiedy tworzono WOT, mówił, że to będzie prywatna armia Macierewicza. Podobnie mówili pana partyjni koledzy i koleżanki. Pan również nie pałał sympatią do polskiego munduru, kiedy w trakcie kampanii wyborczej straszył pan, że PiS wyprowadzi wojsko na ulice. Jak pan widzi, tak się nie stało, bo szanujemy wyroki demokracji, choćby były dla nas niebywale bolesne. (Głos z sali: Proszę uważać.) Kiedy mówił pan te słowa, bądź cynicznie manipulował pan opinią publiczną, w co nie wierzę, bo tak doświadczony, inteligentny polityk nie musi zniżać się do tak prymitywnego poziomu, bądź też drzemie w panu głęboka fobia przed polskim mundurem. Może dobrze, że ministrem obrony zostaje lekarz, bo może pana z tej fobii wyleczy. Już zadaję pytanie. Czy przyzna pan, że po tej krótkiej, kilkudniowej terapii popełnił pan błąd, będąc premierem w latach 2007–2014, kiedy miliardy złotych przeznaczone na modernizację polskiej armii wracały do budżetu centralnego i nie przyczyniały (Dzwonek) się do budowy polskiej armii? (Głos z sali: Nieprawda.) Czy daje pan gwarancję, że w tej kadencji wszystkie pieniądze przeznaczone na modernizację polskiej armii zostaną wykorzystane? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Krzysztof Habura, Koalicja Obywatelska.",
                },
                {
                    "speaker": "Poseł Krzysztof Habura",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Dziś wieczorem wybierzemy nowy rząd. To ważna chwila i ważny dzień, ale to 11 grudnia był jednym z najważniejszych i najradośniejszych dni w historii Polski po 1989 r. Wczoraj, wypełniając wolę milionów wyborców, odsunęliśmy złą władzę PiS-u. (Oklaski) Wczoraj na premiera wybraliśmy pana Donalda Tuska, męża stanu, prawdziwego przywódcę, patriotę… (Oklaski) (Głos z sali: Ooo…) …który po wypełnieniu ważnej misji w Unii Europejskiej cała swoją energię skierował na to, aby przywrócić w Polsce demokrację, praworządność, przyzwoitość, a także szacunek do konstytucji i do drugiego człowieka. Donald Tusk, nasz premier, jest gwarantem tego, że zło poprzedniej władzy zostanie rozliczone, Polska naprawiona, a pogodzeni Polacy znów usiądą (Dzwonek) przy wspólnym stole. Panie premierze, dzięki panu w sercach milionów Polaków znów zagościły radość, nadzieja i wiara, że będziemy żyli w normalnym europejskim kraju. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Michał Gramatyka, Polska 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Michał Gramatyka",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! Panie premierze, pańscy poprzednicy w 2018 r. zaprezentowali program dla Śląska. Obiecali złote góry dla mojego regionu, nad kopalnią Krupiński miały latać drony i eksperymentować, miały powstać elektrownie fotowoltaiczne między CzelaPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 704 dzią a Będzinem. Nie obiecali chyba tylko wiatraków, bo boją się wiatraków jak Don Kichot z La Manchy.",
                },
                {
                    "speaker": "Panie premierze, wierzę w pana. Mam jedną prośbę",
                    "content": "proszę nas, Ślązaków, traktować poważnie. Proszę o uznanie dla śląskiej godki, dla języka śląskiego, którym posługuje się 600 tys. osób w naszym regionie. Proszę o to, aby województwo śląskie było oczkiem w głowie pańskiego rządu. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Michał Pyrzyk, PSL – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Michał Pyrzyk",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! Niezmiernie mnie cieszy bardzo ważne miejsce dla spraw samorządowych, dla spraw lokalnej Polski zarówno w exposé pana premiera, jak i w hierarchii zagadnień koalicji 15 października. Cieszy mnie deklaracja dotycząca decentralizacji ustrojowej i deklaracja współpracy, ale partnerskiej współpracy, z samorządami – nie współpracy opartej na zasadzie klientyzmu czy jakichś nieformalnych układach zależności… (Głos z sali: Panie pośle, niech pan nie narzeka. Było dobrze.) Było dobrze, natomiast partnerstwo i równość w tych relacjach muszą wrócić. Samorządy jak czystego powietrza potrzebują natychmiast i środków z Krajowego Planu Odbudowy i zwiększenia subwencji oświatowej… (Głos z sali: Niech pan powie, ile dostał kasy.) …zwłaszcza w kontekście proponowanych podwyżek dla nauczycieli, rozciągnięcia tej subwencji na przedszkola, pełnego pokrycia (Dzwonek) zadań zleconych z zakresu administracji rządowej, tak aby wójtowie, burmistrzowie, starostowie mogli skutecznie realizować wszystkie swoje zadania nie tylko w Słupcy i nie tylko w Koninie, o których pan premier również wspomniał w swoim exposé. Dziękuję bardzo. (Oklaski) (Głos z sali: Ale Dolata mówi, że pan dostał dużo kasy.)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Panie pośle, czy pan się zapisał do głosu? To niech pan cierpliwie poczeka. Dobrze? Super. Pani posłanka Katarzyna Ueberhan, klub parlamentarny Lewica.",
                },
                {
                    "speaker": "Poseł Katarzyna Ueberhan",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! 15 października wybraliśmy Polskę, wybraliśmy Polskę demokratyczną, praworządną, sprawiedliwą, wolną i równościową. Przed nowym rządem i ministrą do spraw równości stoją ogromne wyzwania. Likwidacja nierówności, asystencja dla osób z niepełnosprawnością, likwidacja luki płacowej czy równość małżeńska to tylko niektóre z nich. Dziś w Strasburgu zapadł wyjątkowy, historyczny wyrok, wyrok, który daje nadzieję wszystkim osobom, wszystkim parom jednopłciowym w naszym państwie na to, że w końcu będą mogli zalegalizować swój związek. Z tego miejsca proszę, pamiętajmy, by związki partnerskie wreszcie stały się też polską rzeczywistością. (Dzwonek) Równość małżeńska to standard w XXI w., równość dla wszystkich to równość w różnorodności. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Przemysław Wipler, Konfederacja. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Przemysław Wipler",
                    "content": "Dziękuję. Panie Premierze! Polska potrzebuje 300-tysięcznej armii, potrzebujemy również 2 mln rezerwistów, żeby ją uzupełnić, gdy dramat się rozpocznie. Co z budową, odbudową obrony cywilnej? Co z budowaniem mechanizmów, dzięki którym będziemy mogli werbować rezerwistów? Powiedział pan, że nie będzie w Polsce miejsca na handel wizami. Czy to oznacza, że całkowicie rezygnujecie z outsourcingu i powierzania prywatnym firmom tego rodzaju działań? Czy chcecie zmienić procedury? Czy i kiedy chcecie zaprezentować poważną politykę imigracyjną? Kasowy PIT, okej, ale co z kasowym VAT, o który również dopominają się przedsiębiorcy? Czy zmienicie zasady naliczania składek dla przedsiębiorców? Jedne z ostatnich decyzji rządu Morawieckiego to podniesienie składek na ubezpieczenie społeczne dla 2 mln polskich firm, jednoosobowych działalności, bardzo skandaliczne zasady rozliczenia, szkodliwe dla samorządów, jeżeli chodzi o składkę zdrowotną. To trzeba zmienić. Zapowiedział pan bardzo konkretne rozwiązania, które spowodują, że Polacy będą mieli benzynę po 5 zł. Co dokładnie chce pan zrobić? Ma pan tu nasze głosy, może pan na nas liczyć. (Dzwonek) Co z likwidacją belkowego? W tym zakresie również może pan liczyć na głosy Konfederacji, nawet jeżeli Lewica będzie przeciwna. Kiedy pan poprze projekt, który zgłosiliśmy za pana, dotyczący podniesienia kwoty wolnej do dwunastokrotności minimalnego wynagrodzenia, minimalnie 60 tys. zł?",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 705",
                },
                {
                    "speaker": "Poseł Przemysław Wipler",
                    "content": "Chętnie wam w tym pomożemy, jeżeli Lewica będzie przeciw. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Bardzo proszę pana posła Pawła Rychlika, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Paweł Rychlik",
                    "content": "Wysoka Izbo! Panie Premierze! We wrześniu 2022 r. na Morzu Bałtyckim doszło do czterech wycieków gazu z gazociągu Nord Stream. Kiedy przyczyny tych zdarzeń były badane, putinowska propaganda – natychmiast po eksplozjach – zaczęła szerzyć insynuacje, że to Polska i Stany Zjednoczone za tym stoją. W tę narrację bardzo dobrze, sprawnie wpisał się Radosław Sikorski, były szef MSZ. Pisał na Twitterze, że za uszkodzeniami gazociągu stoją Stany Zjednoczone. Thank you, USA, dziękujemy ci, Ameryko – tak napisał Sikorski. Dziękujemy, Radosławie Sikorski, za wyjaśnienie, kto stoi za tym terrorystycznym atakiem na infrastrukturę cywilną – w ten sposób wpis Sikorskiego skomentował Dmitrij Poljański, pierwszy zastępca stałego przedstawiciela Rosji przy ONZ. W styczniu tego roku spytany w radiu o to, czy rząd Prawa i Sprawiedliwości myślał o rozbiorze Ukrainy, powiedział: Myślę, że miał moment zawahania w pierwszych 10 dniach wojny. Na te słowa zareagowała rzeczniczka rosyjskiego MSZ Zacharowa: Polscy politycy oficjalnie potwierdzili (Dzwonek), że w początkach napaści myśleli o podziale Ukrainy. Ktoś tak skompromitowany, wpisujący się propagandę Putina nie może być poważnie traktowany przez naszych sojuszników ze Stanów Zjednoczonych i z NATO…",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle.",
                },
                {
                    "speaker": "Poseł Paweł Rychlik",
                    "content": "Panie Premierze! Chciałem tylko zapytać dlaczego. Jakie zależności, czyim… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję, panie pośle. Panie pośle, niczego nie słyszeliśmy przez ostatnie 10 sekund… (Głos z sali: Słyszeliśmy, słyszeliśmy.) …za co pana serdecznie przepraszam. Pani poseł Agnieszka Pomaska, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Agnieszka Pomaska",
                    "content": "Bardzo dziękuję. Panie Marszałku! Panie Premierze! Panie i Panowie Posłowie! Szukam na tej sali pana ministra Budy, który tak ochoczo biegał w trakcie exposé pana premiera Tuska i wręczał listę 100 konkretów. Panie ministrze, przepraszam, już panie pośle Buda, dlaczego nie rozliczył się pan z programu „Mieszkanie+”? (Głos z sali: Pytania są do premiera.) Dlaczego dzisiaj ludzie, którzy oglądają tę debatę, pytają, dlaczego pan ich oszukał? Dlaczego muszą ciągle pytać, dlaczego polski rząd ich oszukał? Przypomnę, że w Gdyni, Krakowie, Lublinie, Mińsku Mazowieckim ludzie nabrali się na wasz program „Mieszkanie+”. Obiecaliście im, że będą mogli kupić mieszkanie za 500 tys. zł. Wiecie, ile dzisiaj to mieszkanie kosztuje? 1,5 mln zł. To jest wasz program mieszkaniowy. To była wasza oferta. Tak, dzisiaj jest o czym rozmawiać i jest po kim sprzątać, a pan minister Buda powinien się po prostu (Dzwonek) wstydzić. Bardzo dziękuję. (Oklaski) (Głos z sali: Pytanie do premiera.)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani poseł Barbara Oliwiecka, Polska 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Barbara Oliwiecka",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Panie Premierze! Kalisz czeka na obwodnicę. Jest jedynym byłym miastem wojewódzkim, które tej obwodnicy nie ma. Przez 8 lat Prawo i Sprawiedliwość więcej obiecywało i mówiło, niż realizowało… (Głos z sali: Kłamstwo!) …ale wcześniej Platforma Obywatelska też zapomniała o Kaliszu. Kalisz i region czekają na oczyszczenie zbiornika retencyjnego na Pokrzywnicy w Szałem. Wody Polskie od lat mówią, że nie mają na to pieniędzy. Zresztą polityka Wód Polskich to temat rzeka, bardzo brudna rzeka, którą musimy oczyścić. Panie Premierze! Już nie tylko Kalisz, ale cała Polska czeka na transformacje energetyczną. Polskie firmy czekają na tanią zieloną energię, która pomoże im utrzymać konkurencyjność, a nasze dzieci czekają na czyste powietrze. Prawa strona ugrzęzła w wyimaginowanej narracji o agentach. Zostawmy ich w tym Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 706 bajorku i bierzmy się do ciężkiej pracy. Jako Polska 2050 zawsze deklarowaliśmy: polityka to służba. Cieszę się, że możemy razem służyć w koalicji 15 października. (Dzwonek) Czyny, nie słowa. Dziękuję ślicznie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo, pani poseł. Pani poseł Magdalena Sroka, PSL – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Magdalena Sroka",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! 15 października prawie 12 mln polskich obywateli powiedziało: stop PiS-owskiej władzy. 2 dni, dwa exposé. Wczorajsze, to cyniczne, obłudne, i dzisiejsze, które patrzy w przyszłość i mówi o odbudowaniu wartości. Ogromna praca przed koalicją 15 października, ogromne wyzwanie przed przyszłym ministrem administracji i spraw wewnętrznych.",
                },
                {
                    "speaker": "Oni zhańbili polski mundur. Nosili na plakatach",
                    "content": "murem za polskim mundurem, a rzeczywiście zhańbili polski mundur. Generał „Granatnik” to wierzchołek góry lodowej. Jeszcze jeden, bardzo ważny temat. Kwestia osób, które do dziś pracują w polskiej Policji. Służą 33 lata. Gdyby odeszły na emeryturę dzisiaj, podlegałyby ustawie dezubekizacyjnej. Trzeba cofnąć te złe zapisy. Przeprosić tych ludzi, którzy (Dzwonek) dzisiaj w sądach dochodzą swoich praw. Cieszę się. Ogromnie się cieszę, że Polska znowuż będzie Polską uśmiechniętą. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani posłanka Paulina Matysiak, klub parlamentarny Lewica. Zapraszam uprzejmie panią posłankę.",
                },
                {
                    "speaker": "Poseł Paulina Matysiak",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! Przed Euro w 2012 r. mówił pan o potrzebie modernizacji kolei. Poszły na to pieniądze, na modernizację linii kolejowych i na modernizację dworców. Ale dziś, w 2023 r. jesteśmy w innym miejscu, bo to, czego potrzebujemy, to budowa nowych linii kolejowych. Dlatego cieszy mnie pańska deklaracja z exposé o tym, że CPK będzie służył polskiej gospodarce. W Polsce, proszę państwa, potrzebujemy linii dużych prędkości. Chcemy jeździć szybko i chcemy jeździć wygodnie, tak jak jeździ się w innych krajach: we Francji, Włoszech, w Hiszpanii czy Maroku. Kolej dużych prędkości może być i powinna być u nas w Polsce, ale to nie znaczy, że można zapomnieć o kolejach w poszczególnych regionach. Trzeba postawić na rozwój połączeń regionalnych, kolejowych i autobusowych (Dzwonek) po to, by dać ludziom wybór, możliwość godnego życia, ale też po to, żeby walczyć ze zmianami klimatycznymi. I panie premierze, pytanie: Czy walka z wykluczeniem transportowym będzie jednym z priorytetów pańskiego rządu? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Michał Wawer, Konfederacja.",
                },
                {
                    "speaker": "Poseł Michał Wawer",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Z exposé niestety nie dowiedzieliśmy się, czym dokładnie będzie się zajmować ministerstwo równości, jakie ma problemy w Polsce do rozwiązania. Podpowiadam i zgłaszam pierwszą sprawę dla tego ministerstwa: nierówność, jakiej doświadczają polscy przewoźnicy, polscy kierowcy, polscy właściciele firm transportowych, którzy muszą konkurować z ukraińskim przewoźnikami, z ukraińskimi firmami dopuszczonymi na rynek unijny bez spełnienia wszystkich obowiązków, jakie się z tym wiążą. Ukraińscy przewoźnicy nie podlegają pakietowi mobilności, nie podlegają polskim podatkom, znacznie wyższym niż na Ukrainie, nie podlegają wymogom technicznym, które Unia narzuca polskim przewoźnikom. I dlatego nie mogą wygrać w tej konkurencji. Dlatego w tej konkurencji przegrywają, bankrutują i dlatego teraz od miesiąca marzną na polskiej granicy, znoszą groźby ze strony Ukraińców, a teraz muszą też fizycznie bronić się przed usunięciem z tejże granicy. (Dzwonek) Panie premierze, pytanie: Czy zamierza pan spełnić postulaty strajkujących polskich przewoźników? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Zbigniew Krzysztof Kuźmiuk, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Zbigniew Krzysztof Kuźmiuk",
                    "content": "Dziękuję bardzo. Panie Marszałku! Panie Premierze! Chciałbym zapytać pana o stosunek do Narodowego Banku Polskiego i prezesa Glapińskiego. W moim rodzinnym Radomiu był pan uprzejmy w kampanii wyborczej powiePrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 707 dzieć, że osobiście będzie pan wyprowadzał pana prezesa Glapińskiego z budynku NBP. Później pan troszeczkę stonował krytykę i mówił tylko o postawieniu prezesa Glapińskiego przed Trybunałem Stanu, i to za dwa rozwiązania, za które międzynarodowe instytucje finansowe, Europejski Bank Centralny, fundusz walutowy, wystawiły mu laurkę. Mam na myśli wsparcie polskiej gospodarki po COVID-zie kwotą ponad 200 mln zł i redukcję inflacji o 12 punktów procentowych – z 18,4 do 6,5. Pan to doskonale wie. Mam nadzieję, że pewnym otrzeźwieniem dla państwa środowiska był także list pani Christine Lagarde (Dzwonek), która bardzo wyraźnie napisała, że będzie stała na straży obrony niezależności polskiego banku centralnego. Mam nadzieję, że państwo to jednak uszanujecie, bo niezależny bank centralny to cecha charakterystyczna każdego państwa demokratycznego. Dziękuję bardzo. (Oklaski) (Poseł Jakub Rutnicki: Pan donosi na Polskę?)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo, panie pośle. W tej chwili głos zabierze pani poseł Elżbieta Gapińska z Koalicji Obywatelskiej.",
                },
                {
                    "speaker": "Poseł Elżbieta Gapińska",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Cieszę się, tak jak cieszą się polscy nauczyciele, rodzice i dzieci, że najgorszy w historii rząd, najgorszy w historii rząd dla edukacji, odchodzi w niepamięć. (Oklaski) Deforma edukacji, którą rozpoczęła minister Zalewska, skutkuje obniżeniem wyników polskich uczniów w międzynarodowych badaniach. Potem był najgorszy w historii minister Czarnek. Odchodzą w niepamięć na zawsze. Myślimy, że polscy nauczyciele odzyskają szacunek i prestiż, który został im odebrany podczas strajków, kiedy ministrowie tego PiS-owskiego rządu poniżali polskich nauczycieli, którzy walczyli o dobrą, polską szkołę. Odpartyjnimy polską szkołę. (Głos z sali: Tak, tak.) Odpartyjnimy na 100%. Podwyższymy wynagrodzenie dla nauczycieli. Polska szkoła będzie miała w centrum polskiego ucznia. (Dzwonek) W każdej szkole będzie pedagog i psycholog, którzy będą pomagać dzieciom w kryzysie. To jest dla nas twarde zobowiązanie. Jestem przekonana, że nasi ministrowie go dotrzymają. Dziękuję bardzo. (Oklaski) (Poseł Krystyna Skowrońska: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Bartosz Romowicz, Polska 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Bartosz Romowicz",
                    "content": "Szanowny Panie Marszałku! Panie Posłanki! Panowie Posłowie! Szanowny Panie Premierze! Powiedział pan wczoraj o swoich dziadkach, a ja jako wnuk przesiedleńca w ramach akcji H–T Hrubieszów–Tomaszów mam do pana prośbę, żebyśmy nigdy więcej nie dzielili Polaków. PiS-owi udało się podzielić nas wszędzie tam, gdzie to było możliwe – przy stole w trakcie imprezy rodzinnej, w zakładach pracy, na uczelniach, ale też wśród samorządów. PiS podzielił samorządowców na tych naszych i nie naszych. Ich nasi dostawali narzędzia do tego, aby realizować swój mandat wójta, burmistrza czy prezydenta miasta w postaci ogromnych, politycznych środków finansowych na realizację zadań publicznych – budowę dróg, szkół czy obiektów sportowych. Nie nasi tego nie dostawali, a tak naprawdę karę za to ponosili mieszkańcy. Ja nigdy nie byłem ich samorządowcem, ale zawsze byłem samorządowcem moich Ustrzyk i moich mieszkańców. Nigdy więcej, i o to pana proszę, nie może być tak, że rząd Rzeczypospolitej Polskiej będzie dzielił samorządowców. Ale też proszę pana o jedno, aby te wszystkie niesprawiedliwości wyrównać. (Dzwonek) Trzeba zrobić audyt, pokazać, jak te środki były przekazywane, i w pierwszej kolejności wesprzeć te samorządy, które regularnie przez ostatnich 8 lat były karane przez Prawo i Sprawiedliwość. Dziękuję. (Oklaski) (Głos z sali: Nie było tak, panie pośle.) (Poseł Tomasz Zimoch: Ale przecież pan poseł był burmistrzem, to chyba najlepiej wie.)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Czy jeszcze macie ochotę państwo… (Gwar na sali) Pani poseł, przepraszam bardzo. Jak macie ochotę państwo sobie pokrzyczeć do siebie, to może na korytarzu, będzie fajnie po prostu. Pan poseł Marek Sawicki, PSL – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Marek Sawicki",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! W dniu 3 maja 2021 r. Ministerstwo Funduszy i Polityki Regionalnej oficjalnie przesłało Krajowy Plan Odbudowy do Komisji Europejskiej. Dokonał tego wiceminister Waldemar Buda. Komisja Europejska zgodnie z prawem miała 2 miesiące na ocenę naszego KPO. Powinna nam w październiku 2021 r. przekazać zaliczkę w wysokości 4,7 mld euro, tj. 13% zakontraktowanych przez pana premiera środków. W raporcie Komisji z dnia 24 maja 2023 r. czytamy, że Polska nie otrzymała zaliczki na KPO, ponieważ zbyt późno złożyła KPO w Brukseli. Wniosek został wycofany, poprawiony (Dzwonek), ale ktoś nie dopilnował terminu jego złożenia. Proszę Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 708 pana premiera, żeby osoby odpowiedzialne za niedostarczenie Polsce ponad 20 mld zł w październiku 2021 r. poniosły odpowiedzialność, bo jeśli nie, to będę musiał sam w tej sprawie złożyć doniesienie do prokuratury. (Oklaski) (Głos z sali: Bardzo dobrze.)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pani posłanka Marcelina Zawisza, klub parlamentarny Lewica. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Marcelina Zawisza",
                    "content": "Szanowny Panie Marszałku! Szanowny Panie Premierze! Wysoka Izbo! 27 listopada w Czechach odbył się ostrzegawczy strajk generalny. Setki tysięcy nauczycielek, pielęgniarek, urzędników i pracowników fabryk wstrzymało się od pracy. W Polsce taki protest byłby nielegalny. Nic dziwnego, obowiązujące prawo bazuje na ustawie z 1982 r., napisanej tak, żeby utrudnić życie „Solidarności”. Pielęgniarki mogą domagać się podwyżek od dyrektora szpitala, nauczycielki od dyrektora szkoły, nie mogą naciskać na ministrów, którzy realnie podejmują decyzje. Pracownicy fabryki nie mogą poprzez strajk wywierać presji na rząd, by zapewnił ich dzieciom dobrą edukację czy ochronę zdrowia. Wolność do strajku to jedna z podstawowych wolności obywatelskich, takich jak wolność zgromadzeń czy wolność słowa. Można z niej korzystać nie tylko u naszych południowych sąsiadów, ale także we Francji, Belgii czy we Włoszech. Pytanie do pana premiera: Panie premierze, czy popiera pan europeizację prawa do strajku politycznego w Polsce, aby realnie dać ludziom prawo do walki o swoje prawa? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Krzysztof Mulawa, Konfederacja.",
                },
                {
                    "speaker": "Poseł Krzysztof Mulawa",
                    "content": "Panie Premierze! Mówił pan w swoim exposé o zawiązanym zespole do spraw strajku przedsiębiorców i przewoźników na granicy. Panie premierze, proszę nie mówić, tylko proszę natychmiast skutecznie zrealizować postulaty polskich przedsiębiorców, którzy oczekują na granicy. Ale proszę się nie pomylić: polskich przewoźników, nie niemieckich i nie ukraińskich. Pół nocy spędziłem dzisiaj w Dorohusku, gdzie w dniu wczorajszym z niewiadomych przyczyn wójt gminy Dorohusk rozwiązał ten protest, a jest to wielkim skandalem, że Ukraińcy wiedzieli o tym 2 dni wcześniej. Niestety – mówię: niestety – jedyne, z czym kojarzyłem w Dorohusku pana, panie premierze, to są białe kaski, podobne do tych, których używał pan do pacyfikacji marszów niepodległości i pod siedzibą JSW. Proszę zapamiętać skromne nazwisko skromnego posła Mulawy i próbować odpowiedzieć w późniejszym czasie na pytanie (Dzwonek), czy będzie pan znowu pozorował działania, czy tym razem w trybie dokonanym załatwi pan polski interes. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle, dziękuję. Pan poseł Jarosław Zieliński, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Jarosław Zieliński",
                    "content": "Swoje exposé, panie premierze, którego główną cechą była wszechobecna obłuda, zakończył pan słowami waszej także fałszywej piosenki: Szczęśliwej Polski już czas. Aby Polska była szczęśliwa, musi być przede wszystkim bezpieczna, a tymczasem za pierwszych pana rządów redukowano polską armię, likwidowano jednostki wojskowe, zwłaszcza na wschodzie, a linię obrony wyznaczono dopiero na linii Wisły. Takim symbolem ówczesnej polityki była likwidacja jedynej jednostki wojskowej przy przesmyku suwalskim, czyli 14. Pułku Artylerii Przeciwpancernej w Suwałkach. W jaki sposób zapewni pan dzisiaj Polsce bezpieczeństwo? W jaki sposób zapewni pan bezpieczeństwo w szczególności mieszkańcom Polski wschodniej? – bo oni czują się szczególnie narażeni na zagrożenie rosyjskim imperializmem. Chociaż oczywiście cała Polska czuje się zagrożona tym, co się dzieje na wschodzie przez rosyjski imperializm, który odżył na naszych oczach. (Dzwonek) W jaki sposób zapewni pan swoją wiarygodność w tej sprawie? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pani poseł Maria Małgorzata Janyska, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Maria Małgorzata Janyska",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! PiS zdemolował tworzenie prawa. Szczególnie dotkliwie odczuli to przedsiębiorcy, którzy za rządów PiS-u nie Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 709 wiedzieli, co ich czeka z dnia na dzień, jakie nowe obciążenia administracyjne, finansowe, organizacyjne, w tym kontekście systemu podatkowego, który zmienialiście wielokrotnie i który cynicznie nazwaliście Polskim Ładem. To była największa bariera w ich działalności, która spowodowała, że ograniczali decyzje inwestycyjne i strategie rozwojowe swoich firm. Teraz czekają na proste, stabilne, zrozumiałe prawo, takie, które będzie tworzone w dialogu społecznym, dialogu, który będzie oparty na wiedzy, na doświadczeniu, tak zwyczajnie – na rozumie, co wam było kompletnie obce. Oczekują także deregulacji tych absurdów, które powprowadzaliście.",
                },
                {
                    "speaker": "Mam w związku z tym pytanie do pana premiera",
                    "content": "Jak organizacyjnie planuje pan umocować system deregulacji tworzenia prawa gospodarczego? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani poseł Ewa Sz… (Poseł Ewa Schädler: Schädler.) Poseł Ewa Schädler, przepraszam panią serdecznie, Polska 2050 – Trzecia Droga. Zapamiętam, już się nigdy nie pomylę.",
                },
                {
                    "speaker": "Poseł Ewa Schädler",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Dziś mieliśmy szansę, tak samo jak i wczoraj, na reset, na prawdziwy reset tego, co dzieli naszą scenę polityczną na naszych i waszych. I tak samo dzieli nasz naród na naszych i waszych. Proszę państwa, wszyscy ponosimy odpowiedzialność za to – żeby już teraz i od dzisiaj tak nie było. Polacy i Polki zasługują na to, żebyśmy postarali się wszyscy ponad podziałami stanąć tutaj i rozpocząć od dzisiejszego dnia współpracę. Współpracę, która może nie jest wygodna dzisiaj dla mnie, dla państwa czy dla państwa, ale tego oczekują nasi wyborcy. Nasi wyborcy poszli 15 października i oddali głos właśnie na przyszłość, a nie na przeszłość. Nie na to, co się wydarzyło 10, 20 lat temu, a może jeszcze w zamierzchłej przeszłości. Pan premier dzisiaj ponownie (Dzwonek) jest premierem. Dajmy mu szansę na to, żeby zbudował coś ponad podziałami. My tego chcemy. Polska 2050 pojawiła się właśnie z tego powodu, że już ma dość tych kłótni. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję pani poseł Ewie Schädler. I bardzo proszę pana posła Mirosława Maliszewskiego, PSL – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Mirosław Maliszewski",
                    "content": "Panie Marszałku! Panie Premierze! W swoim wystąpieniu pan słusznie powiedział, że jednym z ważniejszych problemów, które stoją przed polskim rolnictwem, jest poddanie go nierównej konkurencji z produktami z Ukrainy. Bardzo słusznie też pan zdiagnozował obecną sytuację związaną z importem i z problemami na rynku zbóż, na rynku rzepaku czy na rynku owoców miękkich. Dlatego wydaje się, że te działania, które były do tej pory podejmowane, są działaniami nieskutecznymi i mało strategicznymi. Wypada, by w tych sprawach większą aktywność wykazała Komisja Europejska i Unia Europejska. To m.in. jeden z pomysłów Czesława Siekierskiego, aby ten zakaz importu przedłużyć, ale też aby obejmował on całą Unię Europejską, ale też żeby wpracować strategiczne metody zapewnienia polskim rolnikom konkurowania z produktami ukraińskimi na równych warunkach, zważywszy na to, że mamy w perspektywie członkostwo Ukrainy w Unii Europejskiej. Pytanie: Panie premierze, czy pan minister Czesław Siekierski może liczyć na pana szerokie kontakty w Brukseli, tak aby zapewnić polskim rolnikom (Dzwonek) dobre warunki konkurowania z produktami ukraińskimi w przyszłości? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Maciej Konieczny, klub parlamentarny Lewica. Zapraszam, panie pośle.",
                },
                {
                    "speaker": "Poseł Maciej Konieczny",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Panie premierze, w swoim exposé słusznie zwrócił pan uwagę na niebezpieczeństwo związane z podjęciem przez tymczasowy rząd premiera Morawieckiego kluczowych dla polskiej energetyki decyzji wbrew rekomendacjom służb specjalnych. Chodziło o małe reaktory jądrowe. To, czego niestety w tym przemówieniu zabrakło, to jasna, jednoznaczna deklaracja o kontynuacji polskiego programu energetyki jądrowej. Ja bym takiej deklaracji oczekiwał, bo Polska naprawdę nie ma już czasu. Potrzebujemy kontynuować budowę dużych elektrowni jądrowych w Polsce, bo tylko jak najszybsza finalizacja tego programu zapewni Polsce stabilność energetyczną, zapewni Polsce uwolnienie się od brudnych źródeł energii, zapewni Polsce bezpieczeństwo energetyczne i ochronę klimatu. Dlatego poprosiłbym o jasną i czytelną deklarację, że polski program energetyki jądrowej będzie kontynuowany (Dzwonek), i to będzie kontynuowany z całą mocą. Dziękuję. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 710",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Włodzimierz Skalik, Konfederacja. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Włodzimierz Skalik",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Pański minister Adam Bodnar, odbierając 2 lata temu nagrodę Dialog Prize przyznawaną przez Federalny Związek Towarzystw Niemiecko-Polskich, powiedział następujące słowa: Polska kultura prawna i przemiany po 1989 r. zostały zainspirowane i były wspierane przez niemiecką myśl prawniczą, ale to powoduje po stronie mentora także szczególną odpowiedzialność, jak w przypowieści z „Małego Księcia”: jeśli oswoi się zwierzątko, to nie można go później porzucić. Panie Premierze! Czy wybierając Adama Bodnara na ministra sprawiedliwości, czuje się pan jak oswojone przez Niemców zwierzątko? Niech pan jasno i wyraźnie nam powie, kto jest pańskim mentorem. Ponadto, panie premierze – to bardzo ważna kwestia – proszę też o jasną odpowiedź (Dzwonek), czy podziela pan opinię swojego ministra Adama Bodnara, że Ukraińcy w Polsce powinni mieć prawa wyborcze. Mam nadzieję, że do tej kwestii pan się odniesie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Daniel Milewski, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Daniel Milewski",
                    "content": "Panie Marszałku! Wysoka Izbo! We wczorajszej debacie zwracałem uwagę na kwestie polityki energetycznej, bezpieczeństwa w tym zakresie. Pozostając w tym kluczowym dla Polaków obszarze, pytamy, czy ochrona przed rosnącymi cenami ma obowiązywać tylko przez pół roku. Czy wróci logika, że ceny benzyny czy prądu po wyborach mogą rosnąć już bez granic? Ten konkret, jeden ze 100 konkretów, już mieliście okazję, mogliście zrealizować i tego nie zrobiliście, czyli zamrożenie cen energii na cały 2024 r. Czy ustawa wiatrakowa wróci z całym jej fatalnym, bo pisanym lobbystyczną ręką, kształtem? Czy przywrócicie obligo giełdowe, co przyniesie skokowy wzrost cen dla wszystkich, ale jednocześnie także duże marże dla energii np. z wiatraków czy innych odnawialnych źródeł? Jakie są w końcu szczegółowe plany w zakresie budowy elektrowni jądrowych i czy wpłyną one na zablokowanie albo opóźnienie rozpoczętych już projektów? (Dzwonek) Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pani poseł Krystyna Sibińska, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Krystyna Sibińska",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Dla młodych ludzi, którzy rozpoczynają swoje życie i zakładają rodziny, ważne jest poczucie bezpieczeństwa. Elementem tego poczucia bezpieczeństwa jest własne mieszkanie. PiS-owi kompletnie nie wyszedł żaden program mieszkaniowy. Zmieniało się sześciu ministrów, 44 razy zmieniali Prawo budowlane, 36 – planowanie przestrzenne, powstawały różne dziwne twory, różne instytucje, brali kasę w każdym wymiarze. Mieszkań nie przybyło. Dlatego pytanie i prośba. Proszę o odpowiedź na pytanie, jakie będą programy mieszkaniowe, które pomogą młodym ludziom w podejmowaniu decyzji o zakładaniu własnej rodziny. Na koniec jeszcze jedno pytanie z lubuskiego. Proszę zapisać głęboko w sercu elektryfikację linii 203: Kostrzyn – Gorzów – Tczew. To jest niezwykle potrzebna linia. Ona pozwoli, żeby lubuskie nie było wykluczone komunikacyjnie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Marcin Przydacz, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marcin Przydacz",
                    "content": "Bardzo dziękuję. Panie Marszałku! Szanowny Panie Premierze! Wysoka Izbo! Pan premier w swoim wystąpieniu mówił, że każdy, kto w obliczu zagrożeń pochodzących ze wschodu gra na izolację, naraża Polskę. Otóż informuję pana, panie premierze, że to już po zmianie rządów, po 2015 r. do Polski przybyły znaczne ilości wojsk sojuszniczych, to w ramach decyzji NATO udało się doprowadzić do stworzenia baz eFP tutaj, w Polsce. Kilkanaście tysięcy sojuszniczych wojsk zapewnia dzisiaj, poza obecnością Wojska Polskiego, nasze bezpieczeństwo, bezpieczeństwo Polski i bezpieczeństwo całego regionu. Do 2015 r., panie premierze, nie udało się panu przekonać naszych sojuszników do stałej obecności, znaczącej obecności tutaj, w Polsce. Brak woli i determinacji Polski, także pańskiego rządu, nie przełamał wówczas (Dzwonek) oporu Zachodu przed odrzuceniem aktu stanowiącego NATO – Rosja. Teraz moje pytanie, panie marszałku. Panie premierze, czy pan uważa, że ten akt, akt stanowiący NATO – Rosja, nadal obowiązuje i czy zamierza pan Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 711 zabiegać o wzmocnienie obecności sojuszniczej w Polsce, która pojawiła się za rządów Prawa i Sprawiedliwości? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani poseł Ewa Szymanowska, Polska 2050 – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Ewa Szymanowska",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! Pierwszy program Polski 2050, który został napisany przez Instytut Strategie 2050 to „Państwo i Kościół na swoje miejsce”. Panie premierze, chciałabym zapytać, czy jest pan gotowy na przeprowadzenie rozdziału państwa od Kościoła. (Głos z sali: Jest rozdzielone.) Wiele jest tu do zrobienia, m.in. likwidacja Funduszu Kościelnego i zastąpienie go dobrowolnym odpisem podatkowym, uregulowanie kwestii religii w szkołach i ich finansowania, zaprzestanie finansowania tzw. dzieł ojca dyrektora czy zatrudnienia kapelanów w urzędach, np. w Lasach Państwowych, czy, jak się niedawno dowiedziałam, w niektórych urzędach skarbowych. Kiedy zapytałam łódzkich urzędników, ile nas to kosztuje i co ksiądz robi w urzędzie skarbowym, uzyskałam odpowiedź, że ma wynagrodzenie ok. 6 tys. brutto i wysyła mailem raz w tygodniu w piątek słowo na niedzielę. PiS hojnie wynagradza księży. To jest właśnie przykład rozdawnictwa i niegospodarności (Dzwonek), na które my, posłanki i posłowie Polski 2050 – Trzecia Droga, się nie zgadzamy. Panie Premierze! Polki i Polacy nam zaufali i nie możemy ich zawieść jako koalicja 15 października.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, pani poseł.",
                },
                {
                    "speaker": "Poseł Ewa Szymanowska",
                    "content": "Drugiej szansy nie będzie. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Ireneusz Raś, PSL – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Ireneusz Raś",
                    "content": "Panie Marszałku! Panie Premierze! Mocno wybrzmiały słowa o takich zdecydowanych podwyżkach dla nauczycieli wszystkich szczebli. Chciałbym, żeby pan rozważył możliwość docenienia również trenerów juniorów, dzieci i młodzieży, gdyż wydaje mi się, że to jest dzisiaj największy problem polskiego sportu. Nie ma dobrego traktowania tych fachowców, bez których nie będzie sukcesów polskiej reprezentacji. Na tym tle widać, jak blado wypadamy, jeżeli chodzi o piłkę nożną. Oni często łączą kilka etatów, a jeszcze w weekend, jak pan dobrze wie, muszą poświęcać czas drużynie dziewczyn albo chłopców, jeżdżąc po świecie. Chciałbym też, żeby pan w odpowiedzi odniósł się do turystyki, tym bardziej że turystyka zdaje się jest zapisana w środkach KPO, na które czekamy.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo.",
                },
                {
                    "speaker": "Poseł Ireneusz Raś",
                    "content": "Środki KPO były kierowane (Dzwonek) na niwelowanie skutków pandemii i turystyka była bardzo dotknięta. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Ireneusz Zyska, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Ireneusz Zyska",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Wbrew temu, co od wielu lat próbujecie wmawiać opinii publicznej, odnawialne źródła energii w Polsce rozwijają się bardzo dynamicznie. Świadczy o tym m.in. to, że w 2022 r. byliśmy na drugim miejscu w Unii Europejskiej za Republiką Federalną Niemiec w zakresie przyrostu mocy fotowoltaiki oraz – uwaga – na trzecim miejscu co do nakładów inwestycyjnych na wiatraki na lądzie. (Poseł Izabela Leszczyna: Jakby się dało tę energię odkupić, toby było dobrze.) Nie będę wchodził w szczegóły, bo mamy mało czasu, ale przygotowaliśmy bilans zamknięcia. Pan premier dowie się z tego dokumentu, co udało się zrobić w Ministerstwie Klimatu i Środowiska w tym obszarze. Chciałbym zapytać pana premiera, dlaczego zdecydowaliście się otworzyć szeroko drzwi dla lobbystów wiatrakowych w tym poselskim projekcie ustawy, który za zgodą pana, jak sądzę, został tutaj WyPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 712 sokiej Izbie przedłożony. To naprawdę skandaliczne przepisy. Wywołaliście demony przeszłości. W tej chwili będzie wam o wiele trudniej (Dzwonek) konsultować z opinią publiczną ten rozwój energetyki wiatrowej na lądzie, bo będzie duży sprzeciw społeczny.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle.",
                },
                {
                    "speaker": "Poseł Ireneusz Zyska",
                    "content": "Nie wolno tak robić. Konsultacje społeczne budują zaufanie do… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję, panie pośle, bardzo. Teraz zaproszę pana posła Pawła Śliza z Polski 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Paweł Śliz",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Serce moje jest przepełnione wielką radością, że mogę stać tutaj w tym historycznym momencie, na który ja i moi wyborcy czekali 8 lat. Czekali 8 lat, bo mieli dość kłótni i chcieli iść do przodu. A pójście do przodu dla rządu to będzie bardzo ciężka praca, ale nie tylko merytoryczna w ministerstwach, lecz także w terenie, żeby pojednać ludzi, bo wykopaliście rowy między Polakami i zniszczyliście relacje między nami. Pójście do przodu to praca merytoryczna naszych pań minister, również trzech pań z Trzeciej Drogi i z Polski 2050, pań minister, które – wiem to – swoją mądrością, rozwagą, z uwzględnieniem postulatów będą prowadziły konsultacje i będą rozmawiały ze społeczeństwem, z obywatelami, bo chcemy, żeby polityka przestała być areną sporu. Ale jedna najważniejsza dla mnie rzecz – wymiar sprawiedliwości, system sądownictwa. My go też musimy naprawić (Dzwonek), żeby obywatele mieli poczucie sprawczości, że sądy są sprawiedliwe, a nie są na zawołanie polityków. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Henryk Kiepura, PSL – Trzecia Droga. Czy jest pan poseł? Nie ma. Pan poseł Paweł Hreniak, Klub Parlamentarny Prawo i Sprawiedliwość. Jest.",
                },
                {
                    "speaker": "Poseł Paweł Hreniak",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! W exposé niewiele niestety było konkretów, a już zupełnie nic nie było o służbach mundurowych i o bezpieczeństwie wewnętrznym, nie było nic o Państwowej Straży Pożarnej, Policji, nic nie było o ochotniczych strażach pożarnych, nie było ani słowa o tej kilkusettysięcznej grupie osób, która bezinteresownie dba o bezpieczeństwo obywateli. Ci wyjątkowi ludzie, druhowie ratownicy, nie zostali w żaden sposób zauważeni przez premiera i jest to zastanawiające, tym bardziej że w waszych deklaracjach wyborczych w ich kierunku padały bardzo konkretne obietnice. Padła m.in. obietnica mówiąca o wcześniejszej emeryturze dla druhów. Dziś w exposé o tym cisza. W związku z tym proszę o jednoznaczną odpowiedź, czy nowy rząd zamierza zrealizować obietnicę emerytalną złożoną druhom. Poproszę też o deklarację, że nie zmarnujecie tego wszystkiego, co dla sprawy (Dzwonek) ochotniczych straży pożarnych zrobiło w ostatnim czasie Prawo i Sprawiedliwość. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani poseł Krystyna Skowrońska, Koalicja Obywatelska.",
                },
                {
                    "speaker": "Poseł Krystyna Skowrońska",
                    "content": "Szanowny Panie Marszałku! Panie i Panowie Posłowie! Panie Premierze! Myślę, że pan premier dzisiaj słuchał dokładnie, ale to, jakie pytania zadają posłowie PiS-u, znaczy, że przez ostatnie 8 lat nic nie zrobili. Mówicie o wielu nierozwiązanych problemach. Czekamy na powrót demokracji, na przywrócenie godności, na przywrócenie rzetelności w pracy, na szansę dla młodych, przedsiębiorców, rolników. – to, czego wy nie zrobiliście, bo wy wzięliście wysokie wynagrodzenia i premie. Panie Premierze! Życzymy, aby ten szczyt Rady Europejskiej był bardzo owocny. Czekamy bardzo, jako Polska, przedsiębiorcy i Polacy, na pieniądze z KPO. One są nam potrzebne, aby zlikwidować długi w szpitalach, aby zlikwidować (Dzwonek) kolejki i aby opieka psychiatryczna dla dzieci była zabezpieczona na wysokim poziomie. Dobrych decyzji w Brukseli.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Jarosław Rzepa, PSL – Trzecia Droga. Dziękuję serdecznie, pani poseł. Proszę bardzo Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 713",
                },
                {
                    "speaker": "Poseł Jarosław Rzepa",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Dokładnie 8 miesięcy temu ówczesny wojewoda zachodniopomorski Zbigniew Bogucki, rozszerzając strefę ochronną wokół gazoportu, zamknął drogę ku morzu, jedyną drogę dla prawobrzeżnej części, która łączyła z jedyną plażą. Ta droga została zamknięta. Ponad 100 tys. ludzi, którzy odwiedzali latarnię i Fort Gerharda, nie skorzystało z tej atrakcji w tym roku. Ludzie stracili dochody, poupadały małe biznesy. Kilkadziesiąt kilometrów dalej jest Baltic Pipe. Nikt nie wprowadził żadnej szczególnej ochrony. Ludzie protestowali. Premier Kaczyński obiecał, że drogę otworzy. Dzisiaj mamy 12 grudnia. Droga jest zamknięta. Tracimy ogromne pieniądze na ochronę, a tak naprawdę trzeba przywrócić normalność. Panie Premierze! Mieszkańcy Warszowa w Świnoujściu oczekują, że droga ku morzu w tym mieście zostanie dla nich otwarta, a ludzie będą mogli przyjechać do latarni i do Fortu Gerharda. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pani poseł Ewa Leniart, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Ewa Leniart",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! W swoim exposé wspomniał pan o tym, iż władza centralna jest po to, aby ułatwiać rozwiązywanie problemów lokalnych. Rząd Prawa i Sprawiedliwości za ostatnie 8 lat przekierował na Podkarpacie, które mam zaszczyt reprezentować, znaczne środki: 13,5 mld zł na realizację polityki prorodzinnej, 43,5 mld zł na służbę zdrowia, 10 mld zł na infrastrukturę czy 4 mld zł dla seniorów. Pan, gdy po raz pierwszy obejmował funkcję premiera polskiego rządu, w 2008 r. podjął decyzję o wstrzymaniu dofinansowania ważnych inwestycji dla Podkarpacia, takich jak droga S19 czy też zbiornik Myscowa – Kąty. Czy obecnie jako premier polskiego rządu będzie pan pamiętał, że województwo podkarpackie jest także województwem polskim, które wymaga (Dzwonek) wsparcia finansowego? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani poseł Danuta Jazłowiecka, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Danuta Jazłowiecka",
                    "content": "Dziękuję, panie marszałku. Panie Marszałku! Panie Premierze! Wysoka Izbo! W ostatnich 8 latach nastąpił w Polsce znaczny wzrost ubóstwa energetycznego. W moim województwie ubóstwo energetyczne jest największe w skali kraju, sięga niemal 19% według badań budżetów gospodarstw domowych z 2021 r. I wszędzie tam, gdzie podstawowymi powodami ubóstwa energetycznego są wysokie koszty energii, niskie dochody czy niska efektywność energetyczna budynków, w moim województwie podstawowym problemem są zmiany demograficzne. Zmiany demograficzne, które są jednym z najpoważniejszych problemów dotykających społeczeństwa krajów unijnych, tuż obok zmian klimatycznych, wyzwań energetycznych i globalizacyjnych. Zmiany demograficzne, które poza zwiększeniem skali obciążeń budżetowych oraz trudności w systemach emerytalnych i opiece zdrowotnej, będą niekorzystnie oddziaływać na dynamikę gospodarczą i konkurencyjność inwestycji, rozwój i badania. Pana rząd wypełnia wiele zadań i wyzwań wychodzących naprzeciw walce ze zmianami demograficznymi. (Dzwonek) Proszę jednak rozważyć przeprowadzenie obywatelskiej, ogólnokrajowej debaty nad wdrażaniem kompleksowego programu walki ze zmianami demograficznymi we wszystkich sektorach i szczeblach administracji rządowej i samorządowej. Razem możemy więcej. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Adam Luboński, Polska 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Adam Luboński",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Szanowni Państwo! Najwyższy czas już zakończyć trwające od lat, a w szczególności 8 ostatnich lat, sojusz tronu z ołtarzem. Jak przed chwilą powiedziała moja koleżanka, państwo i Kościół muszą wrócić na swoje miejsce, oczywiście z poszanowaniem wartości każdej ze stron. Tego oczekują od nas nasi wyborcy. Panie Premierze! Jakie są pana poglądy w kwestii rozdziału państwa od Kościoła i jakie kroki zostaną podjęte w celu wzmocnienia tej separacji? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Andrzej Grzyb, PSL – Trzecia Droga. Bardzo proszę Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 714",
                },
                {
                    "speaker": "Poseł Andrzej Grzyb",
                    "content": "Panie Marszałku! Wysoka Izbo! Chciałbym powiedzieć również: Panie Premierze! Pytanie następujące: Czy jesteśmy gotowi na to, aby opracować polską strategię biogospodarki? Program niezmiernie ważny z punktu widzenia naszych możliwości i wykorzystania surowców odnawialnych: od rolnictwa przez leśnictwo do rybołówstwa, akwakultury i gospodarki nabrzeżnej. Surowce odnawialne są szansą dla polskiej gospodarki. Nie mamy tutaj strategii, a wykorzystaliśmy pieniądze m.in. z programu BIOEAST na przygotowanie od strony naukowej tego programu. Po drugie, czy jesteśmy gotowi, aby przygotować i wreszcie uruchomić nową ustawę dla rzemiosła? Cała poprzednia kadencja była strawiona na to, żeby negocjować z tymi przedstawicielami. Nic z tego nie wyszło. Rzemiosło czeka na nową ustawę. I sprawa trzecia – kwestia zrównoważonego rozwoju. Ministerstwa powinny być w Warszawie, a urzędy centralne powinny być w polskiej przestrzeni, w dawnych (Dzwonek) miastach wojewódzkich. To buduje zrównoważony rozwój, m.in. poprzez przeniesienie części instytucji centralnych, to daje szansę młodym ludziom. Wydaje mi się, że…",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie.",
                },
                {
                    "speaker": "Poseł Andrzej Grzyb",
                    "content": "…powinniśmy do tego wrócić. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Bardzo proszę pana posła Waldemara Andzela, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Waldemar Andzel",
                    "content": "Panie Marszałku! Wysoka Izbo! Wystąpienie Donalda Tuska było pełne pustych obietnic i tanich haseł. Ja mam pytanie odnośnie do polskiej armii. Wydatki za rządów Prawa i Sprawiedliwości to 4% PKB, najwięcej w NATO, 137 mld zł. Za Platformy Obywatelskiej i PSL-u w 2015 r. to 37 mld zł. Mam pytanie: Jak się ma obecnie w programie utrzymanie zawartych kontraktów zbrojeniowych do zapowiedzi przeglądu i ewentualnego wypowiedzenia kontraktów zawartych w ostatnich tygodniach? Ostatnie kontrakty mogą zostać unieważnione, tak mówią niektórzy ważni politycy koalicji. Czy chcecie budować europejski system obrony powietrznej? Mam też pytanie: Co chcecie zrobić z PGZ-em i jak się to ma do słów pana Siemoniaka, który zapowiedział, że inwestycja w fabrykę krabów w Gliwicach nie ma sensu, bo trzeba je produkować w Stalowej Woli? Czy chcecie zabrać (Dzwonek) te 850 mln zł z Bumar-Łabędy, które fabryka dostała od rządu Prawa i Sprawiedliwości? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję. Pani poseł Katarzyna Kierzek-Koperska, Koalicja Obywatelska.",
                },
                {
                    "speaker": "Poseł Katarzyna Kierzek-Koperska",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! To wielki dzień dla Polski, bo wreszcie nepotyzm, korupcja polityczna, chora ideologia oraz cwaniactwo kończą się. Czekaliśmy na ten dzień 8 długich lat. I to dzięki wam, Polki i Polacy, bo uwierzyliście, że dobra, mądra polityka jest możliwa, uwierzyliście, że możemy żyć w kraju, z którego będziemy dumni. Kariery Nikodemów Dyzmów kończą się na zawsze. A teraz usiądźcie w swoich sejmowych ławach i zobaczcie, jak uczciwie i mądrze można zarządzać naszą Polską. Polską, która nie dzieli Polaków na lepszy i gorszy sort, Polską, która nie wyklucza nikogo, która szanuje konstytucję i która dba o rozwój dla przyszłych pokoleń. Wiem, że premier Donald Tusk razem ze swoim rządem poradzą sobie z tym zadaniem. Dlatego dzisiaj (Dzwonek) z wielką dumą i odpowiedzialnością zagłosuję za tym rządem i za tym premierem. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Sławomir Ćwik, Polska 2050.",
                },
                {
                    "speaker": "Poseł Sławomir Ćwik",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! Wbrew składanym obietnicom rządy Prawa i Sprawiedliwości oszukały swoich wyborców i nie zadbały o rozwój Polski wschodniej. Brak zrównoważonego rozwoju dla Polski Wschodniej, w szczególności dla terenów dawnego województwa bialskiego, chełmskiego i zamojskiego, powoduje demograficzną katastrofę dla tego regionu. Szczególnie młodzież masowo emigruje z tych terenów, przesiedlając się do aglomeracji i bogatszych regionów, gdzie poszukuje lepszej pracy i wyższego wynagrodzenia. Zgodnie z prognozami taka polityka doprowadzi do demograficznej katastrofy i wyludnienia się tych terenów. Dlatego, panie premierze, zwracam się z pytaniem i prośbą: Czy Polska Wschodnia może liczyć na Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 715 decentralizację instytucji i przeniesienie części z nich szczególnie do byłych miast wojewódzkich, na inwestycje w infrastrukturę w Polsce Wschodniej i na granty dla inwestorów tworzących atrakcyjne miejsca pracy (Dzwonek) i rozwój turystyki? Cała Polska tego potrzebuje. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję. Pan poseł Tadeusz Samborski, PSL – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Tadeusz Samborski",
                    "content": "Szanowny Panie Marszałku! Szanowny Panie Premierze! Wysoka Izbo! Pragnę serdecznie pogratulować panu premierowi i wszystkim liderom partii koalicyjnych, bo stworzenie koalicji z ugrupowań, które mają tak wyrazisty program, poczucie wielkiej autonomii i silne korzenie tożsamościowe, jest niezwykle trudne, wymaga talentu organizacyjnego, sprawności. Serdecznie tego gratuluję. Dobrze się stało, że w tym panoramicznym exposé pana premiera znalazł się także wątek Lasów Państwowych, bo już w trakcie wystąpienia pana premiera otrzymywałem sygnały z Dolnego Śląska, od pracowników wielu nadleśnictw na Dolnym Śląsku, o tym, że występują tam masowo zjawiska patologiczne, zwłaszcza w sferze stosunków międzyludzkich, ale także w sprawach organizacyjnych, produkcyjnych. Te sygnały są niezwykle niepokojące i mam nadzieję, że pan premier pochyli się i podejmie (Dzwonek) ten wątek. Na koniec pragnę zaprosić też pana premiera do Bogatyni, której mieszkańcy mają wiele żalu, pretensji, uzasadnionych zresztą, do rządzących na różnych poziomach władzy. Dziękuję bardzo, panie marszałku. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Kazimierz Gwiazdowski, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Kazimierz Gwiazdowski",
                    "content": "Panie Marszałku! Wysoka Izbo! Szanowni Państwo! W wystąpieniu pana premiera zabrakło głosu o polskiej wsi, o rolnictwie, a myślę, że gdy się ma takiego wybitnego stratega jak Michał Kołodziejczak, powinna wybrzmieć jasna zapowiedź, co dla polskiej wsi zostanie dokonane w najbliższym czasie. Myślę, że polska wieś zasługuje na to, żebyście przedstawili racjonalny program, jak będziecie dbać o polskich rolników i o polską wieś. Bo rząd Prawa i Sprawiedliwości zadbał, a szczególnie o te małe samorządy, które w ostatnich latach otrzymały naprawdę duże dofinansowanie z inwestycji strategicznych Polski Ład czy też z funduszu rozwoju dróg lokalnych. Chciałbym zadać pytanie: Czy rząd utrzyma te programy, które były adresowane do tych najmniejszych samorządów, gdzie naprawdę wiele inwestycji zostało zrealizowanych? Bo jakoś sobie nie przypominam, żeby za rządów Platformy Obywatelskiej były jakieś programy z polskich środków adresowanych do samorządów. Tak że warto te programy utrzymać. (Dzwonek) Chciałem również zapytać: Czy będą kontynuowane budowy dróg ekspresowych S8, S16, Via Carpatia? Dziękuję bardzo. (Oklaski) (Głos z sali: Ale wtedy samorządy miały stałe dofinansowanie…)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję. Pan poseł Marcin Bosacki, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Marcin Bosacki",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! 15 października Polki i Polacy zdecydowali, jakiego państwa już nie chcą, a jakie państwo chcą. Powiedzieli, po pierwsze, że nie chcą już państwa partyjnego, którego głównym zadaniem jest napychanie kieszeni członkom partii rządzącej, ich krewnym i znajomym. Chcą natomiast uczciwego państwa, które dba o interesy obywateli i pomaga im w ich życiu. Po drugie, odrzucili państwo oparte na ideologii, a tak naprawdę na zabobonnych, żeby wspomnieć tylko walkę z in vitro, a chcą państwa opartego na rozsądku, na umiarze i na nauce. I wreszcie po trzecie, odrzucili Polskę, która była osamotniona w świecie, w związku z czym osłabiona, a chcą silnej Polski w strukturach zjednoczonego Zachodu (Dzwonek), zarówno w NATO, jak i w Unii Europejskiej. Panie Premierze! Cieszę się, że te wszystkie rzeczy znalazły się w pana exposé i życzę panu… (Głos z sali: Niech żyje!) …i wszystkim członkom gabinetu koalicji 15 października determinacji w realizacji tych celów. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Jacek Tomczak, PSL – Trzecia Droga Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 716",
                },
                {
                    "speaker": "Poseł Jacek Tomczak",
                    "content": "Panie Marszałku! Wysoka Izbo! Żaden rząd tak nie zaszkodził polskim przedsiębiorcom jak rząd PiS-u. Dlatego dzisiaj ta szansa, ta zmiana jest wielką nadzieją dla polskiej gospodarki, dla polskich przedsiębiorców, zwłaszcza małych i średnich firm rodzinnych, ale także polskich rzemieślników. Pamiętamy te 40 kolejnych podwyżek różnych opłat, danin i podatków dla polskich przedsiębiorców. Pamiętają oni doskonale, jak ich przejechaliście Nowym Ładem, który podwyższył składkę zdrowotną, doprowadził do tego, że wiele firm… (Poseł Zbigniew Dolata: Jacek, ile dostałeś z…) …po tym Nowym Ładzie musiało się zamknąć. Pierwsze dwa kwartały po Nowym Ładzie to 150 tys. zlikwidowanych firm w wyniku waszego fantastycznego pomysłu. Dlatego ten rząd, który dzisiaj mówi ustami pana premiera… Będzie PIT kasowy, będzie szansa na odliczanie składki zdrowotnej. Daje to nową nadzieję polskim przedsiębiorcom. Na ten rząd liczą także polscy rzemieślnicy. (Dzwonek) Liczymy także bardzo na zmianę ustawy o rzemiośle.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Jacek Tomczak",
                    "content": "Dlatego pytanie, czy w planach rządu będzie też zmiana ustawy. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Zapraszam panią poseł Agatę Wojtyszek, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę, pani poseł.",
                },
                {
                    "speaker": "Poseł Agata Wojtyszek",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Mówił pan w swoim wystąpieniu o swojej koalicji jako o ruchu mówienia prawdy, zatem mam pytanie: Co jest prawdą, jeśli chodzi o zapewnienie bezpieczeństwa naszego kraju na granicy z Białorusią? Czy to, co mówili związani z pana obozem politycy, że trzeba będzie zaporę rozebrać, że zaporami w XXI r. nie robi się niczego, że minęły już czasy murów chińskich, żelaznych kurtyn itd., że dzisiaj to nie jest czas zapór? Przypomnę, że politycy pana koalicji byli przeciwni zaporze, kiedy przeznaczaliśmy na ten cel środki finansowe, obrażali strażników granicznych. Dziś mówi pan, że będzie granicy bronił. Czy tak będzie pan bronił jak emerytów, kiedy podniósł pan im wiek emerytalny do 67. roku życia, w tym kobietom na wsi o lat 12? Czy polityka miłości wobec nielegalnych imigrantów będzie wiązała się z likwidacją zapory i słowa „wpuśćmy ich, a potem zobaczymy (Dzwonek), kim są” staną się faktem? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję. Pan poseł Tomasz Zimoch, Polska 2050.",
                },
                {
                    "speaker": "Poseł Tomasz Zimoch",
                    "content": "Panie Marszałku! Wysoki Sejmie! Panie Premierze! 15 października skończyliśmy ten mecz, słaby, zły, nieciekawy. Rozpoczęliśmy nowy i wszystko zróbmy jako koalicja 15 października, by za 4 lata nikt nie krzyczał: panie premierze, kończmy ten mecz, ale by krzyczano: nie kończmy tego meczu. (Poseł Piotr Kaleta: Ale zawsze trzeba kiedyś skończyć.) A pytania zadam w systemie KRS. K jak Krajowa Rada Sądownictwa, źródło wszelkiego zła w wymiarze sprawiedliwości. Który pomysł naprawy KRS, panie premierze, i kiedy pojawi się w Sejmie? (Głos z sali: Ale nie ma premiera.) R jak radio. Wszyscy o telewizji, a przecież media publiczne to także radio, teatr wyobraźni. Jaki czas wyznaczył pan ministrowi kultury na uzdrowienie sytuacji i czy zapewni pan, że media publiczne nie będą wreszcie ramieniem żadnej partii politycznej? I S jak seniorzy. My już, panie premierze, do tej grupy należymy. Rocznik ’57 to bardzo dobry rocznik. (Dzwonek) O seniorach była mowa. S to także sport, o tym też już była mowa. S to także spotkania. Może warto przenieść do Sejmu zwyczaj z parlamentu brytyjskiego – spotkania premiera z posłami.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie.",
                },
                {
                    "speaker": "Poseł Tomasz Zimoch",
                    "content": "I zawsze takie spotkania rozpoczynaliby posłowie opozycji. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pan poseł Zbigniew Ziejewski, PSL. Bardzo proszę. (Głos z sali: Panie marszałku, czy ja mogę złożyć wniosek formalny?) Nie. (Głos z sali: Dlaczego nie?) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 717",
                },
                {
                    "speaker": "Poseł Zbigniew Ziejewski",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Chciałbym do pana premiera się zwrócić z dwoma prośbami, a mianowicie rząd PiS-u 17 września 2022 r. szumnie otwierał przekop Mierzei Wiślanej. Od tamtego czasu nic dalej się nie zrobiło. Pozostał odcinek 900 m do przekopania, pogłębienia toru wodnego. Miasto Elbląg czeka na pogłębienie tego toru. Rząd zaproponował, owszem, wykonanie pogłębienia tego toru wodnego, ale za przejęcie praw w spółce miejskiej. Pan prezydent Elbląga nie zgodził się na taki zapis. Mierzeja jest przekopana, a tor wodny niestety do dzisiaj nie jest pogłębiony. Kolejne pytanie. Jest tutaj pani minister Gembicka. Pani minister, jakie są efekty pani pracy? Pani na posiedzeniu komisji obiecała, że port w Gdyni, nabrzeże (Dzwonek) nie zostanie sprzedane, wydzierżawione na 30 lat. Chciałem się zapytać, czy to kukułcze jajo zostawi pani razem z panem ministrem Telusem nowemu rządowi…",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo serdecznie panu posłowi.",
                },
                {
                    "speaker": "Poseł Zbigniew Ziejewski",
                    "content": "…czy się uporaliście z tym problemem. Dziękuję bardzo. (Oklaski) (Głos z sali: To pytanie do premiera.)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Pan poseł Bartłomiej Dorywalski, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Bartłomiej Dorywalski",
                    "content": "Panie Marszałku! Wysoka Izbo! Pan premier mówił o drugiej waloryzacji emerytur i rent, gdy inflacja będzie przekraczała 5%. Tymczasem wielu ekonomistów prognozuje, że już za kilka miesięcy inflacja wyniesie poniżej 5%. Czy to oznacza, że waloryzacja emerytur będzie na poziomach jak za pierwszych rządów PO, czyli żenująco niska? 3,6 mln Polaków, co stanowi 27% osób zatrudnionych, zarabia najniższą krajową. W latach 2007–2015 imigracja zarobkowa Polaków objęła dziesiątki tysięcy polskich rodzin. W tym czasie minimalne wynagrodzenie za pracę wzrosło o 86%, z 936 zł do 1750 zł, a jego wysokość w połączeniu z wysokim bezrobociem była jednym z głównych impulsów do wyjazdu za granicę, w znacznej mierze do prac sezonowych, np. przy zbiorach szparagów w Niemczech. Od 2015 r. to wynagrodzenie wzrosło o 242%. Emigracja zarobkowa zmieniła się, wielu ludzi wróciło do Polski. W swoim exposé nie odniósł się pan premier do tego problemu, choć wskazał, że żyjemy w trudnych czasach. A zatem czy (Dzwonek) w trudnych czasach tempo podwyżek minimalnej płacy będzie w tej kadencji takie jak w latach 2007–2015, co z powrotem uczyni z naszego narodu tanią siłę roboczą państw wiodących w Unii Europejskiej? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Bardzo proszę panią poseł Iwonę Hartwich, Koalicja Obywatelska.",
                },
                {
                    "speaker": "Poseł Iwona Hartwich",
                    "content": "Panie Marszałku! Wysoka Izbo! Z największą dumą stoję tutaj dzisiaj, panie premierze, i dziękuję, że stanął pan obok wózków inwalidzkich i nas poniżonych, obdartych z godności opiekunów osób niepełnosprawnych. Dziękuję, że wspólnie zainicjowaliśmy projekt o podwyższeniu renty socjalnej. Dzisiaj przecież nie mogę pana pytać o to, czy będzie i kiedy będzie wyższa renta socjalna, bo przecież ja to wiem i pan to wie, że to jest już tylko formalność. Druk nr 30. Podczas protestu projekt obywatelski podpisały wszystkie formacje opozycyjne, oprócz oczywiście PiS-u. Ale problemów jest więcej. Niejednokrotnie, panie premierze, rozmawialiśmy o nich – wieloletnie zaniedbania, brak (Dzwonek) asystentów, brak opieki wytchnieniowej. Wierzę jednak mocno, że uda się je wszystkie rozwiązać. Jest pan dla nas nadzieją. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani poseł. Zapraszam teraz do zadania pytania panią poseł Annę Gembicką. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Anna Gembicka",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Rolnictwo to ważna gałąź polskiej gospodarki. Polscy rolnicy swoją ciężką pracą w trudnych warunkach gwarantują nam bezpieczeństwo żywnościowe. Z tego miejsca chciałabym podziękować wszystkim polskim rolnikom za ich ciężką pracę. Ale bezpieczeństwa żywnościowego nie utrzymamy bez kompleksowych, systemowych rozwiązań zapewniających opłacalność, stabilność, bezpieczeństwo pracy, zdobywanie nowych rynków zbytu, dlatego też przygotowałam odpowiednie projekty i złożyłam do wykazu prac rządu Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 718 Są gotowe rozwiązania. Natomiast pamiętając państwa ostatnie rządy, kiedy pogłowie trzody chlewnej spadło o 7 mln sztuk, kiedy podnieśliście wiek emerytalny dla rolniczek o 12 lat, kiedy sprzedaliście polskich rolników za 300 mln euro od Unii Europejskiej w zamian za wygaszanie polskich cukrowni… (Głos z sali: Nieprawda!) …chciałam zapytać (Dzwonek), czy tym razem dla odmiany zadbacie o polskie rolnictwo i jakie rozwiązania systemowe zaproponujecie polskim rolnikom. Dziękuję. (Oklaski) (Głos z sali: Zadbamy.)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani poseł. Zapraszam do głosu, pana posła Mariusza Witczaka. Proszę bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Mariusz Witczak",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Panie Premierze! Wczoraj pożegnaliśmy z radością najgorszy rząd po 1989 r. (Oklaski), władzę najbardziej antydemokratyczną w historii ostatniego 30-lecia, władzę najbardziej pazerną w ostatnich 30 latach i wreszcie władzę najbardziej zdemoralizowaną. Nastał dobry czas. Możemy teraz, szanowni państwo, przystąpić do naprawy Polski po Kaczyńskim. Chcę państwu powiedzieć, że u mnie w okręgu kalisko-leszczyńskim została na 8 lat zamrożona strategiczna inwestycja, bardzo dobry projekt, który został wprowadzony do dokumentów rządowych przez premier Ewę Kopacz. Polega on na przekształceniu drogi nr 25 w drogę o standardzie ekspresowym, która w ekspresowym standardzie łączy aglomerację kalisko-ostrowską z autostradą A2. (Dzwonek) Zwracam się z serdeczną prośbą do nowego rządu, nowego ministra infrastruktury już niebawem, do premiera Donalda Tuska o pilne zajęcie się tym ważkim problemem, który jest niezwykle wyczekiwany przez społeczność kaliską czy szerzej – społeczność aglomeracji kalisko-ostrowskiej. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Teraz zapraszam do zadania pytania pana posła Jacka Osucha. Proszę bardzo, panie pośle. (Poseł Robert Telus: Panie marszałku, czy z wnioskiem formalnym mogę?) Nie wiem, czy jest czas w tej chwili na wnioski formalne. Proszę bardzo, tylko bardzo krótko, proszę.",
                },
                {
                    "speaker": "Poseł Robert Telus",
                    "content": "Panie Marszałku! Wysoki Sejmie! W związku z tym, że nie ma na sali pana premiera, zgłaszam wniosek formalny, abyśmy zrobili przerwę, bo mógł wyjść, mógł się zmęczyć, żeby wrócił na salę, bo co to za zadawanie pytań, jak pana premiera nie ma na sali. (Poseł Sławomir Nitras: Ale my słuchamy, odpowiemy na każde pytanie.) Ale bez złośliwości, drodzy państwo. Wczoraj pan premier Morawiecki siedział cały czas i odpowiadał na pytania. (Głos z sali: Nie siedział cały czas.) (Głos z sali: Nie, wychodził.) Dziś pana premiera Donalda Tuska nie ma. (Głos z sali: Proszę nie kłamać.) Myślę, że nawet bez głosowania, bez złośliwości poczekajmy, jak wróci na salę. Wtedy będziemy dalej zadawać pytania. Dziękuję, panie marszałku. (Oklaski) (Głos z sali: Proszę nie robić obstrukcji i tak już straciliście władzę.)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo. Pani marszałek Monika Wielichowska. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Monika Wielichowska",
                    "content": "Panie Marszałku! Wysoka Izbo! Wczoraj pan premier Mateusz Morawiecki nie cały czas był na sali, natomiast ja jako prowadząca obrady owszem, tak. Dzisiaj gwarantuję państwu, że każde pytanie merytoryczne, które zadajecie, trafi do pana premiera, który za chwilę wróci na salę. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani marszałek. Szanowni posłowie, myślę, że wszyscy zdajemy sobie sprawę, że mamy tak wiele pytań. Liczba pytań do zadania wynosi jeszcze ok. 150, jeżeli dobrze widzę. Będziemy kontynuować tę serię pytań. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Jacek Osuch",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Pytanie kieruję do nieobecnego pana premiera Donalda Tuska. Kieruję je w trosce o szeroko pojęte dobro obywateli naszej ojczyzny. Panie premierze, czy wzorem poprzedniej pańskiej kadencji rządu będzie pan instrumentalnie wykorzystywał prezesa PSL w celu realizowania niekorzystnych dla Polaków reform takich jak podwyższenie wieku emerytalnego czy skandaliczna sprawa OFE? Drugie pytanie mam też do nieobecnego pana premiera, wicepremiera Kosiniaka-Kamysza: Czy pan Władysław Kosiniak-Kamysz uważa za zasadne wchodzenie po raz drugi do rządu Donalda Tuska… (Poseł Sławomir Nitras: Chyba nawet po raz trzeci, kolego.) …i firmowanie swoją twarzą kolejnych negatywnych rozwiązań ustawowych, zwłaszcza zmniejszenia potencjału obronnego Rzeczypospolitej poprzez zapowiadane ograniczenie liczebności i kontraktów zbrojeniowych Wojska Polskiego? (Dzwonek) Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam, pan poseł Piotr Borys. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Piotr Borys",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! Pan premier przedstawił kompleksową wizję państwa, które po 8 latach musi być odbudowane. Niszczenie instytucji państwa demokratycznego… Właściwie nie ma chociaż jednego obszaru, którego byście nie zniszczyli. Odbudowa sojuszy… (Głos z sali: Próba sojuszy.) …Polska silna, na nowo zintegrowana z Unią Europejską, z NATO – to wszystko jest perspektywą bezpieczeństwa państwa polskiego. Chciałem zapytać o jeden wycinek, który dotyczy nas wszystkich. To kwestia odpadów, których dziesiątki milionów ton wjechało za waszych rządów do Polski. (Głos z sali: To nieprawda!) Co możemy zrobić, szanowny panie premierze, aby zniwelować te nielegalne odpady? Na Dolnym Śląsku jest 40… W Głogowie, w mieście w moim okręgu, jest zmagazynowanych blisko 5 tys. beczek z ostrą chemią. Nie znaleźliście czasu, aby się tym zająć. Takich miejsc w Polsce są setki. To jest jedna ze spraw kluczowych dla bezpieczeństwa mieszkańców Polski (Dzwonek) w wielu miejscach, gdzie za waszej kadencji powstały nielegalne wysypiska. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam, pan poseł Ryszard Terlecki. Proszę bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Ryszard Terlecki",
                    "content": "Panie Marszałku! Wysoka Izbo! W kwietniu tego roku Sejm powołał komisję do spraw badania wpływów rosyjskich na polskie życie publiczne. W sierpniu Sejm mianował czy wybrał dziewięciu członków tej komisji. Komisja pracowała przez 3 miesiące. Przygotowała raport, który okazał się kompromitujący… (Poseł Sławomir Nitras: Dla komisji.) …dla osób, które komisja ocenia jako zagrażające bezpieczeństwu Polski, w tym premiera i ministrów obrony oraz ministrów koordynatorów służb, po czym Sejm po wyborach, właściwie natychmiast po uruchomieniu, w panice odwołał członków tej komisji. Chciałem spytać, co dalej będzie z komisją do spraw badania wpływów, bo sprawa wydaje się kluczowa dla bezpieczeństwa Polski. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam, pan poseł Jakub Rutnicki. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Jakub Rutnicki",
                    "content": "Bardzo dziękuję. Panie Marszałku! Wysoka Izbo! Panie Premierze! Tutaj posłowie PiS-u często mówią o bezpieczeństwie. Niedawno poseł Zieliński, kiedyś minister, pytał, czy Platforma, Koalicja zapewni bezpieczeństwo. Chciałem państwu przypomnieć, bo miliony Polaków nas oglądają, jak policjanci nie mogli wychodzić na ulice polskich miast na patrole, ponieważ musieli wycinać konfetti, którego zażyczył sobie pan minister Zieliński – taka była u was prawda. Szanowni Państwo! Jaka jest różnica? Mówicie o tłustych kotach. Mamy tutaj pana Kowalskiego, który w spółkach Skarbu Państwa zarobił 2,5 mln zł. A my chcemy od 1 stycznia dać podwyżkę nauczycielom, 30%. I tym się, szanowni państwo, różnimy. Wy postanowiliście odebrać młodym rodzinom szansę na posiadanie dziecka, szczególnie tym osobom, które dzieci nie mogły mieć, odebraliście in vitro. Co robi nowa koalicja? Chce (Dzwonek) przywrócić in vitro od 1 czerwca, szanowni państwo. Koalicja Obywatelska to konkrety: podwyżki dla nauczycieli, podwyżki dla budżetówki, ułatwienia dla przedsiębiorców, a wy – ciągły hejt i próba dyskredytacji. Na szczęście ludzie to widzą. Szczęśliwej Polski już czas. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam, pan poseł Jarosław Sellin. Proszę bardzo. 1. posiedzenie Sejmu w dniu 12 grudnia 2023 r. Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                },
                {
                    "speaker": "Poseł Jarosław Sellin",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wczoraj pana przyjaciel, przedstawiając pana sylwetkę, powiedział osobiście, że pan kocha malarstwo i muzykę. Ja w to wierzę, tylko w związku z tym mam pytanie, dlaczego w czasie 8 lat pana rządów kultura była lekceważona w wymiarze, można powiedzieć, liczbowym. Na kulturę pan przeznaczał w budżecie niecałe 3 mld zł rocznie, a my doprowadziliśmy do sytuacji, kiedy jest na nią ok. 8 mld zł rocznie. W związku z tym pytanie, czy będziecie kontynuować ambitną politykę kulturalną, która wyraża się w takim wymiarze liczbowym. Dzisiaj ostatni dzień pełnię funkcję generalnego konserwatora zabytków. Muszę panu powiedzieć, że na zabytki w ciągu 8 lat naszych rządów przeznaczyliśmy 10 razy więcej środków niż wy w ciągu 8 lat waszych rządów. (Dzwonek) Tu jest 8 lat i tu jest 8 lat. Ok. 6 mld zł w czasie naszych rządów, 636 mln zł w czasie waszych. Pytanie, czy ta ambitna polityka kulturalna i ochrona dziedzictwa narodowego będzie kontynuowana, czy będzie zwijana. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Pani poseł Agnieszka Górska. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Agnieszka Górska",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! Czy w związku z zapowiedzią reformowania Trybunału Konstytucyjnego i odwoływania sędziów, którzy złożyli ślubowanie przed polskim prezydentem, zamierza pan dalej kwestionować prezydenturę Andrzeja Dudy i mówić, że moralnie prezydentem jest Rafał Trzaskowski? Czy też wobec wczorajszego przedstawienia kandydatury marszałka Hołowni jako waszego wspólnego kandydata na prezydenta jednak porzucił pan myśl o kandydaturze Trzaskowskiego i nie będzie pan kwestionował prezydentury Andrzeja Dudy, i łamał polskiej konstytucji? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani poseł. Pan poseł Witold Zembaczyński. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Witold Zembaczyński",
                    "content": "Szanowny Panie Marszałku! Wielce Szanowny Panie Premierze! Szanowne Osoby Poselskie! Tymi gołymi rękami obaliliśmy reżim Kaczyńskiego. Reżim ten zwał się spin dyktaturą – dyktaturą, w ramach której władza ma wpływ na obywatela przez propagandę sianą w mediach publicznych. Stąd moje pytanie do szanownego pana premiera: Czy będziemy brali pod rozwagę powołanie komisji śledczej do spraw propagandy, która prześwietliłaby przepływy finansowe między prawicowymi mediami suto karmionymi przez rząd PiS-u, taśmociąg między ulicą Nowogrodzką a nadajnikiem TVP Info, a przede wszystkim to, co mogliśmy znaleźć m.in. w mailach Dworczyka? W jaki sposób były konstruowane nagonki na rodzinę Magdy Filiks, na Pawła Adamowicza? Chodzi też o to, w jaki sposób była konstruowana hejterska nagonka na sędziów, i wiele innych bulwersujących spraw, gdy każdego dnia propaganda na wysokim poziomie była sączona (Dzwonek) po to, żeby mieć trzymanie na obywateli. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam pana posła Zbigniewa Dolatę. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Zbigniew Dolata",
                    "content": "Panie Marszałku! Wysoka Izbo! Gdyby dzisiejsze exposé porównać do zupy grzybowej, w której konkrety to grzyby jadalne, a kłamstwa to trujaki, to borowikowych konkretów byłoby jak na lekarstwo, taka wodnista breja, natomiast byłoby zagęszczenie sromotnikowych kłamstw. To taka gęsta pulpa, którą chcecie nakarmić Polaków. (Poseł Sławomir Nitras: Minę ma pan taką, jakby pan jadł.) Mam pytanie dotyczące konkretnej sprawy, podwyżek dla sfery budżetowej, zwłaszcza dla nauczycieli. To dobrze, że podwyższacie te płace, ale mam pytanie: Czy nie powtórzy się sytuacja z 2012 r., 2013 r., 2014 r. i 2015 r., kiedy zamroziliście płace sfery budżetowej, w tym nauczycieli? Prawo i Sprawiedliwość musiało podwyższać te płace. Podwyższyliśmy (Dzwonek) płace nauczycieli przeciętnie o 47%, płace początkujących nauczycieli o 76%. Mam pytanie: Czy stworzycie mechanizm powiązania płac w sferze budżetowej, płac nauczycieli ze średnią krajową? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam pana posła Jacka Karnowskiego. Proszę bardzo Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                },
                {
                    "speaker": "Poseł Jacek Karnowski",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Przez 8 lat centralizacji kraju i niszczenia samorządności czekaliśmy na te wspaniałe słowa o wspólnocie, o wspólnocie naszych miast i gmin. Czekaliśmy na słowa o decentralizacji. Czekaliśmy na słowa o odejściu od czeków przyznawanych niesprawiedliwie tylko swoim, tylko tym, którzy głosowali na prezydenta Dudę. Czekaliśmy na to, żeby te czeki nie decydowały o tym, czy w Sopocie będzie remontowana ulica Dworcowa, Kolejowa czy 3 Maja, chociaż akurat tutaj pan premier Tusk byłby bardzo kompetentny. (Głos z sali: Wnioski pan składał?) Czekaliśmy na te pieniądze, na dochody własne, na środki unijne, które umożliwią nam realizację KPO. Bardzo dziękujemy za ten dzisiejszy konkret, za tę podwyżkę pensji dla nauczycieli w przedszkolach o 30%, bo to (Dzwonek) uratuje dochody własne bardzo wielu gmin i miast. Panie Premierze! Mam jedno pytanie: Kiedy możemy spodziewać się nowelizacji ustawy o finansach gmin i miast? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam pana posła Piotra Kaletę. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Piotr Kaleta",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Szanowni Państwo! Wiem, że może przyjdzie czas na to, żeby robić sobie bekę z tego wszystkiego, co zostało tutaj dzisiaj powiedziane, ponieważ w bardzo wielu wystąpieniach, przede wszystkim wystąpieniach posłów z tej strony, mogliśmy usłyszeć coś w rodzaju: łubu-dubu, łubu-dubu, niech nam żyje prezes naszego klubu. Proszę państwa, chciałbym też to ująć, ponieważ usłyszeliśmy dzisiaj również o składzie rządu, przyszłego rządu. Skoro kiedyś pan premier Donald Tusk powiedział, że Sławomir Nowak jest więźniem politycznym, to chciałbym zapytać, dlaczego zabrakło dla niego miejsca w rządzie, który się tworzy. Skoro jest więźniem politycznym, już dawno powinien być tutaj razem z nami, jeżeli możemy w ten sposób podchodzić do tych spraw. Powiem jeszcze o jednej sprawie. Dzisiaj pośród tych bardzo wielu złych informacji, żeby tak delikatnie to określić, jeśli chodzi o personalny skład przyszłego rządu, usłyszeliśmy również, że zasiądzie tam pan Sławomir Nitras. Mam prośbę, panie premierze, żeby bardzo mocno (Dzwonek) zachęcić go do tego, żeby pilnował spraw antydopingowych w polskim sporcie. Dziękuję uprzejmie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam teraz panią poseł Martę Wcisło. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Marta Wcisło",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Najlepszą drogą dla Polski jest droga postępu i wolności. Tę drogę wolności wybrali 15 października obywatele naszego kraju, budując koalicję narodowego odrodzenia i dobrej przyszłości opartej na solidarności i społeczeństwie obywatelskim, dając świadectwo wolności i determinacji. Po 8 latach następuje historyczna zmiana rządu i premiera, ale to też zmiana sposobu myślenia i zarządzania. Chodzi o zarządzanie oparte na fundamencie praworządności i demokracji. Skończyły się rządy bezprawia i niesprawiedliwości. Skończyły się wasze rządy. Wkurzyliście Polaków bardziej niż komuna, bo kto sieje wiatr, ten zbiera burzę. 15 października powstała koalicja, powstał rząd, na czele którego stoi Donald Tusk. Jutro, 13 grudnia, w tym symbolicznym dniu, kiedy (Dzwonek) odbierano nam wolność, te rządy sprawiedliwości, te rządy wolności zostaną zaprzysiężone. (Oklaski) Panie Premierze! Polska Wschodnia, Lubelszczyzna, która była przez was tak bardzo oszukiwana i ograbiana, rolnicy, górnicy, pracownicy zakładów azotowych… (Głos z sali: Kłamstwo.) …czekają na ten rząd, czekają na prawdziwie kompetentny rząd. Szczęśliwej Polski już czas. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani poseł. Teraz pan poseł Janusz Kowalski. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Janusz Kowalski",
                    "content": "Panie Marszałku! Panie Premierze! Szanowna Nowa Lewicowa Opozycjo! Twarda deklaracja – jesteśmy merytoryczną opozycją. Popieramy i poprzemy projekt: czyste ręce. Procedujmy nad nim jak najszybciej, ponieważ mamy nie tylko czyste ręce, ale także czyste intencje. (Oklaski) Proponujemy kilka zmian, m.in. obowiązek ujawniania przez marszałków, prezesa Rady Ministrów i ministrów wszystkich dochodów ze źródeł zagranicznych i krajowych oraz wszystkich darowizn na dzieci i na małżonków z ostatnich 10 lat. (Poseł Sławomir Nitras: Finansowanie partii.) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów Chcemy wprowadzić taki zapis. Ufam, że go poprzecie, żeby żaden polski polityk nie został już bohaterem takiej książki jak „Wszystkie pionki Putina” Kacpra Płażyńskiego. Mam pytanie do pana premiera. Obiecał pan, że odpowie pan na wszystkie pytania. Ufam, że odpowie pan na proste, banalne pytanie Janusza Kowalskiego. (Głos z sali: Dlaczego nie przyjął pan kwiatów?) Proszę ujawnić, jakie łącznie miał pan dochody w latach 2014–2019 razem ze świadczeniem przejściowym do 2021 r. z Brukseli. (Dzwonek) Konkretna, łączna kwota z pana PIT-ów za lata 2014–2021. (Poseł Krystyna Skowrońska: Po co to Januszowi?) Miliony Polaków chcą to usłyszeć, a zapewniam państwa, że Donald Tusk na to pytanie Januszowi Kowalskiemu nie odpowie. (Głos z sali: A ile ty zgarnąłeś w spółkach Skarbu Państwa?)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. (Gwar na sali) Ale bardzo proszę… Po co te emocje? Zapraszam panią poseł Annę Wojciechowską. Proszę bardzo, pani poseł.",
                },
                {
                    "speaker": "Poseł Anna Wojciechowska",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Przyszłam tutaj, żeby przypomnieć globalny kryzys finansowy w latach 2008–2010. Zaczęło się to, proszę państwa, zapaścią na rynku pożyczek hipotecznych w Ameryce. Na pewno panowie powinni to doskonale pamiętać. I cały świat odczuł ten kryzys bardzo boleśnie: setki tysięcy zwolnień i recesja, za mało czasu, żeby o tym w szczegółach opowiedzieć. Tragiczna sytuacja była wtedy np. w Grecji, w Hiszpanii, w Irlandii i w innych krajach europejskich. I to był czas rządów pana premiera Tuska. To dzięki pana polityce, panie premierze, Polska ucierpiała wtedy w niewielkim stopniu. W 2010 r. inflacja w naszym kraju była na poziomie 2,6%. Mnóstwo inwestycji, wsparcie dla małych i średnich przedsiębiorstw, dodatnie PKB, jedyne w Europie. I z taką rosnącą gospodarkę przejął PiS. I co z tym zrobił? Sprzeniewierzył. (Dzwonek) Bezprawie, łamanie konstytucji, potężna inflacja, kryzys energetyczny, korupcja. Można byłoby wymieniać i wymieniać. I panie premierze, jest pan naszą ostatnią nadzieją w tej sytuacji. Tak jak w tamtym kryzysie, przeprowadzi pan Polskę tzw. suchą stopą. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani poseł. Zapraszam teraz pana posła Krzysztofa Szczuckiego. (Poseł Sławomir Nitras: To jest ten od niepublikowania wyroków.) Proszę bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Krzysztof Szczucki",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Jakiś czas temu powiedział pan, że będzie pan stosował prawo w taki sposób, jak pan je rozumie. Chciałbym zapytać, czy w ramach pańskiego rozumienia prawa planuje pan odwołać legalnie działających, zgodnie z prawem, sędziów Trybunału Konstytucyjnego. Czy w ramach prawa, tak jak pan je rozumie, zamierza pan odwołać członków Krajowej Rady Sądownictwa, do której zresztą powołaliście swoich przedstawicieli? Czy w ramach tego prawa zamierza pan zawiesić, a w konsekwencji doprowadzić do odwołania wbrew polskiej konstytucji prezesa Narodowego Banku Polskiego? Czy w końcu w ramach tego prawa, jak pan je rozumie, zamierza pan doprowadzić do zmian w mediach publicznych, niezgodnie z ustawą o radiofonii i telewizji i niezgodnie z ustawą o Radzie Mediów Narodowych? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam pana posła Bartosza Zawieję. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Bartosz Zawieja",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! SOS dla instytutów naukowo-badawczych. W 2019 r. powstała sieć naukowa Łukasiewicz, która w swoim zamyśle włączyła do jednej jednostki 37 niezależnych do tamtej pory instytutów naukowo-badawczych. Co się stało? Ich struktura została w taki sposób scentralizowana, że ówczesne rozporządzenie ministra nauki regulowało, czym dany naukowiec i w jakim instytucie ma się zajmować. W poprzednim roku, czyli na początku 2022 r., powstał Poznański Instytut Technologiczny. Do jednej jednostki ponownie włączono wieloletnie doświadczenia, wspaniały dorobek naukowy instytutów, takich jak instytuty pojazdów szynowych, obróbki plastycznej czy technologii drewna. Wymieszano wszelkie możliwe dziedziny. Proszę pana premiera o jedną rzecz w imieniu poznańskich naukowców (Dzwonek), aby wstrzymał kolejną deformę tej organizacji, która ma nastąpić w styczniu przyszłego roku, aby poza uczelniami wyższymi również instytuty naukowe miały autonomię, przywróconą autonomię. Bardzo dziękuję. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. I zapraszam panią poseł Annę Dąbrowską-Banaszek. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Anna Dąbrowska-Banaszek",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! W ostatnich latach wiele dobrego wydarzyło się w Polsce. Wiele inwestycji rozpoczęto, wiele już ukończono, wiele jest w trakcie realizacji. Zapytam o trzy z nich. W lipcu br. obchodziliśmy 80. rocznicę rzezi wołyńskiej – wydarzenia, którego ofiary wciąż czekają na godziwe upamiętnienie. Sejm przyjął wówczas uchwałę mówiącą o tym ludobójstwie. Potomkowie ofiar wciąż czekają na ekshumację i godziwy pochówek swoich bliskich. Ofiary wołają o pamięć. Dotychczas nie ma na świecie miejsca, gdzie w godziwy sposób byłyby upamiętnione tamte wydarzenia, prowadzone byłyby prace, gromadzone dokumenty. W Chełmie ponad 3 lata temu ponad podziałami wszyscy radni wszystkich opcji podjęli inicjatywę wypełnienia tego zobowiązania wobec zamordowanych wówczas na Wołyniu Polaków i ich potomków. Powstał projekt budowy Muzeum Ofiar Rzezi Wołyńskiej i Centrum Prawdy i Pojednania. Obecnie rozpoczęła się wspólna realizacja budowy tego muzeum przez miasto Chełm i Ministerstwo Kultury i Dziedzictwa Narodowego. Moje pytanie, panie premierze: Czy realizacja tego projektu będzie kontynuowana? (Dzwonek) Jeszcze żyją świadkowie wydarzeń na Wołyniu, którzy czekają na to już 80 lat. Zapytam o obwodnice miast, które poprawiają komfort życia mieszkańców, są ważną strategicznie infrastrukturą, która decyduje o bezpieczeństwie, rozwoju, możliwości szybkiego dotarcia do innych części kraju. (Poseł Krystyna Skowrońska: Morawiecki nie załatwił?) Jednym z takich jest Chełm: dwie zaplanowane obwodnice – północna, już budowana, i południowa, wpisana na listę inwestycji strategicznych przez MON. Czy jej budowa będzie realizowana? A kolejne pytanie dotyczy Linii Chełmskiej Szerokotorowej. Posłowie PO wspierali jej powstanie i dopytywali o jej losy. Chciałabym również zapytać o losy LChS-u? Proszę o odpowiedź na pytania. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani poseł. I teraz zapraszam pana posła Piotra Kandybę. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Piotr Kandyba",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Szanowny Panie Premierze! Mam trzy krótkie prośby w następujących tematach. Media publiczne niech nas informują i edukują w paśmie wysokiej oglądalności o ważnych tematach społecznych: depresja, uzależnienia, profilaktyka zdrowia czy ekologia. Nie nadążamy z tymi tematami poniżej, w samorządach. Kolejna rzecz, samorządy. Rewizja janosikowego, unormowanie wpływów z PIT-u, zwiększenie subwencji oświatowej, bo nie starcza, przywrócenie rozmowy na temat ustawy metropolitalnej ważnej dla Warszawy i dużych aglomeracji. Po trzecie, umiejscowienie w Sejmie tablicy z manifestem zwykłego, szarego człowieka, którego pan cytował. Te 15 postulatów powinno zostać upamiętnione w Sejmie w godnym miejscu, aby nigdy nie dopuścić do powtórki rządów bezprawia i niesprawiedliwości. Na koniec zacytuję wiadomość (Dzwonek), którą otrzymałem i która oddaje nastroje wielu Polek i Polaków: wystąpienie Donalda Tuska było znakomite. PiS jest na politycznym oucie. Szczęśliwej Polski już czas. Dziękuję. (Głos z sali: Łubu-dubu, łubu-dubu.)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo. Proszę posłów PiS o powstrzymanie się od śpiewów na sali sejmowej. Chciałbym jeszcze pozdrowić przysłuchujących się naszym obradom na galerii Sejmu uczniów ze szkoły podstawowej nr 9 w Sopocie. Pozdrawiamy serdecznie. (Oklaski) Oddaję głos. Pytanie zadaje pan poseł Marcin Horała. Proszę bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Marcin Horała",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Panie premierze, niestety skłamał pan w swoim exposé, mówiąc o osobach poszkodowanych w wyniku wywłaszczeń pod CPK. Ile osób zostało wywłaszczonych pod CPK? Zero. Nabyliśmy 1200 ha w drodze dobrowolnych nabyć, zwykłej cywilnej umowy kupna–sprzedaży. Oferowaliśmy warunki dużo lepsze niż przy wywłaszczeniach i dlatego właściciele dobrowolnie zgodzili się na sprzedaż. Natomiast to za pana rządów wywłaszczenia były jedyną metodą pozyskiwania gruntów pod inwestycje. Mówił pan, że wtedy nie było protestów. Wydrukowałem drobny ułamek artykułów z tamtych lat na temat protestów przy wywłaszczeniach pod inwestycje. Jeden króciutki cytat: W 2011 r. na bezbronnego człowieka przyjechało pięć radiowozów Policji, sześć wozów firmy ochroniarskiej, antyterroryści z ostrą amunicją. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów Rzeczy zostały spakowane, wywiezione, dom wyburzyli i jeszcze kazali zapłacić 19 tys. zł za tę operację. Tak wywłaszczano za pana rządów. (Dzwonek) Panie premierze, kampania się skończyła. Dosyć kłamstw, dosyć manipulacji na temat CPK. (Poseł Krystyna Skowrońska: Horała, kłamałeś najwięcej.) Budujcie ten strategiczny, ważny dla przyszłości Polski projekt. Wszystko jest przygotowane, byle tego nie zepsuć. Pytanie, czy można mieć jakąś nadzieję, że tego programu nie zepsujecie. (Poseł Donald Tusk: Może mi pan dać ten plik? Chętnie obejrzę.) Proszę uprzejmie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Jak widzimy, pan poseł wręczył premierowi swoje papiery. Niektórzy na transmisji dopytują, ile jeszcze jest pytań, więc poinformuję, że jest jeszcze 129 pytań. Zapraszam, pan poseł Marek Krząkała.",
                },
                {
                    "speaker": "Poseł Marek Krząkała",
                    "content": "Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! W czasie rozmów z ludźmi w trakcie kampanii często przewijały się tematy drożyzny, szalejącej inflacji, ale też środków marnowanych przez różnego rodzaju prorządowe fundacje czy instytucje, chociażby spółkę CPK. Myślę, że społeczeństwo powinno dowiedzieć się, jaki jest rzeczywisty stan finansów państwa, ile wynosi zadłużenie – jednym słowem, jaki jest punkt wyjścia dla nowego rządu. W exposé wspomniał pan, panie premierze, o stabilności finansowej. Ta stabilność finansowa będzie osiągnięta, jeżeli stabilna będzie nasza gospodarka, dlatego czy nie należałoby zacząć jak najszybciej nie tylko od audytu i przeglądu finansów we wszystkich ministerstwach i instytucjach podległych rządowi, lecz także pokazania, jak ucierpiała nasza gospodarka z powodu braku uruchomienia środków z KPO, ile firm zostało zamkniętych (Dzwonek), jakie dramaty przeżywały małe i średnie przedsiębiorstwa, bo to jest niezwykle istotne. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam, pan poseł Norbert Kaczmarczyk. Proszę bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Norbert Jakub Kaczmarczyk",
                    "content": "Bardzo dziękuję. Panie Marszałku! Wysoka Izbo! Panie Premierze! Chciałbym zapytać o kwestie związane z polskim samorządem, dlatego że podczas tych wystąpień i pytań padło bardzo wiele zarzutów dotyczących uznaniowości kwot przyznawanych z Polskiego Ładu dla polskich samorządów. Wnioskuję o to, aby pan premier zapytał tych samorządowców, którzy są związani chociażby z waszą koalicją… Samorządowcy, bardzo dobrzy specjaliści, z którymi współpracuję i których znam z okręgu nr 15, np. Jan Pająk – wójt gminy Drwinia, kandydat Trzeciej Drogi do Sejmu, pan Marcin Gaweł – wójt gminy Pałecznica, pan Tomasz Latocha – burmistrz Brzeska, pan Marek Słowiński – wójt gminy Radziemice korzystali z wielomilionowych dotacji z Polskiego Ładu. To nie był uznaniowy program, to był program dla wszystkich. Oni już dzisiaj pytają, czy ten program będzie kontynuowany, dlatego że żaden system podatkowy nie jest w stanie spowodować, że gminy np. do 20 tys. mieszkańców będą mogły inwestować np. 30 mln zł (Dzwonek) w swoje małe ojczyzny. Dlatego proszę powiedzieć, jak ten system będzie wyglądał, by te małe gminy mogły równie dużo inwestować. Bardzo dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam do głosu, pan poseł Artur Gierada. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Artur Daniel Gierada",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Panie premierze, na wstępie wielkie gratulacje od mieszkańców Kielc i województwa świętokrzyskiego. Dzisiaj dostałem dziesiątki SMS-ów zarówno z prośbą o przekazanie panu życzeń, jak i będących wyrazem wielkiej nadziei, jaką niesie pana wybór. Nawiążę trochę do wątków regionalnych i tego, o czym mówił wczoraj niedoszły premier Mateusz Morawiecki, chwaląc się, jak to bardzo Polska wschodnia była dofinansowana za rządów PiS. W województwie świętokrzyskim tak nie było. To jest kłamstwo, panie premierze. Nie da się nawet porównać 8 lat rządów Platformy Obywatelskiej z 8 latami rządów Prawa i Sprawiedliwości. Przypomnę jedną z pierwszych decyzji Ewy Kopacz – zmiana finansowania służby zdrowia i większe pieniądze dla pacjentów zarabiających mniej. (Głos z sali: Dla pacjentów? A od kiedy pacjentów…) Pamiętam dofinansowanie Targów Kielce, powstanie centrum ekspedycyjno-rozdzielczego Poczty Polskiej, wielkie pieniądze na Politechnikę Świętokrzyską, akademię świętokrzyską czy powołanie uniPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów wersytetu z wydziałem medycznym, który był marzeniem pokoleń kielczan. (Dzwonek) Panie premierze, drogi. Za naszych czasów wybudowano ponad 100 km dróg w systemie ekspresowym. Wiecie, ile wy wybudowaliście przez wasze 8 lat dróg w systemie ekspresowym w województwie świętokrzyskim? Ani 1 km. Panie Premierze! Liczymy na pana wsparcie. Mieszkańcy województwa świętokrzyskiego bardzo na pana liczą. Dziękuję bardzo. (Oklaski) (Poseł Henryk Kowalczyk: I po co takie kłamstwa?)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Zapraszam, pan poseł Jacek Bogucki. Proszę bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Jacek Bogucki",
                    "content": "Panie Marszałku! Wysoka Izbo! Przyszły Panie Premierze! Nawet byłbym w stanie uwierzyć, że pan po powrocie z emigracji zarobkowej do Brukseli nawrócił się na polskość, że już nie będzie niszczenia polskiej gospodarki, wyprzedaży choćby polskiej hodowli zwierząt, że już nie będzie tak, że brakuje jakiejkolwiek pomocy dla rolników, dla Polski Wschodniej, ale ta moja wiara, wiara w człowieka, nawet gdy zaproponował pan nam rewolucję październikową, nazywając ją dla zmyłki koalicją październikową, koalicją miłości, jest niewielka po waszych działaniach. (Poseł Donald Tusk: Oż ty, mądry to ty nie jesteś, chłopie.) I tylko dwa przykłady. Ustawa wiatrakowa to było bronienie interesów dużego podmiotu gospodarczego, ale niemieckiego, który bankrutuje, producenta wiatraków. (Głos z sali: To po co żeście podpisali umowę z…) I drugi przykład to obciążenie tylko polskiej spółki na rzecz czynników energetycznych, a zwolnienie z tych obciążeń podmiotów zachodnich. (Poseł Krystyna Skowrońska: I bardzo dobrze.) A więc jeśli już cytujecie jedną z pięknych piosenek, to powiedzcie dalej: bo nadzieję dając wam, fałszywy klejnot dał. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. Pani poseł Agnieszka Hanajczyk. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Agnieszka Hanajczyk",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Po 8 latach chaosu wreszcie Polska odetchnie. Jestem tego pewna. Bardzo cieszą mnie zapowiedzi pana premiera o niezwłocznej i intensywnej pracy dyplomatycznej, przede wszystkim w sprawie tak potrzebnego i oczekiwanego KPO. Środki z KPO blokowane przez PiS to szansa na likwidację składowisk odpadów niebezpiecznych. To szansa na rozbrojenie bomby ekologicznej, jednej z największych i najgroźniejszych bomb ekologicznych, takich jak w Zgierzu. Panie Premierze! Polacy to ludzie o wielkich sercach i empatii, także wobec zwierząt. PiS przez 8 lat nie zrealizował ani piątki, ani czwórki, ani nawet jedynki dla zwierząt. We wrześniu odwiedził pan schronisko dla zwierząt. To miejsce szczególnej troski o bezdomniaków. Najważniejsze jednak jest to, aby takie schroniska (Dzwonek) były niepotrzebne. Proszę w imieniu swoim, zwierzolubów, ale także samych zwierząt, by walka o zwierzęta, eliminowanie bądź ograniczanie cierpień zwierząt i systemowa walka z bezdomnością były stałym punktem programu rządu koalicji 15 października. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani poseł. Zapraszam panią poseł Teresę Pamułę. Proszę bardzo, pani poseł.",
                },
                {
                    "speaker": "Poseł Teresa Pamuła",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Pada z tej mównicy wiele słów nieprawdziwych ze strony Platformy Obywatelskiej czy Trzeciej Drogi o funduszach dla gmin i samorządów. Panie Premierze! To jest nieprawda. Chciałam przypomnieć, że tylko dla powiatu lubaczowskiego 250 mln zł wpłynęło w ramach tego funduszu. Chciałam też panu powiedzieć, że w okręgu nr 22, który reprezentuję, 54,5% Polaków głosowało na Prawo i Sprawiedliwość, a tylko 13% – na Koalicję Obywatelską. I chciałabym wierzyć, że te słowa, które tutaj padły z pana strony, będą prawdziwe: że S19 będzie budowana, że środki na samorządy (Dzwonek) będą przeznaczane. Jeszcze chciałam zapytać, dlaczego w Parlamencie Europejskim osoby, które szły do wyborów z listy Koalicji Obywatelskiej, głosowały za poprawkami i brakiem głosu dla Polski, tego głosu, który mamy w Unii Europejskiej. Nie pozwolimy na to, żeby głos Polski był niesłyszalny i żeby nie było w Unii Europejskiej prawa głosu i prawa weta. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, pani poseł. I teraz pani poseł Małgorzata Niemczyk. (Wypowiedź poza mikrofonem) Panie pośle, w jakim trybie? (Poseł Witold Zembaczyński: W związku z wnioskiem formalnym, który musi mieć miejsce.) Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Witold Zembaczyński",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Przed chwilą doszło do niebywałego zdarzenia. Została przerwana uroczystość o charakterze religijnym. To jest niedopuszczalne. Poseł Braun, dokonując napaści na uroczystości religijne na polskiej ziemi, gdzie wydarzył się Holokaust… (Głos z sali: Skandal!)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Panie pośle, czy to jest wniosek formalny? Jeżeli tak, z jakiego punktu?",
                },
                {
                    "speaker": "Poseł Witold Zembaczyński",
                    "content": "…dokonał aktu hańbiącego. Dlatego wnoszę o przerwanie obrad, wezwanie pana posła Brauna do Prezydium Sejmu celem wykluczenia z obrad. (Oklaski) Na polskiej ziemi, gdzie wydarzył się Holokaust, nie ma miejsca, przestrzeni na akty antysemickie pod dachem Wysokiego Sejmu. (Oklaski) (Poseł Donald Tusk: Ale powiedz, co tam się stało.) (Głos z sali: Powiedz, co się stało.) (Poseł Grzegorz Braun: W trybie sprostowania, panie marszałku?) Doszło do ataku polegającego na zgaszeniu świec chanukowych przy użyciu gaśnicy przez tego oto ekstremistę, co jest bezpośrednią napaścią (Dzwonek) na akt religijny, i na takie zachowanie nie ma w tej Izbie tolerancji. Podtrzymuję mój wniosek. (Oklaski) (Głos z sali: Skandal!)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Panie pośle, dziękuję bardzo. (Poseł Grzegorz Braun: W trybie sprostowania, panie marszałku?) Już, panie pośle. Rozumiem, że pański wniosek jest kierowany do Prezydium Sejmu. Przy najbliższym spotkaniu w Prezydium pański wniosek przekażę. (Gwar na sali) (Głosy z sali: Nie, teraz.) (Głos z sali: Przekaż, przekaż!) (Głos z sali: Może pan zrobić teraz przerwę.) (Głos z sali: Teraz przerwę zrobić.) Oczywiście, że mogę, tak jest. Panie pośle, w jakim trybie? (Poseł Grzegorz Braun: W trybie sprostowania. Zostało wymienione moje nazwisko w kontekście niewątpliwie zmanipulowanym, krzywdzącym.) (Poseł Krystyna Skowrońska: Tu nie ma sprostowania.) (Poseł Witold Zembaczyński: Nie, panie marszałku…) Bardzo proszę, w trybie sprostowania.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "W trybie sprostowania. Wysoka Izbo! Nie może być miejsca na akty rasistowskiego, plemiennego, dzikiego, talmudycznego kultu na terenie Sejmu Rzeczypospolitej Polskiej. (Gwar na sali) (Głos z sali: Chamstwo!) (Głos z sali: Skandal!) Jak rozumiem, przez zebranych przemawia ignorancja. Nie jesteście państwo świadomi przesłania, treści tego aktu, zwanego niewinnie świętami Chanuka. Jest to… (Głos z sali: Zejdź stamtąd.) (Głos z sali: Wstyd!) (Głos z sali: Wyłączyć mikrofon.) (Głos z sali: Wykluczyć, wykluczyć!)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Panie pośle, proszę odnieść się do słów, które pana dotyczyły, jeżeli pan wypowiada się w trybie sprostowania.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Panie Marszałku! Przypisano mi tutaj pobudki rasistowskie, gdy tymczasem ja właśnie przywracam stan normalności i równowagi, kładąc kres aktom satanistycznego, talmudycznego, rasistowskiego triumfalizmu… (Poruszenie na sali) (Głos z sali: Pan marszałek nie widział…) (Głos z sali: Panie marszałku, niech pan przerwie, to jest wstyd dla Sejmu.) (Głos z sali: Hańba!) (Głos z sali: Panie marszałku, niech pan przywróci powagę…)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Bardzo dziękuję, panie pośle",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "…ponieważ takie jest przesłanie tych świąt. Wyzywam państwa na dysputę teologiczną. Chętnie podzielę się informacjami, które do państwa nie dotarły. (Gwar na sali) (Poseł Monika Wielichowska: Czas minął.) (Głos z sali: Panie pośle, pan zejdzie.) (Głos z sali: Niszczy pan Sejm.) (Głos z sali: Zejdź z mównicy.) (Głos z sali: Schodź stamtąd!)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Panie pośle, bardzo dziękuję. Proszę zejść z mównicy. Dziękuję bardzo, proszę…",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Chyba mam prawo do sprostowania czy nie?",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Już pan poseł sprostował.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Dziękuję. (Głos z sali: Już pan się dość ośmieszył.) (Poseł Monika Wielichowska: Czas minął.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Przejmuję prowadzenie obrad. Bardzo proszę, panie marszałku. Panie pośle Braun, na podstawie art. 22b regulaminu Sejmu stwierdzam, że na terenie pozostającym w zarządzie Kancelarii Sejmu w rażący sposób naruszył pan spokój lub porządek. W związku z tym zbierze się Prezydium Sejmu, które podejmie stosowne uchwały dotyczące ukarania pana. Chcę pana ostrzec, że jeżeli jeszcze raz stanie się to, co stało się przed chwilą… (Głos z sali: Co to znaczy: jeszcze raz?) (Głos z sali: Wykluczyć.) …a więc z mównicy sejmowej będzie pan obrażał wyznawców innych religii, uznam, że naruszył pan powagę Sejmu (Oklaski) i wykluczę pana z obrad. (Poseł Grzegorz Braun: W trybie sprostowania.) Proszę bardzo, jeżeli pan chce, to proszę, niech pan to zrobi. Niech pan to zrobi.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Panie Marszałku! Wyzywam wszystkich tu zebranych, a także słuchaczy, widzów na dysputę historyczno-teologiczną… (Poruszenie na sali) (Głos z sali: Nie no, dajcie spokój.) (Głos z sali: Wyłączyć mikrofon.)",
                },
                {"speaker": "Marszałek", "content": "Panie pośle, zwracam panu uwagę…"},
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Chętnie wykażę panu, panie marszałku, ignorancję pańską i wszystkich zebranych w dziedzinie, w której tak śmiało pan się wypowiada.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, zwracam panu uwagę, że zakłóca pan obrady Sejmu.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Nie ma pan pojęcia o istotnym przesłaniu tego aktu religijnego. (Głos z sali: Proszę mu wyłączyć mikrofon.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, na podstawie art. 175 ust. 3 regulaminu Sejmu przywołuję pana do porządku.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "To mam prawo do sprostowania czy nie? (Głos z sali: Wyłączyć mikrofon.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, na podstawie art. 175 ust. 4 regulaminu Sejmu przywołuję pana do porządku i stwierdzam, że uniemożliwia pan prowadzenie obrad. (Głos z sali: Wykluczyć.)",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Pan mnie sam tu zawezwał. Pan mnie sam tu zawezwał. (Głos z sali: Wykluczyć.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, pan nadal uniemożliwia prowadzenie obrad, zaczął pan znowu obrażać ludzi. Na podstawie art. 175 ust. 5 podejmuję decyzję o wykluczeniu pana z posiedzenia Sejmu. (Oklaski) (Głos z sali: Brawo!) Zgodnie z regulaminem Sejmu proszę opuścić salę posiedzeń. Informuję też pana, że zostanie przeciwko panu skierowany wniosek do prokuratury za zakłócenie obrzędu religijnego na terenie Kancelarii Sejmu. Ogłaszam 5 minut przerwy. (Poseł Grzegorz Braun: Proszę zaprotokołować: marszałek Sejmu ignorant, a na dodatek prowokator.) (Głos z sali: Nie obrażaj.) (Głos z sali: Straż Marszałkowska pana wyprowadzi.) (Głos z sali: Niech posprząta jeszcze. Niech posprząta.)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Wznawiam obrady Sejmu po przerwie. Zapraszam do zadania pytania pana posła Piotra Glińskiego. (Głos z sali: Ja mam pytanie: Co z pana kolegą?) (Głos z sali: Czy nadal jest tu pana kolega?) Proszę bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Piotr Gliński",
                    "content": "Panie Marszałku! Wysoki Sejmie! Panie Premierze! W związku z zaistniałą sytuacją chciałem w imieniu własnym, ale także mam nadzieję i myślę, że całego naszego środowiska, klubu, powiedzieć wyraźnie, że nie zgadzamy się na wszelkie akty nietolerancji i agresji na tle religijnym i jakimkolwiek innym. (Oklaski) To przeczy podstawowym wartościom humanitarnym, humanistycznym. Nie zgadzamy się na to po prostu i w tej atmosferze także ja rezygnuję z zadawania pytania. (Głos z sali: Wycofaliśmy.) Ja mogę za siebie powiedzieć, że rezygnuję z zadawania pytania. Musimy także jako Sejm, chyba że Prezydium już to zrobiło, podjąć jakąś decyzję. Zwracam się także do środowiska Konfederacji. (Głos z sali: Wstyd!) Proszę państwa, przekraczamy w polityce straszliwe granice, bardzo często to się zdarza (Dzwonek), ale to jest agresja… (Głos z sali: Cofnąć immunitet jeszcze dziś...) …nie tylko na tle religijnym, ale także międzyludzkim. Tam były także małe dzieci. To jest w ogóle nie do obrony i nie do rozmowy na ten temat. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo, panie pośle. W sprawie wspomnianej przez pana Prezydium Sejmu zbierze się za chwilę. My obradowaliśmy tutaj, na sali, nie byliśmy świadkami tego, co się stało, więc zaczekajmy na spotkanie Prezydium Sejmu i ewentualne decyzje. Zapraszam do zabrania głosu w tej chwili pana posła Grzegorza Pudę. Proszę bardzo, panie pośle. (Głos z sali: Wycofajcie.)",
                },
                {
                    "speaker": "Poseł Grzegorz Puda",
                    "content": "Dziękuję bardzo. Szanowny Panie Marszałku! Wysoka Izbo! Panie Premierze! Pani Marszałek! Oczywiście ta sytuacja jest sytuacją, która z pewnością powinna od całej grupy, od całej elity parlamentarnej wymagać jedności. (Oklaski) Myślę, że tak jak tu jesteśmy, nie tylko z prawej strony, ale również z innej strony politycznej, nie zgadzamy się z tym, co się wydarzyło. W związku z tym – miałem długie pytanie – zadam tylko krótkie pytanie. Panie premierze – to będzie pytanie merytoryczne – mówił pan tutaj o środkach, o KPO, o Krajowym Planie Odbudowy… (Głos z sali: Wycofajcie te pytania.) (Głos z sali: Naprawdę.) Przepraszam, to jest zadanie pana marszałka. Jeżeli pan marszałek wycofa… (Gwar na sali) (Głos z sali: My wycofaliśmy.) (Głos z sali: To kwestia kultury.)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Panie pośle, pragnę pana poinformować, że dosłownie przed momentem, zanim wznowiłem prowadzenie obrad, konsultowałem się z marszałkiem Szymonem Hołownią, tak że nie jest moją prywatną inicjatywą zakończenie przerwy i kontynuowanie obrad, tylko decyzją marszałka Sejmu. (Głos z sali: Ale po prostu pytania wycofajcie.) Jeżeli będzie inna decyzja marszałka Sejmu, to oczywiście obrady zostaną przerwane. W tej chwili była decyzja, żeby kontynuować sesję pytań i odpowiedzi. (Głos z sali: Musi być wniosek o przerwę.) Mamy 90 osób zapisanych do pytań, w związku z czym kontynuuję prowadzenie Jeżeli ktoś chce złożyć wniosek o przerwę, ma oczywiście takie prawo. (Gwar na sali: To ja złożę we wniosku formalnym.) (Poseł Donald Tusk: Niech pan złoży wniosek o przerwę i poczekajmy.) Panie pośle, bardzo proszę o zakończenie pańskiej wypowiedzi i ewentualnie sformułowanie pytania.",
                },
                {
                    "speaker": "Poseł Grzegorz Puda",
                    "content": "Jeżeli pan marszałek nie ma nic przeciwko, w tej sytuacji, szanowni państwo, proponuję, aby złożyć wniosek. Składam wniosek o przerwę w imieniu klubu Prawa i Sprawiedliwości. (Oklaski) Myślę, że to pozwoli nam po prostu ochłonąć w tej sytuacji. Dziękuję bardzo. (Głos z sali: Głosujmy.)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Dziękuję bardzo. W związku z tym, że widzę tutaj zdecydowaną większość posłów ze wszystkich stron, jestem za tym, żeby… (Głos z sali: Ale zaraz, zaraz… Czyli terrorysta będzie decydował o tym, czy możemy…) (Głosy z sali: Przerwa!) Panie pośle, jeżeli pan chce zabrać głos, to bardzo proszę wejść na mównicę, a jeżeli pan nie chce zabierać głosu, to pozwolę sobie zakończyć to, co mówię.",
                },
                {
                    "speaker": "Poseł Jacek Ozdoba",
                    "content": "Panie Marszałku! Szanowni Państwo! Jeżeli można by było przynajmniej, żeby to pan nie prowadził jednak obrad jako reprezentant… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) (Głos z sali: Dobra, nie rozpędzaj się…)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Przepraszam bardzo, panie pośle… Panie pośle szanowny…",
                },
                {
                    "speaker": "Poseł Jacek Ozdoba",
                    "content": "…tej Izbie. Jakby pan mógł się zamienić z kimkolwiek innym… Może pani marszałek przejmie prowadzenie, bo co najmniej jest pan stronnikiem w tej sprawie… (Głos z sali: A co to, komunistyczna odpowiedzialność zbiorowa?)",
                },
                {
                    "speaker": "Wicemarszałek Krzysztof Bosak",
                    "content": "Panie pośle, pozwoli pan, że będzie Sejm prowadzony zgodnie z wyznaczonym przez Prezydium Sejmu porządkiem. Każdy ma możliwość zadać pytanie, każdy ma możliwość się wypowiedzieć. Jeżeli będzie decyzja o przerwie, to będziemy robić przerwę. W tej chwili była decyzja o prowadzeniu. (Głos z sali: Wszystkie kluby się zgadzają.) Rozumiem. Bardzo proszę, panie pośle, żeby pan zszedł z mównicy. Dziękuję. Czy wniosek złożony tutaj przez posła był złożony w imieniu klubu PiS? Bo tak pan poseł powiedział. (Głos z sali: Tak jest.) Ale inny poseł się odcinał. (Gwar na sali) (Głos z sali: Ale był w imieniu Prawa i Sprawiedliwości.) Czy jest ktoś z władz klubu PiS na sali? Nie widzę. Czyli rozumiem, że był to wniosek pana posła, tak? (Wypowiedź poza mikrofonem) Dobrze. W związku z tym, że widzę, że większość klubów obecnych na sali oczekuje tej przerwy, ogłoszę przerwę do momentu zebrania się Prezydium i dalszych decyzji ze strony Prezydium Sejmu i marszałka Sejmu. Dziękuję państwu bardzo. (Oklaski) Będą informacje, kiedy wznowimy obrady. Dziękuję.",
                },
                {
                    "speaker": "Wicemarszałek Piotr Zgorzelski",
                    "content": "Szanowni Państwo Posłowie! Wznawiam obrady. Kontynuujemy rozpatrywanie punktu 38. porządku dziennego. Ale zanim do tego dojdzie, chciałem… Jest tu obecny także szef naszego klubu parlamentarnego. Jeśli pan przewodniczący pozwoli, to przytoczę ustalenie, że pytania, do których zadania zapisali się posłowie Klubu Parlamentarnego Polskiego Stronnictwa Ludowego, także wycofujemy. W tej sprawie o głos chciał prosić w imieniu klubu pan przewodniczący poseł Przemysław Czarnek. (Poseł Przemysław Czarnek: Przewodniczącym nie jestem, ale mogę być…) Proszę.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "Bardzo dziękuję za nominację. Panie Marszałku! Wysoka Izbo! Wydarzył się ogromny skandal na terenie Sejmu Rzeczpospolitej Polskiej. Przypomnę, że w ciągu ostatniego miesiąca to nie pierwszy skandal. Zajmujemy się tu show, a nie zajmujemy się porządkiem w Wysokiej Izbie i dlatego dochodzi do tego typu sytuacji… (Głos z sali: Ciekawe, kto się zajmuje show?) Ta sytuacja ma wymiar międzynarodowy. I rzeczywiście uderza w nas niebywale, w nas jako Rzeczpospolitą Polską. Mamy jeszcze 100 pytań do pana premiera Donalda Tuska, i to pytań o znaczeniu fundamentalnym, ale nie chcemy zadawać tych pytań dzisiaj, w atmosferze tego skandalu. Ten skandal trzeba wyciszyć, ten skandal trzeba wyjaśnić, o tym skandalu trzeba mówić, żeby zabezpieczyć się na przyszłość przed tego typu ekscesami, dramatycznymi ekscesami. Tu chodzi rzeczywiście o rzecz niebywałą, o zachowanie pana posła Brauna, który dzisiaj atakował i pana prezesa Jarosława Kaczyńskiego, i Prawo i Sprawiedliwość, a który dzisiaj dopuścił się na koniec tego typu rzeczy, że zaatakował gaśnicą dzieci, i to jeszcze w sytuacji właśnie takiej, a nie innej. (Dzwonek) Dlatego, panie marszałku, w imieniu Klubu Parlamentarnego Prawo i Sprawiedliwość wnoszę o odroczenie obrad do jutra. Chcemy zadawać pytania, ale jutro. Dzisiaj ten skandal musi być wyjaśniony, bo to jest skandal, który obciąża również tych, którzy dzisiaj zawiadują Sejmem. Kiedy rządziła tym z tej strony pani marszałek Witek, nigdy do takich skandali nie dochodziło. (Głos z sali: Sprzeciw!) Dzisiaj mamy bałagan w Sejmie. Trzeba to wszystko uporządkować. Dziękuję bardzo. (Oklaski) (Głos z sali: Kpina, wykorzystujecie to politycznie.)",
                },
                {
                    "speaker": "Wicemarszałek Piotr Zgorzelski",
                    "content": "Dziękuję bardzo. Szanowni Państwo! Został zgłoszony wniosek przeciwny. Wydawać by się mogło, że parlamentarzyści Prawa i Sprawiedliwości dołączą solidarnie do wszystkich posłów, którzy zrezygnowali z zadawania pytań… (Głos z sali: Ale my się dołączyliśmy.) A wniosek dotyczy przerwy i przełożenia obrad. (Głos z sali: My chcemy przerwy do jutra.) To jest wniosek przeciwny. (Głos z sali: Przepraszam, panie marszałku, nie było pana na sali, więc proszę nie mówić takich rzeczy.) Rozumiem.",
                },
                {
                    "speaker": "Poseł Monika Wielichowska",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Zgłaszam wniosek przeciwny. (Oklaski) Klub Parlamentarny Koalicja Obywatelska chce kontynuować obrady pomimo tego, co dzisiaj wydarzyło się w Sejmie, co było hańbiące. Pan premier Donald Tusk jest gotowy odpowiedzieć na wszystkie pytania, które padły do tej pory, i te, które ewentualnie padną ze strony posłów i posłanek Prawa i Sprawiedliwości. Dziękuję. (Oklaski) (Poseł Przemysław Czarnek: Panie marszałku, to jeszcze sprostowanie. Ale to wyjaśnimy, o co chodzi.)",
                },
                {
                    "speaker": "Wicemarszałek Piotr Zgorzelski",
                    "content": "Już teraz rozumiem. Pan poseł Suchoń.",
                },
                {
                    "speaker": "Poseł Mirosław Suchoń",
                    "content": "Bardzo dziękuję. Szanowny Panie Marszałku! Wysoka Izbo! To rzeczywiście wstrząsająca sytuacja i również Klub Parlamentarny Polska 2050 – Trzecia Droga niezwłocznie podjął decyzję o wycofaniu wszystkich pytań z kolejki, która została. Tego typu incydenty nigdy nie powinny mieć miejsca. (Głos z sali: A głosowania?) Chcę wyraźnie powiedzieć, że nie ma zgody na nienawiść, nie ma zgody na takie zachowania, które w jakikolwiek sposób podważają prawa innych ludzi, a ta sytuacja, z którą mieliśmy do czynienia w parlamencie, jest przejawem absolutnego niezrozumienia tego, czym jest parlament, komu ma służyć i jakie są idee i wartości przyświecające parlamentaryzmowi. Jest symboliczne, że właśnie niektóre środowiska postępują w sposób, który zaprzecza wszystkim ideom, które powinny nas łączyć. Panie Marszałku! Dziękuję za tę decyzję, dziękuję za przerwę, dziękuję za to, że Sejm w osobie pana marszałka i wicemarszałków zabrał ważny (Dzwonek) głos w tej ważnej sytuacji, w jasny sposób wskazując, że nie ma zgody na tego typu zachowania. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Piotr Zgorzelski",
                    "content": "Bardzo dziękuję. I pan poseł.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "Jeszcze jedno – bardzo dziękuję, panie marszałku – wyjaśnienie, bo doszło tu do jakiegoś nieporozumienia. To w końcu jesteście za kontynuowaniem pytań czy nie? Bo my jesteśmy przeciwko. (Głos z sali: Dzisiaj.) Nie będziemy zadawać pytań w atmosferze skandalu dzisiaj, ale chcemy zadać pytania nowemu premierowi jutro, kiedy ten skandal wyjaśnimy. (Oklaski) A wy z kolei dzisiaj powiedzieliście, że chcecie kontynuować pytania, więc zastanówcie się…",
                },
                {
                    "speaker": "Wicemarszałek Piotr Zgorzelski",
                    "content": "Dziękuję bardzo.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "…co chcecie zrobić z tym skandalem: kontynuować pytania czy nie? My jesteśmy przeciwko pytaniom dzisiaj, chcemy je zadać jutro. Takie jest nasze stanowisko. (Oklaski) (Głos z sali: My nie zadajemy.) (Głos z sali: Kontynuować pytania.)",
                },
                {
                    "speaker": "Wicemarszałek Piotr Zgorzelski",
                    "content": "Dziękuję bardzo. Pan przewodniczący Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga Krzysztof Paszyk.",
                },
                {
                    "speaker": "Poseł Krzysztof Paszyk",
                    "content": "Panie Marszałku! Bardzo dziękuję. Chcę w imieniu Klubu Parlamentarnego Polskiego Stronnictwa Ludowego – Trzeciej Drogi potępić to, co przed kilkudziesięcioma minutami (Oklaski) odbyło się w polskim parlamencie. To zachowanie jednego z posłów, pana posła Brauna, jest skandalem, wymaga potępienia, wyciągnięcia wniosków jak najdalej idących wobec tego człowieka, który naraził na szwank reputację polskiego narodu, reputację naszego państwa. Ale też odpowiadam, nawiązując do słów pana posła Czarnka. Panie Pośle! Nie idźmy scenariuszem, który dzisiaj tu został napisany przez Brauna, i nie destabilizujmy porządku dzisiejszego posiedzenia, które jest bardzo precyzyjnie rozpisane. (Oklaski) (Poseł Przemysław Czarnek: Chcecie pytań, tak?) Odczytuję, że ten wniosek, który pan złożył, jest niestety graniem w scenariuszu, który on tu dzisiaj napisał. Zadaliście jako klub dzisiaj kilkadziesiąt pytań obejmujących całokształt tego, co w exposé powiedział dzisiaj pan premier Tusk. (Poseł Przemysław Czarnek: Panie pośle, jesteście za pytaniami czy przeciwko? My jesteśmy przeciwko.) Naprawdę wystarczy wysłuchać tej odpowiedzi, która na pewno zostanie udzielona. Ale jeszcze raz, panie pośle, pana i pana koleżanki i kolegów z klubu proszę, żeby bardzo poważnie się zastanowić… (Poseł Przemysław Czarnek: Ale my to zrobiliśmy, to myśmy… o przerwę.) …i rozważyć udział w scenariuszu Brauna, który został dzisiaj zapisany. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Piotr Zgorzelski",
                    "content": "Bardzo dziękuję. Pan przewodniczący Krzysztof Gawkowski. (Głos z sali: Wy gracie w scenariuszu Brauna.)",
                },
                {
                    "speaker": "Poseł Krzysztof Gawkowski",
                    "content": "Panie Marszałku! Wysoka Izbo! To ważny dzień dla Polski i dla polskiego parlamentaryzmu. To ważny dzień dla milionów Polek i Polaków, którzy 15 października powiedzieli: tak dla zmiany, ale też poszli do wyborów, bo frekwencja była wielka i duma z tego wydarzenia jest olbrzymia. To święto dzisiaj postanowił wszystkim nam zepsuć jeden poseł, Grzegorz Braun, którego imię powinno być wykasowane ze wszystkich parlamentarnych protokołów nie tylko na tym, ale na każdym posiedzeniu. (Oklaski) Karą za to, co dzisiaj się wydarzyło, powinno być wyeliminowanie z pracy parlamentarnej posła Brauna na całą kadencję. (Oklaski) Nie ma zgody, aby w tej Izbie takie sytuacje miały miejsce. Ale nie ma też zgody, żeby w imię tego, że jeden poseł chce nam zepsuć święto demokracji, prawa część strony politycznej, Prawo i Sprawiedliwość, chciała zdestabilizować państwo. (Dzwonek) Nie ma na to zgody Lewicy. (Poruszenie na sali) (Głos z sali: Nie kłam.) Trzeba to dzisiaj tutaj powiedzieć. (Głos z sali: Hańba!) Chcecie zepsuć nam święto demokracji. Nie będzie na to zgody. (Głos z sali: To nie wycofujcie się z pytań, Krzysztof.)",
                },
                {
                    "speaker": "Wicemarszałek Piotr Zgorzelski",
                    "content": "Dziękuję bardzo. Szanowni państwo, proszę o zajęcie miejsc. Proszę o zajęcie miejsc. Szanowni państwo posłowie, czy mało jest już atmosfery skandalu w tej Izbie dzisiaj? (Głos z sali: No to niech pan zwróci uwagę.) Zatem proszę wysłuchać, co mam do powiedzenia. (Głos z sali: To zrobić przerwę.) A do powiedzenia mam następujący komunikat. W związku z tym, że został zgłoszony wniosek o odroczenie naszych obrad, musimy go przegłosować. Zatem ogłaszam przerwę do godz. 18.40, po zakończeniu której przystąpimy do głosowania.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Wznawiam obrady. Szanowni państwo, wznosicie okrzyki, piszecie różne rzeczy, wypowiadacie się tutaj, na mównicy sejmowej, wiecie, co się stało. Stał się akt absolutnie hańbiący parlament Rzeczypospolitej Polskiej. Stał się akt, który… (Gwar na sali) Pozwólcie państwo, że w obliczu tak poważnej sytuacji skończę zdanie, które chciałem zacząć, dobrze? Wypowiedzi pana posła Czarnka, wypowiedzi pana posła Moskala, wypowiedzi innych posłów robiących z tej strasznej sprawy wydarzenie… (Poseł Przemysław Czarnek: Panie marszałku, ja sobie nie życzę. Ja sobie nie życzę obrażania.) A może pan sobie nie życzyć, panie pośle Czarnek. Panie pośle Czarnek, teraz ja mówię i proszę zająć miejsce. (Poseł Przemysław Czarnek: Ja zgłaszałem wniosek.) Za chwilę ten wniosek będzie głosowany. Proszę zająć miejsce i nie zakłócać powagi Sejmu. Chcę państwa poinformować, że rzucanie teraz oskarżeń politycznych, że to, co się stało, jest współwiną obecnego kierownictwa Sejmu, państwa komentarze… (Gwar na sali) (Poseł Przemysław Czarnek: A nie jest? Jest.) … o tym, że za marszałek Witek tego nie było, są skandaliczne i są próbą uczynienia polityki z czegoś, co do czego powinniśmy być jednomyślni. (Oklaski) Jednomyślni. I bardzo dziękuję tym państwu posłom Prawa i Sprawiedliwości, wszystkich sił politycznych, które na tej sali zasiadają, którzy dali wyraz swojemu oburzeniu, a dało naprawdę wielu z państwa w sposób absolutnie jednoznaczny. (Poseł Przemysław Czarnek: Wszyscy daliśmy wyraz oburzeniu.) Ale nie mogliście się powstrzymać od robienia na tym polityki, niektórzy z was, i to skandal. (Głos z sali: Nie, nie, panie marszałku.) Panie pośle, proszę zająć miejsce. (Głos z sali: Skandalem jest to, co pan mówi.) (Poseł Przemysław Czarnek: Bardzo proszę o głos, panie marszałku.) Poproszę o narzędzia dyscyplinujące posła. (Głos z sali: Skandal.) Wznawiam obrady. Chcę państwa poinformować, że w związku… (Poseł Przemysław Czarnek: Bardzo proszę o pozwolenie.) …z zaistniałym incydentem – pan poseł Braun, jak dobrze wiecie, zakłócił przebieg uroczystości zapalenia świecy chanukowej w holu głównym Sejmu, również z tej mównicy wygłaszał rzeczy, które nie mieszczą się w kanonie rzeczy, które powinny padać gdziekolwiek, a tym bardziej z mównicy Sejmu – podjęliśmy jako Prezydium Sejmu natychmiastowe kroki. Pan poseł Braun został wykluczony z obrad. Zebrało się Prezydium Sejmu, które podjęło decyzję o ukaraniu pana posła Brauna z art. 22b regulaminu Sejmu i art. 175 regulaminu Sejmu maksymalnym wymiarem kary, który jest dostępny Prezydium Sejmu, a więc jest to półroczne pozbawienie diety poselskiej i połowy uposażenia przez 3 miesiące. Kancelaria Sejmu została też zobowiązana i upoważniona do złożenia wniosku do prokuratury. Tu są trzy paragrafy, co do których mamy podejrzenie, że pan Braun mógł je naruszyć, to jest zakłócenie uroczystości religijnej, to jest naruszenie nietykalności cielesnej i to jest sprowadzenie zagrożenia dla życia i zdrowia. (Poseł Piotr Kaleta: Czyli tak jak Wielgus.) Taki wniosek zostanie sporządzony i mam nadzieję, że będziemy mogli szybko rozstrzygnąć o statusie immunitetu pana Brauna na sali sejmowej. Coś takiego nigdy nie powinno mieć miejsca. (Oklaski) To hańbiące wydarzenie musi się spotkać z jednoznaczną i zdecydowaną reakcją nas wszystkich. Zero tolerancji dla dewiacji, ksenofobii i antysemityzmu gdziekolwiek w tym budynku: czy na sali plenarnej, czy gdziekolwiek indziej będą występować. (Głos z sali: A antykatolicyzm?) (Poseł Przemysław Czarnek: Panie marszałku, proszę o wniosek formalny.) Zgłosił pan wniosek formalny o odroczenie posiedzenia i ten wniosek zostanie teraz rozpatrzony. (Głos z sali: Uzasadnienie.) Najpierw przegłosujemy, jeśli pan pozwoli, ten wniosek formalny, który pan złożył. Pan poseł Czarnek przed wznowieniem obrad zgłosił wniosek formalny, żeby przerwać rozpatrywanie tego punktu porządku dziennego do jutra. Sytuacja jest następująca: posłowie Koalicji Obywatelskiej, Trzeciej Drogi i Lewicy wycofali się z dalszego zadawania pytań panu premierowi Tuskowi. Jest 90 pytań, które pozostały ze strony państwa posłów Prawa i Sprawiedliwości. (Poseł Barbara Bartuś: Pan premier wycofał się z exposé?) Pan poseł Czarnek wnosi, aby przerwać posiedzenie tak, iżby zadawanie tych pytań kontynuowane było w dniu jutrzejszym, a więc wniosek o odroczenie posiedzenia. Poddam teraz ten wniosek pod głosowanie. Przystępujemy do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku przedstawionego przez pana posła Czarnka o odroczenie posiedzenia, zechce podnieść teraz rękę i nacisnąć przycisk. Kto z państwa jest przeciw wnioskowi? Kto się wstrzymał? Głosowało 451 posłów. 186 – za, 250 – przeciw, 15 się wstrzymało. Stwierdzam, że Sejm wniosek odrzucił. W związku z powyższym … (Poseł Przemysław Czarnek: Panie marszałku, bardzo proszę o sprostowanie.) Mam tu informację, że pani poseł Żukowska była z wnioskiem formalnym, zanim jeszcze pan poseł zgłosił swój drugi wniosek formalny. (Poseł Barbara Bartuś: Ale było użyte nazwisko pana posła…) Bardzo proszę. Ale proszę, pani poseł Bartuś, spokojnie poczekać na to, aż pan poseł uzyska głos. Kolejność obowiązuje. (Poseł Barbara Bartuś: Sprostowanie.) Dziękuję, pani poseł. Proszę bardzo, pani poseł.",
                },
                {
                    "speaker": "Poseł Anna Maria Żukowska",
                    "content": "Panie Marszałku! Wysoka Izbo! Zgłaszam wniosek o zmianę porządku obrad i dodanie do porządku obrad projektu uchwały Sejmu dotyczącej potępienia zachowania posła Grzegorza Brauna jako motywowanego nienawiścią i antysemityzmem. W Polsce nie ma miejsca na zachowania antysemickie, rasistowskie i ksenofobiczne. (Oklaski) Polska jest państwem otwartym, domem dla wszystkich obywatelek i obywateli niezależnie od różnic w pochodzeniu, tożsamości religijnej i narodowej. Przedkładam ten projekt uchwały panu marszałkowi, ale powiem jeszcze jedno zdanie. Będziemy także wnioskować o wykluczenie z Prezydium Sejmu pana wicemarszałka Bosaka. (Oklaski) Głosowaliśmy przeciwko tej kandydaturze i jesteśmy przeciwko tej kandydaturze, bo pan sobie, panie marszałku, nie poradził z prowadzeniem obrad. Musiał je przejąć pan marszałek Hołownia. (Dzwonek) Będziemy składać ten wniosek. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Pani poseł, pani wniosek… (Gwar na sali) (Głos z sali: Mogę z wnioskiem przeciwnym?) Już, moment, panie pośle, chwila. Chwileczkę, bardzo proszę o spokój. Myślę, że to państwa zainteresuje, bo to jest kwestia, nad którą być może będziemy głosować w przerwie, którą jeszcze dzisiaj planujemy. Przed ostatnim blokiem głosowań zwołam Prezydium Sejmu i Konwent Seniorów. Zaopiniujemy ten wniosek. Jeżeli taka będzie państwa wola, to chcemy też trochę skrócić dzisiejsze posiedzenie w związku z tym, co dzisiaj zaszło. Jeżeli taka będzie wola państwa, Prezydium Sejmu i Konwentu Seniorów, to dodamy głosowanie nad tym punktem do bloku głosowań. W tym bloku głosowań będziemy m.in. wyłaniali skład komisji śledczej. Zostanie rozpatrzony także ten wniosek. Złoży pani, jak rozumiem, wniosek formalny w sprawie zmiany składu Prezydium Sejmu i będziemy się tym dalej zajmować. Pan poseł Czarnek… Tylko upewnię się, w jakim trybie, panie pośle. W trybie sprostowania? (Poseł Przemysław Czarnek: Sprostowania.) (Głos z sali: Ale do czego?) Bardzo proszę, panie pośle. 1 minuta.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "Panie Marszałku! Wysoka Izbo! Mamy do czynienia z kontynuacją skandalu tego wieczora. Zamiast zwracać się do tych, którzy wywołali skandal, i to międzynarodowy skandal, pan marszałek patrzył na nas i ma pretensje, że to my, bo to my, panie marszałku, jako pierwsi zgłosiliśmy wniosek o przerwę, nie chcieliśmy kontynuować punktu dotyczącego zadawania pytań podczas skandalu, który wydarzył się w Sejmie. Ma pan do nas pretensje? Panie marszałku, pan jest od prowadzenia obrad, a nie od recenzowania wniosków formalnych posłów. Jesteśmy pełnoprawnymi uczestnikami tej debaty i nie będzie nas pan recenzował. (Oklaski) Zwracam uwagę, że pan marszałek nie miał nic przeciwko panu Braunowi rano, kiedy miał antysemickie wyjazdy np. pod adresem nazwiska pana premiera Mateusza Morawieckiego. Jakoś to panu nie przeszkadzało. (Oklaski) (Głos z sali: Tak jest.) (Głos z sali: Brawo!) (Głos z sali: Hańba!)",
                },
                {"speaker": "Marszałek", "content": "Panie pośle…"},
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "Teraz ja mówię, panie marszałku. (Gwar na sali) Nie przeszkadzało panu marszałkowi, jak pan prezes Kaczyński był w brutalny sposób atakowany przez pana Brauna.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, proszę na mnie nie pokrzykiwać.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "Nie przeszkadzało panu, jak pani marszałek Witek (Dzwonek) była atakowana w brutalny sposób. Ma pan do nas pretensje, że chcemy zapanować nad sytuacją na sali?",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, proszę opuścić mównicę",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "To jest skandal. To jest pański skandal, panie marszałku. (Oklaski) (Głos z sali: Skandal!) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, proszę opuścić mównicę. Drodzy państwo, wniosek o przerwanie i odroczenie obrad został odrzucony. W związku z powyższym będziemy kontynuowali rozpatrywanie punktu porządku dziennego: Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów. Ilu posłów mamy jeszcze zgłoszonych do pytań? 86. Czy mogę prosić o informację, kto z posłów zada teraz pytanie? (Głos z sali: Po kolei jedziemy.) Tak, po kolei, ale pozwólcie państwo pracownikom Kancelarii Sejmu uruchomić odpowiednią aplikację. Pytanie zada teraz pan poseł Radosław Fogiel z Prawa i Sprawiedliwości. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Radosław Fogiel",
                    "content": "Panie Marszałku! Wysoka Izbo! Mamy bardzo wiele pytań do premiera Tuska, ale trudno zadawać je w atmosferze skandalu, dlatego haniebne dla tej Izby jest to, że nie poparliście państwo wniosku o odroczenie obrad do jutra. O tym, jak pan marszałek tolerował wyskoki posła Brauna, mówił przed chwilą pan minister Czarnek. (Głos z sali: Kłamał.) Szanowni Państwo! W momencie, kiedy wykorzystujecie skandaliczne zachowanie posła Brauna jako pretekst do tego, żeby większość parlamentarna wycofała swoje pytania, należy się zastanowić, komu to służy. Chcecie skrócić debatę? Chcecie ograniczyć pytania do premiera Tuska? Szanowny Panie Marszałku! Proszę się nie oburzać. (Głos z sali: Podlega pan krytyce.) Odpowiedzialność wiąże się z pańską rolą. Wiem, że to nie jest łatwe. To nie jest tylko (Dzwonek) poklask i cieszenie się z popularności. Widzi pan, panie marszałku, do czego może doprowadzić pogoń za lajkami i oglądalnością? Należy wziąć odpowiedzialność. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, za obarczanie mnie odpowiedzialnością czy współodpowiedzialnością za ten antysemicki wybryk spotka pana z mojej strony wniosek do Komisji Etyki Poselskiej. (Oklaski) (Poseł Elżbieta Witek: Co to w ogóle jest?) (Głos z sali: Ooo…) Nie, drodzy państwo, są pewne granice, są pewne granice. Zobaczcie, co się dzisiaj stało. (Poseł Przemysław Czarnek: Do czego pan dopuścił, panie marszałku?) (Głos z sali: Regulamin.) Stała się rzecz, która powinna nas dzisiaj zjednoczyć, powinna nas dzisiaj zjednoczyć w sprzeciwie wobec tego, co się stało. To powinna być treść tego, co dzisiaj czujemy i myślimy. Jestem o tym głęboko przekonany, chyba nie tylko ja. Mam nadzieję, że wyciągniemy też z tej sytuacji stosowne wnioski. (Poseł Barbara Bartuś: W tym jesteśmy zjednoczeni.) (Głos z sali: Panuj nad sobą.) Rozumiem, że pan poseł zadał pytanie. Nie rozumiem tego, że twierdzi pan, że debata jest ograniczana, podczas gdy jest wręcz przeciwnie. To państwo będziecie zadawać premierowi pytania. (Głos z sali: Proszę nie komentować każdego wystąpienia.) Bardzo proszę, żebyście zachowali państwo spokój. Pytanie zada teraz pan Andrzej Gawron z Prawa i Sprawiedliwości. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Andrzej Gawron",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Pan marszałek tak często przytacza przepisy, do których powinni się stosować posłowie. Regulamin Sejmu mówi, że marszałek Sejmu stoi na straży praw, godności i powagi Sejmu. Dziękuję za to, że przybyło panu tej powagi. Nie uciekniecie od odpowiedzialności. (Oklaski) Przed chwilą była przerwa, zebrało się Prezydium Sejmu, w którym nie ma przedstawiciela największego klubu – Prawa i Sprawiedliwości. (Oklaski) Jest za to przedstawiciel Konfederacji. To jest wasza odpowiedzialność. To jest wasza odpowiedzialność, nie uciekniecie od tej odpowiedzialności. (Poseł Przemysław Czarnek: To wyście się dogadali, panie marszałku.) (Głos z sali: To wy głosowaliście za.) Panie Premierze! Chcę się zwrócić w sprawie mikroprzedsiębiorców. W kampanii wyborczej mówił pan o tym, że zostaną przedstawione programy dla mikroprzedsiębiorców, które pomogą im w tej trudnej sytuacji. (Głos z sali: Jeszcze nie dokończyliście.) Szanowni państwo (Dzwonek), pytam o ZUS… (Głos z sali: Czas!) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                },
                {"speaker": "Marszałek", "content": "Dziękuję bardzo, panie pośle."},
                {
                    "speaker": "Poseł Andrzej Gawron",
                    "content": "…czy będzie ten ZUS, który ma być, odwrócony PiT. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Zacytuję panu art. 7: Do podstawowych obowiązków posła należy w szczególności stosowanie się do wynikających z regulaminu Sejmu poleceń marszałka Sejmu. Bardzo proszę, pan poseł… (Gwar na sali) Możecie krzyczeć, ile chcecie. To nie zmieni regulaminu Sejmu. (Oklaski) (Poseł Przemysław Czarnek: Zarządca, zarządca.) Bardzo proszę, pan poseł Czesław Hoc z Prawa i Sprawiedliwości. Jest pan poseł? Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Czesław Hoc",
                    "content": "Panie Marszałku! Wysoki Sejmie! Miała być powaga, a jest rzeczywiście show. (Głos z sali: Z waszej strony.) Jest olbrzymi skandal, olbrzymie wydarzenie, a przechodzimy jednak do porządku dziennego, jakby się nic nie stało. Wobec powyższego, panie premierze, powszechnie znane jest powiedzenie: Pnąc się w górę, bądź miły dla ludzi, albowiem spotkasz ich w drodze powrotnej. I warto o tym stale pamiętać. Tyle pan premier mówił o miłości, o współpracy, wspólnotach, a jednocześnie do poprzedników, poprzedniej władzy mówił: Rozpyliła się złość, zło, stajnia Augiasza, koszmar. To nie było ani spójne, ani przyzwoite. Przychodzi mi na myśl morał ze „Świtezianki” Mickiewicza: Słowicze trel na ustach, lisie zamiary w sercu. (Oklaski) I konkretne pytanie, bo musimy teraz mówić o poważnych kwestiach, o służbie zdrowia. Dlaczego blokujecie w komisjach dalsze procedowanie obywatelskiego projektu ustawy o podwyżkach dla pielęgniarek, który jest już po pierwszym czytaniu? Czy upomnieliście się w tym projekcie ustawy o podwyżki dla innych grup zawodowych medycznych, a więc sekretarek medycznych, opiekunów medycznych, informatorów medycznych, rejestratorek, dietetyków, pracowników administracji służby zdrowia, personelu pomocniczego czy też pielęgniarek z domu pomocy społecznej? To są poważne kwestie. Blokujecie to. To jest teraz dokładnie zamrażarka w komisjach. (Oklaski) (Poseł Tomasz Zimoch: …dlaczego tego nie zrobiliście?) Niby nie ma zamrażarki, a boicie się (Dzwonek) procedować w komisjach nad bardzo ważnymi kwestiami. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Jako następna zabierze głos pani poseł Agnieszka Wojciechowska van Heukelom z Prawa i Sprawiedliwości. Bardzo proszę, pani poseł. Nieobecna? (Głos z sali: Nieobecna.) W takim razie bardzo proszę pana posła Adama Andruszkiewicza też z Prawa i Sprawiedliwości. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Adam Andruszkiewicz",
                    "content": "Panie Marszałku! Wysoka Izbo! Z tego haniebnego zachowania pana posła Brauna mogą się cieszyć tylko wrogowie Polski, dzisiaj na czele z Moskwą, rosyjską oczywiście. (Oklaski) To jest haniebne zachowanie, które tutaj wszyscy potępiamy. Natomiast, panie marszałku, niestety, kto zaczął robić z Sejmu Rzeczypospolitej Polskiej cyrk? Właśnie takie są konsekwencje tego, że tacy ludzie jak Braun czuli się bezkarnie dzisiaj. (Oklaski) Należy z tym jak najszybciej skończyć i dać największemu klubowi w Sejmie, Prawu i Sprawiedliwości, wicemarszałka, który ma reprezentować niemal 8 mln Polaków, którzy na Prawo i Sprawiedliwość, panie marszałku, głosowali. Natomiast dzisiaj, szanowni państwo, pytanie jest fundamentalne dla mieszkańców województwa podlaskiego, dlatego że rząd Prawa i Sprawiedliwości zaczął odbudowywać obecność wojska polskiego w naszym regionie, m.in. nowe jednostki wojskowe w Grajewie, w Augustowie, w Kolnie, wzmacniamy obecność w Białymstoku, w Łomży czy w Suwałkach. (Poseł Jakub Rutnicki: Jeszcze nie ma.) Proste pytanie, szanowni państwo: Czy państwo nie zlikwidujecie tych jednostek wojskowych, bo kiedyś to robiliście? Przypominam, że chociażby na przesmyku suwalskim taka jednostka przez was została zlikwidowana. Po tym, co się wydarzyło w Smoleńsku, już w grudniu 2010 r. zlikwidowaliście jednostkę wojskową w Suwałkach. Czy tych jednostek nie zlikwidujecie po raz (Dzwonek) kolejny? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Pani poseł Anita Czerwińska. Bardzo proszę Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                },
                {
                    "speaker": "Poseł Anita Czerwińska",
                    "content": "Panie Marszałku! Wysoka Izbo! Niestety tak się kończy obniżanie powagi Sejmu, instytucji publicznych, a wy to zaczęliście. (Oklaski) Przypominam wam ciamajdan, przypominam wam to, jak zakłócaliście, także tu obecni posłowie, msze święte, jak zakłócaliście uroczystości państwowe. To z waszej inspiracji i bardzo często z waszym udziałem tak było. I to, co się dzisiaj stało, to jest właśnie konsekwencja tej waszej zachęty do obniżania autorytetu państwa. Natomiast jeśli chodzi o pytanie, to chciałam się odnieść do tego, że jeden z posłów Platformy dzisiaj zadał panu pytanie o politykę historyczną. I podczas tego pytania kontestował żołnierzy wyklętych. Czy to ma znaczyć, że wasza polityka historyczna to będzie powielanie komunistycznej propagandy, która atakowała (Dzwonek) żołnierzy powstania antykomunistycznego? Proszę o odpowiedź na to pytanie. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję. Pan poseł Paweł Sałek. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Paweł Sałek",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Zadam tylko kilka pytań. Nie będę się odnosił do tej skandalicznej sytuacji, która miała miejsce, bo ocena jest jednoznaczna. Przejdę do pytań związanych z exposé pana premiera Tuska, bo chciałem poruszyć takie kwestie. Mianowicie państwo w swoim programie wpisują to, że plany urządzania lasów powinny służyć Polakom i że pozwolicie na to, żeby plany urządzania lasów mogły być konsultowane. Chcę zauważyć, że te plany urządzania lasów, jeśli chodzi o całą substancję przyrodniczą w Polsce, są konsultowane i do tego można się odnieść w przepisach prawa. Państwo to wpisali w swój program. Kolejna rzecz związana jest z tym, że państwo powiedzieli o tym, że będą odtwarzać torfowiska. Odtwarzanie torfowisk jest w rozporządzeniu unijnym, które aktualnie jest dyskutowane, w tzw. respiration low. I jeszcze jedno pytanie bardzo ważne. Mianowicie, czy pan premier Tusk zamierza zmieniać ustawę o działach, gdzie dzisiaj w dziale: Środowisko jest wpisany zakres: leśnictwo i łowiectwo? (Dzwonek) Skoncentruję się tylko na leśnictwie. Sekundę, panie marszałku, jeśli można. Dlatego że jeżeliby doszło do próby przesuwania działu: Leśnictwo do innego podmiotu z ministerstwa środowiska, będzie to naruszanie ustawy o działach. Tylko i wyłącznie zmiana ustawy o działach daje prawo przesunięcia działu: Leśnictwo do innego podmiotu, być może także do kancelarii premiera, jeśli są takie pomysły. Zwracam na to uwagę. Dziękuję uprzejmie. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Teraz pan poseł Mariusz Krystian. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Mariusz Krystian",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Jako samorządowiec pamiętam czasy pana poprzednich rządów. Pamiętam, ile pracy miały ośrodki pomocy społecznej, żeby zapewnić wielu polskim rodzinom, zwłaszcza rodzinom wielodzietnym… bo wiele z tych rodzin pana rząd doprowadził do biedy. Pamiętam, jak Platforma Obywatelska zdecydowała zamknąć w moim okręgu wyborczym kopalnię Brzeszcze. I dopiero rząd pani premier Beaty Szydło tę decyzję zmienił i uratował kopalnię i tysiące miejsc pracy. Dziś urządził pan w Sejmie danse macabre. Wykorzystał pan śmierć do celów politycznych. (Poseł Izabela Leszczyna: Ty nie wiesz, co to jest danse macabre.) Wiem po co. Bo emocje panu służą i pan te emocje wzbudził. Dlatego ja nie mam do pana żadnych pytań, ponieważ nie mam co do pana żadnych złudzeń. Dziś Prawo i Sprawiedliwość przechodzi do opozycji. Będziemy opozycją patriotyczną. Zaczęliście tę kadencję Sejmu od afery wiatrakowej. (Dzwonek) To pierwsza wasza afera i zapewne nie ostatnia, dlatego głównym zadaniem opozycji patriotycznej jest pilnowanie Polski, pilnowanie polskich spraw i patrzenie panu na ręce. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję. Pani poseł Anna Ewa Cicholska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Anna Ewa Cicholska",
                    "content": "Dziękuję. Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! Panie premierze, antysemityzm jest czymś bardzo złym. Zarówno ja, moja rodzina, jak również wielu moich przyjaciół potępia to. Ale czy napadanie na kościoły, zaburzanie porządku religijnego, mszy świętych jest czymś dobrym? A wielu polityków z tej strony brało w tym udział. Powinniśmy też to potępić. Zarówno jedno, jak i drugie jest czymś złym. Zło jest złem. (Oklaski) Panie Premierze! Przed 7 laty do Ciechanowa wróciło wojsko. Koszary kiedyś świecące pustkami (Dzwonek) mają swoją świetność. To jest 5. Mazowiecka Brygada Obrony Terytorialnej. Czy mogę powiedzieć mieszkańcom Ciechanowa, że mogą czuć się bezpiecznie? To są tysiące miejsc pracy. Dziękuję. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, pani poseł. Pani poseł Joanna Borowiak. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Joanna Borowiak",
                    "content": "Panie Marszałku! Wysoki Sejmie! Panie marszałku, rozzuchwalanie brakiem reakcji nie popłaca. Gdyby reagował pan na wystąpienia posła Brauna, nie poczułby się on bezkarny, nie doszłoby do skandalu, którego dzisiaj byliśmy wszyscy świadkami. Pani marszałek Witek reagowała, ale przez waszą decyzję i brak poszanowania dla 8 mln Polaków pani marszałek Elżbiety Witek nie ma dzisiaj w Prezydium Sejmu. To jest skandal i kpina z demokracji. Panie Premierze! A może bardziej: desygnowany na premiera. Dzisiaj powiedział pan, że nic, co dane, nie zostanie zabrane. Czy jednak nie okaże się, że będzie pan zwijał czerwony dywan przed seniorami, zgodnie z wytycznymi waszego guru pana Marka Belki? Czy nie okaże się, że trzynasta emerytura i czternasta emerytura pójdą w zapomnienie? Skądinąd muszę zauważyć jako osoba, która zajmuje się od lat sprawami seniorów, że nie spodziewałam się takiej laurki (Dzwonek) ze strony pana Marka Belki. Skoro praca rządu i posłów Prawa i Sprawiedliwości była rozkładaniem czerwonego dywanu przed seniorami, to znaczy, że zrobiliśmy naprawdę dużo dla seniorów. Ja jestem z tego dumna, ponieważ seniorzy zasługują na szacunek i wsparcie. Proszę zatem, aby zadeklarował pan, kiedy już zwiniecie ten dywan przed seniorami, co odbierzecie seniorom w zamian. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Jako następny głos zabierze pan poseł Przemysław Drabek.",
                },
                {
                    "speaker": "Poseł Przemysław Drabek",
                    "content": "Panie Marszałku! Pani Marszałek! Wysoki Sejmie! Panie Premierze! To, co się wydarzyło dzisiaj w polskim parlamencie, nie wydarzyłoby się, gdyby nad tym Sejmem po prostu ktoś panował. Pan marszałek teraz opuścił niestety salę, ale te skandaliczne zachowania są tylko i wyłącznie dlatego, że dopuszcza się do tego, że robi się show w polskim parlamencie. (Oklaski) Rozmawiamy o bardzo poważnych sprawach. Mówimy o Polsce, o przyszłości Polski, a nie robimy tutaj show ani zabawy. Mam jedno ważne pytanie. W exposé, panie premierze, temat kultury został przemilczany, a zadanie, jakie zostało zadane ministrowi, który ma się zajmować tematem kultury, to jest tylko i wyłącznie niszczenie polskich mediów, przejmowanie polskich mediów. A ja mam pytanie: Jak będzie wyglądała nowa jakość, którą prezentuje Platforma Obywatelska, w kulturze polskiej? Czy będzie wyglądała tak jak rządzenie pani Moniki Strzępki, dyrektor Teatru Dramatycznego w Warszawie, pani, która rozpoczynając swoją działalność, mówiła, że jej kadencja będzie (Dzwonek) pod hasłem terapii dla wszystkich? Deklarowała, że stworzy bezpieczne miejsce pracy. A co się teraz w tej chwili tam dzieje? Pani dyrektor Strzępka nazwała swój gabinet waginetem, Teatrem Dramatycznym zarządza razem ze złożonym z kobiet kolektywem, a pracownicy, cenieni aktorzy, opowiadają, że atmosfera panuje tam bardzo niedobra, ludzie są przerażeni, chorują, mają depresję i stany lękowe. Z 44 osób z zespołu ma być duża część zwolniona. Czy taka jest przyszłość polskiej kultury pod rządami koalicji chaosu? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy panu posłowi. Do głosu zapraszam panią poseł Marlenę Magdalenę Maląg, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marlena Magdalena Maląg",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Przyszło nam obradować w atmosferze skandalu. Ale czegóż można się spodziewać, kiedy z Sejmu, z Wysokiej Izby robi się przedstawienie, robi się show? To jest skandal. Kiedy pani marszałek Elżbieta Witek zarządzała Sejmem, obrady były prowadzone sprawnie i z godnością. Pan marszałek doprowadza do tej sytuacji. Ale wracając do exposé, które dzisiaj wygłosił pan premier, i do exposé, które wczoraj wygłosił pan premier Morawiecki – zderzenie dwóch rzeczywistości. Rzeczywistość planu budowania, wizji Polski nowoczesnej, rozwijającej się, bezpiecznej, suwerennej, wizji z planem działania. Natomiast cóż dzisiaj usłyszeliśmy? Niby polityka miłości. W tym exposé słyszeliśmy, że będzie fajnie, z zaciśniętymi zębami i przede wszystkim: za chwilę (Dzwonek) was rozliczymy. Ale ja bym chciała się dowiedzieć, czy te programy społeczno-gospodarcze, które doprowadziły do tego, że dzisiaj Polska jest w tak komfortowej sytuacji, będą realizowane, czy wrócimy do tych czasów, kiedy było gigantyczne bezrobocie, kiedy Polakom kazano pracować za 3–5 zł, a emeryci mieli waloryzację dwuczy trzyzłotową. (Poseł Monika Wielichowska: Pani marszałek, czas.) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, pani poseł.",
                },
                {
                    "speaker": "Poseł Marlena Magdalena Maląg",
                    "content": "Panie premierze, proszę odpowiedzieć, bo pan mówi, że to, co dane, będzie realizowane…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, pani poseł.",
                },
                {
                    "speaker": "Poseł Marlena Magdalena Maląg",
                    "content": "…a pana parlamentarzyści mówią o tym, że będzie trzeba zwijać czerwone dywany. Jaka jest rzeczywistość? Jaka jest prawda? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł. Do głosu zapraszam pana posła Marcina Grabowskiego, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marcin Grabowski",
                    "content": "Pani Marszałek! Najwyższa Izbo! Panie Premierze! Chciałbym z tego miejsca zadać pytanie panu premierowi. Moi przedmówcy wielokrotnie wspominali jednostki wojskowe. Na początku tego roku minister obrony narodowej pan Mariusz Błaszczak ogłosił bardzo dobrą wiadomość, powstanie pułku przeciwlotniczego 1. Dywizji Piechoty Legionów w Ostrołęce. Panie premierze, moje pytanie jest następujące: Czy ta polityka obecnego rządu będzie kontynuowana? Bezpieczeństwo jest dla nas, Polaków – myślę, że wszystkich z nas, jak tutaj jesteśmy – priorytetem, a dzisiejszy dzień pokazuje, że to bezpieczeństwo jest zagrożone. Wszystkiego dobrego. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję. Do głosu zapraszam pana posła Przemysława Czarnka, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Marszałku Hołownia! Pan uciekł przed nami, mimo że skandal dalej jest i trzeba go wyjaśnić. (Głos z sali: Bo się boi.) Przypomnijmy: 13 listopada, wystąpienie pana posła Brauna, brutalny atak na panią marszałek Witek. Nie przeszkadzało to panu marszałkowi Hołowni. (Głos z sali: Śmiał się.) Kolejny dzień, brutalny atak na pana prezesa Jarosława Kaczyńskiego i na posłów Prawa i Sprawiedliwości. Nie przeszkadzało to panu marszałkowi Hołowni. (Głos z sali: Cieszył się.) Kolejny dzień i kolejne posiedzenie, nasze kolejne spotkanie, antysemickie wycieczki pod adresem Mateusza Morawieckiego i innych. (Poseł Konrad Berkowicz: Kłamstwo! Nie były antysemickie.) Nie przeszkadzało to panu marszałkowi Hołowni. Następnie wczorajsza brutalna prowokacja pana Donalda Tuska, chamska, brutalna prowokacja dotycząca katastrofy smoleńskiej. Pan jako ówczesny premier jest odpowiedzialny politycznie za to, co się stało w Smoleńsku. Pan wczoraj dopuścił się absolutnie skandalicznej prowokacji pod adresem Jarosława Kaczyńskiego. Nie przeszkadzało to panu Hołowni. (Oklaski) A dzisiaj przeszkadza panu Hołowni, że wypominamy mu, że tak naprawdę obezwładnił Straż Marszałkowską, dopuścił wszystkich (Dzwonek) wszędzie i tego rodzaju skandale musiały się wydarzyć. Nie myśleliśmy, że tak wcześnie…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Panie pośle, dziękujemy bardzo.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "…i nie wiedzieliśmy, że będą miały podłoże antysemickie, w polskim parlamencie, i doprowadzą do skandalu międzynarodowego, stawiając nas wszystkich w tragicznym świetle. (Głos z sali: Czas!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy bardzo, panie pośle. Proszę konkludować.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "Skandal, panie marszałku Hołownia. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Chcę panu posłowi przypomnieć, że nazywam się Dorota Niedziela i nie jestem panem marszałkiem Hołownią. Do głosu zapraszam pana posła Michała Moskala, Klub Parlamentarny Prawo i Sprawiedliwość Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów",
                },
                {
                    "speaker": "Poseł Michał Moskal",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! To waszym hasłem było: dym w kościołach. Wszystko można było zrobić przez ostatnich 8 lat. To, co robiliście pani marszałek Elżbiecie Witek, to, jak zakłócaliście uroczystości kościelne – to było przez was absolutnie akceptowane. (Głos z sali: Wstydźcie się!) Dzisiaj unikacie odpowiedzialności za to, że hodowaliście cichego koalicjanta, jak wynikało z taśm Chmaja… (Głos z sali: Atmosfera przyzwolenia.) …za to, że zarządzacie Sejmem i nie potraficie zadbać o jego bezpieczeństwo. To jest Sejm zarządzany przez marszałka Hołownię, który dzisiaj ucieka. Za chwilę będzie przemawiał minister Czarnek, więc marszałka Hołowni już tutaj nie ma. Przestraszył się. Nie ma go wtedy, kiedy jest potrzebny. To jest skandal, jak prowadzicie te obrady, i to jest skandal, jak zarządzacie Sejmem. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Jednak nie podziękuję panu posłowi. Do głosu zapraszam pana posła Dariusza Stefaniuka, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Dariusz Stefaniuk",
                    "content": "Szanowna Pani Marszałek! Szanowny Panie Premierze! Wysoka Izbo! Mam wiele pytań do pana premiera, ale mam nadzieję, że będzie jeszcze okazja zadać te pytania. Szanowni Państwo! To, co się wydarzyło tutaj przed kilkoma godzinami, to jest absolutna odpowiedzialność pana marszałka Szymona Hołowni. (Głos z sali: Tak jest.) To pan marszałek Szymon Hołownia ma całą Kancelarię Sejmu, to pan marszałek Szymon Hołownia zarządza całą Strażą Marszałkowską i to jest obowiązek pana marszałka Szymona Hołowni, żeby dbać o bezpieczeństwo wszystkich parlamentarzystów i osób znajdujących się w budynkach sejmowych. To pan marszałek Szymon Hołownia uciekł jak tchórz do tamtego gabinetu. (Poseł Sławomir Nitras: Ale co to za słowa, człowieku.) Gdy tylko zwrócił uwagę panu Braunowi, oddał prowadzenie obrad panu marszałkowi Bosakowi i dzisiaj podnosi wielkie larum, pyta, dlaczego pan marszałek Bosak nie sprawdził się w roli prowadzącego. Ja pytam, dlaczego pan marszałek Hołownia nie został tutaj do samego końca i nie prowadził tych obrad, tylko uciekł. Dzisiaj Lewica (Dzwonek) zgłasza uchwałę dotyczącą potępienia antysemityzmu. My tę uchwałę poprzemy, ale to będzie cynizm, jeżeli nie dodacie do tej uchwały potępienia wszystkich…",
                },
                {"speaker": "Wicemarszałek Dorota Niedziela", "content": "Dziękujemy."},
                {
                    "speaker": "Poseł Dariusz Stefaniuk",
                    "content": "…ekscesów dotyczących Kościoła katolickiego i zakłócania mszy świętych. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle. Do głosu zapraszam pana posła Piotra Uścińskiego, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Piotr Uściński",
                    "content": "Szanowna Pani Marszałek! Panie Pośle desygnowany na premiera! Szanowni Państwo! Wysoka Izbo! Chciałem zadać panu premierowi Tuskowi pytania dotyczące mieszkalnictwa, bo o mieszkalnictwie, o budownictwie nie zająknął się w swoim exposé ani jednym słowem. Chciałem zapytać o przyszłość kredytu 0%, waszej obietnicy ze 100 konkretów, co do której sami nie możecie się dogadać wewnątrz waszej koalicji parlamentarnej. Ale to, co się dzisiaj stało, ten eksces, ten atak na uroczystość religijną, zmusza mnie do zadania innego pytania. Na czym będzie polegało opiłowywanie katolików w dzisiejszej Polsce? (Oklaski) Jak będziecie robili faktycznie rozdział państwa od Kościoła? Bo to, co dzisiaj widzieliśmy, to jest ewidentnie działanie podżegane przez was, przez to mówienie o rozdzielaniu państwa od Kościoła. (Głos z sali: Skandal! Skandal!) (Głos z sali: Tak, to jest skandal.) Nie możemy zgodzić się na to, żeby uroczystości patriotyczne, religijne, dotyczące jakiejkolwiek religii były zakłócane (Dzwonek) w polskim państwie. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Zapraszam do głosu pana posła Jerzego Polaczka, Klub Parlamentarny Prawo i Sprawiedliwość Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 740",
                },
                {
                    "speaker": "Poseł Jerzy Polaczek",
                    "content": "Pani Marszałek! Wysoka Izbo! Chciałbym Wysokiej Izbie przypomnieć, że symboliczne święto Chanuka w 2006 r. wprowadził ówczesny marszałek Marek Jurek, wybrany z listy Prawa i Sprawiedliwości. (Oklaski) (Głos z sali: Tak jest, tak jest.) Warto to przypomnieć w świetle tego haniebnego skandalu i chuligaństwa posła Grzegorza Brauna. Ale chciałbym również zwrócić uwagę, że ta hańba dzisiejsza odbywała się w kontekście tablicy upamiętniającej ponad 100 posłów II Rzeczypospolitej poległych w łagrach, obozach koncentracyjnych oraz tych, którzy zginęli na frontach II wojny światowej, oraz w kontekście i sąsiedztwie tablicy smoleńskiej upamiętniającej posłów wszystkich klubów, którzy zginęli 10 kwietnia 2010 r. Chciałbym panu premierowi Tuskowi zadać pytanie. Z racji braku czasu będzie tylko jedno: Czy pan premier Donald Tusk zamierza powierzyć funkcję wiceministra kultury i dziedzictwa narodowego (Dzwonek) pani poseł Scheuring-Wielgus, która kilka lat temu przewiozła w bagażniku kilka nieuprawnionych osób na teren Sejmu oraz zakłócała uroczystości religijne w Toruniu? (Głos z sali: I zakłócała msze.) Czy to jest pański kandydat na wiceministra kultury i dziedzictwa narodowego? (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Do głosu zapraszam posła Marcina Romanowskiego, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marcin Romanowski",
                    "content": "Bardzo dziękuję. Pani Marszałek! Wysoka Izbo! Szanowni Państwo! W związku z dzisiejszym incydentem chciałbym wyrazić nadzieję, wręcz wezwać państwa do poparcia ustawy w obronie wolności religijnej, która właśnie tego typu incydenty w sposób zobiektywizowany penalizuje. Natomiast w związku z exposé pana premiera, panie premierze, chciałbym zadać pytanie, które z niepokojem zadają sobie mieszkańcy Lubelszczyzny, mieszkańcy całej Polski wschodniej. Czy pański rząd zamierza powrócić do obowiązującej przed 2015 r. strategii obrony Polski na linii Wisły? Czy w ramach zapowiadanych cięć budżetowych znowu będziecie likwidowali jednostki wojskowe, szczególnie właśnie na terenach wschodnich? Czy w związku z tym pański gabinet ma zamiar porzucić Polskę wschodnią, wstrzymać realizowane inwestycje, ograniczyć je i przywrócić (Dzwonek) tę niechlubną tradycję nazywania jej Polską B, dokładnie z taką pogardą, jak to przed laty wyraził pana współpracownik, który niedawno po wyjściu z aresztu objął mandat europosła? Bardzo dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze pan poseł Antoni Macierewicz, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Antoni Macierewicz",
                    "content": "Pani Marszałek! Wysoka Izbo! To, co się stało, ma swoją genezę w polityce nienawiści, jaką wasza formacja realizowała przynajmniej od zbrodni smoleńskiej. (Oklaski) (Głos z sali: To wy, to wy.) Ta nienawiść wobec Lecha Kaczyńskiego, ta nienawiść wobec jego brata pana Jarosława Kaczyńskiego, ta nienawiść wobec polskich patriotów, którzy pamiętają o tej zbrodni i dążą do tego, żeby mówić o niej prawdę… (Głos z sali: A ile milionów?) (Głos z sali: Kłamcą, kłamcą jesteś.) To wy upowszechniacie właśnie nienawiść, to wy sprawiacie, że człowiek, który jest dzisiaj marszałkiem Sejmu, Hołownia, doprowadził do takiego chaosu w Sejmie, który sprawia, że każda agresja jest możliwa. (Dzwonek) To wasza odpowiedzialność. Proszę odpowiedzieć na pytanie, dlaczego chroni pan pana Putina, chroni pan, wiedząc – od roku 2010 ma pan pełną wiedzę i dowody, od listopada 2010 r. – że piloci nie byli winni. (Głos z sali: Pani marszałek…) (Poseł Krystyna Skowrońska: Pani marszałek…) (Poseł Cezary Tomczyk: Pani marszałek, to już jest po czasie.) Pan o tym wie. Pan przekazał tę informację… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) (Poseł Donald Tusk: Bezwstydny jesteś.) (Poseł Sławomir Nitras: Zejdź z mównicy.) (Poseł Donald Tusk: Jesteś zwykłą hieną.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Panie pośle, bardzo proszę zakończyć swoją wypowiedź. Proszę zejść z mównicy. Zapraszam do głosu panią poseł Elżbietę Witek, Klub Parlamentarny Prawo i Sprawiedliwość. (Oklaski)",
                },
                {
                    "speaker": "Poseł Elżbieta Witek",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Nie uzurpuję sobie prawa do występowania w imieniu wszystkich kobiet w Polsce, w przeciwieństwie do tej strony sali, ale ponieważ najwięcej kobiet zagłosowało na Prawo i Sprawiedliwość, mam prawo występować w imieniu tych kobiet, które są w grupie prawie 8 mln obywateli (Oklaski), którzy zagłosowali na Prawo i SpraPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 741 wiedliwość. Jaka była sytuacja i prawa polskich kobiet, o których pan tak długo i dużo mówi, wiemy i pamiętamy. Tu, na tej sali, jest nas wielu. (Poseł Sławomir Nitras: Wiele.) Pamiętamy dokładnie tamte czasy. Pamiętamy eurosieroctwo. Pamiętamy pozostawianie dzieci pod opieką dziadków i wyjazdy matek za granicę. Pamiętamy zabieranie dzieci z powodu biedy z rodzin. (Głos z sali: Kłamstwo.) (Poseł Izabela Leszczyna: Kłamie pani.) Pamiętamy – wtedy kiedy była przemoc domowa – że to kobiety uciekały z domu, a nie oprawca. Dopiero my to zmieniliśmy. Pamiętamy też sytuację nauczycielek – bo to są głównie nauczycielki pracujące w edukacji, w oświacie – kiedy w trakcie gry zmieniliście zasady gry, czyli odebraliście prawo do przejścia na wcześniejszą emeryturę nauczycielkom. (Głos z sali: Zniszczyliście zawód nauczyciela.) (Głos z sali: Skandal!) Była taka sytuacja, że dwie nauczycielki… (Głos z sali: Pani by wyłączyła już mikrofon.) Proszę wyłączyć, jeżeli pani chce. Ja nie będę protestować, zapewniam pana.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pani poseł, proszę do rzeczy i proszę zakończyć wypowiedź.",
                },
                {
                    "speaker": "Poseł Elżbieta Witek",
                    "content": "Panie Premierze! Ale ważniejsza sprawa. Podwyższyliście wiek emerytalny kobietom o 7 lat, na wsi o 12 lat. (Głos z sali: Ej, czas się skończył.) Pańscy doradcy, ale także politycy Platformy Obywatelskiej i nie tylko…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pani poseł, bardzo proszę…",
                },
                {
                    "speaker": "Poseł Elżbieta Witek",
                    "content": "…mówili o tym, że Polacy powinni pracować dłużej. Proszę odpowiedzieć na pytanie, jaką macie politykę związaną z emeryturami. (Gwar na sali)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pozwólcie państwo…",
                },
                {
                    "speaker": "Poseł Elżbieta Witek",
                    "content": "Czy zamierzacie podnieść wiek emerytalny, w tym wiek emerytalny dla kobiet? Bardzo proszę odpowiedź na to pytanie. (Oklaski) (Poseł Monika Wielichowska: 100 razy pani to już słyszała. Nie dotarło?)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Chcę tylko powiedzieć, że wielokrotnie nie miałam takiej możliwości, pani marszałek, żeby dokończyć swoją wypowiedź. (Poseł Elżbieta Witek: Pani marszałek, proszę mi odebrać głos, jeśli takie są zasady.) Do głosu zapraszam panią poseł Mirosławę Stachowiak-Różecką, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Mirosława Stachowiak-Różecka",
                    "content": "Pani Marszałek! Wysoka Izbo! Wspaniały mieliśmy spektakl przez kilka tygodni, pierwsze posiedzenie Sejmu, światła, konferencje, tiktoki, filmiki, wynajęte sale kinowe, wszyscy obserwowali, jak było wspaniale. Gdy przyszedł pierwszy problem, pierwszy prawdziwy klops, kiedy jeden z aktorów w tym teatrze po prostu odegrał tę rolę nie tak, jak przewidziała to ta większość na sali sejmowej, to okazało się, że światła gasną, debatę na temat exposé szybciutko trzeba skrócić, najlepiej o tym dniu zapomnieć i koniec przedstawienia. (Oklaski) Już uciekający pan marszałek – teraz już można powiedzieć nie rotacyjny, tylko uciekający marszałek – nie widzi potrzeby, żeby tutaj to przedstawienie trwało, bo pojawił się pierwszy problem. Krótkie pytanie, jeśli pani pozwoli, może mi nie przerwie, żeby jednak było do przyszłego pana premiera. (Dzwonek) (Głos z sali: Koniec czasu.) (Głos z sali: Czas wyłączyć.) Wicemarszałek Senatu Marcin Żywno z Polski 2050 mówi…",
                },
                {"speaker": "Wicemarszałek Dorota Niedziela", "content": "Pani poseł…"},
                {
                    "speaker": "Poseł Mirosława Stachowiak-Różecka",
                    "content": "…że Polska nie może sobie pozwolić na utrzymywanie obecnych relacji z Białorusią… (Poseł Izabela Leszczyna: Mówi pani nie na temat.) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 742",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy bardzo, pani poseł.",
                },
                {
                    "speaker": "Poseł Mirosława Stachowiak-Różecka",
                    "content": "…że nie ma wyjścia i musi rozpocząć z nią rozmowę.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pani dużo czasu poświęciła na wprowadzenie. Dziękuję bardzo.",
                },
                {
                    "speaker": "Poseł Mirosława Stachowiak-Różecka",
                    "content": "Pytam zatem, jak te rozmowy, jak to nowe otwarcie… (Poseł Tomasz Zimoch: Ale czas minął.) …z Białorusią i z Łukaszenką ma wyglądać? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Do głosu zapraszam pana posła Marka Asta, klub Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marek Ast",
                    "content": "Pani Marszałek! Wysoka Izbo! Klub Prawa i Sprawiedliwości jednoznacznie potępia wszelkie akty antysemityzmu zarówno na tej sali, w tym obiekcie, jak i w przestrzeni publicznej. Ale ja chciałbym wiedzieć, czy wybrany przez większość sejmową prezes Rady Ministrów potępi akty przemocy, wandalizmu wobec członków Kościoła katolickiego i każdego innego Kościoła? (Oklaski) Czy potępi akty przemocy, bezczeszczenia i zakłócania uroczystości o charakterze żałobnym i religijnym (Oklaski), które odbywają się co miesiąc w Warszawie na placu Piłsudskiego przed pomnikiem upamiętniającym ofiary tragedii smoleńskiej, jak i śp. prezydenta Lecha Kaczyńskiego? (Poseł Antoni Macierewicz: To jest nienawiść.) Chciałbym to wiedzieć i chciałbym wiedzieć (Dzwonek), jakie działania podejmie prezes Rady Ministrów, aby tego rodzaju aktom zapobiec w przyszłości. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle. Do głosu zapraszam pana posła Artura Chojeckiego, Klub Parlamentarny PiS. (Głos z sali: Prawo i Sprawiedliwość, pani marszałek.) Prawo i Sprawiedliwość, pani poseł. Za każdym razem używam… Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Artur Chojecki",
                    "content": "Pani Marszałek! Wysoka Izbo! Władza wiąże się z odpowiedzialnością, a komu więcej dano, od tego będą więcej wymagać. Te słowa powinny być znane zarówno panu marszałkowi i – jak sądzę – także panu premierowi. Dzisiejsze skandaliczne wydarzenie w Sejmie obciąża na pewno przede wszystkim jego autora, ale także obciąża władze Sejmu i stojącą za nim większość parlamentarną. Chciałem zadać pytanie o bezpieczeństwo mieszkańców mojego województwa, województwa warmińsko-mazurskiego, w kontekście bliskości granicy z Federacją Rosyjską, w kontekście odtwarzania jednostek wojskowych. Ale czy od państwa można w ogóle oczekiwać dbałości i odpowiedzialności za bezpieczeństwo państwa? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Do głosu zapraszam pana posła Janusza Cieszyńskiego, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Janusz Cieszyński",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Pan marszałek Hołownia zapowiadał walkę o złoty przycisk. Niestety skończyło się patostreamem. Wstyd. Panie Premierze! Rozpoczął pan swoje exposé od odczytania listu człowieka, który targnął się na swoje życie. Do takich spraw trzeba podchodzić bardzo odpowiedzialnie, kiedy się o nich wspomina. Ministerstwo Cyfryzacji w 2022 r. rozpoczęło współpracę z Niebieską Linią, która prowadzi telefon zaufania dla dorosłych w kryzysie. On jest dostępny dla wszystkich pod bezpłatnym numerem 116 123. Podobny numer 116 111 prowadzi Fundacja Dajemy Dzieciom Siłę. Pani poseł, też o tym powiem. Warto o tym pamiętać, bo nigdy nie wiemy, kiedy ktoś bliski albo my sami się znajdziemy w takiej trudnej sytuacji. I dlatego, panie premierze, chciałbym zapytać: Czy pana rząd (Dzwonek) będzie kontynuował wsparcie dla Niebieskiej Linii? Czy pod 116 123 będzie się dało dodzwonić przez całą dobę?",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Janusz Cieszyński",
                    "content": "Czy odbieralność będzie na tym poziomie, na którym jest teraz dzięki rządowej dotacji? Dziękuję. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 743",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Do głosu zapraszam pana posła Pawła Szrota, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Paweł Szrot",
                    "content": "Pani Marszałek! Wysoka Izbo! Hańba dla Grzegorza Brauna, szacunek dla wszystkich symboli religijnych. Grzegorz Braun w swoim pierwszym wystąpieniu w tej kadencji bezpardonowo i bezprzykładnie zaatakował panią marszałek Elżbietę Witek zgodnie z linią polityczną tej strony sali. Pani marszałek, nie ma dla pani lepszej pochwały i lepszej rekomendacji niż ten atak Grzegorza Brauna. (Oklaski) Panie Premierze! Mam pytanie do pana: Czy zamierza pan powierzyć jakieś jedno ze stanowisk rządowych panu posłowi Romanowi Giertychowi, byłemu przewodniczącemu Ligi Polskich Rodzin, byłemu przewodniczącemu Młodzieży Wszechpolskiej, który, wiele lat temu oczywiście, pisał w swoich publikacjach m.in.: Już 50 lat nasza ojczyzna dźwiga na swoim grzbiecie takie parchy jak wy. (Oklaski) (Głos z sali: Uuu…)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Do głosu zapraszam panią poseł Małgorzatę Golińską, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Małgorzata Golińska",
                    "content": "Pani Marszałek! Panie Premierze! Czyn pana posła Brauna, zakłócanie żydowskiej uroczystości religijnej, jest haniebny i zasługuje na potępienie. Ale na potępienie zasługują również czyny związane z zakłócaniem mszy św., w których niestety brali udział posłowie koalicji. Czy potępiając zachowanie pana posła Brauna, potępicie również zachowanie swoich posłów? (Oklaski) A w nawiązaniu do exposé, panie premierze, zapowiada pan walkę ze smogiem. Oczywiście to jest bardzo ważny temat. Zapomina pan jednak dodać, że ta walka za waszych rządów została podsumowana wyrokiem TSUE za zaniechanie w tym obszarze w latach 2007–2015 i dopiero szereg działań Prawa i Sprawiedliwości spowodował, że jakość powietrza w naszym kraju poprawia się, co potwierdzają wyniki państwowego monitoringu środowiska i roczne oceny jakości powietrza. (Oklaski) Zapowiada pan zakaz sprowadzania śmieci do Polski, zapominając powiedzieć, że taki zakaz wprowadziliśmy w 2018 r. w ustawie. (Dzwonek) Zapowiadacie również projekt odnowy bagien i torfowisk, nie dodając, że ten program funkcjonuje od zeszłego roku. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pani poseł, proszę zmierzać do końca.",
                },
                {
                    "speaker": "Poseł Małgorzata Golińska",
                    "content": "Czy prowadząc takie działania, które prowadziło Prawo i Sprawiedliwość, zadeklarujecie, że utrzymacie również szereg innych ważnych programów, chociażby związanych z polityką niskich podatków? Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Zapraszam do głosu pana posła Roberta Telusa, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Robert Telus",
                    "content": "Szanowna Pani Marszałek! Szanowny Sejmie! Drodzy Państwo! To, co się dzisiaj stało, jest wielkim skandalem. Skandalem, przez który chyba cały świat usłyszy o polskim Sejmie. Ale współwinnym tego jest marszałek Hołownia. (Poseł Paweł Zalewski: To skandal.) (Głos z sali: A jak pan latał z gaśnicą, to kto był winien?) Panie Marszałku! Uciekł pan dzisiaj z obrad, ale to pan jest współodpowiedzialny. Prowadzenie Sejmu, bycie marszałkiem, to nie jest popcorn, to nie są podcasty, to nie jest bicie rekordów na YouTube. To nie jest łapanie pcheł, jak pan mówił. To nie jest kpienie, to nie jest program reality show, to nie jest „Mam talent!”. To jest odpowiedzialna funkcja. A pan z tej funkcji nie zdał egzaminu, pan uciekł. To jest pana odpowiedzialność. Ale również, panie premierze z 13 grudnia, pan jest odpowiedzialny. Pan dzisiaj dziękował właśnie tym łobuzom, którzy na swoich protestach krzyczeli: dym w kościołach. To im pan dzisiaj dziękował. (Oklaski) Ma pan w swojej koalicji posłów (Dzwonek), którzy… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję bardzo, panie pośle. Panie pośle Telus, proszę opuścić mównicę. (Poseł Paweł Zalewski: Pani marszałek, proszę o głos.) Do głosu zapraszam pana posła Krzysztofa Cieciórę, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Krzysztof Ciecióra",
                    "content": "Szanowna Pani Marszałek! Wysoki Sejmie! A miało być tak fajnie. Ludzie mieli się do siebie uśmiechać, Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 744 mieli być sympatyczni, miały być lajki, suby, fejm w Internecie. To wszystko było na wyciągnięcie ręki, tylko ten Braun tak nagle zerwał wam się z tej smyczy. Jak to się stało? Było fajnie, kiedy on wchodził na tę mównicę i obrażał, mieszał z błotem naszych parlamentarzystów. Biliście brawo, cieszyliście się. (Głos z sali: Nie kłam.) Szanowni Państwo! Chciałbym powiedzieć, że my jako posłowie Stowarzyszenia OdNowa będziemy chcieli poprzeć tę uchwałę złożoną przez panią poseł z Lewicy. Ale liczę na to, że… (Gwar na sali) (Głos z sali: Tak było, tak było.) (Poseł Krystyna Skowrońska: Kłamiesz!) Proszę się nie śmiać. …nie zabraknie elementarnej uczciwości i w tej uchwale zawrzecie również potępienie utrudniania przeprowadzania mszy świętych, jakichkolwiek obrządków religijnych. To jest miarą waszej wiarygodności i tego, czy macie czyste intencje. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Do głosu zapraszam pana posła Jana Mosińskiego, Klub Parlamentarny Prawo i Sprawiedliwość. Proszę państwa, rozumiem, że państwo nie macie pytań do premiera, ponieważ 90% waszych wypowiedzi jest o występach pana Brauna, a nie ma pytań do pana premiera. (Głos z sali: Mamy, mamy.) (Głos z sali: Każdy zadaje pytanie.) (Głos z sali: Wyłącz za hejt.) (Głos z sali: Konstytucja.) Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Jan Mosiński",
                    "content": "Pani Marszałek! Wysoka Izbo! Marszałek Sejmu stoi na straży praw, godności i powagi Sejmu. Niestety nie zdał egzaminu z tych obowiązków, za to straszy nas komisją regulaminową i komisją etyki. Wątpliwa to obrona. (Głos z sali: Już to słyszeliśmy.) (Poseł Paweł Zalewski: Do rzeczy. Proszę zadawać pytania premierowi.) Tak samo jak nie zdał egzaminu premier in spe Donald Tusk, kiedy był premierem, kiedy zrobiono nalot służb na tygodnik, jeden z tygodników. Nie zdała pana formacja egzaminu z dialogu społecznego z górnikami i robotnikami, kiedy wdeptaliście dialog społeczny w pośniegowe błoto przed Jastrzębską Spółką Węglową, strzelając, o zgrozo, z broni gładkolufowej do broniących swoich miejsc pracy górników. (Głos z sali: To gen. Szymczyk.) I dzisiaj górnicy mówią: panie pośle, niech pan zapyta Donalda Tuska, czy za jego rządów znowu będą strzelać z broni gładkolufowej do protestujących robotników, którzy będą bronić swoich miejsc pracy. To po pierwsze. I po drugie, jeszcze pan nie rządzi, a dwóch dziennikarzy już nie otrzymało akredytacji: jeden dziennikarz Polskiego Radia i dziennikarz Telewizji Polskiej, którzy chcieli lecieć na szczyt Rady Europejskiej. (Dzwonek) (Głos z sali: Wstyd! Hańba!) Gratuluję odwagi i działań w prześladowaniu wolności wolnej prasy i mediów. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy panu posłowi. Do głosu zapraszam pana posła Jana Warzechę, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Jan Warzecha",
                    "content": "Panie Premierze! Lekarza Władysława Kosiniaka-Kamysza uczynił pan ministrem obrony narodowej. Dariusza Wieczorka, inżyniera elektryka, fachowca od OZE i energetyki, powołuje pan na ministra nauki i szkolnictwa wyższego. Izabelę Leszczynę, nauczycielkę, polonistkę, rekomenduje pan na ministra zdrowia. Posła Dariusza Klimczaka, politologa, kieruje pan do Ministerstwa Infrastruktury. Na ministra sportu mianuje pan Sławomira Nitrasa, kolejnego politologa, pseudonim „Pilnik”. (Głos z sali: Ha, ha, ha!) Określenie pochodzi od jego zapowiedzi piłowania katolików. (Oklaski) Krzysztofa Gawkowskiego, kolejnego politologa i humanistę, autora powieści kryminalnych, sadowi pan w Ministerstwie Cyfryzacji. Paulinę Hennig-Kloskę politologa i współautorkę lobbystycznej ustawy wiatrakowej, nazywanej lex Kloska, nagradza pan Ministerstwem Klimatu i Środowiska. (Głos z sali: Właśnie tak.) Natomiast Agnieszkę Dziemianowicz-Bąk, filozofkę (Dzwonek), zwolenniczkę bezpłatnej i legalnej aborcji do 12. tygodnia życia, czyni pan, uwaga, szefową resortu rodziny. (Głos z sali: Czas się skończył.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Proszę kończyć, panie pośle.",
                },
                {
                    "speaker": "Poseł Jan Warzecha",
                    "content": "Zadaję więc pytanie: Czy te osoby i fakty dają Polakom rękojmię kompetentnego rządu? Dziękuję bardzo. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 745",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Do głosu zapraszam pana posła Grzegorza Lorka, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Grzegorz Lorek",
                    "content": "Pani Marszałek! Panie Premierze! Wysoka Izbo! Jak wiecie państwo, 10. dnia każdego miesiąca modlimy się za ofiary smoleńskie, modlimy się za wszystkie ofiary smoleńskie. I co się wtedy dzieje? Buczenie, śmiech, pogarda. Nawet teraz widzę uśmiechy. My się modlimy za wszystkich jako katolicy. A wy co robicie? Robicie wszystko, żeby nam w tym przeszkodzić. Panie Premierze! Czy pana środowisko zacznie wreszcie oddawać cześć ofiarom smoleńskim? (Oklaski) Panie Premierze! Kultury trzeba się uczyć zawsze i wszędzie. Mam nadzieję, że pana obóz po dzisiejszych wydarzeniach też to zrozumie. Dziękuję. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze poseł Kacper Płażyński, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Kacper Płażyński",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Nie dalej jak rok temu spotykał się pan jako przewodniczący Rady Europejskiej z panią Martą Lempart, która pochwalała niszczenie kościołów. Mam nadzieję, że dzisiaj jest panu trochę wstyd. (Głos z sali: Tak jest.) Jednocześnie na Pomorzu, szanowni państwo, marszałek Struk, marszałek województwa pomorskiego i szef Platformy Obywatelskiej w województwie pomorskim, publicznie mówi o tym, że należy wznowić procedurę wydania decyzji środowiskowej dla elektrowni jądrowej w Choczewie. Decyzja, która teraz została wydana… Trwało to wiele lat, panie premierze, 7 lat to trwało. Zastanawiam się, czy to jest państwa sposób na wycofanie się z realizacji projektu jądrowego, czy tak naprawdę w taki sposób chcecie to rozsadzić. Chciałbym uzyskać pana deklarację, panie premierze, że wy naprawdę chcecie tę elektrownię jądrową w Choczewie wybudować, tak jak to jest przedstawione w harmonogramie. Jeżeli nie, to jest to bardzo niebezpieczne dla przyszłości naszego kraju, dla cen energii, dla życia (Dzwonek) normalnego Polaka. Mam nadzieję, że nam pan tego nie zrobi. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze pan poseł Piotr Müller, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Piotr Müller",
                    "content": "Szanowna Pani Marszałek! Szanowny Panie Premierze! Dzisiaj pan premier przypomniał sobie o 100 konkretach, które zapowiadaliście w czasie kampanii wyborczej, gdy minister Waldemar Buda przyniósł to panu na mównicę sejmową. W związku z tym mam do pana pytanie o dokładny harmonogram wdrożenia każdego z tych najważniejszych punktów programowych. (Głos z sali: W 100 dni.) Chodzi o wdrożenie kwoty wolnej od podatku, wdrożenie wielu innych projektów, które pan zapowiadał. Pan zadeklarował, co było oczywiście dobrą deklaracją i mam nadzieję, że prawdziwą, że odpowie pan na każde pytanie. W związku z tym to jest jedno z głównych pytań. Drugie pytanie nawiązuje do tego, co przed chwilą powiedział pan poseł Płażyński. Ze strony pana klubu parlamentarnego padały stwierdzenia dotyczące wątpliwość w związku z budowaniem elektrowni jądrowej na Pomorzu. W związku z tym proszę o jasną odpowiedź: Czy realizacja tego projektu z tymi inwestorami, z tymi umowami, które zostały podpisane, będzie kontynuowana? Czy będzie kontynuowany projekt budowy farm wiatrowych na morzu? Chodzi o projekty, których realizacja została rozpoczęta przez spółki Skarbu Państwa i powinny być kontynuowana, projekty, które zapewniają bezpieczeństwo Polski. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Do głosu zapraszam pana posła Kazimierza Smolińskiego, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Kazimierz Smoliński",
                    "content": "Pani Marszałek! Panie Premierze! W 100 konkretach ma pan zapis dotyczący odpolitycznienia sądów, tych sądów, które uwalniały od odpowiedzialności osoby, które atakowały kościoły, atakowały księży. Rozumiem, że teraz będą sądy, które będą skazywać tych, którzy zachowują się tak jak dzisiaj pan Braun, nie kto inny. Myślę, że szybko zapadnie decyzja w tej sprawie. Powiedział pan, że prokurator nie może być politykiem, a powołuje pan pana Bodnara, który jest uznawany za tzw. mesjasza Lewicy, czyli waszego polityka, który został senatorem. On będzie prokuratorem generalnym. Mam pytanie. Czy takie słowa jak: faszyści, menele, żulia, nieroby, patologia, zaścianek, pijacy, biedota, potomkowie chłopów folwarcznych, PiS-owska szarańcza, osiem gwiazdek, czy nie uważa pan… To jest słownictwo, które wychodzi z pana (Dzwonek) zaplecza i pan to tolerował. Czy pan się od tego odetnie, od ośmiu gwiazdek? Nigdy tego nie słyszałem. (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 746",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle. Do zabrania głosu zapraszam posła Andrzeja Adamczyka, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Andrzej Adamczyk",
                    "content": "Dziękuję bardzo. Pani Marszałek! Wysoka Izbo! Panie Premierze! Pan marszałek Hołownia nie zdał egzaminu. Myślę, że to memento, to dzisiejsze wydarzenie pozwoli mu podjąć właściwe decyzje i zachowa się jak trzeba. Jeśli chodzi o exposé, które pan wygłosił, to nie będę pytał, panie premierze, o zawarte w exposé deklaracje czy też o wcześniej ogłoszone programy. Zapytam o to, czego pan nie obiecał. Pamiętamy doskonale 2011 r. Nie obiecał pan wtedy w swoim exposé podniesienia wieku emerytalnego. W 2007 r. – doskonale pamiętam to długie wystąpienie, które obfitowało w szczegóły – nie obiecał pan, że przerwiecie realizację Via Carpatii, tak bardzo dzisiaj potrzebnej. Gdybyście (Dzwonek) wówczas tego nie zrobili, to dzisiaj mielibyśmy bez mała drogę rokadową. Pan doskonale o tym wie. (Poseł Krystyna Skowrońska: Zaczęto…) Pytanie brzmi: Czy takie projekty jak Via Carpatia im. prezydenta Lecha Kaczyńskiego będą przerywane? Dziękuję bardzo. (Oklaski) (Głos z sali: Ooo…)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Do zabrania głosu zapraszam panią poseł Marię Koc, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Maria Koc",
                    "content": "Bardzo dziękuję. Szanowna Pani Marszałek! Wysoka Izbo! Panie Premierze! Większość sejmowa przedstawia pana premiera Donalda Tuska jako męża stanu, wręcz wybawiciela narodu, a pan Donald Tusk to polityk, którego wielu Polaków się boi. Boją się, bo pamiętają pańskie niedobre dla Polski rządy. Pamiętają, że podwyższył pan Polakom wiek emerytalny, zabrał oszczędności z OFE, zafundował kilkunastoprocentowe bezrobocie… (Poseł Krystyna Skowrońska: Nieprawda, kłamiesz.) …nie dbał o najsłabszych, współpracował z Putinem i prowadził politykę resetu z Rosją, a na koniec porzucił Polskę dla stanowisk w Brukseli. (Poseł Krystyna Skowrońska: Same kłamstwa.) Panie Premierze! Ludzie nie mają do pana zaufania, bo pan co innego mówi, a co innego robi. Ma pan usta pełne frazesów, mówi o miłości, o szacunku, a Polska pamięta, jak pan traktował prezydenta Lecha Kaczyńskiego i jak traktuje pan oponentów politycznych. Mam pytanie do pana premiera dotyczące Polski Wschodniej. Polska Wschodnia (Dzwonek) to regiony, które były zapomniane przez pana za pańskich poprzednich rządów. Zostały upodmiotowione dopiero przez rząd Mateusza Morawieckiego.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, pani poseł, proszę zmierzać do końca.",
                },
                {
                    "speaker": "Poseł Maria Koc",
                    "content": "Mam pytanie: Czy będzie pan kierował duże środki finansowe…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł.",
                },
                {
                    "speaker": "Poseł Maria Koc",
                    "content": "…z budżetu państwa na inwestycje lokalne w Polsce Wschodniej i czy będziecie szanować Polskę Wschodnią? Bo powołanie do rządu… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pani poseł, bardzo proszę…",
                },
                {
                    "speaker": "Poseł Maria Koc",
                    "content": "…kraju mówił, że to kamieni kupa, nie daje takiej nadziei. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Do głosu zapraszam pana posła Sebastiana Kaletę, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Sebastian Kaleta",
                    "content": "Pani Marszałek! Wysoki Sejmie! Panie Premierze! Pana exposé można streścić jednym zdaniem: będzie można znowu kraść. O tym jest w istocie wasza kampania zemsty, którą pan ogłosił, kampania oparta na sojuszu układu politycznego z układem sędziowskim, Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 747 który sam siebie nazwał kastą. Wszystko pod niemieckim protektoratem poprzez Unię Europejską. Wasza narracja o naruszaniu w Polsce praworządności to żart. Wasza praworządność to doktryna Neumanna, czyli bezkarność dla swoich. Grodzki – immunitet. Nowak, Gawłowski – sędziowie nie kwapią się, żeby ich osądzić. (Głos z sali: Mejza.) A CBA chcecie zlikwidować. Planujecie siłowo, a nie w oparciu o prawo, wprowadzać swoje rządy w instytucjach, które zgodnie z prawem są poza waszą kontrolą, są niezależne. Jeśli wy gdzieś nie rządzicie, to według was nie ma demokracji. Byliście opozycją totalną, teraz taką chcecie być władzą. (Głos z sali: Totalną.) A ten uśmiech, o którym mówicie, w waszym wykonaniu to nie jest uśmiech człowieka uczciwego, szczęśliwego, lecz uśmiech (Dzwonek) rzezimieszka, który z zaciśniętą pięścią naskakuje w ciemnym zaułku na… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie) (Głos z sali: Uważaj, co mówisz.) (Poseł Krystyna Skowrońska: Sam jesteś…)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Do głosu zapraszam panią poseł Katarzynę Czocharę, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Katarzyna Czochara",
                    "content": "Pani Marszałek! Panie Premierze! Wysoka Izbo! Muszę stwierdzić, że w momencie kiedy rozpoczęła się X kadencja Sejmu Rzeczypospolitej Polskiej, poczułam się, jakbym była w programie „Mam talent”… (Poseł Michał Gramatyka: Bardzo śmieszne.) …bo pan marszałek Hołownia niejednokrotnie wykazywał talent do show. I mam nadzieję, że teraz ogląda posiedzenie Sejmu, a nie kręci podcastów. Ale muszę stwierdzić, że pan premier Donald Tusk też ma talent. Słuchałam z uwagą pana wystąpienia i tego, że 16 lat temu było pana pierwsze exposé i wyciągnął pan lekcję. Rzeczywiście wyciągnął pan lekcję i nauczył się pan dobrze, wspaniale grać – grać na emocjach. Gdy pana słuchałam, gdybym panu wierzyła, to wręcz otworzyłabym swoje serce i czekałabym na cud, który nigdy nie nastąpi. (Dzwonek) Ale zacytuję jeszcze może pana manifest. (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) (Poseł Izabela Leszczyna: Następnym razem.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł. Pani poseł, dziękuję bardzo. Do głosu zapraszam panią poseł Józefę Szczurek-Żelazko, Klub Parlamentarny Prawo i Sprawiedliwość. Pani poseł, proszę opuścić mównicę. (Poseł Donald Tusk: To już było, to już było.) (Głos z sali: Czas się pani skończył.) Pani poseł, proszę opuścić mównicę.",
                },
                {
                    "speaker": "Poseł Józefa Szczurek-Żelazko",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Panie Premierze! W swoim exposé mówił pan tak dużo o szacunku do innych, o miłości, o pozytywnych uczuciach. W tym momencie przypomniałam sobie pana wystąpienie, niedawne wystąpienie, kiedy cytował pan fragment wiersza Czesława Miłosza „Który skrzywdziłeś” i powiedział pan wyraźnie, że kieruje pan ten wiersz do prezydenta Rzeczypospolitej Polskiej Andrzeja Dudy. Pozwoli pan, że przytoczę: „Nie bądź bezpieczny./ Poeta pamięta./ Możesz go zabić – narodzi się nowy./ Spisane będą czyny i rozmowy./ Lepszy dla ciebie byłby świt zimowy/ I sznur i gałąź pod ciężarem zgięta”. (Głos z sali: Hańba!) Panie premierze, czy dzisiaj, w przeddzień zaprzysiężenia pana rządu przez pana prezydenta Rzeczypospolitej Polskiej Andrzeja Dudę, powtórzyłby pan ten wiersz i skierowałby pan do niego? Panie premierze, chciałam zadać panu wiele pytań na temat służby zdrowia, bo pan w swoim wystąpieniu nawet nie zająknął się na ten temat (Dzwonek), na ten jakże ważny temat dla Polaków. (Głos z sali: Czas.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł.",
                },
                {
                    "speaker": "Poseł Józefa Szczurek-Żelazko",
                    "content": "Te pytania zadamy panu w późniejszym terminie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Zapraszam do głosu pana posła Jarosława Wiesława Wieczorka, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Jarosław Wiesław Wieczorek",
                    "content": "Szanowna Pani Marszałek! Panie Premierze! Wysoka Izbo! Oczywiście pytań do pana premiera miałbym dziesiątki, jak nie setki, ale czas pozwala mi na zadanie tylko dwóch. Odniosę się do dzisiejszego exposé pana premiera Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 748 Chciałbym zapytać o radę fiskalną, którą pan zapowiedział. Czy nie będzie to wyłącznie przykrywka do niebrania odpowiedzialności za nierealizację, załóżmy, założeń i programów gospodarczych, o których pan powiedział? (Oklaski) (Głos z sali: Brawo!) Jeżeli taka rada fiskalna powie, że nie należy wprowadzać chociażby 60 tys. zł kwoty wolnej od podatku, czy pan mimo to podejmie taką decyzję? To jest pytanie pierwsze. A drugie pytanie dotyczy jednej z wypowiedzi pana posła Siemoniaka odnośnie do naszej obronności i montażu kolejnej linii krabów, armatohaubic. Pan poseł powiedział, że ta druga linia nie ma sensu. Zainwestowaliśmy ogromne środki (Dzwonek), 850 mln zł, w to, żeby właśnie w Gliwicach taka fabryka armatohaubic powstała.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Jarosław Wiesław Wieczorek",
                    "content": "Panie premierze, chcę zapytać o to, czy ma sens obrona naszej niepodległości i naszej suwerenności. Bardzo dziękuję. (Oklaski) (Głos z sali: To ma sens, Siemoniak nie ma sensu.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Zapraszam do głosu pana posła Pawła Jabłońskiego, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Paweł Jabłoński",
                    "content": "Dziękuję, pani marszałek. Patrzę w lewo, w kierunku antycywilizacyjnej lewicy. Pani Scheuring-Wielgus nie ma, uciekli z sali. (Głos z sali: Nie uciekli.) Patrzę prosto na Konfederację. Też ich nie ma. Antycywilizacyjna pseudoprawica. Też uciekli. Pan marszałek Hołownia też uciekł. (Głos z sali: I Jarosław Kaczyński też.) Wy jesteście tacy sami, wam brak odwagi. (Oklaski) I o odwagę właśnie do pana premiera, panie premierze, mam pytanie. (Poseł Donald Tusk: Gdzie jest pan prezes Kaczyński?) Odwaga to jest wartość w polityce. Pan się, panie premierze, obraża o zarzucanie panu, że pan prowadził proniemiecką politykę. (Głos z sali: A gdzie jest pan prezes Kaczyński?) (Poseł Barbara Bartuś: Proszę uciszyć swoich kolegów.) A więc ja chciałbym panu, panie premierze, dać szansę, żeby pan te zarzuty odparł. Czy była choć jedna taka sytuacja, panie premierze, że pan miał odwagę sprzeciwić się Niemcom, sprzeciwić się kanclerzowi Niemiec, tak jak premier Morawiecki w Berlinie, o czym wczoraj mówiłem, który miał odwagę powiedzieć Scholzowi w twarz, że wysyłanie 5 tys. hełmów to jest żart? Jak Niemcy prowadziły prorosyjską politykę (Dzwonek), pan się bał odezwać. Pan mówił, że to błogosławieństwo dla Europy.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle.",
                },
                {
                    "speaker": "Poseł Paweł Jabłoński",
                    "content": "Dlaczego pan się bał? Czemu panu zabrakło odwagi? (Oklaski) (Głos z sali: Zejdź z mównicy.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Do głosu zapraszam pana posła Piotra Polaka, Klub Parlamentarny Prawo i Sprawiedliwość. (Poseł Krystyna Skowrońska: A gdzie prezes?)",
                },
                {
                    "speaker": "Poseł Piotr Polak",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Panie Premierze! W swoim exposé mówił pan, że za 2 dni pan się wybiera do Brukseli na ważne unijne posiedzenie, forum i nie da się pan nikomu ograć z polityków europejskich. Chciałbym zapytać, jakie będzie pana stanowisko, gdy się pan spotka z przywołanym prezydentem Zełenskim czy chociażby z panią przewodniczącą von der Leyen i nacisną na pana, że trzeba złagodzić polskie twarde stanowisko odnośnie do embarga na ukraińskie zboże. I druga sprawa: Czy przekona pan skutecznie, żeby Niemcy zabrali z Polski 35 tys. t śmieci, które nielegalnie do Polski przywieźli, których się wstydzą i których nie chcą z Polski zabrać? (Poseł Adam Szłapka: Które wy sprowadziliście.) (Poseł Izabela Leszczyna: Było nie wpuszczać.) Czekamy na skuteczność w tym wymiarze. I ostatnie pytanie, odnośnie do Jana Pawła II. Wysoka Izbo, pan się wielokrotnie powoływał na nauki, na słowa o miłości, o solidarności – i bardzo dobrze, bo to są piękne słowa, do których się musimy odnosić. Ale są jeszcze słowa Jana Pawła II (Dzwonek) na temat narodu, który zabija własne dzieci…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 749",
                },
                {
                    "speaker": "Poseł Piotr Polak",
                    "content": "…i jest narodem bez przyszłości. Proszę się odnieść do tych słów w kontekście aborcji na życzenie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Zapraszam do głosu pana posła Macieja Małeckiego, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Maciej Małecki",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Szanowni Państwo! Agresja pana posła Brauna rosła wraz z pobłażliwością pana marszałka Hołowni. Gdyby pan marszałek Hołownia reagował od początku na wyskoki posła Brauna wobec pani marszałek Witek, wobec pana premiera Jarosława Kaczyńskiego, wobec pana premiera Mateusza Morawieckiego, to nie doszłoby do tej sytuacji. Zamiast tego mieliśmy heheszki i popisywanie się ripostami. Pytanie do pana premiera Donalda Tuska. Panie premierze, w kampanii wyborczej, żeby zdobyć głosy Polaków, obiecał pan, że cały rok 2024 utrzyma pan ceny gazu na poziomie 2023 r. Co się stało od dnia wyborów, że rakiem wycofaliście się z tej obietnicy i niskie ceny gazu będą tylko do eurowyborów? I jeszcze jedna rzecz: Dlaczego pana rząd (Dzwonek) chciał sprzedać Lotos Rosjanom?",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Maciej Małecki",
                    "content": "Dlaczego wysłaliście zaproszenie do Gazpromu, Rosnieftu, Surgutnieftiegazu i Łukoilu? (Oklaski) (Poseł Izabela Leszczyna: Morawiecki sprzedał.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Do głosu zapraszam pana posła Marka Wesołego, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Marek Wesoły",
                    "content": "Pani Marszałek! Panie Premierze! Wysoka Izbo! Panie premierze, pana exposé to przede wszystkim gra na emocjach, socjotechnika i jednak mimo wszystko mowa nienawiści. Konkretów było mało, raczej z tych konkretów tylko nazwiska, jak to wy mówicie, na obsadzanie stołków. A ja chciałem zapytać, panie premierze, bo wybiera się pan do Brukseli i zapowiedział pan, że przywiezie zablokowane politycznie przez aparat brukselski KPO, a na Śląsku pana koledzy zapowiadali odblokowanie decyzji w sprawie wniosku notyfikacyjnego, jeśli chodzi o pomoc dla wydobycia węgla kamiennego. Chciałem zapytać, czy również ta politycznie zablokowana decyzja będzie przez pana przywieziona, jak rozumiem, w dniu jutrzejszym, bo zapowiedzi były, że w jeden dzień będzie to załatwione. Dziękuję bardzo. (Oklaski) (Głos z sali: 7 mld, PGG. 7 mld.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję. Do głosu zapraszam pana posła Kamila Bortniczuka, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Kamil Bortniczuk",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Najpierw chciałem zwrócić uwagę na ten skandal z udziałem posła Brauna. Sami wypuściliście tego dżina z butelki, obudziliście tego demona, kiedy dawaliście mu powody do satysfakcji z tej trybuny, chcąc upokorzyć panią marszałek Elżbietę Witek. (Głos z sali: Tak było.) Elżbieta Witek umiała trzymać Brauna w ryzach, wy nie potraficie. A jak mówił marszałek Hołownia – co prawda mówił o obrażaniu – upokorzyć też trzeba potrafić. I to upokorzenie obróciło się przeciwko wam, szkoda tylko, że kosztem naszej opinii na arenie międzynarodowej, bo niewątpliwie wywoła to międzynarodowy skandal. (Głos z sali: Takie są skutki waszego działania, lepiej to zrozumcie teraz.) Trzy pytania odnośnie do sportu, panie premierze Donaldzie Tusk. Pierwsze pytanie dotyczące „Sportowych talentów”. To jest pierwszy w historii populacyjny program badania talentów, weryfikowania, identyfikowania sportowych talentów, budowania kultury fizycznej. Czy zobowiąże pan podległych sobie ministrów odpowiednio sportu i edukacji do współpracy i kontynuowania tego programu? W marcu i w kwietniu przyszłego roku po raz pierwszy w historii w każdej polskiej szkole te testy mają być przeprowadzone. Drugie pytanie odnośnie do infrastruktury. Jestem wielkim entuzjastą orlików. Uważam, że to był sukces pańskiego rządu w tamtym czasie. Pan jest źle poinformowany (Dzwonek), bo ja już w ubiegłym roku rozpocząłem program modernizacji orlików. Kilkaset orlików już zostało zmodernizowanych kompleksowo Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 750",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję bardzo, panie pośle.",
                },
                {
                    "speaker": "Poseł Kamil Bortniczuk",
                    "content": "Pani marszałek, kilka sekund dosłownie. Trzecie pytanie to budżet. Nie wiem, czy pan wie, ale dysponujemy dzisiaj czterokrotnie większym budżetem przeznaczonym na sport niż za pana czasów. Czy zobowiąże się pan do tego, żeby na sporcie nie oszczędzać?",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Kamil Bortniczuk",
                    "content": "Pani marszałek, jeszcze jedno pytanie, do pani. (Głos z sali: Już było.) Czy w ramach polityki miłości w tym roku na święta, które się zbliżają, również upiecze pani pierniki z ośmioma gwiazdkami? Bardzo dziękuję. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Wie pan, pierniki to… Rozumiem, że czuje się pan zaproszony, tak? Do głosu zapraszam panią poseł Katarzynę Sójkę, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Katarzyna Sójka",
                    "content": "Dziękuję, pani marszałek. Panie Premierze! Dzisiejsze zdarzenie na górze powinno spotkać się ze zdecydowaną analizą i wyciągnięciem wniosków z tej sytuacji. Wszyscy widzieliśmy, z jaką swobodą pan poseł Braun mógł dokonać tego czynu, bez żadnych przeszkód. Zatrzymać próbowała go pani, która była gościem tej uroczystości i sama została poszkodowana. W ogromnej proszkowej mgle znalazło się wielu dorosłych, ale i dzieci, którzy byli obecni w holu Sejmu. Byli w ogromnym szoku, a proszek tej gaśnicy podrażnił im drogi oddechowe. Cieszę się z deklaracji odpowiedzi pana premiera na każde pytanie, ale okoliczności dzisiejszego skandalu kierują nasze emocje na to oburzające dzisiejsze zachowanie pana posła Brauna. Mam nadzieję, że będzie możliwość, by w spokoju w terminie późniejszym i czasie dłuższym niż minuta zadać wszystkie pytania, które przygotowałam. Ale zadam chociaż jedno. Mówił pan o szacunku. Domyślam się, że zamierza pan wyrazić (Dzwonek) krytykę wobec dzisiejszego skandalu, ale czy również zamierza pan wyrazić krytykę swoich posłów za ich nawoływania na ulicach, na samochodach, do nienawiści, używanie pedagogiki ośmiu gwiazdek i stosunku do wyborców PiS.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł.",
                },
                {
                    "speaker": "Poseł Katarzyna Sójka",
                    "content": "Ale jeszcze tylko jedno zdanie, bardzo proszę. (Głosy z sali: Nie.) (Głos z sali: Wystarczy, naprawdę.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pani poseł, ma pani przedłużony czas o 20 sekund. Dziękuję bardzo, pani poseł.",
                },
                {
                    "speaker": "Poseł Katarzyna Sójka",
                    "content": "W waszym programie, drodzy państwo, w pkt 10, zacytuję: zapewnimy prawo do bezpłatnego znieczulenia przy porodzie… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Zapraszam na mównicę pana posła Andrzeja Śliwkę, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Andrzej Śliwka",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Zanim kilka pytań, trzeba się odnieść do tego, co miało miejsce w polskim Sejmie. Wszyscy potępiamy zachowanie pana posła Brauna, potępili je nawet politycy Konfederacji, ale musimy pamiętać, kto odpowiada za porządek i bezpieczeństwo w Sejmie. Jest to marszałek Sejmu. Pan marszałek Hołownia musi pamiętać, że bycie marszałkiem to nie tylko apanaże, to nie tylko lajki, to nie tylko udostępnienia, to nie tylko złote, srebrne przyciski, ale także odpowiedzialność. Szkoda, że o tym zapomniał i czmychnął z posiedzenia, bo nie chce słuchać tego, co mają do powiedzenia posłowie.… (Głos z sali: Gdzie jest Jarosław?) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 751 Panie Premierze! Trzy pytania. Chciałbym spytać, czy pomimo pana niechęci do rozbudowy polskich portów oraz sceptycyzmu związanego z inwestycją przekopu Mierzei Wiślanej (Dzwonek) oraz także z tym, że samorząd Elbląga jest przeciwnikiem rozbudowy portu morskiego, czy pan premier…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle. (Głos z sali: Czas.) (Głos z sali: Panie pośle.) (Głosy z sali: Koniec.)",
                },
                {
                    "speaker": "Poseł Andrzej Śliwka",
                    "content": "…jest zainteresowany, żeby w Elblągu powstał czwarty port Rzeczypospolitej…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle.",
                },
                {
                    "speaker": "Poseł Andrzej Śliwka",
                    "content": "…o podstawowym znaczeniu dla gospodarki narodowej. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Panie pośle, dziękujemy. Do głosu zapraszam posła Ryszarda Bartosika, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Ryszard Bartosik",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Jeszcze wczoraj głośno krzyczeliście, że to jest koniec rządów PiS, a dziś pokazaliśmy, jak wy zaczynacie swoje rządy. Skandal na cały świat. (Wypowiedź poza mikrofonem) Szanowni Państwo! Skandal na cały świat, pani poseł. Tak zaczynacie swoje rządy. Premier Tusk mówił o Koninie i konińskich górnikach. Panie Premierze! To pan sprzedał konińskie kopalnie, kopalnię Adamów i kopalnię Konin, a dziś pan chce udzielać im pomocy. W związku z tym chciałem zapytać, czy będzie realizowana budowa elektrowni atomowej przez stworzoną spółkę, przez PGE i ZE PAK, która jest tak potrzebna naszemu krajowi i naszemu konińskiemu regionowi. Druga sprawa. Chciałbym zapytać, czy będzie pan realizował ustawę: lokalna spółka, tak potrzebną naszym rolnikom (Dzwonek) i 12 postulatów złożonych przez związki zawodowe rolników. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Głos zabierze, zapraszam, pan poseł Henryk Kowalczyk, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Henryk Kowalczyk",
                    "content": "Dziękuję bardzo. Pani Marszałek! Wysoka Izbo! Panie Premierze! Nawet byłbym w stanie uwierzyć w te pańskie zapewnienia dotyczące zgody narodowej, gdyby nie wstęp i porównanie 15 października do sierpnia 1980 r., do 1989 r. Chyba w innej rzeczywistości wtedy żyliśmy. Teraz odbyły się demokratyczne wybory, demokratyczne dzięki Prawu i Sprawiedliwości. (Głos z sali: Ha, ha, ha!) Ale podziękował pan również Komitetowi Obrony Demokracji, który fizycznie atakował posłów Prawa i Sprawiedliwości, który przygotował pucz uliczny. To jest tak naprawdę dzielenie Polaków, sianie nienawiści, zachęcanie do przestępstw. Więc jak mamy teraz rozumieć pańskie słowa o zgodzie narodowej równocześnie z podziękowaniem w tym kierunku? Drugi element. Napłynęło mnóstwo kłamstw dotyczących rządowego funduszu inwestycji strategicznych. Ale przypomnę, że jesienią 2021 r. (Dzwonek) 97% samorządów otrzymało dotacje z funduszu inwestycji.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle.",
                },
                {
                    "speaker": "Poseł Henryk Kowalczyk",
                    "content": "Czyżby Prawo i Sprawiedliwość miało 97% wójtów i burmistrzów? (Poseł Michał Kołodziejczak: Niech pan nam powie, co ze zbożem.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy. Dziękujemy, panie pośle.",
                },
                {
                    "speaker": "Poseł Henryk Kowalczyk",
                    "content": "A więc pytanie: Czy fundusz inwestycji zostanie zachowany w tej formie, w jakiej jest? (Oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 752",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze poseł Jacek Ozdoba, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Jacek Ozdoba",
                    "content": "Szanowna Pani Marszałek! Szanowny Panie Premierze! Kibic Lechii Gdańsk do legionisty: Żyleto? No daj pan spokój, naprawdę, więc jakby… (Oklaski) Ale tak całkiem serio. Panie Premierze! Rzecz jest jakby dla pana na pewno trudna, współczuję panu roli, bo za pana plecami siedzą ludzie, którzy podpisują się pod aktem barbarzyństwa wobec chrześcijan, wobec krzyża. Tak jak aktem barbarzyństwa jest atak na Chanukę, to, co zrobił Braun, tak samo aktem barbarzyństwa jest próba zdjęcia tego krzyża. A pan dalej buduje środowisko polityczne w takim nurcie. Nie bez przyczyny pan wziął na sztandary te osiem gwiazdek. Naprawdę ma pan zadanie, nawet widzę, że pan zastanawia się, co zrobić, albo to jest taki cyniczny poker face, który pan stosuje, ale to, co tolerujecie wobec chrześcijan, np. na posiedzeniu Rady Miasta Stołecznego Warszawy, wobec katolików, gdzie facet w durszlaku na głowie jest akceptowany, podczas kiedy katolicy chcą uszanować swoje święto… Należy szanować każdą religię, więc liczę na to, że pana środowisko polityczne (Dzwonek) poprze ustawę w obronie chrześcijan, bo to jest nasz obowiązek. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze pan poseł Arkadiusz Mularczyk, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Arkadiusz Mularczyk",
                    "content": "Bardzo dziękuję. Pani Marszałek! Panie Premierze! Wysoka Izbo! Panie premierze, 1 września ub.r. został opublikowany raport o stratach wojennych zadanych przez Niemcy Polsce w wyniku II wojny światowej. Straty w tym raporcie zostały wyliczone na 6220 mld zł. W wyniku tej decyzji i tego raportu 14 września ub.r. Sejm Rzeczypospolitej Polskiej podjął uchwałę w sprawie dochodzenia przez Polskę zadośćuczynienia za szkody spowodowane przez Niemcy w czasie II wojny światowej. Przypomnę, że Sejm Rzeczypospolitej Polskiej wezwał rząd Republiki Federalnej Niemiec do przyjęcia odpowiedzialności finansowej, historycznej, politycznej i prawnej za wszystkie skutki wywołane wynikiem II wojny światowej. W wyniku również inicjatywy Platformy Obywatelskiej wprowadzono zapis dotyczący szacowania strat zadanych przez Związek Sowiecki w czasie II wojny światowej. Panie Premierze! Mam do pana pytanie: Czy pan premier w tej kolejnej kadencji Sejmu będzie kontynuował prace dotyczące (Dzwonek) dochodzenia od Niemiec reparacji wojennych i szacowania strat wojennych zadanych przez władzę sowiecką w Polsce? Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle. Głos zabierze poseł Marek Suski, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marek Suski",
                    "content": "Pani Marszałek! Wysoka Izbo! Ja mam tutaj konstytucję… (Głos z sali: Szkoda, że dopiero teraz.) (Głos z sali: Nieużywana.) …na którą tak często się powołujecie. I w tej konstytucji w art. 54 czytamy: „Każdemu zapewnia się wolność wyrażania swoich poglądów oraz pozyskiwania i rozpowszechniania informacji”. W pkt 2: „Cenzura prewencyjna środków społecznego przekazu oraz koncesjonowanie prasy są zakazane”. (Głos z sali: Nie broń…) A pan zapowiada napad na media publiczne po to, żeby Polacy nie mieli dostępu do informacji. To jest wprost zapowiedź łamania konstytucji, na którą tak chętnie się powołujecie. Ale również pan mówił o dbałości o polską gospodarkę i przedsiębiorców. To ja mam pytanie: Jak pan rządził, to jak pan zadbał o stoczniowców, likwidując stocznie? (Poseł Izabela Leszczyna: Jaworski sprzedał stocznie.) A później pana kolega z Platformy organizował dla stoczniowców za publiczne pieniądze kursy dla psich fryzjerów. Wtedy były samobójstwa, bo ludzie nie mieli z czego żyć (Dzwonek), a pan dzisiaj powołuje się na list samobójcy, krytykując Prawo i Sprawiedliwość. (Oklaski) Hańba! (Poseł Krystyna Skowrońska: To Jaworski.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Głos zabierze pani poseł Elżbieta Duda, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Elżbieta Duda",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Pana przemówienie to jak ładnie zapakowany prePrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 753 zent. Nie wiemy, co jest w środku, więc poczekamy, jak zostanie rozpakowany. Jest przejawem socjotechniki – wyłącznie. Ani słowa o programie. Nie usłyszałam konkretów. Były cytaty wielkich autorytetów, ale proszę pamiętać, że własny autorytet szlifuje się własnymi czynami. Pamiętam czas, kiedy kapitał z Polski był wyprowadzany, było opuszczanie Polski za poszukiwaniem pracy, za poszukiwaniem chleba. O inwestycjach na skalę światową mogliśmy tylko pomarzyć. Pytam z troski o Polskę. Pragnę zapytać i proszę o szczerą odpowiedź: Czy budowa Centralnego Portu Komunikacyjnego będzie kontynuowana? Czy jest pan zwolennikiem budowy wspólnoty Trójmorza? Jeśli tak, to proszę przedstawić plan działania. (Dzwonek) Proszę również o szczerą odpowiedź również na pytanie: Dlaczego chce pan zlikwidować IPN i CBA?",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł.",
                },
                {
                    "speaker": "Poseł Elżbieta Duda",
                    "content": "Pytają mnie również przedsiębiorcy…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł.",
                },
                {
                    "speaker": "Poseł Elżbieta Duda",
                    "content": "…jakie pozytywne zmiany obejmą…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pani poseł, bardzo dziekuję.",
                },
                {
                    "speaker": "Poseł Elżbieta Duda",
                    "content": "…małe i średnie przedsiębiorstwa. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze poseł Łukasz Schreiber, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Łukasz Schreiber",
                    "content": "Pani Marszałek! Wysoka Izbo! Rzygać się chce. (Głos z sali: Ojej.) (Głos z sali: Panie pośle…) Seryjni zabójcy kobiet. Jedna z najbardziej opresyjnych dyktatur. Prezes ma pełne gacie referendum. To nie są słowa jakiegoś menela. (Poseł Antoni Macierewicz: Słusznie zareagowaliście.) To nie są słowa trolla internetowego, to nie są nawet słowa szeregowego działacza Platformy. To słowa człowieka, którego państwo chcecie wynieść do najwyższych godności w państwie – na fotel prezesa Rady Ministrów. I stąd pierwsze moje pytanie: Czy nie jest panu tak po ludzku wstyd za te słowa? (Głos z sali: Jest bezwstydny.) Druga sprawa. Widzi pan, jakie to przewrotne. Atakował pan Prawo i Sprawiedliwość, oskarżaliście nas o wszystko i o wszystkich, o każdą drobnostkę i o ogólnoświatową inflację, a tymczasem co się dzisiaj okazało? Że nie potraficie wziąć odpowiedzialności za to, co się dzieje w tej Izbie. Opowiadał pan nam tutaj bajki o wzmocnieniu roli Polski w Unii Europejskiej, w NATO, a ograł was (Dzwonek) Braun na własnym podwórku, a przy okazji niestety ośmieszył Polskę. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze poseł Kazimierz Bogusław Choma, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Kazimierz Bogusław Choma",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Kandydacie na Premiera! 20 maja 2013 r. – premierem był pan Donald Tusk, ministrem skarbu Włodzimierz Karpiński. Sprzedano FŁT-Kraśnik w ręce inwestora chińskiego, według Agencji Reuters za 300 mln zł, gdy przychód w poprzednim roku był na poziomie 265 mln, zysk – 2,6 mln zł, a zatrudnienie na poziomie 2 tys. osób. Ta prywatyzacja miała pomóc w rozwoju fabryki. Obecnie fabryka zatrudnia 1181 osób, zapowiadane są następne zwolnienia. Proszę o odpowiedź na pytanie: W jaki sposób jako premier chce pan naprawić swój błąd? Tak aby ludzie (Dzwonek), w części pańscy wyborcy, nie byli wyrzucani na bruk i mogli utrzymać swoje rodziny. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze poseł Witold Wojciech Czarnecki, Klub Parlamentarny Prawo i Sprawiedliwość Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 754",
                },
                {
                    "speaker": "Poseł Witold Wojciech Czarnecki",
                    "content": "Pani Marszałek! Wysoka Izbo! Czy uważa pan, panie premierze, że wykorzystywanie exposé do składania podziękowań aktywistom politycznym, którzy wprowadzili do debaty publicznej wulgarny język nienawiści, jest odpowiednią i etyczną praktyką w polityce? Mówi pan o potrzebie prowadzenia polityki miłości, ale nie zauważa pan nienawiści i pogardy wypływającej z własnego środowiska. Nie chcę powtarzać wulgaryzmów, jednego użyłem dzisiaj w oryginale podczas pańskiego exposé. Nie chcę przypominać, co oznacza osiem liter czy co znaczy 11 gwiazdek, których pańscy koledzy używają z uśmiechem na ustach. Panie Premierze! Czy mówienie o odbudowywaniu wspólnoty narodowej przy jednoczesnym tolerowaniu, a nawet afirmacji języka nienawiści oraz dehumanizacji przeciwników politycznych (Dzwonek) to nie jest hipokryzja? Czy pan tego nie zauważa, tej rażącej sprzeczności? Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze poseł Waldemar Buda, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Waldemar Buda",
                    "content": "Pani Marszałek! Wysoka Izbo! Dzisiaj zamiast marszałka mamy króla heheszków. Widzimy tego pierwsze efekty. Kiedą są żarciki, wszyscy się śmieją, jest wspaniale, wesoło, jest klikalność, jest oglądalność, ale kiedy dochodzi do poważnej sytuacji, nie ma kto za nią wziąć odpowiedzialności. Oczywiście pan marszałek Hołownia nie upilnuje tutaj każdego, nie każdego złapie tutaj za rękę, ale ponosi on polityczną odpowiedzialność za to, co dzieje się w tej Izbie, w tym budynku. To nie jest chłopiec w krótkich spodenkach, to jest marszałek Sejmu. (Poseł Izabela Leszczyna: A ty za mieszkania…) Panie Premierze! Chciałem zapytać o politykę mieszkaniową, ponieważ przekazałem panu 100 konkretów z lekką nadzieją, że jednak pan się z nimi zapozna, że jednak odniesie się pan jakoś do tych 100 konkretów, o których pan mówił w kampanii wyborczej. O polityce mieszkaniowej było niewiele, przepraszam, nie było nic… (Głos z sali: Wyście zbudowali…) …stąd moje proste pytanie: Czy bezpieczny kredyt 2% będzie kontynuowany? Czy może będzie to 0% lub 1,5 %, jak przedstawiał to koalicyjny PSL? (Dzwonek) W każdym razie taki program jest potrzebny, więc proszę odpowiedzieć na to pytanie. Dziękuję bardzo. (Oklaski) (Głos z sali: A zbudowaliście te mieszkania?) (Poseł Krystyna Skowrońska: Mieszkanie+ poproszę.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze pani poseł Dominika Chorosińska, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Dominika Chorosińska",
                    "content": "Pani Marszałek! Wysoka Izbo! Przez ostatnie 8 lat Prawo i Sprawiedliwość prowadziło bardzo ambitną politykę kulturalną w naszym kraju, za co chciałabym z tego miejsca bardzo podziękować panu ministrowi Glińskiemu. Wysoko postawił poprzeczkę. (Oklaski) Z pana exposé nie dowiedzieliśmy się niczego na temat polityki kulturalnej. Kultura to również ludzie. W ich imieniu pytam pana premiera Donalda Tuska, czy zamierza pan odebrać artystom 50-procentowy uzysk, tak jak pan to zrobił za czasów poprzednich pana rządów. Przypomnę tylko, że Prawo i Sprawiedliwość przywróciło artystom ten przywilej. Panie Premierze! Mam drugie pytanie. Czy nie odczuwa pan pewnego dysonansu poznawczego, cytując Jana Pawła II – słusznie, bo to wielki Polak – a jednocześnie obsadzając w roli ministra czy wiceministra kogoś, kto mówi o (Dzwonek) piłowaniu katolików? Chodzi też o panią minister, która mówiła, że Polskę trzeba odjaniepawlić i atakowała Jana Pawła II. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy bardzo, pani poseł. Głos zabierze poseł Jan Krzysztof Ardanowski, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Jan Krzysztof Ardanowski",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Premierze! Moje pytania miały oscylować wokół bezpieczeństwa żywnościowego, czyli jednego z najważniejszych elementów bezpieczeństwa każdego państwa, w kontekście nielogicznej i coraz bardziej antyrolnicznej polityki Unii Europejskiej, ale może będzie okazja podyskutować kiedyś na ten temat, zresztą będę w tej sprawie rozmawiał z panem ministrem Siekierskim. Chcę jednak skoncentrować się na tym haniebnym akcie, który miał dzisiaj miejsce w wykonaniu posła Brauna. Mówię to jako wieloletni członek, a przez jakiś czas przewodniczący, polsko-izraelskiej grupy parlamentarnej. Ten karygodny atak Brauna może być wykorzystany w mediach globalnych przeciwko Polsce przez nieżyczliwe nam środowiska jako przykład antysemityzmu polskiego parlamentu. (Głos z sali: Już jest.) (Głos z sali: Tak jest.) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 755 Nie wolno do tego dopuścić, ale w tym kontekście trzeba również (Dzwonek) wziąć pod uwagę, nie tylko dlatego, że dotyczy to starszych braci w wierze, że wszelkie ataki na swobody religijne, na prawo wyznawania swoich wartości muszą być potępione. Bardzo proszę, żeby pan, żeby pana środowisko polityczne również wyciągnęło wnioski z tego haniebnego czynu, który…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Jan Krzysztof Ardanowski",
                    "content": "…został dokonany przez Brauna, żeby nigdy nie było zamachu również na inne religie w Polsce, w tym na religię katolicką. (Oklaski) (Poseł Antoni Macierewicz: A robicie to ciągle.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Głos zabierze pani poseł Agnieszka Anna Soin, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Agnieszka Anna Soin",
                    "content": "Pani Marszałek! Wysoka Izbo! Jestem zawiedziona exposé wygłoszonym przez nowego premiera Donalda Tuska. Polacy liczyli na konkrety, których niestety nie usłyszeli.",
                },
                {
                    "speaker": "Panie Premierze! W swoim exposé powiedział pan",
                    "content": "Polska może być lepsza. Chcę zapytać, w jaki sposób pan to dostrzega. Czy chodzi o powrót do bezrobocia, osłabienie militarne naszego kraju, dzielenie Polski na Polskę A i Polskę B, ponowne stworzenie eldorado dla mafii paliwowych? Wspomniał pan o szacunku, o demokracji, o niepodległości. Czy może nam pan obiecać, że zachowamy swoją niepodległość i nie pozwoli pan na federalizację? Czy pana ugrupowanie nadal sądzi, że programy społeczne jak 500+, 800+ to rozdawnictwo? W swoim exposé użył pan słowa: gwałt. Proszę mi uwierzyć, że (Dzwonek) wiele kobiet tak się poczuło, kiedy pana rząd podniósł im wiek emerytalny.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł.",
                },
                {
                    "speaker": "Poseł Agnieszka Anna Soin",
                    "content": "Czy zagwarantuje pan, że tym razem polskie kobiety będą mogły czuć się bezpiecznie? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, pani poseł. Głos zabierze poseł Władysław Kurowski, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Władysław Kurowski",
                    "content": "Pani Marszałek! Wysoki Sejmie! Panie Premierze! W pana exposé miało być wiele konkretów. Niestety doczekaliśmy się kilku. Było wiele emocji, była piękna socjotechnika, natomiast zabrakło temu exposé wiarygodności. Chciałbym odnieść się do tego fragmentu pana exposé, w którym przytaczał pan słowa św. Jana Pawła II o solidarności. Faktycznie św. Jan Paweł II mówił dużo o solidarności międzyludzkiej, ale mówił też o wielu sferach życia społecznego, o roli rodziny w życiu społecznym, o małżeństwie jako o związku kobiety i mężczyzny, o roli mamy i taty w wychowaniu dzieci i w rodzinie. Mówił tez bardzo dużo o życiu, o wartości życia, o ochronie życia od poczęcia (Dzwonek) do śmierci. Mam do pana pytanie: Czy w związku z tym coś zmieniło się w pana podejściu do ochrony życia od poczęcia aż do śmierci? Pytam o to ze względu na tzw. prawo kobiety…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Władysław Kurowski",
                    "content": "…nazwane tak przez was, prawo dotyczące aborcji do 12 tygodnia życia.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Głos zabierze…",
                },
                {
                    "speaker": "Poseł Władysław Kurowski",
                    "content": "I czy będzie pan też dążył do legalizacji… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 756",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze poseł Patryk Wicher, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Patryk Wicher",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Panie Premierze Elekcie! Apeluję: zatrzymajcie się. Próbowaliście zniszczyć autorytety, polskie autorytety – Jan Paweł II Wielki – ataki na niego, podważyć autorytet Kościoła, zniszczyć wszystko, każdy autorytet, na bazie którego budowaliśmy naszą godność narodową. (Poseł Antoni Macierewicz: Dokładnie tak.) Zatrzymajcie się. Nie tańczcie nad grobami zmarłych. Niech nie będzie tego tańca śmierci, danse macabre, bo wszyscy jesteśmy względem śmierci równi, panie premierze. Opamiętajcie się. Nie niszczcie korzeni naszego narodu. Szanujcie drugiego człowieka. Nie wykorzystujcie nieszczęścia drugiego człowieka. Czy wam nie wstyd? Serduszka na waszych klapach to miłość ponoć, miłość do drugiego człowieka, panie premierze. A jeden z waszych posłów, pan poseł Sowa, ułożył litanię do drzewa, o które rozbiła się pani premier Szydło, bo taki jest cwany i brak mu szacunku nawet do kobiety. (Dzwonek) A więc ułożę jedną zwrotkę.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Patryk Wicher",
                    "content": "O, święte drzewo, oświeć was, żebyście znaleźli krztę… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Do głosu zapraszam panią poseł Dorotę Arciszewską-Mielewicz… (Poseł Dorota Arciszewska-Mielewczyk: Mielewczyk.) Mielewczyk, przepraszam, pani poseł, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Dorota Arciszewska-Mielewczyk",
                    "content": "Pani Marszałek! Wysoki Sejmie! W latach 90. dotkliwym ciosem dla Polskich Linii Oceanicznych armatora z 73 latami historii, jednego z największych armatorów w Europie i na świecie, była przyspieszona i źle przeprowadzona komercjalizacja. W efekcie wiele spółek grupy PLO zbankrutowało. Na lepsze sytuacja zmieniła się dopiero za rządów Prawa i Sprawiedliwości. W miejsce wycofanych, wyeksploatowanych statków kupiono nowoczesne większe jednostki – dzięki wsparciu rządu pana Morawieckiego i Agencji Rozwoju Przemysłu. Były to pierwsze zakupy w po 30 latach. Pana rząd sprzedał 960 spółek, nie widząc dla nich przyszłości, kontynuując politykę pana Lewandowskiego, który zasłynął jako prywatyzator III Rzeczypospolitej i wysprzedawał wszystkie dobra narodowe, członka waszej partii. Czy zamierza pan kontynuować proces rozwoju floty, która stanowi bardzo ważny element niezależności, bezpieczeństwa Polski, pełni w bilansie płatniczych kraju funkcję antyimportową (Dzwonek) i proeksportową, a także strategiczną? Panie premierze, na Kaszubach mówi się: My trzymamy z Bogiem. Nie wystarczy budować ołtarzyki, brać ślub kościelny…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, pani poseł.",
                },
                {
                    "speaker": "Poseł Dorota Arciszewska-Mielewczyk",
                    "content": "…tylko trzeba naprawdę z tym Bogiem trzymać i… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, pani poseł. Do głosu zapraszam pana posła Fryderyka Sylwestra Kapinosa, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Fryderyk Sylwester Kapinos",
                    "content": "Szanowna Pani Marszałek! Wysoki Sejmie! W ogólnokrajowym referendum w dniu 15 października br. ponad 10,8 mln osób opowiedziało się przeciw wyprzedaży majątku państwowego podmiotom zagranicznym. Ponad 10,6 mln osób opowiedziało się przeciw podniesieniu wieku emerytalnego, w tym przywrócenia podwyższonego do 67 lat wieku emerytalnego dla kobiet i mężczyzn. Ponad 10,8 mln osób opowiedziało się przeciw likwidacji bariery na granicy Rzeczypospolitej Polskiej z Republiką Białorusi. Ponad 10,8 mln osób opowiedziało się przeciw przyjęciu tysięcy nielegalnych imigrantów z Bliskiego Wschodu i Afryki zgodnie z przymusowym mechanizmem relokacji narzucanym przez biurokracje europejskie Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 757 Moje pytanie brzmi: Czy Donald Tusk jako prezes Rady Ministrów weźmie pod uwagę głos blisko 11 mln Polaków w kreowanej przez siebie polityce i polityce swego rządu? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze pani poseł Anna Kwiecień, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Anna Kwiecień",
                    "content": "Pani Marszałek! Wysoka Izbo! W roku 2021 odbył się spis powszechny. I w ramach tego spisu w rubryce wyznanie 27 mln Polaków zadeklarowało, że są katolikami – 27 mln. To trochę więcej niż 11 mln, niż nawet 8 mln wspólnie. W tym samym roku odbył się Campus Polska, na którym za chwilę pan minister sportu przedstawił pierwszy raz program dla tych 27 mln Polaków – opiłowywanie katolików. Opiłowywanie. Tak, panie premierze. (Poseł Antoni Macierewicz: Może tego nie było, może to nieprawda.) Ja mówię to, żeby pan się zastanowił. Bo przecież pan też deklaruje wiarę katolicką. Pan robił sobie zdjęcia, ołtarzyk, cała rodzina, wszyscy to widzieliśmy. (Dzwonek) Ta nienawiść kiedyś może wrócić do pana. (Poseł Antoni Macierewicz: Ale chcecie katolików opiłować.) Już dzisiaj widzimy, co się dzieje, jak ktoś lekceważy jakiekolwiek symbole religijne.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, pani poseł. Pani poseł, dziękujemy bardzo.",
                },
                {
                    "speaker": "Poseł Anna Kwiecień",
                    "content": "Ja tak samo proszę pana: opamiętajcie się.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, pani poseł.",
                },
                {
                    "speaker": "Poseł Anna Kwiecień",
                    "content": "A miałam dzisiaj panu tutaj zadać pytanie o prywatyzację… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Pani poseł, czas minął. (Głos z sali: Czas się skończył.) Do głosu zapraszam pana posła Roberta Gontarza, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Robert Gontarz",
                    "content": "Szanowna Pani Marszałek! Panie Premierze! Wysoka Izbo! Chyba wszyscy potępiamy to dzisiejsze wydarzenie, które miało miejsce w Sejmie, polegające na przerwaniu uroczystości religijnych. Co do tego, myślę, nie ma wątpliwości. Niemniej jednak kiedy w tekście mówiącym o tym, że wszyscy potępiamy obrażanie uczuć religijnych, pojawia się słowo: katolików, nagle zapada pewna kurtyna hipokryzji. Wtedy znaczna część tej sali przestaje to dostrzegać. Zaczyna mówić, że to jest wyrażanie własnych uczuć, swoich emocji, i przestaje zauważać, że obrażanie uczuć religijnych katolików to jest coś bardzo złego. Panie premierze, dziś pan powiedział, że odpowie na każde pytanie. Obiecał pan i mam nadzieję, że choć w tym wypadku dotrzyma pan słowa i odpowie na to pytanie: Czy w pana rządzie znajdą się osoby, które atakowały katolików? Czy w pana rządzie znajdą się ludzie, którzy przerywali bądź które przerywały uroczystości religijne, msze święte? Panie Premierze! To jest bardzo proste pytanie i proszę tu nie lać wody, tylko konkretnie (Dzwonek) odpowiedzieć: tak, w moim rządzie znajdą się osoby, które obrażają katolików, bądź: nie, nie znajdą się takie osoby.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy panu posłowi.",
                },
                {
                    "speaker": "Poseł Robert Gontarz",
                    "content": "Bo to ma fundamentalne znaczenie dla kilkudziesięciu milionów Polaków. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy panu posłowi. Głos zabierze poseł Marek Matuszewski, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marek Matuszewski",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Czy jest pan katolikiem? (Głos z sali: Co to za pytanie? Wstydu nie masz?) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 758 Czy jest pan katolikiem praktykującym? Jest pan? Aha, jest pan. To dlaczego nie broni pan wartości chrześcijańskich? (Oklaski) Jak krzyczą: dym w kościołach, na manifestacjach – tak było w 2020 r. – to dlaczego pan później z jedną z tych osób, organizatorką spotyka się? (Głos z sali: Popiera ją.) Nie wiem, czy to są wartości. Panie Premierze! W małych gminach, miasteczkach dzieci, młodzież, dorośli uprawiają sport na pięknych nowych boiskach, w halach sportowych, w salach gimnastycznych, na stadionach lekkoatletycznych, lodowiskach, które zostały wybudowane przez samorządy dzięki miliardom złotych dotacji na sport, przez rząd Prawa i Sprawiedliwości. Czy będzie dalej tak, panie premierze? Czy wy też będziecie budować? Bo samorządowcy bardzo się martwią. (Dzwonek)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle.",
                },
                {
                    "speaker": "Poseł Marek Matuszewski",
                    "content": "I na koniec, Wysoka Izbo: zrobiliśmy bardzo dużo, wrócimy jeszcze silniejsi. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze poseł Zbigniew Hoffmann, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Zbigniew Hoffmann",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Panie Premierze! Chciałem do pana skierować pytanie z dziedziny mi bardzo bliskiej – bezpieczeństwa publicznego, ale niestety po tym, co się dzisiaj wydarzyło, jestem zmuszony skierować krótki apel do pana marszałka Hołowni. Panie Marszałku! To jest wielka odpowiedzialność bycie marszałkiem polskiego Sejmu, Sejmu Rzeczypospolitej. To jest odpowiedzialność przed Polakami, to jest odpowiedzialność przed polskim państwem. Sytuacja dojrzała do tego, żeby pan zmienił sposób zarządzania Sejmem, bo inaczej może tu naprawdę wydarzyć się jakaś straszliwa tragedia, a tego przecież nikt na tej sali nie chce. Tak że, panie marszałku, jeżeli pan tego sposobu nie potrafi zmienić, proszę się podać natychmiast do dymisji. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Głos zabierze pan poseł Andrzej Kryj, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Andrzej Kryj",
                    "content": "Szanowna Pani Marszałek! Wysoka Izbo! Panie Premierze! Ostrowiec Świętokrzyski, Opatów, Sandomierz, Bałtów, Bodzechów, Ćmielów, Kunów, Waśniów, powiat ostrowiecki, Baćkowice, Ożarów, Wojciechowice, powiat opatowski, Łoniów, Wilczyce, Obrazów, Samborzec czy powiat sandomierski. To tylko kilkanaście samorządów spośród samorządów województwa świętokrzyskiego, które w ostatnich latach dzięki środkom skierowanym do nich przez rząd pana premiera Mateusza Morawieckiego otrzymały potężny impuls rozwojowy. W tych samorządach rządzą w większości włodarze niezwiązani z Prawem i Sprawiedliwości. Co więcej, część z nich to reprezentanci tzw. anty-PiS-u. Pomimo to, wbrew temu, co mówili niektórzy przedstawiciele sejmowej większości, obficie korzystali oni ze środków rządowych, nazywając je często eufemistycznie środkami zewnętrznymi. Dziś wielu z tych samorządowców zadaje sobie pytanie, czy nadal takie środki będą kierowane do nich z budżetu centralnego. Dlatego chciałbym prosić pana premiera (Dzwonek) o wyjaśnienie, czy i jak pana rząd zamierza wspierać polskie samorządy…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Andrzej Kryj",
                    "content": "…szczególnie te najsłabsze i najmniejsze. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Głos zabierze pani poseł Marzena Anna Machałek, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marzena Anna Machałek",
                    "content": "Pani Marszałek! Wysoka Izbo! Dzisiaj rzeczywiście poruszające wydarzenia w Sejmie. Poruszające, bo trudno się z nimi zgodzić. Dołączam się do wszystkich, którzy potępili zachowanie posła Brauna, ale dołączam się też do tych, którzy twierdzą i uważają, że to jest sposób prowadzenia – dodaję – ciągle 1. posiedzenia Sejmu. Wielka oglądalność, dzisiaj będzie jeszcze większa, ale ze smutkiem stwierdzam, że chyba nie o to chodziło Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 759 Szanowni Państwo! Chcę się odnieść też do tego exposé. Jest to bulwersujące, że wykorzystano w nim słowa osoby, która w tragiczny sposób zakończyła swoje życie. Zachowania suicydalne wśród młodzieży, o których dzisiaj mówiono, są rzeczywiście problemem. Wynikają ze zmian cywilizacyjnych. (Dzwonek) Prawo i Sprawiedliwość prowadziło ambitną politykę. Stworzyliśmy dodatkowo prawie 100% więcej miejsc dla specjalistów w szkołach i przedszkolach.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł.",
                },
                {"speaker": "Poseł Marzena Anna Machałek", "content": ""},
                {
                    "speaker": "I do pana, panie premierze, powinno być pytanie",
                    "content": "Czy pan wie, co to jest efekt Wertera i czy można upowszechniać… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) (Głos z sali: Nieładnie, pani marszałek.) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł. Głos zabierze pan poseł Dariusz Piontkowski, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Dariusz Piontkowski",
                    "content": "Panie Premierze! Spodziewaliśmy się dzisiaj konkretów. Zamiast tego znowu próbował pan manipulować nie tylko tą salą, ale też wszystkimi Polakami, przedstawiając taką wizję świata, jaką pan chciał, żeby Polacy wierzyli, że pan ma, albo żeby postrzegali to tak, jak pan to próbował dziś przedstawić. Zabrakło informacji o tym, co pan zrobi chociażby z migrantami, a mieszkańcy Podlasia, mojego Podlasia, pytają, czy zachowa pan zaporę na granicy, czy pozwoli pan Straży Granicznej i innym formacjom mundurowym bronić Polaków przed napływem nielegalnych migrantów. Mieszkańcy mojego regionu pytają również, czy nie zrobi pan tak jak przed Euro 2012, gdy zabrał pan kilka miliardów złotych na budowę trasy S8 łączącej Warszawę z Białymstokiem, a tym razem nie odbierze pan tych pieniędzy z budowy chociażby Via Carpatia i odbierze pan możliwość podróżowania wzdłuż wschodniej granicy Polski i rozwoju tych regionów. Jeden element, o którym pan wspomniał, to podwyżki dla nauczycieli. Zapomniał pan jednak powiedzieć o tym, że w budżecie przygotowanym przez Prawo i Sprawiedliwość na rok 2024 oferujemy (Dzwonek) już kilkanaście procent… (Głos z sali: 12.) …wzrostu wynagrodzenia. Gdyby pan był uczciwy, powiedziałby pan, że…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Dariusz Piontkowski",
                    "content": "…chcemy dodać dodatkowo kilkanaście procent. Skąd pan weźmie te 14 mld zł? Bo tyle to będzie kosztowało. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Bardzo dziękuję, panie pośle. Głos zabierze pan poseł Tadeusz Woźniak, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Tadeusz Woźniak",
                    "content": "Wysoki Sejmie! Panie Premierze! Przez wiele lat zagraniczni politycy wspierali pana w walce z legalnie funkcjonującym rządem Rzeczypospolitej Polskiej. Obecnie w formie zmowy zawiązał pan koalicję przegranych przeciwko zwycięskiej formacji politycznej, czyli Prawu i Sprawiedliwości, Zjednoczonej Prawicy. To akurat pana prawo, ale ludzi, którzy obrażali naszego wielkiego sojusznika, czyli Stany Zjednoczone Ameryki, za chwilę uczyni pan ministrami w swoim rządzie. Pana zwolennicy notorycznie atakowali Kościół katolicki, duchownych i świeckich oraz symbole święte dla ludzi wierzących. Zapowiadali, że po dojściu do władzy opiłują katolików z przywilejów. Dzisiaj ci sami ludzie również mają zostać ministrami w pana rządzie. Najpierw zapowiadał pan siłowe rozwiązania, a teraz zapowiada pan odwet na konkurentach politycznych. Nie mam pytań o to, co pan i pana poplecznicy będą robić w najbliższej i dalszej przyszłości. To z grubsza wiem. Mam tylko jedno pytanie. (Dzwonek) Jak panu nie wstyd, szczególnie w obliczu dzisiejszego skandalu? Bo już dziś zbiera pan żniwo swojej obłędnej działalności. (Oklaski) (Poseł Antoni Macierewicz: Na nas, na Polskę to spada.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Głos zabierze poseł Edward Siarka, Klub Parlamentarny Prawo i Sprawiedliwość Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 760",
                },
                {
                    "speaker": "Poseł Edward Siarka",
                    "content": "Pani Marszałek! Wysoki Sejmie! Słuchałem dzisiejszego exposé pana premiera. Odniosłem nieodparte wrażenie, że zostało ono napisane na podstawie wpisów i postów w mediach społecznościowych. (Poseł Antoni Macierewicz: Tak to jest na całym świecie.) Niestety, tak to jest, ale część tych wpisów państwo sami tworzyli. Jedno z takich haseł, które państwo wytworzyli, którym pan bardzo sprawnie się posługiwał, to hasło: wyrzynają polskie lasy. Otóż chcę panu powiedzieć, że plany urządzenia lasów, na podstawie których pozyskuje się drewno, zatwierdzone były również za państwa rządów. (Głos z sali: Ale zmieniliście.) Proszę pamiętać, że ilość drewna, które w Polsce pozyskujemy, nie odbiega od ilości, którą pozyskiwaliśmy kiedyś, przed laty. To jest ta sama liczba, w granicach 40 mln m3. Pytanie: Czym, panie premierze, w takim razie zastąpić surowiec odnawialny i ekologiczny, jeśli państwo chcecie realizować rzeczywiście unijne cele klimatyczne? To jest bardzo poważne pytanie. (Dzwonek) Jeszcze do tego państwo dorzucili hasło: wywozicie drzewo do Chin. Niestety, Lasy ani 1 m3 drewna nie sprzedały do Chin. Dziękuję bardzo. (Oklaski) (Poseł Donald Tusk: Pośrednicy. Wiemy przecież.)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękujemy, panie pośle. Głos zabierze pani poseł Maria Kurowska, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Maria Kurowska",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Już za kilka godzin będzie pan premierem naszej ojczyzny. A ja bym chciała w krótkich słowach uświadomić panu, że będzie pan premierem niezwykłego kraju, chociaż pan o polskości kiedyś wypowiedział się bardzo niepozytywnie. Nie chcę tego przypominać. Panie premierze, Polska to jedyny taki kraj w świecie, który wziął się z chrztu świętego. Dzięki temu, że Mieszko I, władca Polan, przyjął chrzest, to potem inne plemiona do niego dołączały, wszystkie pozostałe, które wtedy były na terytorium Polski, i stała się wielka Polska. Fundamentem tej Polski była wiara w Boga, wiara w Jezusa Chrystusa, a podstawą tego jest miłość Boga i miłość ludzi. Dzięki temu nasza historia jest taka niezwykła. Chodzi o to, że gdy trzeba było bronić tę Europę, w której pan sprawował swoje piękne funkcje, to… Proszę zauważyć, że gdy (Dzwonek) nawałnica turecka szła na Europę, to my ją odgoniliśmy. Jan III Sobieski obronił. Gdy bolszewicka szła na Warszawę i na Europę, też obroniliśmy Europę. Gdy trzeba… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł. Zapraszam do zabrania głosu pana posła Jerzego Maternę, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Jerzy Materna",
                    "content": "Pani Marszałek! Wysoka Izbo! Czas, by Klub Parlamentarny Prawo i Sprawiedliwość, największy klub, miał swojego wicemarszałka w osobie Elżbiety Witek. Szanuję demokrację i większość parlamentarną, która wyłoniła premiera nowego rządu. Przez jakiś czas jako sekretarz stanu w Ministerstwie Gospodarki Morskiej i Żeglugi Śródlądowej zajmowałem się żeglugą śródlądową. W krótkim czasie przygotowaliśmy program rozwoju dróg wodnych w Polsce o znaczeniu międzynarodowym. Ratyfikowaliśmy europejskie porozumienie AGN. Przygotowane zostały przez ministerstwo plany, uzgodnienia środowiskowe dla Odry i Wisły. Mieliśmy szerokie poparcie urzędów marszałkowskich wszystkich województw, które leżą przy Odrze i Wiśle, w tym lubuskiego. Przypomnę, że Polska przyjmuje tylko 6% wód opadowych z 65 mld m3. Jesteśmy pod tym względem na ostatnim miejscu w Europie. Dla porównania Hiszpania przyjmuje 50%. (Dzwonek) Jest potrzeba wybudowania kilkudziesięciu zbiorników u podnóża gór od wschodu do zachodu kraju, które mają na celu alimentowanie wody, zapobieganie powodziom… (Wicemarszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Zapraszam do zabrania głosu pana posła Artura Szałabawkę, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Artur Szałabawka",
                    "content": "Pani Marszałek! Panie Premierze! Wysoka Izbo! Chile, rok 2020, palone kościoły – tak się wiąże ten dym w kościołach… Pan się spotkał z tą osobą, z tą dziczą lewacką, która to robiła. Powinien pan to odwołać, powinien pan odwołać te…, powiedzieć, że to był błąd. Panie Premierze! Silne Pomorze Zachodnie to polska racja stanu. Infrastruktura na Pomorzu Zachodnim, infrastruktura drogowa w ostatnich latach rozwinęła się niesamowicie. Nie wszystkie rzeczy zdążyliśmy zrobić. Wszystkie rzeczy są mocno zaawansowane. Zostały w realizacji dwie ważne inwestycje: obwodnica zachodnia Szczecina z tunelem Police – Święta i droga S10. To są drogi, na które już są rozpisane przetargi. Te inwestycje już są w toku. ChciałPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów 761 bym usłyszeć… Najważniejszą rzeczą jest, jak premier, polityk (Dzwonek) najważniejszy w kraju, powie: tak, te inwestycje będą dalej finansowane, te inwestycje będą dla zachodniopomorskiego realizowane. Na to liczę. Z góry o to proszę. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Głos zabierze poseł Sylwester Tułajew, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Sylwester Tułajew",
                    "content": "Pani Marszałek! Wysoka Izbo! Polska była i jest krajem praworządnym i krajem demokratycznym. Podważacie to? A to właśnie dzięki demokracji dokonywane są kolejne zmiany rządów. Jako Prawo i Sprawiedliwość zwyciężyliśmy w tych wyborach, chociaż stajemy się opozycją. Będziemy opozycją patriotyczną. W swoim wystąpieniu nie zaproponował pan żadnego nowego programu dotyczącego zdrowia psychicznego. Chciałbym zapytać, jak panu nie wstyd. Jak panu nie wstyd odczytywać list samobójcy? Pana działanie jest nieodpowiedzialne i bardzo szkodliwe społecznie. Bardzo nieodpowiedzialne jest również podnoszenie samobójstwa do rangi bohaterskiego czynu. Jak panu nie wstyd? Który Donald Tusk jest prawdziwy? Czy ten, który 13 kwietnia (Dzwonek) mówił, że wolałby się nie urodzić…",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle.",
                },
                {
                    "speaker": "Poseł Sylwester Tułajew",
                    "content": "…niż na grobach zmarłych budować karierę polityczną, czy ten, który jako o fundamencie mówi o samobójczych czynach? (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, panie pośle. Głos zabierze pani poseł Lidia Burzyńska, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Lidia Burzyńska",
                    "content": "Pani Marszałek! Wysoka Izbo! Panie Premierze! Przez 8 lat byłam świadkiem wielu niekulturalnych zachowań w tej sali, takich jak okupowanie mównicy, zrzucanie sztucznych banknotów z balkonu czy też śpiew, co prawda fałszowany, ale śpiew. Natomiast dzisiaj w tej Izbie, w parlamencie przy udziale pana Brauna miało miejsce coś, co szokuje każdego. Panie Premierze! W swoim exposé, które wygłaszał pan przez prawie 2,5 godziny, mówił pan dużo, przedstawiając konkretne działania swego rządu. Ze 100 konkretów udało się panu przedstawić tylko pięć. Chyba nie tego spodziewali się Polacy po pana wystąpieniu. Ale jedna niespójność nie daje mi spokoju. Mianowicie usłyszałam, że wszystkie polskie kobiety poczują poprawę swojego życia. Jak to się ma do zniesienia zakazu handlu w niedzielę? Jak to się ma do tych słów? Przecież chyba (Dzwonek) pan wie… Albo inaczej: powinien pan wiedzieć, że w handlu pracuje ok. 2 mln osób, z czego ok. 90% to kobiety.",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Dziękuję, pani poseł.",
                },
                {
                    "speaker": "Poseł Lidia Burzyńska",
                    "content": "Jaką więc poprawę będą mieć wszystkie polskie kobiety? (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Wicemarszałek Dorota Niedziela",
                    "content": "Bardzo dziękuję, pani poseł. Głos zabierze poseł Michał Wójcik, Klub Parlamentarny Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Michał Wójcik",
                    "content": "Szanowna Pani Marszałek! Szanowny Panie Premierze! Szanowni Państwo! To, co dzisiaj się stało, to straszne obrazki, które pójdą w świat. Taka jest prawda. W związku z tym myślę, że już na tym posiedzeniu możemy zrobić pewną rzecz. Mianowicie nie wiem, czy pan wie, panie premierze, że po drugim czytaniu jest projekt Suwerennej Polski dotyczący obrony wolności religijnej, wolności wyznania. Wolność religijna, wolność wyznania to jedna z najważniejszych wolności, to autonomia człowieka. Niestety w poprzednich czytaniach głosowaliście przeciwko. Ale mam propozycję, żebyśmy już na tym posiedzeniu pochylili się nad tym projektem i go przyjęli. Niech to będzie taki test, bo przecież była mowa o opiłowywaniu katolików, Kościołów, malowaniu kościołów… Chrońmy chrześcijan, wyznawców judaizmu, islamu, niezależnie od tego, jaka by to była religia.  Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów W związku z tym składam, panie marszałku… Dla pana marszałka to również jest test, bo wszystkich nas oburzyło to zdarzenie. (Dzwonek) (Poseł Mirosław Suchoń: Przestań ściemniać, ty…) Jest projekt obywatelski. Podpisało się pod nim 0,5 mln osób. Mam prośbę, a jednocześnie formalny wniosek, ażeby rozszerzyć porządek obrad i poddać pod głosowanie projekt dotyczący obrony wolności religijnej, wolności wyznania. Jest po drugim czytaniu, jest u pana marszałka. Myślę, że możemy tę sprawę załatwić jeszcze na tym posiedzeniu. Dziękuję. (Oklaski) (Głos z sali: Tak jest!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Jak pan wie, wszystkie projekty obywatelskie zostaną rozpatrzone w terminie 6 miesięcy od rozpoczęcia kadencji Sejmu. (Gwar na sali) (Głos z sali: Ha, ha, ha!) (Głos z sali: Przecież to bezczelność.) Ale chwileczkę, dajcie mi państwo powiedzieć. (Poseł Piotr Kaleta: Teraz jest dobry moment na rehabilitację.) Postaram się ten wniosek pana posła uwzględnić, żeby stało się to możliwie jak najszybciej. Bardzo proszę, pan poseł Aleksander Mikołaj Mrówczyński.",
                },
                {
                    "speaker": "Poseł Aleksander Mikołaj Mrówczyński",
                    "content": "Panie Marszałku! Wysoka Izbo! Pamięć jest zawodna. Ile zła uczyniła koalicja PO–PSL w latach 2007–2015 Polsce, Polakom, Polacy zapomnieli w większości 15 października. Do waszych, Neumanna, Palikota, doktryn charakteryzujących się wsparciem swoich i bezgranicznym kłamstwem doszła mowa przekleństw, wulgaryzmów, ataki na Kościół, na św. Jana Pawła II, do którego dzisiaj się pan, panie premierze, odwołuje. A jakże wielu z was z totalnej opozycji – zawsze nią będziecie – przy ślubowaniu odwoływało się do Boga, a są zwolennikami aborcji, którą pan, panie premierze, zapowiedział! Lata 2015–2023 to najlepszy czas dla Rzeczypospolitej. Przede wszystkim przywróciliśmy godność Polakom, lepsze jutro. Przekazujemy nowo rządzącym Polskę zasobną, suwerenną, ze stolicą w Warszawie. Nie zwalczajcie dobra złem. (Dzwonek) Panie Premierze! Czy dalej chcecie kłamać, gdyż kłamstwa wielokrotnie powtarzane stają się prawdą? Czy pozwoli pan katolików opiłować? To jest najważniejsze. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Przedostatni zabierze głos pan poseł Bartłomiej Wróblewski.",
                },
                {
                    "speaker": "Poseł Bartłomiej Wróblewski",
                    "content": "Panie Marszałku! Wysoka Izbo! Dołączam do apelu pana posła Wójcika odnośnie do szybkiego rozpatrzenia projektu obywatelskiego dotyczącego ochrony wolności religijnej. To bardzo ważny projekt. Jeśli chodzi o pana wystąpienie, złożył pan kategoryczną, ważną deklarację, że zasady demokracji będą szanowane bez wyjątku. Właśnie o te wyjątki chciałem zapytać, wyjątki, które widzimy w obecnym Sejmie. Dlaczego odchodzicie od parytetu, jeśli chodzi o liczbę komisji, gdzie przewodnictwo ma opozycja? W poprzedniej kadencji mieliście dwa razy więcej komisji, niż dzisiaj ma Prawo i Sprawiedliwość. Dlaczego po raz pierwszy zdarzyło się, że sześciu parlamentarzystów, którzy trafili do KRS, jest z rekomendacji lewicowo-liberalnej koalicji, a nie ma nikogo z rekomendacji opozycji? Dlaczego wreszcie Prawo i Sprawiedliwość nie ma wicemarszałka ani w Sejmie, ani w Senacie? To jest pytanie o pana wiarygodność (Dzwonek), pytanie o konsekwencję. Ważna deklaracja została złożona. Chciałbym wiedzieć, dlaczego to nie jest dotrzymywane. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Bardzo proszę, pan poseł Rafał Weber.",
                },
                {
                    "speaker": "Poseł Rafał Weber",
                    "content": "Panie Marszałku! Wysoka Izbo! Szanowni Państwo! Przedstawiciele Większości Sejmowej! Pozwalaliście na to, aby poseł Grzegorz Braun podczas tego cały czas pierwszego posiedzenia Sejmu atakował polityków Prawa i Sprawiedliwości. Śmialiście się z tego razem z nim, a dzisiaj zbieracie tego żniwo. (Poseł Mirosław Suchoń: Przestań głupoty opowiadać.) Szanowni Państwo! Nie ma żadnej różnicy między posłem Braunem a Januszem Palikotem, którego też przez lata hodowaliście i wypuszczaliście, wtedy kiedy trzeba było atakować śp. Lecha Kaczyńskiego, wtedy kiedy trzeba było atakować Jarosława Kaczyńskiego, wtedy kiedy trzeba było zniżać się do najniższych instynktów, aby zarzucać Prawo i Sprawiedliwość obelgami, chamstwem, hejtem, wszelkimi niegodziwościami. Jesteście współodpowiedzialni za ten skandal, który dzisiaj stał się w Sejmie. Można, szaPrzedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów nowni państwo, mieć marszałka rotacyjnego, ale (Dzwonek) rotacyjnej odpowiedzialności nie będzie. Jesteście temu współwinni. (Oklaski) (Głos z sali: Tak jest!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Na tym wyczerpaliśmy listę posłów, którzy chcieli zadać pytania. Za chwilę oddam głos panu premierowi. Proszę mi pozwolić jedynie – ponieważ spora część z państwa odnosiła się też do mnie – że powiem bardzo krótko i mam nadzieję, że co do tego akurat wszyscy się zgodzimy. Nie możemy pozwolić złu zwyciężyć dobra. Nie możemy dopuścić do tego, żeby szaleństwo, żeby absurdy, żeby obrażanie, żeby dewiacje ksenofobii czy antysemityzmu… (Głos z sali: Czy antypolonizmu też?) …układały porządek obrad Sejmu Rzeczypospolitej, decydowały o tym, kiedy mają być powoływani prezesi Rady Ministrów i kiedy mają być odwoływani. Nie możemy pozwolić, żeby ludzie tacy jak poseł Braun sprawili, że my staniemy się gorszymi ludźmi. (Głos z sali: Tacy jak ty.) Dlatego zapewniam państwa, że Sejm nadal pozostanie otwarty dla wszystkich ludzi dobrej woli (Oklaski), nadal będzie Sejmem, który będzie cieszył się, a nie martwił tym, że oglądają go miliony Polaków, nadal będzie miejscem, gdzie spotykać się będziecie państwo z mojej strony z szacunkiem, serdecznością i uśmiechem. Bo to jest właśnie to, co najbardziej zawstydza i niszczy ludzi takich jak poseł Braun, który dzisiaj pokazał się z najgorszej możliwej strony. Drodzy Państwo! Nie możemy pozwolić, żebyśmy się stali zakładnikami Brauna, żebyśmy się stali zakładnikami innych Braunów świata. Nie możemy dopuścić, żebyśmy stali się ludźmi zalęknionymi, a więc agresywnymi w reakcji na tego typu incydenty. Chcę państwa zapewnić, że zrobiliśmy absolutnie wszystko – jeszcze dzisiaj w sprawie posła Brauna zostanie złożony wniosek do prokuratury. A ja chciałbym, mówiąc o tym, że Sejm nie będzie zamkniętą twierdzą już nigdy, będzie miejscem otwartym dla ludzi dobrej woli, odczytać list, bo myślę, że to ważne. Powinniśmy dzisiaj dać głos tej stronie – panu rabinowi Schudrichowi i panu rabinowi Szalomowi Ber Stamblerowi – i odczytać ten list, który skierowali do mnie. Bardzo bym prosił, żebyście państwo wysłuchali, bo tam jest zawarta moim zdaniem bardzo trafna propozycja, z której chciałbym, żebyśmy wspólnie skorzystali: Szanowny Panie Marszałku! Wciąż jesteśmy zszokowani dzisiejszym incydentem w gmachu Sejmu przy okazji ceremonii zapalenia świec chanukowych. Przez wiele lat polski Sejm gościnnie przyjmował przedstawicieli wspólnoty żydowskiej w okresie święta Chanuki. Kolejni marszałkowie i parlamentarzyści różnych opcji politycznych przyłączali się do wspólnego świętowania, skupiając się wokół światła, symbolu mądrości, tolerancji i jedności ponad podziałami. Również dzisiaj, pomimo iż jest to jest dzień wyboru nowego rządu i intensywnych obrad, Kancelaria Sejmu umożliwiła nam organizację dorocznej ceremonii, która w zasadniczej części przebiegła bez zakłóceń. Tym bardziej szokujące było to, co nastąpiło chwilę później. Jesteśmy bardzo wdzięczni panu marszałkowi, Prezydium Sejmu i wszystkim parlamentarzystom za szybkie i stanowcze potępienie tego incydentu. Obawiamy się jednak, że przekaz, który poszedł w świat, zniweczy nasze wieloletnie starania o ugruntowanie obrazu Polski jako kraju tolerancyjnego i otwartego na różnorodność. Święto Chanuki uczy nas, że nawet małe światełko może rozproszyć wielką ciemność. Musimy jednak być wytrwali w podtrzymywaniu tego światła, by skutecznie walczyć ze złem i nienawiścią. Dlatego zwracamy się do pana marszałka z prośbą o umożliwienie nam ponownego zapalenia świec chanukowych w Sejmie w dniu jutrzejszym. Ta sytuacja wymaga działania już, a nie za rok przy okazji kolejnej Chanuki. (Oklaski) Liczymy bardzo na współpracę ze strony pana marszałka i Kancelarii Sejmu. Wspólnie w sposób pokojowy musimy przeciwstawić się zachowaniom antysemickim i agresywnym, które uwłaczają godności polskiego parlamentaryzmu. Jedyną naszą szansą jest zło dobrem zwyciężać. Drodzy Państwo! Z przyjemnością chciałbym odpowiedzieć na ten apel panów rabinów. Jutro zorganizujemy po raz drugi zapalenie świecy chanukowej na terenie Sejmu. Serdecznie państwa wszystkich na tę uroczystość zapraszam (Oklaski), niezależnie od barw partyjnych, niezależnie od przynależności, sympatii czy antypatii. Bądźmy jutro wszyscy razem i pokażmy naszą solidarność w tym względzie. (Poseł Jakub Rutnicki: O której?) Z kwestii formalnych… (Poseł Jakub Rutnicki: O której godzinie?) To właśnie jeszcze ustalamy z przedstawicielami wspólnoty żydowskiej. (Poseł Antoni Macierewicz: Z panem Tuskiem koniecznie.) Dam państwu znać jeszcze w czasie tego posiedzenia Sejmu. Szanowni Państwo! Chcę poinformować, że wpłynęły, jak państwo wiecie, dwie uchwały Lewicy. Jedna dotyczy podjęcia dzisiaj uchwały potępiającej to, co się stało, druga dotyczy odwołania pana wicemarszałka Bosaka ze składu Prezydium Sejmu. Nad tą pierwszą będziemy procedować jeszcze dzisiaj, jeżeli zgodzą się na to Prezydium Sejmu i Konwent Seniorów, które zwołam w przerwie w ciemnym saloniku po wystąpieniu pana premiera. Natomiast procedowanie nad drugą z nich zaplanowałem – mówię o odwołaniu pana marszałka Bosaka z Prezydium Sejmu Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów – na przyszłotygodniowym posiedzeniu Sejmu po zaopiniowaniu przez Prezydium i Konwent Seniorów. W przerwie po wystąpieniu pana premiera, tak jak powiedziałem, zapraszam Prezydium i Konwent do ciemnego saloniku. Dokonamy też korekty w dzisiejszym planie obrad, najprawdopodobniej tak, żebyśmy mogli skupić się wyłącznie na rzeczach niecierpiących zwłoki. Panie premierze, bardzo proszę. (Poseł Antoni Macierewicz: Czy można, przepraszam bardzo?) Panie pośle, w jakim trybie? (Poseł Antoni Macierewicz: To jest pytanie.) Tak, proszę.",
                },
                {
                    "speaker": "Poseł Antoni Macierewicz",
                    "content": "Panie Marszałku! Wysoka Izbo! Sprawa tej uchwały jest bardzo ważna, to prawda, ale rozumiem, że zawiera ona uzupełnienie, o którym tu była mowa, a mianowicie także kwestię nieatakowania katolicyzmu. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, to będzie przedmiotem narady Prezydium i Konwentu Seniorów. Druk został już państwu posłom w formie elektronicznej dostarczony, bo przed chwilą poleciłem drukować oba te projekty uchwał. Bardzo proszę, panie premierze, o zabranie głosu. (Oklaski)",
                },
                {
                    "speaker": "Prezes Rady Ministrów Donald Tusk",
                    "content": "Panie Marszałku! Szanowne Posłanki! Szanowni Posłowie! Wszyscy jesteśmy przygnębieni tym, co zdarzyło się w naszym Sejmie. Wszyscy czujemy brzemię odpowiedzialności za to, w jaki sposób obserwujący to, co się dzieje w Sejmie, Polki, Polacy, wspólnota żydowska w Polsce… Obawiamy się też, i chyba słusznie, że także na świecie sporo ludzi, sporo środowisk obserwowało z niepokojem to, co wydarzyło się w Sejmie. To jest nasza wspólna odpowiedzialność też za to, żeby zapobiec nie tylko takim zdarzeniom, ale żeby w tej sprawie nikt z nas… Bo wydaje mi się, że można, skoro nie ma na tej sali w tej chwili pana posła Brauna, że chyba nie jest ryzykowne powiedzenie, że nikt więcej na tej sali nie akceptowałby w żadnej sytuacji takiego zachowania (Oklaski), że jest chyba możliwe, i do tego starałem się przekonać – wiem, że nie wszystkich przekonałem, niektórzy ciągle podejrzewają zawsze jakieś złowrogie intencje, ale starałem się bardzo szczerze przekonać do tego – że istnieje pewien fundament, istnieje pewna kategoria… (Poseł Antoni Macierewicz: …co pan mówi.) …spraw, wokół której nie powinno być sporów. Powinien być możliwie pełny konsensus i to nie jest trudne. I wiecie co? Był taki moment, kiedy jeden z posłów, poseł Zembaczyński, wszedł na mównicę i poinformował siedzących na sali, co się wydarzyło. Część z państwa pewnie to widziała też na telefonach, bo było to widać na filmach. I zauważyłem – przecież byłem z wami na sali – że w ciągu tych pierwszych sekund, a nawet pierwszych minut reakcja wszystkich bez wyjątku była identyczna. To znaczy nagle przez moment naprawdę nie widziałem żadnej różnicy między lewą stroną, prawą stroną i centrum. Wszyscy zareagowali w taki sam sposób, może Konfederacja trochę bardziej powściągliwie, raczej ze wstydem niż z oburzeniem, ale cała reszta zachowała się dokładnie tak samo. I był taki moment unikatowy, kiedy można było poczuć, że w takich najważniejszych sprawach czujemy mniej więcej to samo i reagujemy mniej więcej tak samo. Wydaje mi się, że właśnie w takich sprawach powinniśmy starać się podtrzymać tę gotowość do bycia razem wobec np. tak ewidentnego manifestacyjnego zła, jakie wydarzyło się tutaj, w Sejmie. Chcę też powiedzieć, bo wiecie, źle by się stało, gdyby Polska pomyślała przez moment, że tego typu bandycki wyczyn, że on może podważyć to wszystko, nad czym pracujemy dzisiaj, wspierając się, dyskutując, a my dzisiaj dyskutujemy nad wyłonieniem nowego rządu. Można lubić ten nowy rząd, nie lubić, ale wszyscy mieliśmy poczucie wagi tego dnia i powagi sytuacji. Dlatego bardzo bym chciał powiedzieć tutaj wbrew temu zrozumiałemu nastrojowi – sam uległem temu nastrojowi przygnębienia, właściwie, szczerze powiedziawszy, chyba wszyscy przeżyliśmy szok – wbrew być może intencjom pana posła Brauna, żebyśmy nie skapitulowali przed tego typu manifestacjami i żebyśmy dalej robili swoje, żebyśmy dzisiaj powiedzieli Polsce: jest nowy rząd. Stało się coś bardzo złego, ale proszę państwa, my jesteśmy tutaj od tego, żeby takie złe rzeczy nie podważały niczego, co jest dla nas i dla Polski istotne (Oklaski), żebyśmy się nie dali temu w najmniejszym stopniu. (Głos z sali: Ale rząd PiS…) 7 godzin siedziałem tak jak niektórzy z pań i panów posłów na tej sali, słuchając pytań czy, powiedziałbym raczej jednak w przygniatającej większości przypadków, pewnych manifestów, wypowiedzi, krytyki. Pamiętam jeszcze z dawniejszych czasów oczywiście, że taka jest logika tzw. pytań, że to służy zamanifestowaniu własnego poglądu, chociaż muszę powiedzieć, że zmieniły się trochę proporcje. Pozwolicie państwo, że z tego 7-godzinnego materiału wyłowimy to, co było pytaniem domagającym się precyzyjnej odpowiedzi Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów. Sprawy formalne Proszę się nie gniewać, to nie jest uwaga do nikogo na tej sali, ani personalna, ani klubowa, ale to nie jest tak prosto wyłowić konkretne pytania, które dotyczyły konkretnych spraw w tym jednak zalewie raczej takiej politycznej konfrontacji i politycznych manifestów. Otrzymacie państwo na każde pytanie, które było pytaniem, a nie politycznym manifestem, odpowiedź na piśmie. (Oklaski) I dostaniecie tę odpowiedź, każda z pań i każdy z panów posłów, na piśmie do czasu, kiedy spotkamy się następny raz w tej sali, a więc to będzie początek przyszłego tygodnia. Na pewno istotną część czasu, soboty, a także jutrzejszego dnia po zaprzysiężeniu, moi ministrowie już spędzą, żeby przypilnować rzetelności odpowiedzi na to, co było naprawdę pytaniami. Ale nie mogę też nie zauważyć tego, że przy tej bardzo przykrej okazji, jaką stał się ten eksces pana posła Brauna, pojawiły się też projekty i pomysły, żeby np. odroczyć posiedzenie i żeby je jutro kontynuować. Pan poseł Przemysław Czarnek zaproponował to odroczenie. Proszę państwa, wydaje się, że to próba odroczenia werdyktu wyborców. Ona powinna mieć swoje granice. Nie musicie państwo szanować mojego czasu czy tego, co ustaliliśmy po stronie koalicji rządowej, ale część z państwa chyba orientuje się, że wczoraj na długim, niespodziewanie długim i dobrym spotkaniu z panem prezydentem Dudą, tu, w gmachu parlamentu, ustaliliśmy, i to była też jego propozycja, że jutro o godz. 9 rano ma nastąpić zaprzysiężenie nowego rządu. Wiecie państwo – pan prezydent rozumiał to bardzo dobrze – że ten pośpiech jest potrzebny także ze względu na okoliczności zewnętrzne. To dotyczy zarówno misji prezydenta Zełenskiego w Brukseli – wiecie, że będę tam chciał być i na pewno w imieniu was wszystkich też wesprzeć w kwestiach wojennych Ukrainę w Brukseli – jak i kwestii tych pieniędzy. Dobrze rozumiemy, że nie warto tutaj już grać w żaden sposób na zwłokę. Tak że bardzo bym prosił państwa, żeby szczególnie tak ponurych incydentów nie wykorzystywać jako sposobu na przedłużanie, na grę na czas, bo szkoda Polski, że tak powiem (Oklaski), na tego typu grę, bo tak to wyglądało. (Poseł Antoni Macierewicz: To nie był taki sposób, proszę takich aluzji nie robić.) Proszę państwa, ja oczywiście nie jestem gospodarzem tej Izby, jestem jednym z was, jestem wciąż szeregowym posłem, ale wydaje mi się, że jest bardzo ważne… Przecież będziemy tu razem pracowali przez 4 lata. (Głos z sali: Okaże się.) Jak wiemy, przez 2 lata, lubicie to słowo: rotacyjny, marszałkiem będzie, wszystko na to wskazuje, pan marszałek Hołownia. Ja rozumiem emocje, też rozumiem jakieś negatywne sentymenty, normalne w polityce, ale po tych kilku minutach takiego wspólnego, naprawdę szlachetnego oburzenia na to, co zrobił Braun, tak szybko przejść do próby obarczenia za to, co się tutaj stało, marszałka Hołowni – to też jest przekroczenie granic. Naprawdę nie można robić takich rzeczy. (Oklaski) Jeśli komuś do głowy dzisiaj przyszło powiedzieć, że za to, co zrobił Braun, za atak gaśnicą na świece chanukowe, na kobietę, na te dzieci, przypadkowo trafione tym proszkiem z gaśnicy… Pewnie nieintencjonalnie, ale to wszystko było makabryczne i niestety świat to zobaczył. Przecież chcemy się wszyscy od tego odciąć kategorycznie i jednoznacznie. No nie wierzę w to, żeby ktokolwiek z tej strony sali naprawdę wierzył, że marszałek Hołownia jest za to odpowiedzialny. Na miłość Boga, ludzie, my się w żadnej sprawie nie dogadamy, jak będziemy takie rzeczy opowiadali. (Oklaski) Tak że ja ciągle biorę za znak nadziei tę pierwszą naszą reakcję. Ona była naprawdę wspólna i ona jest znakiem nadziei na to, że w sytuacjach krytycznych, kiedy zło jest manifestacyjne, kiedy coś złego, groźnego się dzieje, odnajdziemy jakiś elementarny, wspólny język. Na to bardzo liczę. I jeszcze raz zwracam się do wszystkich, którzy nas pewnie też z domu przez cały dzień oglądają. Stało się coś złego, ale przejdziemy to… (Poseł Małgorzata Gosiewska: Ale ktoś jest odpowiedzialny za to.) …przejdziemy to i za kilka minut, za kilkanaście minut będziecie świadkami powstania nowego rządu, a jutro ten rząd zostanie przez pana prezydenta zaprzysiężony. (Oklaski) Tak że nie traćcie nadziei. Nie ma żadnego powodu. A zło, które się tutaj zamanifestowało, pokonamy – wspólnie czy nowa koalicja, ale to zło na pewno pokonamy. Jeszcze raz bardzo dziękuję. (Oklaski) Jeśli chodzi o odpowiedzi na pytania, może państwa nie było na sali, kiedy precyzyjnie wytłumaczyłem… (Głos z sali: Ale Polacy chcą usłyszeć.) …kiedy otrzymacie odpowiedź na każde z pytań. Dziękuję bardzo. (Oklaski, poruszenie na sali)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Zamykam dyskusję. (Wypowiedź poza mikrofonem) Słucham? (Poseł Paweł Jabłoński: Krótki wniosek formalny.) (Poseł Mirosław Suchoń: Nie ma czegoś takiego, nie ma trybu.) (Poseł Paweł Jabłoński: Panie marszałku, wniosek formalny…) Bardzo proszę… (Gwar na sali) Ale poczekajcie państwo, sprawa jest jasna.",
                },
                {
                    "speaker": "Poseł Paweł Jabłoński",
                    "content": "Dziękuję, panie marszałku. Wniosek formalny. Art. 117 ust. 2 regulaminu mówi, że debata nad wnioskiem obejmuje zadawanie pytań prezesowi Rady Ministrów oraz… (Głos z sali: Odpowiedzi.) Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów …jego odpowiedzi na te pytania. (Oklaski) Panie premierze, wczoraj byliśmy w tej Izbie, pan premier Morawiecki przez prawie godzinę odnosił się do pytania każdego jednego posła – z szacunku do tej Izby. Jeśli chodzi o pytania w sprawach bieżących, w sprawach dotyczących różnych kwestii Rady Ministrów, oczywiście odpowiedzi na te pytania mogą być udzielane na piśmie, to jest normalne. Ale w debacie nad wotum zaufania… (Poseł Jan Grabiec: Jest nie jest wotum zaufania, to jest wybór.) …naprawdę zasługuje nie tylko Sejm, zasługujemy nie tylko my na tej sali, nie tylko posłowie, ale zasługują te miliony ludzi, na które się tak bardzo chętnie powołujecie, żeby pan udzielił tej odpowiedzi. Ja pana pytałem o odwagę.",
                },
                {"speaker": "Marszałek", "content": "Panie pośle…"},
                {
                    "speaker": "Poseł Paweł Jabłoński",
                    "content": "Ja pana pytałem o odwagę. (Poseł Donald Tusk: Jesteśmy w innym punkcie.) Niech pan ma odwagę udzielić odpowiedzi na pytania w tej Izbie.",
                },
                {"speaker": "Marszałek", "content": "Panie pośle…"},
                {
                    "speaker": "Poseł Paweł Jabłoński",
                    "content": "Panie marszałku, wnoszę o to, żeby pan zobowiązał premiera do przestrzegania regulaminu, art. 117 pkt 2. (Oklaski) (Poseł Mirosław Suchoń: Nie zna pan regulaminu.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Tak, panie pośle. Pomylił pan artykuły. Art. 117 dotyczy wotum zaufania wyrażanego Radzie Ministrów, a my jesteśmy w art. 113, który bardzo precyzyjnie opisuje, jak wygląda powoływanie Rady Ministrów w drugim konstytucyjnym etapie, i tam słowa, o których pan mówi, i procedury, o których pan mówi, nie mają zastosowania. (Głos z sali: Debaty nie ma.) Przeczytam panu, żeby nie miał pan wątpliwości. (Oklaski) (Głos z sali: Skandal!) Sejm wybiera prezesa Rady Ministrów w głosowaniu imiennym. Prezes Rady Ministrów przedstawia Sejmowi na posiedzeniu program działania rządu oraz proponowany przez niego skład Rady Ministrów. Wniosek prezesa Rady Ministrów w sprawie wyboru Rady Ministrów jest głosowany łącznie. Art. 112 ust. 2 stosuje się odpowiednio. Wszystkie punkty tej procedury zostały wypełnione. Rozumiem, że pan premier odniósł się do tych głosów, które miały miejsce, w sposób, jaki uznał za stosowny. (Poseł Antoni Macierewicz: Niech pan nie wprowadza w błąd.) (Głos z sali: Skandal!) A państwo będą mogli wyrazić swoją ocenę tej sytuacji w głosowaniu. Zarządzam przerwę do godziny 21.35. I wtedy, będę bardzo prosił państwa o obecność na sali, będziemy głosować. A teraz zwołuję Prezydium Sejmu, a następnie Konwent Seniorów w ciemnym saloniku. Dziękuję. (Głos z sali: To jest kabaret.) Ogłaszam przerwę.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Szanowni Państwo! Bardzo się cieszę z waszego dobrego samopoczucia. Zapraszam Konwent Seniorów na chwilę do ciemnego saloniku.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Wznawiam obrady. Powracamy do rozpatrywania punktu 38. porządku dziennego: Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów. (Gwar na sali) Bardzo proszę o ciszę. Sejm wysłuchał prezesa Rady Ministrów pana Donalda Tuska oraz przeprowadził dyskusję. Przypominam, że zgodnie z art… (Wypowiedź poza mikrofonem) Szanowni państwo, zacytowałem literalnie artykuł regulaminu Sejmu. W którym punkcie jesteśmy, wiemy. Został zrealizowany. Przypominam, że zgodnie z art. 154 ust. 3 Konstytucji Rzeczypospolitej Polskiej Sejm wybiera członków Rady Ministrów zaproponowanych przez prezesa Rady Ministrów bezwzględną większością głosów w obecności co najmniej połowy ustawowej liczby posłów Przedstawienie przez Prezesa Rady Ministrów programu działania oraz składu Rady Ministrów wraz z wnioskiem w sprawie wyboru członków Rady Ministrów – głosowanie Zgodnie z art. 113 ust. 5 regulaminu Sejmu wniosek prezesa Rady Ministrów w sprawie wyboru Rady Ministrów jest głosowany łącznie. Przystępujemy do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku prezesa Rady Ministrów pana Donalda Tuska w sprawie wyboru członków Rady Ministrów, druk nr 96, w składzie: — pana Władysława Kosiniaka-Kamysza – na urzędy wiceprezesa Rady Ministrów i ministra obrony narodowej, — pana Krzysztofa Gawkowskiego – na urzędy wiceprezesa Rady Ministrów i ministra cyfryzacji, — pana Macieja Berka – na urząd ministra – członka Rady Ministrów, — pana Adama Bodnara – na urząd ministra sprawiedliwości, — panią Agnieszkę Buczyńską – na urzędy ministra do spraw społeczeństwa obywatelskiego i przewodniczącej Komitetu do spraw Pożytku Publicznego, — pana Borysa Budkę – na urząd ministra aktywów państwowych, — panią Marzenę Czarnecką – na urząd ministra przemysłu, — pana Andrzeja Domańskiego – na urząd ministra finansów, — panią Agnieszkę Dziemianowicz-Bąk – na urząd ministra rodziny, pracy i polityki społecznej, — pana Jana Grabca – na urząd ministra – członka Rady Ministrów, — panią Paulinę Hennig-Kloskę – na urząd ministra klimatu i środowiska, — pana Krzysztofa Hetmana – na urząd ministra rozwoju i technologii, — pana Marcina Kierwińskiego – na urząd ministra spraw wewnętrznych i administracji, — pana Dariusza Klimczaka – na urząd ministra infrastruktury, — panią Katarzynę Kotulę – na urząd ministra do spraw równości, — panią Izabelę Leszczynę – na urząd ministra zdrowia, — pana Sławomira Nitrasa – na urząd ministra sportu i turystyki, — panią Barbarę Nowacką – na urząd ministra edukacji, — panią Marzenę Okłę-Drewnowicz – na urząd ministra do spraw polityki senioralnej, — panią Katarzynę Pełczyńską-Nałęcz – na urząd ministra funduszy i polityki regionalnej, — pana Czesława Siekierskiego – na urząd ministra rolnictwa i rozwoju wsi, — pana Tomasza Siemoniaka – na urząd ministra – członka Rady Ministrów, — pana Bartłomieja Sienkiewicza – na urząd ministra kultury i dziedzictwa narodowego, — pana Radosława Sikorskiego – na urząd ministra spraw zagranicznych, — pana Adama Szłapkę – na urząd ministra do spraw Unii Europejskiej, — pana Dariusza Wieczorka – na urząd ministra nauki zechce podnieść rękę i nacisnąć przycisk. (Głosy z sali: Hańba!) (Głos z sali: Skandal!) (Głos z sali: Wstyd!) (Głos z sali: Zdrajca!) Kto jest przeciw? Kto się wstrzymał? Głosowało 449 posłów. Większość bezwzględna wynosiła 225. Za było 248 posłów, przeciw – 201, nikt się nie wstrzymał. Stwierdzam, że Sejm bezwzględną większością głosów wybrał Radę Ministrów zgodnie z wnioskiem prezesa Rady Ministrów Donalda Tuska, zawartym w druku nr 96. (Część posłów wstaje, burzliwe oklaski) Serdecznie gratuluję Radzie Ministrów, państwu ministrom. (Część posłów skanduje: Donald Tusk! Donald Tusk! Donald Tusk!) Proszę państwa, przed nami jeszcze w tym bloku głosowań dwa głosowania. Prezydium Sejmu, po zasięgnięciu opinii Konwentu Seniorów, przedłożyło wniosek w sprawie wyboru składu osobowego Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego, druk nr 93. W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o punkt obejmujący rozpatrzenie tego wniosku. Przystępujemy do rozpatrzenia punktu 40. porządku dziennego: Wybór składu osobowego Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego (druk nr 93). Prezydium Sejmu na podstawie art. 2 ust. 1 ustawy o sejmowej komisji śledczej oraz art. 136c ust. 1 regulaminu Sejmu przedłożyło wniosek w sprawie wyboru składu osobowego komisji śledczej. Czy ktoś z pań i panów posłów pragnie zabrać głos w sprawie zgłoszonych kandydatur? Nikt się nie zgłasza. Przechodzimy do głosowania. Przypominam, że na podstawie art. 2 ust. 1 ustawy o sejmowej komisji śledczej Sejm dokonuje wyboru składu osobowego komisji śledczej bezwzględną większością głosów Wybór składu osobowego Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego – głosowanie Przystępujemy do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku w brzmieniu z druku nr 93, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 449 posłów. Większość bezwzględna to 225. Za było 447, nikt nie był przeciw, 2 posłów wstrzymało się od głosu. Stwierdzam, że Sejm bezwzględną większością podjął uchwałę w sprawie wyboru składu osobowego Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego. Informuję, że pierwsze posiedzenie tej komisji zostało zwołane na dzień 13 grudnia 2023 r. na godz. 11. Informuję, że punkt porządku dziennego obejmujący sprawozdanie komisji o poselskim projekcie uchwały w sprawie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań, a także występowania nadużyć, zaniedbań i zaniechań w zakresie legalizacji pobytu cudzoziemców na terytorium Rzeczypospolitej Polskiej w okresie od dnia 1 stycznia 2019 r. do dnia 20 listopada 2023 r., druki nr 56 i 80, tj. pkt 41. porządku dziennego, nie zostanie rozpatrzony w dniu dzisiejszym. Właściwa komisja przedłożyła sprawozdanie o poselskim projekcie ustawy o zmianie ustawy o doręczeniach elektronicznych, druk nr 94. W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o punkt obejmujący rozpatrzenie tego sprawozdania. Proponuję, aby w tym przypadku Sejm wyraził zgodę na skrócenie terminu, o którym mowa w art. 44 ust. 3 regulaminu Sejmu, oraz w dyskusji nad tym punktem porządku dziennego wysłuchał 5-minutowych oświadczeń w imieniu klubów i 3-minutowego oświadczenia w imieniu koła. Jeżeli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycje przyjął. Sprzeciwu nie słyszę. Przystępujemy do rozpatrzenia punktu 42. porządku dziennego: Sprawozdanie Komisji Cyfryzacji, Innowacyjności i Nowoczesnych Technologii o poselskim projekcie ustawy o zmianie ustawy o doręczeniach elektronicznych (druki nr 92 i 94). Proszę pana posła Michała Gramatykę o krótkie przedstawienie sprawozdania komisji. Jest to, drodzy państwo, projekt niekontrowersyjny, ważny dla Polaków. Mam nadzieję, że szybko go dzisiaj przeprocedujemy, tak żeby mógł zająć się nim Senat. Poseł Sprawozdawca",
                },
                {
                    "speaker": "Michał Gramatyka",
                    "content": "Szanowny Panie Marszałku! Wysoki Sejmie! Komisja Cyfryzacji, Innowacyjności i Nowoczesnych Technologii obradowała nad projektem w dniu wczorajszym. Żadne postanowienia projektu tej ustawy nie wzbudziły najmniejszych kontrowersji. Wszystkie zgłoszone podczas prac komisji poprawki zostały przyjęte jednogłośnie, podobnie jednogłośnie została wyrażona pozytywna opinia dla tego projektu ustawy. Projekt ustawy jest niezbędny, aby odsunąć w czasie powstanie obowiązków związanych z zakładaniem skrzynek do elektronicznych doręczeń, a w szczególności odsunąć w czasie powstanie obowiązków, które rodzi w związku z założeniem takich skrzynek Kodeks postępowania administracyjnego. Czas, który zyskamy dzięki temu projektowi, mamy nadzieję wykorzystać na udoskonalenie tego systemu, co oczywiście nastąpi za zgodą Wysokiej Izby. Bardzo dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Stwierdzam, że do głosu nie zgłosił się żaden reprezentant klubów i koła… Jest pan poseł Cieszyński. Otwieram dyskusję. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Janusz Cieszyński",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! To jest projekt, nad którym komisja obradowała wyjątkowo zgodnie. Wszystkie kluby poparły te zmiany. To są dobre zmiany na wniosek wszystkich zainteresowanych. One pozwolą tę usługę wdrożyć jeszcze lepiej, niż to byłoby możliwe w tym roku. Tak że sugeruję, żeby głosować za tym projektem. Dziękuję bardzo. (Oklaski) (Głos z sali: Panie marszałku, jeszcze…)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "W tej sprawie, tak? Jako przedstawiciel klubu? Bardzo proszę, panie pośle. Są zgłoszeni do głosu.",
                },
                {
                    "speaker": "Poseł Grzegorz Bernard Napieralski",
                    "content": "Panie Marszałku! Wysoka Izbo! Chciałem powiedzieć, że ta ustawa jest o tyle ważna, że tak naprawdę w czasie, kiedy świat bardzo się zmienia, nowe technologie i to wszystko, co tak naprawdę ma służyć Polkom i Polakom, jest bardzo istotne, to termin wdrożenia tego systemu był przekładany trzy razy Sprawozdanie Komisji Cyfryzacji, Innowacyjności i Nowoczesnych Technologii o poselskim projekcie ustawy o zmianie ustawy o doręczeniach elektronicznych I chciałem powiedzieć, że tutaj chodzi o bezpieczeństwo Polek i Polaków, bo od 1 stycznia ten system po prostu by nie zadziałał. Dzisiaj robimy wszystko, aby ten termin przełożyć. Nie odkładamy tego terminu na święte nigdy, dajemy czas ministrowi cyfryzacji i jego współpracownikom, aby bardzo dobrze przygotowali ten system, tak aby służył on Polkom i Polakom. Mam nadzieję, że dzisiaj po prostu to przegłosujemy. I jest też apel do pana prezydenta Andrzeja Dudy, aby jak najszybciej podpisał tę ustawę. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Pan poseł Paweł Śliz, Polska 2050 – Trzecia Droga. Proszę o zwięzłość, panie pośle.",
                },
                {
                    "speaker": "Poseł Paweł Śliz",
                    "content": "W imieniu klubu Polska 2050 chciałbym zwrócić uwagę, że ten projekt ustawy jest bardzo istotny. Wydaje mi się, że projekt jest ponadpartyjny, bo daje bezpieczeństwo niewystąpienia chaosu wśród przedsiębiorców, ale także wśród zawodów zaufania publicznego. Przesunięcie tego terminu daje możliwość przystosowania się przez operatora do zapewnienia warunków technicznych, dlatego w imieniu klubu Polska 2050 – Trzecia Droga deklaruję, że będziemy popierać ten projekt. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję. Pan poseł Michał Gramatyka chce jeszcze zabrać głos? (Wypowiedź poza mikrofonem) Nie musi pan. Pan poseł Adam Dziedzic, Polskie Stronnictwo Ludowe – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Adam Dziedzic",
                    "content": "Panie Marszałku! Wysoka Izbo! Szanowni Państwo! Projektowana zmiana umożliwia dalsze przesunięcie daty wdrożenia środków technicznych umożliwiających realizację przepisów tejże ustawy. Komisja pochyliła się nad tą kwestią. Te terminy muszą zostać przesunięte, dlatego że nie mamy dzisiaj gotowego systemu. Do tego w trakcie prac komisji, mając na względzie przede wszystkim spójność zmian, przesunięto również datę obowiązku utworzenia adresu do doręczeń w ramach publicznej usługi rejestrowanego doręczenia elektronicznego. Szanowni państwo, poprawka zabezpiecza również prawidłowość doręczeń korespondencji dla tych podmiotów, które już dokonały rejestracji e-skrzynek do doręczeń. Kierując się potrzebą ratowania sytuacji, rekomenduję, aby te poprawki przyjąć. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję. Pan poseł Adrian Zandberg z Lewicy. Zaraz po nim jako ostatni pan poseł Bartłomiej Pejo z Konfederacji.",
                },
                {
                    "speaker": "Poseł Adrian Zandberg",
                    "content": "Drodzy Państwo! Nie można oczywiście nakładać na obywateli obowiązku, kiedy państwo nie dostarczyło na czas systemu, który pozwoliłby im na wypełnienie tego obowiązku. Przyjmijmy szybko te poprawki i idźmy dalej. Jest już późno, nie czas na retoryczne popisy. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Pan poseł Bartłomiej Pejo, Konfederacja.",
                },
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "Panie Marszałku! Wysoka Izbo! Reprezentując klub parlamentarny Konfederacji, pragnę podkreślić nasze głębokie zaangażowanie w sprawy dotyczące cyfryzacji kraju i wyrazić nasze stanowisko. Kto ma rację dzień wcześniej od innych, ten przez dobę uchodzi za idiotę, jak mawiał Antoine de Rivaro. Konfederacja już 3 lata temu jako jedyna siła polityczna głosowała przeciwko pierwotnemu projektowi ustawy. Nasz przedstawiciel podnosił wówczas kwestie monopolu Poczty Polskiej i wątpliwości co do jej zdolności do efektywnego świadczenia usług elektronicznych. Nasze obawy, choć wówczas ignorowane, okazały się całkowicie słuszne. Obecnie stoimy przed koniecznością kolejnego już przesunięcia terminu wdrożenia środków technicznych przewidzianych ustawą, co jest świadectwem braku przygotowania i efektywności ze strony odpowiedzialnych instytucji. Chcemy podkreślić, że nie sprzeciwiamy się idei cyfryzacji administracji publicznej, wręcz przeciwnie, jesteśmy jej gorącymi zwolennikami. Cyfryzacja powinna iść ręka w rękę z racjonalizacją kosztów i usprawnieniem dostępu do usług publicznych dla wszystkich obywateli. Jednakże sposób, w jaki obecnie jest realizowana, rodzi szereg problemów i wątpliwości. Nowy system doręczeń elektronicznych przewiduje, Sprawozdanie Komisji Cyfryzacji, Innowacyjności i Nowoczesnych Technologii o poselskim projekcie ustawy o zmianie ustawy o doręczeniach elektronicznych że elektroniczne skrzynki podawcze ePUAP zostaną de facto zastąpione przez dwie usługi świadczone przez Pocztę Polską – publiczną usługę hybrydową oraz publiczną usługę rejestrowanego doręczania elektronicznego. Pierwsza z nich jest rozwinięciem tradycyjnych listów poleconych i wymaga ich fizycznego dostarczenia. Koszt tej usługi został ustalony na poziomie 6,95 zł netto za przesyłkę. Natomiast druga usługa, będąca usługą całkowicie cyfrową, obciążona jest opłatą 4,40 zł za przesyłkę, podczas gdy koszt doręczenia przez Pocztę Polską tradycyjnego listu papierowego wynosi 3,90 zł. Jak można uzasadnić to, że usługa elektroniczna – z natury tańsza i efektywniejsza – ma być droższa niż usługa tradycyjna? (Poseł Konrad Berkowicz: Kpina.) W sektorze prywatnym, gdzie istnieje konkurencja, koszt podobnej usługi to jedynie 1,79 zł netto. Widać więc wyraźnie, że monopol Poczty Polskiej nie tylko nie sprzyja efektywności ekonomicznej, ale wręcz prowadzi do nieuzasadnionego wzrostu kosztów. To stawia pod znakiem zapytania sens ekonomiczny takiej usługi, w szczególności gdy porównamy ją z tradycyjną pocztą elektroniczną czy elektroniczną skrzynką podawczą w ePUAP, która dotychczas była udostępniana nieodpłatnie przez administrację publiczną. Brakuje uzasadnienia tego, by e-usługa, która dotychczas była świadczona nieodpłatnie przez administrację publiczną, została przekształcona w odpłatną usługę oferowaną przez spółkę akcyjną w arbitralnie narzuconych cenach. Wysokość tych opłat może wynikać jedynie z nieefektywności ekonomicznej spółek zarządzanych przez Skarb Państwa oraz zagwarantowanego przez ustawę monopolu. Niniejszy projekt nowelizacji ustawy wskazuje na kolejne przesunięcie terminu wdrożenia e-doręczeń. Czy to nie jest dowód na to, że Poczta Polska – mimo przyznanego jej monopolu – nie jest przygotowana na takie zadanie? Warto przypomnieć, że Komitet Ekonomiczny Rady Ministrów na wniosek ministra cyfryzacji wybrał wariant monopolu właśnie Poczty Polskiej na doręczenia elektroniczne i ten wariant obowiązuje już od 5 lat. Po ponad 5 latach od podjęcia tamtej decyzji stajemy przed faktem, że monopolista nie jest w stanie wdrożyć tych usług. Dodatkowo należy podkreślić szereg istotnych wątpliwości dotyczących efektywności i bezpieczeństwa świadczenia usług doręczeń elektronicznych przez Pocztę Polską. Po pierwsze, istnieje realne ryzyko dalszych opóźnień i problemów technicznych wynikające z braku doświadczenia tej instytucji w zarządzaniu skomplikowanymi systemami elektronicznymi. Po drugie, monopol Poczty Polskiej może znacząco ograniczyć wprowadzenie nowoczesnych, innowacyjnych rozwiązań oraz adaptację do dynamicznie zmieniających się potrzeb i oczekiwań użytkowników. Po trzecie, musimy brać pod uwagę potencjalne ryzyko naruszenia bezpieczeństwa danych, co może być spowodowane lukami w infrastrukturze IT Poczty Polskiej oraz brakiem odpowiednich kompetencji w zakresie cyberbezpieczeństwa. Na koniec, monopolistyczna pozycja Poczty Polskiej prowadzi do nieefektywności ekonomicznej manifestującej się w wyższych kosztach operacyjnych, które ostatecznie obciążają użytkowników usług. Te aspekty wskazują na pilną potrzebę (Oklaski) przemyślenia i restrukturyzacji obecnego modelu świadczenia usług doręczeń elektronicznych, aby służyły one w pełni interesom obywateli i były zgodne z zasadami efektywności oraz nowoczesności. Naszym zdaniem usługa powinna zostać przejęta, utrzymywana i świadczona bezpłatnie przez administrację publiczną na zasadach podobnych do innych usług, w tym (Dzwonek) do dotychczasowych skrzynki podawczej ePUAP. Taka zmiana pozwoli na lepszą integrację ze środowiskiem aplikacji mObywatel oraz z innymi e-usługami, tworząc koherentne środowisko dostępu do e-administracji. (Oklaski) (Głos z sali: Brawo!)",
                },
                {"speaker": "Marszałek", "content": "Panie pośle, czas minął."},
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "Proponujemy też, aby świadczenie usług hybrydowych, które wymagają fizycznego dostarczenia wydrukowanych listów, było możliwie także przez inne podmioty gospodarcze…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, nie sądziłem, że przy takim punkcie porządku dziennego będę komuś wyłączał mikrofon, ale naprawdę proszę zmierzać do brzegu.",
                },
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "Już zmierzam, panie marszałku. Obowiązek świadczenia tej usługi przez Pocztę Polską powinien zostać zlikwidowany, a cena takiej usługi ustalona na zasadach wolnej konkurencji. W kontekście procedowanej ustawy uważamy, że Poczta Polska nie powinna mieć zagwarantowanego ustawowego monopolu na świadczenie tych usług… (Głos z sali: Niech pan nie krzyczy.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziesięć, dziewięć… Sprawozdanie Komisji Cyfryzacji, Innowacyjności i Nowoczesnych Technologii o poselskim projekcie ustawy o zmianie ustawy o doręczeniach elektronicznych. Oświadczenia poselskie",
                },
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "…ani teraz, ani za rok, ani nigdy. (Oklaski) (Głos z sali: Brawo!)",
                },
                {"speaker": "Marszałek", "content": "…osiem, siedem, sześć…"},
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "Przedłużenie tego terminu wdrożenia systemu…",
                },
                {"speaker": "Marszałek", "content": "…pięć, cztery…"},
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "…powinno być więc wykorzystywane…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "…trzy, dwa, jeden. (Głos z sali: Koniec!)",
                },
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "…do przygotowania zrewidowanego całego systemu doręczeń… (Marszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Zamykam dyskusję. (Głos z sali: Bis! Bis!) Bisów nie przewidujemy. Przystępujemy do trzeciego czytania. Komisja wnosi o uchwalenie projektu ustawy z druku nr 94. Przystępujemy do głosowania. Kto z pań i panów posłów jest za przyjęciem w całości projektu ustawy w brzmieniu z druku nr 94, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 448 posłów. Za – 431, przeciw – 12, wstrzymało się 5. Stwierdzam, że Sejm uchwalił ustawę o zmianie ustawy o doręczeniach elektronicznych. (Oklaski) Na tym zakończyliśmy rozpatrywanie punktów porządku dziennego zaplanowanych na dzień 12 grudnia 2023 r. Informuję państwa, że zgodnie z decyzją Konwentu Seniorów nie będziemy w dniu dzisiejszym procedować nad uchwałą zgłoszoną przez klub Lewicy. (Głos z sali: Uuu…) Jesteśmy głęboko przekonani jako większość, nie całość, przyznaję, Konwentu Seniorów, że wywołałaby ona dzisiaj, przy tym poziomie emocji na sali, ten poziom emocji i ten poziom podziałów, nie co do samej zasady i oceny tego, co się stało, ale co do wątków pobocznych, którego nie chcemy i którego powinniśmy uniknąć. (Oklaski) (Głos z sali: Bo była poprawka.) Spotkajmy się, jeżeli taka będzie państwa wola, jutro, przy zapaleniu świeczek chanukowych po raz kolejny w gmachu Sejmu. (Poseł Michał Wójcik: Wniosek formalny.) Zaraz panu wyjaśnię, panie pośle Wójcik. Ogłaszam 30 minut przerwy, po której posłowie, którzy zgłosili się do wygłoszenia oświadczeń poselskich, będą mieli taką szansę. Dziękuję państwu bardzo.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Wznawiam obrady. Informuję, że zgłosili się posłowie w celu wygłoszenia oświadczeń poselskich. Czy ktoś z pań i panów posłów pragnie jeszcze wygłosić oświadczenie? Nikt się nie zgłasza. Zamykam listę. Ustalam czas na wygłoszenie oświadczenia na 1 minutę. Bardzo proszę pana posła Szymona Giżyńskiego. (Wypowiedź poza mikrofonem) Na 1 minutę. Wszyscy mamy dosyć, proszę państwa. (Głos z sali: Marszałek nie jest hojny.) Nie jest hojny, ale może jest mądry. Naprawdę siedzimy tu od godz. 7 rano. Jest pan poseł Giżyński? (Poseł Szymon Giżyński: Jestem, jestem. Byłem zapisany jako jedenasty, a jestem pierwszy.) Dla mnie zawsze jest pan pierwszy. Proszę bardzo.",
                },
                {
                    "speaker": "Poseł Szymon Giżyński",
                    "content": "Dziękuję bardzo. Wysoki Sejmie! Największe osiągnięcie w ostatnich dniach koalicji 15 października sposobiącej się poselskie do przejęcia władzy w Polsce znakomicie oddaje parafraza niewielkiego fragmentu wiersza Cypriana Kamila Norwida „Epos – nasza”: Partia różnolica podmieniła wiatraki z la Manczy szlachcica. Dziękuję uprzejmie.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Tadeusz Tomaszewski, Lewica. Dziękuję. Pani posłanka Paulina Matysiak, Lewica. Proszę.",
                },
                {
                    "speaker": "Poseł Paulina Matysiak",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Chciałabym poruszyć bardzo ważny temat związany z otrzymywaniem informacji przez podróżujących koleją, bo w ostatnich dniach były z tym bardzo częste problemy. Tej kwestii było poświęcone posiedzenie Komisji Infrastruktury. Natomiast to nie jest tak, że to jest problem, który pojawił się w ostatnich dniach i który jest problemem jednostkowym, bo pojawia się bardzo często. Chciałabym powiedzieć, że każdy pasażer, niezależnie od tego, w jakim regionie Polski podróżuje, na jakiej trasie, z usług jakiego przewoźnika korzysta, zasługuje na to, żeby w sytuacji opóźnienia, czy to spowodowanego ze strony zarządcy infrastruktury, ze strony przewoźnika, czy też po prostu losowymi zdarzeniami, mógł otrzymać tę informację na czas na dworcu, na peronie. Jest z tym bardzo duży kłopot. Tak nie powinno to wyglądać. I myślę, że w kwestii tego, jak działa aplikacja: Portal pasażera, jeszcze się zgłoszę z jakimś oświadczeniem. Bardzo dziękuję. (Dzwonek) Dobranoc, panie marszałku.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, pani posłanko. Dobranoc, życzę miłych snów. Pan poseł Fryderyk Sylwester Kapinos, Prawo i Sprawiedliwość. Nie ma. Pan poseł Łukasz Kmita, Prawo i Sprawiedliwość. Nie ma. Pan poseł Zbigniew Bogucki. (Poseł Fryderyk Kapinos: Jestem.) Przepraszam, panie pośle, pan Kapinos był pierwszy. W ostatniej chwili wpadł. Czekaliśmy na pana, panie pośle. (Poseł Fryderyk Sylwester Kapinos: Ile minut?) Minutka. Jeżeli chce pan zrezygnować, nie ma problemu. Jest pan poseł Kmita. (Poseł Fryderyk Sylwester Kapinos: Nie, nie chcę. Ale może mi pan marszałek troszeczkę wydłużyć…) Nie, 1 minuta. I już panu leci czas, 7 sekund poszło. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Fryderyk Sylwester Kapinos",
                    "content": "Panie Marszałku! Wysoka Izbo! Misericors – tak brzmi nazwa honorowego wyróżnienia, które przyznaje Caritas Diecezji Tarnowskiej. Jest ono uhonorowaniem działalności na rzecz ubogich i cierpiących, wsparcia ludzi w potrzebie oraz postawy pełnej chrześcijańskiego miłosierdzia. Bardzo się cieszę, że na zorganizowanej przeze mnie II Mieleckiej Gali Wolontariatu zastępca dyrektora Caritas Diecezji Tarnowskiej ks. Krzysztof Majerczak i sekretarz Caritas Diecezji Tarnowskiej Jerzy Pikul wręczyli honorowe wyróżnienia Misericors, które otrzymali: ks. Adam Bezak, wikariusz w parafii pw. Najświętszej Marii Panny Królowej Polski w Dobryninie, organizator zbiórek darów dla potrzebujących (Dzwonek), ks. Jan Tomczyk, proboszcz parafii pw. św. Wojciecha w Trześni…",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle.",
                },
                {
                    "speaker": "Poseł Fryderyk Sylwester Kapinos",
                    "content": "…zaangażowany w pomoc seniorom, chorym, niepełnosprawnym. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Super, dziękuję. Pan poseł Łukasz Kmita, Prawo i Sprawiedliwość. Nie ma posła Kmity. Pan poseł Zbigniew Bogucki, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Zbigniew Bogucki",
                    "content": "Panie Marszałku! Wysoki Sejmie! Na początku tej dzisiejszej debaty, ważnej debaty przed powołaniem nowego rządu Donald Tusk obiecał, że odpowie na wszystkie pytania wszystkich posłów. Co się stało później? Nie odpowiedział na żadne pytanie, nie tylko na moje pytania, nie tylko na pytania posłów Prawa i Sprawiedliwości, ale nie odpowiedział również na państwa pytania, pytania swoich posłów, pytania swoich koalicjantów. To pokazuje nie tylko to, jak traktuje Prawo i Sprawiedliwość, ale również to, jak poselskie 773 traktuje państwo, jak traktuje wyborów. Nie chciał odpowiedzieć na żadne z tych pytań. I niestety pomógł mu w tym również pan marszałek Hołownia, który bardzo elastycznie, mówiąc eufemistycznie, potraktował regulamin. Jeżeli nie miało być odpowiedzi na te pytania i taka była procedura w regulaminie, to po co te pytania były zadawane, po co te godziny zadawania pytań zarówno z lewej, jak i z prawej strony? Szanowni Państwo! Niestety bardzo źle zaczynacie. (Dzwonek) Pan premier Tusk rozpoczyna od złamania obietnicy. Dziękuję bardzo.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Bardzo miło, dziękuję. Ponieważ jestem wicemarszałkiem Sejmu, skomentuję to. Użył pan nazwiska pana marszałka Szymona Hołowni. Pan marszałek Szymon Hołownia wszystko zrobił w tej sprawie zgodnie z regulaminem. (Poseł Zbigniew Bogucki: Nie zgadzam się.) Państwo powołaliście się na inną procedurę i na inny punkt. Państwo się powołaliście na pierwszy krok, a to był drugi krok. Dziękuję serdecznie. Pani poseł Renata Urszula Rak, Koalicja Obywatelska. (Wypowiedź poza mikrofonem) Proszę pana, skończyłem w tej sprawie, tak? Bardzo proszę, pani poseł.",
                },
                {
                    "speaker": "Poseł Renata Urszula Rak",
                    "content": "Panie Marszałku! Wysoka Izbo! Rząd premiera Morawieckiego nie otrzymał mojego wotum zaufania za upartyjnienie mediów publicznych, za hejt i mowę nienawiści, za kamuflowanie wydatków partyjnych poprzez programy willa+ czy referendum, za upolitycznienie szkół, wprowadzenie podręcznika do HIT-u, nośnika światopoglądu PiS-u, a nie rzetelnej wiedzy, za pogardę dla kobiet, którą widzieliśmy wielokrotnie, którą pokazała komisja spraw poselskich i immunitetowych powołana w związku ze słowami Jarosława Kaczyńskiego, że kobiety zamiast rodzić dzieci, dają w szyję. Posłowie PiS-u, próbując udowodnić, że Kaczyński szanuje kobiety, obrażali, poniżali i wyśmiewali autorkę wniosku o uchylenie immunitetu. Nie ma zgody ani przyzwolenia na brak szacunku dla drugiego człowieka. Moją obecność w Sejmie zawdzięczam swoim wyborcom, ale także pośrednio wam, posłowie PiS-u, i waszym rządom, które były pełne buty i arogancji. Dlatego powiedzieliśmy: dość, dość rządów bezprawia. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Adrian Witczak, Koalicja Obywatelska.",
                },
                {
                    "speaker": "Poseł Adrian Witczak",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Odejść też trzeba umieć. Okazanie szacunku prawie 12 milionom naszych rodaków, którzy 15 października powierzyli odpowiedzialność za losy Rzeczypospolitej Polskiej demokratycznej opozycji, to był święty obowiązek odchodzącej elity władzy. Zamiast tego nastąpiła miesięczna próba odwracania wyniku wyborów. Jednak nadszedł ten piękny poniedziałek 11 grudnia 2023 r. To dzień, który przejdzie do historii. To dzień, w którym prawda zwyciężyła z kłamstwem, w którym żegnamy się z ignorancją i arogancją, w którym wraca wrażliwość i szacunek do innych ludzi. Szanowny Panie Premierze! Jako przedstawiciel młodego pokolenia, nauczyciel i były radny odetchnąłem z ulgą. Jestem spokojny, bo wiem, że polska szkoła będzie miejscem przyjaznym i otwartym, że będzie miejscem, które tworzyć będą uczniowie, rodzice i (Dzwonek) nauczyciele, a nie pełny nienawiści minister Czarnek. Jestem spokojny, bo wiem, że samorządy przestaną być drenowane przez rząd i będą mogły samodzielnie podejmować decyzje. Szczęśliwej Polski już czas. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Andrzej Tomasz Zapałowski, Konfederacja. Nie ma. Pan poseł Norbert Jakub Kaczmarczyk, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Norbert Jakub Kaczmarczyk",
                    "content": "Bardzo dziękuję. Szanowny Panie Marszałku! Wysoka Izbo! Chciałbym bardzo serdecznie podziękować rządowi pani premier Beaty Szydło oraz panu premierowi Mateuszowi Morawieckiemu za wiele lat pracy na rzecz Polski, na rzecz Polski A, Polski bez podziałów, za wielką współpracę również na rzecz Polski powiatowo-gminnej. Chciałbym podziękować również mojemu szefowi, panu ministrowi Zbigniewowi Ziobrze za wiele lat pracy na rzecz budowania i odbudowy wymiaru sprawiedliwości po komunie. Bardzo się cieszę, że te wiele lat przyniosło tak naprawdę bardzo wiele wspaniałych projektów obywatelskich, ale też projektów, które powodowały, że obywatele z małych miejscowości mogli poczuć się poselskie 774 docenieni. Gminy, które miały na inwestycje tylko kilkaset tysięcy albo kilka milionów złotych, korzystały z wielomilionowych dotacji. Często były to gminy zarządzane przez samorządowców z państwa strony, więc cieszymy się i mamy nadzieję (Dzwonek), że przyszły rząd również będzie dzielił pieniądze równo i nie będzie kategoryzował Polaków, nie będzie dzielił Polski na Polskę A i Polskę B. Bardzo dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Mariusz Krystian, Klub Parlamentarny Prawo i Sprawiedliwość. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Mariusz Krystian",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Miałem wygłosić oświadczenie o wielkiej pozytywnej rewolucji komunikacyjnej w Małopolsce, ale nie sposób tego zrobić w minutę. Panie Marszałku! Wiem, że siedzimy tutaj od rana, ale proszę mi wierzyć, miliony Polaków pracują po 8 godzin, 10 godzin, 12 godzin dziennie. Miliony Polaków pracują w systemie zmianowym, pracują w systemie 12 godzin na 24 godziny lub 24 godziny na 48 godzin.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Już minęło panu 20 sekund.",
                },
                {
                    "speaker": "Poseł Mariusz Krystian",
                    "content": "To nic dziwnego. Jest raptem 22.46. Oświadczenia mogą trwać 2 minuty. Można wtedy spokojnie wygłosić oświadczenie, poseł może powiedzieć to, co ma na myśli. Panie Marszałku! Proszę o refleksję. Proszę umożliwić posłom pracę parlamentarną. Dziękuję bardzo.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję, panie pośle. Dzisiaj usiądę i przemyślę pana słowa, pewnie są słuszne. (Głos z sali: Panie marszałku, do czasu COVID-19 oświadczenia trwały 5 minut…) Trzeba było się wtedy zgłaszać. Pan poseł Marcin Romanowski, Klub Parlamentarny Prawo i Sprawiedliwość. Czy ma pan zamiar zabrać głos czy nie? Jeżeli nie, to pan poseł Bartosz Zawieja, Koalicja… Ma pan ochotę, tak? No to proszę. Na co pan czeka?",
                },
                {
                    "speaker": "Poseł Marcin Romanowski",
                    "content": "Bardzo dziękuję, panie marszałku, za ten czas. Wysoka Izbo! Przeszło 2 tygodnie temu, 28 listopada, minęła kolejna rocznica jednego z najtragiczniejszych wydarzeń w XX-wiecznej historii Polski. Mowa tu o powstaniu zamojskim, drugim co do wielkości akcie zorganizowanego oporu wobec niemieckiego okupanta w czasie II wojny światowej. Przez lata pamięć o powstaniu zamojskim i porwanych przez Niemców dzieciach, Dzieciach Zamojszczyzny, żyła wśród mieszkańców województwa lubelskiego. Teraz jest pora, aby stała się powszechna w całej Polsce. Ma temu służyć zgłoszony przez grupę posłów projekt ustawy o ustanowieniu Narodowego Dnia Powstania Zamojskiego i Pamięci Dzieci Zamojszczyzny, który jest też realizacją mojego zobowiązania wobec mieszkańców regionu. Mam nadzieję, że wszystkie kluby parlamentarne, wszyscy posłowie poprą ten projekt, który tworzy pamięć o tym ważnym (Dzwonek) wydarzeniu w historii naszej ojczyzny. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Bardzo dziękuję, panie pośle. Pan poseł Bartosz Zawieja, Koalicja Obywatelska. Nie ma. Pani poseł Izabela Bodnar, Polska 2050 – Trzecia Droga. Zapraszam.",
                },
                {
                    "speaker": "Poseł Izabela Bodnar",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! 15 października polskie społeczeństwo głośnym, wielomilionowym chórem powiedziało: dość władzy dewastującej demokrację i wolności obywatelskie. Dzisiaj wraz z powołaniem nowego rządu pod batutą premiera Donalda Tuska z doskonałym koalicyjnym partnerstwem koalicji 15 października Polska staje na progu odrodzenia, nowej ery opartej na fundamentach prawdy, otwartości i współpracy. To moment, w którym otwieramy drzwi ku przyszłości, ale musimy wyciągnąć lekcję, wszczepić w naszą demokrację, która została pokaleczona ostatnimi 8 latami, odpowiednią dawkę przeciwciał, żeby ta choroba nam się więcej nie przytrafiła. Przeżywam obalanie totalitaryzmu w swoim życiu po raz trzeci. Nie chcę już tego więcej przeżywać. Musimy zakopać podziały społeczne, scementować wspólnotę, rozliczyć winnych łamania prawa, żeby odbudować zdrową poselskie 775 tkankę społeczną i zaufanie do państwa (Dzwonek), doprowadzić do odrodzenia Polski, przywrócić zgodę, uśmiech, tolerancję i przyjaźń. Nowy rząd we współpracy z parlamentem będzie potrafił sobie świetnie z tym poradzić. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Dariusz Marek, Koalicja Obywatelska. O, przepraszam, pan poseł Dariusz Matecki. Czy coś się stało? Coś pomóc? (Poseł Dorota Marek: Nie, spokojnie.) Przepraszam, panie pośle. Pan poseł Dariusz Matecki.",
                },
                {
                    "speaker": "Poseł Dariusz Matecki",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Dzisiaj Lewica zgłosiła projekt uchwały potępiającej antysemityzm. Bardzo chętnie poparłbym tę uchwałę, gdyby dopisać do tego projektu uchwały również potępienie chrystianofobii. Również chrystianofobii wśród posłów Lewicy. Np. pani Joanna Scheuring-Wielgus zakłócała mszę św. Wszyscy widzieli jej polityczny happening w kościele podczas mszy św. Chodzi o to, by m.in. potępić chrystianofobię pana posła Nitrasa, który teraz został ministrem, a wcześniej mówił o opiłowywaniu katolików. Potępić zrobienie sobie zdjęcia przez premiera Donalda Tuska z panią Martą Lempart, która wzywała na ulicach polskich miast do tego, żeby palić kościoły. Krzyczała: Dym w kościołach. Z takimi ludźmi premier polskiego rządu już w tej chwili robił sobie zdjęcia. Apelujemy również do marszałka Hołowni, żeby pilnie procedować nad projektem uchwały w obronie chrześcijan, gdzie zebraliśmy prawie 0,5 mln podpisów, który rzeczywiście broni (Dzwonek) chrześcijan, a także innych wyznawców religii. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo. Pani poseł Dorota Marek, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Dorota Marek",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Partia Prawo i Sprawiedliwość to partia odwróconych znaczeń. Prawo zamienia w bezprawie, sprawiedliwość w niesprawiedliwość i nawet exposé, które zwykle premierzy wygłaszali na początku kadencji, pan Morawiecki wygłosił na jej końcu. W sumie nie powinno nas to dziwić. Ostatnim i chyba jedynym osiągnięciem 14-dniowego rządu było odmienianie przez wszystkie przypadki słowa „lobby”. Ale wiemy, opanowali to do perfekcji. Pytam dziś partię PiS: Kto u was lobbował za tym, żeby przeprowadzić wybory kopertowe i w nielegalny sposób pozyskać dane wyborców z gminnych baz PESEL? Kto lobbował za tym, żeby założyć Pegasusa głównym politykom opozycji, a nie terrorystom? I na koniec: Kto lobbował za tym, żeby wizy sprzedawać na targach i bazarach? Straszyliście uchodźcami (Dzwonek), a jednocześnie wpuściliście nie tylko do Polski, ale do strefy Schengen ludzi, którzy nigdy nie zostali poprawnie zweryfikowani, za to mieli grube portfele, aby zapłacić za możliwość wjazdu do zachodniego świata.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pani poseł, wyjaśnimy to w komisjach śledczych. Pani poseł Karolina Pawliczak, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Karolina Pawliczak",
                    "content": "Panie Marszałku! Wysoka Izbo! Wszyscy wierzyliśmy w zwycięstwo, które dokonuje się na naszych oczach, bo na naszych oczach dokonuje się zmiana. Ja bardzo cieszę się, że pan premier w swoim exposé mówił tak wiele o infrastrukturze, bo występuję tutaj w imieniu tysięcy mieszkańców Kalisza, ale i części regionu południowej Wielkopolski w sprawie obwodnicy Kalisza, której PiS przez blisko dekadę, mimo że obiecał, nie potrafił wybudować. Pięciu ministrów z okręgu, nieustanna, pusta, tępa propaganda i nic poza tym. Kiedy 4 lata temu przy exposé mówiłam o tym panu Morawieckiemu, miałam wrażenie, że szuka w telefonie na mapie Polski Kalisza. Przypomnę, najstarszego miasta w Polsce. To jedna z waszych PiS-owskich niespełnionych obietnic, bo i program 100 obwodnic został tylko pustym sloganem. Dlatego m.in. straciliście, nieudacznicy, władzę, bo nie spełniliście oczekiwań i zawiedliście na całej linii. Cały region czeka na tę inwestycję po waszych rządach, bo poza skonfliktowaniem (Dzwonek) społeczeństwa niewiele zrobiliście. Wierzę, że w tej kadencji ta sprawa wreszcie się dokona. Jednocześnie deklaruję swoje pełne zaangażowanie w tę priorytetową dla regionu sprawę. Pokażemy, jak należy wypełniać zobowiązania. Dziękuję. (Oklaski) poselskie 776",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję bardzo, pani poseł. Pan poseł Łukasz Ściebiorowski, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Łukasz Ściebiorowski",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Jako poseł ziemi śląskiej wyrażam zadowolenie z faktu, że Ministerstwo Przemysłu na czele z panią minister Marzeną Czarnecką, zgodnie z zapowiedzią premiera i dzisiejszą naszą decyzją, tzw. koalicji 15 października, powstanie na Śląsku. Zwłaszcza w kontekście wyzwań, jakie stoją przed regionem i województwem śląskim, zarówno w obszarze górnictwa, rozwoju technologicznego, jak i zagospodarowania terenów poprzemysłowych, zgodnie z oczekiwaniami lokalnych samorządów, które liczą, że na powrót staną się partnerem dla rządu, a nie obszarem politycznego zainteresowania służb specjalnych i prokuratury, bo takie przypadki były, jak to działo się też w ostatnich latach. Musimy wesprzeć samorządy również w bardzo wielu innych obszarach jak np. finansowanie służby zdrowia, edukacji, bo dziś to samorządy ponoszą ogromne koszty realizacji tych zadań. Istotna jest również rozbudowa infrastruktury sportowej, w tym m.in. budowa nowego stadionu Ruchu Chorzów, ale też innych lokalnych obiektów sportowych. Nowemu rządowi (Dzwonek) chciałem przekazać życzenia powodzenia, tak jak to się mówi na Śląsku, takim zwrotem: Panie Premierze! Rządzie! Patrzcie tam jako, patrzcie tam jako. Dziękuję, panie marszałku. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Nie wiem, jak się odpowiada na to, ale gdybym wiedział, tobym panu odpowiedział. Pan poseł Tadeusz Woźniak, Klub Parlamentarny Prawo i Sprawiedliwość. (Głos z sali: Nie ma.) Pan poseł Tadeusz Samborski, PSL – Trzecia Droga. Witam, Tadeuszu. Zapraszam.",
                },
                {
                    "speaker": "Poseł Tadeusz Samborski",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Kilka dni temu w Centralnej Bibliotece Rolniczej w Warszawie odbyła się piękna uroczystość 95. rocznicy utworzenia Związku Młodzieży Wiejskiej RP „Wici”. Przypomnę, że w szeregach tej organizacji działał m.in. Józef Ulma, głowa niedawno beatyfikowanej rodziny zasłużonej w szlachetnym dziele ratowania Żydów w okrutnych czasach Holokaustu. Dzisiaj współczesnym spadkobiercą tej organizacji jest Związek Młodzieży Wiejskiej kierowany przez Adama Nowaka. W statucie tej organizacji jest m.in. takie piękne zdanie: przygotowanie młodzieży wiejskiej do wykonywania obowiązków i uprawnień obywatelskich we wszystkich dziedzinach życia społecznego, kulturalnego i gospodarczego. A hymnem tej organizacji są piękne słowa: Do niebieskich pował od grud czarnej ziemi,/ Już się sztandar nasz wiciowy kolorami mieni./ Pod sztandarem naszym kwitnie wiara (Dzwonek) chłopska,/ Cała ziemia za nim ruszy, pójdzie żywa Polska. Dziękuję bardzo. Dziękuję, panie marszałku. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję, drogi Tadeuszu. Pan poseł Andrzej Grzyb PSL – Trzecia Droga. Dziękuję bardzo. (Poseł Karolina Pawliczak: Brawo!)",
                },
                {
                    "speaker": "Poseł Andrzej Grzyb",
                    "content": "Panie Marszałku! Wysoka Izbo! Jutro mamy dzień 13 grudnia. Jest to rocznica stanu wojennego, ale też w historii ruchu ludowego jest to ważna data, ponieważ 13 grudnia 1966 r. zmarł premier Stanisław Mikołajczyk, prezes Polskiego Stronnictwa Ludowego na uchodźstwie, ale również odrodzonego w 1945 r. Premier rządu po śmierci gen. Sikorskiego, ale też wcześniej powstaniec wielkopolski, żołnierz wojny bolszewickiej, żołnierz września i człowiek, który przeszedł wraz z całą rzeszą Polaków tę uchodźczą gehennę, ale też nigdy nie zawahał się marzyć o wolnej Polsce. To się niestety nie stało w jego pamięci, ponieważ, mimo że był wicepremierem rządu tymczasowego, to jednak jego polityka nie znalazła aprobaty władz komunistycznych. Musiał uciekać z Polski. (Dzwonek) Zmarł na uchodźstwie, a całą tę historię opisał w książce „Polska zgwałcona”, która została przetłumaczona na siedem języków, „The Rape of Poland”, co było też przestrogą w sprawie. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pan poseł Bartosz Romowicz, Polska 2050.",
                },
                {
                    "speaker": "Poseł Bartosz Romowicz",
                    "content": "Szanowny Panie Marszałku! Panie Posłanki! Panowie Posłowie! Od wielu lat jako burmistrz Ustrzyk poselskie 777 Dolnych aktywnie działałem w środowisku młodego samorządu, czyli osób, które nawet czasem fanatycznie były oddane służbie swojej lokalnej społeczności, osób, które szły do samorządu nie dla wielkiej polityki. Ci ludzie, młodzi samorządowcy, oddali młode lata, chcąc zmieniać swoje najbliższe otoczenie. Sytuacja w samorządach w Polsce z roku na rok staje się coraz gorsza i o ile da się wygospodarować środki na inwestycje, o tyle ze środkami bieżącymi jest duży problem. Do wydatków bieżących zaliczają się również pensje dla nauczycieli, pracowników oświaty czy koszty utrzymania budynków. Każdy wie, że potrzebna jest podwyżka dla nauczycieli, bo nauczyciele od wielu lat byli marginalizowani. Pojawia się jednak wiele znaków zapytania, a nawet lęków dotyczących sposobu finansowania tego wydatku. W imieniu samorządowców przypominam, że to środowisko w znacznej części oparło się potrzebie organizacji wyborów kopertowych, wspomogło państwo w pandemii COVID, a także przeżyło reformę byłego ministra Przemysława (Dzwonek) Czarnka. Panie Premierze! Proszę pana o to, aby uwzględnić przy podwyżkach dla nauczycieli, że samorządy muszą otrzymać całość środków na podwyżki do swojego budżetu. Dziękuję bardzo.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie, panie pośle. Pani poseł Iwona Małgorzata Krawczyk, Koalicja Obywatelska. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Iwona Małgorzata Krawczyk",
                    "content": "Panie Marszałku! Wysoka Izbo! Dwa dni, dwa exposé, dwóch premierów. Odniosę się do exposé premiera Morawieckiego, który wiedząc, że odchodzi, zapomniał przeprosić. Zapomniał przeprosić Polaków za państwo PiS z PowerPointa, za gest posłanki Lichockiej, za wybuch granatnika w siedzibie Komendy Głównej Policji, za okładanie pałkami protestujących, za rakietę, za zdetronizowanie Polski na arenie międzynarodowej, za szarego człowieka i szkołę Czarnka. I mamy exposé premiera Donalda Tuska, który odpowiedzialnie utworzył nowy, demokratyczny rząd, wypełniając wolę rodaków wyrażoną 15 października 2023 r. Nadszedł kres okładania kobiet pałkami, wciągania do radiowozów, koniec klauzuli dla ludzi bez sumień. (Dzwonek) Koniec kobiecych ofiar. To koniec wstydu polskich uczniów i nauczycieli za ministra Czarnka. Koniec mentalnego średniowiecza w polskiej szkole i polskim państwie. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję serdecznie. Pan poseł Włodzimierz Skalik, Konfederacja. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Włodzimierz Skalik",
                    "content": "Panie Marszałku! Wysoka Izbo! Szanowni Państwo! Dzisiaj byliśmy poruszeni tym, co wydarzyło się na terenie Sejmu. Chciałbym tytułem uzupełnienia, bo opinia publiczna powinna również o tym fakcie wiedzieć, że na terenie Sejmu obok roll upu Chabad Lubawicz, oddziału warszawskiego był wizerunek rabina Menachema Mendla Schneersona. Rabin ten zasłynął stwierdzeniem… Ja tylko podaję fakty, państwo sami ocenicie. Rabin ten stwierdził swego czasu: osoba Żyda jest czymś całkowicie różnym od innych narodów świata. Dusza nieżydowska pochodzi ze sfer szatańskich, podczas gdy dusza Żyda ma pochodzenie święte. Dziękuję bardzo, panie marszałku.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "A pan Braun to jest z jakiego klubu? (Poseł Włodzimierz Skalik: Panie marszałku, myślę, że pan dobrze wie.) A pan wie? Z Konfederacji. Pan też jest z Konfederacji. Super. Pan Jarosław Wałęsa, poseł Koalicji Obywatelskiej. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Jarosław Wałęsa",
                    "content": "Dziękuję, panie marszałku. Trzeba się cieszyć z tego, że tylko po 58 dniach od wyborów mamy w końcu rząd. Cieszmy się z tego, naprawdę cieszmy się z tego, to jest wspaniała zdobycz. Powoli ludzie tracili nadzieję. Naprawdę można było oczekiwać najgorszych rzeczy z PiS-u, że zaczną kombinować, tak żeby tego rządu nigdy nie było. Nawet dzisiaj próbowali odraczać. Wiedzieli dobrze, że pan prezydent Duda umówił się już na zaprzysiężenie o godz. 9 jutro, ale nie, jeszcze chcieli to przesuwać. Tymczasem się udało. Chciałem się po prostu cieszyć z tego powodu. Ale niestety nie da się nie zauważyć sprawy, która dzisiaj wyniknęła. Grzegorz Braun jednak zrobił rzecz straszną, tak straszną, że mam nadzieję, że zostanie pociągnięty do odpowiedzialności, że straci mandat. Ale zanim to nastąpi, to jednak upłynie trochę czasu, więc zastanawiam się, czy powinniśmy się czuć bezpieczni. Ten człowiek jest zdolny do wszystkiego. Jeżeli nie będzie się zgadzał z naszą opinią, ktoś się wyrazi tutaj w sposób, który będzie przeczył poselskie 778 jego ideałom, to czy nagle nie wyciągnie jakieś broni (Dzwonek) i nie zagrozi naszemu zdrowiu i życiu. Więc, panie marszałku, chciałbym też zwrócić uwagę, że powinniśmy maksymalnie ograniczyć jego wstęp do Wysokiej Izby, dopóki nie straci tego mandatu. (Oklaski)",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Dziękuję za radę, dziękuję, panie pośle. Dziękuję, drogi Jarosławie. Pan poseł Waldemar Andzel, Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Waldemar Andzel",
                    "content": "Panie Marszałku! Wysoka Izbo! Dzisiejsze oświadczenie mam na temat rzeczywistego stanu ubóstwa w Polsce. Bardzo proszę o niekłamanie i o nieprzekręcanie faktów na temat ubóstwa w Polsce. Wstydu nie mają ci, którzy wytykają nam, że nie dbamy o dzieci, o osoby niepełnosprawne i seniorów. Przypomnę, że za rządów PO i PSL przybyło Polaków żyjących w skrajnej biedzie. Czy państwo w ogóle wiedzą, co to jest? Najwyraźniej nie, bo dla was istnieją tylko dwie kategorie społeczeństwa: plebs i członkowie Platformy Obywatelskiej. Naprawdę nie podczepiajcie się pod nasze programy społeczne i wielkie osiągnięcia. Spróbujcie sami coś zrobić dla zwykłych ludzi, a nie dla siebie. Mam nadzieję, że niedługo okaże się to wszystko, co mówię, i Prawo i Sprawiedliwość wygra i wróci do władzy. Dziękuję bardzo.",
                },
                {
                    "speaker": "Wicemarszałek Włodzimierz Czarzasty",
                    "content": "Na tym zakończyliśmy oświadczenia poselskie*). Panie i panowie posłowie, informuję, że pierwsze posiedzenie Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego odbędzie się w dniu 19 grudnia br. o godz. 10, a nie w dniu 13 grudnia br. o godz. 11. Zarządzam przerwę w posiedzeniu do dnia 19 grudnia 2023 r. do godz. 14. Bardzo serdecznie państwu dziękuję za dzisiejsze fantastyczne, miłe, sympatyczne, pracowite posiedzenie. Do widzenia. Dziękuję.",
                },
            ],
        )
