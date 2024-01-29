import os
import unittest
from src.custom_json import obj2pretty_json
from src.lib import report_to_obj


class TestReportToObj(unittest.TestCase):
    def test_01_a(self):
        file_path = os.path.join("files", "01_a_ksiazka.pdf")
        obj = report_to_obj(file_path)
        print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-13T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "12:07:00")
        self.assertEqual(
            obj["table_of_contents"],
            [
                {
                    "type": "HEADER",
                    "name": "Otwarcie 1. posiedzenia Sejmu RP X kadencji",
                    "speakers": [
                        {"position": "Marszałek Senior", "name": "Marek Sawicki"}
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Przemówienie Prezydenta RP",
                    "speakers": [{"position": "Prezydent RP", "name": "Andrzeja Dudy"}],
                },
                {
                    "type": "HEADER",
                    "name": "Przemówienie Marszałka Seniora",
                    "speakers": [
                        {"position": "Marszałek Senior", "name": "Marka Sawickiego"}
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Powołanie tymczasowych sekretarzy Sejmu Ślubowanie poselskie",
                    "speakers": [
                        {"position": "Sekretarz Poseł", "name": "Bożena Żelazowska"},
                        {
                            "position": "Sekretarz Poseł",
                            "name": "Alicja Łepkowska-Gołaś",
                        },
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Wystąpienie prezesa Rady Ministrów",
                    "speakers": [
                        {
                            "position": "Prezes Rady Ministrów",
                            "name": "Mateusza Morawieckiego",
                        }
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 1. porządku dziennego: Wybór marszałka Sejmu Rzeczypospolitej Polskiej",
                    "speakers": [
                        {"position": "Poseł", "name": "Władysław Kosiniak-Kamysz"},
                        {"position": "Poseł", "name": "Mariusz Błaszczak"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [
                        {"position": "Marszałek Senior", "name": "Marek Sawicki"},
                        {"position": "Marszałek", "name": "Marszałek"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 2. porządku dziennego: Poselskie projekty uchwał w sprawie ustalenia liczby wicemarszałków Sejmu Rzeczypospolitej Polskiej",
                    "speakers": [
                        {"position": "Poseł", "name": "Stanisław Tyszka"},
                        {"position": "Poseł", "name": "Borys Budka"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Paulina Hennig-Kloska"},
                        {"position": "Poseł", "name": "Krzysztof Gawkowski"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 3. porządku dziennego: Wybór wicemarszałków Sejmu Rzeczypospolitej Polskiej",
                    "speakers": [
                        {"position": "Poseł", "name": "Michał Wawer"},
                        {"position": "Poseł", "name": "Krzysztof Gawkowski"},
                        {"position": "Poseł", "name": "Borys Budka"},
                        {"position": "Poseł", "name": "Jarosław Kaczyński"},
                        {"position": "Poseł", "name": "Władysław Kosiniak-Kamysz"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {"type": "BREAK"},
            ],
        )

    def test_01_b(self):
        file_path = os.path.join("files", "01_b_ksiazka.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-14T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "16:33:00")
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 4. porządku dziennego: Wybór sekretarzy Sejmu",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 5. porządku dziennego: Wybór składu osobowego Komisji Regulaminowej, Spraw Poselskich i Immunitetowych",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 6. porządku dziennego: Pierwsze czytanie przedstawionego przez Prezydium Sejmu projektu uchwały w sprawie ustalenia liczby członków Komisji do Spraw Służb Specjalnych",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 7. porządku dziennego: Wybór posłów-członków Krajowej Rady Sądownictwa",
                    "speakers": [
                        {"position": "Poseł", "name": "Anna Milczanowska"},
                        {"position": "Poseł", "name": "Borys Budka"},
                        {
                            "position": "Minister Sprawiedliwości",
                            "name": "Zbigniew Ziobro",
                        },
                        {"position": "Poseł", "name": "Krzysztof Śmiszek"},
                        {
                            "position": "Minister Edukacji i Nauki",
                            "name": "Przemysław Czarnek",
                        },
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {
                            "position": "Minister – Członek Rady Ministrów",
                            "name": "Łukasz Schreiber",
                        },
                        {
                            "position": "Minister do Spraw Unii Europejskiej",
                            "name": "Szymon Szynkowski vel Sęk",
                        },
                        {"position": "Poseł", "name": "Krzysztof Szczucki"},
                        {"position": "Poseł", "name": "Sebastian Kaleta"},
                        {"position": "Poseł", "name": "Arkadiusz Myrcha"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Krzysztof Gawkowski"},
                        {
                            "position": "Minister Edukacji i Nauki",
                            "name": "Przemysław Czarnek",
                        },
                        {"position": "Poseł", "name": "Michał Wawer"},
                        {
                            "position": "Minister – Członek Rady Ministrów",
                            "name": "Michał Wójcik",
                        },
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {"type": "BREAK"},
            ],
        )

    def test_01_c(self):
        file_path = os.path.join("files", "01_c_ksiazka_bis.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-21T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "12:04:00")
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Stefan Krajewski"},
                        {"position": "Poseł", "name": "Andrzej Adamczyk"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Michał Wawer"},
                        {"position": "Poseł", "name": "Paweł Jabłoński"},
                        {"position": "Poseł", "name": "Konrad Berkowicz"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {
                            "position": "Minister do Spraw Unii Europejskiej",
                            "name": "Szymon Szynkowski vel Sęk",
                        },
                        {"position": "Poseł", "name": "Paweł Zalewski"},
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Spraw Zagranicznych",
                            "name": "Paweł Jabłoński",
                        },
                        {
                            "position": "Minister – Członek Rady Ministrów",
                            "name": "Michał Wójcik",
                        },
                        {
                            "position": "Minister – Członek Rady Ministrów",
                            "name": "Łukasz Schreiber",
                        },
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 8. porządku dziennego: Wybór składów osobowych komisji sejmowych",
                    "speakers": [
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Spraw Zagranicznych",
                            "name": "Paweł Jabłoński",
                        }
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 9. porządku dziennego: Wybór składu osobowego Komisji do Spraw Unii Europejskiej",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 10. porządku dziennego: Wybór składu osobowego Komisji Etyki Poselskiej",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 11. porządku dziennego: Wybór składu osobowego Komisji do Spraw Służb Specjalnych",
                    "speakers": [
                        {"position": "Poseł", "name": "Marek Suski"},
                        {"position": "Poseł", "name": "Zbigniew Konwiński"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 12. porządku dziennego: Wybór członków Trybunału Stanu",
                    "speakers": [
                        {"position": "Poseł", "name": "Lidia Burzyńska"},
                        {"position": "Poseł", "name": "Arkadiusz Myrcha"},
                        {"position": "Poseł", "name": "Krzysztof Śmiszek"},
                        {"position": "Poseł", "name": "Robert Kropiwnicki"},
                        {"position": "Poseł", "name": "Sławomir Nitras"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Piotr Zgorzelski"},
                        {"position": "Poseł", "name": "Paweł Śliz"},
                        {"position": "Poseł", "name": "Bartłomiej Pejo"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Paweł Jabłoński"},
                        {"position": "Poseł", "name": "Marek Sawicki"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Komunikaty",
                    "speakers": [
                        {
                            "position": "Sekretarz Poseł",
                            "name": "Aleksandra Karolina Wiśniewska",
                        }
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Oświadczenia",
                    "speakers": [
                        {"position": "Poseł", "name": "Antoni Macierewicz"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Grzegorz Lorek"},
                        {"position": "Poseł", "name": "Anna Wojciechowska"},
                    ],
                },
                {"type": "BREAK"},
            ],
        )

    def test_01_d(self):
        file_path = os.path.join("files", "01_d_ksiazka.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-22T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "11:06:00")
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Grzegorz Adam Płaczek"},
                        {"position": "Poseł", "name": "Waldemar Buda"},
                        {"position": "Poseł", "name": "Paulina Hennig-Kloska"},
                        {"position": "Poseł", "name": "Adrian Zandberg"},
                        {
                            "position": "Minister do spraw Unii Europejskiej",
                            "name": "Szymon Szynkowski vel Sęk",
                        },
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 13. porządku dziennego: Pierwsze czytanie obywatelskiego projektu ustawy o zmianie ustawy o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych",
                    "speakers": [
                        {
                            "position": "Przedstawiciel Komitetu Inicjatywy Ustawodawczej",
                            "name": "Agnieszka Pomaska",
                        },
                        {"position": "Poseł", "name": "Józefa Szczurek-Żelazko"},
                        {"position": "Poseł", "name": "Monika Wielichowska"},
                        {"position": "Poseł", "name": "Barbara Nowacka"},
                        {"position": "Poseł", "name": "Wioleta Tomczak"},
                        {"position": "Poseł", "name": "Władysław Kosiniak-Kamysz"},
                        {"position": "Poseł", "name": "Agnieszka Maria Kłopotek"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Konrad Berkowicz"},
                        {"position": "Minister Zdrowia", "name": "Katarzyna Sójka"},
                        {"position": "Poseł", "name": "Anna Dąbrowska-Banaszek"},
                        {"position": "Poseł", "name": "Monika Rosa"},
                        {"position": "Poseł", "name": "Barbara Oliwiecka"},
                        {"position": "Poseł", "name": "Dariusz Klimczak"},
                        {"position": "Poseł", "name": "Joanna Scheuring-Wielgus"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Czesław Hoc"},
                        {"position": "Poseł", "name": "Bartosz Arłukowicz"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Marcelina Zawisza"},
                        {"position": "Poseł", "name": "Bolesław Piecha"},
                        {"position": "Poseł", "name": "Aleksandra Gajewska"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Jarosław Rzepa"},
                        {"position": "Poseł", "name": "Paulina Matysiak"},
                        {"position": "Poseł", "name": "Sławomir Nitras"},
                        {"position": "Poseł", "name": "Urszula Pasławska"},
                        {"position": "Poseł", "name": "Daria Gosek-Popiołek"},
                        {"position": "Poseł", "name": "Piotr Uściński"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Joanna Wicha"},
                        {"position": "Poseł", "name": "Katarzyna Maria Piekarska"},
                        {"position": "Poseł", "name": "Dorota Olko"},
                        {"position": "Poseł", "name": "Paweł Szrot"},
                        {"position": "Poseł", "name": "Katarzyna Anna Lubnauer"},
                        {"position": "Poseł", "name": "Adrian Zandberg"},
                        {"position": "Poseł", "name": "Andrzej Gawron"},
                        {"position": "Poseł", "name": "Marzena Okła-Drewnowicz"},
                        {"position": "Poseł", "name": "Tomasz Dominik Trela"},
                        {"position": "Poseł", "name": "Maria Kurowska"},
                        {"position": "Poseł", "name": "Cezary Tomczyk"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Dariusz Matecki"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Anita Kucharska-Dziedzic"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Anna Wojciechowska"},
                        {"position": "Poseł", "name": "Arkadiusz Marchewka"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Zofia Czernow"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Małgorzata Tracz"},
                        {"position": "Poseł", "name": "Urszula Sara Zielińska"},
                        {"position": "Poseł", "name": "Krzysztof Habura"},
                        {"position": "Poseł", "name": "Karolina Pawliczak"},
                        {"position": "Poseł", "name": "Piotr Borys"},
                        {"position": "Poseł", "name": "Katarzyna Matusik-Lipiec"},
                        {"position": "Poseł", "name": "Adam Szłapka"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Katarzyna Kierzek-Koperska"},
                        {"position": "Poseł", "name": "Przemysław Witek"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Paweł Bliźniuk"},
                        {"position": "Poseł", "name": "Maria Małgorzata Janyska"},
                        {"position": "Poseł", "name": "Krystyna Sibińska"},
                        {"position": "Poseł", "name": "Elżbieta Gapińska"},
                        {"position": "Poseł", "name": "Iwona Maria Kozłowska"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Mateusz Bochenek"},
                        {"position": "Poseł", "name": "Marcin Józefaciuk"},
                        {"position": "Poseł", "name": "Marek Rząsa"},
                        {"position": "Poseł", "name": "Jolanta Niezgodzka"},
                        {"position": "Poseł", "name": "Krzysztof Truskolaski"},
                        {"position": "Poseł", "name": "Małgorzata Niemczyk"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Maciej Wróbel"},
                        {"position": "Poseł", "name": "Patryk Jaskulski"},
                        {"position": "Poseł", "name": "Michał Krawczyk"},
                        {"position": "Poseł", "name": "Iwona Hartwich"},
                        {"position": "Poseł", "name": "Artur Daniel Gierada"},
                        {"position": "Poseł", "name": "Aleksander Miszalski"},
                        {"position": "Poseł", "name": "Franciszek Sterczewski"},
                        {"position": "Poseł", "name": "Krystyna Szumilas"},
                        {"position": "Poseł", "name": "Agnieszka Hanajczyk"},
                        {"position": "Poseł", "name": "Artur Jarosław Łącki"},
                        {"position": "Poseł", "name": "Adrian Witczak"},
                        {"position": "Poseł", "name": "Jan Krzysztof Ardanowski"},
                        {"position": "Poseł", "name": "Andrzej Szewiński"},
                        {"position": "Poseł", "name": "Łukasz Ściebiorowski"},
                        {"position": "Poseł", "name": "Krystian Łuczak"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Krzysztof Ciecióra"},
                        {"position": "Poseł", "name": "Piotr Kaleta"},
                        {
                            "position": "Zastępca Przedstawiciela Komitetu Inicjatywy Ustawodawczej",
                            "name": "Małgorzata Rozenek-Majdan",
                        },
                        {
                            "position": "Przedstawiciel Komitetu Inicjatywy Ustawodawczej",
                            "name": "Agnieszka Pomaska",
                        },
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Oświadczenia",
                    "speakers": [
                        {"position": "Poseł", "name": "Grzegorz Lorek"},
                        {"position": "Poseł", "name": "Mariusz Krystian"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Iwona Małgorzata Krawczyk"},
                        {"position": "Poseł", "name": "Paulina Matysiak"},
                        {"position": "Poseł", "name": "Katarzyna Maria Piekarska"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Łukasz Horbatowski"},
                        {"position": "Poseł", "name": "Marek Jan Chmielewski"},
                        {"position": "Poseł", "name": "Norbert Jakub Kaczmarczyk"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                    ],
                },
                {"type": "BREAK"},
            ],
        )

    def test_01_e(self):
        file_path = os.path.join("files", "01_e_ksiazka_bis.pdf")
        obj = report_to_obj(file_path)
        print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-28T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "12:05:00")
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Komunikaty",
                    "speakers": [
                        {"position": "Sekretarz Poseł", "name": "Patryk Jaskulski"}
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {
                            "position": "Prezes Rady Ministrów",
                            "name": "Mateusz Morawiecki",
                        },
                        {"position": "Poseł", "name": "Waldemar Buda"},
                        {"position": "Poseł", "name": "Michał Wawer"},
                        {"position": "Poseł", "name": "Krzysztof Gawkowski"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 14. porządku dziennego: Powołanie Rzecznika Praw Dziecka",
                    "speakers": [],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Paweł Jabłoński"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 14. porządku dziennego (cd.)",
                    "speakers": [
                        {"position": "Poseł", "name": "Marzena Okła-Drewnowicz"},
                        {"position": "Poseł Sprawozdawca", "name": "Michał Krawczyk"},
                        {"position": "Poseł", "name": "Dorota Łoboda"},
                        {"position": "Poseł", "name": "Maja Ewa Nowak"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Katarzyna Kotula"},
                        {"position": "Poseł", "name": "Grzegorz Adam Płaczek"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 15. porządku dziennego: Powołanie członka Państwowej Komisji do spraw przeciwdziałania wykorzystaniu seksualnemu małoletnich poniżej lat 15",
                    "speakers": [
                        {
                            "position": "Poseł Sprawozdawca",
                            "name": "Katarzyna Ueberhan",
                        },
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Joanna Mucha"},
                        {"position": "Poseł", "name": "Katarzyna Ueberhan"},
                        {"position": "Poseł", "name": "Monika Rosa"},
                        {"position": "Poseł", "name": "Konrad Berkowicz"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 16. porządku dziennego: Pierwsze czytanie przedstawionego przez Prezydium Sejmu projektu uchwały w sprawie powołania i wyboru składu osobowego Komisji Nadzwyczajnej do spraw zmian w kodyfikacjach",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 13. porządku dziennego: Pierwsze czytanie obywatelskiego projektu ustawy o zmianie ustawy o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 17. porządku dziennego: Sprawozdanie Komisji Gospodarki i Rozwoju o poselskim projekcie ustawy o zmianie ustawy o ograniczeniu handlu w niedziele i święta oraz niektóre inne dni",
                    "speakers": [
                        {
                            "position": "Poseł Sprawozdawca",
                            "name": "Adam Michał Gomoła",
                        },
                        {"position": "", "name": "Adam Michał Gomoła"},
                        {"position": "Poseł", "name": "Urszula Rusecka"},
                        {"position": "Poseł", "name": "Michał Jaros"},
                        {"position": "Poseł", "name": "Maria Małgorzata Janyska"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Magdalena Sroka"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Przemysław Wipler"},
                        {"position": "Poseł", "name": "Grzegorz Lorek"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Adrian Zandberg"},
                        {"position": "Poseł", "name": "Marcin Porzucek"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Katarzyna Kierzek-Koperska"},
                        {"position": "Poseł", "name": "Paulina Matysiak"},
                        {"position": "Poseł", "name": "Mirosława Nykiel"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Krzysztof Truskolaski"},
                        {"position": "Poseł", "name": "Małgorzata Niemczyk"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Katarzyna Anna Lubnauer"},
                        {"position": "Poseł", "name": "Rafał Kasprzyk"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Michał Jaros"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Rodziny i Polityki Społecznej",
                            "name": "Stanisław Szwed",
                        },
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 18. porządku dziennego: Pierwsze czytanie poselskiego projektu uchwały w sprawie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego",
                    "speakers": [
                        {"position": "Poseł", "name": "Zbigniew Konwiński"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Cezary Tomczyk"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Urszula Nowogórska"},
                        {"position": "Poseł", "name": "Joanna Scheuring-Wielgus"},
                        {"position": "Poseł", "name": "Witold Tumanowicz"},
                        {"position": "Poseł", "name": "Władysław Dajczak"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Bożena Żelazowska"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Mariusz Krystian"},
                        {"position": "Poseł", "name": "Mateusz Bochenek"},
                        {"position": "Poseł", "name": "Barbara Oliwiecka"},
                        {"position": "Poseł", "name": "Zbigniew Sosnowski"},
                        {"position": "Poseł", "name": "Mariusz Witczak"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Zbigniew Dolata"},
                        {"position": "Poseł", "name": "Małgorzata Tracz"},
                        {"position": "Poseł", "name": "Piotr Kaleta"},
                        {"position": "Poseł", "name": "Piotr Głowski"},
                        {"position": "Poseł", "name": "Robert Gontarz"},
                        {"position": "Poseł", "name": "Karolina Pawliczak"},
                        {"position": "Poseł", "name": "Łukasz Kmita"},
                        {"position": "Poseł", "name": "Elżbieta Anna Polak"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {
                            "position": "Poseł",
                            "name": "Magdalena Małgorzata Kołodziejczak",
                        },
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Katarzyna Matusik-Lipiec"},
                        {"position": "Poseł", "name": "Małgorzata Niemczyk"},
                        {"position": "Poseł", "name": "Adrian Witczak"},
                        {"position": "Poseł", "name": "Sylwia Bielawska"},
                        {"position": "Poseł", "name": "Marek Jan Chmielewski"},
                        {"position": "Poseł", "name": "Łukasz Ściebiorowski"},
                        {"position": "Poseł", "name": "Zbigniew Konwiński"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 19. porządku dziennego: Pierwsze czytanie poselskiego projektu uchwały w sprawie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości czynności operacyjno-rozpoznawczych podejmowanych m.in. z wykorzystaniem oprogramowania Pegasus przez członków Rady Ministrów, służby specjalne, Policję, organy kontroli skarbowej oraz celno-skarbowej w okresie od dnia 16 listopada 2015 r. do dnia 20 listopada 2023 r.",
                    "speakers": [
                        {"position": "Poseł", "name": "Robert Kropiwnicki"},
                        {"position": "Poseł", "name": "Michał Wójcik"},
                        {"position": "Poseł", "name": "Jacek Karnowski"},
                        {"position": "Poseł", "name": "Krzysztof Brejza"},
                        {"position": "Poseł", "name": "Paweł Śliz"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Tomasz Trela"},
                        {"position": "Poseł", "name": "Sławomir Mentzen"},
                        {"position": "Poseł", "name": "Paweł Kukiz"},
                        {"position": "Poseł", "name": "Jacek Ozdoba"},
                        {"position": "Poseł", "name": "Marcin Bosacki"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Przemysław Wipler"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Magdalena Sroka"},
                        {"position": "Poseł", "name": "Roman Fritz"},
                        {"position": "Poseł", "name": "Piotr Adamowicz"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Michał Pyrzyk"},
                        {"position": "Poseł", "name": "Krzysztof Truskolaski"},
                        {"position": "Poseł", "name": "Zbigniew Sosnowski"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Zofia Czernow"},
                        {"position": "Poseł", "name": "Krzysztof Habura"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Mirosława Nykiel"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Przemysław Witek"},
                        {"position": "Poseł", "name": "Łukasz Horbatowski"},
                        {"position": "Poseł", "name": "Anna Sobolak"},
                        {"position": "Poseł", "name": "Paweł Kukiz"},
                        {
                            "position": "Minister Sprawiedliwości",
                            "name": "Marcin Warchoł",
                        },
                        {"position": "Poseł", "name": "Krzysztof Brejza"},
                        {"position": "Poseł", "name": "Robert Kropiwnicki"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 20. porządku dziennego: Pierwsze czytanie poselskiego projektu uchwały w sprawie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań, a także występowania nadużyć, zaniedbań i zaniechań w zakresie legalizacji pobytu cudzoziemców na terytorium Rzeczypospolitej Polskiej w okresie od dnia 1 stycznia 2019 r. do dnia 20 listopada 2023 r.",
                    "speakers": [
                        {"position": "Poseł", "name": "Tomasz Szymański"},
                        {"position": "Poseł", "name": "Paweł Jabłoński"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Sławomir Nitras"},
                        {"position": "Poseł", "name": "Ewa Schädler"},
                        {"position": "Poseł", "name": "Aleksandra Leo"},
                        {"position": "Poseł", "name": "Marek Biernacki"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Krzysztof Mulawa"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Marek Jakubiak"},
                        {"position": "Poseł", "name": "Radosław Fogiel"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Agnieszka Buczyńska"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Rafał Kasprzyk"},
                        {"position": "Poseł", "name": "Jarosław Rzepa"},
                        {"position": "Poseł", "name": "Dariusz Wieczorek"},
                        {"position": "Poseł", "name": "Marek Krząkała"},
                        {"position": "Poseł", "name": "Adam Luboński"},
                        {"position": "Poseł", "name": "Piotr Borys"},
                        {"position": "Poseł", "name": "Urszula Sara Zielińska"},
                        {"position": "Poseł", "name": "Waldemar Sługocki"},
                        {"position": "Poseł", "name": "Marek Sowa"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Iwona Maria Kozłowska"},
                        {"position": "Poseł", "name": "Artur Jarosław Łącki"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Anna Wojciechowska"},
                        {"position": "Poseł", "name": "Patryk Gabriel"},
                        {"position": "Poseł", "name": "Bartosz Zawieja"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Marcin Grabowski"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Paweł Jabłoński"},
                        {"position": "Poseł", "name": "Tomasz Szymański"},
                        {"position": "Poseł", "name": "Radosław Fogiel"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Oświadczenia",
                    "speakers": [
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Szymon Giżyński"},
                        {"position": "Poseł", "name": "Anna Dąbrowska-Banaszek"},
                        {"position": "Poseł", "name": "Michał Pyrzyk"},
                        {"position": "Poseł", "name": "Barbara Bartuś"},
                        {"position": "Poseł", "name": "Marcin Józefaciuk"},
                        {"position": "Poseł", "name": "Iwona Małgorzata Krawczyk"},
                        {"position": "Poseł", "name": "Andrzej Tomasz Zapałowski"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Maciej Wróbel"},
                        {"position": "Poseł", "name": "Tadeusz Samborski"},
                        {"position": "Poseł", "name": "Renata Urszula Rak"},
                        {"position": "Poseł", "name": "Sylwia Bielawska"},
                    ],
                },
                {"type": "BREAK"},
                {
                    "type": "HEADER",
                    "name": "Załącznik – Teksty wystąpień niewygłoszonych",
                    "speakers": [
                        {"position": "Poseł", "name": "Waldemar Andzel"},
                        {"position": "Poseł", "name": "Grzegorz Lorek"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                    ],
                },
            ],
        )

    def test_01_f(self):
        file_path = os.path.join("files", "01_f_ksiazka.pdf")
        obj = report_to_obj(file_path)
        print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-29T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "09:04:00")
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Komunikaty",
                    "speakers": [
                        {"position": "Sekretarz Poseł", "name": "Patryk Jaskulski"}
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {
                            "position": "Prezes Rady Ministrów",
                            "name": "Mateusz Morawiecki",
                        },
                        {"position": "Poseł", "name": "Waldemar Buda"},
                        {"position": "Poseł", "name": "Michał Wawer"},
                        {"position": "Poseł", "name": "Krzysztof Gawkowski"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 14. porządku dziennego: Powołanie Rzecznika Praw Dziecka",
                    "speakers": [],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Paweł Jabłoński"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 14. porządku dziennego (cd.)",
                    "speakers": [
                        {"position": "Poseł", "name": "Marzena Okła-Drewnowicz"},
                        {"position": "Poseł Sprawozdawca", "name": "Michał Krawczyk"},
                        {"position": "Poseł", "name": "Dorota Łoboda"},
                        {"position": "Poseł", "name": "Maja Ewa Nowak"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Katarzyna Kotula"},
                        {"position": "Poseł", "name": "Grzegorz Adam Płaczek"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 15. porządku dziennego: Powołanie członka Państwowej Komisji do spraw przeciwdziałania wykorzystaniu seksualnemu małoletnich poniżej lat 15",
                    "speakers": [
                        {
                            "position": "Poseł Sprawozdawca",
                            "name": "Katarzyna Ueberhan",
                        },
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Joanna Mucha"},
                        {"position": "Poseł", "name": "Katarzyna Ueberhan"},
                        {"position": "Poseł", "name": "Monika Rosa"},
                        {"position": "Poseł", "name": "Konrad Berkowicz"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 16. porządku dziennego: Pierwsze czytanie przedstawionego przez Prezydium Sejmu projektu uchwały w sprawie powołania i wyboru składu osobowego Komisji Nadzwyczajnej do spraw zmian w kodyfikacjach",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 13. porządku dziennego: Pierwsze czytanie obywatelskiego projektu ustawy o zmianie ustawy o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Marszałek"}],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 17. porządku dziennego: Sprawozdanie Komisji Gospodarki i Rozwoju o poselskim projekcie ustawy o zmianie ustawy o ograniczeniu handlu w niedziele i święta oraz niektóre inne dni",
                    "speakers": [
                        {
                            "position": "Poseł Sprawozdawca",
                            "name": "Adam Michał Gomoła",
                        },
                        {"position": "", "name": "Adam Michał Gomoła"},
                        {"position": "Poseł", "name": "Urszula Rusecka"},
                        {"position": "Poseł", "name": "Michał Jaros"},
                        {"position": "Poseł", "name": "Maria Małgorzata Janyska"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Magdalena Sroka"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Przemysław Wipler"},
                        {"position": "Poseł", "name": "Grzegorz Lorek"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Adrian Zandberg"},
                        {"position": "Poseł", "name": "Marcin Porzucek"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Katarzyna Kierzek-Koperska"},
                        {"position": "Poseł", "name": "Paulina Matysiak"},
                        {"position": "Poseł", "name": "Mirosława Nykiel"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Krzysztof Truskolaski"},
                        {"position": "Poseł", "name": "Małgorzata Niemczyk"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Katarzyna Anna Lubnauer"},
                        {"position": "Poseł", "name": "Rafał Kasprzyk"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Michał Jaros"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Rodziny i Polityki Społecznej",
                            "name": "Stanisław Szwed",
                        },
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 18. porządku dziennego: Pierwsze czytanie poselskiego projektu uchwały w sprawie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego",
                    "speakers": [
                        {"position": "Poseł", "name": "Zbigniew Konwiński"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Cezary Tomczyk"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Urszula Nowogórska"},
                        {"position": "Poseł", "name": "Joanna Scheuring-Wielgus"},
                        {"position": "Poseł", "name": "Witold Tumanowicz"},
                        {"position": "Poseł", "name": "Władysław Dajczak"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Bożena Żelazowska"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Mariusz Krystian"},
                        {"position": "Poseł", "name": "Mateusz Bochenek"},
                        {"position": "Poseł", "name": "Barbara Oliwiecka"},
                        {"position": "Poseł", "name": "Zbigniew Sosnowski"},
                        {"position": "Poseł", "name": "Mariusz Witczak"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Zbigniew Dolata"},
                        {"position": "Poseł", "name": "Małgorzata Tracz"},
                        {"position": "Poseł", "name": "Piotr Kaleta"},
                        {"position": "Poseł", "name": "Piotr Głowski"},
                        {"position": "Poseł", "name": "Robert Gontarz"},
                        {"position": "Poseł", "name": "Karolina Pawliczak"},
                        {"position": "Poseł", "name": "Łukasz Kmita"},
                        {"position": "Poseł", "name": "Elżbieta Anna Polak"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {
                            "position": "Poseł",
                            "name": "Magdalena Małgorzata Kołodziejczak",
                        },
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Katarzyna Matusik-Lipiec"},
                        {"position": "Poseł", "name": "Małgorzata Niemczyk"},
                        {"position": "Poseł", "name": "Adrian Witczak"},
                        {"position": "Poseł", "name": "Sylwia Bielawska"},
                        {"position": "Poseł", "name": "Marek Jan Chmielewski"},
                        {"position": "Poseł", "name": "Łukasz Ściebiorowski"},
                        {"position": "Poseł", "name": "Zbigniew Konwiński"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 19. porządku dziennego: Pierwsze czytanie poselskiego projektu uchwały w sprawie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości czynności operacyjno-rozpoznawczych podejmowanych m.in. z wykorzystaniem oprogramowania Pegasus przez członków Rady Ministrów, służby specjalne, Policję, organy kontroli skarbowej oraz celno-skarbowej w okresie od dnia 16 listopada 2015 r. do dnia 20 listopada 2023 r.",
                    "speakers": [
                        {"position": "Poseł", "name": "Robert Kropiwnicki"},
                        {"position": "Poseł", "name": "Michał Wójcik"},
                        {"position": "Poseł", "name": "Jacek Karnowski"},
                        {"position": "Poseł", "name": "Krzysztof Brejza"},
                        {"position": "Poseł", "name": "Paweł Śliz"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Tomasz Trela"},
                        {"position": "Poseł", "name": "Sławomir Mentzen"},
                        {"position": "Poseł", "name": "Paweł Kukiz"},
                        {"position": "Poseł", "name": "Jacek Ozdoba"},
                        {"position": "Poseł", "name": "Marcin Bosacki"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Przemysław Wipler"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Magdalena Sroka"},
                        {"position": "Poseł", "name": "Roman Fritz"},
                        {"position": "Poseł", "name": "Piotr Adamowicz"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Michał Pyrzyk"},
                        {"position": "Poseł", "name": "Krzysztof Truskolaski"},
                        {"position": "Poseł", "name": "Zbigniew Sosnowski"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Zofia Czernow"},
                        {"position": "Poseł", "name": "Krzysztof Habura"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Mirosława Nykiel"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Przemysław Witek"},
                        {"position": "Poseł", "name": "Łukasz Horbatowski"},
                        {"position": "Poseł", "name": "Anna Sobolak"},
                        {"position": "Poseł", "name": "Paweł Kukiz"},
                        {
                            "position": "Minister Sprawiedliwości",
                            "name": "Marcin Warchoł",
                        },
                        {"position": "Poseł", "name": "Krzysztof Brejza"},
                        {"position": "Poseł", "name": "Robert Kropiwnicki"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 20. porządku dziennego: Pierwsze czytanie poselskiego projektu uchwały w sprawie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań, a także występowania nadużyć, zaniedbań i zaniechań w zakresie legalizacji pobytu cudzoziemców na terytorium Rzeczypospolitej Polskiej w okresie od dnia 1 stycznia 2019 r. do dnia 20 listopada 2023 r.",
                    "speakers": [
                        {"position": "Poseł", "name": "Tomasz Szymański"},
                        {"position": "Poseł", "name": "Paweł Jabłoński"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Sławomir Nitras"},
                        {"position": "Poseł", "name": "Ewa Schädler"},
                        {"position": "Poseł", "name": "Aleksandra Leo"},
                        {"position": "Poseł", "name": "Marek Biernacki"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Krzysztof Mulawa"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Marek Jakubiak"},
                        {"position": "Poseł", "name": "Radosław Fogiel"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Agnieszka Buczyńska"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Rafał Kasprzyk"},
                        {"position": "Poseł", "name": "Jarosław Rzepa"},
                        {"position": "Poseł", "name": "Dariusz Wieczorek"},
                        {"position": "Poseł", "name": "Marek Krząkała"},
                        {"position": "Poseł", "name": "Adam Luboński"},
                        {"position": "Poseł", "name": "Piotr Borys"},
                        {"position": "Poseł", "name": "Urszula Sara Zielińska"},
                        {"position": "Poseł", "name": "Waldemar Sługocki"},
                        {"position": "Poseł", "name": "Marek Sowa"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Iwona Maria Kozłowska"},
                        {"position": "Poseł", "name": "Artur Jarosław Łącki"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Anna Wojciechowska"},
                        {"position": "Poseł", "name": "Patryk Gabriel"},
                        {"position": "Poseł", "name": "Bartosz Zawieja"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Marcin Grabowski"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Paweł Jabłoński"},
                        {"position": "Poseł", "name": "Tomasz Szymański"},
                        {"position": "Poseł", "name": "Radosław Fogiel"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Oświadczenia",
                    "speakers": [
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Szymon Giżyński"},
                        {"position": "Poseł", "name": "Anna Dąbrowska-Banaszek"},
                        {"position": "Poseł", "name": "Michał Pyrzyk"},
                        {"position": "Poseł", "name": "Barbara Bartuś"},
                        {"position": "Poseł", "name": "Marcin Józefaciuk"},
                        {"position": "Poseł", "name": "Iwona Małgorzata Krawczyk"},
                        {"position": "Poseł", "name": "Andrzej Tomasz Zapałowski"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Maciej Wróbel"},
                        {"position": "Poseł", "name": "Tadeusz Samborski"},
                        {"position": "Poseł", "name": "Renata Urszula Rak"},
                        {"position": "Poseł", "name": "Sylwia Bielawska"},
                    ],
                },
                {"type": "BREAK"},
                {
                    "type": "HEADER",
                    "name": "Załącznik – Teksty wystąpień niewygłoszonych",
                    "speakers": [
                        {"position": "Poseł", "name": "Waldemar Andzel"},
                        {"position": "Poseł", "name": "Grzegorz Lorek"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                    ],
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
