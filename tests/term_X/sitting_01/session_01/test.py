import unittest
from src.custom_json import obj2pretty_json
from src.lib import report_to_obj
from datetime import time
from tests.utils import get_file_path_in_same_folder


class SessionReport(unittest.TestCase):
    def test(self):
        file_path = get_file_path_in_same_folder(__file__, "01_a_ksiazka.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))
        # exit()

        self.assertEqual(obj["term_number"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["sitting_day"], 1)
        self.assertEqual(obj["sitting_start_time"], time(12, 7))
        self.assertEqual(obj["sitting_end_time"], None)
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-13T00:00:00")
        self.assertEqual(obj["session_start_time"], time(12, 7))
        self.assertEqual(obj["session_end_time"], time(19, 47))
        self.assertEqual(
            obj["session_intra_breaks_times"],
            [
                {
                    "start": time(14, 25),
                    "end": time(14, 53),
                },
                {
                    "start": time(15, 31),
                    "end": time(17, 48),
                },
                {
                    "start": time(18, 3),
                    "end": time(19, 19),
                },
            ],
        )
        self.assertEqual(obj["speaker_senior"], "Marek Sawicki")
        self.assertEqual(obj["speaker"], "Szymon Hołownia")
        self.assertEqual(obj["vicespeakers"], [])
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
                    "name": "Powołanie tymczasowych sekretarzy Sejmu",
                    "speakers": [],
                },
                {
                    "type": "HEADER",
                    "name": "Ślubowanie poselskie",
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
                        {"position": "Marszałek", "name": "Szymon Hołownia"},
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
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
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
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {"type": "BREAK"},
            ],
        )
        self.assertEqual(
            obj["content"],
            [
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Otwieram 1. posiedzenie Sejmu Rzeczypospolitej Polskiej X kadencji. (Marszałek senior trzykrotnie uderza laską marszałkowską, oklaski) (Orkiestra gra hymn państwowy, zebrani wstają i śpiewają) Szanowni Państwo! Serdecznie witam przybyłych na naszą uroczystość: prezydenta Rzeczypospolitej Polskiej pana Andrzeja Dudę (Oklaski, część posłów wstaje), prezesa Rady Ministrów pana Mateusza Morawieckiego wraz z członkami Rady Ministrów. (Oklaski, część posłów wstaje) Witam byłego prezydenta Rzeczypospolitej Polskiej pana Bronisława Komorowskiego. (Oklaski) Witam marszałka seniora Senatu Rzeczypospolitej Polskiej XI kadencji pana Michała Seweryńskiego. (Oklaski) Witam marszałków Sejmu i Senatu ubiegłych kadencji. (Oklaski) Witam byłych premierów Rzeczypospolitej Polskiej. Serdecznie witam korpus dyplomatyczny wraz z jego dziekanem nuncjuszem apostolskim w Polsce Antonio Guido Filipazzim. (Oklaski) Witam duchowieństwo na czele z przewodniczącym Konferencji Episkopatu Polski Jego Ekscelencją księdzem arcybiskupem Stanisławem Gądeckim. (Oklaski) Witam członków Polskiej Rady Ekumenicznej oraz wszystkich przedstawicieli innych Kościołów i związków wyznaniowych. (Oklaski) Witam dowódców Sił Zbrojnych Rzeczypospolitej Polskiej na czele z szefem Sztabu Generalnego Wojska Polskiego generałem Wiesławem Kukułą. (Oklaski) Witam wszystkich panie i panów wybranych na posłów Sejmu Rzeczypospolitej Polskiej oraz wszystkich gości, którzy swoją obecnością uświetniają inaugurację 1. posiedzenia Sejmu X kadencji. (Oklaski) Bardzo proszę prezydenta Rzeczypospolitej Polskiej pana Andrzeja Dudę o wygłoszenie orędzia na 1. posiedzeniu Sejmu X kadencji. (Oklaski)",
                },
                {
                    "speaker": "Prezydent Rzeczypospolitej Polskiej Andrzej Duda",
                    "content": "Drodzy Rodacy! Wielce Szanowny Panie Marszałku Seniorze! Szanowny Panie Prezydencie! Szanowni Państwo Marszałkowie poprzedniej i wcześniejszych kadencji! Wielce Szanowny Panie Premierze! Szanowne Panie Premier i Szanowni Panowie Premierzy poprzednich rządów! Szanowne Panie Minister i Szanowni Panowie Ministrowie! Szanowne Panie Posłanki i Szanowni Panowie Posłowie! Ekscelencjo, Czcigodny Księże Arcybiskupie, Dziekanie korpusu dyplomatycznego wraz ze wszystkimi ekscelencjami, przedstawicielami korpusu dyplomatycznego, ambasadorami, konsulami i wszystkimi zagranicznymi gośćmi reprezentującymi swoje kraje w Rzeczypospolitej Polskiej! Eminencjo, Księże Kardynale! Ekscelencje, Księża Arcybiskupi i Biskupi! Wszystkie Osoby Stanu Duchownego obecne na tej sali! Szanowne Panie i Szanowni Panowie Generałowie, Oficerowie! Wszyscy Dostojni Przybyli Goście! Przedstawiciele instytucji państwowych i samorządowych! Wszyscy Wielce Szanowni Państwo! 21 966 891 osób! Dokładnie tylu polskich obywateli zagłosowało w wyborach 15 października. Frekwencja wyborcza osiągnęła ponad 74%. To wielka rzecz. To wielki sukces polskiej demokracji. Dziękuję, dziękuję i jeszcze raz dziękuję wszystkim, którzy wzięli udział w wyborach parlamentarnych, wszystkim paniom i panom wyborcom. Dziękuję z całego serca! (Oklaski) Demokracja w Polsce nigdy nie była tak silna. Jest najsilniejsza bez wątpienia w całej naszej historii. Oczywiście my, Polacy, w wielu sprawach istotnie się różnimy w poglądach i będziemy się różnić. Prowadzimy często gorące spory i zapewne będziemy je prowadzić, bo taka jest natura demokracji. Najważniejsze jednak jest to, że spory te rozstrzygamy przy urnie wyborczej, i to jest właśnie istota demokracji. To jest wielki sukces ostatnich lat. Polacy ponownie uwierzyli, że ich głos ma znaczenie, że mogą jako obywatele decydować o najważniejszych dla Polski sprawach, decydować o kierunkach rozwoju naszej Ojczyzny. Świadczy o tym właśnie rosnąca z roku na rok, z wyborów na wybory frekwencja. Już 4 lata temu w wyborach parlamentarnych była wysoka, w wyborach prezydenckich w 2020 r. jeszcze wyższa, a teraz osiągnęła absolutnie rekordowy poziom. A przecież nie zawsze tak było. Wszyscy pamiętamy, jak jeszcze kilkanaście lat temu w wyborach uczestniczyło poniżej 50% uprawnionych. Na polskiej wsi głosowało wówczas zaledwie 36% wyborców. Ludzie byli zniechęceni. Uważali, że politycy ich nie reprezentują, że sami nie mają jako obywatele realnego wpływu na to, co dzieje się w Polsce, co dzieje się w naszym kraju. Dziś jest zupełnie inaczej. Polacy biorą licznie udział w wyborach niezależnie od tego, czy mieszkają na wsi, w małym, średnim bądź dużym mieście. To wielka zmiana, to wielki sukces, ale to także i wielkie zadanie. Zadanie dla wszystkich państwa, którzy zasiadają dzisiaj w ławach poselskich – zarówno tych, którzy będą tworzyć większość rządową, jak i tych, którzy znajdą się w opozycji. To od waszych decyzji, od tego, jak będziecie sprawować swój mandat, zależy, czy Polacy tej wiary w naszą demokrację nie utracą. To wielka odpowiedzialność. (Oklaski) Szanowni Państwo! „Polska bez silnego, zdrowego, szanującego się i szanowanego Sejmu nie może istnieć” – to niezwykle ważne słowa jednego z ojców naszej niepodległości, Ignacego Daszyńskiego. To dla mnie wielki zaszczyt wygłaszać orędzie podczas inauguracji jubileuszowej X kadencji Sejmu Rzeczypospolitej Polskiej. Sejmu wolnej, niepodległej, suwerennej i demokratycznej Rzeczypospolitej. Zaledwie 2 dni temu obchodziliśmy 105. rocznicę odzyskania przez Polskę niepodległości. Po 123 latach zaborów, kiedy nie było nas na mapach świata. Ojcowie naszej niepodległości wierzyli wówczas, że odrodzona Rzeczpospolita ma przed sobą wspaniałą przyszłość. Niestety nie było jej dane długo cieszyć się odzyskaną wolnością. Najpierw nastąpiła olbrzymia tragedia II wojny światowej, a później długi okres sowieckiej dominacji, kiedy nie byliśmy jako Polska krajem w pełni niepodległym i w pełni suwerennym. Dlatego tym bardziej powinniśmy doceniać ostatnie ponad 30 lat wolności, kiedy wreszcie możemy sami o sobie w pełni decydować, o najważniejszych dla Polski sprawach, o tym, w jakim kierunku będzie się rozwijać nasza Ojczyzna. Wielkie marzenie całych pokoleń Polaków ziściło się i spełnia się na naszych oczach. To marzenie jest dzisiaj dla nas wszystkich wielkim zobowiązaniem. Polska jest naszym wspólnym, wielkim zobowiązaniem. (Oklaski) Bo jak mówił kolejny z ojców naszej niepodległości, Roman Dmowski: „Jesteśmy różni, pochodzimy z różnych stron Polski, mamy różne zainteresowania, ale łączy nas jeden cel. Cel ten to Ojczyzna, dla której chcemy żyć i pracować”. (Oklaski) Dlatego z całego serca gratuluję wszystkim paniom posłankom i panom posłom wyboru i życzę państwu wytrwałości w służbie dla Rzeczypospolitej. Chciałbym też z tego miejsca zaapelować do was o to, abyście szanowali siebie nawzajem. Wyrazem tego wzajemnego szacunku, ale też szacunku wobec wyborców powinno być to, że każdy klub parlamentarny, każdy, nawet ten najmniejszy, będzie miał wskazanego przez siebie reprezentanta w Prezydium Sejmu. To powinien być dobry i stały zwyczaj parlamentarny. (Oklaski) (Poseł Cezary Tomczyk: O 2015 r. pan zapomniał.) Warto pamiętać, że w demokracji jest tak, że ci, którzy dzisiaj sprawują władzę czy jutro będą ją sprawować, za jakiś czas znajdą się w opozycji. Niestety rządzący, niezależnie od opcji politycznej, zbyt często zapominają o tym oczywistym fakcie. (Poruszenie na sali, oklaski, wesołość na sali) (Głos z sali: Ooo…) (Głos z sali: Brawo!) W sposób szczególny w tym uroczystym dniu zwracam się do 117 posłanek i posłów, którzy będą sprawować swój mandat poselski po raz pierwszy. Doskonale pamiętam, co sam czułem, kiedy 8 listopada 2011 r. składałem swoje ślubowanie poselskie. Towarzyszyły mi wtedy wielkie emocje, radość i duma, ale przede wszystkim poczucie olbrzymiego zobowiązania wobec wyborców – wyborców, którzy zaufali mi i powierzyli swoje sprawy, abym godnie reprezentował ich w Sejmie. Uwierzcie mi państwo, zapamiętacie ten dzień do końca życia, a słowa poselskiego ślubowania, które za chwilę wypowiecie, niech będą dla was drogowskazem. Przytoczę je, bo nigdy wystarczająco wiele razy je powtarzać: „Uroczyście ślubuję rzetelnie i sumiennie wykonywać obowiązki wobec Narodu, strzec suwerenności i interesów Państwa, czynić wszystko dla pomyślności Ojczyzny i dobra obywateli, przestrzegać Konstytucji i innych praw Rzeczypospolitej”. (Poruszenie na sali, oklaski) (Głos z sali: Tak jest.) (Głos z sali: Ooo…) (Głos z sali: Brawo!) Suwerenność Rzeczypospolitej, interes państwa i dobro obywateli – to są właśnie te najważniejsze sprawy, którym wszyscy zobowiązujemy się służyć. (Oklaski) Szanowni Państwo! Jako prezydent Rzeczypospolitej deklaruję gotowość do współpracy z nowo wybranym parlamentem. Najważniejszym moim przesłaniem od samego początku sprawowania urzędu, od 2015 r., była i jest współpraca i jeszcze raz współpraca w najważniejszych dla Polski sprawach. Drzwi Pałacu Prezydenckiego są zawsze otwarte dla wszystkich, którzy są gotowi taką współpracę podejmować. Dziś zdecydowanie najważniejszą sprawą, która wymaga ponadpartyjnej współpracy, jest bezpieczeństwo naszej Ojczyzny. Żyjemy w niebezpiecznych czasach. Pełnoskalowa wojna tuż za naszą wschodnią granicą uświadamia nam to dobitnie, ostatnio każdego dnia. Dziękuję, że w najważniejszych momentach, zaraz po rosyjskiej agresji na Ukrainę, ale także i potem, pokazaliście wszyscy państwo niezwykłą odpowiedzialność. Dziękuję za ponadpartyjne poparcie tutaj, w parlamencie ustawy o obronie Ojczyzny, która umożliwiła zwiększenie finansowania oraz szybszą modernizację i wzmocnienie polskiego wojska. Mam nadzieję, że ten właściwy kierunek zostanie utrzymany, programy zbrojeniowe będą kontynuowane, a wydatki na Siły Zbrojne – utrzymane na poziomie tych co najmniej 4% produktu krajowego brutto. (Oklaski) To powinna być sprawa łącząca dzisiaj i niezmiennie wszystkie ugrupowania zasiadające w parlamencie. Jako zwierzchnikowi Sił Zbrojnych ogromnie mi na tym zależy, bo silne i nowoczesne Wojsko Polskie to najlepsza gwarancja bezpieczeństwa dla naszej Ojczyzny, dla naszych rodaków, dla naszych współobywateli. (Oklaski) Szanowni Państwo! Musimy szybko wyciągać wnioski z tego, co dzieje się na Ukrainie. Musimy je wyciągać po to, by jeszcze skuteczniej dbać o bezpieczeństwo naszego kraju i kontynentu. Dlatego właśnie pod koniec kadencji poprzedniego parlamentu złożyłem w Sejmie projekt ustawy o działaniach organów władzy państwowej na wypadek zewnętrznego zagrożenia bezpieczeństwa państwa – ustawy, która reformuje system dowodzenia polskiej armii. Zapraszam do współpracy nad tym niezwykle ważnym tematem. Mam nadzieję, że w rozpoczynającej się właśnie kadencji Sejmu ta ważna ustawa zostanie przez państwa uchwalona ponad wszelkimi podziałami. Zbliżający się rok 2024 to rok dwóch ważnych jubileuszy: 25-lecia przystąpienia Polski do Sojuszu Północnoatlantyckiego oraz 20-lecia wejścia Polski do Unii Europejskiej. Obecność Polski w NATO, jak i w Unii Europejskiej to fundamenty naszego bezpieczeństwa, to polska racja stanu. Mówiłem o tym wielokrotnie. Dlatego tak ważna jest dobra współpraca także w zakresie polityki międzynarodowej. Dobre przygotowanie do kolejnego szczytu Sojuszu Północnoatlantyckiego, który odbędzie się w przyszłym roku w Waszyngtonie, a także do polskiej prezydencji w Unii Europejskiej, która będzie miała miejsce w pierwszym półroczu 2025 r. Będziemy wówczas gospodarzem wielu niezwykle istotnych wydarzeń związanych z funkcjonowaniem Unii, relacjami transatlantyckimi, interesami gospodarczymi całej Wspólnoty. Najważniejszym celem polskiej prezydencji będzie zacieśnianie relacji Unii Europejskiej ze Stanami Zjednoczonymi. Chcemy również dalszego rozszerzania Unii na Wschód i Południe. Kolejna ważna kwestia to przygotowywanie planu odbudowy Ukrainy po wojnie, wreszcie sprawiedliwa i mądrze zrealizowana transformacja energetyczna. Już dziś musimy zacząć przygotowywać się do tego niezwykle ważnego czasu. Szanowni Państwo! „Winni jesteśmy wobec kraju zapomnieć nareszcie o tym, co nas dzieli, a pomyśleć o tym, co nas może jednoczyć” – te słowa wypowiedziane przez wybitnego marszałka Sejmu Macieja Rataja są mi szczególnie bliskie. Przed wyborami w 2020 r. apelowałem, żeby budować koalicję polskich spraw wokół najważniejszych dla naszej Ojczyzny tematów, takich jak rodzina, bezpieczeństwo, praca, inwestycje oraz godność Polski i Polaków. I chcę z tego miejsca wyraźnie powiedzieć: taka koalicja polskich spraw jest Polsce nadal bardzo potrzebna. Może to być oczywiście koalicja rządowa, choć nie musi. Może mieć również formułę szerokiej koalicji parlamentarnej, skupionej wokół kluczowych dla Polski tematów. Chciałbym, żeby była to koalicja złożona również z samorządowców, organizacji społecznych i pozarządowych, wszystkich, którym dobro naszej Ojczyzny leży szczególnie głęboko na sercu. Zapraszam wszystkich do takiej szerokiej koalicji polskich spraw. W takim duchu będę też postępował do końca swojej prezydentury. Szanowni Państwo! Równocześnie chciałbym wyraźnie powiedzieć, że będę stał na straży najważniejszych osiągnięć ostatnich 8 lat. To było dobrych 8 lat dla Polski i dla Polaków. (Oklaski) To było dobrych 8 lat z bilansem dodatnim, w których mimo dramatycznie trudnych wyzwań, takich jak kryzys wywołany na świecie pandemią koronawirusa i rosyjska agresja na Ukrainę, udało się utrzymać stabilność systemu finansowego, naszej waluty i udało się, co niezwykle ważne, utrzymać miejsca pracy. Dlatego wsparcie dla rodzin, kluczowe programy społeczne: 500, a już wkrótce 800+, obniżenie wieku emerytalnego, wsparcie dla emerytów i wiele innych, muszą zostać utrzymane. (Oklaski) Muszą być kontynuowane. Musi też zostać utrzymana i być kontynuowana stabilność finansowa i gospodarcza państwa. (Oklaski) Podkreślam to wyraźnie i podkreślałem w trakcie powyborczych konsultacji ze wszystkimi komitetami wyborczymi. Ja swoje słowo traktuję niezwykle poważnie i tego słowa z całą pewnością dotrzymam. (Oklaski) Szanowni Państwo! Nie zgodzę się na żadne próby ograniczania, podważania czy kwestionowania konstytucyjnych uprawnień prezydenta. (Oklaski) Z dwóch kadencji, przez które pełnię swój urząd, zostało mi zaledwie już 20 miesięcy urzędowania. (Oklaski) (Głosy z sali: Ooo…) (Głos z sali: Brawo!) Nie robię tego i nie będę robił dla siebie, ale dla Polski i dla kolejnych prezydentów, którzy przyjdą po mnie. (Oklaski) (Głos z sali: Brawo!) Porządek konstytucyjny musi zostać zachowany. (Głos z sali: Przywrócony.) Nie zgodzę się na żadne obchodzenie czy naginanie prawa. (Poruszenie na sali, oklaski) (Głos z sali: Ha, ha, ha!) Zawsze broniłem i będę bronił dwóch najważniejszych polskich wartości, o które walczyły całe pokolenia: wolności i solidarności. (Oklaski) Jeżeli uznam, że jakieś rozwiązanie budzi poważne wątpliwości merytoryczne czy prawne, to nie zawaham się skorzystać z prezydenckiego weta czy skierować ustawy do Trybunału Konstytucyjnego. (Oklaski) Obóz polityczny, z którego się wywodzę, przekonał się o tym wielokrotnie… (Głos z sali: Ha, ha, ha!) …także w odniesieniu do niezwykle głośnych medialnie ustaw w ciągu ostatnich 8 lat. Chciałbym jednak z tego miejsca wyraźnie powiedzieć wszystkim formacjom politycznym, że ewentualne weto prezydenta nie może być usprawiedliwieniem dla niezrealizowania państwa zapowiedzi i obietnic wyborczych. (Poruszenie na sali, oklaski) (Głos z sali: Brawo!) (Głosy z sali: Ha, ha, ha!) Ja swoje słowa traktuję niezwykle poważnie. (Głos z sali: Ha, ha, ha!) Wy też macie obietnice, które złożyliście Polakom, i bardzo proszę, zrealizujcie je. (Oklaski) Najpierw to na tej sali musi paść odpowiedź, czy jest większość wobec konkretnego projektu ustawy. Ja ostateczne decyzje będę podejmował dopiero wtedy, kiedy na moje biurko będą trafiały uchwalone już ustawy. Ale proszę pamiętać, że zawsze także wcześniej gotów jestem do konsultacji, jeżeli ktoś będzie miał taką wolę, żeby skonsultować się z prezydentem Rzeczypospolitej. Tak jak powiedziałem, drzwi Pałacu Prezydenckiego są i będą otwarte. Szanowni Państwo! Przyszłość ma na imię Polska. Z takim przesłaniem startowałem w wyborach w 2015 r. Nie zmieniłem zdania – nadal głęboko wierzę w Polskę, wierzę w Polaków, wierzę w pomyślną przyszłość naszej Ojczyzny. Chcemy ambitnej Polski, Polski, która rozwija swój potencjał, która tworzy dobrze płatne miejsca pracy dla naszych obywateli, Polski, która będzie konkurować w kolejnych dziedzinach z innymi państwami. Jednak żeby się tak stało, niezbędne są inwestycje i niezbędny jest rozwój. To państwo polskie musi dawać impuls, to państwo polskie musi dawać przykład. Wiedzieli o tym doskonale ojcowie naszej niepodległości. To dlatego dopiero co odradzające się państwo polskie, które przecież musiało scalić trzy zabory z różną infrastrukturą, z różnym porządkiem prawnym, podjęło się niesłychanie ambitnych wyzwań, takich jak budowa Centralnego Okręgu Przemysłowego, jak budowa Gdyni – polskiego okna na świat. Jak mówił wówczas twórca Gdyni i Centralnego Okręgu Przemysłowego wicepremier Eugeniusz Kwiatkowski: „w tym bowiem miejscu Europy, gdzie leży Polska, istnieć może tylko państwo silne, rządne, świadome swych trudności i swego celu, wolne (…), zwarte i zorganizowane, solidarne i silne wewnętrznie, budzące szacunek na zewnątrz (…). Czy możemy wahać się, stojąc u drogowskazu, gdzie pójść?”. Dziś jako Polska stoimy przed podobnymi wyzwaniami i potrafimy na nie odpowiedzieć. Wybudowana niemal od podstaw sieć dróg ekspresowych i autostrad, które połączyły największe polskie miasta i wszystkie regiony. Gazoport w Świnoujściu, który rozbudowujemy. Wreszcie odważna i dalekowzroczna decyzja o budowie gazociągu Baltic Pipe. To tylko niektóre z projektów. Warto sobie głośno zadać pytanie, gdzie bylibyśmy dzisiaj, gdyby nie budowa gazoportu, gdyby nie budowa interkonektorów gazowych. (Oklaski) (Poseł Jakub Rutnicki: No właśnie.) Gdzie bylibyśmy dzisiaj, gdyby nie budowa Baltic Pipe? Dlatego właśnie Polska musi stawiać sobie kolejne ambitne cele. Takim ambitnym projektem jest budowa Centralnego Portu Komunikacyjnego… (Oklaski) (Głos z sali: Brawo!) …który ma być nowym polskim oknem na świat – tym razem w wymiarze lotniczym – ale również krokiem milowym w rozwoju infrastruktury kolejowej łączącej najdalsze zakątki Polski. Takim ambitnym projektem jest budowa polskich elektrowni atomowych, która istotnie zwiększy nasze bezpieczeństwo energetyczne (Oklaski) i pozwoli zrealizować zobowiązania z zakresu ochrony klimatu. Wreszcie takim ambitnym projektem jest dalsza i konsekwentna rozbudowa polskich portów, w tym budowa portu kontenerowego w Świnoujściu. (Oklaski) Tych ambitnych projektów będę jako prezydent Rzeczypospolitej bronił, będę im patronował, będę dbał o to, by zostały zrealizowane. (Oklaski) To dzisiaj rozstrzygają się losy Polski na dziesięciolecia i nie stać nas na bezczynność, nie stać nas na brak ambicji, nie stać nas na podporządkowywanie się. Potrzebujemy inwestycji, ale potrzebujemy też wyzwań, które dadzą nam impuls do działania. Takim impulsem było swego czasu polsko-ukraińskie Euro 2012. Olbrzymi sukces naszego kraju, olbrzymi sukces naszego społeczeństwa ponad podziałami politycznymi (Oklaski), bo ponad podziałami politycznymi to zostało zrealizowane. Zostało uzyskane przez jedną stronę sceny politycznej, a zrealizowane za rządów drugiej strony sceny politycznej i było sukcesem Polski. Wspólnym. Szanowni Państwo! Ten olbrzymi sukces naszego kraju udowodnił, to my udowodniliśmy, że potrafimy wspaniale zorganizować wielką imprezę, wielkie wydarzenie sportowe. (Poseł Barbara Nowacka: Sasinaria?) Takim impulsem może być w przyszłości organizacja przez Polskę igrzysk olimpijskich. Nie bójmy się marzyć, ale bądźmy ambitni i realizujmy nasze marzenia. (Oklaski) Szanowni Państwo! Drodzy Rodacy! Za nami długa i intensywna kampania wyborcza. Czas walki o jak najlepszy wynik, zaciętej często rywalizacji o mandaty poselskie. Któż lepiej niż państwo to wie? Kampanii zawsze towarzyszą olbrzymie emocje i wysoka temperatura sporów. Tak jest na całym świecie, taka jest jej natura – Polska nie jest tu żadnym wyjątkiem. To czas ostrych sporów i ostrych wystąpień. Były wielkie emocje i spory: w pracy, wśród znajomych, często też w rodzinach. To normalne. Ale ten czas już za nami. Dlatego tak jak w 2019 r., tak i dziś chciałbym po zakończeniu swojego wystąpienia powtórzyć gest podania dłoni wszystkim państwu posłom i posłankom poprzez symboliczne podanie dłoni tym, którzy zasiadają w pierwszych rzędach tutaj, w Sejmie. Niech to będzie symboliczne zakończenie okresu kampanii, niech stanie się to dobrą tradycją w naszym parlamencie. Tak zaczynajmy każde pierwsze posiedzenie nowego Sejmu – od podania sobie ręki. Nie tylko z prezydentem, ale od podania sobie ręki nawzajem. Pamiętajmy o słowach Wincentego Witosa, trzykrotnego premiera, kolejnego z ojców naszej niepodległości: „Nie ma sprawy ważniejszej niż Polska”. To jest prawda. Nie ma. (Oklaski) Nie ma sprawy ważniejszej niż Polska. Niech żyje niepodległa i demokratyczna Rzeczpospolita! Boże, błogosław Polsce, błogosław naszą Ojczyznę! Dziękuję. (Część posłów wstaje, oklaski) (Głosy z sali: Brawo!) (Prezydent Rzeczypospolitej Polskiej Andrzej Duda podchodzi do posłów w pierwszym rzędzie i podaje im rękę)",
                },
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Dziękuję panu prezydentowi. Szanowny Panie Prezydencie! Szanowny Panie Były Prezydencie! Szanowny Panie Marszałku Seniorze Senatu! Szanowny Panie Premierze! Czcigodni Goście! Panie Posłanki! Panowie Posłowie! „Jest Polska, jest Sejm – jej przedstawicielstwo” – tymi słowami Macieja Rataja, marszałka Sejmu odrodzonej przed ponad 100 laty naszej ojczyzny, pragnę podkreślić uroczysty moment inauguracji X kadencji Sejmu Rzeczypospolitej Polskiej. Wypowiadający je wybitny nasz poprzednik widział Polskę jako państwo demokracji parlamentarnej. Urzeczywistnienie tej wizji, tego narodowego pragnienia, jest także dziś naszym wspólnym zadaniem i obowiązkiem. Jako marszałek senior w imieniu nas wszystkich, nowo wybranych posłanek i posłów, składam podziękowania Polkom i Polakom, którzy tak licznie w kraju i za granicą z wielkim zaangażowaniem, niekiedy z poświęceniem wykonali swój obywatelski obowiązek udziału w wyborach parlamentarnych, upoważniając nas i zobowiązując do podjęcia troski o dobro wspólne – Rzeczpospolitą. (Oklaski) Gratuluję wybranym 15 października posłankom i posłom, życząc państwu, by każdy dzień realizacji powierzonego przez naród mandatu przedstawicielskiego dawał poczucie spełnienia zamierzeń, które dobrze służą Polsce. Wyrażam nadzieję, że nowa kadencja pozwoli odbudować, począwszy od nas, poczucie wspólnoty narodowej, za którą opowiedziało się tak wielu wyborców. (Oklaski) Dziękuję panu prezydentowi Andrzejowi Dudzie za jego obecność podczas tej uroczystej inauguracji nowej kadencji Sejmu oraz za wygłoszone słowa, które dają nadzieję, że poszanowanie ustrojowej zasady współdziałania władz pozwoli nam zmieniać Polskę zgodnie z oczekiwaniami narodu. (Oklaski) Powierzenie mi obowiązków marszałka seniora poczytuję jako dostrzeżenie, docenienie i podkreślenie dokonań wszystkich parlamentarzystów, z którymi na przestrzeni ostatnich 30 lat przyszło mi uczestniczyć w szczególności w opracowaniu i przyjęciu konstytucji z 1997 r. oraz w realizacji starań o polskie członkostwo w NATO oraz Unii Europejskiej. Szeroka konsolidacja klasy politycznej wokół tej miary celów i skuteczność w ich osiąganiu stanowi dobry wzorzec i inspirację dla współczesnych przedstawicieli obywateli Rzeczypospolitej. Polska bowiem, z jej potencjałem ludzkim, ekonomicznym i politycznym, zasługuje i jest do tego zdolna, aby zająć godne miejsce w strukturach społeczności międzynarodowej, aktywnie uczestnicząc w ustalaniu i realizacji programów ich działania. Trudna i wymagająca współczesność, naznaczona toczącymi się konfliktami zbrojnymi m.in. w Ukrainie i na Bliskim Wschodzie, jak również stagflacja gospodarcza w Polsce i w Europie stawiają przed nami wyzwania, którym sprostanie wymaga wspólnego przyjęcia i pełnego wdrożenia dyrektyw, jakie ustrojodawca zawarł w preambule do Konstytucji Rzeczypospolitej Polskiej. Szczególnie dziś aktualizuje się potrzeba przywrócenia współpracy ze wszystkimi krajami dla dobra rodziny ludzkiej. Wynegocjowany 20 lat temu format naszej obecności w Unii Europejskiej dał obecnym i przyszłym pokoleniom możliwość społecznego i gospodarczego rozwoju. Podejmijmy więc starania, by nasz kraj powrócił do awangardy wartości europejskich, które – osadzone na chrześcijańskim dziedzictwie, na inspiracjach czerpanych z tradycji demokracji ateńskiej i prawa rzymskiego – stanowią solidny fundament odbudowy i umacniania wspólnoty narodów, Europy ojczyzn. (Oklaski) Motywację w tym zakresie czerpiemy z młodych polskich serc, które integracji pragną i oczekują, aspirując do pełnego uczestnictwa w opartym na zasadzie równości, akceptacji, na wiedzy i innowacjach europejskim dobrobycie. Niech w tych staraniach nie będą przeszkodą formułowane w gmachu Trybunału Konstytucyjnego rzekome sprzeczności polskiej konstytucji z traktatami konstytuującymi Unię Europejską. (Oklaski) Ustrojodawca w treści preambuły wzywa nas także do respektowania praw obywatelskich oraz do zapewnienia działaniu instytucji publicznych rzetelności i sprawności. Nie ma prawdziwej demokracji, nie ma inkluzywnej i skutecznej polityki publicznej bez otwartego parlamentaryzmu. Wysokie standardy postępowania ustawodawczego i towarzyszących mu konsultacji, jawna i rozważna debata, rzeczywista kontrola parlamentarna, ponadpartyjne podejście do kompetencji kreacyjnych Sejmu, a także przywrócenie konstytucyjnej postaci i znaczenia budżetu państwa oraz kontroli nad jego wykonaniem to w moim przekonaniu warunki konieczne respektowania istoty ustrojowej funkcji Wysokiej Izby. (Oklaski) Są dwa fundamenty, na których powinna opierać się działalność każdej władzy, a przede wszystkim parlamentu: państwo prawa i godność człowieka. Apeluję przy tym, by artykułowane przez większość parlamentarną wyzwanie przywrócenia i wzmacniania praworządności podjąć i realizować z poszanowaniem zasady legalizmu. (Oklaski) Delikty, jakich dopuszczono się przy wykonywaniu powierzonej władzy, mogą być sprawiedliwie ocenione i naprawione tylko środkami respektującymi obowiązujące prawo i konstytucyjny podział kompetencji. (Oklaski) Jestem pewien, że uczciwe zamiary uzdrowienia polskiej struktury państwowej znajdą wsparcie i sojuszników wśród przedstawicieli wszystkich sił politycznych w parlamencie. Ufam, że jesteśmy w stanie wspólnie pamiętać i doceniać zasługi Kościoła katolickiego i innych Kościołów (Oklaski) na naszej drodze do odzyskania w 1989 r. suwerenności ojczyzny, zaangażowanie w budowanie patriotycznej duchowości narodu oraz prowadzenie działalności charytatywno-opiekuńczej. (Oklaski) Rozumiem tych, którzy uważają, że w ostatnich latach określona w postanowieniach konstytucji i konkordatu linia demarkacyjna rozgraniczająca pola ingerencji pomiędzy polityką państwa a misją Kościoła została naruszona, wywołując niekiedy poczucie krzywdy (Oklaski) lub poczucie nadużycia. Jestem jednak przekonany, że z poszanowaniem zasad funkcjonowania demokratycznego państwa uda się nam przywrócić właściwe relacje pomiędzy państwem a działającymi w Polsce Kościołami, gwarantując wszystkim wiernym poszanowanie wolności religijnej, zaś instytucjom publicznym neutralny światopoglądowo charakter. (Oklaski) Umacniając sojusze i wzmacniając potencjał obronny państwa, nie możemy też zapomnieć o znaczeniu daru chleba. Daru chleba, którego brak w wielu częściach świata aktywuje i podsyca konflikty oraz wywołuje kryzysy migracyjne. Dzisiejszą Europę niewątpliwie stać na więcej empatii, ukierunkowanej na rozdysponowanie nadwyżek żywności do braci w dalszych zakątkach świata, którzy jej potrzebują, co ustabilizuje przy tym sytuację na lokalnych rynkach rolnych. Prawo i wolność są największym skarbem narodu, mówił ojciec polskiej Niepodległej, Wincenty Witos, podczas procesu brzeskiego. Hańba jego skazania została dopiero w tym roku zmazana z państwa polskiego orzeczeniem niezawisłych sędziów Sądu Najwyższego. Ufać należy, że wartość tego skarbu będzie przyświecać wszystkim, którzy podjęli się służby państwu i społeczeństwu. Jako długoletni poseł namawiam również, byśmy porzucili przekonanie o naszej omnipotencji w ustalaniu tego, co dobre i słuszne. Wykonując kompetencje prawodawcze, otwórzmy się na współpracę z ekspertami świata nauki i gospodarki oraz z instytucjami społeczeństwa obywatelskiego. Usuńmy bariery, które dzielą nas od tych, którzy nas wybrali, oraz od służących im dziennikarzy. (Oklaski) Słuchajmy narodu, nie tylko w codziennym kontekście w biurach poselskich, w konsultacjach społecznych, ale również w najważniejszych sprawach, odwołując się uczciwie do instytucji referendum. Pamiętajmy, że stanowione przez nas prawo ma być oparte na poszanowaniu wolności i sprawiedliwości, współdziałaniu władz w dialogu społecznym oraz na zasadzie pomocniczości umacniającej uprawnienia obywateli i ich wspólnot. Kończąc, pragnę podkreślić, że w demokratycznym państwie zgodnie z wolą suwerena zmieniają się prezydenci, zmieniają się premierzy i rządy, zmienia się też skład osobowy tej Izby. Jedno przy tym jest stałe i niezmienne: Rzeczpospolita. (Oklaski) Pozwólcie, że z moich ust wybrzmi raz jeszcze przesłanie premiera naszej wolności, Wincentego Witosa: „A Polska winna trwać wiecznie”. (Głos z sali: Brawo!) (Zebrani wstają, długotrwałe oklaski) Wysoka Izbo! Zgodnie z art. 2 ust. 2 regulaminu Sejmu na sekretarzy tymczasowych Sejmu powołuję panią poseł Alicję Łepkowską-Gołaś (Oklaski), panią poseł Dorotę Olko (Oklaski), panią poseł Annę Pieczarkę (Oklaski), panią poseł Wioletę Tomczak (Oklaski), pana posła Ryszarda Wilka (Oklaski), a także panią poseł Bożenę Żelazowską. (Oklaski) Za chwilę przystąpimy do ślubowania poselskiego. Zgodnie z art. 2 ust. 3 regulaminu Sejmu ślubowanie odbywa się w ten sposób, że po odczytaniu roty każdy z kolejno wywoływanych posłów, powstawszy, wypowiada słowo „ślubuję”. Poseł może dodać zdanie: „Tak mi dopomóż Bóg”. Odmowa złożenia ślubowania oznacza zrzeczenie się mandatu poselskiego. Spośród sekretarzy tymczasowych do przeprowadzenia ślubowania powołuję panią poseł Alicję Łepkowską-Gołaś oraz panią poseł Bożenę Żelazowską, które będą odczytywały nazwiska pań i panów posłów oraz zaznaczały nazwiska posłów składających ślubowanie i ewentualnie nieobecnych. Informuję także, że nazwiska posłów będą odczytywane w kolejności zgodnej z porządkiem zajmowanych miejsc na sali posiedzeń Sejmu. Proszę wyznaczonych sekretarzy o podejście do mównicy. Proszę wszystkich obecnych o powstanie i wysłuchanie roty ślubowania. (Zebrani wstają) „Uroczyście ślubuję rzetelnie i sumiennie wykonywać obowiązki wobec Narodu, strzec suwerenności i interesów Państwa, czynić wszystko dla pomyślności Ojczyzny i dobra obywateli, przestrzegać Konstytucji i innych praw Rzeczypospolitej Polskiej”. Dziękuję. Proszę o zajęcie miejsc, a posłów sekretarzy o przystąpienie do swoich obowiązków.",
                },
                {
                    "speaker": "Sekretarz Poseł Bożena Żelazowska",
                    "content": "(Sekretarz poseł odczytuje nazwiska posłów)",
                },
                {
                    "speaker": "Poseł Marek Sawicki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Włodzimierz Czarzasty", "content": "Ślubuję."},
                {"speaker": "Poseł Adam Szłapka", "content": "Ślubuję."},
                {"speaker": "Poseł Barbara Nowacka", "content": "Ślubuję."},
                {"speaker": "Poseł Marcin Kierwiński", "content": "Ślubuję."},
                {"speaker": "Poseł Donald Franciszek Tusk", "content": "Ślubuję."},
                {"speaker": "Poseł Borys Budka", "content": "Ślubuję."},
                {"speaker": "Poseł Izabela Leszczyna", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Szymon Hołownia",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Władysław Kosiniak-Kamysz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Sławomir Mentzen",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Zbigniew Ziobro",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jacek Sasin",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Elżbieta Witek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Mateusz Morawiecki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Barbara Bartuś",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Ryszard Terlecki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jarosław Kaczyński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Mariusz Błaszczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Leonard Krasulski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Andrzej Adamczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Gliński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Łukasz Schreiber",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Mariusz Kamiński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Antoni Macierewicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Tchórzewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Bożena Borys-Szopa",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Bosak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Michał Wawer",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Stanisław Tyszka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Włodzimierz Skalik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Paszyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Zgorzelski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Agnieszka Buczyńska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Paulina Hennig-Kloska", "content": "Ślubuję."},
                {"speaker": "Poseł Urszula Sara Zielińska", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Tomasz Siemoniak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Monika Wielichowska", "content": "Ślubuję."},
                {"speaker": "Poseł Jan Grabiec", "content": "Ślubuję."},
                {"speaker": "Poseł Sławomir Nitras", "content": "Ślubuję."},
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {"speaker": "Poseł Agnieszka Pomaska", "content": "Ślubuję."},
                {"speaker": "Poseł Cezary Tomczyk", "content": "Ślubuję."},
                {"speaker": "Poseł Bartosz Arłukowicz", "content": "Ślubuję."},
                {"speaker": "Poseł Agnieszka Dziemianowicz-Bąk", "content": "Ślubuję."},
                {"speaker": "Poseł Krzysztof Gawkowski", "content": "Ślubuję."},
                {"speaker": "Poseł Dariusz Wieczorek", "content": "Ślubuję."},
                {"speaker": "Poseł Marcin Kulasek", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Tomasz Głogowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Kazimierz Plocke",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Mirosława Nykiel", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Krystyna Skowrońska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Krystyna Szumilas", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Marzena Okła-Drewnowicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Paweł Olszewski", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Zbigniew Konwiński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Izabela Katarzyna Mrzygłocka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Urszula Augustyn",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Joanna Mucha", "content": "Ślubuję."},
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Mirosław Suchoń",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Urszula Pasławska", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Andrzej Grzyb",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Przemysław Wipler",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Konrad Berkowicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Witold Tumanowicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Tuduj",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Ślubuję. Tak mi dopomóż Bóg w Trójcy Jedyny i wszyscy święci.",
                },
                {
                    "speaker": "Poseł Mirosława Stachowiak-Różecka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Iwona Ewa Arent",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Małgorzata Wassermann",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Stanisław Szwed",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Suski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Anita Czerwińska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Sobolewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Ast",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Witold Wojciech Czarnecki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Gróbarczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Małgorzata Gosiewska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Joanna Lichocka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Ewa Malik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {
                    "speaker": "Poseł Waldemar Andzel",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Zbigniew Rau",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jarosław Zieliński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Anna Kwiecień",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marlena Magdalena Maląg",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Henryk Kowalczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Kaleta",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Urszula Rusecka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Andrzej Tomasz Zapałowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Ireneusz Raś",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Michał Kobosko",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Tomasz Zimoch",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Ryszard Petru", "content": "Ślubuję."},
                {"speaker": "Poseł Jacek Protas", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Michał Kołodziejczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Kowal",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Robert Kropiwnicki", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Wojciech Saługa",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Czesław Mroczek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Gadowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Tomasz Piotr Nowak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Bartłomiej Sienkiewicz", "content": "Ślubuję."},
                {"speaker": "Poseł Katarzyna Maria Piekarska", "content": "Ślubuję."},
                {"speaker": "Poseł Katarzyna Kotula", "content": "Ślubuję."},
                {"speaker": "Poseł Katarzyna Ueberhan", "content": "Ślubuję."},
                {"speaker": "Poseł Krzysztof Śmiszek", "content": "Ślubuję."},
                {"speaker": "Poseł Joanna Scheuring-Wielgus", "content": "Ślubuję."},
                {"speaker": "Poseł Marek Rząsa", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Michał Jaros",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Michał Szczerba",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Waldemar Sługocki", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Jarosław Urbaniak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Krząkała",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Jagna Marczułajtis-Walczak", "content": "Ślubuję."},
                {"speaker": "Poseł Dorota Niedziela", "content": "Ślubuję."},
                {"speaker": "Poseł Joanna Kluzik-Rostkowska", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Jakub Rutnicki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Janusz Cichoń",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Krzysztof Brejza", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Tomasz Szymański",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {
                    "speaker": "Poseł Ewa Schädler",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Ewa Szymanowska", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Rafał Komarewicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Zalewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jacek Tomczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Hetman",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Ryszard Wilk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Roman Fritz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg w Trójcy Jedyny i wszyscy święci.",
                },
                {
                    "speaker": "Poseł Zbigniew Chmielowiec",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marzena Anna Machałek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jerzy Polaczek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jarosław Sellin",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Anna Krupka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Dariusz Piontkowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Grzegorz Woźniak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jan Mosiński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jan Krzysztof Ardanowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Sylwester Tułajew",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Babinetz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Kuchciński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Paweł Szefernaker",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Małgorzata Golińska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Czesław Hoc",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Teresa Wilk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Lidia Burzyńska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Joanna Borowiak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jacek Osuch",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Arkadiusz Mularczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Kazimierz Smoliński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Matuszewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Arkadiusz Czartoryski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Rafał Weber",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Waldemar Buda",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Szymon Szynkowski vel Sęk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marcin Horała",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Müller",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Maciej Małecki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Szymon Giżyński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Rychlik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Sławomir Zawiślak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {
                    "speaker": "Poseł Bartłomiej Wróblewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Karina Anna Bosak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Mulawa",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Bronisław Foltyn",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Urszula Nowogórska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Mirosław Maliszewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Władysław Bartoszewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Aleksandra Leo", "content": "Ślubuję."},
                {"speaker": "Poseł Barbara Oliwiecka", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Kamil Wnuk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Śliz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Małgorzata Niemczyk", "content": "Ślubuję."},
                {"speaker": "Poseł Agnieszka Hanajczyk", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Mariusz Witczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Jarosław Wałęsa", "content": "Ślubuję."},
                {"speaker": "Poseł Artur Daniel Gierada", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Krystyna Sibińska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Maria Małgorzata Janyska", "content": "Ślubuję."},
                {"speaker": "Poseł Elżbieta Gapińska", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Małgorzata Pępek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Henryka Krzywonos-Strycharska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Barbara Dolniak", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Bogdan Andrzej Zdrojewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Sowa",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Monika Rosa", "content": "Ślubuję."},
                {"speaker": "Poseł Katarzyna Anna Lubnauer", "content": "Ślubuję."},
                {"speaker": "Poseł Witold Zembaczyński", "content": "Ślubuję."},
                {"speaker": "Poseł Marcelina Zawisza", "content": "Ślubuję."},
                {"speaker": "Poseł Adrian Zandberg", "content": "Ślubuję."},
                {"speaker": "Poseł Dorota Olko", "content": "Ślubuję."},
                {"speaker": "Poseł Daria Gosek-Popiołek", "content": "Ślubuję."},
                {"speaker": "Poseł Anna Maria Żukowska", "content": "Ślubuję."},
                {"speaker": "Poseł Tomasz Kostuś", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Ewa Kołodziej",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Paweł Suski", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Grzegorz Bernard Napieralski",
                    "content": "Ślubuję.",
                },
                {
                    "speaker": "Poseł Zdzisław Gawlik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Elżbieta Gelert",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Marek Tomasz Hok", "content": "Ślubuję."},
                {"speaker": "Poseł Rajmund Miller", "content": "Ślubuję."},
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {"speaker": "Poseł Gabriela Lenartowicz", "content": "Ślubuję."},
                {"speaker": "Poseł Zofia Czernow", "content": "Ślubuję."},
                {"speaker": "Poseł Arkadiusz Marchewka", "content": "Ślubuję."},
                {"speaker": "Poseł Kamila Gasiuk-Pihowicz", "content": "Ślubuję."},
                {"speaker": "Poseł Aleksander Miszalski", "content": "Ślubuję."},
                {"speaker": "Poseł Krzysztof Truskolaski", "content": "Ślubuję."},
                {"speaker": "Poseł Arkadiusz Myrcha", "content": "Ślubuję."},
                {"speaker": "Poseł Marcin Skonieczka", "content": "Ślubuję."},
                {"speaker": "Poseł Wioleta Tomczak", "content": "Ślubuję."},
                {"speaker": "Poseł Rafał Kasprzyk", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Dariusz Klimczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Bejda",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Zbigniew Sosnowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Agnieszka Maria Kłopotek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Grzegorz Adam Płaczek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Andrzej Kosztowniak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Edward Siarka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Józefa Szczurek-Żelazko",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Polak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jacek Świat",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Anna Gembicka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Daniel Milewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Robert Telus",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Grzegorz Matusiak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jan Warzecha",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Lipiec",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Zbigniew Dolata",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Artur Soboń",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Grzegorz Puda",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Anna Schmidt",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Maciej Wąsik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Rafał Bochenek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Zbigniew Hoffmann",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jan Michał Dziedziczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Bartosz Józef Kownacki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Wojciech Michał Zubowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Hreniak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Agnieszka Anna Soin",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Elżbieta Duda",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Anna Milczanowska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {
                    "speaker": "Poseł Kamil Bortniczuk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Tadeusz Woźniak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Król",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Katarzyna Czochara",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Kazimierz Gołojuch",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marcin Przydacz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Andrzej Kryj",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Jabłoński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Wiesław Krajewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Ryszard Bartosik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Janusz Cieszyński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Szrot",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Aleksander Mikołaj Mrówczyński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Uruski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Tomasz Zieliński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Robert Warwas",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jerzy Materna",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Sławomir Skwarek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Agnieszka Wojciechowska van Heukelom",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marcin Romanowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Michał Pyrzyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Tadeusz Samborski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Czesław Siekierski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Adam Dziedzic",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Adam Luboński", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Żaneta Cwalina-Śliwowska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Łukasz Osmalak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Dariusz Joński", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Konrad Frysztak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Aleksandra Gajewska", "content": "Ślubuję."},
                {"speaker": "Poseł Michał Krawczyk", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Katarzyna Matusik-Lipiec",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Kinga Gajewska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Marta Golbik", "content": "Ślubuję."},
                {"speaker": "Poseł Andrzej Szewiński", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Krzysztof Grabczuk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Wojciech Król",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Iwona Maria Kozłowska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Joanna Frydrych",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marta Wcisło",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {
                    "speaker": "Poseł Roman Giertych",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Borys",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Danuta Jazłowiecka", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Alicja Chybicka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Robert Dowhan", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Stanisław Lamczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Paulina Matysiak", "content": "Ślubuję."},
                {"speaker": "Poseł Joanna Wicha", "content": "Ślubuję."},
                {"speaker": "Poseł Maciej Konieczny", "content": "Ślubuję."},
                {"speaker": "Poseł Anita Kucharska-Dziedzic", "content": "Ślubuję."},
                {"speaker": "Poseł Wanda Nowicka", "content": "Ślubuję."},
                {"speaker": "Poseł Tomasz Dominik Trela", "content": "Ślubuję."},
                {"speaker": "Poseł Stanisław Gorczyca", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Robert Wardzała",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Franciszek Sterczewski", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Mateusz Bochenek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Karolina Pawliczak", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Iwona Hartwich",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Bogusław Wołoszański", "content": "Ślubuję."},
                {"speaker": "Poseł Iwona Małgorzata Krawczyk", "content": "Ślubuję."},
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {"speaker": "Poseł Klaudia Jachira", "content": "Ślubuję."},
                {"speaker": "Poseł Małgorzata Tracz", "content": "Ślubuję."},
                {"speaker": "Poseł Katarzyna Osos", "content": "Ślubuję."},
                {"speaker": "Poseł Magdalena Filiks", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Lucjan Marek Pietrzczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Adamowicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Marcin Bosacki", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Piotr Głowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Elżbieta Anna Polak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jacek Karnowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Maciej Lasek", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Grzegorz Rusiecki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Anna Wojciechowska", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Artur Jarosław Łącki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Paweł Strach",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Izabela Bodnar", "content": "Ślubuję."},
                {"speaker": "Poseł Piotr Górnikiewicz", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Sławomir Ćwik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Magdalena Sroka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jolanta Zięba-Gzik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {
                    "speaker": "Poseł Stanisław Tomczyszyn",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jarosław Rzepa",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Kazimierz Bogusław Choma",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Bartłomiej Dorywalski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Filip Kaczyński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Sebastian Kaleta",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Adam Andruszkiewicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Maria Kurowska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Olga Ewa Semeniuk-Patkowska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Norbert Jakub Kaczmarczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jarosław Wiesław Wieczorek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Mariusz Gosek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Łukasz Kmita",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Agnieszka Ścigaj",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Maria Koc",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Andrzej Gawron",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Kazimierz Gwiazdowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Ciecióra",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jacek Bogucki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Ewa Leniart",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Bolesław Piecha",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Artur Szałabawka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Władysław Dajczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Artur Chojecki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Zbigniew Bogucki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Piotr Uściński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Zbigniew Krzysztof Kuźmiuk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Radosław Fogiel",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Andrzej Śliwka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Dorota Arciszewska-Mielewczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Sałek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Michał Paweł Dworczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Kubów",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marcin Gwóźdź",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Szczucki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Agata Wojtyszek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Przemysław Drabek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Szymon Pogoda",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Dariusz Stefaniuk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Grzegorz Lorek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {
                    "speaker": "Poseł Ireneusz Zyska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Michał Moskal",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Grzegorz Piechowiak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marcin Ociepa",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marcin Warchoł",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Anna Dąbrowska-Banaszek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Kacper Płażyński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Anna Ewa Cicholska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marcin Porzucek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Mariusz Kałużny",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Michał Woś",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Łukasz Mejza",
                    "content": "Ślubuję. Tak mi dopomóż Bóg. (Głosy z sali: Uuu…) (Głos z sali: Skandal!)",
                },
                {
                    "speaker": "Poseł Dominika Chorosińska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Czarnecki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jan Kanthak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Wesoły",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Tadeusz Chrzan",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Teresa Pamuła",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Władysław Kurowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Henryk Kiepura",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Stefan Krajewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Zbigniew Ziejewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Bartosz Romowicz", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Adam Michał Gomoła",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Elżbieta Jolanta Burkiewicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marek Gzik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Przemysław Witek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Apoloniusz Tajner", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Magdalena Małgorzata Kołodziejczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Renata Urszula Rak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Henryk Szopiński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Katarzyna Kierzek-Koperska", "content": "Ślubuję."},
                {"speaker": "Poseł Andrzej Domański", "content": "Ślubuję."},
                {"speaker": "Poseł Adam Krzemiński", "content": "Ślubuję."},
                {"speaker": "Poseł Piotr Kandyba", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Małgorzata Gromadzka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Iwona Karolewska", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Piotr Lachowicz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Weronika Smarduch", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Paweł Bliźniuk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {"speaker": "Poseł Marcin Józefaciuk", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Krzysztof Habura",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Łukasz Horbatowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Anna Sobolak", "content": "Ślubuję."},
                {"speaker": "Poseł Tadeusz Tomaszewski", "content": "Ślubuję."},
                {"speaker": "Poseł Wiesław Szczepański", "content": "Ślubuję."},
                {"speaker": "Poseł Andrzej Szejna", "content": "Ślubuję."},
                {"speaker": "Poseł Arkadiusz Sikora", "content": "Ślubuję."},
                {"speaker": "Poseł Jacek Czerniak", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Łukasz Litewka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Jolanta Niezgodzka", "content": "Ślubuję."},
                {"speaker": "Poseł Sylwia Bielawska", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Marek Jan Chmielewski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Aleksandra Karolina Wiśniewska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Adrian Witczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Dorota Marek", "content": "Ślubuję."},
                {"speaker": "Poseł Włodzisław Giziński", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Krystian Łuczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Krzysztof Bojarski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Dorota Łoboda", "content": "Ślubuję."},
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {"speaker": "Poseł Paweł Papke", "content": "Ślubuję."},
                {"speaker": "Poseł Maciej Wróbel", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Bartosz Zawieja",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Patryk Jaskulski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Patryk Gabriel", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Rafał Siemaszko",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Jacek Niedźwiedzki", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Łukasz Ściebiorowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Norbert Pietrykowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Barbara Okuła", "content": "Ślubuję."},
                {"speaker": "Poseł Michał Gramatyka", "content": "Ślubuję."},
                {"speaker": "Poseł Maja Ewa Nowak", "content": "Ślubuję."},
                {"speaker": "Poseł Marek Biernacki", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Radosław Lubczyk",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Mirosław Adam Orliński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Wiesław Różyński",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Janusz Kowalski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Patryk Wicher",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Wojciech Szarama",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Paweł Kukiz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {
                    "speaker": "Poseł Marek Jakubiak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jarosław Sachajko",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Robert Gontarz",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Fryderyk Sylwester Kapinos",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Michał Cieślak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Michał Wójcik",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Dariusz Matecki",
                    "content": "Ślubuję. Tak mi dopomóż Bóg. (Głosy z sali: Uuu…) (Głos z sali: Hejter!)",
                },
                {
                    "speaker": "Poseł Andrzej Gut-Mostowy",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Poseł Sebastian Łukaszewicz", "content": "Ślubuję."},
                {
                    "speaker": "Poseł Mariusz Krystian",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Grzegorz Gaża",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Jacek Ozdoba",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Przemysław Czarnek",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Katarzyna Sójka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Agnieszka Górska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Marcin Grabowski",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Magdalena Filipek-Sobczak",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {
                    "speaker": "Poseł Anna Pieczarka",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Alicja Łepkowska-Gołaś", "content": ""},
                {
                    "speaker": "Poseł Bożena Żelazowska",
                    "content": "Ślubuję. Tak mi dopomóż Bóg.",
                },
                {"speaker": "Sekretarz Poseł Bożena Żelazowska", "content": ""},
                {"speaker": "Poseł Alicja Łepkowska-Gołaś", "content": "Ślubuję."},
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Czy ktoś z obecnych pań i panów posłów nie złożył ślubowania? Nikt się nie zgłasza. Stwierdzam, że wszyscy posłowie obecni do tej chwili na posiedzeniu złożyli ślubowanie poselskie. (Oklaski) Proszę o zabranie głosu prezesa Rady Ministrów pana Mateusza Morawieckiego w trybie art. 162 ust. 1 konstytucji. (Oklaski)",
                },
                {
                    "speaker": "Prezes Rady Ministrów Mateusz Morawiecki",
                    "content": "Wielce Szanowny Panie Prezydencie! Szanowny Panie Marszałku! Szanowna Pani Marszałek! Szanowny Panie Prezydencie! Szanowne Panie i Panowie Posłowie! Senatorowie! Panie Marszałku! Panie Marszałku Seniorze Senatu! Wszyscy Szanowni Goście! Zgodnie z parlamentarnym obyczajem chciałem dzisiaj na ręce pana marszałka seniora złożyć z jednej strony sprawozdanie i złożyć dymisję… (Głos z sali: Nie.) (Głos z sali: Jakie sprawozdanie?) …a z drugiej strony chciałem przedstawić naszym rodakom pokrótce, jak to jest przyjęte w naszym Sejmie, krótką panoramę ostatnich 4 lat, co udało się zrobić, na co powinniśmy zwrócić uwagę szczególną. (Głos z sali: Nie.) (Głos z sali: Nie trzeba.) Przed chwilą wszyscy ślubowaliśmy uroczyście wobec narodu strzec suwerenności i niech te słowa przyświecają nam szczególnie w najbliższym czasie, ponieważ zdajemy sobie na pewno doskonale sprawę z tego, jak wielkie wyzwania ten najbliższy czas będzie przynosił. 2 dni temu obchodziliśmy Święto Niepodległości Polski, 105. rocznicę odzyskania niepodległości. TaSekretarz Poseł Alicja Łepkowska-Gołaś kie wielkie, wspaniałe nasze święto zobowiązuje. Ono mówi o tym, że o niepodległość trzeba dbać, trzeba ją szanować, trzeba zabiegać o nią, trzeba czuwać nad niepodległością, suwerennością. I obok krótkiego podsumowania także będę chciał kilka zdań powiedzieć na ten jakże kluczowy temat, w sprawie którego przed chwilą wszyscy ślubowaliśmy właśnie tej suwerenności strzec, niepodległości strzec, a więc jest naszym poselskim zobowiązaniem. Ale zanim do tego przejdę, krótko chciałem powiedzieć o tych ostatnich 4 latach, a także o pewnych wspólnych mianownikach tych 4 lat. To też przecież jest bardzo ważne. Pierwszym wspólnym mianownikiem naszych 4 czy 8 lat, myślę, że pewną nowością w polskiej polityce, może nie absolutną nowością, ale w takim natężeniu czymś zupełnie wyjątkowym była wiarygodność realizacji tych zapowiedzi, które wcześniej obiecywaliśmy wyborcom. (Oklaski) To wprawdzie powinno być coś oczywistego, ale nie było to powszechnie stosowaną walutą polityczną. Dlatego chcę podkreślić wagę tego z punktu widzenia tego, co udało się zrealizować, ale także naszego programu na przyszłość, ponieważ w tym momencie chcę podziękować panu prezydentowi za oświadczenie, które złożył, i powiedział o tym, że będzie chciał mnie desygnować na funkcję prezesa Rady Ministrów. I właśnie w oparciu o te nasze zobowiązania będę chciał również nakłonić Wysoką Izbę do tego, aby poparła mnie w tej funkcji, która została mi powierzona. (Głos z sali: Nie ma szans.) (Głos z sali: Daj spokój już.) (Głos z sali: Bez szans.) Bardzo dziękuję, panie prezydencie. (Oklaski) A więc po pierwsze, wiarygodność, ale drugim wspólnym mianownikiem, takim praźródłem naszego sukcesu w dziedzinie spraw społecznych, co jest chyba dość powszechnie doceniane w polskim społeczeństwie, także i po tej stronie parlamentu, a zwłaszcza po stronie lewicowej, która przecież tak często podnosi wagę spraw społecznych, praźródłem tego była naprawa państwa, w szczególności naprawa finansów publicznych państwa. Myślę, że patrząc na nowożytną historię Polski, możemy powiedzieć tak: że to jest historia wielkiego narodu, ale słabego państwa przez ostatnie setki lat, to mam przede wszystkim na myśli. To, że dołożyliśmy jako Prawo i Sprawiedliwość cegłę, może cegiełkę nawet do tego, żeby poprawić struktury państwa, a zwłaszcza niewydolne struktury finansów publicznych, jest niezwykle ważnym osiągnięciem i jednocześnie tą praprzyczyną wielkich naszych polityk. O społecznej już powiedziałem, ale warto powiedzieć o wielkiej polityce zrównoważonego rozwoju, Polsce lokalnej. Warto powiedzieć o wielkiej polityce bezpieczeństwa, o naszej wielkiej polityce wobec polskiej wsi, rolnictwa, wyrównywania szans na polskiej wsi, ale także naszej polityce kulturalnej, polityce oświatowej, również polityce rozwoju… (Poseł Jakub Rutnicki: Dotacje dla Bąkiewicza.) …która przecież jakościowo zasadniczo różni się od tego, co było wcześniej, i o czymś, czego nie można pominąć dzisiaj, czyli wielkiej polityce bezpieczeństwa naszych granic, naszych ulic, ale w szczególności naszych granic. Do tego jeszcze się później pokrótce odniosę. A więc, szanowni państwo, podsumowując te 4 lata, chciałbym przejść przez to w pewnej takiej chronologii czterech wielkich kryzysów, które na nas spadły. I to, że mogliśmy na nie reagować, też brało się z tego, że traktowaliśmy nasze obietnice, nasze zapowiedzi wobec rodaków bardzo, bardzo poważnie. Wiedzieliśmy, że czy pogoda, czy słota chcemy zrealizować nasze zapowiedzi i ratować to, co jest konieczne do uratowania w trakcie poszczególnych kryzysów. Zacznę od tego najwcześniejszego, który uderzył już wkrótce po rozpoczęciu ostatniej kadencji Sejmu. To kryzys pandemiczny, kryzys związany z COVID-19, kryzys, który mógł doprowadzić do gigantycznego wzrostu bezrobocia, upadłości setek tysięcy firm i jednocześnie do tego, aby polska gospodarka bardzo gwałtownie cofnęła się w rozwoju. (Poseł Jakub Rutnicki: O respiratorach teraz.) Z powodu naszych tarcz: antykryzysowej, finansowej nie tylko obroniliśmy miliony miejsc pracy, uratowaliśmy od bankructwa setki tysięcy firm, ale również w naszym kraju nie dochodziło do selekcji pacjentów, co miało miejsce we Włoszech, w Hiszpanii, we Francji, krajach o wiele bogatszych. A Polska nie tylko w rozwoju się nie cofnęła, ale możemy podsumować to najlepiej może najważniejszą gospodarczo liczbą… (Głos z sali: Ludzie płot rozebrali w międzyczasie.) …podsumować te 4 lata wzrostem gospodarczym – chodzi o taki przecież wszechogarniający wskaźnik wzrostu PKB. Otóż, szanowni państwo, od 2019 r. do końca 2023 r., bo on już się kończy… Wiadomo mniej więcej, jaki będzie wzrost gospodarczy w Polsce, a jaki w innych krajach – wzrost gospodarczy tu to 11%. Jest to jeden z absolutnie najwyższych wzrostów w Unii Europejskich, w krajach OECD również. (Oklaski) (Poseł Jakub Rutnicki: Zielona wyspa.) Dla porównania: u naszych sąsiadów zachodnich i południowych, Czechów, przez te 4 lata wskaźnik wzrósł o 0,5 punktu procentowego, tu – 11%, tam – 0,5 punktu procentowego. Strefa euro – wzrost o 3 punkty procentowe przez te 4 lata. Potrafiliśmy zatem obronić mocny wzrost gospodarczy, który jest podstawą naszej polityki społecznej. Później przyszedł drugi kryzys, kryzys migracyjny. (Poseł Jakub Rutnicki: Wawrzyk.) Tutaj najpierw obroniliśmy się przed szaleństwami płynącymi z Zachodu. Obroniliśmy się na posiedzeniach Rady Europejskiej w 2017 r., 2018 r. i 2019 r. przed przymusem relokacji. Postawiliśmy twarde weto i nie przyjęliśmy nielegalnych imigrantów. (Oklaski) Warto o tym pamiętać, bo wprawdzie wtedy przed tym się obroniliśmy, ale Wysoka Izba, także posłowie Trzeciej Drogi, Lewicy, będzie musiała wkrótce podejmować decyzje prawdopodobnie dotyczące ponownej próby narzucenia nam przymusu relokacji nielegalnych imigrantów. A tutaj, jak myślę, jest jeden z kolejnych wspólnych mianowników, który łączy nas, Prawo i Sprawiedliwość, właśnie z większością posłów Trzeciej Drogi, ale nie tylko. Otóż, kiedy na jakiś czas, jak się okazało, minęło tamto szaleństwo z Zachodu, czekało nas jeszcze poważniejsze uderzenie, bardzo realne: atak ze Wschodu. To atak Łukaszenki na zlecenie Putina, który ściągnął w sztuczny sposób, zinstrumentalizował dziesiątki tysięcy migrantów z Bliskiego Wschodu. (Poseł Jakub Rutnicki: A wy ile ściągnęliście?) I postawiliśmy mur, który miał nie powstać w 3 lata, postawiliśmy zaporę, twardą zaporę przed nielegalną imigracją. Staraliśmy się ten wielki kryzys migracyjny w odpowiedni sposób zmitygować, zabezpieczyć wschodnie granice Polski, ale także wschodnie granice NATO i wschodnie granice Unii Europejskiej, która bez tego byłaby narażona na gigantyczne przepływy nielegalnych imigrantów tą bezpieczną, bo lądową, drogą. I to drugi wielki kryzys, przed którym przyszło nam stanąć i obronić Rzeczpospolitą, obronić naszych rodaków. Potem nastąpił chronologicznie trzeci wielki, największy kryzys, bo taki, który jest największym zagrożeniem geopolitycznym dla Rzeczypospolitej, dla Europy, może nawet dla świata, ostatnich dziesięcioleci. To wojna na Ukrainie. I wprawdzie dzisiaj jest wielu mądrych, którzy twierdzą, że przewidywali wszystko, pokazują, jacy to oni dzisiaj są odważni, że mogliby stawić czoła temu rosyjskiemu zagrożeniu, ale warto przypomnieć pokrótce chronologię i perspektywę, która wiązała się z tym zagrożeniem i jego identyfikacją. Trzeba jako o pierwszym powiedzieć o panu prezydencie Lechu Kaczyńskim, który w 2008 r. wypowiedział swoje prorocze słowa, a którego misję przerwała później niestety ogromna, okrutna tragedia. Bierność Zachodu dopełniła reszty i w roku 2014 nastąpiła pierwsza, właśnie ta proroczo przez niego przewidziana, agresja na Ukrainę, a później, w 2022 r. – kolejna. I kiedy jechaliśmy razem z panem prezesem Jarosławem Kaczyńskim, z premierami Czech i Słowenii do Kijowa w niespełna 2,5 tygodnia po rozpoczęciu ataku Rosji na Ukrainę, to przede wszystkim ta właśnie myśl nam przyświecała: w jaki sposób zapobiec sytuacji, w której tamte słowa o ataku na Ukrainę, potem na państwa bałtyckie, a następnie na Polskę, stałyby się rzeczywistością. I przed tym, nasi drodzy rodacy, rząd Prawa i Sprawiedliwości chronił Polaków poprzez przede wszystkim umacnianie naszego sojuszu ze Stanami Zjednoczonymi, a także wielką rozbudowę polskiej armii, wielki program modernizacji polskiej armii. To właśnie ten program modernizacji doprowadził do tego, że dziś wielu komentatorów nasze plany uczynienia Wojska Polskiego najsilniejszą armią lądową w Europie uważa za jak najbardziej realne, jak najbardziej realistyczne. I to niezwykle ważny kierunek działań. Wspomniał o nim w swoim wystąpieniu inauguracyjnym pan prezydent, któremu bardzo za to dziękuję, ponieważ niezależnie od tego, jak potoczy się los tworzenia rządu, wierzę, że to jest naczelny imperatyw, który spoczywa na barkach wszystkich posłów, i wierzę jednocześnie, że zwłaszcza ci posłowie, którym drogie jest bezpieczeństwo Polski, będą mieli na uwadze to, że to właśnie rząd Prawa i Sprawiedliwości do bezpieczeństwa przykłada najwyższą wagę. (Oklaski) My nie będziemy rewidować żadnych umów, ba, będziemy zawierać nowe umowy, które dalej umocnią bezpieczeństwo Polski. To, sądzę, jest sprawa absolutnie fundamentalna. I wreszcie ostatni z czterech wielkich kryzysów, kryzys energetyczny i inflacyjny. Wiemy doskonale, że energia jest matką wszystkich kosztów czy większości kosztów w gospodarce i że inflacja wynikała przede wszystkim z tych przyczyn, które swój początek brały w epidemii i w wojnie na Ukrainie. Europejski Bank Centralny podał, że za inflację w 72% odpowiadają właśnie te czynniki. A więc dzisiaj, kiedy kurz bitewny kampanii wyborczej opadł, myślę, że wszyscy państwo możecie już śmiało potwierdzić to, o czym mówiliśmy od dawna, że jest to absolutnie importowana inflacja. (Poseł Marcin Kierwiński: Że doprowadziłeś do inflacji.) (Głos z sali: Nieprawda.) Ale zacznijmy te kilka zdań refleksji na temat inflacji od tego, w jaki sposób walczono z inflacją przez poprzedzające 25 lat według szkoły Leszka Balcerowicza. Otóż walczono w bardzo prosty sposób, każdy może sobie to przypomnieć, drodzy państwo – poprzez tzw. przymrożenie gospodarki, czyli wysokie bezrobocie, wzrost bezrobocia. Oczywiście natychmiast siadał wtedy popyt, natychmiast bankrutowały dziesiątki tysięcy firm i inflacja wtedy spadała. My przyjęliśmy inną drogę – drogę obrony miejsc pracy, obrony firm, was, drodzy przedsiębiorcy, i was, drodzy rodacy, waszych miejsc pracy. I to się powiodło (Oklaski), ponieważ łatwo zobaczyć, że jeszcze 1,5 roku temu, kiedy inflacja była w okolicach prawie 20%, nikt nie wierzył w to, co mówiliśmy, że ona spadnie pod koniec tego roku w okolice 6–7%, a właśnie tak się stało. Dziś inflacja to 6,5%, jest w trendzie spadkowym i można powiedzieć, że w dużym stopniu udała się już ta operacja obrony społeczeństwa polskiego przed bezrobociem, przed kolejną falą bezrobocia. A to przecież kluczowa sprawa, fundamentalna, bo bezrobocie było zmorą III Rzeczypospolitej. Pamiętamy wszyscy, drodzy rodacy, jak wszyscy baliśmy się tego. Stąd też tak cieszę się, że ta nasza recepta okazała się skuteczna, i na walkę z inflacją, i na zapobieżenie przyrostowi bezrobocia. (Oklaski) Ale też niech mi będzie wolno na tej kanwie przejść do podsumowania podstawowych parametrów gospodarczych, ponieważ inflacja jest jednym z nich, rzecz jasna, ale nie jedynym i nawet nie najważniejszym. Najważniejszym są miejsca pracy, najważniejszym jest stabilność makroekonomiczna, makrogospodarcza, najważniejszym jest jak najniższy poziom bezrobocia. I tutaj, uwaga, cytuję dane Komisji Europejskiej: mamy wyjątkowo stabilny system finansów publicznych. To będzie ważne, bo za chwilę powiem o obietnicach jednej z partii… (Poseł Marcin Kierwiński: Już kończ.) …która składała te obietnice przed wyborami. Mamy bardzo stabilne finanse publiczne. Popatrzcie wszyscy, drodzy rodacy, na tabelę równowagi makroekonomicznej prezentowaną przez Komisję Europejską, na dane Eurostatu: mamy najwyższą, rekordową liczbę osób pracujących, powyżej 17 mln. Pomimo tych czterech egipskich plag, które na nas spadły – było ich siedem, oby trzech nam Pan Bóg oszczędził – mamy bardzo stabilne finanse publiczne. Dług publiczny – uwaga, warto również przytoczyć te dane – urósł za czasów naszych poprzedników o 7,5 punktu procentowego, o 7,5 punktu procentowego, i to pomimo zagarnięcia OFE, 155 mld, i pomimo wyprzedaży majątku w wysokości ok. 58 mld. Nastąpił przyrost o 7,5 punktu procentowego. To do wszystkich państwa z tej strony sceny politycznej, którym miła jest stabilność finansów publicznych, a także obniżanie długu publicznego. Pamiętajcie o tym, zwłaszcza posłowie Trzeciej Drogi. W spokojniejszych czasach ci, którzy chcą być waszymi koalicjantami, doprowadzili do gwałtownego przyrostu długu. W naszych czasach przez 8 lat mimo tych wielkich kryzysów dług publiczny w relacji do PKB zmalał o 3,5 punktu procentowego. (Oklaski) Podaję dane na koniec tego roku. (Poseł Marcin Kierwiński: Pan premier już spakowany?) Ale obok tego trzeba podkreślić także rekordowe inwestycje w Polskę lokalną. Drodzy państwo posłowie Platformy Obywatelskiej, posłowie Trzeciej Drogi, PSL-u czy Polski 2050 albo Lewicy, zapytajcie swoich samorządowców, znajomych, swoich wójtów, burmistrzów, starostów, czy kiedykolwiek wcześniej w czasach III Rzeczypospolitej było więcej inwestycji w Polskę lokalną z budżetu centralnego niż w czasach rządów Prawa i Sprawiedliwości. (Oklaski) To też mogliśmy zrealizować, a więc ratowanie miejsc pracy, rekordowe inwestycje w szkoły, żłobki, szpitale, przedszkola, drogi powiatowe i gminne. To wszystko niezwykle ważna część całego naszego horyzontu gospodarczo-społecznego, który przyświecał nam w działaniach. Ale też chcę z tego miejsca, szanowni państwo, powiedzieć, że na pewno nie wszystko się udało. I zdaję sobie z tego sprawę, że gdyby pan marszałek dał mi więcej czasu, mógłbym długo o tym mówić. (Głos z sali: Nie, nie.) Bo, rzecz jasna, są też takie punkty. Ale za te wszystkie punkty na pewno warto przeprosić – za nasze błędy. Tylko władza, która nic nie robi, nie popełnia błędów. Chociaż był taki rząd w naszej historii nie tak dawno temu, który niewiele robił i też popełniał błędy (Oklaski), więc takie osiągnięcia też się niektórym udają. (Głos z sali: Rząd Szydło?) Ale oczywiście za te potknięcia i za nasze niewłaściwe działania warto przeprosić. Szanowni Państwo! Teraz chciałbym przejść do drugiej części mojego wystąpienia i powiedzieć właśnie o tym, o czym powiedział pan prezydent, ale patrząc na przyszłość i z perspektywy parlamentarnej – o koalicji polskich spraw. Drodzy Parlamentarzyści! Drodzy Rodacy! Mamy oczywiście teraz przed sobą okres tworzenia rządu. Chcę wszystkich zaprosić do takiej właśnie koalicji, o jakiej mówił pan prezydent: koalicji polskich spraw, koalicji, która będzie dbała o sprawy społeczne, o sprawy bezpieczeństwa narodowego, o sprawy suwerenności, ale także o wielkie projekty, które rozpoczęliśmy, a od ciągłości ich realizacji zależy przyszłość naszej ojczyzny. (Poseł Jakub Rutnicki: Izera.) Do takiej właśnie koalicji bardzo chciałem zaprosić, bo od tego, w jaki sposób poprowadzimy nasze polskie sprawy, będzie zależeć przyszłość naszej ojczyzny. Ale teraz chcę przejść do kolejnej części, o której wspomniałem na początku, czyli do tej, która dość niespodziewanie w ostatnich kilku miesiącach stała się dla nas priorytetem i myślę, że jest dla wszystkich rodaków priorytetem, numerem jeden. A mianowicie do zadbania o to, aby Polska pozostała Polską, żeby Polska była Polską. Żeby Polska była suwerenna, żebyśmy sami mogli rządzić we własnym domu. Wierzę, że ta idea jest droga wszystkim państwu. Wierzę, że tak jest również wśród partii, które dzisiaj próbują tworzyć koalicję. Uważam, że ta idea jest droga wam wszystkim. Ale też aby uświadomić, jakie konkrety nam tutaj grożą, przeglądnąłem bardzo dokładnie cały zestaw zagadnień, który dzisiaj idzie przez Parlament Europejski i za którym głosowała Platforma Obywatelska w Parlamencie Europejskim. I wkrótce na posiedzeniu Rady Unii Europejskiej ma odbyć się głosowanie w tej sprawie. Drodzy Rodacy! Panie Prezydencie! Panie Marszałku Seniorze! Drodzy Parlamentarzyści! Chciałem o tych kilku bardzo konkretnych sprawach powiedzieć, przytaczając jednocześnie numery poprawek, które wiążą się z planami zmian, fundamentalnych zmian w systemie stanowienia prawa i zdolności tego parlamentu, naszego Sejmu i naszego Senatu do stanowienia prawa w imieniu rodaków. A więc, po pierwsze, poprawki od numeru 178 do 186, jak ktoś chciałby to wszystko sprawdzić, zweryfikować, przeanalizować. Zachęcam do tego dziennikarzy, zachęcam do tego wszystkich ludzi dobrej woli. Nie wiem, czy macie państwo świadomość, że po przeprowadzeniu tych poprawek, które teraz idą właśnie przez Parlament Europejski, Radę Unii Europejskiej, potem Konwent i w bardzo krótkim czasie mogą stać się rzeczywistością, będziemy całkowicie zależni od Brukseli w odniesieniu do źródeł energii, które stanowią podstawę naszego systemu energetycznego. Niedawno, pamiętamy, była sytuacja Turowa. Przypominam ją tylko dlatego, że to dzięki uporowi Prawa i Sprawiedliwości elektrownia (Oklaski) i kopalnia Turów istnieją. Bo byłyby zamknięte. 6% naszego systemu elektroenergetycznego. A miks energetyczny jest kluczowy dla każdego z państw. Będziemy pozbawieni możliwości decydowania o miksie energetycznym, drodzy mieszkańcy Śląska i wszystkich miast, gdzie są elektrownie, kopalnie, ale także elektrownie gazowe. (Poseł Jakub Rutnicki: Nie strasz, nie strasz.) Będziemy pozbawieni tej możliwości. Unia Europejska będzie mogła praktycznie z dnia na dzień zamknąć bez naszego prawa głosu nasze elektrownie, nasze kopalnie i np. zaordynować, że trzeba czerpać energię elektryczną z importu. Myślę, że to nie jest takie śmieszne, panowie posłowie. (Poseł Borys Budka: To jest żenujące.) (Głos z sali: Trzeba już się pakować.) Patrzę tutaj, to jest rzeczywiście coś niezwykle niebezpiecznego. Myślę, że wszyscy rodacy to rozumieją. Poprawki numer 247, 248 – podatki. Czy zdajecie sobie państwo sprawę z tego, że po zmianie prawa Unii będzie możliwość nałożenia nowych podatków? Do tej pory wetowałem wiele takich prób. Teraz nie będzie możliwości weta, ponieważ całe władztwo podatkowe przejdzie właśnie w ręce Unii Europejskiej. Co to oznacza? Będzie można nałożyć każdy rodzaj podatku, wziąć go jako wspólny dochód do budżetu Unii Europejskiej i zrealizować na tej podstawie cele, które są nam bardzo obce. Ani euro, ani złotówka z tego polskiego podatku może nie wrócić do Polski. Nie będziemy tego mogli jako Sejm, ale również żaden kolejny rząd nie będzie mógł tego oprotestować, nie będzie mógł zawetować. A przecież wyobraźnia wszystkich urzędników unijnych co do tego, jakie podatki można nakładać: nowe podatki na emisję dwutlenku węgla, od samochodów spalinowych, od jedzenia mięsa itd., to naprawdę jest rzeczywistość, która może się zbliżać szybkimi krokami. Punkt trzeci, jak myślę, może wielu z państwa zaszokować. To poprawka nr 124. Otóż nie wiem, czy wiecie państwo, że reforma traktatów doprowadzi do tego, że obca policja będzie mogła bez zgody państwa polskiego wjechać na terytorium państwa polskiego, aresztować kogoś, nawet aresztować Polaków, ponieważ to będzie wynikało z zasad ustalonych bez procedury jednomyślności. Zabierana jest procedura jednomyślności. W Unii Europejskiej decyzja będzie zapadała na zasadzie zwykłej większości bądź kwalifikowanej większości, bądź wzmocnionej kwalifikowanej większości, ale, drodzy państwo, powiedzmy sobie szczerze, co oznacza taka kwalifikowana większość. (Poseł Jakub Rutnicki: Złóż tę dymisję i zejdź.) Rządzą dzisiaj w Unii Europejskiej silni. Rządzą Niemcy, Francja i kilka silnych krajów, które z nimi najbliżej współpracują. (Poseł Jakub Rutnicki: Co to jest, panie marszałku?) Pomyślcie, poprawka 124, likwidacja tej zasady doprowadzi do tego, że obce służby będą mogły w naszym kraju prowadzić działanie bez zgody polskiego rządu. Kolejna poprawka, nr 112. Nie wiem, czy wiecie państwo, że Unia zyska nową kompetencję w zakresie kontroli granic. (Poseł Jakub Rutnicki: Do rzeczy.) Praktycznie zabrana może być kompetencja dotycząca ochrony polskich granic. Rozebrany może być mur na granicy z Białorusią. (Poseł Jakub Rutnicki: Co tam u Wawrzyka?) Ta rzeczywistość, drodzy rodacy, jest absolutnie przed nami. To najbliższe miesiące, kwartały, lata mogą o tym zadecydować. To dlatego koalicja polskich spraw musi się opierać na tych parlamentarzystach, którzy naprawdę z trwogą patrzą na te elementy pozbawienia nas suwerenności. Dzisiaj w Unii Europejskiej wiele krajów, wielu przywódców mówi w sposób absolutnie otwarty: zlikwidować państwa narodowe. Oni się z tym nie kryją. W programie partii, które zawiązują koalicje niektórych państw członkowskich, jest taki zapis: zlikwidować państwa członkowskie. Szanowni państwo, my nie tylko szanujemy naszą niepodległość, suwerenność. Biało-Czerwona i możliwość stanowienia o sobie – nic o nas bez nas – są fundamentem naszej polityki. (Oklaski) Kolejne punkty, ekologia. Wszyscy oczywiście kochamy środowisko naturalne. Ale grozić będzie to, że ci, którzy sobie pobudowali drogi, w czasie kiedy nie obowiązywały te reguły, dzisiaj nam zablokują rozwój; gdzieś znalezione zostanie siedlisko ślimaków czy minogów i będą opóźniali realizację. To jest rzeczywistość, zapytajcie samorządowców. Będzie ta rzeczywistość zupełnie niezależna od nas. Ale także, szanowni państwo, jest poprawka 154 – zniesiona jednomyślność w sprawie zabezpieczenia społecznego, a więc i wiek emerytalny będzie mógł być podniesiony do 67. roku życia bez nas. Polityka zagraniczna: poprawki 55–58. Zwracam na to uwagę. Polityka obronna: poprawki 59–70. Szanowni państwo, komuś może się nie spodobać, że Polska się zbroi – już dzisiaj pojawiają się takie głosy na Zachodzie – ponieważ prowokuje to Rosję. Mogą w duchu dzisiaj tworzonej właśnie w nowych traktatach unii obronności zablokować szybki plan modernizacji polskiej armii. Wreszcie ostatnia poprawka z tych, które chcę przywołać, poprawka nr 117. To szczególnie istotny i czuły szczegół, ponieważ dotyczy naszych dzieci. Nie wiem, czy macie państwo świadomość, że Unia będzie mogła narzucić Polsce rozwiązania, które ułatwią wywożenie dzieci za granice naszego kraju pod pretekstem współpracy sądowej. Do tej pory obowiązywała jednomyślność, mogliśmy zablokować taką regulację. W przypadku gdy nowe reguły traktatowe zostaną zrealizowane, nie będziemy mogli tego robić. Panie Prezydencie! Panie Marszałku! Wysoka Izbo! To jest gra o suwerenność. To jest gra o polską niepodległość. Ona się będzie toczyła metodami politycznymi. Ale fakt, że ona będzie się toczyła metodami politycznymi – a nie jak za naszą wschodnią granicą, gdzie metodami wojennymi pozbawia się niepodległości naszego sąsiada – nie znaczy, że tej niepodległości nie możemy być pozbawieni. Ba, właśnie trudniej jest dostrzec taką zmianę traktatową. Trudniej jest ją docenić, trudniej ją wypatrzeć, dlatego podałem dzisiaj państwu tych kilka przykładów. Panie Prezydencie! Panie Marszałku! Wysoka Izbo! Bardzo ważny jest wątek dotyczący suwerenności, ale jeszcze istotniejsze jest to, aby wszyscy drodzy rodacy zrozumieli, że to właśnie nasze życie, to właśnie wasze podatki, edukacja waszych dzieci, to właśnie ekologia we właściwy sposób stosowana… (Poseł Jakub Rutnicki: Odra.) …bezpieczeństwo, obronność, to właśnie to, czy będziemy mogli stanowić w naszym kraju prawo, są dzisiaj przedmiotem zmian traktatowych w ramach Unii Europejskiej. Jesteśmy i będziemy członkiem Unii Europejskiej. Jesteśmy państwem, które bardzo mocno zaznacza swoją obecność na poziomie Unii Europejskiej, bo bronimy polskich interesów. Nie chcemy poklepywania po plecach, tylko bronimy naszych interesów. Drodzy państwo, różnimy się w tak wielu sprawach, często nie zauważamy jednak, że te właśnie tematy, o których tutaj powiedziałem, są chyba tematami, które nas jednoczą. Przynajmniej mam taką nadzieję. Myślę, że to może być taki dekalog polskich spraw najważniejszych dla utrzymania naszej szybkiej ścieżki rozwoju, naszego doganiania tych najbogatszych – bo dogoniliśmy ich w ostatnich 8 latach bardzo szybko. Dziś to jest już ok. 80% średniej unijnej liczonej jako PKB na głowę mieszkańca w sile nabywczej pieniądza, ale 86%, doliczając do tego naszą politykę społeczną. Jesteśmy na poziomie Hiszpanii. (Oklaski) (Głos z sali: Do dymisji!)",
                },
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Panie premierze, przypominam, że umawialiśmy się na sprawozdanie, a na exposé to przyjdzie jeszcze czas. (Wesołość na sali, oklaski) (Głosy z sali: Brawo! Brawo!)",
                },
                {
                    "speaker": "Prezes Rady Ministrów Mateusz Morawiecki",
                    "content": "Tak jest, panie marszałku, postaram się w parę minut zakończyć. Dziękuję bardzo. (Poseł Borys Budka: Nie, już kończ.) Szanowni Państwo! A więc niech ten dekalog polskich spraw będzie taką właśnie podstawą do współpracy, bo Polacy w tych wyborach przecież postawili na równowagę. Polacy postawili na równowagę. Polacy nie chcą żadnej zemsty, nie chcą wojny polsko-polskiej. Polacy chcą, żebyśmy odstawili dawne waśnie do lamusa… (Głosy z sali: Ooo…) …i żebyśmy postarali się zbudować rząd, można powiedzieć to dawne sformułowanie: ponad podziałami, nawet mogę powiedzieć: ponadpartyjny w jakimś stopniu, dlatego że właśnie żyjemy w tak szczególnym czasie, przy tych zagrożeniach, które są za naszą wschodnią granicą, ale także właśnie przy zagrożeniach dotyczących naszej suwerenności, o czym przed chwilą powiedziałem. Dlatego chciałbym zaprosić wszystkich, którzy tutaj, na tej sali, będą budowali większość parlamentarną… (Poseł Borys Budka: Ale pan składa dymisję.) …aby poparli właśnie mój rząd, który będę starał się stworzyć. (Oklaski) (Głosy z sali: Ha, ha, ha!) Dlatego będę także prosił pana prezydenta o wsparcie. Będę prosił pana prezydenta o wsparcie w tych działaniach, po to aby wszyscy nasi rodacy zauważyli, dostrzegli, na jak ważnym zakręcie historii Polska się znalazła. (Głos z sali: Przez was.) Szanowni Państwo! Polska jest wolna… (Głos z sali: Od was?) …od ponad 30 lat i myślę, że wszyscy po trosze przyczyniliśmy się do tego. Wszyscy powinniśmy dziękować naszym rodakom, powinniśmy się cieszyć z tego, że Polska jest wolna i powinniśmy dbać o tę wolność, o suwerenność, o niepodległość – dbać jak o źrenicę oka. (Głos z sali: Mógłby pan posłuchać marszałka seniora?) Powinniśmy także podziękować wszystkim rodakom za to, że właśnie pozwolili nam przez ostatnie 8 lat i mam nadzieję – pozwolą przez kolejne lata, w nowej, innej sytuacji politycznej, ale w sytuacji innej równowagi, rozwijać szybko naszą politykę społeczną, politykę bezpieczeństwa, politykę zrównoważonego rozwoju, także dla wsi, dla małych miasteczek. To zawsze było naszym celem. To wszystko to dekalog polskich spraw, który – mam nadzieję – będzie stanowił podstawę koalicji polskich spraw. To moje zobowiązanie jest aktualne dziś, będzie aktualne także jutro i pojutrze. W najbliższym czasie… (Wypowiedź poza mikrofonem) Panie marszałku, ostatnie zdania. W najbliższym czasie chcemy jako rząd, który cały czas działa, wykorzystać te ustawy, które już przyjęliśmy. (Poseł Barbara Nowacka: Przestańcie już wykorzystywać.) Chodzi o ustawę o wakacjach kredytowych, te ustawy, które są procedowane, jak np. ustawa osłonowa o cenach energii, gazu, energii elektrycznej. Chcemy tak procedować, żeby Wysoka Izba mogła się nimi jak najszybciej zająć. Podobnie jest z ustawą osłonową przedłużającą zerowy VAT na żywność do co najmniej połowy przyszłego roku. (Oklaski) To są te wszystkie ustawy. Mamy plan działań. Będziemy na pewno je prezentować. (Głos z sali: Do dymisji!) Szanowny Panie Prezydencie! Szanowny Panie Marszałku! Wysoka Izbo! Drodzy Rodacy! (Głos z sali: Czas kończyć.) Bardzo gorąco dziękuję za wszystko, co udało się zrobić. (Głos z sali: A przepraszam?) Raz jeszcze przepraszam za potknięcia, błędy ostatnich 4 lat… (Głosy z sali: Ooo…) …i proponuję koalicję polskich spraw. Polska jest tego warta. Walczmy o Polskę. Niech żyje niepodległa, suwerenna, dostatnia i solidarna Rzeczpospolita! (Głos z sali: Do dymisji!) Dziękuję bardzo. (Część posłów wstaje, długotrwałe oklaski) (Część posłów skanduje: Mateusz! Mateusz! Mateusz!) (Część posłów skanduje: Do dymisji! Do dymisji! Do dymisji!)",
                },
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Dziękuję bardzo panu premierowi. Panie i panowie posłowie, za chwilę zarządzę przerwę w obradach. W przerwie proszę o zgłaszanie kandydatów na stanowisko marszałka Sejmu. Na zgłoszenia oczekuję w gabinecie marszałka seniora do godz. 14.45. Zarządzam 20-minutową przerwę.",
                },
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Proszę o zajmowanie miejsc. Wznawiam obrady. Przystępujemy do rozpatrzenia punktu 1. porządku dziennego: Wybór marszałka Sejmu Rzeczypospolitej Polskiej. Informuję, że zgodnie z art. 4 ust. 2 regulaminu Sejmu na stanowisko marszałka Sejmu zgłoszono kandydatury posła Szymona Hołowni oraz poseł Elżbiety Witek. Czy są jeszcze inne kandydatury? (Poseł Jakub Rutnicki: Jeszcze chwila, jeszcze nie ma wszystkich.) Nie ma innych zgłoszeń. Stwierdzam, że lista kandydatów na stanowisko marszałka Sejmu została zamknięta. Proszę pana posła Władysława Kosiniaka-Kamysza o przedstawienie kandydatury pana posła Szymona Hołowni. (Oklaski)",
                },
                {
                    "speaker": "Poseł Władysław Kosiniak-Kamysz",
                    "content": "Szanowny Panie Marszałku! Szanowny Panie Prezydencie Rzeczypospolitej! Dostojni Goście! Panie i Panowie Posłowie! Wysoka Izbo! W imieniu grupy posłów reprezentujących cztery kluby parlamentarne: Koalicję Obywatelską, Polskę 2050 – Trzecią Drogę, PSL – Trzecią Drogę oraz Lewicę mam zaszczyt zaprezentować kandydaturę pana posła Szymona Hołowni na funkcję marszałka Sejmu Rzeczypospolitej. (Oklaski) Prezentacji tej kandydatury dokonam w oparciu o cechy, które według wnioskodawców powinien posiadać marszałek Sejmu, a w mojej opinii są przymiotami kandydata, pana posła Hołowni. Po pierwsze, erudycja. Ta wywodząca się z domu, wywodząca się z doświadczenia życiowego, wywodząca się z zajmowanych i sprawowanych funkcji, miejsc pracy, doświadczenia, które powoduje, że masz świadomość, masz wiedzę, masz umiejętności. (Głos z sali: A wykształcenie jakie?) Słowo dla parlamentaryzmu to jest klucz. Szacunek do słowa, słowo, które daje nadzieję, słowo, które daje odwagę, słowo, które krzepi. I to samo słowo często wypowiedziane w nieodpowiedni sposób albo złe słowo niszczy, krzywdzi. Parlamentaryzm to jest sztuka posługiwania się słowem. Nasz kandydat Szymon Hołownia tę sztukę posługiwania się słowem opanował do perfekcji, także i w piśmie, bo jest autorem ponad 20 książek, wielu publikacji, dziennikarzem i publicystą docenianym za swoje osiągnięcia. W 2006 r. i 2007 r. laureat nagrody Grand Press. To osoba, która w niezwykły sposób w wielu redakcjach, czy to w dziennikach, czy to w tygodnikach, ale również w radiu i w telewizji, zarządzała, ale i w niezwykły sposób posługiwała się słowem, brała za to słowo odpowiedzialność. Marszałek Sejmu wypowiadający słowa w imieniu Wysokiej Izby musi się cechować ogromną odpowiedzialnością za słowo, być erudytą i dawać nadzieję w tym słowie, które mówi. Szymon Hołownia jest takim kandydatem, jest takim posłem. (Oklaski) Empatia, wrażliwość społeczna, słuch społeczny. Wszyscy, tak jak tutaj siedzimy, jesteśmy wybrani przez naród, przez naszych obywateli. Kontakt z nimi jest jednym z podstawowych obowiązków parlamentarnych. Słuch społeczny to jest jedna z tych cech, które parlamentarzysta, a pierwszy spośród nas szczególnie, musi posiadać. Słuch społeczny, który pozwala słyszeć tych, którym jest najtrudniej, tych, którzy często nie mogą się przebić, tych, którzy są uciemiężeni, czasem upokorzeni, tych, którzy potrzebują wielkiego wsparcia. Ten słuch społeczny daje później poczucie odpowiedzialności i rozwagi w podejmowanych decyzjach. Bez słuchu społecznego, bez tego posiadania kontaktu ze społeczeństwem odrywa się od rzeczywistości, a to w historii polskiego parlamentaryzmu, również tej niedawnej, bardzo źle się skończyło. Dlatego słuch i wrażliwość społeczna, którymi cechuje się pan poseł Szymon Hołownia, są niezbędne. A jaka to jest wrażliwość społeczna? To jest pochylenie się nad tymi, którym naprawdę w życiu jest najtrudniej, których los najbardziej doświadczył. To jest założenie Fundacji Kasisi w 2013 r., a rok później Fundacji Dobra Fabryka działających na rzecz najbiedniejszych, najbardziej cierpiących w Afryce, w Zambii, gdzie powstał dom dziecka, ale także w 11 krajach na trzech kontynentach: w Azji, w Europie i w Afryce, na rzecz tych, którzy tego wsparcia potrzebują. Docenieniem tej wrażliwości jest otrzymanie odznaki honorowej na rzecz zabiegania o prawa dzieci w 2016 r. Docenieniem tej roli jest funkcja ambasadora na rzecz celów zrównoważonego rozwoju ONZ. Docenieniem tej roli są zbiórki społeczne organizowane przez Szymona Hołownię na rzecz choćby telefonu zaufania. Słuch społeczny, jakim się wykazywał w swej działalności na wszystkich etapach swojego życia, jako dziennikarz, publicysta, jak również polityk, wskazuje na to, że potrzeby tych, którym najtrudniej, których czasem trudno usłyszeć, będą słyszane i realizowane. Tak więc empatia to jest druga z cech, które są potrzebne, żeby dobrze pełnić funkcję marszałka Sejmu. I trzecia – odwaga. Odwaga, bez której nie ma zwycięstwa, odwaga, bez której nie ma zmiany, odwaga, bez której nie przenosi się Polski z kraju marzeń w rzeczywistość. Ta odwaga była obecna u Szymona Hołowni w szczególnym momencie, kiedy zdecydował się, że z życia dość mocno poukładanego, pięknie rozwijającej się kariery, w takim ludzkim odczuciu, bardzo bezpiecznego życia przyszedł do świata polityki i poddał się weryfikacji wyborców. Najpierw w wyborach prezydenckich, otrzymując blisko 3 mln głosów, a później zakładając ruch społeczny – Polskę 2050, innowacyjną w swym wymiarze. Bo to nie tylko partia polityczna, ale i think-tank, jak również działalność społeczna i charytatywna, która w tym szerokim ruchu społecznym się mieści. Trzeba było mieć odwagę, żeby porzucić wygodne życie i oddać się do dyspozycji społeczeństwa i usłyszeć też wyroki tego społeczeństwa wobec swojej osoby. W pierwszym kroku w wyborach prezydenckich, a w drugim kroku w wyborach parlamentarnych, w których niezwykłym zaufaniem obdarzyli go wyborcy w województwie podlaskim, dając mu samemu, nie liście wyborczej, blisko 14% poparcia. (Oklaski) To jest wyraz wielkiego zaufania społecznego, wyraz odwagi do podejmowania daleko idących celów. Ta odwaga w funkcji marszałka jest potrzebna do praworządności, do sprawiedliwości, do przyzwoitości, do szanowania wyborów Polaków, którzy wskazali większość, ale też poszanowania tych, którzy są w mniejszości, do szacunku dla każdego z naszych wyborców. Ta odwaga jest potrzebna, żeby godnie reprezentować w trudnych czasach Rzeczpospolitą i w kraju, i w dyplomacji parlamentarnej, żeby podejmować najodważniejsze decyzje w imieniu narodu, bo my jesteśmy tylko tymi, którzy są pośrednikami woli narodu. Szymon Hołownia, nasz kandydat na stanowisko marszałka Sejmu Rzeczypospolitej, ma wszystkie wymienione cechy i przymioty. Ma cechę erudycji, ma wielki przymiot wrażliwości społecznej i odwagi. Proszę Wysoką Izbę o wybranie na swojego marszałka Szymona Hołownię. (Oklaski)",
                },
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Dziękuję panu posłowi. Bardzo proszę pana posła Mariusza Błaszczaka o przedstawienie kandydatury pani poseł Elżbiety Witek. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Poseł Mariusz Błaszczak",
                    "content": "Bardzo dziękuję. Szanowny Panie Marszałku! Wysoki Sejmie! Mam zaszczyt w imieniu Klubu Parlamentarnego Prawo i Sprawiedliwość, najliczniejszego klubu parlamentarnego w Sejmie X kadencji (Oklaski), przedstawić kandydaturę pani marszałek Elżbiety Witek na urząd marszałka Sejmu Rzeczypospolitej Polskiej. (Oklaski) Pani Elżbieta Witek jest wieloletnim parlamentarzystą. W ławach poselskich zasiada od 2005 r., od V kadencji. Była członkiem Komisji Regulaminowej, Spraw Poselskich i Immunitetowych, Komisji Etyki Poselskiej, Komisji Edukacji, Nauki i Młodzieży oraz Komisji Polityki Społecznej i Rodziny. Pochodzi z Jawora na Dolnym Śląsku. Jest mężatką, ma dwie dorosłe córki. Elżbieta Witek ukończyła wymarzone studia na Uniwersytecie Wrocławskim. Był to jeden z tych ośrodków naukowych, w których kształtowała się niezależna myśl naukowo-polityczna. Ona uformowała Elżbietę Witek, obudziła w niej pragnienie wolności i społecznej sprawiedliwości, a także chęć do podejmowania działań zmierzających do zmian społeczno-politycznych w Polsce. W 1980 r. Elżbieta Witek została członkiem NSZZ „Solidarność”. Z wielkim zaangażowaniem i typową dla siebie energią włączyła się w działalność związkową, a po wprowadzeniu stanu wojennego w działalność opozycyjną. Za swoją antykomunistyczną aktywność w 1982 r. była aresztowana i osadzona w więzieniu. Ci, którzy doświadczyli komunistycznych represji, wiedzą, jak okrutnych metod używały służby, by złamać opozycjonistów. Elżbieta Witek nigdy się nie poddała. Za swoją niezłomną postawę została wyróżniona Krzyżem Wolności i Solidarności. Przez wiele lat pracowała jako nauczycielka i dyrektorka w Szkole Podstawowej nr 2 oraz w Zespole Szkół Ogólnokształcących w Jaworze. Swoją pracę zawsze wypełniała ponad powierzone zawodowe obowiązki, swoich uczniów otaczała troską i zrozumieniem. Za wzorową pracę odebrała Medal Komisji Edukacji Narodowej. Dbałość o wychowanie dzieci, kształtowanie ich w duchu patriotycznych wartości, a przede wszystkim zapewnienie im bezpieczeństwa wciąż pozostają dla niej priorytetem. Nie ustawała również w służbie społeczeństwu, podejmując wiele działań dla dobra mieszkańców regionu. W latach 2015–2017 była ministrem – członkiem Rady Ministrów, szefem gabinetu politycznego prezesa Rady Ministrów, rzecznikiem prasowym rządu. Od czerwca 2019 r. pełniła urząd ministra spraw wewnętrznych i administracji, a następnie urząd marszałka Sejmu VIII i IX kadencji. Elżbieta Witek była najdłużej urzędującym marszałkiem Sejmu w III Rzeczypospolitej. (Oklaski) Opozycja nigdy nie skierowała wniosku o odwołanie pani marszałek. Zawsze godnie reprezentowała naszą Izbę nie tylko w kraju, ale także na forum międzynarodowym. Do współpracy zapraszała nie tylko posłów partii rządzącej, ale także posłów opozycji. Jest inicjatorką nowego formatu współpracy kobiet – przewodniczących parlamentów państw Unii Europejskiej, który cieszy się dużym uznaniem i który podejmował wiele ważnych spraw, takich jak współczesny handel ludźmi, a przede wszystkim kobietami, czy też uprowadzanie dzieci z objętej wojną Ukrainy oraz organizowanie pomocy dla kobiet – ofiar wojny na Ukrainie. Rozpoczęła również cykl spotkań najmłodszych parlamentarzystów państw Trójmorza czy też współpracę z państwami afrykańskimi poprzez zorganizowanie, jako pierwszego kroku, konferencji z udziałem ambasadorów państw kontynentu afrykańskiego, w której uczestniczyli przedstawiciele wszystkich ugrupowań reprezentowanych w Sejmie. Okres pełnienia funkcji marszałka Sejmu przypadł na czasy pandemii. Dzięki znakomitej współpracy z Kancelarią Sejmu i jej pracownikami w krótkim czasie pani marszałek doprowadziła do organizacji prac Sejmu w systemie zdalnym. Byliśmy pierwszym parlamentem w Europie, który pracował w takim trybie. Potem przyszła wojna na Ukrainie i związane z nią kryzysy – gospodarczy i ekonomiczny. Sejm musiał, podobnie jak rząd, podejmować szybkie decyzje i działać w niestandardowych okolicznościach. Czas miał tu znaczenie, chodziło bowiem o zapewnienie bezpieczeństwa naszym obywatelom i o szybką pomoc przedsiębiorcom. Organizacja prac Sejmu i komisji w tak trudnym czasie wymagała dużej odporności, przemyślanych, ale szybkich decyzji i umiejętności organizatorskich. Pani marszałek Elżbieta Witek sprawnie przeprowadziła Sejm przez ten trudny czas. Pracowitość, ogromne życiowe i zawodowe doświadczenie, parlamentarny dorobek oraz zdolności organizacyjne, a także wysoka kultura osobista, takt, wyważone opinie i znakomite relacje z ludźmi dowodzą, że pani poseł Elżbieta Witek jest właściwą kandydatką na funkcję marszałka Sejmu Rzeczypospolitej Polskiej. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Dziękuję panu posłowi. Czy ktoś z pań, panów posłów pragnie zabrać głos w sprawie zgłoszonej kandydatury? (Wypowiedź poza mikrofonem) Chwileczkę, chwileczkę. Czy są inne zgłoszenia? (Głos z sali: Nie ma.) Jeszcze nie ma innych zgłoszeń. Bardzo proszę, pan poseł Braun. Czas – 3 minuty. (Głos z sali: Ooo…) (Głos z sali: Nowe standardy.)",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Szczęść Boże! Wysoka Izbo! Nie może być tak, że taktownie przemilczymy tutaj tak nietaktownie zgłoszoną kandydaturę Elżbiety Witek na marszałka tego Sejmu… (Głos z sali: Wstydź się.) (Głos z sali: Siadaj.) …ponieważ to jest kandydatura sztandarowa, która uosabia standard pogardy, lekceważenia prawa za rządów Zjednoczonej łże-Prawicy. (Głos z sali: Zapisz się do PO.) I wysunięcie tej kandydatury jest manifestacją braku woli koncyliacji, dialogu, zmian, prawdziwie dobrej zmiany na polskiej scenie politycznej. Wysunięcie tej kandydatury w praktyce przestępczej, tak bliskiej przecież obozowi Zjednoczonej łże-Prawicy… (Głos z sali: Licz pan słowa.) …to się nazywa: iść w zaparte. Zjednoczona Prawica idzie w zaparte, wysuwając Elżbietę Witek do urzędu marszałka, drugiej osoby w państwie. Przypomnijmy, że Elżbieta Witek zaznaczyła się w historii polskiego parlamentaryzmu, lekceważąc następstwo poselskie. Pan poseł Kawęcki nigdy nie został zaprzysiężony, nigdy nie miał okazji złożyć ślubowania, chociaż jego mandat został opróżniony po przedwczesnym zgonie poprzednika. Było to jeszcze w końcu VIII kadencji, ale to był prognostyk lekceważenia tego, co będzie się tutaj działo. A później matactwa, matactwa w głosowaniach, słynne: musimy anulować, bo przegrywamy. I to nie jeden raz, szanowni państwo. Pomiatanie Wysoką Izbą. Nie zdziwiliście się państwo, zasiadając w tych fotelach, że będziecie mieli do czynienia z przenoszeniem standardów szkoły podstawowej do Wysokiej Izby, ale zdziwiliście się, że to będzie poprawczak. (Głos z sali: Ha, ha, ha!) Szanowni Państwo! Nigdy więcej, dość, skończmy z tą groteską, jaką było przewodzenie pracom, Wysokiej Izbie przez osoby tak dalece odbiegające od wyobrażeń polskiego państwowca o potrzebach polskiego parlamentaryzmu. (Głos z sali: Hańba!) Mobbing, przemoc urzędowa i rytualna tu, w Wysokiej Izbie… (Poseł Anita Czerwińska: Nie kłam.) …wobec osób, które odważyły się nie respektować prawem kaduka narzucanych przez panią marszałek standardów i załganych, doraźnie improwizowanych przepisów, sprowadzanie powszechnego niebezpieczeństwa na naród polski poprzez udział w podżeganiu do wojny. (Głos z sali: Lekarza.) Dłuższa debata należy się (Dzwonek) tym przypadkom z ostatnich 4 lat, ale dziś powiem tylko, Wysoka Izbo, szanowny panie marszałku, że klub Konfederacji z całą pewnością nie poprze tej kandydatury. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek Senior Marek Sawicki",
                    "content": "Dziękuję panu posłowi. Zamykam dyskusję. W związku z tym, że zgłoszono dwie kandydatury na stanowisko marszałka Sejmu, nad wyborem marszałka Sejmu przeprowadzimy głosowanie za pomocą urządzenia do liczenia głosów, wykorzystując funkcję tego urządzenia umożliwiającą dokonanie wyboru z listy. Teraz bardzo proszę o uwagę, bo jest to ważne szczególnie dla posłów debiutujących. Przedstawiam zasady głosowania z wykorzystaniem funkcji umożliwiającej dokonanie wyboru z listy. Po zarządzeniu głosowania na wyświetlaczu pojawi się lista z nazwiskami kandydatów, którą można przesuwać za pomocą pola do przewijania ekranu dotykowego. Aby oddać głos za kandydaturą, należy dotknąć kwadratowego pola celem zaznaczenia wyboru danej kandydatury. Potwierdzenie zaznaczenia pojawi się w kwadratowym polu wyboru. Aby zmienić decyzję, należy ponownie dotknąć pola wyboru, aby odznaczyć, a następnie należy dokonać ponownego wyboru innej kandydatury. Po dokonaniu wyboru należy zatwierdzić swoją decyzję przez naciśnięcie przycisku „zatwierdź i wyślij”. Jest to równoznaczne z ostatecznym oddaniem głosu, a zatem brakiem możliwości zmiany decyzji. Niezaznaczenie żadnej z kandydatur i naciśnięcie przycisku „zatwierdź i wyślij” jest równoznaczne z oddaniem głosu przeciwko obu kandydaturom. Nie słyszę uwag, nie słyszę pytań. Wszystko jasne. Zgodnie z art. 4 ust. 3 regulaminu Sejmu Sejm wybiera marszałka Sejmu bezwzględną większością głosów. Przypominam, że na stanowisko marszałka Sejmu zgłoszone zostały kandydatury posła Szymona Hołowni i poseł Elżbiety Witek. Po rozpoczęciu głosowania lista w kolejności alfabetycznej zostanie umieszczona w czytniku urządzenia do liczenia głosów. Przypominam, że poprzeć można tylko jedną kandydaturę. Ponownie przypominam paniom i panom posłom, że naciśnięcie przycisku „zatwierdź i wyślij” jest równoznaczne z ostatecznym podjęciem decyzji, zatem proszę, aby tego przycisku użyć jako ostatniego. Przystępujemy do głosowania. Proszę obecnie panie i panów posłów o podejmowanie decyzji w sprawie wyboru marszałka Sejmu. Czy wszyscy posłowie podjęli już decyzję? Zamykam głosowanie. Proszę o wyświetlenie wyników. (Oklaski) (Część posłów wstaje i skanduje: Demokracja! Demokracja! Demokracja!) (Posłowie składają gratulacje i wręczają kwiaty Szymonowi Hołowni) Drodzy Państwo! Głosowanie jeszcze niezakończone. W głosowaniu wzięło udział 459 posłów. Większość bezwzględna wynosi 230 posłów. Poseł Szymon Hołownia uzyskał 265 głosów. Poseł Elżbieta Witek – 193. Stwierdzam, że na marszałka Sejmu został wybrany poseł Szymon Hołownia. (Część posłów wstaje, długotrwałe oklaski) (Poseł Szymon Hołownia: Dziękuję bardzo.) Drodzy Państwo! Panie i Panowie Posłowie! Bardzo proszę pana marszałka Szymona Hołownię o objęcie przewodnictwa i dalsze prowadzenie obrad. Gratuluję, panie marszałku, i życzę powodzenia. (Poseł Szymon Hołownia: Dziękuję ci bardzo, dzięki serdeczne. Panowie ministrowie, dziękuję bardzo.) (Głos z sali: Szanowny panie marszałku, bardzo dziękujemy za piękne reprezentowanie nas, za sprawne prowadzenie posiedzenia. Szymon, jeszcze raz gratulacje. Życzę ci powodzenia. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Szanowni Państwo! Panie Marszałku Seniorze! Panie i Panowie Posłowie! Wysoka Izbo! A przede wszystkim: Drodzy Współobywatele! (Głos z sali: Jeszcze pan prezydent.) Jest pan prezydent? Przepraszam, panie prezydencie. Spodziewałem się pana tutaj. Cieszę się, że jest pan wciąż z nami. Bardzo się z tego cieszę. Tego wystąpienia nie sposób nie zacząć tak, jak zrobił to właśnie pan prezydent Andrzej Duda – od podziękowania tym 21 966 891 wyborcom, którzy 15 października zdecydowali w tak jednoznaczny sposób o przyszłości Polski. Dali nam, 460 posłankom i posłom, najsilniejszy w historii wolnej Polski mandat do reprezentowania ich w tej Izbie. To wielki honor, to potężne zobowiązanie. To dowód, że Polki i Polacy naprawdę są bardzo dojrzałym społeczeństwem. (Oklaski) A skoro ten Sejm wziął się z tak bezprecedensowego społecznego zrywu, to na te 4 lata mamy bardzo jasne zadanie: każdego dnia dowodzić, że nasi rodacy nie pomylili się, stojąc 15 października w długich kolejkach pod lokalami wyborczymi. Nie możemy zawieść oglądających nas teraz naszych dzieci i tych, którzy w sztafecie pokoleń stali przed nami w tym miejscu, gdzie teraz stoję, czyli wielkich marszałków Sejmu odrodzonej Rzeczypospolitej, których wspominali już dzisiaj pan prezydent i marszałek senior: wywodzącego się z endecji Wojciecha Trąmpczyńskiego, ludowca Macieja Rataja, socjalisty Ignacego Daszyńskiego. Przyszedłem do polityki spoza polityki. Nie znam jej wszystkich trików, ale znam jej serce, o którym czasem – zbyt często – się zapomina. Polityka to nie przemoc, polityka to troska. Ta sala to nie oktagon z gali MMA, to dom spotkań i rozmowy. Polacy tą ogromną frekwencją powiedzieli nam bardzo wyraźnie: dość już tego, co było. Ma się zmienić nie tylko partia, ma się zmienić polityka. Ona zaczęła się psuć od Sejmu i od Sejmu musi zacząć się jej naprawa. (Oklaski) Dlatego od jutra, nawet od dziś, jak już dowiadujemy się z mediów, wiele się tutaj zmieni. (Głos z sali: Już się boję.) Przede wszystkim przestawimy te dwie litery i najważniejsze znów stanie się tu słowo „patria”, a nie „partia”. (Oklaski) Z gabinetu marszałka z hukiem wyjedzie zamrażarka. Znikną szpecące Sejm policyjne barierki, bo dość już tych barier (Oklaski) nastawiano między nami. Nawiasem mówiąc, nie wiem, czy państwo wiecie, ale nasze słowo, nasza wola, ma niezwykłą moc sprawczą, bo jeszcze zanim powiedzieliśmy o tym my i nasi koledzy, to Policja zaczęła proces rozmontowywania tych barierek, które dzisiaj stoją samotne pod Sejmem. (Oklaski) Poczucie, że Sejm jest oblężoną twierdzą, nie jest budujące. Ten proces zostanie dokończony. W przerwie porozmawiam z panią minister Kaczmarską, z komendantem Straży Marszałkowskiej, skontaktujemy się z komendą stołeczną Policji i te barierki wreszcie, po tych 7 latach, znikną spod Sejmu. (Oklaski) Sejm Rzeczypospolitej Polskiej nigdy więcej nie będzie punktem obsługi rządu. Nie będzie czyjąkolwiek maszynką do głosowania. (Oklaski) Chcę uspokoić państwa posłów, że nie trzeba już będzie udawać, że ma się wniosek formalny, bo będzie można normalnie zabrać głos. Zaproponuję Prezydium, żebyśmy mogli na początku każdego posiedzenia Sejmu mieć serię pytań od szefów klubów i kół poselskich do rządu, do ministrów, żeby tę komunikację udrożnić i nie naruszać powagi tej Izby. Zaproszę w najbliższych dniach najstarszych sejmowym stażem dziennikarzy, by pomogli mi znów mądrze otworzyć dla nich Sejm. Przywrócimy śniadania prasowe z marszałkiem, regularne briefingi, na których przedstawiciele mediów będą mogli dowiedzieć się, co dzieje się w tej Izbie. (Głos z sali: Ooo…) Chcę spróbować wyjść do tych, którzy w demokrację wciąż mało wierzą. Marszałek Sejmu będzie obecny w mediach, będzie miał swój podcast, przez serię wydarzeń, o których opowiem za chwilę… (Poruszenie na sali) Drodzy państwo, jeżeli tylko wyrazicie swoją wolę, będziecie gośćmi tego podcastu (Oklaski), bo jak dobrze wiemy, emocje to jest coś, co współczesne media lubią najbardziej. A jestem przekonany, że ich tam nie zabraknie. (Wypowiedź poza mikrofonem) Ja też oglądałem, droga pani poseł, bardzo ceniłem ten program. Sejm nie będzie azylem dla przestępców. Sejm nie będzie polem do korupcji. Sejm nie będzie nigdy więcej trybuną dla pogardy. Mój cel i program są proste. (Poruszenie na sali, oklaski) (Posłowie skandują: Mejza, Mejza, Mejza!) Widzicie państwo, to dobry moment, idealny wręcz, żeby powiedzieć, że mój cel i program są proste. Chciałbym, aby rodzice, gdy w telewizji pokazują dzieciom Sejm, nie zasłaniali im oczu i nie zatykali uszu. Przeciwnie, by mówili: Zobaczcie, tak można ze sobą rozmawiać, nawet gdy się ze sobą nie zgadzamy. (Oklaski) Szanowni Państwo! Panie Prezydencie! Po tym głosowaniu nikt nie może już mieć wątpliwości, że jest w tym Sejmie większość gotowa do wzięcia odpowiedzialności za kraj. (Oklaski) Wiem też jednak, że wybraliście mnie na marszałka Sejmu, a nie części sali. Zasiadają na niej ugrupowania, z których poglądami głęboko się nie zgadzam. Ale są tu one z woli Polek i Polaków. Zapewniam więc, że Sejm nie będzie kolejną areną wyniszczającej wojny polsko-polskiej. Tu wszystkich posłów, czy z koalicji rządzącej, czy z opozycji, obowiązywać odtąd znów będą te same standardy, a rolą marszałka będzie pilnowanie zasad fair play. Zleciliście mi dziś pracę, rolę stróża powagi i porządku w tej Izbie. Zapowiadam wam więc, że będę bezwzględnie przestrzegał zasad, na które się wspólnie umówiliśmy, z szacunku do tych 21 mln Polaków, którzy nie po to stali nocą w kolejkach, żebyśmy teraz tracili ich cenny czas na kolejne show. Zakładam, że nie tylko jeden ja na tej sali – chciałbym w to wierzyć Projekt uchwał w sprawie ustalenia liczby wicemarszałków Sejmu Rzeczypospolitej Polskiej – mam już za sobą etap show i etap płomiennej publicystyki i że chcecie, żebyśmy wspólnie zbudowali nowy Sejm – Sejm szacunku: do siebie nawzajem i do wszystkich obywateli i obywatelek Rzeczypospolitej, niezależnie od ich wieku, płci, tego, czy są wierzący czy niewierzący, czy mieszkają na wsi czy w małych miastach, czy w metropoliach, czy są seniorami czy osobami z niepełnosprawnością. Drogie Posłanki! Drodzy Posłowie! Witajcie w Sejmie różnych Polaków, w Sejmie Rzeczypospolitej. Wiwat wszystkie stany! (Oklaski) (Poseł Piotr Kaleta: Aż się popłakałem.) Postaramy się coś na to zaradzić, panie pośle. Panie i Panowie Posłowie! Za chwilę zarządzę przerwę, w której będę oczekiwał na przedłożenie projektu uchwały, o której mowa w art. 5 ust. 2 regulaminu Sejmu, dotyczącej ustalenia liczby wicemarszałków Sejmu. W tym celu zarządzam przerwę w obradach do godz. 17.30.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Szanowni Państwo! Wznawiam obrady. Przystępujemy do rozpatrzenia punktu 2. porządku dziennego: Poselskie projekty uchwał w sprawie ustalenia liczby wicemarszałków Sejmu Rzeczypospolitej Polskiej (druki nr 1 i 2). Chcę poinformować państwa, że tych projektów uchwał wpłynęło więcej, ale wpłynęły po czasie, który uzgodniliśmy sobie na składanie tych wniosków. Z naszych informacji wynika, że wnioski są tożsame, a więc przystąpimy tylko do rozpatrzenia tych dwóch wniosków, które zostały złożone w czasie, na który się umówiliśmy. Sejm, zgodnie z art. 5 ust. 2 regulaminu Sejmu, ustala liczbę wicemarszałków w drodze uchwały. Na podstawie art. 5 ust. 4 regulaminu Sejmu do tego projektu uchwały nie stosuje się przepisów o terminie wniesienia i doręczenia projektów. Projekt tej uchwały rozpatruje się w jednym czytaniu. Proszę pana posła Stanisława Tyszkę o przedstawienie uzasadnienia projektu uchwały z druku nr 1.",
                },
                {
                    "speaker": "Poseł Stanisław Tyszka",
                    "content": "Dziękuję bardzo. Panie Marszałku! Wysoka Izbo! O ile wiem, treść naszego projektu uchwały jest tożsama z drukiem nr 2, czyli proponujemy sześciu wicemarszałków. Proponujemy w tym celu, żeby każdy klub reprezentowany w Sejmie X kadencji miał przedstawiciela w gremium zarządzającym pracami Sejmu. To wynika po prostu z szacunku do wyborców, z szacunku do wszystkich ludzi, którzy poszli oddać na nas głosy. My jako najmniejszy klub tej kadencji również chcemy reprezentować 1,5 mln ludzi, którzy oddali na nas głosy i współtworzyć porządek prac Sejmu X kadencji. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo panu posłowi. Proszę pana posła Borysa Budkę o przedstawienie uzasadnienia projektu uchwały z druku nr 2.",
                },
                {
                    "speaker": "Poseł Borys Budka",
                    "content": "Panie Marszałku! Wysoka Izbo! W imieniu klubu Koalicji Obywatelskiej składam wniosek o ustalenie liczby wicemarszałków na sześć osób. Kierujemy się bardzo prostą zasadą, że każde ugrupowanie, każdy klub parlamentarny powinien mieć swojego przedstawiciela. Przypomnę, że nie zawsze była to reguła w tej Izbie. W 2015 r. ci, którzy dzisiaj apelują o zasady, złamali tę zasadę. Klub Polskiego Stronnictwa Ludowego został pozbawiony reprezentacji w Prezydium Sejmu. Zrobiono to w sposób absolutnie urągający wszelkim zasadom. (Poseł Jakub Rutnicki: I co?) (Głos z sali: Hańba!) Natomiast, Wysoka Izbo, panie marszałku, szanowni państwo, jest jedna podstawowa zasada. Prezydium Sejmu jest przeznaczone dla osób, które szanują elementarne zasady parlamentaryzmu. (Oklaski) Prezydium Sejmu to miejsce, w którym nie mogą znaleźć się ludzie, którzy przez ostatnie 8 lat w sposób ordynarny łamali polską konstytucję, łamali zasady parlamentaryzmu, którzy w sposób absolutnie bezczelny traktowali tę Izbę jak maszynkę do głosowania. (Głos z sali: Kłamstwo!) (Głos z sali: Sam jesteś maszynką.) Dlatego klub Koalicji Obywatelskiej z oczywistych względów odmówi poparcia tym kandydaturom, które będą godziły w demokratyczne zasady w tej Izbie. (Poseł Barbara Bartuś: To jest uzasadnienie projektu uchwały?) I chciałbym, żeby była to wykładnia dla wszystkich, którzy będą podejmować decyzje w tej sprawie. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję panu posłowi. Wiem, że są zgłoszenia do dyskusji. Proponuję, żeby w dyskusji nad tym punktem porządku dziennego Sejm wysłuchał 3-minutowych oświadczeń w imieniu klubów i koła. Jeśli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycję przyjął. Projekt uchwał w sprawie ustalenia liczby wicemarszałków Sejmu Rzeczypospolitej Polskiej Sprzeciwu nie słyszę. Otwieram dyskusję. Jako pierwszy głos zabierze pan poseł Krzysztof Paszyk z Klubu Parlamentarnego PSL – Trzecia Droga. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Krzysztof Paszyk",
                    "content": "Bardzo dziękuję. Panie Marszałku! Panie i Panowie Posłowie! Czas szybko leci. O pewnych zdarzeniach opinia publiczna i część tej Izby pewnie gotowa była zapomnieć, ale warto dzisiaj, w tym momencie przypomnieć analogiczny okres, jesień roku 2015. Klub Parlamentarny Polskiego Stronnictwa Ludowego, wtedy świeżo ukonstytuowany, zgłosił akces to tego, aby uszanowano w tej Izbie wieloletni, wielokadencyjny, chciałoby się powiedzieć, obyczaj dotyczący przedstawicielstwa każdego klubu parlamentarnego w Prezydium Sejmu, w prezydium tej Izby. Wówczas z niezrozumiałych zupełnie powodów, tylko po to, aby rozpocząć polityczną wendetę na Polskim Stronnictwie Ludowym przez prawą stronę sali politycznej, ostentacyjnie pozbawiono nas szansy udziału w Prezydium Sejmu. Mało tego, pozbawiono nas szansy na przewodniczenie nawet w najmniejszej komisji sejmowej. Dlaczego? Z powodów czysto politycznych, aby niszczyć, aby deptać Polskie Stronnictwo Ludowe, które wtedy miało pełne prawo do tego, aby uczestniczyć w obradach Prezydium Sejmu, aby uczestniczyć w obradach prezydiów komisji. Dlaczego? Ponieważ Polacy zdecydowali wtedy, aby nasi przedstawiciele, posłowie Polskiego Stronnictwa Ludowego, mają zasiadać w tej Izbie. Jako Klub Parlamentarny Polskie Stronnictwo Ludowe – Trzecia Droga chcemy dzisiaj przestrzec przed deptaniem dobrych, parlamentarnych zwyczajów, chcemy jednoznacznie wrócić do dobrego obyczaju, aby każdy klub parlamentarny, który za sprawą poparcia wielu setek tysięcy, milionów Polaków znalazł się w tej Izbie, miał prawo do zasiadania w Prezydium Sejmu. Chcemy dać jasny, jednoznaczny sygnał, że nie ma zgody – Polacy jasno wyrazili to w tych wyborach – absolutnie nie ma zgody na to, żeby w imię partykularnych, partyjniackich interesów deptać te dobre obyczaje. Dlatego dzisiaj jednoznacznie opowiadamy się za tym, aby w Prezydium Sejmu X kadencji reprezentowane były wszystkie kluby parlamentarne zasiadające na tej sali. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Głos zabierze pani poseł Paulina Hennig-Kloska z Klubu Parlamentarnego Polska 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Paulina Hennig-Kloska",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Posłanki! Panowie Posłowie! Klub Parlamentarny Polska 2050 – Trzecia Droga złożył tożsamy projekt uchwały powołującej sześciu wicemarszałków. Wpłynął po czasie, dlatego nie może być uwzględniony, ale oczywiście będziemy głosować za tym rozwiązaniem. Powód, dla którego podjęliśmy taką decyzję, jest bardzo prosty. Jako małe koło parlamentarne złożone pod koniec kadencji z sześciu parlamentarzystów bardzo często byliśmy pozbawiani możliwości wykonywania swoich obowiązków, a nasze prawa były pomijane. Działo się tak m.in. za sprawą pani marszałek Witek. Niestety, pani marszałek, dokładnie pamiętam, jak potrafiła pani dopuścić posłów wszystkich klubów do głosu np. w ramach prozaicznych, prostych wniosków formalnych, a mnie pani po prostu bardzo często nie dopuszczała. (Głos z sali: Uuu…) (Poseł Barbara Bartuś: Ale przecież to jest regulamin Sejmu, a nie zła wola pani marszałek.) Szanowni Państwo! Demokracja to coś więcej niż dzień wyborów. Demokracja to także umiejętność wsłuchiwania się w głos mniejszości, z którym czasami się po prostu nie zgadzamy. Niestety pani jako marszałkini tej Izby nie potrafiła tego robić w momencie, kiedy byliśmy mniejszym kołem. (Oklaski) (Głos z sali: Marszałek!) Dlatego Klub Parlamentarny Polska 2050 – Trzecia Droga będzie głosował za uchwałą powołującą sześciu marszałków, tak aby każdy klub miał możliwość współuczestniczenia w procesie tworzenia harmonogramu Sejmu, a także odmrażania szuflad w gabinecie marszałka. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, pani poseł. Głos zabierze pan poseł Krzysztof Gawkowski z Klubu Parlamentarnego Nowa Lewica.",
                },
                {
                    "speaker": "Poseł Krzysztof Gawkowski",
                    "content": "Panie Marszałku! Wysoka Izbo! 15 października Polska się obudziła. Obudziła się i ponad 21 mln Polek i Polaków przy urnach wyborczych udowodniło, że chce zmiany, również zmiany tego, jak ma wyglądać debata parlamentarna, zmiany narracji, traktowania, zmiany dotyczącej umiejętności szukania kompromisu, a przede wszystkim szacunku, szacunku dla tych kół, dla tych klubów, które mają swoich parlamentarzystów. W poprzedniej kadencji Lewica zawsze szukała porozumienia. Pomimo różnic, a często braku wspólnych tematów, chcieliśmy siadać do stołu, rozmawiać, a nie rozpoczynać od wojen na tej sali plenarnej, które zazwyczaj kończyły się wojną polsko-polską. Projekt uchwał w sprawie ustalenia liczby wicemarszałków Sejmu Rzeczypospolitej Polskiej – głosowanie Dobrą zasadą na przyszłość, nie tylko w tej kadencji, jest wprowadzenie tego zwyczaju, zgodnie z którym ile jest klubów, tylu mamy marszałków wybranych do prezydium tej Izby. Odpowiedzialność za tę decyzję spoczywa w rękach nas wszystkich. Klub Lewicy bierze na siebie tę odpowiedzialność, dlatego zdecydowaliśmy, że poprzemy uchwałę, która zdecyduje o tym, że będziemy wybierali sześciu wicemarszałków. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo panu posłowi. Jako ostatni ze zgłoszonych głos zabierze pan poseł Łukasz Schreiber z Klubu Parlamentarnego Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Łukasz Schreiber",
                    "content": "Panie Marszałku! Panie Premierze! Wysoka Izbo! Padło bardzo dużo słów o wzajemnym szacunku, o tym, by każdy klub parlamentarny mógł mieć swojego przedstawiciela w Prezydium Sejmu. Oczywiście Prawo i Sprawiedliwość to popiera. Chciałbym także przypomnieć kolegom, którzy może trochę gorzej znają historię parlamentaryzmu, że w 2001 r. w tej Izbie głosami ówczesnej większości, czyli SLD i PSL, nie dopuszczono do tego, by swoich przedstawicieli w prezydium miały Prawo i Sprawiedliwość oraz Liga Polskich Rodzin. To po pierwsze. Po drugie, chciałem zabrać głos, żeby przypomnieć sytuację z 2015 r., którą przedstawiono tutaj w nieprawdziwy sposób. Otóż przez 8 lat rządów Prawa i Sprawiedliwości, przez 8 lat, w trakcie których Prawo i Sprawiedliwość miało samodzielną większość w tej Izbie, w Prezydium zawsze było trzech przedstawicieli większości parlamentarnej i trzech przedstawicieli opozycji. Myślę, że jeżeli ktoś mówi o dobrych obyczajach, to, jak rozumiem, będzie się odnosił właśnie do tych standardów. (Oklaski) Wysoka Izbo! To, co dzisiaj słyszymy, że największy klub parlamentarny liczący 194 osoby być może będzie miał jednego wicemarszałka, ale pod warunkiem, że będzie to ktoś taki, kto się wam podoba, jest, Wysoka Izbo, kpiną… (Głos z sali: Tak!) (Głos z sali: Hańba!) …z dobrych obyczajów. To nie ma z nimi nic wspólnego. (Oklaski) Apeluję także o refleksję oraz o to, by faktycznie zacząć od wzajemnego szacunku. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo panu posłowi. Lista posłów zapisanych do głosu została wyczerpana. Zamykam dyskusję. Przechodzimy do głosowania nad tożsamymi projektami uchwał. Wnioskodawcy w przedłożonych projektach uchwał proponują, aby ustalić liczbę wicemarszałków Sejmu na sześć osób. Przystępujemy do głosowania. Kto z pań i panów posłów jest za ustaleniem liczby wicemarszałków Sejmu Rzeczypospolitej Polskiej na sześć, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 458 posłów. Wszyscy byli za, nikt nie był przeciw, nikt się nie wstrzymał. Stwierdzam, że Sejm Rzeczypospolitej Polskiej ustalił liczbę wicemarszałków Sejmu na sześć osób. Drodzy Państwo! Określam termin zgłaszania kandydatów na wicemarszałków Sejmu – na godz. 18.30. Proszę, żeby do godz. 18.30 wpłynęły zgłoszenia kandydatów na wicemarszałków Sejmu, tak żeby Kancelaria Sejmu mogła przygotować stosowne druki uchwał. Zarządzam przerwę w obradach do godz. 19.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Wznawiam obrady. Przepraszam państwa bardzo za przedłużenie przerwy. To wyniknęło z prośby Sekretariatu Posiedzeń Sejmu, konieczności dodatkowej pracy nad uchwałami, nad którymi za chwilę będziemy głosować. Przystępujemy do rozpatrzenia punktu 3. porządku dziennego: Wybór wicemarszałków Sejmu Rzeczypospolitej Polskiej (druki nr 3, 4, 5, 6, 7 i 8). Informuję, że grupy posłów zgłosiły następujących kandydatów na wicemarszałków Sejmu: pana posła Krzysztofa Bosaka, pana posła Włodzimierza Czarzastego, panią poseł Dorotę Niedzielę, panią poseł Monikę Wielichowską, panią poseł Elżbietę Witek (Oklaski), pana posła Piotra Zgorzelskiego. Proszę pana posła Michała Wawera o przedstawienie kandydatury pana posła Krzysztofa Bosaka.",
                },
                {
                    "speaker": "Poseł Michał Wawer",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Mam zaszczyt dzisiaj po raz pierwszy w życiu przemawiać z tego miejsca do Wysokiej Izby, więc z góry przepraszam, jeżeli będzie widać zdenerwowanie, ale niech to moje ewentualnie widoczne zdenerwowanie tylko podkreśla to, jak wielkie doświadczenie ma kandydat… (Gwar na sali) (Głos z sali: Mów.)",
                },
                {"speaker": "Marszałek", "content": "Bardzo proszę państwa o spokój."},
                {
                    "speaker": "Poseł Michał Wawer",
                    "content": "…którego mam przyjemność zaprezentować, czyli Krzysztof Bosak. Krzysztofa Bosaka nie trzeba nikomu przedstawiać. (Oklaski, wesołość na sali) Jego rozpoznawalność jest powszechna zarówno na tej sali, jak i w skali całego kraju. Jego kompetencje, kultura osobista, sprawność retoryczna zdobyły uznanie nie tylko wyborców Konfederacji, ale w ogóle powszechny szacunek w całym polskim społeczeństwie, ponad podziałami politycznymi, również wśród polityków innych opcji. Nawiązując do tego, co pan marszałek mówił w swoim inauguracyjnym przemówieniu: potrzebujemy w Prezydium Sejmu Rzeczypospolitej Polskiej ludzi dialogu, którzy potrafią pomimo różnic światopoglądowych kulturalnie, konstruktywnie rozmawiać na każdy temat, który będzie przedmiotem obrad tego Sejmu przez najbliższe 4 lata. Krzysztof Bosak jest właśnie takim człowiekiem: człowiekiem dialogu, zdolnym do kulturalnej wymiany poglądów na każdy temat, również wtedy, kiedy występują skrajne różnice zdań, a w tej Izbie takie różnice będą z całą pewnością w najbliższych latach występować. Nie znaczy to, że Krzysztof w jakimkolwiek zakresie kiedykolwiek ze swoich poglądów rezygnował. Ja z Krzysztofem znamy się od, jeśli dobrze liczę, 17 lat i w tym okresie Krzysztof nigdy w żadnej ważnej sprawie ze swoich poglądów nie zrezygnował, ale zawsze potrafił o nich rozmawiać w sposób kulturalny, wyważony, z szacunkiem do rozmówców, nawet do tych, którzy mieli, tak jak mówię, skrajnie odmienne poglądy. Jeżeli szukamy członka Prezydium Sejmu Rzeczypospolitej Polskiej, który będzie reprezentował poglądy 1,5 mln wyborców Konfederacji, to nie ma lepszego kandydata, który zapewniłby rzeczywistą reprezentatywność i demokratyczny charakter Prezydium Sejmu. Obszerne kompetencje i doświadczenie polityczne Krzysztofa są znane, więc o tym mówił nie będę, powiem natomiast o tym, o czym nie wszyscy muszą w tej Izbie wiedzieć, mianowicie o jego innych doświadczeniach i kompetencjach. Mianowicie w tych okresach… Może inaczej: korzenie Krzysztofa Bosaka, jego motywacja do tego, żeby zająć się polityką, mają charakter czysto społeczny, trzeciosektorowy. Krzysztof, zanim został po raz pierwszy posłem w 2005 r., działał w organizacjach katolickich, narodowych, harcerskich, również republikańskich. I to są korzenie, do których powrócił po tym, kiedy w 2007 r. nie udało mu się odnowić mandatu. Przez 12 lat poza Sejmem pracował w think tankach, organizacjach społecznych, jako ekspert, analityk, w redakcjach pism i portali. I to przełożyło się na unikalne doświadczenie i kompetencje, które wykorzystuje w pracy poselskiej i które wniesie również do pracy Prezydium Sejmu. Przecież Prezydium Sejmu, każdy z wicemarszałków, musi po trosze znać się na wszystkim, jako że wicemarszałkowie zajmują się projektami ustaw z rozmaitych dziedzin, z rozmaitych obszarów. Krzysztof Bosak jest kandydatem gwarantującym zarazem dialog, jak i stałość poglądów. Proszę więc Wysoką Izbę o poparcie go, jeżeli chcemy, aby Prezydium tego Sejmu było rzeczywiście reprezentatywne i demokratyczne. Ja z Krzysztofem znamy się od lat kilkunastu i pracujemy razem od lat kilku. (Głos z sali: Ha, ha, ha.) Nigdy się tą współpracą nie rozczarowałem. Rekomenduję Wysokiej Izbie, żeby dała sobie szansę na to, żeby również skorzystać na współpracy z wicemarszałkiem Krzysztofem Bosakiem. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie Pośle Krzysztofie Bosak! Ma pan w tej Izbie wielu wielbicieli, co było słychać. Dziękuję bardzo panu posłowi. Proszę pana posła Krzysztofa Gawkowskiego o przedstawienie kandydatury pana posła Włodzimierza Czarzastego na wicemarszałka Sejmu.",
                },
                {
                    "speaker": "Poseł Krzysztof Gawkowski",
                    "content": "Panie Marszałku! Wysoka Izbo! Pan poseł Włodzimierz Czarzasty jest współprzewodniczącym Nowej Lewicy, ale ma też bogatą przeszłość (Wesołość na sali) związaną z wykształceniem, odpowiedzialnością za państwo, budowaniem porozumienia w tej Izbie, a przede wszystkim jest człowiekiem mediów i kultury. Jeżeli chodzi o tę kulturę, nieraz na tej sali mieliśmy poczucie, że mogą być inne standardy, że można zabierać głos i nie trzeba go odbierać. (Oklaski) Mieliśmy poczucie, że marszałek Sejmu to nie tylko osoba, człowiek, ale przede wszystkim bycie marszałkiem oznacza umiejętność szukania dialogu. I takim właśnie człowiekiem, takim posłem, takim wicemarszałkiem Sejmu w poprzedniej kadencji był pan poseł Włodzimierz Czarzasty. Przez wiele lat pracował w obszarze mediów i kultury. Założył jedno z największych polskich wydawnictw – wydawnictwo Muza. Pracował również w Radzie Nadzorczej Polskiego Radia, był jej przewodniczącym, oraz w Krajowej Radzie Radiofonii i Telewizji, gdzie z nominacji Aleksandra Kwaśniewskiego sprawował funkcję sekretarza rady radiofonii i telewizji. W latach 2006–2017 był przewodniczącym zarządu Stowarzyszenia „Ordynacka”. (Poseł Anita Czerwińska: A wcześniej?) Włodzimierz Czarzasty był posłem IX i jest posłem X kadencji. Przez ostatnie 4 lata swoją funkcję wykonywał z zaangażowaniem i udowodnił, że warto mu po raz kolejny powierzyć funkcję członka Prezydium Sejmu RP. Włodzimierz Czarzasty jest absolwentem Wydziału Dziennikarstwa i Nauk Politycznych Uniwersytetu Warszawskiego. Z całą mocą, serdecznością i przyjacielską chęcią rekomenduję państwu głosowanie na Włodzimierza Czarzastego w celu pełnienia przez niego funkcji wicemarszałka Sejmu RP. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Teraz proszę pana posła Borysa Budkę o przedstawienie kandydatur pani poseł Doroty Niedzieli oraz pani poseł Moniki Wielichowskiej. (Oklaski)",
                },
                {
                    "speaker": "Poseł Borys Budka",
                    "content": "Panie Marszałku! Wysoka Izbo! Szanowni Państwo! Niezwykły to zaszczyt i olbrzymia przyjemność móc zaprezentować Wysokiej Izbie dwie wspaniałe kandydatury, dwie osoby, które Koalicja Obywatelska rekomenduje na stanowiska wicemarszałkiń Sejmu RP. Dorota Niedziela to posłanka z Oświęcimia. Jest absolwentką Wydziału Medycyny Weterynaryjnej Akademii Rolniczej we Wrocławiu. Specjalizuje się w chirurgii weterynaryjnej i radiologii. Ale przede wszystkim dała się poznać jako bardzo zaangażowana posłanka VII, VIII, IX i X kadencji. Wybitna ekspertka, jeżeli chodzi o kwestie związane z prawami zwierząt, z rolnictwem, ale równocześnie człowiek o niesamowicie ciepłym sercu. Wiele i wielu z nas miało okazję poznać Dorotę Niedzielę w trudnych chwilach, kiedy zawsze była gotowa służyć swoją radą, kiedy służyła swoją pomocą i zawsze była otwarta na to, by wysłuchać. Jestem przekonany, że Sejm Rzeczypospolitej i Prezydium Sejmu potrzebują właśnie takich osób – jednocześnie kompetentnych, wiedzących, po co są w polityce, ale z drugiej strony bardzo otwartych również na tych, którzy mają inne poglądy. To, co robi w parlamencie i jak jest oceniana, najlepiej pokazują wyniki wyborcze, bo, tak jak wspomniałem, nieprzerwanie od 2011 r. jest posłanką na Sejm Rzeczypospolitej. Pani poseł Dorota Niedziela ma doświadczenie w pracy parlamentarnej, pełniła w zeszłej kadencji m.in. funkcję zastępcy przewodniczącego Komisji Rolnictwa i Rozwoju Wsi, jest wiceprzewodniczącą Platformy Obywatelskiej, jak również pełniła funkcję sekretarza stanu w Ministerstwie Środowiska. Jestem przekonany, że kandydatura pani posłanki Doroty Niedzieli to kandydatura, która spotka się z powszechną akceptacją w Wysokiej Izbie, bo właśnie takie osoby powinny nas reprezentować i kierować pracami tej Izby. Dlatego w imieniu klubu Koalicji Obywatelskiej proszę panie posłanki i panów posłów o poparcie tej kandydatury. (Oklaski) Jeżeli pan marszałek pozwoli, to od razu w imieniu klubu Koalicji Obywatelskiej chciałbym państwu rekomendować drugą z kandydatur. Pani posłanka Monika Wielichowska doświadczenie parlamentarne zdobywała, pełniąc mandat posłanki z okręgu wałbrzyskiego już od VI kadencji Sejmu, nieprzerwanie wybierana i potwierdzająca swój mandat w kolejnych wyborach, z rekordowym poparciem w okręgu wałbrzyskim w tegorocznych wyborach. Ale Monika Wielichowska to również doświadczona samorządowiec, to osoba, która pełniła funkcję starosty powiatu kłodzkiego. Jest magistrem ekonomii, zdobyła wykształcenie na Akademii Ekonomicznej we Wrocławiu. Dodatkowo jest absolwentką Podyplomowego Studium Dziennikarstwa i Zarządzania Informacją na Uniwersytecie Wrocławskim oraz studiów podyplomowych dotyczących funduszy europejskich, a także studiów podyplomowych w zakresie zarządzania i finansowania infrastruktury drogowej w Szkole Głównej Handlowej w Warszawie. Każdy, kto zna panią posłankę Monikę Wielichowską, wie doskonale, że to osoba niezwykle dobrze zorganizowana, o wysokich umiejętnościach menedżerskich, która potrafi sprostać każdemu zadaniu organizacyjnemu. My w Koalicji Obywatelskiej i w Platformie Obywatelskiej wiemy doskonale, że jeżeli jest jakieś trudne zadanie do wykonania, zorganizowanie naprawdę dużego przedsięwzięcia, to Monika Wielichowska jest w stanie sprostać każdemu zadaniu. Właśnie takie osoby są potrzebne, by w tym najważniejszym dla Sejmu Rzeczypospolitej organie, czyli Prezydium Sejmu, reprezentować posłanki i posłów, by kierować pracami Sejmu wspólnie z marszałkiem Sejmu, by być otwartymi na sugestie, by wiedzieć, jak prawidłowo pomagać posłankom i posłom w realizacji ich mandatu poselskiego. Jestem przekonany, że również ta kandydatura, kandydatura posłanki Moniki Wielichowskiej, będzie cieszyła się państwa poparciem. Dlatego w imieniu klubu Koalicji Obywatelskiej chciałbym również rekomendować panią posłankę na funkcję wicemarszałkini Sejmu Rzeczypospolitej. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Bardzo proszę pana posła Jarosława Kaczyńskiego o przedstawienie kandydatury pani poseł Elżbiety Witek. (Oklaski) (Głos z sali: Ooo…)",
                },
                {
                    "speaker": "Poseł Jarosław Kaczyński",
                    "content": "Panie Marszałku! Wysoka Izbo! Pani marszałek Witek była przez przeszło 50 miesięcy marszałkiem Sejmu. I to był naprawdę wyjątkowo trudny czas. (Głosy z sali: To prawda.) To był wyjątkowo trudny czas ze względu na to, że opozycja ogłosiła się opozycją totalną, ale nie tylko się ogłosiła, ale niestety także była opozycją totalną. W związku z tym tutaj, w Sejmie, mieliśmy do czynienia z niebywałym wręcz poziomem agresji, grubiaństwa, po prostu chamstwa. (Poseł Sławomir Nitras: Mordy zdradzieckie.) I to wszystko pani marszałek znosiła naprawdę z anielską cierpliwością i ogromną kulturą. (Oklaski) I choćby tylko to jest wystarczającym powodem, żeby ją na to stanowisko wybrać. Nie mówię już tutaj o ogólnych regułach, które powinny obowiązywać w normalnie funkcjonującym parlamencie. (Głos z sali: Bez trybu.) Natomiast wiadomo, że wy stosujecie zasadę odwracania znaczeń słów i odznaczania znaczeń sytuacji. (Głos z sali: Kota.) (Głos z sali: A wy bez trybu.) Wy nieustannie próbujecie uznać się za opozycję demokratyczną, a macie do tego dokładnie takie samo prawo jak Blok Demokratyczny z lat 40. Dokładnie takie samo prawo. (Oklaski) (Głos z sali: Uuu…) (Poseł Marcin Kierwiński: Słabe.) A nawet dzisiaj posuwacie się już dalej niż oni, bo oni przynajmniej formalnie nie deklarowali, że zlikwidują państwo polskie. I to wszystko, co mam do powiedzenia. (Oklaski) (Głos z sali: Zejdź.) (Poseł Jakub Rutnicki: Hańba!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję panu posłowi. Proszę teraz pana posła Władysława Kosiniaka-Kamysza o przedstawienie kandydatury pana posła Piotra Zgorzelskiego.",
                },
                {
                    "speaker": "Poseł Władysław Kosiniak-Kamysz",
                    "content": "Panie Marszałku! Wysoka Izbo! W imieniu klubu parlamentarnego PSL –Trzecia Droga mam zaszczyt przedstawić kandydaturę pana posła Piotra Zgorzelskiego na funkcję wicemarszałka Sejmu. Mówię to już nie w imieniu partii tworzących opozycję demokratyczną, tylko większość parlamentarną. I to jest bardzo ważna zmiana, która nastąpiła po tych wyborach. A do tej zmiany przyczynił się w zasadniczy sposób pan marszałek Piotr Zgorzelski, który będąc przez ostatnie 4 lata wicemarszałkiem tej Izby, a wcześniej posłem VII, VIII, IX i obecnej kadencji, wykazał się niezwykłą starannością w pełnieniu mandatu posła, co obywatele i wyborcy docenili, każdorazowo w większej liczbie oddając na niego głos – w każdych wyborach ta liczba znacząco wzrastała, do najwyższego poziomu w ostatnich wyborach. Pan marszałek Piotr Zgorzelski jest absolwentem Uniwersytetu Łódzkiego, historii na Uniwersytecie Łódzkim, jest absolwentem studiów podyplomowych na Uniwersytecie Mikołaja Kopernika w Toruniu w zakresie ekonomii i Szkoły Wyższej w Płocku im. Pawła Włodkowica w zakresie integracji europejskiej. Jest samorządowcem z krwi i kości i z tego powodu był zawsze najbardziej dumny: deklaruje, że jedną z najpiękniejszych misji, jaką mu przyszło sprawować i pełnić, była funkcja starosty płockiego, jego ukochanego miasta i powiatu, do którego zawsze się odwołuje. Wcześniej był samorządowcem w gminie Bielsk w powiecie płockim, jak również pełnił zaszczytne funkcje w administracji samorządu województwa mazowieckiego. Czyli przeszedł wszystkie stopnie i zna wszystkie poziomy samorządności w Polsce. Pan poseł Piotr Zgorzelski jest organizatorem i niestrudzonym orędownikiem prawdy dotyczącej historii, również tej trudnej. Jest współautorem uchwały upamiętniającej rzeź na Wołyniu i ustanawiającej 11 lipca dniem pamięci o tych bardzo tragicznych, ale jakże znaczących w pamięci naszej wydarzeniach. Jest współtwórcą okrągłego stołu w sprawie wymiaru sprawiedliwości dotyczącego pokrzywdzonych. I to są dokonania w ostatnich latach, które w niezwykły sposób wpisały się w aktywność parlamentarną pana posła Piotra Zgorzelskiego. W działalności politycznej, tak jak w byciu wicemarszałkiem, cechują go moim zdaniem dwie niezwykle ważne cechy potrzebne do zasiadania w tak ważnym miejscu, tj. skuteczność i życzliwość. Te dwie rzeczy czasem jest bardzo trudno połączyć. Jemu się to skutecznie udaje. Skuteczność w działaniu, czasem bezkompromisowość i stanowczość, również kiedy zasiada w fotelu marszałka, prowadzi obrady, ale i życzliwość wobec wszystkich, którzy w tej Izbie zasiadają, i niezwykła staranność w pełnieniu swojej funkcji, o czym mogą zaświadczyć ci, którzy pracują w Kancelarii Sejmu. Wielokrotnie spotykałem się z wyrazami uznania wszystkich pracowników Sejmu, niezależnie od tego, w jakiej komórce organizacyjnej, w jakim miejscu pełnią swoją misję, dla posługi, dla tego, co robi pan marszałek Piotr Zgorzelski. Jest dla mnie niezwykłym zaszczytem i dumą, że 4 lata temu mogłem prezentować tę kandydaturę. Bardzo rzadko zdarza się w polskim parlamentaryzmie, że ta misja jest kontynuowana. Dzisiaj mam ogromny zaszczyt powtórzyć tę rekomendację i poprosić Wysoką Izbę o poparcie kandydatury pana posła Piotra Zgorzelskiego na funkcję wicemarszałka Sejmu Rzeczypospolitej. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Czy ktoś z pań i panów posłów pragnie zabrać głos w sprawie zgłoszonych kandydatur? Nikt się nie zgłasza. Sejm zgodnie z art. 5 ust. 6, w związku z art. 4 ust. 3 regulaminu Sejmu, wybiera wicemarszałków Sejmu bezwzględną większością głosów. Informuję, że liczba zgłoszonych kandydatów odpowiada liczbie wicemarszałków ustalonej w uchwale Sejmu, w związku z tym Sejm przeprowadzi głosowanie w tej sprawie kolejno nad poszczególnymi kandydaturami za pomocą urządzenia do liczenia głosów, stosując sekwencję pytań: kto jest za, kto jest przeciw, kto się wstrzymał. Głosować będziemy nad kandydaturami w porządku alfabetycznym. Przystępujemy do głosowania nad kandydaturą posła Krzysztofa Bosaka. Kto z pań i panów posłów jest za wyborem na stanowisko wicemarszałka Sejmu pana posła Krzysztofa Bosaka, zechce podnieść rękę i nacisnąć przycisk. (Głos z sali: Nie działa, panie marszałku.) Nie działa? Działa, jak trzeba? Kto jest przeciw? Kto się wstrzymał? Głosowało 452 posłów. Za – 272, przeciw – 27, wstrzymało się 153. Stwierdzam, że Sejm bezwzględną większością głosów wybrał pana Krzysztofa Bosaka na stanowisko wicemarszałka Sejmu Rzeczypospolitej Polskiej. (Oklaski) Gratuluję, panie pośle. Przystępujemy do głosowania nad kandydaturą posła Włodzimierza Czarzastego. Kto z pań i panów posłów jest za wyborem na stanowisko wicemarszałka Sejmu pana posła Włodzimierza Czarzastego, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 458 posłów. Za – 250, przeciw – 196, wstrzymało się 12. Stwierdzam, że Sejm bezwzględną większością głosów wybrał pana posła Włodzimierza Czarzastego na stanowisko wicemarszałka Sejmu Rzeczypospolitej Polskiej. (Oklaski) Przystępujemy do głosowania nad kandydaturą pani poseł Doroty Niedzieli. Kto z pań i panów posłów jest za wyborem na stanowisko wicemarszałka Sejmu pani poseł Doroty Niedzieli, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 458 posłów. Za – 257, przeciw – 185, wstrzymało się 16. Stwierdzam, że Sejm bezwzględną większością głosów wybrał panią poseł Dorotę Niedzielę na stanowisko wicemarszałka Sejmu Rzeczypospolitej Polskiej. (Oklaski) Gratulacje, pani poseł. Przystępujemy do głosowania nad kandydaturą pani poseł Moniki Wielichowskiej. Kto z pań i panów posłów jest za wyborem na stanowisko wicemarszałka Sejmu pani poseł Moniki Wielichowskiej, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 456 posłów. Za – 252, przeciw – 186, wstrzymało się 18. Stwierdzam, że Sejm bezwzględną większością głosów wybrał panią poseł Monikę Wielichowską na stanowisko wicemarszałka Sejmu Rzeczypospolitej Polskiej. (Oklaski) Gratulacje, pani poseł. Przystępujemy do głosowania nad kandydaturą pani poseł Elżbiety Witek. Kto z pań i panów posłów jest za wyborem na stanowisko wicemarszałka Sejmu pani poseł Elżbiety Witek, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 458 posłów. Za – 203, przeciw – 252, wstrzymało się 3. Stwierdzam, że wobec nieuzyskania bezwzględnej większości głosów Sejm nie wybrał pani poseł Elżbiety Witek na stanowisko wicemarszałka Sejmu Rzeczypospolitej Polskiej. (Oklaski) (Głos z sali: Ooo…) (Głos z sali: Brawo!) Przystępujemy do głosowania nad kandydaturą pana posła Piotra Zgorzelskiego. Kto z pań i panów posłów jest za wyborem na stanowisko wicemarszałka Sejmu pana Piotra Zgorzelskiego, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 456 posłów. Za – 267, przeciw – 184, wstrzymało się 5. Stwierdzam, że Sejm bezwzględną większością głosów wybrał pana posła Piotra Zgorzelskiego na stanowisko wicemarszałka Sejmu Rzeczypospolitej Polskiej. (Oklaski) (Głos z sali: Brawo!) W związku z tym, że Sejm nie dokonał wyboru wicemarszałka Sejmu, procedurę jego wyboru przeprowadzimy ponownie w późniejszym terminie. Drodzy Państwo! Za chwilę zarządzę przerwę w obradach, podczas której zwołam posiedzenia Prezydium Sejmu i Konwentu Seniorów w sprawie kontynuacji 1. posiedzenia Sejmu oraz realizacji planowanego porządku dziennego. Informuję członków Prezydium Sejmu, że pierwsze posiedzenie Prezydium Sejmu X kadencji odbędzie się o godz. 20.15 w gabinecie marszałka Sejmu, a w następnej kolejności odbędzie się tam posiedzenie Konwentu Seniorów. Planowane jest teraz przerwanie obrad w posiedzeniu do jutra, tj. do dnia 14 listopada, do godz. 16. Mówię: planowane, a nie: zarządzam, ponieważ będzie to decyzja Prezydium Sejmu, którą temuż Prezydium będę gorąco rekomendował. Zaczniemy po południu, dlatego że, jak państwo wiecie, mamy wiele obowiązków w czasie tego 1. posiedzenia związanych z wyborem różnych organów państwa i chcemy dać państwu czas jutro rano na przygotowanie stosownych wniosków, kandydatur i dopełnienie wszelkich formalności, tak żebyśmy mogli sprawnie przez ten proces po południu przejść, a następnie najprawdopodobniej kontynuować obrady Sejmu w przyszłym tygodniu, dalej idąc tym procesem, którego regulamin i konstytucja wymagają, żeby został na 1. posiedzeniu Sejmu dopełniony. A więc zarządzam przerwę w posiedzeniu Sejmu.",
                },
            ],
        )
        self.assertEqual(obj["session_not_delivered_speeches"], [])
