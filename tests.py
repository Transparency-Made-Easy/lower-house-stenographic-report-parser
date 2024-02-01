import os
import unittest
from src.custom_json import obj2pretty_json
from src.lib import report_to_obj


class TestReportToObj(unittest.TestCase):
    def test_01_a(self):
        file_path = os.path.join("files", "01_a_ksiazka.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-13T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "12:07:00")
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
            obj["text"],
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

    def test_01_b(self):
        file_path = os.path.join("files", "01_b_ksiazka.pdf")
        obj = report_to_obj(file_path)
        print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-14T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "16:33:00")
        self.assertEqual(obj["speaker_senior"], None)
        self.assertEqual(obj["speaker"], "Szymon Hołownia")
        self.assertEqual(obj["vicespeakers"], [])
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
                    "name": "Punkt 4. porządku dziennego: Wybór sekretarzy Sejmu",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 5. porządku dziennego: Wybór składu osobowego Komisji Regulaminowej, Spraw Poselskich i Immunitetowych",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 6. porządku dziennego: Pierwsze czytanie przedstawionego przez Prezydium Sejmu projektu uchwały w sprawie ustalenia liczby członków Komisji do Spraw Służb Specjalnych",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
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
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {"type": "BREAK"},
            ],
        )
        self.assertEqual(
            obj["text"],
            [
                {
                    "speaker": "Marszałek",
                    "content": "Wznawiam posiedzenie. (Zebrani wstają) Wysoka Izbo! W dniu 12 listopada br. zmarła Hanna Gucwińska, znana i ceniona przez miliony Polaków posłanka na Sejm IV kadencji. Uczcijmy jej pamięć minutą ciszy. (Chwila ciszy) (Poseł Robert Telus: Wieczny odpoczynek racz jej dać, Panie…) (Posłowie: A światłość wiekuista niechaj jej świeci…) (Poseł Robert Telus: Niech odpoczywa w pokoju wiecznym…) (Posłowie: Amen.) Dziękuję państwu bardzo. Szanowni Państwo! Na wstępie przepraszam za to opóźnienie w rozpoczęciu obrad, ale o godz. 16 mieliśmy jeszcze 130 posłów, którzy nie odebrali legitymacji poselskich, i musieliśmy poczekać, aby każdy mógł wziąć udział w tych głosowaniach. Prezydium Sejmu przedłożyło wnioski w sprawie: — wyboru sekretarzy Sejmu, druk nr 9, — wyboru składu osobowego Komisji Regulaminowej, Spraw Poselskich i Immunitetowych, druk nr 11. W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o punkty obejmujące rozpatrzenie tych wniosków. Prezydium Sejmu przedłożyło projekt uchwały w sprawie ustalenia liczby członków Komisji do Spraw Służb Specjalnych, druk nr 10. W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o punkt obejmujący rozpatrzenie tego projektu. Proponuję, aby w tym przypadku Sejm wyraził zgodę na zastosowanie art. 51 pkt 1 regulaminu Sejmu. Jeżeli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycję przyjął. Sprzeciwu nie słyszę. Grupy posłów przedłożyły wnioski w sprawie wyboru posłów-członków Krajowej Rady Sądownictwa, druki nr 12–19. W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o punkt obejmujący rozpatrzenie tych wniosków. Proponuję, aby w tych przypadkach Sejm wyraził zgodę na skrócenie terminu, o którym mowa w art. 30 ust. 4 regulaminu Sejmu, oraz rozpatrzył wnioski bez przesyłania ich do właściwej komisji. Jeśli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycje przyjął. Sprzeciwu nie słyszę. Przystępujemy do rozpatrzenia punktu 4. porządku dziennego: Wybór sekretarzy Sejmu (druk nr 9). Prezydium Sejmu na podstawie art. 6 ust. 2 regulaminu Sejmu przedstawiło wniosek w sprawie wyboru sekretarzy Sejmu. Przypominam, że zgodnie z art. 6 regulaminu Sejmu Sejm wybiera 20 sekretarzy w głosowaniu łącznym. Czy ktoś z pań i panów posłów chce zabrać głos w sprawie zgłoszonych kandydatur? Nikt się nie zgłasza. Przystępujemy do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku z druku nr 9, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 457 posłów. Za – 457, przeciw nie głosował nikt, nikt się nie wstrzymał. Stwierdzam, że Sejm podjął uchwałę w sprawie wyboru sekretarzy Sejmu. Przystępujemy do rozpatrzenia punktu 5. porządku dziennego: Wybór składu osobowego Komisji Regulaminowej, Spraw Poselskich i Immunitetowych (druk nr 11). Prezydium Sejmu, po zasięgnięciu opinii Konwentu Seniorów, na podstawie art. 20 ust. 1 regulaminu Sejmu przedstawiło wniosek w sprawie wyboru składu osobowego Komisji Regulaminowej, Spraw Poselskich i Immunitetowych. Czy ktoś z pań i panów posłów chce zabrać głos w sprawie zgłoszonych kandydatur? (Wznowienie posiedzenia o godz. 16 min 33) Nikt się nie zgłasza. Przystępujemy zatem do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku w brzmieniu z druku nr 11, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 458 posłów. Za – 458, nikt nie był przeciw, nikt się nie wstrzymał. Stwierdzam, że Sejm podjął uchwałę w sprawie wyboru składu osobowego Komisji Regulaminowej, Spraw Poselskich i Immunitetowych. Zgodnie z art. 20 ust. 2 regulaminu Sejmu zwołuję pierwsze posiedzenie Komisji Regulaminowej, Spraw Poselskich i Immunitetowych w sali nr 13 w budynku G – 15 minut po zakończeniu głosowań. Przystępujemy do rozpatrzenia punktu 6. porządku dziennego: Pierwsze czytanie przedstawionego przez Prezydium Sejmu projektu uchwały w sprawie ustalenia liczby członków Komisji do Spraw Służb Specjalnych (druk nr 10). Zgodnie z art. 137 ust. 1 regulaminu Sejmu w skład Komisji do Spraw Służb Specjalnych wchodzi nie więcej niż siedmiu posłów. Sejm, na wniosek Prezydium Sejmu, w drodze uchwały ustala liczbę członków Komisji do Spraw Służb Specjalnych. Prezydium Sejmu, po zasięgnięciu opinii Konwentu Seniorów, proponuje, aby Sejm ustalił liczbę członków tej komisji na siedmiu. Czy ktoś z pań i panów posłów pragnie zabrać głos w pierwszym czytaniu projektu tej uchwały? Nikt się nie zgłasza. Proponuję, aby Sejm przystąpił niezwłocznie do drugiego czytania projektu tej uchwały. Jeśli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycję przyjął. Sprzeciwu nie słyszę. Przystępujemy więc do drugiego czytania projektu uchwały. Czy ktoś z pań i panów posłów pragnie zabrać głos w drugim czytaniu projektu uchwały? Nikt się nie zgłasza. Przystępujemy więc do głosowania nad całością projektu uchwały. Kto z pań i panów posłów jest za przyjęciem w całości projektu uchwały w brzmieniu z druku nr 10, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 458 posłów. Za – 458, nikt nie był przeciw, nikt się nie wstrzymał. Stwierdzam, że Sejm podjął uchwałę w sprawie ustalenia liczby członków Komisji do Spraw Służb Specjalnych. Przystępujemy do rozpatrzenia punktu 7. porządku dziennego: Wybór posłów-członków Krajowej Rady Sądownictwa (druki nr 12, 13, 14, 15, 16, 17, 18 i 19). Wysoka Izbo! Zgodnie z art. 187 ust. 1 pkt 3 Konstytucji Rzeczypospolitej Polskiej Krajowa Rada Sądownictwa składa się m.in. z czterech członków wybieranych przez Sejm spośród posłów. Kadencja posłów-członków Rady zgodnie z art. 187 ust. 3 Konstytucji Rzeczypospolitej Polskiej oraz art. 9 ust. 1 ustawy o Krajowej Radzie Sądownictwa trwa 4 lata. Wnioski w sprawie kandydatów na członków Krajowej Rady Sądownictwa zostały paniom i panom posłom doręczone odpowiednio w drukach nr 12, 13, 14, 15, 16, 17, 18 i 19. Proszę teraz o zabranie głosu panią poseł Annę Milczanowską w celu przedstawienia kandydatur: pana posła Arkadiusz Mularczyka, pana posła Kazimierza Smolińskiego, pana posła Bartosza Kownackiego, pana posła Marka Asta, zgłoszonych przez grupę posłów z Klubu Parlamentarnego Prawo i Sprawiedliwość. Bardzo proszę, pani poseł.",
                },
                {
                    "speaker": "Poseł Anna Milczanowska",
                    "content": "Panie Marszałku! Wysoka Izbo! Mam zaszczyt przedstawić dane o kandydatach do Krajowej Rady Sądownictwa. Zacznę, tak jak pan marszałek wyczytywał, od pana posła Arkadiusza Mularczyka. Urodził się 4 lutego 1971 r. w Raciborzu. Jest adwokatem i parlamentarzystą sprawującym mandat posła V, VI, VII, VIII, IX i X kadencji Sejmu Rzeczypospolitej Polskiej. W 1996 r. ukończył studia na Wydziale Prawa i Administracji Uniwersytetu Jagiellońskiego w Krakowie. Po studiach pracował m.in. w Biurze Legislacyjnym Kancelarii Senatu. W 1999 r. zdał przed komisją Ministerstwa Skarbu Państwa egzamin na członków rad nadzorczych. W 2000 r. ukończył podyplomowe studia w Helsińskiej Fundacji Praw Człowieka w Warszawie – prawa i wolności człowieka. W latach 1997–2001 odbył aplikację adwokacką w Okręgowej Radzie Adwokackiej w Krakowie, a w 2001 r. zdał egzamin adwokacki. W 2005 r. wykonywał zawód adwokata w Nowym Sączu. Był wpisany na listę kandydatów na syndyków prezesa Sądu Okręgowego w Nowym Sączu. Od 2005 r. jest posłem na Sejm Rzeczypospolitej Polskiej. W trakcie swojej osiemnastoletniej służby parlamentarnej pracował jako przewodniczący lub wiceprzewodniczący wielu sejmowych komisji: Sprawiedliwości i Praw Człowieka, Ustawodawczej, Odpowiedzialności Konstytucyjnej, Spraw Zagranicznych, Komisji Nadzwyczajnej do spraw zmian w kodyfikacjach i w wielu podkomisjach, w tym w podkomisji do spraw Trybunału Konstytucyjnego. Pracował także w komisji śledczej ds. nielegalnego wywierania wpływu na funkcjonariuszy służb specjalnych i wymiaru sprawiedliwości. W imieniu Sejmu Rzeczypospolitej Polskiej wielokrotnie występował przed Trybunałem Konstytucyjnym. 1. posiedzenie Sejmu w dniu 14 listopada 2023 r. Punkty 5. i 6. porządku dziennego – głosowanie. W 2011 r. został powołany na członka delegacji Sejmu i Senatu do Zgromadzenia Parlamentarnego Rady Europy w Strasburgu. Był członkiem Komisji Prawnej oraz wiceprzewodniczącym Komisji ds. wyboru sędziów Europejskiego Trybunału Praw Człowieka. 22 listopada 2019 r. został wybrany przez Sejm w skład Krajowej Rady Sądownictwa. W październiku 2020 r. został wybrany przez KRS na stanowisko jej wiceprzewodniczącego. W tym samym roku objął też funkcję wiceprzewodniczącego delegacji polskiego parlamentu do Zgromadzenia Parlamentarnego Rady Europy, a w 2021 r. został wiceprzewodniczącym Zgromadzenia Parlamentarnego Rady Europy. Jest autorem skarg konstytucyjnych do Trybunału Konstytucyjnego, m.in. o zbadanie uprawnień Trybunału Sprawiedliwości Unii Europejskiej do kontroli prawa krajowego i stosowania środków tymczasowych czy też skargi o zbadanie zgodności z konstytucją przepisów Kodeksu postępowania cywilnego, z których wywodzi się zasadę immunitetu jurysdykcyjnego obcych państw w sprawach o odszkodowania z tytułu zbrodni wojennych, ludobójstwa czy zbrodni przeciwko ludzkości. Reprezentuje Sejm Rzeczypospolitej Polskiej w szeregu postępowań przed Trybunałem Konstytucyjnym. W październiku 2022 r. został powołany na stanowisko sekretarza stanu ds. polityki europejskiej w Ministerstwie Spraw Zagranicznych. Przewodniczący Parlamentarnego Zespołu ds. Oszacowania Wysokości Odszkodowań Należnych Polsce od Niemiec za Szkody Wyrządzone w trakcie II Wojny Światowej. Współautor raportu o stratach wojennych Polski zadanych przez agresję i okupację niemiecką podczas II wojny światowej. Pełni także funkcję przewodniczącego Rady Instytutu Strat Wojennych im. Jana Karskiego oraz od 2022 r. – pełnomocnika rządu ds. odszkodowań za szkody wyrządzone agresją i okupacją niemiecką w latach 1939–1945. Zarówno wykształcenie prawnicze i praktyka adwokacka, jak i bogate doświadczenie parlamentarne i międzynarodowe pana posła Arkadiusza Mularczyka uzasadniają przedstawienie jego kandydatury na przedstawiciela Sejmu Rzeczpospolitej Polskiej w Krajowej Radzie Sądownictwa. Pan Marek Ast urodził się 27 września 1958 r. w Zielonej Górze. Maturę zdał w roku 1977 w Liceum Ogólnokształcącym nr 7 w Zielonej Górze. W 1984 r. ukończył studia na Wydziale Prawa i Administracji na Uniwersytecie Wrocławskim. W latach 1987–1990 odbył aplikację radcowską w Okręgowej Izbie Radców Prawnych w Zielonej Górze. W latach 1984–1989 pracował jako wychowawca i nauczyciel, najpierw w Państwowym Domu Dziecka, a następnie w Zespole Szkół Zawodowych we Wschowie. Od 1990 r. jako radca prawny obsługiwał podmioty gospodarcze i jednostki samorządowe w województwie leszczyńskim. W latach 1991–2006 pełnił funkcję burmistrza miasta i gminy Szlichtyngowa, a w kadencji 1998– 2002 był radnym wojewódzkim w Sejmiku Województwa Lubuskiego. W 2006 r. objął urząd wojewody lubuskiego i w tym samym roku mandat posła na Sejm V kadencji. Poseł V, VI, VII, VIII, IX i X kadencji Sejmu. W parlamencie pracował w Komisji Sprawiedliwości i Praw Człowieka, Komisji Nadzwyczajnej do spraw zmian w kodyfikacjach, Komisji Mniejszości Narodowych i Etnicznych i Komisji Ustawodawczej. W tych dwóch ostatnich pełnił funkcję przewodniczącego komisji. W poprzedniej kadencji Sejmu został wybrany na przewodniczącego Komisji Sprawiedliwości i Praw Człowieka. 22 listopada 2019 r. wybrany przez Sejm na członka Krajowej Rady Sądownictwa. Jako poseł wielokrotnie reprezentował wnioskodawców i Sejm Rzeczypospolitej Polskiej przed Trybunałem Konstytucyjnym. W roku 2000 został odznaczony Złotym Krzyżem Zasługi. Zarówno wykształcenie i praktyka radcowska, jak i bogate doświadczenie zawodowe pana posła Marka Asta uzasadniają przedstawienie jego kandydatury na przedstawiciela Sejmu Rzeczypospolitej w Krajowej Radzie Sądownictwa. Pan Kazimierz Smoliński urodził się 15 lipca 1955 r. w Malborku. Jest żonaty, ma dwóch synów. W latach 1974–1978 studiował na Wydziale Prawa i Administracji Uniwersytetu Gdańskiego i uzyskał tytuł magistra prawa. W 1984 r. ukończył studia podyplomowe radców prawnych na Uniwersytecie im. Adama Mickiewicza w Poznaniu, a w 2001 r. studia podyplomowe na Uniwersytecie Gdańskim z zarządzania przedsiębiorstwem. Uprawnienia zawodowe radcy prawnego zdobył w 1983 r. po odbyciu aplikacji radcowskiej w Okręgowej Izbie Radców Prawnych w Gdańsku. W 1986 r. uzyskał wpis na listę adwokatów w Okręgowej Radzie Adwokackiej w Gdańsku. Pracę zawodową rozpoczął w 1978 r. w Państwowym Zakładzie Ubezpieczeń, gdzie pracował od 1983 r. jako radca prawny. W 1993 r. założył własną kancelarię prawną w Tczewie, w której wykonywał zawód radcy prawnego, a następnie adwokata do roku 2015. W latach 2015–2018 pełnił obowiązki sekretarza stanu w Ministerstwie Infrastruktury i Budownictwa. Zajmował stanowiska kierownicze w gospodarce, był m.in. prezesem Zarządu Stoczni Gdynia w Gdyni. Pełnił obowiązki członka rady nadzorczej w latach 2000–2002 jako sekretarz Rady Nadzorczej Zakładu Energetyki Cieplnej w Tczewie. W latach 2004–2006 był członkiem rady pomorskiego oddziału NFZ w Gdańsku. Działalnością społeczną zajmuje się od wielu lat, m.in. w latach 1993–1996 w Regionalnej Izbie Gospodarczej w Tczewie był wiceprezesem zarządu, a w latach 1996–2002 w Pomorskiej Izbie Przemysłowo-Handlowej w Gdańsku był przewodniczącym Sądu Organizacyjnego. Ponadto działa w Klubie Inteligencji Katolickiej w Gdańsku oraz w Instytucie Gospodarki Narodowej w Warszawie. Działał też w samorządzie gminnym w Radzie Miejskiej w Tczewie, gdzie w latach 1998–2002 był przewodniczącym tej rady, a w latach 2006–2010 był jej członkiem. Kazimierz Smoliński był posłem na Sejm VI, VII, VIII, IX i jest posłem X kadencji. Pełnił funkcję wiceprzewodniczącego Komisji Odpowiedzialności Konstytucyjnej, przewodniczącego Komisji Regulaminowej, Spraw Poselskich i Immunitetowych, a także członka Komisji Sprawiedliwości i Praw Człowieka oraz Komisji Finansów Publicznych. To członek Krajowej Rady Sądownictwa od roku 2019. Zarówno wykształcenie i praktyka radcowska, jak i bogate doświadczenie zawodowe pana posła Kazimierza Smolińskiego uzasadniają przedstawienie jego kandydatury na przedstawiciela Sejmu Rzeczypospolitej Polskiej w Krajowej Radzie Sądownictwa. Pan Bartosz Kownacki urodził się 11 sierpnia 1979 r. w Warszawie. Był współpracownikiem byłego premiera śp. Jana Olszewskiego i pracownikiem Koła Poselskiego Ruchu Odbudowy Polski. W roku 2003 z wyróżnieniem ukończył studia na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego. Pracował jako wykładowca w Wyższej Szkole Mazowieckiej. W latach 2003–2006 odbywał aplikację prokuratorską, a po zdanych egzaminach uzyskał wpis na listę radców prawnych. Następnie pracował m.in. jako dyrektor Biura Prawnego Służby Kontrwywiadu Wojskowego oraz radca prawny w Kancelarii Prezydenta Rzeczypospolitej Polskiej, pana prof. Lecha Kaczyńskiego. W roku 2009 rozpoczął praktykę adwokacką. Reprezentował m.in. pana Jarosława Kaczyńskiego, Zbigniewa Ziobrę, a po katastrofie smoleńskiej niektóre rodziny ofiar. W 2011 r. po raz pierwszy uzyskał manat posła na Sejm Rzeczypospolitej Polskiej. Po reelekcji w 2015 r. został powołany na funkcję sekretarza stanu w Ministerstwie Obrony Narodowej, którą pełnił do 2018 r. W 2023 r. po raz czwarty został wybrany na posła Sejmu Rzeczypospolitej Polskiej. Odznaczony został przez prezydenta Rzeczypospolitej Polskiej Lecha Kaczyńskiego Złotym Krzyżem Zasługi. Zarówno wykształcenie i praktyka adwokacka, jak i bogate doświadczenie zawodowe pana posła Bartosza Kownackiego uzasadniają przedstawienie jego kandydatury na przedstawiciela Sejmu Rzeczypospolitej Polskiej w Krajowej Radzie Sądownictwa. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, pani poseł. Proszę teraz o zabranie głosu pana posła Borysa Budkę w celu przedstawienia kandydatur pana posła Roberta Kropiwnickiego i pani poseł Kamili Gasiuk-Pihowicz, zgłoszonych przez grupę posłów z Klubu Parlamentarnego Koalicja Obywatelska – Platforma Obywatelska, Nowoczesna, Inicjatywa Polska, Zieloni.",
                },
                {
                    "speaker": "Poseł Borys Budka",
                    "content": "Dziękuję, panie marszałku. Wysoka Izbo! W imieniu klubu Koalicji Obywatelskiej chciałbym zgłosić dwie kandydatury do Krajowej Rady Sądownictwa, przypominając jednocześnie, że zgodnie z art. 187 ust. 1 pkt 3 Konstytucji Rzeczypospolitej to Sejm wybiera czterech przedstawicieli w tym konstytucyjnym gremium, natomiast Sejm zeszłej kadencji dopuścił się w tym zakresie poważnego naruszenia konstytucji, wybierając ponad to wskazanie 15 członków Krajowej Rady Sądownictwa, czym w oczywisty sposób przekroczył swoje uprawnienia i spowodował, że dzisiejszy skład Krajowej Rady Sądownictwa w części dotyczącej tych 15 sędziów wybranych przez Sejm jest w sposób oczywisty sprzeczny z konstytucją, co skutkuje nieważnością przeprowadzanych przez ten organ nominacji sędziowskich. (Oklaski) Szanowni Państwo! Wracam do kandydatur, które chciałbym przedstawić. Po pierwsze, pani poseł Kamila Gasiuk-Pihowicz. To absolwentka Wydziału Prawa i Administracji Uniwersytetu im. Kardynała Stefana Wyszyńskiego. Jest magistrem prawa, jest również adwokatem. Egzamin adwokacki zdała w 2011 r. Jednocześnie pani poseł Gasiuk-Pihowicz posiada wykształcenie wyższe zdobyte w zakresie finansów i bankowości w Szkole Głównej Handlowej. Była pracownikiem Biura Rzecznika Praw Obywatelskich. Odbyła, jak już wspomniałem, aplikację adwokacką. W 2015 r. uzyskała mandat poselski. Potwierdziła ten mandat w 2019 r. i w wyborach 15 października 2023 r., uzyskując rekordowo duże poparcie w swoim okręgu wyborczym. Zarówno doświadczenie parlamentarne, jak i przede wszystkim zdobyta wiedza, umiejętności, kwalifikacje zawodowe potwierdzone egzaminem adwokackim z całą pewnością sprawiają, że ta kandydatka jest odpowiednia do zasiadania w tym gremium. W dodatku pani poseł Gasiuk-Pihowicz od samego początku zasiada w Komisji Sprawiedliwości i Praw Człowieka. Jest osobą, która wielokrotnie z mównicy sejmowej, a także podczas posiedzeń komisji walczyła o zachowanie konstytucyjnych standardów, sprzeciwiając się od samego początku zasiadania w tym parlamencie rażącemu łamaniu prawa przez większość parlamentarną, jeżeli chodzi o kwestie związane chociażby z wymiarem sprawiedliwości czy Trybunałem Konstytucyjnym. Szanowni Państwo! Druga z kandydatur to kandydatura pana posła Roberta Kropiwnickiego, doktora nauk prawnych. To absolwent Wydziału Prawa, Administracji i Ekonomii Uniwersytetu Wrocławskiego, samorządowiec. Pełnił również funkcje mediatora sądowego przy Sądzie Rejonowym w Legnicy. Dodatkowo działa w organizacjach pozarządowych z terenu Dolnego Śląska. Poseł na Sejm VI, VII, VIII, IX i X kadencji. Był członkiem Komisji Nadzwyczajnej do rozpatrzenia projektu uchwały w zakresie zmiany Regulaminu Sejmu, Komisji Odpowiedzialności Konstytucyjnej, Komisji Sprawiedliwości i Praw Człowieka, Komisji Ustawodawczej i Komisji Nadzwyczajnej do spraw zmian w kodyfikacjach. Jest w oczywisty sposób doskonale przygotowany do pełnienia tej roli. Tak jak wspomniałem na początku mojego wystąpienia, dzisiaj rozpoczynamy proces uzdrowienia konstytucyjnego organu, jakim jest Krajowa Rada Sądownictwa. Dzisiaj Sejm Rzeczypospolitej Polskiej zgodnie z konstytucją wybierze czworo przedstawicieli w tym gremium. Natomiast kolejnym krokiem, niezbędnym do tego, by przywrócić konstytucyjną funkcję tego organu, jest oczywiście usunięcie wadliwości składu, który tam zasiada. Bo przypomnę, że Sejm zarówno w poprzedniej kadencji, jak i jeszcze wcześniej dopuścił się rażącego naruszenia konstytucji, formując ten organ w sposób rażąco sprzeczny z konstytucją. Szanowni Państwo! Krajowa Rada Sądownictwa ma stać na straży niezawisłości sędziowskiej i niezależności sądów. Niestety Krajowa Rada Sądownictwa w obecnym składzie stała się przybudówką na szczęście ustępującego już rządu. Zamiast stać na straży niezawisłości sędziowskiej, stała się trampoliną do karier ludzi, którzy zhańbili togę sędziowską, którzy zhańbili noszone godło Rzeczypospolitej. (Głos z sali: Do rzeczy.) Krajowa Rada Sądownictwa ukształtowana w poprzednich kadencjach stała się niestety miejscem, w którym mierni, bierni, ale wierni władzy zdobywali kolejne szczeble w sędziowskich karierach. (Oklaski) (Głos z sali: Brawo!) (Poseł Anita Czerwińska: Nie kłam!) (Poseł Marek Suski: Kłamca!) Cała Polska była świadkiem, kiedy pod dyktando polityka członkowie tej rady zmieniali sposób głosowania, kiedy obserwowaliśmy bulwersujące sceny, kiedy politycy wracali po nieobecności do tego organu i wskazywali, w jaki sposób sędziowie mają głosować. (Poseł Anita Czerwińska: To ma być prezentacja?) Polska potrzebuje niezależnego wymiaru sprawiedliwości. Krajowa Rada Sądownictwa stała się jednym z elementów, który sprawił, że poprzednia większość parlamentarna zablokowała Polakom dostęp do środków z Funduszu Odbudowy. (Głos z sali: Wy zablokowaliście.) Szanowni Państwo! Dzisiaj rozpoczynamy proces sanacji tych organów, które zostały skażone przez poprzednią władzę. (Oklaski) Dzisiaj jest ten czas, żeby powiedzieć: dosyć, dosyć psucia państwa, dosyć zawłaszczania konstytucyjnych organów, ale przede wszystkim dosyć wprowadzania standardów, z których byliby dumni wasi wschodni przyjaciele. Zrobiliście z wymiarem sprawiedliwości rzecz niedopuszczalną. Staliście się niestety jednymi z autorów największej destrukcji, jeżeli chodzi o to, co stało się w Rzeczypospolitej po 1989 r. Krajowa Rada Sądownictwa to organ, który powinien pilnować, żeby sądy Rzeczypospolitej były miejscem, w którym jest przestrzegane prawo, w którym politycy nie piszą wyroków sądowych, w którym politycy nie zmieniają na usłużnych funkcyjnych sędziów, prezesów i wiceprezesów. Ale przede wszystkim krajowa rada… (Głos z sali: Panie marszałku, miał przedstawić kandydatów. Konstytucjonalista rozwala cały system. To nie jest dyskusja na ten temat.) (Poseł Anita Czerwińska: Kto prowadzi obrady?)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Pan poseł Budka przedstawia kandydatury i motywacje, które stoją za… (Poruszenie na sali) (Część posłów uderza w pulpity) Proszę państwa o spokój… (Gwar na sali) Proszę państwa o spokój. (Gwar na sali) Proszę państwa o spokój raz jeszcze. Za chwilę będzie możliwość zabrania głosu w dyskusji. I mam nadzieję, że państwo z tej możliwości skorzystają. (Poseł Barbara Bartuś: To ma być przedstawienie kandydatury.) W tej chwili ze swojej możliwości wypowiedzi korzysta pan poseł Budka, którego proszę też o zbliżanie się do końca wypowiedzi. (Oklaski) (Głos z sali: Kompromitacja.)",
                },
                {
                    "speaker": "Poseł Borys Budka",
                    "content": "Bardzo dziękuję. Panie Marszałku! Wysoka Izbo! W Krajowej Radzie Sądownictwa są potrzebni ludzie, którzy znają polską konstytucję, którzy wiedzą, czym jest art. 10 konstytucji, art. 173 konstytucji, zasada trójpodziału władzy, niezależności władzy sędziowskiej, którzy wiedzą, jaka jest rola Krajowej Rady Sądownictwa. Niestety Krajowa Rada Sądownictwa w dzisiejszym składzie nie spełnia tych europejskich i światowych standardów. (Głos z sali: Nie kłam!) Rozumiem to podenerwowanie tej strony sceny politycznej, ale musicie państwo zrozumieć, że rozpoczął się czas uzdrowienia polskiego ustroju. (Oklaski) Musicie państwo zrozumieć, że Krajowa Rada Sądownictwa znowu stanie się organem, który zgodnie z konstytucją będzie stał na straży niezawisłości sędziowskiej i niezależności wymiaru sprawiedliwości. (Poseł Barbara Bartuś: I ona właśnie stoi.) Szanowni Państwo! Jeżeli chcecie poznać uzasadnienie tych kandydatur, to ono jest bardzo proste. Dzisiaj potrzebujemy ludzi, którzy wiedzą, że wymiar sprawiedliwości jest od kontrolowania władzy, a nie od tego, by władza kontrolowała wymiar sprawiedliwości. (Oklaski) Krajowa Rada Sądownictwa to miejsce dla ludzi, którzy idą tam po to, by realizować tę konstytucyjną zasadę, a nie po to, by zajmować się awansami dla swoich. (Oklaski) Szanowni Państwo! Takim symbolem tego, co działo się w Krajowej Radzie Sądownictwa, jest ścieżka kariery osób, które tam się znalazły. To stało się trampoliną dla swoich… (Głos z sali: Nie na temat.) …to stało się miejscem, gdzie bierni, mierni, ale wierni… (Poseł Barbara Bartuś: O kim pan mówi, panie Budka? Ale czy to jest przedstawienie kandydatur? Kogo pan przedstawia, panie pośle Budka? Kogo pan przedstawia?) …awansowali, pięli się na kolejne szczeble, to stało się miejscem, w którym ludzie byli wskazywani przez partię rządzącą. Dlatego tak ważne jest, by Krajowa Rada Sądownictwa odzyskała przede wszystkim zaufanie obywateli, żeby przede wszystkim znalazły się tam osoby, które to rozumieją. I możecie państwo pokrzykiwać, możecie państwo się burzyć… (Poseł Barbara Bartuś: Ale pan ma przedstawić kandydaturę.) …ale 15 października 2023 r. skończył się w Polsce czas bezprawia i niesprawiedliwości. (Oklaski) (Poseł Barbara Bartuś: Zaczyna się terror.) Dziś mamy do czynienia z normalnymi standardami państwa prawa, w przeciwieństwie do tego, co działo się przez ostatnich 8 lat. (Poseł Barbara Bartuś: Panie marszałku, pan przewodniczący ma przedstawić kandydaturę. Co to jest?) Szanowni Państwo! Dzisiaj trzeba jasno powiedzieć: to uzdrawianie wymiaru sprawiedliwości rozpoczyna się dzisiaj, ale przed nami… (Poseł Barbara Bartuś: Nie mamy debaty, tylko przedstawienie kandydatury.) …dosyć trudna, wyboista, ale finalnie bardzo szczęśliwa droga. Otóż tak jak zainfekowaliście Krajową Radę Sądownictwa, zainfekowaliście Trybunał Konstytucyjny, tak niestety musicie się liczyć z tym, że ci, którzy rozumieją standardy państwa prawa, będą po kolei te wszystkie elementy, które są dzisiaj zainfekowane, w sposób zgodny z prawem, zgodny z konstytucją, krok po kroku czyścić. Szanowni Państwo! Możecie sobie krzyczeć, możecie sobie zachowywać się, jak się zachowujecie, ale musicie zrozumieć podstawową rzecz. Naprawdę czas bezprawia skończył się nieodwołalnie i dzisiaj ten wybór rozpoczyna czas naprawy. (Oklaski) Dlatego, szanowni państwo, klub Koalicji Obywatelskiej zgłasza te kandydatury, jednocześnie przedstawiając dalsze kroki, które będą towarzyszyć uzdrowieniu tych konstytucyjnych organów. Mam nadzieję, że gdy przez to wszystko wspólnie przejdziemy, zrozumiecie państwo, jak bardzo się myliliście, zrozumiecie państwo, na czym polega państwo prawa, zrozumiecie państwo, na czym polega sprawiedliwość. Wreszcie zrozumiecie państwo, że w demokratycznym państwie prawnym to sądy są od tego, by kontrolować władzę. Naprawdę możecie być państwo spokojni. A myślę – powiem tak na zakończenie, patrząc państwu prosto w oczy – że dzisiaj nikt tak bardzo nie potrzebuje niezależnego wymiaru sprawiedliwości jak wy, drodzy państwo, naprawdę. (Oklaski) (Głos z sali: Ha, ha, ha!) Nikt tak dzisiaj nie potrzebuje niezawisłych sędziów jak państwo, jak ta strona sceny politycznej, bo przecież będziecie państwo rozliczani z tego, co zrobiliście… (Część posłów skanduje: Giertych! Giertych! Giertych!) …i to w waszym interesie jest to, żebyście państwo stawali przed niezależnymi sądami i niezawisłymi sędziami. Krajowa Rada Sądownictwa w nowym kształcie z pewnością będzie gwarantem tego, że procesy w Polsce będą prawe i sprawiedliwe. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję panu posłowi. Proszę o zabranie głosu pana posła Krzysztofa Śmiszka w celu przedstawienia kandydatury pani poseł Anny Marii Żukowskiej. (Minister Sprawiedliwości Zbigniew Ziobro: Panie marszałku…) (Głos z sali: Zejdź!) (Głos z sali: Siadaj!) (Głos z sali: W jakim trybie?) Przepraszam, panie ministrze, są zgłoszeni członkowie rządu do wystąpienia po wystąpieniach klubowych. Udzielę wtedy też panu głosu. Zgodnie z regulaminem Sejmu udzielę głosu panu Schreiberowi, panu Szynkowskiemu vel Sękowi i panu. Chce pan wystąpić teraz? (Minister Sprawiedliwości Zbigniew Ziobro: Teraz.) W tej chwili? (Minister Sprawiedliwości Zbigniew Ziobro: Tak.) (Głosy z sali: Nie, nie.) Drodzy państwo, regulamin Sejmu niestety nie pozostawia w tym względzie ruchu. Jest w nim wyraźnie napisane w art. 186, że… (Gwar na sali) Proszę o ciszę, dobrze? Proszę państwa o ciszę. …marszałek Sejmu udziela głosu członkom Rady Ministrów, prezesowi… Proszę o ciszę! (Poruszenie na sali) (Głosy z sali: Ooo…) …Najwyższej Izby Kontroli, szefowi Kancelarii Prezydenta oraz sekretarzowi stanu w Kancelarii Prezydenta na danym posiedzeniu, poza kolejnością mówców zapisanych do głosu, ilekroć tego zażądają. Jesteśmy w Izbie, która szanuje zasady, na które się umówiła, a ja poproszę tylko pana ministra, żeby to wystąpienie było objęte tym limitem czasu… (Głos z sali: Nie ma limitu.) …na który umówimy się w czasie wystąpień klubowych, a więc 3 minut, bo w takim trybie wszyscy mówcy dzisiaj w dyskusji będą przemawiać. Dziękuję bardzo. (Poseł Krzysztof Śmiszek: Ale w jakim trybie? Pan minister jest ministrem?) Pan minister jest ministrem. (Poseł Krzysztof Śmiszek: No to mamy inne zdanie.)",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Szanowny Panie Marszałku! Na wstępie chciałem podziękować, że zechciał pan dochować lojalności wobec regulaminu Sejmu, który reguluje zasady pracy Wysokiej Izby. Mam nadzieję, że tak będzie i w przyszłości, bo wczoraj mieliśmy okazję przekonać się, że to, co jest piękną tradycją Wysokiej Izby, zostało w sposób brutalny i haniebny złamane (Oklaski) poprzez odmowę największemu klubowi udziału w Prezydium Sejmu, Prezydium Senatu jeszcze. Pazerność Platformy Obywatelskiej nie zna granic, ale bezczelność i buta jeszcze bardziej. Otóż, szanowny panie Budka, chciałem panu przypomnieć, że to Trybunał Konstytucyjny decyduje o tym, czy w tym wypadku ustawa jest zgodna z konstytucją, czy też nie, a nie Borys Budka. (Oklaski) To po pierwsze. Po drugie, panie Budka… (Głos z sali: Panie pośle!) …to konstytucja, ta konstytucja, którą tak chętnie pan i pana koleżanki i koledzy na KOD-owskich manifestacjach, gdzie te piękne słowa, rodem z najpiękniejszej polskiej literatury, często padają… Tak często machacie tam tymi konstytucjami. W tych konstytucjach, w tych książeczkach, książkach, w tych zapisach jest też norma prawna, która mówi, że dopóki ustawa nie została zakwestionowana przez Trybunał Konstytucyjny, a nie przez pana Borysa Budkę, jest obowiązującym w Polsce prawem. (Oklaski) (Głos z sali: Brawo!) A więc jeśli pan mówi o prawie i o praworządności, to niech pan będzie konsekwentny. (Część posłów skanduje: Konstytucja! Konstytucja! Konstytucja!) Konstytucja! Konstytucja! A po trzecie, jako że doprowadza pan Wysoką Izbę, a przy okazji wszystkich oglądających nas do wniosków, które są sprzeczne z literą konstytucji, to pozwolę sobie ją wprost zacytować, by pokazać pana manipulacje i manipulację, która kryje się za tymi inicjatywami, które padły tu przed chwilą sygnalizacyjnie, a co do których ufam, że nie dojdą do skutku… (Głos z sali: Pistolet masz?) …bo to byłoby rażącym złamaniem prawa i czystym kryminałem. I przestrzegam: Po nocy jest dzień. (Poseł Urszula Sara Zielińska: Właśnie nastał dzień.) Przyjdzie czas, że wy też znajdziecie się w ławach opozycji, a wtedy będziecie rozliczani również za łamanie konstytucji… (Głos z sali: Będziesz siedział.) …ale też i za możliwe przestępstwa kryminalne, które z tym są związane. Niech pan nie będzie taki pewny siebie, czas biegnie szybko. Więc… (Oklaski) (Część posłów skanduje: Będziesz siedział! Będziesz siedział! Będziesz siedział!) Liczę na was! Mam nadzieję, że nie okażecie się takimi fujarami jak za czasów Trybunału Stanu. Otóż pozwólcie, że zacytuję. (Głos z sali: Czas!) Nie bójcie się słów konstytucji, które będę tu przytaczał. Tak bardzo lubiliście powoływać się na ten akt prawny. Zacytuję. Otóż art. 187 konstytucji…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie ministrze, czas pana wypowiedzi minął. (Poseł Barbara Bartuś: Nie ma limitu czasu.)",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "…mówi, że Krajowa Rada…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie ministrze, czas pana wypowiedzi minął.",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Panie marszałku, kończę już…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Proszę bardzo, ma pan 10 sekund. (Poruszenie na sali) Ma pan 10 sekund, panie ministrze.",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Liczę na was! (Część posłów skanduje: Pięć, cztery, trzy, dwa…) (Głos z sali: Koniec, koniec!) A jak się boją konstytucji! Ha, ha, ha!",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie ministrze.",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Skąd taki strach?",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Proszę o zabranie głosu pana posła Krzysztofa Śmiszka…",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Panie marszałku…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "…w celu przedstawienia kandydatury pani poseł Anny Marii Żukowskiej zgłoszonej przez grupę posłów z Koalicyjnego Klubu Parlamentarnego Lewicy. (Część posłów skanduje: Regulamin! Regulamin! Regulamin!) Regulamin Sejmu został zastosowany w tej sprawie w sposób literalny. Jeżeli państwo posłowie będą w dalszym ciągu uniemożliwiali prowadzenie obrad, rozpocznę procedurę przywoływania państwa posłów do porządku, która zakończy się przerwaniem obrad. Jeżeli to jest to, co chcieli państwo uzyskać, to do tego właśnie to prowadzi. Pan minister Ziobro poprosił o głos w trybie przewidzianym przez regulamin Sejmu i ten głos uzyskał. Nie macie co do tego żadnych wątpliwości. (Poseł Barbara Bartuś: Ale nie ma limitu czasu.)",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Ale, panie marszałku, przerywany…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Wiem, panie ministrze. Ale mamy na to dowody w postaci 460 par oczu na tej sali… (Głos z sali: Nieprawda.) …że wstępując na tę mównicę, zgodził się pan z czasem… (Poseł Barbara Bartuś: Nieprawda.) …który został przeznaczony na pana wypowiedź. (Oklaski) Ten czas wynosił 3 minuty. W związku z powyższym bardzo pana proszę o opuszczenie mównicy. (Poseł Barbara Bartuś: Nie ma limitu czasu dla ministrów.)",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Panie marszałku, szanuję pana zapewnienie, że wszystkich pan traktuje równo.",
                },
                {"speaker": "Marszałek", "content": "Tak właśnie jest."},
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Zaznaczył pan wczoraj, że ma pan jasne upodobania polityczne i z niektórymi się zdecydowanie nie zgadza, ale wszystkich chce traktować równo. Ja nie chcę z zegarkiem, ze stoperem obliczyć, jak długo mówił pan Borys Budka, ale…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Mówił dokładnie w czasie, który był przewidziany…",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Mówił dokładnie ponad 3 minuty i sala mu nie przerywała…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "…i z którego państwa posłanka też w pełni skorzystała. (Poseł Barbara Bartuś: Ale w jakim trybie pan marszałek…)",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Pan mi uniemożliwia dokończenie wypowiedzi, panie marszałku. Regulamin pozwala panu zareagować, pozwolić mi jako ministrowi dokończyć kwestię.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, zastosowałem przepis regulaminu, który pozwala panu ministrowi zabrać głos na posiedzeniu, i zastosowałem czas, który będzie przewidziany w dyskusji, której się spodziewam, nad tymi kandydaturami. (Poseł Barbara Bartuś: Ale to jest coś innego.) Nie wiem, o co wnosi teraz pan minister, stojąc na mównicy.",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Panie marszałku, wnoszę o możliwość dokończenia kwestii…",
                },
                {"speaker": "Marszałek", "content": "A ile pan przewiduje?"},
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Pół minuty.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Pół minuty, 30 sekund, panie pośle.",
                },
                {
                    "speaker": "Minister Sprawiedliwości Zbigniew Ziobro",
                    "content": "Otóż art. 187 ust. 1 konstytucji o Krajowej Radzie Sądownictwa stanowi, że składa się ona m.in. – pkt 2 – z 15 członków wybranych spośród sędziów Sądu Najwyższego, sądów powszechnych, sądów administracyjnych i sądów wojskowych, a w ust. 4 tenże artykuł mówi, że ustrój, zakres działania i tryb pracy Krajowej Rady Sądownictwa oraz sposób wyboru jej członków określa… Kto? Borys Budka? (Głos z sali: Ha, ha, ha!) Nie, ustawa! (Oklaski) A co ustawa określa? Wybierają sędziowie? Nie, parlament wybrał, bo tak ustawa zdecydowała, panie Budka. Niech pan nie wprowadza ludzi w błąd. Jest granica bezczelności, naprawdę. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Proszę o zabranie głosu pana posła Krzysztofa Śmiszka w celu przedstawienia kandydatury pani poseł Anny Marii Żukowskiej zgłoszonej przez grupę posłów z Koalicyjnego Klubu Parlamentarnego Lewicy. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Krzysztof Śmiszek",
                    "content": "Panie Marszałku! Wysoka Izbo! Zanim przejdę do prezentacji tej kandydatury, mam jedną informację dla pana prokuratora Ziobry. Nie tylko na tej mównicy minął pana czas, ale w polityce minął pana czas. (Oklaski) Może pan krzyczeć, może pan machać rękami, może pan robić awantury, ale to już nic nie da. Was już nie ma w rządzie. (Oklaski) I może pan ostatni raz zabierać głos jako minister, ale dał pan świadectwo, jak pan traktuje standardy parlamentarne i standardy konstytucyjne. (Poseł Antoni Macierewicz: Nie bądź śmieszny.) Szanowni Państwo! Dzisiaj debatujemy nad ważnymi kandydaturami do ważnego organu, organu ustrojowego, organu konstytucyjnego, który ma stać na straży niezawisłości i niezależności sądów. (Poseł Barbara Bartuś: To nie jest jeszcze debata.) Co wyście uczynili z tym KRS-em? Co wyście zrobili z tym najważniejszym organem, który ma stać na straży naszych praw i naszych wolności obywatelskich? Zrobiliście sobie maszynkę do powoływania takich sędziów, którzy nie stoją przy konstytucji, nie stoją przy literze prawa, tylko stoją przy statucie partii Prawo i Sprawiedliwość. Te czasy już minęły. (Oklaski) Szanowni Państwo! Dzisiaj tak naprawdę stoimy przed ważnym konstytucyjnym momentem, w ważnym konstytucyjnym momencie, bo dzisiaj debatujemy nad osobami, które zgodnie z konstytucją, zgodnie z prawem, a nie zgodnie z wolą pana jednego lub drugiego z prawej strony, będą reprezentowali sędziów i ich interes, interes wymiaru sprawiedliwości w naszym kraju. Dzisiaj tak naprawdę wybieramy tylko cztery osoby, tak jak wymaga tego od nas konstytucja, a nie sędziów, którzy będą na telefon, a nie sędziów, którzy są wybierani przez polityków. Dzisiaj wybieramy polityków zgodnie z konstytucją. Będziemy zaraz wybierali w wyższej izbie, dzisiaj wybieramy w Sejmie. I to są jedyni kandydaci, jedyne osoby, które mogą zasiadać z rekomendacji Sejmu w Krajowej Radzie Sądownictwa. Dlatego mam niezwykły zaszczyt i przyjemność w imieniu klubu Lewicy zaprezentować kandydaturę pani posłanki Anny Marii Żukowskiej do Krajowej Rady Sądownictwa. Szanowni Państwo! Pani posłanka urodziła się 11 czerwca 1983 r. w Warszawie. Jest anglistką, ale jest także prawniczką.. W IX kadencji Sejmu była m.in wiceprzewodniczącą komisji sprawiedliwości. Była także osobą bardzo zaangażowaną w ochronę praw i wolności obywatelskich. W Krajowej Radzie Sądownictwa potrzebujemy także parlamentarzysty, który będzie walczył o prawa i wolności obywatelskie. Pani posłanka zajmowała się także ważnymi projektami ustaw w IX kadencji. Była także członkinią Komisji Odpowiedzialności Konstytucyjnej, a także pracowała w Komisji Nadzwyczajnej do rozpatrzenia projektu ustawy o zmianie Konstytucji Rzeczypospolitej Polskiej. Należała także do wielu zespołów parlamentarnych, ale przede wszystkim była przez 4 lata zaangażowana w dialog z organizacjami pozarządowymi, prawniczymi, które wypracowywały sposoby wyjścia z tego bagna prawnego, w jakie wpędziło nas Prawo i Sprawiedliwość przez ostatnie 8 lat. Tak, szanowni państwo, jesteśmy w bagnie prawnym po uszy, w bagnie konstytucyjnym, którego autorami są posłowie i posłanki, parlamentarzyści Prawa i Sprawiedliwości. Ci ludzie, którzy dzisiaj idą do Krajowej Rady Sądownictwa, mają jedno wielkie zadanie: odbudować autorytet Krajowej Rady Sądownictwa, patrzeć na ręce tym wszystkim, którzy pracują w tym organie, ale przede wszystkim reprezentować interes obywateli, którzy wybrali ich do parlamentu. Pani posłanka była zaangażowana w dialog z organizacjami prawniczymi. Wypracowywała, tak jak powiedziałem, rozwiązania mające na celu naprawienie praworządności w Polsce. Jest gwarantem demokratycznego, proprawnoczłowieczego głosu w Krajowej Radzie Sądownictwa. Co istotne, pani poseł była także zaangażowana w walkę o godną pracę i godną płacę pracowników sądów i prokuratur, bo w tym całym 8-letnim rządzie i w tych czasach, przez 8 lat rządów Prawa i Sprawiedliwości zajmowano się wszystkim w wymiarze sprawiedliwości, tylko nie poprawą losu pracowników sądów i prokuratur, na których tak naprawdę, na ich barkach, cały wymiar sprawiedliwości jest oparty. Była zaangażowana, tak jak powiedziałem, w obronę praw człowieka, także wolności obywatelskich, m.in. osób LGBT. Pomagała także osobom represjonowanym przez reżim Prawa i Sprawiedliwości podczas tzw. tęczowej nocy zatrzymań w Warszawie w sierpniu 2020 r. Daje gwarancję, że w przeciwieństwie do dotychczasowych członków Krajowej Rady Sądownictwa, którzy byli delegowani przez Prawo i Sprawiedliwość, będzie trzymała się konstytucji, będzie realizowała swoją misję w oparciu o konstytucję i przepisy prawa. Pan minister Ziobro, który wyszedł na mównicę, mówił pięknie, krzyczał o tym, że przecież konstytucja, art. 187 konstytucji mówi o tym, że sposób działania Krajowej Rady Sądownictwa jest uregulowany w ustawie. No ale pan minister Ziobro zapomniał chyba powiedzieć o jednym: że te wszystkie ustawy, które przyjmuje parlament, muszą być zgodne z konstytucją. O jakiej zgodności z konstytucją możemy mówić w przypadku neo-KRS 2.0? Bo dzisiaj mamy neo-KRS 2.0. To jest kolejne wcielenie nielegalnego ciała, które działa niezgodnie z ustawą zasadniczą. O jakiej zgodności tej ustawy można mówić, skoro konstytucja wyraźnie stanowi: Sejm wysyła czterech przedstawicieli, Senat wysyła dwóch przedstawicieli? Nie wysyłamy tam żadnych sędziów jako parlamentarzyści. Nie wysyłamy tam innych osób. Wysyłamy tam tylko parlamentarzystów. A Prawo i Sprawiedliwość, jak już bierze władzę, to za nic ma konstytucję, za nic ma wartości, za nic ma zasady. Szanowni Państwo! Czeka nas bardzo długi okres naprawy praworządności, powrotu na ścieżkę demokracji, powrotu na ścieżkę praworządności, ale damy radę, bo 11,5 mln Polaków 15 października powiedziało: odrzucamy waszą wizję konstytucji, odrzucamy waszą wizję działania państwa, odrzucamy plucie na konstytucję i odrzucamy szarganie konstytucji. (Poseł Barbara Bartuś: Ile Lewica dostała posłów?) Polacy, 12 mln Polaków powiedziało: chcemy wreszcie standardów konstytucyjnych, chcemy wreszcie powrotu na ścieżkę praworządności. Tego słowa dotrzymamy. Możecie sobie krzyczeć, możecie sobie machać rękami, ale powrotu na ścieżkę demokracji już nic nie zatrzyma. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Drodzy państwo, jesteśmy w sytuacji, w której do głosu zgłasza się kolejny minister… (Gwar na sali) Zaraz, chwilę, dajcie mi państwo skończyć. (Poseł Jarosław Urbaniak: Panie marszałku, to nie jest minister. Wczoraj się podał panu do dymisji.) Tak, ja to wiem, natomiast powierzona została im misja kontynuowania pracy do momentu powołania nowej Rady Ministrów. (Gwar na sali) Drodzy państwo, czy zechcecie mnie posłuchać przez chwilę? Przyszedł kolejny członek tego rządu, który chce zabrać głos… (Gwar na sali) (Minister Edukacji i Nauki Przemysław Czarnek: To ja, to ja.) (Oklaski) Moment, proszę wysłuchać, co mam do powiedzenia. …w trybie, który jest dopuszczany w regulaminie Sejmu. Natomiast zwracam też państwu uwagę, że każdego przepisu można nadużyć. (Minister Edukacji i Nauki Przemysław Czarnek: Panie marszałku, ja jeszcze nie zacząłem, a pan tu takie rzeczy już mówi. No na litość boską!) Jeżeli będziemy mieć tu do czynienia z sytuacją, w której zgłosi się cała Rada Ministrów, żeby w mojej ocenie zakłócać porządek obrad Sejmu… (Głos z sali: Ooo…) …to decyzją marszałka, tę decyzję biorąc na siebie, liczbę wystąpień członków Rady Ministrów w czasie tej debaty ograniczę. (Gwar na sali, oklaski) (Poseł Piotr Kaleta: Barierki na mównicę.) Proszę poczekać. Na samym początku procedowania nad tym punktem porządku dziennego zgłosiło się do głosu dwóch członków Rady Ministrów. W międzyczasie o głos poprosił pan minister Ziobro. Teraz o głos prosi pan minister Czarnek. Informuję państwa, że ponieważ wcześniej do głosu zgłosili się minister Schreiber i minister Szynkowski vel Sęk… Mając świadomość tego, że w tym punkcie przewidziana jest dyskusja, a więc sytuacja, w której siły polityczne reprezentowane w parlamencie będą mogły zabrać głos w procedowanej sprawie, informuję, że na ministrze Szynkowskim vel Sęku lista członków Rady Ministrów przed dyskusją zostanie wyczerpana. (Gwar na sali) (Głos z sali: Regulamin!) Jeżeli panowie posłowie i panie posłanki będą mieli w tej sprawie wątpliwości, bardzo proszę o zgłoszenie wniosku do komisji regulaminowej i spraw poselskich, która na pewno się do tego odniesie. (Oklaski) (Poseł Krzysztof Lipiec: Czytaj regulamin!) 3 minuty, panie ministrze.",
                },
                {
                    "speaker": "Minister Edukacji i Nauki Przemysław Czarnek",
                    "content": "Panie Marszałku Rotacyjny! Wysoki Sejmie Nierotacyjny… (Wesołość na sali, oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Przepraszam bardzo, ale w tym momencie, panie ministrze, narusza pan powagę tej Izby i jej organów. (Gwar na sali, oklaski) Ma pan 3 minuty na wystąpienie.",
                },
                {
                    "speaker": "Minister Edukacji i Nauki Przemysław Czarnek",
                    "content": "Panie marszałku, to wyście nazwali tę funkcję marszałkiem rotacyjnym, nie my. Dlaczego pan ma o to pretensje? Niech pan ma pretensje do swoich. (Oklaski) Panie marszałku, jest taka dobra zasada: nie mierz kogoś swoją miarą. (Oklaski) Pan teraz nadużywa regulaminu, a mówi o nadużyciach prawa, zanim ja jeszcze wystąpiłem. Na litość boską! Nie mierz kogoś swoją miarą. (Głos z sali: Ooo…)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie ministrze, korzysta pan ze swojego czasu.",
                },
                {
                    "speaker": "Minister Edukacji i Nauki Przemysław Czarnek",
                    "content": "Panie marszałku, teraz ja mówię. Takie są standardy w Izbie demokratycznej. (Oklaski) (Głos z sali: Uspokój się.) Otóż mamy do czynienia z daleko posuniętą… Już nie z bezczelnością, tylko wręcz chamstwem politycznym. Na tej mównicy przed momentem występował przedstawiciel Lewicy, która uzyskała, proszę państwa, w tych wyborach milion osiemset kilkadziesiąt tysięcy głosów. Występował po ministrze Zbigniewie Ziobrze, który startował z komitetu wyborczego, który uzyskał 7660 tys. głosów. (Oklaski) (Głos z sali: No i co z tego?) Jeśli pan dobrze liczy, panie pośle Śmiszek… Ale pan dobrze nie liczy. To jest prawie 6 mln wyborców więcej. 6 mln wyborców więcej oddało głos na listy wyborcze, z których startował pan minister Ziobro, aniżeli na Lewicę. I pan z tej mównicy wyrzuca ministra Ziobrę z polityki? Pan z tego państwa przed momentem wyrzucił ponad 6 mln ludzi, więcej, 7660 tys. ludzi. (Głos z sali: Hańba!) (Głos z sali: Skandal!) Oni się dla was nie liczą, oni są dla was nikim, a nie takie są standardy demokratyczne. Demokracja polega na tym, że głos mają ludzie, a nie Śmiszki, które nie potrafią liczyć. (Oklaski) (Głos z sali: Brawo!) To jest pierwsza rzecz. Druga rzecz. Przed momentem pan Budka w swoim wykładzie powiedział, że do Krajowej Rady Sądownictwa muszą trafić ludzie, którzy znają konstytucję i rozumieją, co w niej jest. Panie pośle, niech pan nam przypomni, kto w 2015 r. zgłaszał do ustawy o Trybunale Konstytucyjnym, do tego zamachu na Trybunał Konstytucyjny, który zrobiliście jeszcze w tamtej haniebnej kadencji 2011–2015, poprawki, które umożliwiły wam wybór dwóch sędziów… (Głos z sali: Trzech.) …Trybunału Konstytucyjnego na zaś, na zapas, kompletnie niezgodnie z konstytucją. Kto następnie stwierdził niekonstytucyjność tych poprawek? Trybunał Konstytucyjny z panem Rzeplińskim na czele. Wie pan, kto zgłaszał te poprawki? M.in. pan Kropiwnicki, którego pan teraz chce dać do KRS-u. (Głosy z sali: Ooo…) Gdzie tu jest logika? Gdzie tu jest logika? (Głos z sali: Jesteście kłamcami.) Trzecia rzecz: proszę państwa, przez całe 4 lata, więcej, przez prawie 8 lat słyszeliśmy, że nie ma KRS-u, że jest neo-KRS, że w zasadzie to wszystko nie działa. A oni dzisiaj procedują nad wyborem swoich kandydatów do czegoś, czego nie ma. U was brakuje logiki, zwykłej logiki. (Wesołość na sali, oklaski) (Głos z sali: Brawo!) A jak nie ma logiki, to nie ma demokracji. Uczcie się demokracji. Konstytucję… Nie płaczcie nad nią, tylko ją po prostu raz przeczytajcie. Dziękuję bardzo. (Wesołość na sali, oklaski) (Część posłów skanduje: Przemek! Przemek! Przemek!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, przyznam szczerze, że to są jakieś standardy, które nie do końca pojmuję. (Wesołość na sali) Okazuję panu szacunek, okazuję szacunek pana stanowisku, pozwalam zabrać głos zgodnie z regulaminem… (Gwar na sali) (Głos z sali: Uuu…) …natomiast spotyka mnie za to coś, co można nazwać afrontem. Jeżeli są to pana standardy parlamentaryzmu, to muszę powiedzieć, że głęboko nad tym ubolewam. (Gwar na sali) Proszę o zabranie głosu pana posła Mirosława Suchonia w celu przedstawienia kandydatury pana posła Tomasza Zimocha zgłoszonej przez grupę posłów z Klubu Parlamentarnego Polska 2050 – Trzecia Droga.",
                },
                {
                    "speaker": "Poseł Mirosław Suchoń",
                    "content": "Wielce Szanowny Panie Marszałku! Wysoka Izbo! Wydaje się, że minister edukacji nie powinien mieć kłopotów z matematyką, wydaje się, że 12 mln głosów to jednak więcej niż 7 mln. I gdyby pan minister miał choć trochę przyzwoitości, to z pewnością nie dzierżyłby już tej teki, tylko podał się skutecznie do dymisji także dlatego, żeby uznać, że głos suwerena wyrażony w tak wyraźny sposób, ponad 12 mln głosów, jest głosem, który mówi, że powinna nastąpić zmiana, także w tej Izbie. (Gwar na sali) A to, co widzieliśmy przed chwilą, kiedy pan minister Wójcik, stojący tutaj obok, pokazywał panu ministrowi Ziobrze z szelmowskim uśmiechem: kontynuuj, kontynuuj, kontynuuj, nie ma na celu żadnej merytorycznej dyskusji, a tylko i wyłącznie zrobienie z Wysokiej Izby miejsca, którego Polacy nie akceptują. (Gwar na sali) Polacy nie zaakceptowali tego, co robiliście przez ostatnie 8 lat, i dlatego 12 mln obywateli powiedziało, że chce zmiany. Dzisiaj z tego miejsca, z tej mównicy apeluję, żeby Prawo i Sprawiedliwość wreszcie uznało decyzję suwerena. Za każdym razem w trakcie debaty parlamentarnej w ciągu ostatnich 8 lat mówiliście: uznawajcie decyzje suwerena. Czas sięgnąć po ten argument we własnym gronie. Czas, aby klub Prawa i Sprawiedliwości pogodził się z decyzją suwerena, i czas na to, aby Wysoka Izba rozpoczęła proces odwracania tych zmian, tych złych zmian, do których państwo doprowadziliście. (Oklaski) (Poseł Antoni Macierewicz: Czas, byście przestali kłamać.) Jedną z tych zmian, których oczekują obywatele, jest szacunek. Szacunek do siebie nawzajem… (Głos z sali: Osiem gwiazdek.) …szacunek do marszałka Sejmu, szacunek do Wysokiej Izby, szacunek do tych, którzy z nami debatują. (Poseł Antoni Macierewicz: Szacunek do Polski.) (Głos z sali: I kto to mówi?) Dzisiaj jedyną stroną, która tego szacunku w trakcie tej ważnej debaty nie okazuje, jest klub Prawa i Sprawiedliwości. (Poseł Tadeusz Woźniak: Puknij się w głowę!) Mówię to z przykrością, dlatego że debatujemy o jednej z najważniejszych spraw z punktu widzenia obywateli. (Poseł Barbara Bartuś: Ma pan zgłaszać kandydatów. To nie jest czas debaty.) Krajowa Rada Sądownictwa jako organ konstytucyjny stoi na straży niezależności sądownictwa i niezawisłości sędziów. Ta sprawa dotyka każdego z nas. Ta sprawa dotyka każdego obywatela, bo przecież każdy z nas może być uczestnikiem postępowania sądowego. (Głos z sali: Oby.) To oznacza, że jeżeli ktoś jest w tym procesie sądowym, to od tego, w jaki sposób pracowała Krajowa Rada Sądownictwa, zależy to, czy jego sprawa zostanie rozpatrzona sprawiedliwie i w takim czasie, który będzie czasem odpowiednim. Jeżeli czytamy przepisy konstytucji, to art. 187 mówi nam, że jako Sejm wybieramy czterech członków KRS. Czterech, nie kilkunastu. Gdybyśmy się wgłębili – tak jak proponował to wielce szanowny pan minister Ziobro – w lekturę konstytucji, to np. art. 190 ust. 2 mówi o niezwłocznym ogłaszaniu orzeczeń Trybunału Konstytucyjnego. Przypominam, bo przecież państwo o tym zapomnieli. A gdyby państwo wrócili do lektury konstytucji, to polecam od razu ciągiem cały rozdział, który nazywa się Trybunał Stanu. I żeby ułatwić, zaczyna się od art. 198. Myślę, że w kolejnych latach będzie to państwu bardzo potrzebne. W tej ważnej debacie mam zaszczyt przedstawić kandydata do Krajowej Rady Sądownictwa, który zgłaszany jest przez Trzecią Drogę, przez Klub Parlamentarny Polska 2050 – Trzecia Droga i Klub Parlamentarny Polskie Stronnictwo Ludowe – Trzecia Droga. Mam zaszczyt zaprezentować kandydaturę pana posła Tomasza Zimocha. Pan Tomasz Zimoch ma 66 lat. Jest magistrem prawa. Po ukończeniu studiów na Wydziale Prawa i Administracji Uniwersytetu Łódzkiego odbył aplikację i zdał egzamin sędziowski. To niezwykle ważne, ponieważ większość z nas zna Tomasza Zimocha jako redaktora, jako dziennikarza, natomiast niezwykle ważna jest ta podbudowa merytoryczna, czyli ukończone studia prawnicze oraz aplikacja i zdany egzamin sędziowski. Pan poseł Tomasz Zimoch w IX kadencji Sejmu zasiadał w Komisji Sprawiedliwości i Praw Człowieka, w której znany był z tego, że bronił niezależności sądów i niezawisłości sędziów. To jest niezwykle ważne, ponieważ wkraczamy na drogę przywracania praworządności w Polsce. Prawidłowy wybór członków Krajowej Rady Sądownictwa oznacza, że ten proces rozpocznie się niezwykle dynamicznie. To, co jest ważne, to to, aby w Krajowej Radzie Sądownictwa zasiadały osoby, które naprawdę wiedzą, że to jest niezwykle ważna funkcja, niezwykle ważna z powodów państwa demokratycznego, konstytucyjnych, ale także to, o czym mówiłem, że ma to pośredni wpływ na każdego obywatela, na gospodarkę, na to wszystko, co w naszym państwie się dzieje. Z tego tytułu tym kandydatem jest Tomasz Zimoch, który w Krajowej Radzie Sądownictwa te wszystkie doświadczenia zarówno w warstwie merytorycznej, jak i praktycznej, również w Sejmie, będzie przenosił i będzie współtworzył dobre standardy. Szanowni Państwo! Reasumując, zarówno wykształcenie, jak i doświadczenie płynące m.in. z pracy parlamentarnej oraz nieskazitelna opinia na temat jego dotychczasowej pracy pozwalają zgłosić pana posła Tomasza Zimocha jako znakomitego kandydata na członka Krajowej Rady Sądownictwa. Bardzo proszę o poparcie pana posła w głosowaniu. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Zgodnie z tym, co powiedziałem przed chwilą, proszę o zabranie głosu pana Łukasza Schreibera, ministra – członka Rady Ministrów, który zgłosił się do zabrania głosu w trybie art. 185 regulaminu Sejmu. Panie pośle, bardzo proszę, żeby pana wypowiedź trwała 3 minuty. (Poseł Barbara Bartuś: Dlaczego?) Tak jak przyjęliśmy to w głosach klubowych. (Poruszenie na sali) Rozumiem, rozumiem.",
                },
                {
                    "speaker": "Minister – Członek Rady Ministrów Łukasz Schreiber",
                    "content": "Wielce Szanowny Panie Marszałku! Ministrowie proszą o głos w trybie faktycznie art. 186, który nie ogranicza ich limitem czasu, dlatego że z tej mównicy, przed chwilą, podczas tej dyskusji nie tylko padały słowa, które miały na celu przedstawienie kandydatów, lecz także prowadzono debatę, a tak naprawdę urągano standardom demokratycznym. (Oklaski) W bezprawny sposób oskarżano ministrów i prawą część tej sali o rzeczy zupełnie niewiarygodne i skandaliczne. Przez ostatnie 8 lat – ja wiem, że pana marszałka nie było wtedy tutaj z nami – z lewej strony sali, zwłaszcza ze strony Platformy Obywatelskiej, padały groźby, i to nie tylko w stosunku do posłów, lecz także w stosunku do mediów, w stosunku do sędziów. Gdy wyroki były dla was niekorzystne, tak wyglądała tu demokracja, tak wyglądało poszanowanie prawa. Mówię to jako minister do spraw parlamentarnych. (Poseł Borys Budka: Czego?) Wielokrotnie widziałem, z jaką pogardą, z jakim także chamstwem zwracano się do pani marszałek. To, co wczoraj pokazaliście… Mogliście zacząć inaczej, a zaczęliście od tego, że największy klub parlamentarny został pozbawiony miejsca w Prezydium Sejmu. (Głos z sali: I Senatu.) To jest okazanie – żebyście dobrze wiedzieli – pogardy, i to nawet nie w stosunku do pani marszałek, nie w stosunku do Prawa i Sprawiedliwości, tylko w stosunku do 7600 tys. wyborców. (Oklaski) (Głos z sali: Brawo!) Wysoka Izbo! Wiem, że miłe są wam standardy, które wprowadzaliście za czasów swoich rządów. Sędziowie na telefon – tak, pamiętamy te standardy. Miłe wam jest to, że lider waszego ugrupowania na wiecach politycznych unieważnia referendum. Miłe wam jest to, że z tej mównicy posłowie unieważniają ustawy i konstytucję. Takie są nowe standardy? Chcę zapewnić tu o jednym: my się z tym nie pogodzimy. Możecie nas pozbawić wszelkich miejsc i wszelkich stanowisk, ale my będziemy korzystali z regulaminu Sejmu, aby przeciwstawiać się waszej agresji, łamaniu przez was zasad, procedur, ustaw i konstytucji. Będziemy w tym, panie marszałku, zdecydowani. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Pan minister Szymon Szynkowski vel Sęk.",
                },
                {
                    "speaker": "Minister do Spraw Unii Europejskiej Szymon Szynkowski vel Sęk",
                    "content": "Panie Marszałku! Wysoka Izbo! Myślę, że zgodzimy się z tym wszyscy, że kandydatami do Krajowej Rady Sądownictwa, którą – jak już wspominano państwu wcześniej – nazywaliście neo-KRS, a która teraz nagle uzdrowiła się dzięki obecności państwa w większej liczbie na tej sali w nowej kadencji, powinny być osoby o nieposzlakowanej opinii. Niewątpliwie kandydatem nie powinna być zatem osoba, która regularnie posługuje się nieprawdą w życiu publicznym. Dlatego chciałbym wskazać, że w mojej opinii kryteriów nie spełnia pod tym względem pani poseł Kamila Gasiuk-Pihowicz. (Oklaski) I wskażę tutaj przykład, jeśli państwo pozwolicie, wynikający wprost z moich doświadczeń, kompetencji. Mieliśmy w ostatnich dniach na posiedzeniu Komisji do Spraw Unii Europejskiej okazję przesłuchiwać kandydatów do Trybunału Sprawiedliwości Unii Europejskiej oraz Sądu Unii Europejskiej. Podczas tego przesłuchania kandydatów – dwójki profesorów o niezwykle wysokich kompetencjach, jednej pani doktor, pani poseł Kamila Gasiuk-Pihowicz, która nie jest członkiem tej komisji, ale korzystała z prawa do obecności, a także zadawania pytań na tym posiedzeniu komisji, kilkukrotnie posłużyła się w stosunku do tych kandydatów oskarżeniami, zarzutami o charakterze nieprawdziwym. Zaraz wykażę, że jest to prawda. Pierwszy z brzegu przykład to fakt zaatakowania rodziny jednej z kandydatek. (Głos z sali: Hańba!) Pani poseł Kamila Gasiuk-Pihowicz uznała, że trzeba zaatakować męża jednej z kandydatek, mówiąc, że jest neosędzią. Pomijam fakt tego nazewnictwa, używania członu „neo”, który stanowi niezwykły przedmiot ulubienia pani poseł, bo okazało się, że jest on sędzią od kilkunastu lat, że jest to po prostu nieprawdziwy zarzut. To się okazało jeszcze w trakcie posiedzenia komisji. Następnie pani poseł powiedziała innej z kandydatek – pani profesor z dużym dorobkiem, pracującej od wielu lat w administracji publicznej, że awansowała ona i robiła karierę tylko za rządów Prawa i Sprawiedliwości, podczas gdy pani profesor zaczynała swoją karierę w administracji publicznej za rządów premiera Jerzego Buzka, później pracowała z panią minister Izabelą Jarugą-Nowacką. To nie przeszkodziło pani poseł postawić takiego zarzutu. Wreszcie, w ferworze stawiania nieprawdziwych zarzutów powiedziała, że Rada Ministrów, która zaakceptowała tych kandydatów, zamiast zajmować się budżetem zajmuje się kandydatami do organów Unii Europejskiej. Za chwilę okazało się, że Rada Ministrów na tym samym posiedzeniu zajmowała się również budżetem państwa. Pani poseł strzela więc oskarżeniami, nieprawdziwymi zarzutami, nie ma żadnych skrupułów, mogłaby postawić każdy zarzut każdej osobie. Nie są tu zatem spełnione warunki dotyczące posiadania nieposzlakowanej opinii. W mojej ocenie taka osoba nie powinna pełnić funkcji w Krajowej Radzie Sądownictwa. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie ministrze. Po temperaturze emocji, które towarzyszyły prezentacji kandydatów, wnoszę, że są chętni do dyskusji – i tak rzeczywiście jest. Proponuję, aby w dyskusji nad tym punktem porządku dziennego Sejm wysłuchał 3-minutowych oświadczeń w imieniu klubów i koła. Jeżeli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycję przyjął. Sprzeciwu nie słyszę… (Poseł Barbara Bartuś: Sprzeciw.) Jest sprzeciw? Bardzo proszę. Jeżeli jest sprzeciw, tę propozycję poddamy głosowaniu. Kto z pań i panów posłów jest za propozycją, aby w dyskusji nad tym punktem porządku dziennego Sejm wysłuchał 3-minutowych oświadczeń w imieniu klubów i koła, proszę podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 452 posłów. 245 – za, 191 – przeciw, 16 się wstrzymało. Stwierdzam, że Sejm propozycję, aby w dyskusji nad tym punktem porządku dziennego Sejm wysłuchał 3-minutowych oświadczeń w imieniu klubów i koła, przyjął. Gdzie mamy listę mówców? Niestety, mieliśmy przed chwilą… (Wesołość na sali) (Głos z sali: Ojej…) (Wypowiedź poza mikrofonem) Bardzo cenię państwa komentarze i uwagi, natomiast zwracam też uwagę, że z mojej perspektywy stają się odrobinę monotematyczne. Zachęcam do większej oryginalności, pracy intelektualnej. (Wesołość na sali, oklaski) Obrazić też trzeba umieć. Dobrze, mamy listę na tablicy. Ja jej nie widzę u siebie, a więc… (Wypowiedź poza mikrofonem) Nie, oczywiście rozumiem, że jeżeli mamy dwóch zgłoszonych mówców, to chcą podzielić swój czas na pół i mówić przez… A nie, jest ich nawet trzech, a więc każdy z panów chce mówić po 1 minucie. Rozumiem, że taka jest decyzja. Otwieram dyskusję. Zapraszam pana posła Krzysztofa Szczuckiego z Klubu Parlamentarnego Prawo i Sprawiedliwość. 1 minuta, panie pośle. (Głos z sali: Dlaczego?) Dlatego, że są 3 minuty na wypowiedzi w imieniu klubów i koła. 1 minuta. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Krzysztof Szczucki",
                    "content": "Panie Marszałku! Wysoka Izbo! Najpierw krótka lekcja regulaminu dla pana marszałka. Marszałek Sejmu udziela głosu członkom Rady Ministrów poza kolejnością mówców zapisanych do głosu, ilekroć tego zażądają. Jeżeli minister rządu Rzeczypospolitej Polskiej i inni ministrowi będą chcieli tutaj mówić do rana, to pan marszałek i my wszyscy mamy obowiązek ich wysłuchać. (Oklaski) Tak mówi regulamin. (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, myli się pan. Myli się pan.",
                },
                {
                    "speaker": "Poseł Krzysztof Szczucki",
                    "content": "Przechodząc do rzeczy…",
                },
                {"speaker": "Marszałek", "content": "Myli się pan."},
                {
                    "speaker": "Poseł Krzysztof Szczucki",
                    "content": "Panie Marszałku! Wysoka Izbo! Zgodnie z art. 187 konstytucji pkt 2 Krajowa Rada Sądownictwa składa się z 15 członków wybranych spośród sędziów Sądu Najwyższego, sądów powszechnych, sądów administracyjnych, sądów wojskowych. Ustrój, zakres działania i tryb pracy KRS oraz sposób wyboru jej członków określa ustawa. Fakt, że konstytucja nie przewiduje organu, który ma wybrać sędziów do Krajowej Rady Sądownictwa, oznacza tylko tyle, że Sejm ma prawo ustalić organ w ustawie. Sejm, Senat i pan prezydent swoim podpisem ustanawiają organ, który wybiera sędziów do Krajowej Rady Sądownictwa. Ustawa, nie stowarzyszenie „Iustitia”, nie pan, panie pośle Budka, nie pan, panie pośle Śmiszek, tylko ustawa Sejmu, ustawa, której przysługuje przymiot konstytucyjności. A fakt, że art. 10 stanowi, że ustrój opiera się na podziale i równowadze władzy ustawodawczej, władzy wykonawczej i władzy sądowniczej, oznacza właśnie to, że Krajowa Rada Sądownictwa uzyskuje swój mandat demokratyczny dzięki temu, że sędziowie do KRS wybrani są nie przez inny organ, ale przez Sejm. Dzięki temu Krajowa Rada Sądownictwa przestała w końcu być organem ochrony interesów sędziów i w końcu stanęła na straży praworządnego wymiaru sprawiedliwości. Dziękuję bardzo.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Głos zabierze pan poseł Sebastian Kaleta z Klubu Parlamentarnego Prawo i Sprawiedliwość. Zwracam uwagę, że wykorzystano prawie 2 minuty czasu wypowiedzi przewidzianego dla klubu Prawo i Sprawiedliwość. Ma pan 1 minutę i 2 sekundy, panie pośle.",
                },
                {
                    "speaker": "Poseł Sebastian Kaleta",
                    "content": "Panie Marszałku sprawujący funkcję w systemie rotacyjnym! Wysoka Izbo! Dzisiaj pan poseł Budka poniewierał polską konstytucją, poniewierał polską dumą narodową, polską demokracją. Dlaczego? Mówił o tym, że Polska nie stosuje jakichś wartości europejskich, że jesteśmy jako państwo gorsi, waśnie z perspektywy funkcjonowania Krajowej Rady Sądownictwa. Tylko że nasza konstytucja i nasza Krajowa Rada Sądownictwa funkcjonują analogicznie do Krajowej Rady Sądownictwa w Hiszpanii. Czy Hiszpanie się wstydzą? Czy Hiszpanie są poniewierani na forum Unii Europejskiej? Czy hiszpańskie władze proszą o wsparcie Unię Europejską? Nie. Dlatego też warto powiedzieć, że upolitycznianie, które wy tak zarzucacie Krajowej Radzie Sądownictwa w Polsce, to nie jest żadna sprawa, która narusza jakiekolwiek standardy, bo chociażby w Niemczech sędziów do sądów federalnych powołują politycy. Panie premierze, panie przewodniczący Tusk, takie są właśnie niemieckie standardy… (Poseł Jakub Rutnicki: W Polsce jesteśmy.) …a wam się nie podoba, że w Polsce możemy mieć Krajową Radę Sądownictwa wybieraną zgodnie z polską konstytucją… (Dzwonek) (Głos z sali: Czas!) (Głos z sali: Mamy czas.) …i zasadami polskiej demokracji, a nie według podległych standardów, w które wy wpychacie Polskę.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Czas minął. (Poseł Mariusz Kałużny: Panie marszałku…) Przepraszam? (Wypowiedź poza mikrofonem) Przecież jest debata i Izba zagłosowała nad kształtem tej debaty. Nie rozumiem zdumienia pana posła. (Poseł Mariusz Kałużny: Szanowni państwo…) (Głos z sali: Złaź z mównicy!) (Głos z sali: Zejdź, zejdź!) Bardzo proszę o zabranie głosu pana posła Arkadiusza Myrchę z klubu Koalicji Obywatelskiej. Bardzo proszę, panie pośle. 3 minuty.",
                },
                {
                    "speaker": "Poseł Arkadiusz Myrcha",
                    "content": "Panie Marszałku! Wysoka Izbo! Wystąpienie pana posła Zbigniewa Ziobry trochę przypomniało mi słowa nie tak dawno wypowiedziane przez pana najbliższego politycznego sojusznika, przyjaciela, pana posła Mateusza Morawieckiego. (Poseł Iwona Ewa Arent: Jeszcze pana premiera.) Pozwolił on sobie na zdanie, które być może przejdzie do historii jego aktywności politycznej jako jedyne prawdziwe. Komentując właśnie pana osiągnięcia w dziedzinie wymiaru sprawiedliwości, powiedział: najgłośniej ryczy krowa, która najmniej mleka daje. (Poruszenie na sali, oklaski) Panie premierze, pełna zgoda. Dzisiaj pan to potwierdził. Dokładnie tak jest. (Głos z sali: To o was.) Ale widząc to energiczne pana wystąpienie z charakterystycznym lekko purpurowym zacięciem… (Oklaski) (Głos z sali: Ha, ha, ha!) …tak się zastanawiałem, dlaczego pan nie był taki aktywny (Oklaski) na posiedzeniach Krajowej Rady Sądownictwa, której tak pan dzisiaj broni. Proszę powiedzieć, ile razy pan był na posiedzeniu Krajowej Rady Sądownictwa. (Poseł Adam Szłapka: Mutację miał wtedy.) Chociażby w tym roku. (Głos z sali: Zero.) Zero. A proszę powiedzieć, w ilu jawnych głosowaniach pan brał udział. (Głos z sali: Zero.) Zero? (Głos z sali: Uuu…) A teraz uwaga: A proszę powiedzieć, ile pan zarobił w KRS-ie. (Głos z sali: Miliony…) (Poseł Borys Budka: 44…) Nie zero. (Wesołość na sali) Czterdzieści kilka tysięcy? Trzydzieści kilka? Właśnie, panie pośle Kaleta, Krajowa Rada Sądownictwa za waszych rządów nie działa jak hiszpańska. Ona działa jak wasze spółki Skarbu Państwa. (Oklaski) Zrobiliście sobie z KRS-u krajową radę szmalu. (Oklaski) Gdzie są panowie Kownacki, Mularczyk? Powiedzcie dzisiaj śmiało opinii publicznej, ile zarobiliście w KRS-ie. 100 tys.? (Głos z sali: Mało.) 120 tys.? Na litość boską! A jakie są efekty tej pracy? Wydłużające się kolejki w sądach? Wakaty na stanowiskach sędziowskich. Postępowania przeciwko praworządności. Miejcie odrobinę honoru, miejcie odrobinę godności, bo to, że przegraliście wybory, to cała Polska wie. (Gwar na sali) (Poseł Bożena Borys-Szopa: Kto tu mówi o godności?) Przepraszam, poza 194 osobami… (Głos z sali: I prezydentem.) …cała Polska wie, że przegraliście. (Oklaski) Jeżeli, panie Zbigniewie, do tej pory nie nauczyliście się odchodzić z godnością, to nigdy nie jest za późno na naukę. Można. I Krajowa Rada Sądownictwa, tak jak powiedział pan przewodniczący Budka, wróci na swoje konstytucyjne tory. Skończy się bezprawie, skończy się niesprawiedliwość, a w Krajowej Radzie Sądownictwa będą zasiadali ci, którzy dadzą największą rękojmię niezależności od polityki. (Gwar na sali) Nie będzie tam partyjnych kacyków, którzy pilnują głosowań, panowie Mularczyk i Kownacki. Krajowa Rada Sądownictwa jest wielkim osiągnięciem okresu transformacji ustrojowej, o którą walczyli tutaj wszyscy (Dzwonek), od prawa do lewa, a wy sobie zrobiliście z niej dojną krowę. (Głos z sali: Brawo!) Koniec z tym. Polacy powiedzieli: dość. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo panu posłowi. Teraz głos zabierze pan poseł Michał Gramatyka z Klubu Parlamentarnego Polska 2050 – Trzecia Droga. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Michał Gramatyka",
                    "content": "Szanowny Panie Marszałku! Wysoki Sejmie! Krajowa Rada Sądownictwa ukształtowana od 2018 r. nie jest tożsama z organem konstytucyjnym. To nie jest teza posła Trzeciej Drogi, posła Koalicji Obywatelskiej, Lewicy czy PSL-u. (Głos z sali: Oddaj pieniądze.) To jest cytat z uchwały siedmioosobowego składu Izby Karnej Polskiego Sądu Najwyższego podjętej 2 czerwca ub.r. Cytuję dalej tę uchwałę: W obecnym KRS i tym właściwym, wynikającym z konstytucji, wspólna jest tylko nazwa. Nie trzeba szukać daleko, żeby wiedzieć, że polski Sąd Najwyższy potwierdził tylko to, co, jak się wydaje, jest oczywiste dla prawników, profesorów, teoretyków i praktyków prawa, którzy walczą od wielu lat z deformą polskiego sądownictwa, dla Trybunału Sprawiedliwości Unii Europejskiej, dla polskiego Naczelnego Sądu Administracyjnego, który przecież tę prawdę wyrażał w niezliczonych orzeczeniach, dla historycznej bezprecedensowej uchwały pełnego składu połączonych izb polskiego Sądu Najwyższego ze stycznia 2020 r. Nie wolno skapitulować przed bezprawiem, nie wolno czekać. 15 października miliony Polek i Polaków zagłosowało za przywróceniem praworządności tu i teraz, bo praworządność służy ochronie wolności, ochronie praw człowieka. To nie jest kwestia odwetu czy bycia radykalnym. To jest kwestia poszanowania ustawy zasadniczej, polskiej konstytucji. Ja wam bardzo chętnie przypomnę: Wszystkich, którzy dla dobra Trzeciej Rzeczypospolitej tę konstytucję będą stosowali… (Poseł Anita Czerwińska: Ile zarobiłeś w Tauronie?) …wzywamy, aby czynili to, dbając o zachowanie przyrodzonej godności człowieka, jego prawa do wolności, a poszanowanie tych zasad mieli za niewzruszoną podstawę Rzeczypospolitej Polskiej. Warto sięgnąć do ustawy zasadniczej. Klub Polska 2050 – Trzecia Droga zagłosuje za kandydatami ugrupowań demokratycznych i przeciw tym, którzy przykładali rękę do niszczenia praworządności w Polsce. Dziękuję. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję panu posłowi. Teraz głos zabierze pan poseł Krzysztof Paszyk z Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Krzysztof Paszyk",
                    "content": "Bardzo dziękuję. Panie Marszałku! Wysoka Izbo! Mieliśmy dzisiaj nie po raz pierwszy od wczoraj dowód na to, że wedle prawej strony tej sceny najlepsze standardy to są jej standardy. Pozostałe, jakiekolwiek by były, zawsze będą krytykowane, kwestionowane. (Poseł Barbara Bartuś: To chyba o sobie pan mówi.) Panie pośle Czarnek… (Głos z sali: Ministrze.) …pana atakiem na jednego z posłów tej Izby, na pana posła Krzysztofa Śmiszka, pokazał pan, że nie tylko nie ma pan kultury, ale i wiedzy panu brak. (Oklaski) Bo jakby pan wiedzę miał, toby pan wiedział, że każdy mandat w tej Izbie jest jaki? Równy. (Oklaski) (Głos z sali: Brawo!) I wie pan, czego pan nie ma? Jeszcze pan jednej rzeczy nie ma, do której się pan niestety bardzo często odwołuje – religijności w panu za grosz. Gdyby pan był, tak jak pan się z tym obnosi, człowiekiem religijnym, to w życiu by pan wobec drugiego człowieka tak się nie zachował jak przed chwilą z tego miejsca. Nigdy. (Oklaski) (Głos z sali: Faryzeusze.) Wysoka Izbo! Kandydatów zaprezentowanych do Krajowej Rady Sądownictwa można podzielić na dwie grupy. Pierwsza grupa to są ci, którzy wiele zrobili, żeby zniszczyć Krajową Radę Sądownictwa. Od nich zacznę, bo bardzo mało mówimy o skutkach tego niszczycielstwa. Już kilka miliardów złotych kosztowała nie posła, posłankę, ministra PiS-u, tylko państwo polskie, każdego z podatników, działalność tej zepsutej Krajowej Rady Sądownictwa. Ale jest jeszcze jeden negatywny skutek tego, co zrobiliście w ostatnich latach z KRS. Kilkaset tysięcy Polaków, których sprawy w ostatnich latach przed sądami rozstrzygnięto przez sędziów powołanych przez waszą Krajową Radę Sądownictwa, jeszcze bardzo często przez wiele lat nie będzie mogło spać spokojnie, bo ich sprawy niestety będą bardzo łatwe do podważenia. Zrobiliście im wielką krzywdę i myślę, że ci Polacy wam tego przez długie lata nie zapomną. Jest grupa kandydatów, która chce ten KRS naprawiać. Jest wiele do zrobienia i niełatwe zadanie przed nami. Posłowie Gasiuk-Pihowicz, Kropiwnicki, poseł Zimoch czy posłanka Żukowska to są posłowie, którzy chcą naprawiać Krajową Radę Sądownictwa. Klub Parlamentarny Polskiego Stronnictwa Ludowego – Trzecia Droga, który mam przyjemność reprezentować, za tą grupą zagłosuje. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Teraz głos zabierze pan poseł Krzysztof Gawkowski z klubu parlamentarnego Nowej Lewicy.",
                },
                {
                    "speaker": "Poseł Krzysztof Gawkowski",
                    "content": "Panie Marszałku! Wysoka Izbo! Prawo i Sprawiedliwość Krajową Radę Sądownictwa upolityczniło i upodliło, a na czele tej zorganizowanej mafii stał pan Ziobro i to jest dzisiaj jego największa odpowiedzialność, bo odpowiada za ten stan w Polsce. (Oklaski) Panie Ministrze Ziobro! Pan tutaj dzisiaj stanął taki rozedrgany, smutny. Ja pana raz widziałem w takim stanie, też pan po Sejmie taki chodził, jak pan szukał miękiszonów. (Oklaski) Ja panu pokażę, gdzie siedzi. Tutaj. Serdecznie proszę, żeby pan podszedł, porozmawiał. (Oklaski) Druga sprawa, bo pan minister Czarnek tak się przejmuje wyborcami Lewicy. Panie ministrze Czarnek, ja proponuję, żeby pan się zaczął przejmować swoimi kolegami… (Głos z sali: Nie strasz, nie strasz.) …tym, za którą kratą niedługo będzie pan ich szukał… (Poruszenie na sali, część posłów uderza w pulpity) (Głosy z sali: Ooo…) …a nie o wyborców Lewicy się martwił. (Oklaski) Prawo i Sprawiedliwość w mijającej kadencji, która przedwczoraj się zakończyła, było jak dżuma dla Polski. Byliście parlamentarzystami, którzy niszczyli polską konstytucję, którzy nie szanowali regulaminu Sejmu, a Krajową Radę Sądownictwa traktowaliście jak łup polityczny, na którym zarabialiście i nic tam nie robiliście. Pan minister Schreiber – taki oczytany, często tutaj występujący, mówiący o tym, że chciałby porozmawiać. Panie ministrze, mam nadzieję, że pan czytał „Dżumę”, mam nadzieję, przynajmniej tak mi się wydaje. Powinien pan wiedzieć, kiedy pan tutaj opowiadał o pogardzie – o pogardzie, którą kierował w tę stronę – że pogarda to w waszych rękach i w waszym wydaniu było największe zło, z jakim traktowaliście nie nas, parlamentarzystów, ale Polki i Polaków. Przez 8 lat pogarda była w waszych rękach jak młot (Oklaski), który co posiedzenie Sejmu, co posiedzenie rządu uderzał w ludzi, którzy chcieli żyć w Polsce wolnej, bezpiecznej i szanującej konstytucję. Tego nie robiliście. I mam dla pana taki mały cytacik, bo myślę, że pan lubi cytaty, pan tutaj o cesarzach opowiadał. Albert Camus w „Dżumie” powiedział, że rzeczy, które najbardziej trzeba cenić w ludziach, to podziw dla nich, a nie pogarda. Niech pan o tym pamięta i wy wszyscy, koleżanki i koledzy z PiS-u, bo tak o was będę mówił przez 4 lata, pamiętajcie: dzisiaj ta większość, po tej stronie sali, to większość, która chce was szanować, ale pozwalajcie się, panie ministrze Ziobro, szanować. (Głos z sali: Nie kłam!) (Poseł Iwona Ewa Arent: Nie rozśmieszaj nas.) Bo wy nawet się szanować nie pozwalacie. Chcecie z nami dzisiaj dyskutować, to dyskutujcie, ale w powadze, w rozsądku. I pamiętajcie: 4 lata siedzicie w opozycji i tak będziemy was traktowali, jak wy nas traktowaliście. Dzięki. (Głos z sali: Ooo…)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Głos zabierze pan poseł… (Wypowiedź poza mikrofonem) Panie ministrze, zabierał pan głos i marszałek rotacyjny zauważył to. (Oklaski) (Głos z sali: Brawo!) (Minister Edukacji i Nauki Przemysław Czarnek: Panie marszałku, zdanie tylko do tego, co powiedział poseł.) Panie pośle, panie ministrze, nadużywa pan… (Minister Edukacji i Nauki Przemysław Czarnek: Minister zawsze…) Wiem, ale wypowiadał się pan już. (Oklaski) (Minister Edukacji i Nauki Przemysław Czarnek: Bardzo proszę, jedno zdanie.) Jedno zdanie, panie ministrze. Jedno zdanie. (Część posłów skanduje: Regulamin! Regulamin! Regulamin!) Proszę państwa, znam to słowo, nie ma potrzeby skandowania go. Oszczędzajcie gardła na debatę. Proszę bardzo.",
                },
                {
                    "speaker": "Minister Edukacji i Nauki Przemysław Czarnek",
                    "content": "Szanowni Państwo! Ponieważ posłowie bardzo lubią się odnosić do ministra Czarnka w swoich wystąpieniach, panie marszałku, szanowni państwo… (Poseł Krzysztof Gawkowski: Panie ministrze, pan się do nas odnosi.) Otóż, panie pośle Krzysztofie, pan nic nie zrozumiał z tego, co powiedziałem. (Oklaski) To pan poseł Śmiszek powiedział, że pan Ziobro jest wyrzucony z polityki. Więc raz jeszcze przypominam: 7660 tys. mieszkańców to są obywatele Rzeczypospolitej Polskiej, którzy nas do polityki wprowadzili i dali nam mandaty, legalne, bezpośrednie…",
                },
                {"speaker": "Marszałek", "content": "Panie ministrze…"},
                {
                    "speaker": "Minister Edukacji i Nauki Przemysław Czarnek",
                    "content": "Dużo więcej niż wasza Izba. To wyście… Bardzo dziękuję.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Pana definicja jednego zdania jest nieznana polskiej gramatyce. Dziękuję bardzo. (Oklaski) (Wypowiedź poza mikrofonem) Nie, panie ministrze, nie kontynuujemy już tej debaty. (Poseł Bartosz Józef Kownacki: Ale jak to, nie ma w trybie sprostowania.) Teraz proszę o zabranie głosu pana posła Michała Wawra. Uszanujcie państwo to, że przedstawiciel klubu parlamentarnego chce zabrać głos w dyskusji nad ważną dla Polaków sprawą. (Poseł Barbara Bartuś: Niech pan szanuje regulamin.) Panie pośle, bardzo proszę.",
                },
                {
                    "speaker": "Poseł Michał Wawer",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Jeżeli wyborcy liczyli na to, że nowa kadencja przyniesie wyższy poziom debaty na tej sali, to się niestety już drugiego dnia bardzo rozczarowali, i mówię tutaj do obu stron sali. A jeżeli wyborcy liczyli na to, że nowa kadencja przyniesie naprawę wymiaru sprawiedliwości, to patrząc na listę kandydatów do Krajowej Rady Sądownictwa, również się bardzo rozczarowali. Z obu stron – i z PiS-u, i ze zjednoczonego centrolewu – wystawieni zostali kandydaci, którzy są politycznymi awanturnikami, umoczonymi w trwającą od 8 lat wojnę o sądy, skompromitowanymi publicznie, którzy nie dają żadnej rękojmi tego, że będą pracować na rzecz uzdrowienia polskiego wymiaru sprawiedliwości, a wręcz przeciwnie, będą walczyć o wymiar sprawiedliwości jak o zbójeckie łupy rozszarpywane pomiędzy PiS-em a Platformą, o to, kto będzie rządził sądami, które powinny być niezwisłe. (Oklaski) Dzisiaj oglądamy zawłaszczanie Krajowej Rady Sądownictwa, kolejne odcinki to będą Trybunał Konstytucyjny i Sąd Najwyższy. Można już w tej chwili, w dniu dzisiejszym przewidzieć, jak ten serial będzie się rozwijał i jak będzie trwał i że niestety to nie jest ostatnia awantura na tej sali sejmowej. To są wojenki, które nie mają większego znaczenia dla milionów Polaków. Polacy oczekują, że ktoś zrobi coś nie z Krajową Radą Sądownictwa, nie z Trybunałem Konstytucyjnym, oczekują, że ktoś coś zrobi z sądami rejonowymi, gdzie przez długie miesiące i lata nie można się doczekać na wyrok w najprostszej sprawie, gdzie przedsiębiorcy nie mają pewności, że umowy, które zawierają, będą w stanie potem wyegzekwować sądownie. Ja jako radca prawny się z tym zetknąłem w praktyce. Zetknąłem się w praktyce z tym, że na koniec rządów poprzednich Platformy Obywatelskiej stan sądownictwa był fatalny, a na koniec rządów Prawa i Sprawiedliwości stan sądownictwa to jest kompletna ruina. Wy zostawiliście w stanie złym, wy zostawiacie w jeszcze gorszym, a Polacy chcieliby, żeby ktoś przyszedł i naprawił organizację sądownictwa – nie zmienił nominowanych politycznie przedstawicieli na samym szczycie tej struktury (Oklaski), tylko naprawił funkcjonowanie sądów rejonowych, sądów okręgowych. Awanturnicy zgłoszeni dzisiaj do Krajowej Rady Sądownictwa nie pomogą w tej sprawie. Konfederacja będzie głosować przeciwko kandydatom zgłoszonym i z jednej, i z drugiej strony i apelujemy do pozostałych posłów o to samo. Odrzućmy razem te kandydatury. Zwracam się do pana marszałka, żeby po odrzuceniu tych kandydatur zwołać w cywilizowanych, kulturalnych warunkach spotkanie przedstawicieli klubów, na którym będziemy w stanie wybrać takich posłów prawników z naszego grona, którzy niezależnie od przynależności politycznej zostaną przez wszystkich zaakceptowani ponad podziałami i będą w stanie przyjąć jedną, prostą misję: naprawić polskie sądownictwo, a nie zawłaszczać je dla jednej z partii, które tutaj siedzą. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle, i z całego serca podziwiam pana niezachwianą wiarę w człowieka i w polski parlamentaryzm. Do głosu zgłosił się jeszcze minister – członek Rady Ministrów pan Michał Wójcik. Panie Pośle! Panie Ministrze! Bardzo pana proszę o respektowanie czasu, na który umówiliśmy się przy wystąpieniach w czasie tej debaty. Bardzo proszę, panie ministrze.",
                },
                {
                    "speaker": "Minister – Członek Rady Ministrów Michał Wójcik",
                    "content": "Szanowny Panie Marszałku! Szanowni Państwo! Jak pan widzi, nie jest łatwo być marszałkiem Sejmu Rzeczypospolitej Polskiej.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Nie spodziewałem się niczego innego, panie pośle. (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Minister – Członek Rady Ministrów Michał Wójcik",
                    "content": "Chcieliśmy panu pomóc i dlatego wczoraj głosowaliśmy za Elżbietą Witek, bo po prostu była znakomitym marszałkiem przez 4 lata. (Oklaski) I nie było takich sytuacji, panie marszałku, żeby w tak drastyczny sposób łamać regulamin Sejmu. Art. 186 w sposób jednoznaczny mówi, że każdy członek Rady Ministrów ma prawo zabrać głos, kiedy tylko ma ochotę, a pan niestety, ale musi dopuścić te osoby do głosu.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie ministrze, nie podejmując dyskusji z panem, bardzo proszę o zabranie głosu w trybie punktu regulaminu, który pan przywołał. Bardzo proszę.",
                },
                {
                    "speaker": "Minister – Członek Rady Ministrów Michał Wójcik",
                    "content": "Nie byłoby tej dyskusji, gdyby nie pan poseł Borys Budka, który rozgrzał emocje. (Głos z sali: Ha, ha, ha!) Państwo już od wczoraj jak Hunowie wjechaliście do tej Izby, zawłaszczacie wszystko, palicie, niszczycie. I skończycie jak Hunowie, panie przewodniczący. (Oklaski) Skończycie tak samo, zobaczy pan. Pan nie będzie Attylą, zobaczy pan. A jak sobie wyobrażacie wymiar sprawiedliwości, panie pośle Borysie Budka? Otóż przeczytam panu, zacytuję panu pewne zdanie: Sądy dzisiaj, ja ci gwarantuję, nie rozstrzygną żadnej sprawy przed wyborami. Żadnej. Przez rok nie zrobią k… nic. (Głos z sali: Ha, ha, ha!) Będą prowadzić sprawy i ch… Trzy gwiazdki. Tak zapewniał lokalnych działaczy Platformy Obywatelskiej w Tczewie kto? Wasz kolega. Pan Sławek Neumann. Jest? Nie wiem, czy jest. Tak sobie wyobrażacie wymiar sprawiedliwości. Przywołany „sędzia na telefon” – również w waszych czasach. To nie w naszych, to wy chcieliście mieć takich sędziów, a dzisiaj chcecie mieć taką samą Krajową Radę Sądownictwa. Jaką? Szanowni Państwo! Kolesie kolesiów mają wybierać. O to panu chodzi. (Poseł Tomasz Zimoch: A pan ludzi oskarżał…) Nie tak, że… Pan nie szanuje konstytucji, art. 4: zwierzchnia władza należy do narodu. Do narodu. (Oklaski) Proszę się nauczyć konstytucji. (Poseł Jakub Rutnicki: Lekarza.) My zgodnie z tym artykułem przygotowaliśmy ustawę dotyczącą Krajowej Rady Sądownictwa. I taki wybór był dokonany, zgodnie z art. 4, na podstawie systemu hiszpańskiego, Kortezów. (Poseł Mirosław Suchoń: Suweren.) Kiedy się okazało, że przyjechali – oczywiście na wasze zawołanie – przedstawiciele Komisji Weneckiej, to w resorcie sprawiedliwości odbyło się spotkanie i zapytaliśmy wówczas, minister Zbigniew Ziobro zapytał, czym różni się ten system od hiszpańskiego. Wiecie, co powiedzieli eksperci? Wy macie niższą kulturę prawną. Wy czapkujecie wszystkim, zginacie kark. Wy tak naprawdę wycieraliście wycieraczki w różnych stolicach Europy – dzisiaj jest, jak jest. Mogę powiedzieć: Hunowie wjechali do tej Izby. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie ministrze, za tę wypowiedź, pełną erudycji i historycznych refleksji, które podniosły poziom debaty w tej Izbie. Zamykam dyskusję. W związku z tym, że zgłoszono osiem kandydatur na członków Krajowej Rady Sądownictwa, przeprowadzimy głosowanie za pomocą urządzenia do liczenia głosów, wykorzystując funkcję tego urządzenia umożliwiającą dokonanie wyboru z listy. Jestem zobowiązany do przedstawienia państwu zasad głosowania z wykorzystaniem funkcji umożliwiającej dokonanie wyboru z listy. Po zarządzeniu głosowania na wyświetlaczu pojawi się lista z imionami i nazwiskami kandydatur, którą można przesuwać za pomocą pola do przewijania ekranu dotykowego. Aby oddać głos za kandydaturą, należy dotknąć kwadratowego pola celem zaznaczenia wyboru danej kandydatury. Potwierdzenie zaznaczenia pojawi się w kwadratowym polu wyboru. Aby zmienić decyzję, należy ponownie dotknąć pola wyboru, aby odznaczyć, a następnie należy dokonać ponownego wyboru innej kandydatury. Po dokonaniu wyboru należy zatwierdzić swoją decyzję przez naciśnięcie przycisku „zatwierdź i wyślij”. Jest to równoznaczne z ostatecznym oddaniem głosu, a zatem brakiem możliwości zmiany decyzji. Niezaznaczenie żadnej z kandydatur i naciśnięcie przycisku „zatwierdź i wyślij” jest równoznaczne z oddaniem głosu przeciwko wszystkim kandydaturom. – głosowanie Czy wszyscy posłowie są już gotowi do przeprowadzenia głosowania? (Głosy z sali: Tak.) Przechodzimy do głosowania. Zgodnie z art. 31 ust. 1 regulaminu Sejmu Sejm wybiera posłów – członków Krajowej Rady Sądownictwa bezwzględną większością głosów. Przypominam, że na stanowiska członków Krajowej Rady Sądownictwa zgłoszone zostały kandydatury: pana posła Marka Asta, pani poseł Kamili Gasiuk-Pihowicz, pana posła Bartosza Kownackiego, pana posła Roberta Kropiwnickiego, pana posła Arkadiusza Mularczyka, pana posła Kazimierza Smolińskiego, pana posła Tomasza Zimocha oraz pani poseł Anny Marii Żukowskiej. Po rozpoczęciu głosowania lista w kolejności alfabetycznej zostanie umieszczona w czytniku urządzenia do liczenia głosów. Przypominam, że poprzeć można tylko cztery kandydatury. Ponownie przypominam paniom i panom posłom, że naciśnięcie przycisku „zatwierdź i wyślij” jest równoznaczne z ostatecznym podjęciem decyzji, zatem proszę, aby tego przycisku użyć jako ostatniego. Przystępujemy do głosowania. Proszę obecnie panie i panów posłów o podejmowanie decyzji w sprawie wyboru posłów – członków Krajowej Rady Sądownictwa. Czy wszyscy państwo podjęli już decyzję? (Głos z sali: Tak.) Dziękuję bardzo. Proszę o wyświetlenie wyników. W głosowaniu wzięło udział 457 posłów. Większość bezwzględna wynosiła 229 posłów. (Oklaski) Pani poseł Kamila Gasiuk-Pihowicz uzyskała 246 głosów, pan Tomasz Zimoch uzyskał 246 głosów, pani Anna Maria Żukowska uzyskała 245 głosów, pan Robert Kropiwnicki uzyskał 243 głosy, pan Marek Ast – 193 głosy, pan Arkadiusz Mularczyk – 192 głosy, pan poseł Kazimierz Smoliński – 192 głosy, pan Bartosz Józef Kownacki uzyskał 191 głosów. (Oklaski) Stwierdzam, że Sejm bezwzględną większością głosów wybrał posłów: Kamilę Gasiuk-Pihowicz, Roberta Kropiwnickiego, Tomasza Zimocha i Annę Marię Żukowską na stanowiska członków Krajowej Rady Sądownictwa. (Oklaski) Drodzy Państwo! Na tym zakończyliśmy rozpatrywanie punktów porządku dziennego zaplanowanych na dzień 14 listopada. Zarządzam przerwę w posiedzeniu. Zanim ją zarządzę, mam jeszcze jedną uwagę i prośbę do państwa oraz komentarz po tym, co wydarzyło się dziś na tej sali. Mikrofony na sali sejmowej zbierają wypowiedzi tylko tych, którzy przemawiają. Chciałbym, żeby Polki i Polacy, którzy śledzą obrady Sejmu, wiedzieli, że dzisiaj na tej sali w mojej ocenie – myślę, że też w ocenie wielu z nas – przekroczone zostały standardy demokratycznej debaty. (Oklaski) Chcę państwa zapewnić, że jako marszałek Sejmu nigdy nie będę okazywał państwu niczego innego niż szacunek i poważanie dla mandatu, który państwo otrzymali od obywateli. Natomiast gorąco zachęcam państwa do tego, żeby pogarda, nienawiść, agresja i okrzyki takie jak: puknij się w głowę, które dzisiaj słyszeliśmy na tej sali, nigdy więcej na niej nie gościły, bo są policzkiem wymierzonym tym, którzy poszli na wybory 15 października tego roku. (Oklaski) Zarządzam przerwę w posiedzeniu do dnia 21 listopada, czyli do wtorku, do godz. 12. Bardzo proszę państwa posłów o to, żebyście nie zapomnieli o zabraniu waszych legitymacji poselskich z czytników. Przypominam o pierwszym posiedzeniu komisji regulaminowej i spraw poselskich za 15 minut w sali nr 13 w budynku G. Dziękuję państwu.",
                },
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
        self.assertEqual(obj["speaker_senior"], None)
        self.assertEqual(obj["speaker"], "Szymon Hołownia")
        self.assertEqual(obj["vicespeakers"], [])
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
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 9. porządku dziennego: Wybór składu osobowego Komisji do Spraw Unii Europejskiej",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 10. porządku dziennego: Wybór składu osobowego Komisji Etyki Poselskiej",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
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
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
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
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
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
        self.assertEqual(
            obj["text"],
            [
                {
                    "speaker": "Marszałek",
                    "content": "Wznawiam posiedzenie. Szanowni Państwo! Chcę poinformować… (Wypowiedź poza mikrofonem) Proszę się zgłosić, wnioski formalne są już zarejestrowane, więc rozumiem, że pan poseł będzie miał kolejny wniosek. Przed wejściem w punkt, po odczytaniu wszystkich formalności udzielę państwu głosu. (Wypowiedź poza mikrofonem) Tak, wiem, tylko odczytam najpierw informacje związane z sekretarzami i przed rozpoczęciem punktu będziecie państwo mogli złożyć wniosek formalny. Szanowni Państwo! Chcę państwa poinformować, choć pewnie już to wiecie ze swoich klubów, że nadałem numery druków wszystkim projektom obywatelskim, które przeszły przez proces dyskontynuacji, a wszystkie projekty ustaw i uchwał wniesione do tej pory przez państwa kluby rozpoczną swój bieg od analiz, a następnie będą procedowane zgodnie ze sztuką przyjętą w tym Sejmie. Na sekretarzy dzisiejszych obrad powołuję posłów Aleksandrę Karolinę Wiśniewską oraz Adama Michała Gomołę. Protokół i listę mówców prowadzić będzie pani poseł Aleksandra Karolina Wiśniewska. Prezydium Sejmu przedłożyło wnioski w sprawie: — wyboru składów osobowych komisji sejmowych, druk nr 20, — wyboru składu osobowego Komisji do Spraw Unii Europejskiej, druk nr 21, — wyboru składu osobowego Komisji Etyki Poselskiej, druk nr 22, — wyboru składu osobowego Komisji do Spraw Służb Specjalnych, druk nr 23. W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o punkty obejmujące rozpatrzenie tych wniosków. Grupy posłów przedłożyły wnioski w sprawie wyboru członków Trybunału Stanu, druki nr 34–51. W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o punkt obejmujący rozpatrzenie tych wniosków. Proponuję, aby w tych przypadkach Sejm wyraził zgodę na skrócenie terminu, o którym mowa w art. 30 ust. 4 regulaminu Sejmu, oraz rozpatrzył wnioski bez przesyłania ich do właściwej komisji. Jeśli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycje przyjął. Sprzeciwu nie słyszę. (Poseł Barbara Bartuś: Sprzeciw.) Grupa obywateli… (Poseł Barbara Bartuś: Sprzeciw.) Sprzeciw? Nie słyszałem pani poseł, bardzo przepraszam. (Poseł Barbara Bartuś: Żeby skrócić czas.) Czyli sprzeciwia się pani temu, żeby Sejm odstąpił od terminu, o którym mowa w art. 30 ust. 4 regulaminu Sejmu. (Poseł Barbara Bartuś: Dokładnie.) W związku ze zgłoszonym sprzeciwem sprawę tę rozstrzygniemy w głosowaniu. Przystępujemy do głosowania. Kto z pań i panów posłów jest za wyrażeniem zgody na skrócenie terminu, o którym mowa w art. 30 ust. 4 regulaminu Sejmu, oraz na rozpatrzenie wniosków bez przesyłania ich do właściwej komisji, zechce podnieść rękę i nacisnąć przycisk. (Głos z sali: Nie działa.) Nam też nie działa. Zaraz, mam nadzieję, zadziała. Działa, a więc głosujemy. Kto jest za? Kto jest przeciw? Kto się wstrzymał? Głosowało 448 posłów. 243 – za, 188 – przeciw, 17 się wstrzymało. Stwierdzam, że Sejm przyjął propozycję skrócenia terminu, o którym mowa w art. 30 ust. 4 regulaminu Sejmu, i zgodził się na rozpatrzenie wniosków bez przesyłania ich do właściwej komisji. Grupa obywateli przedłożyła projekt ustawy o zmianie ustawy o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych, druk nr 31, chodzi o ustawę w sprawie procedury in vitro.  W związku z tym, po uzyskaniu jednolitej opinii Konwentu Seniorów, podjąłem decyzję o uzupełnieniu porządku dziennego o punkt obejmujący pierwsze czytanie tego projektu. Proponuję, aby w tym przypadku Sejm wyraził zgodę na skrócenie terminu, o którym mowa w art. 37 ust. 4 regulaminu Sejmu, oraz w dyskusji nad tym punktem porządku dziennego wysłuchał 10-minutowych oświadczeń w imieniu klubów i 5-minutowych oświadczeń w imieniu koła. Jeżeli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycje przyjął. (Poseł Grzegorz Braun: Sprzeciw.) Słyszę sprzeciw, a więc przystępujemy do głosowania. (Głos z sali: Ooo…) Kto z pań i panów posłów jest za wyrażeniem zgody na skrócenie terminu, o którym mowa w art. 37 ust. 4 regulaminu Sejmu, oraz na wysłuchanie 10-minutowych oświadczeń w imieniu klubów i 5-minutowych oświadczeń w imieniu koła w dyskusji nad tym punktem porządku dziennego, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? (Głos z sali: Nie działa.) Działa? Kto się wstrzymał? Głosowało 453 posłów. 247 – za, 206 – przeciw, nikt się nie wstrzymał. Stwierdzam, że Sejm zgodził się na skrócenie terminu, o którym mowa w art. 37 ust. 4 regulaminu Sejmu, oraz na wysłuchanie 10-minutowych oświadczeń w imieniu klubów i 5-minutowych oświadczeń w imieniu koła w dyskusji nad tym punktem porządku dziennego. Przed wejściem w punkt 8. porządku dziennego – wnioski formalne. (Poseł Joanna Lichocka: Proszę mówić po polsku: zajmujemy się punktem.) Zgłosiły się trzy osoby do wniosków formalnych. Jako pierwszy pan poseł Stefan Krajewski z Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Stefan Krajewski",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Narasta kryzys na granicy polsko-ukraińskiej, gdzie protestują polscy przewoźnicy. Polski rząd zgodził się w Brukseli na to, żeby nie rozwiązać problemów polskich rolników ze zbożem, które napływało, i zgodził się na to, żeby poprzeć umowę z Ukrainą, która znosiła zezwolenia dla ukraińskich przewoźników, co jest dzisiaj źródłem tego problemu. Wnoszę o przerwę i przekazanie informacji właściwego ministra, który poparł rozwiązania uderzające w polską gospodarkę. Słyszymy, że rząd działa, ministrowie działają, chyba to nie polega na oglądaniu Netfliksa i pakowaniu kuwet. Trzeba działać, rozwiązać problem. Nie broniliście polskich rolników, nie bronicie polskich przewoźników. Zróbcie coś jeszcze z tym. (Dzwonek) Myślę, że pan premier Morawiecki działa. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Rozumiem, że pan poseł zgłosił wniosek formalny o przerwę. (Poseł Stefan Krajewski: Tak.) W takim razie musimy ten wniosek… (Poseł Łukasz Schreiber: Jest głos przeciw.) (Poseł Andrzej Adamczyk: Chciałbym odpowiedzieć…) Przepraszam? (Poseł Andrzej Adamczyk: Chciałbym odpowiedzieć, odnieść się do…) Rozumiem, że pan się… (Wypowiedź poza mikrofonem) Ja to wiem, oczywiście, przecież zdaję sobie z tego sprawę. Natomiast chciałbym, żebyśmy przegłosowali wniosek pana posła. (Poseł Andrzej Adamczyk: Przed głosowaniem…) (Głos z sali: Sprzeciw.) Zachęcam do tego, żeby poważnie potraktować wniosek formalny pana posła, przegłosować go, a następnie udzielę panu głosu, dobrze? (Poseł Andrzej Adamczyk: Ale to jest głos przeciw.) (Poseł Bożena Borys-Szopa: Ale jest głos przeciw.) (Poseł Łukasz Schreiber: Głos przeciw.) Głos przeciw wnioskowi formalnemu? Proszę bardzo, proszę bardzo.",
                },
                {
                    "speaker": "Poseł Andrzej Adamczyk",
                    "content": "Dziękuję bardzo. Panie i Panowie! Wysoki Sejmie! Panie Marszałku! Pragnę odpowiedzieć nie tylko panu posłowi, ale też grupie parlamentarzystów, szczególnie z Koalicji Obywatelskiej, będącej w koalicji: otóż decyzja Komisji Europejskiej, aby to Unia Europejska podpisała umowę z Ukrainą, zapadła niezależnie od naszych opinii, bo takich nie zasięgano. Unia Europejska niezależnie podpisała z Ukrainą umowę, na podstawie której czasowo zawieszono obowiązek… Unia Europejska podpisała tę umowę z Ukrainą. Jeszcze raz powtarzam, Unia Europejska podpisała tę umowę z Ukrainą… (Głos z sali: A co pan robił?) …bo tak działa ten system, w którym oddajemy powoli naszą suwerenność, a teraz będziemy oddawali ją bardzo szybko. (Dzwonek) (Głos z sali: Nie.) (Głos z sali: Popieraliście to.) (Głos z sali: Nieprawda.) (Poseł Witold Tumanowicz: Sprzeciw, był z waszej strony sprzeciw?) Otóż została podpisana umowa, na skutek której został zawieszony obowiązek posiadania zezwoleń przez transportowców z Ukrainy, którzy wjeżdżają do Polski. Do momentu podpisania tej umowy obowiązywały zezwolenia, które symetrycznie pozwalały realizować kontrakty przewozowe przez polskich przedsiębiorców na Ukrainie i ukraińskich przedsiębiorców w Polsce.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, przekroczył pan czas wypowiedzi o pół minuty. (Głos z sali: Jako minister.) Nie, pan poseł, wchodząc na mównicę, wyraźnie powiedział, że występuje jako poseł w odpowiedzi na wniosek formalny. (Głos z sali: Proszę nie przerywać.)",
                },
                {
                    "speaker": "Poseł Andrzej Adamczyk",
                    "content": "To zostało złamane i to jest podstawą protestu polskich przewoźników, którzy blokują dzisiaj granicę.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Czas odpowiedzi na wniosek formalny wynosi 1 minutę. Pan poseł przemawia niespełna 2 minuty.",
                },
                {
                    "speaker": "Poseł Andrzej Adamczyk",
                    "content": "Drugim z elementów jest decyzja władz Ukrainy.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Ma pan jeszcze 30 sekund, panie pośle, zanim wyłączę panu mikrofon.",
                },
                {
                    "speaker": "Poseł Andrzej Adamczyk",
                    "content": "Ukraińcy jednostronnie wprowadzili zmiany na drogach dojazdowych do granicy i na samej granicy po stronie ukraińskiej, co powoduje, że polscy przedsiębiorcy stoją w kolejkach kilka, kilkanaście dni. (Głos z sali: Siadaj już.) (Poseł Witold Tumanowicz: Hipokryta. Siadaj.) I to jest powodem protestu, a nie decyzje polskiego rządu, a nie decyzje ministra infrastruktury i pana premiera Mateusza Morawieckiego. Trzeba spowodować, aby Komisja Europejska, wbrew temu, co jej wysoki przedstawiciel powiedział jeszcze w ubiegłym tygodniu w Dorohusku na spotkaniu z przedstawicielami rządu… (Marszałek wyłącza mikrofon, poseł przemawia przy wyłączonym mikrofonie, oklaski) (Poseł Barbara Bartuś: Ale minister na temat się wypowiada.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Przypomnę państwu odnośny punkt regulaminu. Art. 184 regulaminu Sejmu, jego pkt 5: Sejm rozstrzyga o wniosku formalnym po wysłuchaniu wnioskodawcy i ewentualnie jednego przeciwnika wniosku. Pkt 8 tego… (Poseł Barbara Bartuś: Ale to pan minister się wypowiadał na temat.) Nie, pan wyraźnie stwierdził, że jest posłem, wypowiada się jako poseł. Wystąpienia poza porządkiem dziennym, w tym zgłoszenie wniosku formalnego, nie mogą trwać dłużej niż 2 minuty, z wyjątkiem sprostowań, które nie mogą trwać dłużej niż 1 minutę. Panie pośle Suski, w jakim trybie znalazł się pan przed obliczem Wysokiej Izby? (Oklaski) (Głos z sali: Bez trybu.) Ta obecność mnie cieszy, natomiast został zgłoszony wniosek formalny. Jak pan się pewnie orientuje, wystąpił już jeden z posłów jako przeciwnik tego wniosku formalnego. (Poseł Stanisław Tyszka: Głosujemy.) W jakim trybie chce pan wystąpić, panie pośle Marku Suski? (Poseł Marek Suski: Wystąpił pan minister…) (Głos z sali: Z przyzwyczajenia.) (Głos z sali: Ha, ha, ha!) Przyzwyczajenie drugą naturą człowieka. Wszystko to jasne. Bardzo dobrze. (Głos z sali: Głosujemy.) (Głos z sali: Głosowanie. Głosowanie.) Pan poseł w jasny sposób zawiadomił mnie, iż występuje tutaj, na mównicy, jako poseł i zgłosił sprzeciw wobec wniosku formalnego. Poddaję pod głosowanie wniosek formalny o przerwę w obradach. (Poseł Barbara Bartuś: Łamie pan regulamin.) (Poseł Marek Suski: To skandal! Marszałek łamie regulamin!) (Oklaski) Przystępujemy do głosowania. Kto z pań i panów posłów jest za zarządzeniem przerwy w obradach, zechce podnieść rękę i nacisnąć przycisk. Przypomnę państwu, jeżeli ktoś z państwa się zagubił: otóż głosujemy nad wnioskiem o przerwę w obradach, o zarządzenie przerwy w obradach. Kto jest przeciw? Kto się wstrzymał? Głosowało 456 posłów. 237 – za, 10 – przeciw, 209 się wstrzymało. (Oklaski) (Głos z sali: Ha, ha, ha!) W tej sytuacji ogłaszam przerwę w obradach zgodnie z wnioskiem pana posła Stefana Krajewskiego i rozumiem, że po tej przerwie… (Głos z sali: Do jutra.) (Poseł Piotr Kaleta: Jak długo?) (Głos z sali: Do której?) Minuta przerwy. (Oklaski) (Głos z sali: Ha, ha, ha!) A po tej przerwie… Panie ministrze, panie pośle, czym mogę panu służyć? (Głos z sali: Ha, ha, ha!) (Poseł Andrzej Adamczyk: Proszę o sprostowanie… Jako minister konstytucyjny, ale również jako poseł, ale przede wszystkim jako minister konstytucyjny mam prawo do tego, żeby w każdym czasie zabrać głos, a szczególnie w sprawach, które tu zostały poruszone. I proszę pana marszałka, żeby pan tej zasady przestrzegał.) Tak. Bardzo serdecznie dziękuję, panie pośle, panie ministrze. (Głos z sali: Przerwa.) Widzę w bardzo jasny sposób, że zamierzają państwo kontynuować procedurę, którą rozpoczęliście na poprzednim posiedzeniu tej Izby, czyli nadużywania art. 186 regulaminu Sejmu… (Poseł Barbara Bartuś: Co to znaczy: nadużywania?) (Głos z sali: Regulamin, regulamin.) …w sprawie której jest już uchwała Prezydium Sejmu. Zasięgnąłem opinii nie pięciu, ale trzech prawników, którzy w jasny sposób dają do zrozumienia, jak przepis ten powinien być interpretowany. (Oklaski) (Poseł Marek Suski: Pan nie zna tej uchwały, jeżeli pan twierdzi, że może pan nie udzielić ministrowi głosu…) (Głos z sali: Przerwa jest.) Panie pośle Suski, teraz jest przerwa. (Głos z sali: Ha, ha, ha!) Rozmawiamy, to miłe… (Poseł Marek Suski: Na posiedzeniu komisji regulaminowej…)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Wznawiam obrady. (Wesołość na sali) (Głos z sali: Ha, ha, ha!) Drodzy Państwo! To nie ja, ale to wy przed obliczem milionów Polek i Polaków dzisiaj pokazujecie, jak wygląda parlamentaryzm. Następny do zgłoszenia wniosku formalnego zapisał się pan poseł Michał Wawer z Konfederacji. Bardzo proszę, panie pośle. (Poseł Bożena Borys-Szopa: Po przerwie miało być wyjaśnienie ministra.) (Wypowiedź poza mikrofonem) Ale czy ja mam z tym jakiś kłopot? Absolutnie nie, panie pośle. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Michał Wawer",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Piękne jest to obserwowanie, jak PiS z PSL-em przerzucają się odpowiedzialnością za to, co się dzieje na granicy i co się dzieje w polskiej gospodarce. Ja przypominam, że 19 maja 2022 r. w Parlamencie Europejskim wszystkie obecne tu partie poza Konfederacją zagłosowały za otwarciem granic Unii na ukraińską gospodarkę, na ukraiński transport. (Oklaski) (Poseł Stanisław Tyszka: Tak jest! Brawo!) Lewica, Platforma, PSL i PiS. (Głos z sali: Hańba!) Szanowni Państwo! My mamy nadal rząd Mateusza Morawieckiego. Przypominam siedzącym tutaj, na tej sali, ministrom, wiceministrom, panu premierowi, że nadal pełnicie funkcje, i w tym czasie, kiedy my tu siedzimy i dzielimy sobie funkcje w komisjach, polscy transportowcy na granicy kolejny tydzień marzną, głodują, zmagają się z groźbami przemocy fizycznej ze strony Ukraińców. (Głos z sali: Hańba!) Składam więc wniosek formalny, żeby ministrowie, wiceministrowie przestali się bawić w okupowanie mównicy i wzięli się do roboty, żeby wesprzeć polską branżę transportową. Dziękuję. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Kolejny wniosek formalny zgłosił pan poseł Paweł Jabłoński. Jeśli tylko można, panie pośle, gwoli informacji, bo jej przepływ czasami ze względu na intensywność obrad bywa utrudniony, pański wniosek dotyczy poselskiego projektu uchwały w sprawie zatrzymania niebezpiecznych dla Rzeczypospolitej Polskiej zmian Traktatu o Unii Europejskiej oraz Traktatu o funkcjonowaniu Unii Europejskiej. Chcę poinformować pana posła, że ten projekt zostanie skierowany czy został już przeze mnie skierowany do rozpatrzenia w Komisji do Spraw Europejskich w ramach pierwszego czytania tej uchwały. Oczywiste jest to, że musimy poczekać, aż ukonstytuuje się dzisiaj komisja do spraw europejskich, która nad tym projektem będzie procedować. Oczywiście może pan złożyć wniosek formalny, natomiast chciałem, żeby miał pan pełny stan wiedzy w sprawie",
                },
                {
                    "speaker": "Poseł Paweł Jabłoński",
                    "content": "Dziękuję, panie marszałku. Wysoka Izbo! Ja znam te informacje, słuchałem konferencji pana marszałka, na której pan marszałek stwierdził, za co jestem wdzięczny, że to jest projekt niezwykle ważny. Cytuję to, co pan marszałek powiedział, i cieszę się, że się w tej sprawie zgadzamy, bo to, co dzieje się w tej chwili, a w zasadzie co wydarzy się w ciągu niecałych 24 godzin w Parlamencie Europejskim, to jest sprawa niezwykle ważna. Będzie głosowanie nad pakietem 267 poprawek, które w radykalny sposób – to nie są moje słowa, to jest cytat ze strony Parlamentu Europejskiego – zmieniają Unię Europejską z organizacji suwerennych, współpracujących ze sobą, ale odrębnych od siebie państw w twór, który będzie zarządzany centralistycznie. I zdaniem posłów Prawa i Sprawiedliwości kluczowe jest to, żeby dzisiaj zwrócić się z apelem do wszystkich polskich europosłów, żeby się temu sprzeciwili. Ten projekt został przygotowany w Komisji Spraw Konstytucyjnych. Tam było pięciu europosłów, z tego czterech to byli europosłowie z Niemiec. Ja nie mam pretensji do polityków niemieckich, że reprezentują interesy Niemiec. (Dzwonek) Bardzo dobrze, że reprezentują interesy swojego kraju. Europosłowie z Polski powinni reprezentować interesy polskie, a Sejm Rzeczypospolitej Polskiej w tej sprawie nie może milczeć, nie może być Sejmem niemym. Panie marszałku, jeszcze jedna rzecz, bo nasi obywatele może nie do końca o tym wiedzą. Dzisiaj obrady Sejmu zostały wyznaczone od godz. 12 do godz. 14.30. Mówił pan dzisiaj rano na konferencji prasowej, że Sejm pracuje 24 godziny na dobę. Apeluję, żebyśmy w tej sprawie, w przypadku której rzeczywiście w ciągu 24 godzin dojdzie do kluczowego głosowania w Parlamencie Europejskim, przyspieszyli. (Oklaski) Dlatego składam wniosek o szybkie nadanie numeru druku i procedowanie nad tym nie na posiedzeniu komisji, panie marszałku, ale na posiedzeniu plenarnym. To jest zbyt ważna sprawa. Apeluję o to, żebyśmy uzupełnili porządek obrad o rozpatrzenie tej uchwały. Bardzo dziękuję. (Oklaski) (Głos z sali: Do roboty.) (Poseł Konrad Berkowicz: Wniosek przeciwny.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Wniosek przeciwny. Bardzo proszę. (Poseł Maciej Konieczny: Panie marszałku…) A, przepraszam, nie zauważyłem. Za chwilę dopuszczę pana posła. Przepraszam.",
                },
                {
                    "speaker": "Poseł Konrad Berkowicz",
                    "content": "Wniosek sam w sobie jest dobry, ale śmieszne jest to, że składa go ktoś z Prawa i Sprawiedliwości, które rządzi od 8 lat i prowadziło, poza machaniem szabelką, politykę całkowitej uległości wobec Unii Europejskiej. (Oklaski) (Poseł Stanisław Tyszka: Tak jest!) To premier Mateusz Morawiecki jeździł do Unii Europejskiej lobbować, żeby Unia Europejska mogła nakładać na nas podatki. To premier Morawiecki nie złożył weta, do czego miał prawo, podczas uchwalania Fit for 55. (Poseł Stanisław Tyszka: Hańba!) To premier Morawiecki nie zgłosił sprzeciwu wobec zakazu samochodów spalinowych na szczycie klimatycznym. Jesteście hipokrytami i tylko Konfederacja jest w stanie przywrócić Polsce suwerenność. Dziękuję bardzo. (Oklaski) (Głos z sali: Brawo!) (Głos z sali: Ha, ha, ha!) (Głos z sali: Słowa prawdy.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Pan poseł Maciej Konieczny z Lewicy. (Wypowiedź poza mikrofonem) Tak, za chwilę już, przepraszam.",
                },
                {
                    "speaker": "Poseł Maciej Konieczny",
                    "content": "Przede wszystkim warto zgłosić sprzeciw wobec identyfikowania… (Poseł Barbara Bartuś: A to powiedz „sprzeciw”.) …interesu polskiego, interesu Polski jako sprzecznego z integracją europejską. (Oklaski) To jest wbrew woli ogromnej większości Polaków, którzy życzą sobie integracji europejskiej, naszej obecności w Europie i sprawnej Europy. (Poseł Barbara Bartuś: Ale my jesteśmy w Europie.) Europa wymaga reform, Europa musi być sprawna na arenie międzynarodowej, Europa musi skutecznie konkurować z innymi centrami na arenie globalnej, takimi jak chociażby Chiny. Do tego wymagany jest namysł i bardzo rozsądna reforma Unii Europejskiej w celu usprawnienia także procesów decyzyjnych. I powinniśmy dzisiaj zastanawiać się nad tym, jak to zrobić, żeby działo się to w interesie Polski. Bo w interesie Polski jest dalsza integracja europejska, w interesie Polski jest silna Europa, a przeciwko interesowi Polski działają ci, którzy osłabiają Europę, bo oni działają na rzecz innych centrów, takich jak chociażby Chiny. (Oklaski) (Poseł Barbara Bartuś: Interesem Polski jest silna Polska.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. W tej chwili udzielę głosu panu ministrowi Szymonowi Szynkowskiemu vel Sękowi z jednym zastrzeżeniem. Bardzo się cieszę, że będę mógł po raz pierwszy zastosować w praktyce wykładnię, której dokonało Prezydium Sejmu. (Głos z sali: Ooo…) (Poseł Barbara Bartuś: Ale jeszcze nie została przyjęta.) Projekt wykładni Prezydium Sejmu, który mówi bardzo wyraźnie i jasno o tym, że art. 186 rzeczywiście umożliwia członkom Rady Ministrów zabieranie głosu w czasie posiedzenia Sejmu w obszarach, które dotyczą ich kompetencji. Ta dyskusja, która tu się toczy, dotyczy kompetencji pana ministra Szynkowskiego vel Sęka. W związku z powyższym proszę go teraz o zabranie głosu. (Poseł Robert Kropiwnicki: To są wnioski formalne, nie debata.) Mam również bardzo interesującą w zakresie możliwości marszałka, jeżeli oczywiście państwo zechcą uznać to za głos w jakiś sposób was wiążący, wypowiedź pana ministra Michała Wójcika – zacytuję ją, jeśli pozwolicie – jeżeli Prezydium Sejmu nie jest tutaj dostatecznie kompetentne: Ja również rozmawiałem z panią marszałek, tak samo jak i z panem marszałkiem Terleckim, i chcę powiedzieć, że nic nadzwyczajnego w tym nie widzę. Wielokrotnie zdarza się tak w trakcie debat sejmowych, sam tego doświadczyłem nawet jako minister konstytucyjny, że nie byłem dopuszczany, dlatego że marszałkowie decydują o porządku na sali obrad, więc decydują, kto może zabrać głos, a kto nie. (Oklaski) (Głos z sali: Brawo!) Ta wykładnia, powiedziałbym, zwyczajowa, dokonana przez pana Michała Wójcika jest mi bliska i, korzystając z niej, chciałbym prosić pana ministra o zabranie głosu.",
                },
                {
                    "speaker": "Minister do Spraw Unii Europejskiej Szymon Szynkowski vel Sęk",
                    "content": "Dziękuję, panie marszałku. Wydaje mi się, że pan marszałek mówił o wprowadzaniu nowego standardu parlamentaryzmu, a teraz odwołuje się do wypowiedzi ministrów rządu Prawa i Sprawiedliwości. To oczywiście dobry kierunek, żeby odwoływać się do wypowiedzi ministrów naszego rządu, natomiast chcielibyśmy, żeby był po prostu szanowany regulamin (Oklaski) i tego oczekujemy: sprawiedliwego stosowania i szanowania regulaminu. Natomiast ja wypowiem się rzeczywiście w sprawie fundamentalnej wagi, Wysoka Izbo. (Poseł Robert Kropiwnicki: To są wnioski formalne.) Wystąpię w sprawie fundamentalnej wagi, nie z wnioskiem formalnym, jako minister do spraw Unii Europejskiej… (Głos z sali: Ale nie ma debaty.) …w sprawie zmian traktatów, które w tej chwili są procedowane w Parlamencie Europejskim, bo uważam, że jestem winny Wysokiej Izbie wyjaśnienie, jak ważne są to kwestie i jak fundamentalnych z punktu widzenia suwerenności naszego kraju tematów dotyczą. Komisja Spraw Konstytucyjnych Parlamentu Europejskiego przyjęła pakiet zmian. Propozycji tych zmian jest rzeczywiście bardzo wiele. Jutro o godz. 12 te propozycje będą przedmiotem głosowania całej izby w Parlamencie Europejskim. Dlatego właśnie klub Prawa i Sprawiedliwości zaproponował, żeby jeszcze dzisiaj Wysoka Izba, Sejm mógł się w tej sprawie wypowiedzieć, bo jest ona bardzo ważna. W tej sprawie wypowiedziała się Rada Ministrów. Rada Ministrów przyjęła na dzisiejszym posiedzeniu uchwałę, w której odnosi się krytycznie do zmian proponowanych i procedowanych w Parlamencie Europejskim z kilku względów. Po pierwsze, te zmiany w szeregu dziedzin przenoszą kompetencje narodowe, kompetencje krajów członkowskich na poziom kompetencji unijnych. W tak ważnych dziedzinach jak ochrona środowiska, polityka klimatyczna, bioróżnorodność te kompetencje stają się kompetencjami wyłącznymi Unii Europejskiej. Co to oznacza? Oznacza to nie tylko to, że w tych zakresach Polska nie będzie miała uprawnień do stanowienia przepisów, decydowania, bo te kompetencje będą leżały po stronie Unii Europejskiej, ale także np. to, że Polska jako kraj nie będzie uprawniona do zawierania zewnętrznych umów międzynarodowych. Takie umowy w imieniu naszego kraju będzie zawierała Unia Europejska. Nie muszę dzisiaj pewnie nikomu, mam nadzieję, tłumaczyć, na jak wiele elementów wpływa polityka klimatyczna, polityka dotycząca ochrony środowiska czy elementów np. konkurencyjności gospodarczej, a także tego, czy będziemy w stanie bronić naszej gospodarki przed zakusami, żeby ograniczyć jej konkurencyjność. Wiemy, że przepisy regulacyjne z zakresu polityki klimatycznej niestety bardzo często stanowią brzemię dla naszej gospodarki. Wystarczy tylko powiedzieć, że w Polsce działanie systemu ETS, systemu handlu emisjami, wpływa na 50% ogólnej ceny prądu, w Unii Europejskiej – przeciętnie na 20%, bo nasz kraj ma taką, a nie inną, historię także w zakresie miksu energetycznego i takie, a nie inne, możliwości ewolucyjnej zmiany tegoż miksu energetycznego. (Poseł Grzegorz Braun: Teraz o tym mówicie?) Ale jeżeli mówimy o miksie energetycznym, to chodzi tu o kolejną dziedzinę, gdzie Unia Europejska będzie miała uprawnienia, tzw. kompetencje dzielone, będzie miała wpływ na to, jak kraje konstruują swój miks energetyczny. Co to oznacza? To może oznaczać dla przeciętnego obywatela tyle, że nałożone przez Unię Europejską na gospodarkę, na przemysł wymogi spowodują, że cena energii w przypadku końcowego konsumenta, przedsiębiorcy, ale także po prostu osoby prywatnej, może wzrosnąć dwu- czy trzykrotnie, a my nie będziemy mieli nad tym żadnej kontroli. Nie będziemy mieli na to wpływu, nie będziemy w stanie bronić obywateli przed tymi drastycznymi podwyżkami cen energii. (Poseł Grzegorz Braun: Mieliście ten wpływ i nie skorzystaliście.) Wreszcie inne sprawy: obrona granicy. Obrona granic to również kompetencja przenoszona do kompetencji dzielonych Unii Europejskiej. Czy muszę tłumaczyć, jak fundamentalna, związana z suwerennością jest to sprawa? Czy muszę państwu tłumaczyć, że jest to immanentna cecha suwerenności danego państwa, szczególnie ważna w warunkach geopolitycznej niestabilności? To miałoby być zgodnie z tymi propozycjami przeniesione również w sferę kompetencji dzielonych Unii Europejskiej. Wieloletnie ramy finansowe. O wieloletnich ramach finansowych decydowano by nie jednomyślnie, a nawet nie w wyniku uzyskania większości kwalifikowanej, ale w wyniku uzyskania zwykłej większości głosów. Czy muszę państwu wyjaśniać, jaki miałoby to wpływ na uwzględnianie interesów poszczególnych krajów członkowskich? (Poseł Mirosław Suchoń: Nie, nie wyjaśniaj.) Myślę, że tego wyjaśniać państwu nie trzeba. Kolejne kwestie: polityka zagraniczna, polityka obronna – to są kompetencje przechodzące w sferę kompetencji dzielonych. Kompetencje z dziedziny zdrowia także przechodzą w sferę kompetencji dzielonych. Co oznacza to, że kompetencje są dzielone? To znaczy, że jakaś dziedzina może podlegać albo kompetencjom Unii, albo kompetencjom państw członkowskich, ale jeżeli choć raz Unia wykona uprawnienia w konkretnym zakresie kompetencyjnym, państwa członkowskie nie mają już wstępu na to pole, które zostało zajęte przez Unię. A jest dość oczywiste, że Unia, znana przecież z chęci regulowania wielu dziedzin, te pola kompetencyjne bardzo szybko zajmie. I to tylko jeden z aspektów niebezpieczeństwa, na jakie chciałem Wysokiej Izbie zwrócić uwagę. Drugi aspekt związany jest z przeniesieniem, jeśli chodzi o poziom wymogów dotyczących głosowania. Wiele obszarów strategicznych, gdzie dzisiaj wymagane są decyzje podejmowane jednomyślnie, jest przenoszonych na poziom podejmowania decyzji większością kwalifikowaną bądź większością zwykłą. Większość zwykła, czyli państwa reprezentujące powyżej 50% populacji, to ma być procedura standardowa. Jeżeli nie ma zapisu, że jest stosowana inna procedura, decyzje podejmie się większością zwykłą. Co to oznacza? To oznacza, że rządzą oczywiście najsilniejsi, że rządzą przede wszystkim dwa najsilniejsze państwa Unii Europejskiej kosztem państw mniejszych, kosztem państw średnich czy małych. Czy tak rozumiana zasada wzajemnego zaufania, współpracy partnerskiej w Unii Europejskiej, jest zasadą, która przyświeca całej Unii Europejskiej i powinna już jej przyświecać? Z jednej strony oczywiście najważniejszy dla nas jest interes Polski, ale czy tak widzimy świetlaną przyszłość Unii Europejskiej, którą rządzą tylko wybrani, którą rządzą silniejsi kosztem interesów tych, którzy muszą się podporządkowywać? A te zmiany, szanowni państwo, niestety do tego właśnie prowadzą. Jeszcze jeden bardzo ważny element, proszę, żeby Wysoka Izba zwróciła na niego uwagę: przyszłe zmiany traktatów. Jeżeli ta propozycja zostałaby przyjęta, a przypomnę, że na poszczególnych etapach przyjęć Parlament Europejski głosuje nad nią jutro, później Rada do Spraw Ogólnych, później Rada Europejska, na końcu konferencja międzyrządowa, gdzie dzisiaj jest wymagana jednomyślność… Jeżeli ta zmiana zostałaby przyjęta, do przyszłych zmian traktatowych nie będzie wymagana jednomyślność. Co to oznacza? To oznacza, że Polska może zostać związana umową międzynarodową, której nie będzie sygnatariuszem. Polska nie poprze przyszłej zmiany traktatu, a jednocześnie tą zmianą traktatu zostaną na nią nałożone określone obowiązki, czyli przekroczymy czerwoną granicę, za którą po prostu niektóre elementy będą już nieodwracalne. Mogę powiedzieć jako minister do spraw Unii Europejskiej, znający – też z racji mojego wykształcenia – historię Unii Europejskiej, że od czasu traktatów rzymskich, od lat 50., od czasu powstania Europejskiej Wspólnoty Gospodarczej nie było tak daleko idącej zmiany – jest to propozycja zmiany o charakterze bezprecedensowym. Były po drodze różne traktaty akcesyjne, Unia się poszerzała, zmieniała, był jednolity akt europejski, traktat z Maastricht, traktat z Amsterdamu, Nicea, Lizbona. Rzeczywiście w tych traktatach było tak, że część kompetencji przekazywano na rzecz instytucji unijnych. W 2009 r. przecież wokół tego też toczyła się żywa dyskusja. Wówczas śp. prezydent Lech Kaczyński, negocjując rozwiązania traktatu lizbońskiego, zapisał odpowiednie bezpieczniki, bo też były wątpliwości co do tego, czy przekazanie kompetencji nie idzie zbyt daleko. Zostały zapisane bezpieczniki, m.in. tzw. protokół brytyjski, mechanizm z Joaniny i inne elementy. Tym razem ta zmiana idzie, po pierwsze, o wiele dalej niż wszelkie poprzednie zmiany. Po drugie, przekracza granicę, za którą to będzie po prostu zmiana o charakterze nieodwracalnym. I teraz, szanowni państwo, czy wobec tak fundamentalnie ważnych propozycji nie uważacie państwo, Wysoki Sejmie, panie marszałku, że Wysoki Sejm w przededniu głosowania w Parlamencie Europejskim winien się wypowiedzieć w sytuacji (Oklaski), w której dyskutujemy o tym, czy polska suwerenność się obroni, czy immanentne cechy polskiej suwerenności, państwowości będą mogły być zachowane? To naprawdę, szanowni państwo, nie są żarty, to naprawdę nie jest jedna z wielu kolejnych dyskusji politycznych, jakich jest wiele i w tej Izbie, i na forum Parlamentu Europejskiego, i w łonie Unii Europejskiej. To może być moment zwrotny. I dlatego chciałem prosić Wysoką Izbę i pana marszałka, wszystkich posłów, apelując do państwa odpowiedzialności, o najgłębszy namysł nad tą sprawą. Czy to nie jest ostatni moment, właśnie w przededniu głosowania w Parlamencie Europejskim, żeby nad tą sprawą się pochylić? Może nad tym przecież obradować dzisiaj po południu Komisja do Spraw Unii Europejskiej, jeżeli konieczne jest jej powołanie. Ale może też nad tym obradować cała Izba. Można dzisiaj jeszcze podjąć decyzję, wyrażając wspólny głos całej Izby w tej sprawie. (Oklaski) Apeluję o to, żeby u startu nowej kadencji Sejmu, który reprezentuje wszystkich rodaków, którzy tak gremialnie oddali swoje głosy na wszystkich państwa, swoich reprezentantów, odpowiedzialność za tę fundamentalną sprawę wzięła cała klasa polityczna. To jest kwestia suwerenności Polski, to jest kwestia naszej państwowości, naszej przyszłości. Bardzo dziękuję. (Oklaski) (Głos z sali: Brawo!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie ministrze, za tak wyczerpującą wypowiedź. Chciałbym też jeszcze raz poinformować całą Izbę o tym, jak wygląda stan spraw związany z rzeczoną uchwałą. Rzeczona uchwała wczoraj została nam dostarczona na chwilę przed obradami Prezydium Sejmu. To poważny tekst o poważnych konsekwencjach… (Poseł Barbara Bartuś: No właśnie, dyskutujmy o tym.) …nakładający zobowiązania na rząd czy też apelujący o nałożenie tych zobowiązań, nakładający zobowiązania na posłów, na przedstawicieli Polski w Parlamencie Europejskim, dlatego też zdecydowałem o nadaniu numeru druku temu tekstowi i wysłaniu go do najbardziej kompetentnej komisji, która w tym parlamencie może się tym zająć. (Głos z sali: Nie ma jeszcze komisji.) Ale przepraszam bardzo, na to, że nie ma jeszcze komisji, macie bezpośredni wpływ wszyscy państwo, ponieważ opóźniacie obrady. Gdybyśmy szybko i sprawnie przeprowadzili proces powołania komisji i ich kreowania, wtedy już można byłoby procedować nad państwa projektem uchwały. (Poseł Antoni Macierewicz: Nie kłam, nie oszukuj.) (Głos z sali: Teraz można.) Prezydium Sejmu, po zasięgnięciu opinii Konwentu Seniorów, podjęło jasną decyzję w tej sprawie. Ta decyzja nie zostanie zmieniona. (Poseł Marek Suski: Był sprzeciw.) A ja chciałbym, żeby propozycje w tak poważnych kwestiach, w tak poważnych sprawach były przygotowywane wcześniej, tak iżby wszyscy posłowie mogli zawczasu zapoznać się z propozycjami, które państwo przedkładacie. (Oklaski) To jest fundamentalnie ważne, żebyśmy w tak ważnym momencie historii Unii Europejskiej, co podkreślił pan minister Szynkowski vel Sęk, podejmowali decyzje roztropnie i po namyśle, a nie na podstawie tekstów, których większość przedstawicieli tej Izby nie miała szansy przeczytać. (Głos z sali: Zamrażarka.) Jest wniosek… (Poseł Paweł Jabłoński: W trybie sprostowania.) Za chwilę, panie pośle. Staram się w sprawny sposób zarządzić ruchem z państwa strony, tj. członków Rady Ministrów, ale i dopuścić do głosu również przedstawicieli Izby, którzy ministrami nie są. Poproszę teraz z wnioskiem formalnym pana Pawła Zalewskiego z Polski 2050 – Trzeciej Drogi. (Poseł Paweł Jabłoński: W trybie sprostowania.) (Głos z sali: Ale nie był pan wymieniony.) Sprostowania odnośnie do czego, panie ministrze? (Wypowiedź poza mikrofonem) Przepraszam, to w takim razie chwilę po pośle Zalewskim, 20 sekund, zgodnie z pana prośbą i dyspozycją.",
                },
                {
                    "speaker": "Poseł Paweł Zalewski",
                    "content": "Panie Marszałku! Wysoka Izbo! PiS uczynił z Unii Europejskiej swojego wroga, całkowicie wbrew interesom naszego narodu, bo suwerenność Polski można wzmacniać i rozwijać dzięki obecności w Unii Europejskiej. (Oklaski) To nie jest przypadek, panie i panowie, że dzisiaj tysiące Ukraińców ginie po to, aby mieć możliwość uzyskania członkostwa w Unii Europejskiej (Poruszenie na sali), czegoś, z czego wy uczyniliście przedmiot nienawiści w polskiej polityce. (Oklaski) (Poseł Barbara Bartuś: W obronie swojej niepodległości giną.) Unia Europejska jest także symbolem waszej nieudolności, bo żadnego ważnego polskiego interesu nie potrafiliście w niej rozwiązać. (Oklaski) Natomiast ta uchwała, ten projekt czy – co ważniejsze – ta propozycja komisji konstytucyjnej, nad którą odbędzie się jutro głosowanie w Parlamencie Europejskim, jest (Dzwonek) bardzo daleko idąca i bardzo ważna. W tej sali są jej zwolennicy i przeciwnicy. (Głos z sali: I zdrajcy.) Muszę powiedzieć, że dzisiaj to, co proponujecie… Z poważnej dyskusji na temat polskiego stanowiska wobec propozycji komisji konstytucyjnej i być może Parlamentu Europejskiego… (Poseł Bożena Borys-Szopa: A wniosek formalny?) …czynicie hucpę, dlatego że zapomnieliście, jak powinna wyglądać… (Głosy z sali: Czas! Czas!) …normalna procedura w tej Izbie. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, zbliżamy się do końca.",
                },
                {
                    "speaker": "Poseł Paweł Zalewski",
                    "content": "Otóż od rozpatrzenia takich uchwał jest Komisja Europejska. To w niej powinniśmy – i mam nadzieję, że będziemy szybko – tę kwestię omawiać. Dopiero po gruntownej dyskusji, z wysłuchaniem także ekspertów różnych stron, również strony społecznej, także przedstawicieli różnych instytucji, które w tej sprawie mają wiele do powiedzenia…",
                },
                {"speaker": "Marszałek", "content": "Panie pośle, kończymy."},
                {
                    "speaker": "Poseł Paweł Zalewski",
                    "content": "…dopiero wtedy powinniśmy nad tą kwestią obradować w Sejmie. (Głos z sali: Czas!) Tak że wnoszę, panie marszałku, o odrzucenie tej propozycji – to jest głos przeciwny wobec tej propozycji – i wnoszę o zmianę… (Głos z sali: Czas!) …sposobu prowadzenia obrad w taki sposób, aby już przejść do głosowania. Dziękuję, panie marszałku. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Przyjąłem sugestię pana posła. (Głos z sali: Swoim kolegom to pan przedłuża czas.) Przedłużyłem dokładnie tyle, ile przedłużyłem panu ministrowi Adamczykowi. (Poseł Barbara Bartuś: Minister miał 15 minut.) Przepraszam bardzo, pan minister wypowiadał się jako poseł, a ja nie będę tutaj wnikał w to, jaką tożsamość czy jaką część tożsamości uruchamia któryś z państwa, wchodząc na mównicę. (Poseł Barbara Bartuś: Jako minister odpowiadał.) Drodzy państwo, wnioski formalne zostały wyczerpane. Panu ministrowi obiecałem 20 sekund. Bardzo proszę, panie ministrze. (Głos z sali: Panie marszałku, ja…) Pamiętam. Tęskniłem i pamiętam, panie pośle.",
                },
                {
                    "speaker": "Sekretarz Stanu w Ministerstwie Spraw Zagranicznych Paweł Jabłoński",
                    "content": "Panie Marszałku! Dziękuję bardzo. W trybie sprostowania. Trzeba trzymać się faktów. Do momentu wznowienia obrad nie został nadany numer druku, dlatego właśnie jest wniosek o nadanie numeru druku i uzupełnienie porządku dziennego. Apeluję o to, bo ta sprawa jest bardzo ważna, jak mówi minister Szynkowski. I druga sprawa. Ta uchwała wyraża zdecydowane poparcie dla członkostwa Polski w Unii Europejskiej, w takiej, jaka ona jest dzisiaj… (Oklaski) (Głos z sali: Brawo!) …a nie w takiej, na jaką chcecie ją zmienić, centralnie zarządzanej. I to są fakty, które powinny być również znane, panie pośle Zalewski.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Wśród członków Rady Ministrów, którzy nie zabrali jeszcze dziś głosu, jest pan poseł Michał Wójcik. Rozumiem, że odwołuje się pan tutaj do swojego zakresu kompetencji. Przeczytałem przed chwilą rozporządzenie pana premiera Morawieckiego wyznaczające pana zakres kompetencji. Jest wśród nich m.in. obrona praw obywatelskich oraz ochrona tożsamości europejskiej. Jak rozumiem, w tej kwestii chciał się pan wypowiedzieć. (Poseł Mirosław Suchoń: Jakiś żart.) Jeżeli natomiast mogę mieć tylko uprzejmą prośbę do pana ministra, to chciałbym zapytać, czy zechciałby pan ograniczyć czas swojej wypowiedzi do czasu, który w tym dniu przewidzieliśmy dla przedstawicieli klubów parlamentarnych. (Głos z sali: Nie.) Będę bardzo zobowiązany za zastosowanie się do mojej prośby.",
                },
                {
                    "speaker": "Minister – Członek Rady Ministrów Michał Wójcik",
                    "content": "Ależ oczywiście, panie marszałku. 15 minut będę przemawiał. (Poseł Sławomir Nitras: Chyba żart.) Szanowny Panie Marszałku! Szanowni Państwo!",
                },
                {
                    "speaker": "Marszałek",
                    "content": "3 minuty. Proszę o 3 minuty, jeżeli mogę prosić.",
                },
                {
                    "speaker": "Minister – Członek Rady Ministrów Michał Wójcik",
                    "content": "Oczywiście, jak najbardziej.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Ja jestem tylko skromnym marszałkiem, a pan członkiem Rady Ministrów",
                },
                {
                    "speaker": "Minister – Członek Rady Ministrów Michał Wójcik",
                    "content": "Panie Marszałku! Szanowni Państwo! Rozmawiamy o suwerenności, a suwerenność to jest dusza narodu, to jest esencja. Nie rozmawiamy o czymkolwiek. To nie jest jakaś tam sobie uchwała. (Poseł Sławomir Nitras: To jest jakaś tam sobie uchwała.) To jest uchwała, która dotyczy, szanowni państwo, naszej pozycji w Unii Europejskiej, tego, czy będziemy prowincjonalnym krajem, który nic nie będzie mógł robić, bo tak naprawdę są tworzone w Unii Europejskiej dwa ośrodki władzy, czy będziemy pozbawieni wszelkich kompetencji. Przecież, panie marszałku, powinniśmy tak naprawdę natychmiast nad tym usiąść. To jest kluczowa sprawa. Przecież to chodzi o wolność obywateli, o to, jaką pozycję ma mieć nasz kraj, o naszą państwowość. My swoją robotę jako Rada Ministrów dzisiaj już zrobiliśmy, bo przyjęliśmy uchwałę w tej sprawie, jednoznacznie mówiąc: nie (Oklaski), nie zgadzając się na to, co robi Unia Europejska. Chodzi o to, nad czym ma odbyć się jutro głosowanie. Powiem więcej, panie marszałku. Jutro o godz. 12 odbędzie się to głosowanie. Kiedy pan chce nad tym procedować? Musimy mieć stanowisko parlamentu wypracowane wcześniej. (Głos z sali: Dzisiaj.) Dzisiaj oczywiście. (Oklaski) Tu się przyłączam do tego, co mówił pan minister Jabłoński. A jeżeli chodzi o pana posła Zalewskiego, to chcę powiedzieć, że my nie rozmawiamy o Unii Europejskiej, tylko my rozmawiamy o Polsce. (Oklaski) Wobec tego bardzo bym prosił, żeby procedować natychmiast nad tą uchwałą, panie marszałku. Jeszcze jedna rzecz. Wracam trochę do pewnego wątku historycznego. Kiedy Polska odzyskała niepodległość po 123 latach, to pomimo wielkich sporów, które dzieliły całą scenę polityczną, szanowni państwo, wszyscy potrafili usiąść do jednego stołu i wypracować kompromis: i Daszyński, i Dmowski, i Piłsudski, i Paderewski, i Korfanty, wszyscy. I Witos też, oczywiście. A dzisiaj, szanowni państwo, wy to chcecie gdzieś tam odrzucić na bok. Suwerenność to jest kluczowa sprawa. (Oklaski) Proszę o natychmiastowe przejście do pochylenia się parlamentu, całej Izby nad tą uchwałą. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, panie ministrze akurat w tej sytuacji, bardzo dziękuję za pana głos. Powtórzę raz jeszcze: Komisja do Spraw Unii Europejskiej jest organem polskiego parlamentu. (Poseł Marek Suski: Można bez odsyłania do komisji.) (Poseł Antoni Macierewicz: To nie jest konieczne.) Każda minuta, którą spędzamy na tej dyskusji na tej sali, oddala nas od wystąpienia do tej komisji i przygotowania materiału przez tę komisję, który mógłby posłużyć refleksją tym, którzy jutro w Unii Europejskiej będę podejmowali decyzję. (Poseł Antoni Macierewicz: Wprowadza pan w błąd.) Czy głos chciał zabrać jeszcze pan minister Łukasz Schreiber? Bo takie zgłoszenie mam. (Poseł Łukasz Schreiber: Tak.) Ale nie, ja nie chcę się narzucać. Zgłosił się pan, tylko bardzo bym prosił, jeżeli mogę: krótko, panie ministrze. (Poseł Łukasz Schreiber: Dobrze.) (Głos z sali: Wnioski formalne.) Za chwilę będziemy głosować nad kolejnym wnioskiem formalnym, natomiast pan minister był pierwszy, nawet przed panem ministrem Wójcikiem, a ja nie chciałbym czynić mu dyshonoru.",
                },
                {
                    "speaker": "Minister – Członek Rady Ministrów Łukasz Schreiber",
                    "content": "Czekam spokojnie, dziękuję. Wielce Szanowny Panie Marszałku! Panie Premierze! Wysoka Izbo! Myślę, że warto zacząć od podkreślenia czegoś, co jest też istotne, tj. od zwrócenia uwagi, że pan marszałek jednak, w przeciwieństwie do ostatnich 8 lat, do tego, co słyszeliśmy z lewej strony sali, w przeciwieństwie do tej agresji, pogardy, także chamstwa w stosunku do pani marszałek, do prawej strony Izby, i to nie tylko werbalnego, jeżeli chodzi o okupację Izby, rzucanie w naszego lidera bucikami, śmiecenie na tej sali, przyniósł do tej Izby kulturę. I to jest dobra rzecz, która wymaga odnotowania. I ja za to osobiście dziękuję. Jest tylko jedno ale, że te piękne słowa czasem rozmijają się trochę z czynami. I to jest rzecz, o którą chciałem do pana marszałka zaapelować. Bardzo pięknie pan mówi o nowych standardach. Pozbawienie największego klubu parlamentarnego stanowiska wicemarszałka wprawdzie jest nowym standardem, ale chyba nie takim, do którego byśmy chcieli nawiązywać. Stwierdzenie, że wicepremier nie może zabrać głosu, tak jak to było na ostatnim posiedzeniu, także nie. Stwierdzenie, że największy klub parlamentarny, jak słyszymy, ma mieć pięciu przewodniczących, to wprawdzie także jest chyba nowy standard, ale niekoniecznie ten, do którego byśmy chcieli nawiązywać. O Senacie nie będę mówił, ale zwrócę uwagę na to, o czym mówili dzisiaj też koledzy. Mamy sprawę fundamentalną. Mamy projekt, który dotyczy zmiany traktatów i który może być rozpatrywany w tej Izbie także w dniu dzisiejszym, biorąc pod uwagę, ile czasu zostało. Mamy ustawę o zerowym podatku VAT na żywność, na której przedłużenie na rok 2024 na pewno czekają obywatele. (Poseł Paulina Hennig-Kloska: W budżecie nie zapisaliście.) Mamy ustawę o wakacjach kredytowych, która także jest przygotowana i na którą czekają obywatele. Panie Marszałku! Albo są to, i chcemy w to wierzyć, nowe standardy – jeżeli pan to wszystko zrobi, na pewno zyska pan szacunek także prawej strony sali – albo jest to tylko kontynuacja polityki TKM. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję. Panie ministrze, moja wiara jest niewzruszona i nic nią nie zachwieje. Dziękuję, że zechciał się pan tak zdyscyplinować czasowo. Mam nadzieję zasłużyć na pewnym etapie naszej znajomości i współpracy na państwa szacunek, bo szacunek zawsze państwu okazuję. Chcę zwrócić uwagę, że pan poseł Zalewski w trybie art. 184 pkt 5 zgłosił wniosek o przejście do kolejnego punktu porządku dziennego. Chciałbym teraz poddać ten wniosek pod głosowanie. Ten wniosek formalny wymaga decyzji pań i panów posłów. Przypominam, że jest to wniosek o przejście do kolejnego punktu porządku dziennego. Przystępujemy do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku formalnego o przejście w tej chwili do kolejnego punktu porządku dziennego, zechce podnieść rękę i nacisnąć przycisk… (Poseł Paweł Jabłoński: Wniosek o przerwę był wcześniej.) Tak, ale wniosek o przerwę to był wniosek o przerwę, a w tej chwili mamy wniosek o przejście do porządku dziennego. (Poseł Barbara Bartuś: Ale wcześniej był o przerwę.) (Głos z sali: Była już przerwa.) Wniosek o przerwę był, dlatego kolejne wnioski o przerwę są bezprzedmiotowe. (Wypowiedź poza mikrofonem) Ach, po wznowieniu obrad pierwszy wniosek o przerwę. Państwo zgłaszaliście wniosek formalny o przerwę? (Wypowiedź poza mikrofonem) Pan poseł Jabłoński. Oczywiście, bardzo dobrze. Poinformowałem pana posła o tym, jaki jest stan prac. Nad tym wnioskiem o przerwę będziemy teraz głosować. (Poseł Barbara Bartuś: To teraz głosujemy?) Ale spokojnie, proszę bez emocji. Będziemy głosować nad wnioskiem złożonym przez pana posła Jabłońskiego o przerwę w obradach. (Gwar na sali) Proszę państwa, bardzo proszę o odrobinę spokoju. Dobrze, zamykamy formalnie tamto głosowanie. Uznaję rację pana posła Jabłońskiego i głosujemy nad jego wnioskiem o przerwę, a nad wnioskiem pana posła Zalewskiego będziemy głosować w następnej kolejności. Bardzo proszę, wniosek o przerwę w obradach. Kto z pań i panów posłów… (Gwar na sali.) Aha, dobrze, dobrze. Przepraszam bardzo, przepraszam państwa, to moja wina. Biję się w piersi, to moja wina, ale chaos, który generuje się w niektórych miejscach na tej sali, uniemożliwia skupienie się nad państwa wnioskami napływającymi do stołu prezydialnego. Musimy formalnie zamknąć głosowanie w sprawie przejścia do kolejnego punktu porządku dziennego. Pytam jeszcze raz, bo głosowanie technicznie jest otwarte. Kto z pań i panów posłów jest za wnioskiem o przejście do kolejnego punktu porządku dziennego, zechce podnieść rękę i nacisnąć przycisk. Kto z pań i panów posłów jest przeciw temu wnioskowi? (Wypowiedź poza mikrofonem) Bardzo dobrze. Słyszę, a i maszyna na pewno to zauważyła. Kto się wstrzymał? Głosowało 456 posłów. 264 – za, 190 – przeciw, 2 się wstrzymało. Stwierdzam, że Sejm przyjął wniosek o przejście do kolejnego punktu porządku dziennego. Ten punkt… (Poseł Barbara Bartuś: A co z wnioskiem o przerwę?) No nie, jesteśmy w kolejnym punkcie. Przystępujemy do rozpatrzenia punktu 8. porządku dziennego: Wybór składów osobowych komisji sejmowych (druk nr 20). Wysoka Izbo! Prezydium Sejmu, po zasięgnięciu opinii Konwentu Seniorów, na podstawie art. 20 ust. 1 regulaminu Sejmu przedstawiło wniosek w sprawie wyboru składów osobowych komisji sejmowych. Proszę o uwzględnienie, na prośbę Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga, poprawek polegających na: — wykreśleniu ze składu Komisji Obrony Narodowej posła Pawła Bejdy i dopisaniu posła Andrzeja Grzyba, — dopisaniu do składu Komisji Cyfryzacji, Innowacyjności i Nowoczesnych Technologii posła Krzysztofa Hetmana, — wykreśleniu ze składu Komisji Polityki Społecznej i Rodziny poseł Urszuli Pasławskiej i dopisaniu posła Dariusza Klimczaka, — wykreśleniu ze składu Komisji Zdrowia posła Mirosława Adama Orlińskiego i dopisaniu posła Władysława Kosiniaka-Kamysza. Czy ktoś z pań i panów posłów pragnie zabrać głos w sprawie tej konkretnej, przedstawionej propozycji? Nikt się nie zgłasza. (Głos z sali: Zgłasza się.) Zgłasza się? (Głos z sali: Zgłasza się.) Zgłasza się. Pan w tej sprawie, panie ministrze? Proszę bardzo.",
                },
                {
                    "speaker": "Sekretarz Stanu w Ministerstwie Spraw Zagranicznych Paweł Jabłoński",
                    "content": "Panie marszałku, ja się zgłaszam z wnioskiem formalnym. (Głosy z sali: Nie! Nie ma!) Rozumiem, że pan przez pomyłkę poddał pod głosowanie najpierw wniosek chronologicznie drugi, ale mój wniosek formalny cały czas nie został rozpoznany. Zgłaszam wniosek o to, żeby on został rozpoznany. On pozostaje w tej chwili…",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Tylko że jesteśmy w innym punkcie porządku dziennego, jak pan zdaje sobie sprawę. (Oklaski)",
                },
                {
                    "speaker": "Sekretarz Stanu w Ministerstwie Spraw Zagranicznych Paweł Jabłoński",
                    "content": "Zgłaszam, panie marszałku, wniosek o to, żeby rozpoznać ten wniosek, który zgodnie z regulaminem Sejmu cały czas czeka na rozpoznanie. (Oklaski) (Poseł Jacek Protas: Został przegłosowany.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Zapytałem pracowników Kancelarii Sejmu i nie mamy co do tego wątpliwości, że będąc w innym punkcie porządku dziennego, nad tym wnioskiem głosować już nie będziemy. (Oklaski) Jeżeli zgłaszał pan wniosek, który dotyczył przerwy w poprzednim punkcie obrad, to nawet na logikę, jeżeli jesteśmy w kolejnym punkcie obrad, zgłaszanie tego wniosku nosiłoby cechy obstrukcji parlamentarnej, niczego więcej. Chyba że chce pan zgłaszać wniosek o przerwę z powodu chęci złożenia wniosku o przerwę. (Poseł Barbara Bartuś: Trochę powagi.) On dotyczył konkretnej rzeczy, panie pośle, bardzo konkretnej rzeczy. Chciał pan, żeby Sejm zajął się projektem uchwały, który złożyliście państwo i który uważacie za bardzo ważny – ja zresztą też tak uważam – jeżeli chodzi o procedowanie w Sejmie. Wyjaśniliśmy, mam nadzieję, w sposób kompetentny, jaka będzie droga procedowania tego projektu w Sejmie i żadna przerwa tego nie zmieni, a poza tym jesteśmy w innym punkcie porządku obrad. (Poseł Antoni Macierewicz: Zdrajca.) Przystępujemy do głosowania nad składem komisji sejmowych. Kto z pań i panów posłów jest za przyjęciem wniosku z druku nr 20 wraz z poprawkami, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 454 posłów. 273 – za, 178 – przeciw, wstrzymało się 3 posłów. Stwierdzam, że Sejm podjął uchwałę w sprawie wyboru składów osobowych komisji sejmowych. Przystępujemy do rozpatrzenia punktu 9. porządku dziennego: Wybór składu osobowego Komisji do Spraw Unii Europejskiej (druk nr 21). Prezydium Sejmu, po zasięgnięciu opinii Konwentu Seniorów, na podstawie art. 148a ust. 8 regulaminu Sejmu przedłożyło wniosek w sprawie wyboru składu osobowego Komisji do Spraw Unii Europejskiej. Przypominam, że Sejm dokonuje wyboru członków komisji w głosowaniu łącznym. Czy ktoś z pań i panów posłów pragnie zabrać głos w sprawie przedstawionej propozycji? Nikt się nie zgłasza. Przystępujemy więc do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku z druku nr 21, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 456 posłów. 265 – za, 191 – przeciw, nikt się nie wstrzymał. Stwierdzam, że Sejm podjął uchwałę w sprawie wyboru składu osobowego Komisji do Spraw Unii Europejskiej. Przystępujemy do rozpatrzenia punktu 10. porządku dziennego: Wybór składu osobowego Komisji Etyki Poselskiej (druk nr 22). Prezydium Sejmu, po zasięgnięciu opinii Konwentu Seniorów, na podstawie art. 143 ust. 11 regulaminu Sejmu przedstawiło wniosek w sprawie wyboru składu Komisji Etyki Poselskiej. Przypominam, że Sejm dokonuje wyboru członków komisji w głosowaniu łącznym. Czy ktoś z pań i panów posłów chce zabrać głos w tej sprawie? Nikt się nie zgłasza. Przystępujemy więc do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku w brzmieniu z druku nr 22, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 455 posłów. 263 – za, 190 – przeciw, 2 się wstrzymało Stwierdzam, że Sejm podjął uchwałę w sprawie wyboru składu osobowego Komisji Etyki Poselskiej. Przystępujemy do rozpatrzenia punktu 11. porządku dziennego: Wybór składu osobowego Komisji do Spraw Służb Specjalnych (druk nr 23). Prezydium Sejmu, po zasięgnięciu opinii Konwentu Seniorów, na podstawie art. 137 ust. 4 regulaminu Sejmu przedłożyło wniosek w sprawie wyboru składu osobowego Komisji do Spraw Służb Specjalnych. Sejm na podstawie art. 137 ust. 4 regulaminu Sejmu wybiera skład osobowy komisji w głosowaniu łącznym. Czy ktoś z pań i panów posłów pragnie zabrać głos w sprawie przedstawionych propozycji? (Głos z sali: Tak.) Nikt się nie zgłasza. (Głos z sali: Zgłasza się.) A, jest, pan poseł Suski. Otwieram dyskusję. Proponuję, aby w dyskusji Sejm wysłuchał 3-minutowych oświadczeń w imieniu klubów i koła. Jeśli nie usłyszę sprzeciwu, będę uważał, że Sejm tę propozycję przyjął. Sprzeciwu nie słyszę. Bardzo proszę, głos ma poseł Marek Suski z klubu Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Marek Suski",
                    "content": "Dziękuję bardzo. Panie Marszałku! Wysoka Izbo! Panie Premierze! Przypomnę, że podczas posiedzenia Konwentu dowiedziałem się, że w komisji do spraw służb Prawo i Sprawiedliwość będzie miało jedno miejsce, choć z parytetu na dobrą sprawę wypadają nam tam trzy miejsca, 2,8, czyli w zaokrągleniu trzy miejsca. Ale szanowni państwo, prosiłem też na posiedzeniu Konwentu, żeby w związku z tym, że jest propozycja jednego miejsca dla nas, zostawić wakat. Oczywiście pan marszałek się nie zgodził, powiedział, że to już zamknięta procedura, a teraz się dowiedzieliśmy, że jednak po zamknięciu procedury klub PSL-u złożył szereg zmian do komisji, czyli taka możliwość była, jak widać, ale nie było dobrej woli. (Głos z sali: To koledzy są.) (Poseł Antoni Macierewicz: Jest procedura i jest interes.) Chciałem powiedzieć, że komisja do spraw służb jest niezwykle ważna. Pozbawienie parytetu, zresztą tak jak w innych sprawach – za chwilę będziemy mówili o Trybunale Stanu, gdzie również w tamtej sprawie państwo nam kradniecie po prostu to, co nam się z parytetu należy – to jest polityczne złodziejstwo, więc wyrażam sprzeciw wobec wyboru w tym składzie komisji do spraw służb. (Oklaski) Dziękuję bardzo, panie marszałku. A panu zwracam uwagę, że pan permanentnie łamie regulamin. Nawet ta uchwała, którą przyjęliśmy przed chwilą na posiedzeniu komisji regulaminowej, nie zakazuje posłom, którzy są ministrami, zabierania głosu, a tylko pan chce przydzielić sobie prawo do tego, że przed wystąpieniem będzie pan oceniał, czy minister będzie mówił na temat czy też nie. To jest po prostu cenzura. W PRL-u była cenzura prewencyjna, teraz wraca PRL. (Oklaski) (Głos z sali: PRL!)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle Suski, dyskutuje pan z czymś, co nie istnieje, bo… (Poseł Barbara Bartuś: Ale pan nie jest od komentowania.) …jasno i wyraźnie wynika z uchwały – odnoszę się teraz do uchwały Prezydium Sejmu, którą komentował pan poseł Suski – że nikt nigdy w tej Izbie, czego ja jestem dowodem i żywym przykładem, nie zabrania członkom Rady Ministrów zabierania głosu w trybie odnośnego artykułu regulaminu Sejmu. Kolejny głos zabierze pan poseł Zbigniew Konwiński z klubu Koalicji Obywatelskiej.",
                },
                {
                    "speaker": "Poseł Zbigniew Konwiński",
                    "content": "Panie Marszałku! Wysoka Izbo! Panie Pośle Suski! Nastały czasy, że regulamin Sejmu obowiązuje. (Oklaski) Państwo zgłosiliście osobę, która jest nieuprawniona do zasiadania w komisji, bo jest sekretarzem stanu. Może pan przyzwyczaił się do czasów, gdy wystarczyła wola polityczna. Nie, w tej chwili regulamin Sejmu obowiązuje, takie czasy nastały. To po pierwsze. (Oklaski) (Głos z sali: Łamiecie regulamin.) Po drugie, przywracamy rotacyjność przewodniczącego Komisji do Spraw Służb Specjalnych. (Oklaski) Powiem więcej, mimo że, jak widzimy, na sali jest większość dawnej opozycji demokratycznej, to wy będziecie mieli przez pewien czas swojego przewodniczącego w Komisji do Spraw Służb Specjalnych. Wiem, że to was może dziwić, może śmieszyć, ale tak, uszanujemy werdykt demokratyczny i PiS będzie miał również przez pewien czas swojego przewodniczącego Komisji do Spraw Służb Specjalnych. Jeszcze jedna kwestia, panie pośle. Przecież opowiadacie od paru tygodni, że macie większość, że premier Morawiecki buduje większość, że rząd będzie miał większość w Sejmie, to co się pan przejmuje tym, co panu ktoś na posiedzeniu Konwentu powiedział? Pan ma większość, to pan za chwilę przegłosuje to tak, jak pan chce. (Wesołość na sali, oklaski) Chyba że od paru tygodni okłamujecie Polaków, mówiąc o tej większości, chyba że od paru tygodni okłamujecie prezydenta, mówiąc o tym, że budujecie większość. A to nieładnie, nieładnie. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Lista posłów zapisanych do głosu została wyczerpana. Zamykam dyskusję. Przystępujemy do głosowania. Kto z pań i panów posłów jest za przyjęciem wniosku z druku nr 23, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 456 posłów. 264 – za, 192 – przeciw, nikt się nie wstrzymał. Stwierdzam, że Sejm podjął uchwałę w sprawie składu osobowego Komisji do Spraw Służb Specjalnych. Przystępujemy do rozpatrzenia punktu 12. porządku dziennego: Wybór członków Trybunału Stanu (druki nr 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 i 51). Zgodnie z art. 199 ust. 1 Konstytucji Rzeczypospolitej Polskiej Sejm dokonuje wyboru dwóch zastępców przewodniczącego i 16 członków Trybunału Stanu. Proszę o zabranie głosu panią poseł Lidię Burzyńską w celu przedstawienia kandydata na zastępcę przewodniczącego Trybunału Stanu pana Piotra Łukasza Juliusza Andrzejewskiego i kandydatów na członków Trybunału Stanu: pana Marka Czeszkiewicza, pana Jana Majchrowskiego, pana Adriana Salusa, pana Piotra Saka, pana Marcina Wawrzyniaka i pana Macieja Gustawa Zaborowskiego, zgłoszonych przez posłów z Klubu Parlamentarnego Prawo i Sprawiedliwość. Bardzo proszę, pani poseł.",
                },
                {
                    "speaker": "Poseł Lidia Burzyńska",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Przedstawiam kandydata do Trybunału Stanu. Pan Piotr Łukasz Juliusz Andrzejewski urodził się 2 stycznia 1942 r. w Warszawie. W 1964 r. ukończył studia prawnicze na Uniwersytecie Warszawskim. Na tej samej uczelni otrzymał absolutorium z historii sztuki. Po odbyciu aplikacji sędziowskiej i złożeniu egzaminu sędziowskiego rozpoczął aplikację adwokacką. Po złożeniu egzaminu adwokackiego rozpoczął praktykę adwokacką w 1971 r. Był związany z opozycją demokratyczną, w odróżnieniu od obecnych. Na przełomie sierpnia i września 1980 r. był pierwszym konsultantem prawnym międzyzakładowego komitetu strajkowego z siedzibą w Hucie Katowice, a jako pełnomocnik tego komitetu był autorem pierwszego wniosku o rejestrację NSZZ „Solidarność” w Sądzie Wojewódzkim w Warszawie. Po wprowadzeniu stanu wojennego był obrońcą w licznych procesach politycznych działaczy NSZZ „Solidarność”, w tym w pierwszym procesie stanu wojennego pracowników Instytutu Badań Jądrowych z warszawskiego Żerania. Na I Krajowym Zjeździe Adwokatury w 1983 r. publicznie potępił łamanie praw człowieka w okresie stanu wojennego. Na polecenie ówczesnych władz wytoczono mu osiem spraw dyscyplinarnych pod pozorem naruszenia wolności słowa. W wyniku jednej z nich, po rewizji nadzwyczajnej wniesionej do Sądu Najwyższego przez ministra sprawiedliwości, został pozbawiony prawa wykonywania zawodu na rok. Był jednym z inicjatorów powtórnej rejestracji zakładowych komitetów założycielskich NSZZ „Solidarność” i reprezentował w sądach ok. 40 takich komitetów. W wyborach w czerwcu 1989 r. był członkiem Państwowej Komisji Wyborczej jako przedstawiciel komitetu obywatelskiego przy Lechu Wałęsie. W dniu głosowania w wyborach do Sejmu i Senatu skutecznie przeciwstawiał się manipulacjom mającym zmienić wyniki tzw. listy krajowej. Od 1983 r. był członkiem konspiracyjno-dokumentacyjnej struktury Komitetu Helsińskiego, a następnie członkiem założycielem Helsińskiej Fundacji Praw Człowieka. W 1988 r. otrzymał nagrodę duńskiej fundacji za działalność w obronie praw człowieka. Od 15 grudnia 1991 r. do 6 września 1992 r. pełnił funkcję dyrektora generalnego – likwidatora dotychczasowych struktur państwowej jednostki organizacyjnej radio i telewizja. Autor ustawy o zwrocie korzyści uzyskanych niesłusznie kosztem Skarbu Państwa oraz reprezentant NSZZ „Solidarność” w procesach wytoczonych na jej podstawie. Członek komisji konstytucyjnej i ugrupowań centroprawicowych. Przewodniczący działu źródeł prawa i wymiaru sprawiedliwości. Współautor obywatelskiego projektu konstytucji, członek Komisji Konstytucyjnej Zgromadzenia Narodowego, przewodniczący podkomisji źródeł prawa. W Senacie I kadencji był członkiem Komisji Praw Człowieka i Praworządności, Komisji Samorządu Terytorialnego oraz Komisji Nadzwyczajnej do spraw górnictwa. W II kadencji był wiceprzewodniczącym Komisji Regulaminowej i Spraw Senatorskich oraz Komisji Inicjatyw i Prac Ustawodawczych. W III kadencji był członkiem założycielem i uczestnikiem Społecznej Komisji Konstytucyjnej NSZZ „Solidarność” i ugrupowań centroprawicowych. W IV kadencji przewodniczył Komisji Ustawodawczej i był członkiem Komisji Kultury i Środków Przekazu. Od 2019 r. zastępca przewodniczącego Trybunału Stanu, w którym jest od 2011 r. Był i jest bezpartyjny. Zarówno wykształcenie, jak i bogate doświadczenie zawodowe wskazują, iż pan Piotr Łukasz Juliusz Andrzejewski jest dobrym kandydatem na stanowisko zastępcy przewodniczącego Trybunału Stanu. Przedstawiam pana Jana Majchrowskiego. Urodził się 17 listopada 1964 r. w Warszawie, gdzie ukończył Liceum im. Stefana Batorego. Następnie studiował na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego, gdzie w 1990 r. uzyskał dyplom magistra prawa z wyróżnieniem. Studiował również na Wydziale Dziennikarstwa i Nauk Politycznych Uniwersytetu Warszawskiego i uzyskał dyplom magistra nauk politycznych z wyróżnieniem. W 1997 r. na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego obronił pracę doktorską i otrzymał stopień doktora nauk prawnych, zaś w 2012 r. na tej samej uczelni w wyniku jednogłośnie przyjętego kolokwium habilitacyjnego został doktorem habilitowanym nauk prawnych o specjalności prawo konstytucyjne i teoria państwa. Wykształcenie uzupełniał w ramach licznych stypendiów, staży i kursów zagranicznych. Jest profesorem Uniwersytetu Warszawskiego zatrudnionym na Wydziale Prawa i Administracji nieprzerwanie od 33 lat. Jest to obecnie jedyne miejsce jego pracy. Był pięciokrotnie wyróżniany nagrodą rektora Uniwersytetu Warszawskiego. Jest autorem, współautorem lub redaktorem 10 książek oraz autorem kilkudziesięciu artykułów naukowych, głównie z dziedziny prawa konstytucyjnego i nauki o państwie, oraz kilkuset artykułów publicystycznych o podobnej tematyce. W przeszłości równolegle z pracą naukowo-dydaktyczną na Wydziale Prawa i Administracji podejmował także inną działalność zawodową i profesjonalną, w tym społeczną. W jej ramach był m.in. doradcą naukowym generalnego komisarza wyborczego, ekspertem społecznej komisji konstytucyjnej, adiunktem na wydziale prawa, doradcą w gabinecie politycznym ministra spraw wewnętrznych i administracji w 1998 r., podsekretarzem stanu w MSWiA, delegatem rządu do spraw administracyjnych w województwie lubuskim, wojewodą lubuskim i dyrektorem oddziału regionalnego ARiMR w województwie lubuskim. Od 2001 r. był asystentem naukowym sędziego Trybunału Konstytucyjnego, a następnie – doradcą prezesa Trybunału Konstytucyjnego, z której to funkcji zrezygnował. Odszedł z pracy w Trybunale Konstytucyjnym na własną prośbę w roku 2009. Był także ekspertem Rady Europy do spraw finansowania partii politycznych w ramach Grupy Państw przeciwko Korupcji. Nie należy do partii politycznych, związków zawodowych, stowarzyszeń ani innych organizacji społecznych. Jest honorowym obywatelem Wschowy. Zarówno wykształcenie, jak i bogate doświadczenie zawodowe wskazują, iż pan Jan Majchrowski jest dobrym kandydatem na stanowisko członka Trybunału Stanu. Wysoka Izbo! Przedstawiam teraz kandydata na członka Trybunału Stanu Piotra Saka, który urodził się 29 maja 1983 r. w Tarnowie. W latach 2002–2007 odbył studia magisterskie na Wydziale Prawa i Administracji Uniwersytetu Jagiellońskiego w Krakowie. W 2009 r. rozpoczął aplikację adwokacką, którą zakończył w 2012 r. W tym samym roku złożył egzamin adwokacki i został wpisany na listę adwokatów Krakowskiej Izby Adwokackiej. Ukończył także studium menedżerskie w Szkole Przedsiębiorczości i Zarządzania Akademii Ekonomicznej w Krakowie. Autor wielu artykułów w zakresie prawa pracy, publikowanych m.in. w „Rzeczpospolitej”, „Dzienniku Gazecie Prawnej” i miesięczniku „Praca i Zabezpieczenie Społeczne”. Od 2019 r. do 2023 r. był posłem IX kadencji. W tym czasie pełnił funkcję przewodniczącego nadzwyczajnej komisji do spraw zmian w kodyfikacjach. Był także członkiem komisji kontroli państwowej i Komisji Sprawiedliwości i Praw Człowieka. W latach 2010–2014 był radnym Sejmiku Województwa Małopolskiego. W tym czasie pełnił funkcję m.in. przewodniczącego komisji statutowo-prawnej. W latach 2014–2019 piastował funkcję radnego Rady Miejskiej w Tarnowie. Przez wiele lat stale świadczył pomoc prawną pro bono na rzecz osób pokrzywdzonych i poszkodowanych. Wiedza prawnicza, doświadczenie zawodowe i społeczne stanowią rękojmię należytego wykonywania przez pana Piotra Saka funkcji członka Trybunału Stanu. Następnym kandydatem na członka Trybunału Stanu, którego przedstawiam Wysokiej Izbie, jest pan Adrian Salus. W 2009 r. ukończył z wyróżnieniem dzienne magisterskie studia prawnicze na Uniwersytecie Rzeszowskim. Pracę magisterską napisał pod patronatem konstytucjonalisty pana prof. dr. hab. Stanisława Sagana, a tematem pracy była instytucja komisji śledczej w Sejmie Rzeczypospolitej Polskiej. W 2013 r. ukończył z bardzo dobrymi ocenami aplikację radcowską prowadzoną przez Okręgową Izbę Radców Prawnych w Kielcach. Adrian Salus został wpisany na listę radców prawnych w sierpniu 2013 r. Od tego czasu świadczy profesjonalne doradztwo prawne. Kandydat objęty jest ustawicznym cyklem szkoleniowym z różnych dziedzin prawa, który trwale podnosi kwalifikacje zawodowe i buduje nowe kompetencje. Jeszcze jako aplikant radcowski pan Adrian Salus w swojej pracy zawodowej miał bezpośrednią styczność z prawem ustrojowym, będąc doradcą członków śledczej komisji sejmowej. Już wtedy poznał bardzo dobrze niuanse funkcjonowania samego parlamentu i przynależnych mu procedur. Przez wiele lat obsługi prawnej podmiotów biorących udział w życiu publicznym kandydat wyspecjalizował się w praktyce prawa ustrojowego, ze szczególnym uwzględnieniem procesów wyborczych, legislacyjnych oraz zagadnień związanych z funkcjonowaniem i działalnością organów władzy ustawodawczej, wykonawczej i partii politycznych. W latach 2015–2016 pełnił funkcję społecznego doradcy prawnego prezesa Rady Ministrów. Od niemal 15 lat wykonuje pracę zawodową związaną z poszczególnymi zagadnieniami prawa konstytucyjnego, prawa publicznego. Od ponad 10 lat jako radca prawny świadczy profesjonalne doradztwo prawne osobom fizycznym i prawnym, łącznie z pełną reprezentacją procesową. Doświadczenie kandydata poszerza byłe wieloletnie członkostwo w organach nadzorczych licznych spółek kapitałowych. Aktualnie kandydat nie jest członkiem żadnych organów nadzoru Pan Adrian Salus zbudował swoje kompetencje w zakresie doradztwa prawnego w sektorze biznesu na wieloletniej współpracy z licznymi podmiotami prawa handlowego, także jako doradca organów zarządczych do spraw prawnych. Kandydat posiada bardzo duże doświadczenie w zakresie znajomości funkcjonowania organów i instytucji administracji publicznej, także w ujęciu praktycznym. Ponadto w bieżącej działalności wyspecjalizował się w praktyce praw podmiotowych, w szczególności związanych z ochroną dóbr osobistych i praw wizerunkowych. Kompetencję tę zbudował, zapewniając kompleksową obsługę prawną w zakresie doradztwa i zastępstwa procesowego wielu osobom fizycznym i prawnym. Częstą aktywnością zawodową kandydata jest również praktyka prawa prasowego i autorskiego. Radca prawny pan Adrian Salus udziela się także w ramach pomocy prawnej pro bono osobom potrzebującym. W tym zakresie już w czasie studiów pracował nieodpłatnie w poradni prawnej. Kandydat swobodnie porozumiewa się w języku angielskim, zna podstawy języka niemieckiego i rosyjskiego. Zarówno wykształcenie, jak i bogate doświadczenie zawodowe wskazują, iż pan Adrian Salus jest dobrym kandydatem na stanowisko członka Trybunału Stanu. Następnym kandydatem na członka jest pan Maciej Gustaw Zaborowski, który jest adwokatem, wykładowcą, certyfikowanym mediatorem oraz działaczem społecznym. Urodzony 10 lutego 1984 r., absolwent Wydziału Prawa i Administracji na Uniwersytecie Warszawskim. Ukończył także Harvard Law School oraz studia podyplomowe – prawo własności intelektualnej na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego, a także studia podyplomowe – prawo dowodowe na Wydziale Prawa i Administracji Uniwersytetu Kardynała Stefana Wyszyńskiego. Odbył także aplikację w Izbie Adwokackiej w Warszawie zakończoną zdanym egzaminem. Ukończył szereg innych kursów i szkoleń za granicą. Swoje doświadczenie zawodowe zdobywał m.in. w kilku znanych warszawskich kancelariach adwokackich, także w Ambasadzie Rzeczypospolitej Polskiej w Rzymie, w Ministerstwie Sprawiedliwości i w Sejmie Rzeczypospolitej Polskiej, gdzie jest współautorem m.in. raportu sejmowej Komisji Śledczej do zbadania sprawy przebiegu procesu legislacyjnego ustaw nowelizujących ustawę z dnia 29 lipca 1992 r. o grach i zakładach wzajemnych i wydanych na ich podstawie przepisów wykonawczych w zakresie dotyczącym gier na automatach o niskich wygranych i wideoloterii oraz do zbadania legalności działania organów administracji rządowej badających ten proces. Zawodowy mediator Centrum Mediacji przy Naczelnej Radzie Adwokackiej oraz stały mediator przy Prokuratorii Generalnej Rzeczypospolitej Polskiej. Wykładowca akademicki. Współautor publikacji książkowych z zakresu prawa karnego, w tym komentarza: Prawo obrotu pieniężnego. Aktualnie jako adwokat jest partnerem zarządzającym w kancelarii Kopeć Zaborowski Adwokaci i Radcowie Prawni. Ekspert ministra sprawiedliwości w zakresie zmian w prawie karnym. Współautor nowelizacji Kodeksu karnego, Kodeksu karnego wykonawczego, Kodeksu postępowania karnego, w tym m.in. dotyczących tzw. konfiskaty rozszerzonej, rozszerzonej odpowiedzialności karnej biegłych sądowych, tzw. przestępstwa niealimentacji oraz odpowiedzialności podmiotów zbiorowych za czyny zabronione pod groźbą kary. Od najmłodszych lat związany z działalnością pro publico bono, w tym m.in. pełniący obowiązki przewodniczącego Rady Fundatorów Fundacji Odpowiedzialność Obywatelska. Stały komentator z zakresu bieżących wydarzeń w aspekcie prawnym w telewizji i w prasie. Trzykrotnie wskazany przez „Dziennik Gazeta Prawna” w rankingu 50. najbardziej wpływowych prawników w Polsce. Wielokrotnie nagradzany oraz wyróżniany w polskich i międzynarodowych rankingach prawniczych, w tym również w rankingu dziennika „Rzeczpospolita” jako ekspert lider w dziedzinie prawa karnego dla biznesu. Nagrodzony także dodatkowo za działalność pro publico bono przez Okręgową Radę Adwokacką w Warszawie. Wybrany przez Sejm Rzeczypospolitej Polskiej VIII i IX kadencji na sędziego Trybunału Stanu. W lutym 2019 r. (Dzwonek) odznaczony przez prezydenta Rzeczypospolitej Medalem Stulecia Odzyskanej Niepodległości. Kolejną osobą… Panie marszałku, jeszcze dwie kandydatury.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Ale jakby pani mogła w miarę skrótowo. Dziękuję.",
                },
                {
                    "speaker": "Poseł Lidia Burzyńska",
                    "content": "Pan Marek Czeszkiewicz, urodzony w 1961 r. w Augustowie, adwokat, sędzia Trybunału Stanu VIII i IX kadencji, jest absolwentem Wydziału Prawa w Białymstoku, który ukończył z wyróżnieniem, jak również ukończył podyplomowe studia problematyki zorganizowanej przestępczości i terroryzmu na Uniwersytecie Warszawskim. Brał udział w przygotowaniu i tworzeniu specjalistycznych programów rządowych, resortowych, prowadził szkolenia, kursy specjalistyczne dla aplikantów adwokackich, radców prawnych oraz organów administracji publicznej, uczestniczył w przygotowaniu i tworzeniu projektów ustaw, m.in. o Straży Marszałkowskiej. Wielokrotnie nagradzany za wyniki i osiągnięcia. Publikacje z zakresu: zwalczanie przestępczości zorganizowanej w Polsce, świadek anonimowy – incognito, zakazy dowodowe dotyczące tajemnicy adwokackiej w polskim procesie karnym, model doradztwa podatkowego Od wielu lat poświęca się m.in. działalności pro bono, m.in. jako wolontariusz brał udział w bezpośredniej pomocy w czasie powodzi w Tarnobrzegu i Sandomierzu w 2010 r. Jest też wolontariuszem w hospicjum, m.in. fundacji pomocy chorym dzieciom z chorobami nowotworowymi oraz Caritas. Jest także instruktorem ZHP. Zarówno wykształcenie, jak i bogate doświadczenie zawodowe wskazują, iż pan Marek Czeszkiewicz jest dobrym kandydatem na stanowisko członka Trybunału Stanu. Ostatni kandydat przedstawiany przeze mnie Wysokiej Izbie. Pan Marcin Wawrzyniak urodził się 16 maja 1984 r. w Warszawie. Odbył studia na Wydziale Prawa i Administracji uniwersytetu w Warszawie. Dyplom obronił z oceną bardzo dobrą. W latach 2009–2012 odbywał aplikację adwokacką w Warszawie pod patronatem mecenas Magdaleny Fertak. Od 2013 r. jest adwokatem, członkiem Izby Adwokackiej, a od września 2018 r. także członkiem Okręgowej Izby Radców Prawnych w Warszawie. Wykonuje do dziś zawód adwokata, a także radcy prawnego. Wykładowca licznych szkoleń, seminariów, współautor pięciu książek prawniczych, w tym aktualnego komentarza do ustawy o partnerstwie publiczno-prawnym, oraz autor kilkudziesięciu publikacji i artykułów o tej samej tematyce. Od 2018 r. prezes Fundacji Sursum Corda przy Bazylice Świętego Krzyża w Warszawie, kanclerz chorągwi Świętego Krzyża Zakonu Rycerzy Jana Pawła II, członek Trybunału Stanu w latach 2019–2023. Zarówno wykształcenie, jak i bogate doświadczenie zawodowe wskazują, iż pan Marcin Wawrzyniak jest dobrym kandydatem na stanowisko członka Trybunału Stanu. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, pani poseł. Proszę teraz o zabranie głosu pana posła Arkadiusza Myrchę w celu przedstawienia kandydata na zastępcę przewodniczącego Trybunału Stanu pana Jacka Dubois i kandydata na członka Trybunału Stanu pana Adama Koczyka, zgłoszonych przez posłów z Klubu Parlamentarnego Koalicja Obywatelska – Platforma Obywatelska, Nowoczesna, Inicjatywa Polska, Zieloni.",
                },
                {
                    "speaker": "Poseł Arkadiusz Myrcha",
                    "content": "Dziękuję. Panie Marszałku! Wysoka Izbo! Przypadł mi niezwykły zaszczyt przedstawienia dwóch niezwykłych prawników, pana mecenasa Jacka Dubois i pana mecenasa Adama Koczyka, którzy staną się członkami Trybunału Stanu. Pan mecenas, adwokat Jacek Dubois, sylwetka powszechnie znana, szanowany za swoje osiągnięcia w dziedzinie prawa karnego, słynny obrońca osób pokrzywdzonych przez aparat władzy, przez ostatnie lata zasłynął wieloma znakomitymi obronami zarówno na etapie postępowania przygotowawczego, jak i na etapie postępowania sądowego, świadcząc najwyższej jakości usługi pro publico bono. Pan adwokat Jacek Dubois w swoim dorobku ma już doświadczenie pracy w charakterze członka Trybunału Stanu, po raz pierwszy został nim w 2011 r., a w 2012 r. został wybrany na stanowisko zastępcy przewodniczącego Trybunału Stanu. Następnie w latach 2015 i 2019 został wybrany na sędziego Trybunału Stanu. To tylko potwierdza, że ma bogate doświadczenie zarówno zawodowe, jak i merytoryczne, żeby piastować niezwykle istotną funkcję członka Trybunału Stanu, tego, który ma osądzać przedstawicieli władzy. Pan mecenas Jacek Dubois w latach 1981–1986 odbył studia prawnicze na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego, a od 1986 r. jest członkiem Okręgowej Rady Adwokackiej w Warszawie. W latach 1986–1990 odbywał aplikację adwokacką pod patronatem pani mecenas Ewy Milewskiej-Celińskiej. W 1990 r. zdał egzamin adwokacki i rozpoczął praktykę w Zespole Adwokackim nr 25 w Warszawie, a od 1995 r. nieprzerwanie pracuje i prowadzi kancelarię Dubois i Wspólnicy, Kancelaria Adwokacko-Radcowska sp.j. W latach 2000–2005 pełnił funkcję zastępcy rzecznika dyscyplinarnego przy Okręgowej Radzie Adwokackiej w Warszawie. W samorządzie adwokackim pełnił także funkcję członka komisji do spraw kontaktów z mediami. Od 2007 r. jest wykładowcą prawa karnego i prawa karnego procesowego w ramach komisji szkolenia aplikantów. Pan mecenas Jacek Dubois spełnia oczywiście wszystkie warunki formalne, żeby zostać członkiem Trybunału Stanu, podobnie jak pan Adam Koczyk. Pan Adam Koczyk w 2015 r. z wyróżnieniem zdał państwowy egzamin radcowski, po ukończeniu 3-letniej aplikacji radcowskiej przy Okręgowej Izbie Radców Prawnych w Krakowie, i od tego czasu wykonuje zawód radcy prawnego przy Okręgowej Izbie Radców Prawnych w Katowicach. Posiada bogate doświadczenie zawodowe w świadczeniu pomocy prawnej, jak i dydaktycznej. Od 2013 r. zatrudniony jest w Zakładzie Prawa i Administracji Uniwersytetu WSB Merito w Poznaniu z filią w Chorzowie, gdzie prowadzi zajęcia z różnych dziedzin. Specjalizuje się w dziedzinie prawa cywilnego i postępowania cywilnego. Pan mecenas Koczyk od wielu lat jest wykładowcą kursów specjalistycznych z wybranych dziedzin prawa, a swoje doświadczenie zawodowe i zdobytą wiedzę wykorzystuje także w działalności społecznej, gdyż od lat jest związany ze stowarzyszeniami niosącymi pomoc osobom z niepełnosprawnościami. Pan Adam Koczyk jest autorem kilkunastu prac naukowych, w tym części monografii wydanej przez wydawnictwo C.H.Beck oraz podręcznika podstaw prawa dla studentów ekonomii, a także jest autorem wielu publikacji z zakresu energetyki, prawa energetycznego, jak chociażby „Problematyka klauzul abuzywnych w umowach na dostarczanie energii elektrycznej” czy „Prawo gospodarcze dla ekonomistów”. Jest także autorem wielu glos, komentarzy do wyroków i orzeczeń Sądu Najwyższego. Panie Marszałku! Wysoka Izbo! Z najwyższą przyjemnością i zaszczytem rekomenduję tych dwóch panów mecenasów na członków Trybunału Stanu. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Proszę teraz o zabranie głosu pana posła Krzysztofa Śmiszka w celu przedstawienia kandydatki na członka Trybunału Stanu pani Kamili Ferenc, zgłoszonej przez posłów z Klubu Parlamentarnego Koalicja Obywatelska – Platforma Obywatelska, Nowoczesna, Inicjatywa Polska, Zieloni, Koalicyjnego Klubu Parlamentarnego Lewicy (Nowa Lewica, PPS, Razem, Unia Pracy), Klubu Parlamentarnego Polska 2050 – Trzecia Droga i Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Krzysztof Śmiszek",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Mam zaszczyt zaprezentować sylwetkę pani mecenas Kamili Ferenc jako kandydatki na członkinię Trybunału Stanu. Pani mecenas w 2015 r. ukończyła studia prawnicze na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego. W czasie studiów doświadczenie zawodowe zdobywała w biurze Trybunału Konstytucyjnego, w Biurze Rzecznika Praw Obywatelskich, a także w kancelariach prawnych. Jest wpisana na listę adwokatów Izby Adwokackiej w Warszawie. Jest praktykującą adwokatką współpracującą z organizacjami pozarządowymi, przede wszystkim z Fundacją na Rzecz Kobiet i Planowania Rodziny Federa. W pracy zawodowej zajmuje się w szczególności prawami człowieka, wolnościami obywatelskimi, praworządnością, rządami prawa, zdrowiem reprodukcyjnym, przeciwdziałaniem przemocy domowej i seksualnej oraz dyskryminacji. Pani mecenas Kamila Ferenc jest autorką projektów aktów prawnych, projektów ustaw oraz jest wykładowczynią w ramach licznych szkoleń i seminariów, także na poziomie międzynarodowym. W 2017 r. ukończyła seminarium dla praktyków prawa EU Gender Equality Law w Akademii Prawa Europejskiego w niemieckim Trewirze, a w 2019 r. – Women’s Human Right Training Institute. W latach 2014–2016 była ambasadorką Rzecznika Praw Obywatelskich i promowała działalność Biura Rzecznika Praw Obywatelskich. W 2020 r. została nominowana w konkursie Rising Stars Prawnicy – liderzy jutra, a w 2021 r. została prawniczką pro bono w konkursie dziennika „Rzeczpospolita”. W 2022 r. została nominowana do nagrody Medal Wolności Słowa w kategorii obywatel/obywatelka przyznawanej przez Fundację Grand Press. W 2023 r. została wpisana na listę 25 prawniczek w biznesie magazynu „Forbes Women”. Prowadzi liczne strategiczne litygacje przed Europejskim Trybunałem Praw Człowieka w Strasburgu. Z uwagi na wszystkie te osiągnięcia, karierę zawodową, zaangażowanie społeczne, wierność konstytucji i literze prawa pani mecenas Kamila Ferenc to osoba kompetentna, doświadczona i wiarygodna. Jest to właściwa kandydatka na funkcję członkini Trybunału Stanu. Dziękuję bardzo.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Bardzo dziękuję, panie pośle. Proszę o zabranie głosu pana posła Roberta Kropiwnickiego w celu przedstawienia kandydatów na członków Trybunału Stanu: pani Sabiny Grabowskiej i pana Przemysława Rosatiego, zgłoszonych przez posłów z Klubu Parlamentarnego Koalicja Obywatelska – Platforma Obywatelska, Nowoczesna, Inicjatywa Polska, Zieloni.",
                },
                {
                    "speaker": "Poseł Robert Kropiwnicki",
                    "content": "Panie Marszałku! Wysoka Izbo! Mam zaszczyt przedstawić kandydaturę pani prof. Sabiny Grabowskiej, która jest polską prawniczką, radcą prawnym, specjalizuje się w prawie konstytucyjnym, jest doktorem habilitowanym nauk prawnych. Pani profesor specjalizuje się w kwestii odpowiedzialności konstytucyjnej. Jej główne publikacje dotyczyły właśnie instytucji odpowiedzialności konstytucyjnej głowy państwa, ale też w ogóle szeroko rozumianej instytucji Trybunału Stanu i mechanizmów związanych z odpowiedzialnością konstytucyjną. Przykładowe publikacje to „Model odpowiedzialności konstytucyjnej prezydenta we współczesnych państwach europejskich”, „Odpowiedzialność konstytucyjna głowy państwa przed parlamentem na przykładzie republik europejskich” czy „Trybunał Stanu jako specjalny organ orzekający w sprawie odpowiedzialności konstytucyjnej prezydenta”. Na swoim koncie ma ponad 150 publikacji, w dużej mierze właśnie związanych z odpowiedzialnością konstytucyjną, więc myślę, że to jest bardzo dobra kandydatura. Kandydatka jest wyspecjalizowana w dziedzinie szeroko rozumianej odpowiedzialności konstytucyjnej, a w szczególności w kwestii odpowiedzialności głowy państwa. Może to być bardzo cenny wkład w prace merytoryczne zarówno Trybunału Stanu, jak i orzekania w ogóle w tej instytucji. Liczę na to, że wiedza i doświadczenie badawcze pani profesor będą bardzo przydatne w pracy w Trybunale Stanu. Pani profesor jest dziekanem w Kolegium Nauk Społecznych Uniwersytetu Rzeszowskiego. Jest czynnym naukowcem, jak również recenzentem wielu prac naukowych, jest redaktorem naczelnym „Przeglądu Prawa Konstytucyjnego”, więc ma ogromne doświadczenie w tej sprawie. Druga kandydatura, którą mam zaszczyt państwu przedstawić, to kandydatura pana mecenasa Przemysława Rosatiego, który jest prezesem Naczelnej Rady Adwokackiej. W samorządzie adwokackim działa od 2012 r. Studia ukończył na Wydziale Prawa i Administracji Uniwersytetu Marii Curie-Skłodowskiej, a od 2006 r. jest członkiem Izby Adwokackiej w Warszawie. Aplikację ukończył w 2010 r. i zdał wtedy również egzamin adwokacki. W swojej karierze prowadził wiele ważnych spraw, ale też poświęca się bardzo mocno samorządowi adwokackiemu i ma doskonałe przygotowanie w zakresie procedury karnej, procedury prawa procesowego, tak żeby móc dobrze pełnić funkcję sędziego Trybunału Stanu. Mam nadzieję, że obie kandydatury spotkają się z przychylnością Wysokiej Izby. Dziękuję bardzo.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Proszę teraz o zabranie głosu pana posła Sławomira Nitrasa w celu przedstawienia kandydatów na członków Trybunału Stanu: pana Marka Mikołajczyka i pana Piotra Benedykta Zientarskiego, zgłoszonych przez posłów z Klubu Parlamentarnego Koalicja Obywatelska – Platforma Obywatelska, Nowoczesna, Inicjatywa Polska, Zieloni.",
                },
                {
                    "speaker": "Poseł Sławomir Nitras",
                    "content": "Dziękuję, panie marszałku. To niewątpliwy zaszczyt móc w Sejmie X kadencji zgłosić nazwiska dwóch wybitnych prawników, adwokatów na członków Trybunału Stanu. Jestem posłem ziemi zachodniopomorskiej, tym milej mi zgłosić dwóch wybitnych, jak powiedziałem, adwokatów reprezentujących właśnie województwo zachodniopomorskie. Pierwszym z nich jest pan Marek Mikołajczyk. Marek Mikołajczyk urodził się 14 października 1952 r. Jest adwokatem. W 1971 r. rozpoczął studia na Wydziale Prawa i Administracji Uniwersytetu im. Adama Mickiewicza w Poznaniu. Studia ukończył w 1975 r., po czym w tym samym roku rozpoczął aplikację sędziowską w Sądzie Wojewódzkim w Szczecinie, którą ukończył zdaniem egzaminu sędziowskiego w 1978 r. Po ukończonej aplikacji nie ubiegał się o nominację sędziowską i podjął decyzję o rozpoczęciu aplikacji adwokackiej. Marek Mikołajczyk w 1983 r. zdał egzamin adwokacki i po uzyskaniu wpisu na listę adwokatów od tego czasu do dzisiaj wykonuje zawód adwokata w Szczecińskiej Izbie Adwokackiej. Marek Mikołajczyk w ramach prowadzonej działalności zawodowej zajmuje się reprezentacją w sporach sądowych ze szczególnym wyprofilowaniem działalności na prowadzenie obrony w sprawach karnych. Naturalnym środowiskiem prowadzenia działalności zawodowej przez pana adwokata Marka Mikołajczyka od początku jest wykonywanie jej na sali sądowej. Pan Marek Mikołajczyk pełnił również szereg zaszczytnych i ważnych funkcji w samorządzie zawodowym. W latach 1992–1998 był wicedziekanem Szczecińskiej Izby Adwokackiej. W latach 1998–2004 oraz 2010–2013 pełnił funkcję dziekana Okręgowej Rady Adwokackiej w Szczecinie. Niezależnie od ww. pełnionych funkcji nieprzerwanie od roku 1998 do dnia dzisiejszego jest członkiem Naczelnej Rady Adwokackiej. Mandat do pełnienia funkcji uzyskiwał oczywiście w wyniku wyborów przez krajowe zjazdy adwokatury. W związku z przedstawionymi informacjami pan Marek Mikołajczyk jest osobą doskonale przygotowaną do pełnienia funkcji członka Trybunału Stanu. Kandydat w toku swojej działalności publicznej i zawodowej udowodnił wysoki poziom wiedzy merytorycznej oraz nieskazitelność charakteru, które to przymioty dają gwarancję należytego wypełnienia przez kandydata obowiązków członka Trybunału Stanu. Jeśli pan marszałek pozwoli, od razu druga kandydatura.",
                },
                {"speaker": "Marszałek", "content": "Proszę bardzo."},
                {
                    "speaker": "Poseł Sławomir Nitras",
                    "content": "Pan Piotr Benedykt Zientarski. Postać znana, parlamentarzysta, doktor habilitowany nauk prawnych w zakresie prawa konstytucyjnego. Profesor Akademii Nauk Stosowanych Wyższej Szkoły Gospodarki Euroregionalnej im. Alcide De Gasperi w Józefowie, adwokat. Kandydat w 1975 r. uzyskał tytuł magistra prawa na Wydziale Prawa i Administracji Uniwersytetu im. Adama Mickiewicza w Poznaniu. W 1977 r. zdał egzamin sędziowski i radcowski, następnie w 1981 r. – egzamin adwokacki, a także uzyskał wpis na listę adwokatów. Pan Piotr Benedykt Zientarski od 2010 r. posiada stopień doktora nauk prawnych, a od 2020 r. – stopień doktora habilitowanego nauk prawnych. W latach 80. był obrońcą działaczy opozycyjnych, doradcą i pełnomocnikiem biskupa diecezji koszalińsko-kołobrzeskiej. Został odznaczony medalem adwokatury dla obrońcy praw człowieka i odznaką honorową „Adwokatura Zasłużonym” Ze względu na swoją postawę adwokacką wobec Służby Bezpieczeństwa i odmowę współpracy uznany został przez Instytut Pamięci Narodowej za pokrzywdzonego. Pan Piotr Benedykt Zientarski był naszym kolegą z ław parlamentarnych, był posłem IX, ostatniej kadencji. Przez cztery kadencje pełnił zaszczytną funkcję senatora Rzeczypospolitej Polskiej. W latach 2007– 2015 reprezentował Senat Rzeczypospolitej Polskiej w Krajowej Radzie Sądownictwa. W latach 2009–2015 przewodniczył senackiej Komisji Ustawodawczej. Dwukrotnie został odznaczony medalem ministra sprawiedliwości w uznaniu zasług w realizacji wyroków Trybunału Konstytucyjnego oraz wkładu w rozwój praworządności w Polsce. Od roku 2019 pełnił funkcję przewodniczącego Parlamentarnego Zespołu Obrony Praworządności. Reprezentował parlament na forach międzynarodowych, m.in. Komisji Weneckiej i Parlamentu Europejskiego. Autor kilkuset poprawek do ustaw ustrojowych i kodeksowych, m.in. przyczynił się do rozpoczęcia i kontynuowania realizacji orzeczeń Trybunału Konstytucyjnego. Jest autorem i redaktorem naukowym kilkudziesięciu publikacji naukowych w zakresie Prawa konstytucyjnego. Był członkiem kolegiów redakcyjnych wielu prestiżowych wydawnictw prawniczych, m.in. „Palestry”, członkiem rady naukowej „Humanistycznych Zeszytów Naukowych Prawa Człowieka”, przewodniczącym komitetów organizacyjnych, naukowych ponad 30 konferencji naukowych. W związku z powyższym pan Piotr Benedykt Zientarski jest osobą doskonale przygotowaną do pełnienia funkcji członka Trybunału Stanu. Kandydat w toku swojej działalności zawodowej udowodnił wysoki poziom wiedzy merytorycznej oraz nieskazitelność charakteru, które to przymioty dają gwarancję należytego wypełnienia przez kandydata obowiązków członka Trybunału Stanu. Dziękuję, panie marszałku. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Bardzo dziękuję, panie pośle. Proszę teraz o zabranie głosu pana posła Krzysztofa Paszyka w celu przedstawienia kandydata na członka Trybunału Stanu pana Marka Małeckiego, zgłoszonego przez posłów z Klubu Parlamentarnego Polska 2050 – Trzecia Droga i Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Krzysztof Paszyk",
                    "content": "Szanowny Panie Marszałku! Panie i Panowie Posłowie! Mam w imieniu Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga przyjemność zaprezentowania jednego z naszych kandydatów do Trybunału Stanu, jakim jest mecenas Marek Małecki, który urodził się 9 stycznia 1972 r. w Warszawie. Jest adwokatem, działaczem społecznym, ale też sędzią sportowym. Od urodzenia mieszka w Warszawie, gdzie ukończył szkołę podstawową i liceum ogólnokształcące. W 1996 r. ukończył z wyróżnieniem studia prawnicze na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego. Był szefem samorządu studenckiego, członkiem rady wydziału i senatu uczelni, członkiem parlamentu studenckiego, członkiem NZS-u. W latach 1996–2000 odbył aplikację adwokacką przy Okręgowej Radzie Adwokackiej w Warszawie pod patronatem adwokata Eugeniusza Baworowskiego i kierownictwem adwokat Grażyny Włodkiewicz i w 2000 r. zdał egzamin adwokacki. Karierę prawniczą rozpoczął w 1992 r. w Warszawie w oddziale amerykańskiej kancelarii prawniczej. Odbył szkolenia zawodowe we Francji, w Austrii, Wielkiej Brytanii, Szwajcarii, Niemczech i Stanach Zjednoczonych. Po 10 latach pracy dla amerykańskiej kancelarii w Warszawie, Chicago, Nowym Jorku i Londynie został szefem departamentu prawnego jednego z najbardziej wiarygodnych banków na świecie. Zajmuje się sprawami głównie z zakresu prawa cywilnego, gospodarczego i karnego, ze szczególnym uwzględnieniem tzw. przestępstw białych kołnierzyków. Jest mecenasem sztuki i filantropem, którego głównym celem jest ochrona dorobku kulturalnego. Jego zbiory można oglądać np. na Zamku Królewskim w Warszawie czy w Muzeum Narodowym w Warszawie. Udziela również pomocy prawnej i finansowej muzykom, kompozytorom, organizacjom non profit promującym rozwój kultury i sztuki. Od 2001 r. wykonuje czynnie zawód adwokata. Brał udział w najciekawszych procesach sądowych przełomu XX i XXI w. Współtworzył jako doradca prawny najważniejsze instytucje państwowe w Polsce. Od 2012 r. jest założycielem kancelarii prawniczej Kancelaria Adwokacja Marek Małecki z siedzibą w Warszawie. Wysoka Izbo! Osoba pana mecenasa Marka Małeckiego ma wszelkie kwalifikacje etyczne, moralne, wszelkie kompetencje i dorobek zawodowy do tego, aby zająć miejsce w Trybunale Stanu z rekomendacji polskiego Sejmu. Dziękuję bardzo.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Teraz proszę o zabranie głosu pana posła Piotra Zgorzelskiego w celu przedstawienia kandydata na członka Trybunału Stanu pana Józefa Zycha, zgłoszonego przez posłów z Klubu Parlamentarnego Polska 2050 – Trzecia Droga i Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga. Bardzo proszę, panie marszałku",
                },
                {
                    "speaker": "Poseł Piotr Zgorzelski",
                    "content": "Panie Marszałku! Wysoka Izbo! Mam ogromny zaszczyt przedstawić w imieniu naszego klubu parlamentarnego kandydaturę pana marszałka Józefa Zycha na członka Trybunału Stanu. Pan marszałek Józef Zych urodził się 23 marca 1938 r. w Giedlarowej, województwo podkarpackie. Jest doktorem nauk prawnych, radcą prawnym spełniającym wymogi dotyczące zajmowania stanowiska sędziego. Marszałek Sejmu II kadencji, trzykrotny wicemarszałek Sejmu i dwukrotny marszałek senior. Był organizatorem samorządu radców prawnych oraz jego prezesem I i II kadencji. Autor ponad 20 pozycji książkowych oraz ponad 300 artykułów na tematy prawnicze. W szczególności zajmował się prawem konstytucyjnym i ubezpieczeniowym. Przewodniczył m.in. Komisji Odpowiedzialności Konstytucyjnej, a także był członkiem Trybunału Stanu w latach 2015–2019. Jako przewodniczący Zgromadzenia Narodowego wniósł istotny wkład w przygotowanie Konstytucji Rzeczypospolitej Polskiej z 1997 r. Jako jedyny polski prawnik na zaproszenie Parlamentu Europejskiego uczestniczył w pracach nad konstytucją europejską. Obecnie został zaproszony do prac nad ustaleniem kryteriów, jakie musi spełniać państwo, aby uznać je za państwo praworządne. Prace są prowadzone przez przedstawicieli nauki prawa ośmiu państw Unii Europejskiej. W czasie sprawowania funkcji marszałka Sejmu, a także przewodniczącego komisji dbał o autorytet Sejmu i posłów. Wykazał się bezstronnością w czasie procedur legislacyjnych nad projektami ustaw, a także w rozwiązywaniu trudnych spraw dotyczących posłów. W okresie prac nad konstytucją oraz w czasie przygotowań do ratyfikacji konkordatu jako umowy międzynarodowej wielokrotnie spotykał się z papieżem Janem Pawłem II. M.in. z prezesem Polskiego Stronnictwa Ludowego Władysławem Kosiniakiem-Kamyszem był inicjatorem postępowania kasacyjnego w sprawie uniewinnienia Wincentego Witosa oraz innych skazanych w procesie brzeskim. Był pełnomocnikiem społecznym w tym postępowaniu przed Sądem Najwyższym. Proces zakończył się uniewinnieniem przed Sądem Najwyższym Wincentego Witosa i pozostałych ośmiu skazanych. Na arenie międzynarodowej cieszy się uznaniem, o czym świadczy m.in. fakt odznaczenia go przez prezydenta Republiki Francuskiej Legią Honorową Wielkiego Oficera. Doświadczenie parlamentarne, znajomość problemów konstytucyjnych, a także procedur sądowych oraz dotychczasowa postawa gwarantują, że będzie przydatny w pracach Trybunału Stanu. Panie i Panowie Posłowie! W imieniu Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga rekomenduję osobę pana marszałka Józefa Zycha jako kandydata do Trybunału Stanu. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie marszałku. Bardzo proszę o zabranie głosu pana posła Pawła Śliza w celu przedstawienia kandydata na członka Trybunału Stanu pana Marcina Radwana-Röhrenschefa, zgłoszonego przez posłów z Koalicyjnego Klubu Parlamentarnego Lewicy (Nowa Lewica, PPS, Razem, Unia Pracy), Klubu Parlamentarnego Polska 2050 – Trzecia Droga i Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Paweł Śliz",
                    "content": "Panie Marszałku! Wysoka Izbo! Jest mi bardzo miło, że mogę przedstawić kandydata na członka Trybunału Stanu, pana mecenasa Marcina Radwana-Röhrenschefa. Trybunał Stanu jest fundamentem ochrony konstytucji. Wspomaga kontrolę władzy wykonawczej. Dlatego jako Polska 2050 podeszliśmy do tego problemu z najwyższą starannością. Odbyliśmy konsultacje z pięcioma zgłoszonymi przez nas kandydatami. Spośród tych kandydatów, którzy wykazali się wysokim poziomem wiedzy merytorycznej, ogromnym doświadczeniem i etyką zawodową, a także etosem zawodowym, musieliśmy dokonać trudnego wyboru. Dokonaliśmy tego wyboru. Co nas przekonało? Przede wszystkim powściągliwość pana mecenasa, jeśli chodziło o konkretne pytania związane z przyszłym wykonywaniem przez niego obowiązków sędziego Trybunału Stanu. To pokazało, że jest to gwarancja jego niezawisłości i rzetelności w powierzonych mu i wykonywanych przez niego obowiązkach. Pan mecenas Marcin Radwan-Röhrenschef jest adwokatem od 25 lat, od 1998 r. Wcześniej ukończył Uniwersytet Warszawski. Jest doktorem nauk prawnych, od 2009 r. – wspólnikiem w kancelarii, która jest jednym z liderów krajowych i międzynarodowych rankingów w zakresie sporów gospodarczych. Zajmował się także obsługą prawną bardzo dużych projektów infrastrukturalnych, reprezentował Skarb Państwa w postępowaniu przed TSUE, a także występował w Trybunale Konstytucyjnym, reprezentując stowarzyszenie Integracja w sprawach z zakresu Kodeksu wyborczego, zabiegając o uprawnienia niepełnosprawnych w procesie wyborczym. Jest także sędzią Wyższego Sądu Dyscyplinarnego przy Naczelnej Radzie Adwokackiej. Pan Marcin Radwan swoim bogatym doświadczeniem zawodowym i dotychczasową praktyką daje pełną rękojmię tego, że podjęte obowiązki członka Trybunału Stanu będzie wykonywał z poszanowaniem prawa i pełnym zaangażowaniem. Z całą pewnością i sercem pełnym nadziei chciałbym zarekomendować kandydaturę pana mecenasa Marcina Radwana-Röhrenschefa. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo. Bardzo proszę o zabranie głosu pana posła Bartłomieja Peja. Przepraszam, nie wiedziałem, czy pan poseł się deklinuje. (Wypowiedź poza mikrofonem) Nie deklinuje się pan poseł. Zapamiętam na zawsze, że pan poseł Bartłomiej Pejo się nie deklinuje. Właśnie jego zapraszam w celu przedstawienia kandydata na członka Trybunału Stanu pana Macieja Miłosza, zgłoszonego przez posłów z Klubu Poselskiego Konfederacja, Klubu Parlamentarnego Polska 2050 – Trzecia Droga i Klubu Parlamentarnego Polskie Stronnictwo Ludowe – Trzecia Droga. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Bartłomiej Pejo",
                    "content": "Panie Marszałku! Wysoka Izbo! W imieniu wszystkich wnioskodawców, w szczególności parlamentarzystów klubu parlamentarnego Konfederacja, mam niewątpliwy zaszczyt przedstawić Wysokiej Izbie kandydaturę pana mecenasa Macieja Miłosza na członka Trybunału Stanu. Pan Maciej Miłosz jest aktualnie radcą prawnym, a zarazem niewykonującym zawodu adwokatem. Piastuje stanowisko członka Państwowej Komisji Wyborczej. Uprzednio z woli Sejmu Rzeczypospolitej Polskiej został wybrany na członka Trybunału Stanu. Pan Maciej Miłosz jest bezpartyjny. Mecenas Maciej Miłosz urodził się w dniu 18 października 1980 r. w Lublinie. Ukończył III Liceum Ogólnokształcące im. Unii Lubelskiej w Lublinie. W latach 1999–2004 studiował prawo na Wydziale Prawa, Prawa Kanonicznego i Administracji Katolickiego Uniwersytetu Lubelskiego. W roku 2004 uzyskał tytuł magistra prawa wskutek obrony pracy „Prawo do własności w świetle orzecznictwa Europejskiego Trybunału Praw Człowieka w Strasburgu”. W latach 2006–2010 odbywał aplikację adwokacką w Izbie Adwokackiej w Lublinie. Od 2010 r., po złożeniu egzaminu adwokackiego, nieprzerwanie wykonywał zawód adwokata, a następnie radcy prawnego w Lublinie, Stalowej Woli i Warszawie. Posiada bogate doświadczenie w doradztwie prawnym na rzecz szeroko pojętego obrotu gospodarczego, co stanowi główny obszar jego praktyki zawodowej. Dwukrotnie był zastępcą członka Komisji Rewizyjnej Izby Adwokackiej w Lublinie. W latach 2004–2007 był doktorantem na seminarium z prawa porównawczego amerykańskiego i europejskiego. W 2003 r. otrzymał stypendium na Uniwersytecie w Gandawie ufundowane przez Ministerstwo do spraw Związku Flamandzkiego Królestwa Belgii. Na przełomie lat 2004 i 2005 odbył staż w Parlamencie Europejskim w Brukseli i Strasburgu. W 2005 r. ukończył podyplomowe studia w Centrum Prawa Amerykańskiego – wspólnej inicjatywie Chicago-Kent College of Law i Katolickiego Uniwersytetu Lubelskiego. W latach 2005–2006 był asystentem w zakładzie naukowym Katolickiego Uniwersytetu Lubelskiego przy udziale Temple University. W przeszłości prawnik fundacji Instytut na rzecz Państwa Prawa w Lublinie. Korporant, reaktywator i prezes założonej w 1922 r. korporacji akademickiej Concordia w Lublinie. Od 2010 r. członek zarządu, a następnie wiceprezes Stowarzyszenia Filistrów Polskich Korporacji Akademickich w Warszawie. Pan mecenas Maciej Miłosz spełnia określone Konstytucją Rzeczypospolitej Polskiej wymagania na członka Trybunału Stanu, to jest posiada wszelkie kwalifikacje uprawniające do zajmowania stanowiska sędziego. Rekomenduję Wysokiej Izbie powołanie pana Macieja Miłosza na członka Trybunału Stanu. Dziękuję bardzo. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Na tym zakończyliśmy prezentację kandydatów. Czy ktoś z pań i panów posłów pragnie zabrać głos w sprawie zgłoszonych kandydatur? Nikt się nie zgłasza. Zgodnie z art. 31 ust. 1 regulaminu Sejmu Sejm wybiera zastępców przewodniczącego i członków Trybunału Stanu bezwzględną większością głosów. Zgodnie z art. 26 ust. 2 regulaminu Sejmu wybór członków Trybunału Stanu odbywa się łącznie, chyba że Sejm postanowi inaczej. Jeżeli nie usłyszę sprzeciwu, będę uważał, że Sejm propozycję przyjął. Sprzeciwu nie słyszę. Przystępujemy więc do głosowania łącznego w sprawie wyboru członków Trybunału Stanu. Kto z pań i panów posłów jest za wyborem dwóch zastępców przewodniczącego i członków Trybunału Stanu, zgodnie z listą kandydatów z druków nr 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 i 51, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? Kto się wstrzymał? Głosowało 436 posłów. Większość bezwzględna wynosi 219. Za głosowało 431 posłów, przeciw – 1, wstrzymało się 4 posłów. Stwierdzam, że Sejm bezwzględną większością głosów wybrał dwóch zastępców przewodniczącego Trybunału Stanu: pana Jacka Dubois i pana Piotra Łukasza Juliusza Andrzejewskiego, a także 16 członków Trybunału Stanu: pana Marka Czeszkiewicza, pana Jana Majchrowskiego, pana Adriana Salusa, pana Piotra Saka, pana Marcina Wawrzyniaka, pana Macieja Gustawa Zaborowskiego, panią Sabinę Grabowską, pana Adama Koczyka, pana Marka Mikołajczyka, pana Przemysława Rosatiego, pana Piotra Benedykta Zientarskiego, pana Marka Małeckiego, pana Józefa Zycha, pana Marcina Radwana-Röhrenschefa, panią Kamilę Ferenc oraz pana Macieja Miłosza. (Oklaski) Dziękuję państwu bardzo za to głosowanie. Został złożony do mnie wniosek formalny, złożył go pan poseł Paweł Jabłoński, o przerwanie posiedzenia Sejmu do dnia 21 listopada do godz. 18. Zechce pan krótko uzasadnić wniosek?",
                },
                {
                    "speaker": "Poseł Paweł Jabłoński",
                    "content": "Panie Marszałku! Wysoki Sejmie! Ten wniosek tak naprawdę ponawiam, lekko go modyfikując, dlatego że wniosek, który został złożony prawidłowo, nie został rozpoznany, a ja chcę dać państwu szansę, żebyście państwo nie bali się… (Głosy z sali: Ooo…) …wyrazić w głosowaniu, co sądzicie o zmianie traktatów, co sądzicie o tym, co ma być głosowane w Parlamencie Europejskim. Stanowisko Prawa i Sprawiedliwości jest jasne. Stanowiska Platformy, Trzeciej Drogi, Lewicy obywatele nie znają. Dajcie szansę sobie, dajcie szansę naszym obywatelom, żeby poznali, jakie jest wasze stanowisko w tej sprawie. Ja wiem, panie marszałku, że dzisiaj o godz. 18 jest posiedzenie Komisji do Spraw Unii Europejskiej. Mam nadzieję, że tam ten projekt również będzie procedowany, choć uważam, że projekt powinien być procedowany tutaj dzisiaj na posiedzeniu plenarnym. Jutro będzie za późno. Dlatego składam wniosek o to, żeby przerwa, którą pan marszałek planował pierwotnie do jutra do godz. 11, została tak naprawdę skrócona, żeby Sejm zebrał się dzisiaj jeszcze raz na posiedzeniu plenarnym i kontynuował prace. (Dzwonek) Sejm, szanowni państwo, nie może być Sejmem niemym (Oklaski), Sejm nie może być Sejmem leniwym. Mamy obowiązek wobec naszych obywateli, żeby w istotnych sprawach pracować. Pracujmy, szanowni państwo. (Poseł Mirosław Suchoń: Na razie robicie zadymę, a nie pracujecie.) (Poseł Paulina Hennig-Kloska: Dajcie pracować rządowi.)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Jest wniosek przeciwny, sprzeciw wobec tego wniosku. Pan poseł Marek Sawicki.",
                },
                {
                    "speaker": "Poseł Marek Sawicki",
                    "content": "Panie Marszałku! Wysoka Izbo! Wniosek przeciwny i apel i do pana ministra Jabłońskiego, i do pana premiera Morawieckiego. Wyjaśnijcie polskiemu społeczeństwu, dlaczego bez zmiany traktatów europejskich zgodziliście się na federalizację finansową Unii Europejskiej. (Oklaski) Mamy wspólne podatki za zgodą pana premiera. Mamy wspólne pożyczki i kredyty i uwspólnotowienie długu za zgodą pana premiera. I mamy zapis o wypłacie pieniędzy na zasadach bliżej nieokreślonej praworządności. Na to wszystko zgodził się pan premier Morawiecki. (Oklaski) A więc przestańcie uprawiać tę hipokryzję i dajcie normalnie w tym Sejmie procedować. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Pan poseł Jabłoński złożył konkretny wniosek formalny. Wnosi o przerwanie posiedzenia Sejmu do godz. 18. (Poseł Zbigniew Krzysztof Kuźmiuk: Panie marszałku…) Przepraszam, w jakim trybie? (Poseł Zbigniew Krzysztof Kuźmiuk: Sprostowanie.) Zaraz, chwila. Był wniosek formalny, był sprzeciw wobec wniosku formalnego, głosujemy nad wnioskiem formalnym. Wniosek formalny dotyczy przerwy, a nie dotyczy naszego stanowiska wobec kwestii, które wyrażane były przez państwa posłów. (Poseł Zbigniew Krzysztof Kuźmiuk: W trybie sprostowania, panie marszałku.) Zapraszam do dania temu świadectwa, panie pośle, w oświadczeniach poselskich, które będą za chwilę, a ja z uwagą tych oświadczeń wysłucham, podobnie jak Wysoka Izba. (Oklaski) (Głos z sali: Brawo!) (Poseł Zbigniew Krzysztof Kuźmiuk: Poseł Sawicki skłamał.) Poddaję wniosek formalny pod głosowanie. Kto z pań i panów posłów jest za zarządzeniem przerwy w obradach, zechce podnieść rękę i nacisnąć przycisk. Kto jest przeciw? (Głos z sali: Skrócenie przerwy.) (Głos z sali: Ale źle pan odczytał.) Nie, proszę pani, pani poseł, wyraźnie odczytałem wniosek i za chwilę, tylko skończmy głosowanie, przeczytam państwu wniosek. Kto się wstrzymał? (Wypowiedź poza mikrofonem) Zaraz, zaraz. Wniosek pana posła Jabłońskiego. Pan poseł wyraźnie wnosi o przerwanie posiedzenia Sejmu RP do godz. 18 w dniu dzisiejszym, tj. 21 listopada 2023 r. Głosowało 455 posłów. Za – 208, przeciw – 247, nikt się nie wstrzymał. Stwierdzam, że Sejm wniosek o przerwę odrzucił. Proszę panią poseł sekretarz o odczytanie komunikatu.",
                },
                {
                    "speaker": "Sekretarz Poseł Aleksandra Karolina Wiśniewska",
                    "content": "Szanowny Panie Marszałku! Wysoka Izbo! Komunikat w sprawie pierwszych posiedzeń stałych komisji sejmowych. Marszałek Sejmu na podstawie art. 20 ust. 2 regulaminu Sejmu zwołał na dzień 21 listopada 2023 r. pierwsze posiedzenia Komisji: — Finansów Publicznych – sala nr 14, budynek G, godz. 15, — Obrony Narodowej – sala nr 24, budynek G, godz. 15, — do Spraw Energii, Klimatu i Aktywów Państwowych – sala nr 12, budynek G, godz. 15, — do Spraw Służb Specjalnych – sala nr 309, budynek S, godz. 15, — Mniejszości Narodowych i Etnicznych – sala nr 12, budynek G, godz. 15.45, — Edukacji, Nauki i Młodzieży – sala nr 14, budynek G, godz. 15.45, — Infrastruktury – sala nr 24, budynek G, godz. 15.45, — Etyki Poselskiej – sala nr 301A, budynek K, godz. 15.45, — Sprawiedliwości i Praw Człowieka – sala nr 14, budynek G, godz. 16.30, — Cyfryzacji, Innowacyjności i Nowoczesnych Technologii – sala nr 12, budynek G, godz. 16.30, — Spraw Zagranicznych – sala nr 22, budynek G, godz. 16.30, — Administracji i Spraw Wewnętrznych – sala nr 14, budynek G, godz. 17.15, — Rolnictwa i Rozwoju Wsi – sala nr 24, budynek G, godz. 17.15, — Polityki Senioralnej – sala nr 12, budynek G, godz. 17.15, — Kultury i Środków Przekazu – sala nr 22, budynek G, godz. 17.15, — Gospodarki Morskiej i Żeglugi Śródlądowej – sala nr 12, budynek G, godz. 18, — Kultury Fizycznej, Sportu i Turystyki – sala nr 24, budynek G, godz. 18, — Gospodarki i Rozwoju – sala nr 14, budynek G, godz. 18, — do Spraw Unii Europejskiej – sala nr 412, budynek U, godz. 18, — Zdrowia – sala nr 14, budynek G, godz. 18.45, — Łączności z Polakami za Granicą – sala nr 24, budynek G, godz. 18.45, — do Spraw Kontroli Państwowej – sala nr 12, budynek G, godz. 18.45, — Samorządu Terytorialnego i Polityki Regionalnej – sala nr 14, budynek G, godz. 19.30, — Ochrony Środowiska, Zasobów Naturalnych i Leśnictwa – sala nr 24, budynek G, godz. 19.30. Dziękuję.",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, pani poseł. Stwierdzam, że na tym zakończyliśmy rozpatrywanie punktów porządku dziennego zaplanowanych na dzień 21 listopada br. Otrzymali państwo informację o tym, kiedy będą odbywać się obrady komisji, podczas których wyłaniane będą prezydia. Komisje będą mogły powstać. Dzięki temu będą mogły być do nich kierowane ustawy, które kluby parlamentarne już wnoszą. Zgodnie z tym, co ustaliliśmy, jutro będziemy procedować nad obywatelskim projektem w sprawie procedury in vitro. Informuję, że zgłosili się posłowie w celu wygłoszenia oświadczeń poselskich. Czy ktoś z pań i panów posłów pragnie jeszcze wygłosić oświadczenie? Nikt się nie zgłasza. Listę posłów zgłoszonych do oświadczeń uważam zatem za zamkniętą. Głos ma poseł Antoni Macierewicz z Klubu Parlamentarnego Prawo i Sprawiedliwość. Czas wypowiedzi w tym punkcie – 3 minuty. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Antoni Macierewicz",
                    "content": "Panie Marszałku! Wysoka Izbo! Ten projekt pana marszałka Hołowni, by oświadczenia trwały 3 minuty, jest zupełnie nową w ciągu ostatnich 30 lat koncepcją. Panie marszałku, pan idzie za daleko. Może pan to ograniczy do 30 sekund? A może do 2 sekund?",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Panie pośle, nie mam takiego zamiaru, ale jeżeli nie zmieści się pan w 3 minutach, z przyjemnością doliczę panu 2 minuty.",
                },
                {
                    "speaker": "Poseł Antoni Macierewicz",
                    "content": "To, co pan robi, to jest po prostu skandal. Realizuje pan to w sposób, który ma pana usprawiedliwić, dlatego że istota polega na tym, że odrzucił pan wraz ze swoją formacją możliwość przekazania przez polski Sejm jednoznacznego stanowiska w sprawie jutrzejszego działania Unii Europejskiej, która ma pozbawić Polskę niepodległości. I to pan właśnie oraz pana formacja sprawiliście, że polski Sejm nie może się przed decyzją Unii Europejskiej publicznie wypowiedzieć. Wy się zgadzacie na to, by Polska została pozbawiona niepodległości. To jest zdrada stanu. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Nie wykorzystał pan nawet tych 3 minut. (Poseł Iwona Ewa Arent: Nie komentuj, prowadź.) Przypominam art. 185 regulaminu Sejmu, który mówi, iż oświadczenia poselskie nie mogą trwać dłuposelskie żej niż 5 minut, co zostawia mi pole do interpretacji i stwierdzenia, że dzisiaj będą trwały 3 minuty. Bardzo proszę, pani poseł Klaudia Jachira z Koalicji Obywatelskiej, a później pan poseł Grzegorz Braun z Konfederacji.",
                },
                {
                    "speaker": "Poseł Klaudia Jachira",
                    "content": "Szeregowy pośle Kaczyński – tymi słowami zwracałam się z mównicy sejmowej przez ostatnie 4 lata poprzedniej kadencji. Mówiłam tak, żeby podkreślić, że niezgodnie z prawem uzurpował pan sobie władzę, która zgodnie z konstytucją przynależy prawowitemu marszałkowi Sejmu i Wysokiej Izbie. Szanowni państwo, przegraliście wybory, więc czas waszego zawłaszczania państwa, omijania konstytucji dobiega końca. Dlatego nie będę się już tak więcej zwracać z tej mównicy. Panie Marszałku! Wysoka Izbo! Powoli odsłaniają się mechanizmy działania odchodzącego reżimu. Przestępcy na szczytach władzy, tajne służby niszczące przeciwników politycznych, skorumpowani dziennikarze, państwowe firmy napędzające machinę propagandy i prokuratura chroniąca cały ten ogromny, chory, mafijny układ. Teraz staje się zrozumiałe pozornie absurdalne zachowanie prezydenta Dudy, który misję tworzenia rządu powierza przegranym. Toną i zrobią wszystko, byle tylko jeszcze trochę utrzymać się na powierzchni. Wiedzą, że zachowywali się podle. Wszystkich do siebie zrazili i nikt im teraz nie poda ręki. Swoje rządy oparli na rozdawnictwie, dezinformacji i kłamstwie. Nie mieli żadnych ideałów. Na zewnątrz: pląsy przed ołtarzem, wstawanie z kolan i gęby pełne frazesów, a w środku: po trupach do władzy, korupcja polityczna, zdrada i grabież państwowej kasy. Mieli obsesję władzy i za nic nie chcieli jej oddać. Po drodze zniszczyli państwo prawa, gospodarkę, armię, edukację i naukę, zniszczyli prawa kobiet, wywołali inflację i drożyznę, uderzyli w nasze strategiczne sojusze i bezpieczeństwo, poszli na wojnę z prawami kobiet i utuczyli przestępców w sutannach. Mścili się na środowisku naturalnym, wycinali lasy i puszcze, zatruwali powietrze i wodę. Walczyli z kulturą, nauką, ekologią, postępem, humanizmem i zdrowym rozsądkiem. Jeszcze jedna kadencja i zafundowaliby nam nową Berezę Kartuską, rządy biskupów i procesy czarownic. Teraz za to odpowiedzą. Jak sami zwykli mówić, im się to po prostu należy. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, pani poseł. Teraz oświadczenie wygłosi pan poseł Grzegorz Braun z Konfederacji. Bardzo proszę, panie pośle.",
                },
                {
                    "speaker": "Poseł Grzegorz Braun",
                    "content": "Szczęść Boże! Wysoka Pustoszejąca Izbo! My tu gadu-gadu, a tam na rubieżach, które niebezpiecznie zbliżyły się po ostatnich wiekach do stolicy Polski, na pograniczu, na Podkarpaciu, Lubelszczyźnie nasi rolnicy, przewoźnicy, transportowcy, kierowcy koczują w obronie swoich – uwaga, to powinno się bardzo podobać lewicy z lewej – miejsc pracy. A co powinno podobno podobać się lewicy z prawej? Oni koczują, protestują w obronie suwerenności Polski, bronią przed inwazją, agresją eurokołchozu. I to powinno się wam podobać, chociaż jedni i drudzy przyczyniliście się do tego, żeby Polskę na przestrzał otworzyć na już nie sugestie, tylko dyktat Brukseli. Otóż Bruksela podyktowała, że znosi się zezwolenia na pracę kierowców w trasach wykraczających poza ich państwa. Dogadano, dobito tego targu ponad naszymi głowami. Ale działo się to w czasie, kiedy Warszawa, rządzący, rząd Zjednoczonej łże-Prawicy deklarował się jako chętny, by pełnić rolę, cytuję klasyka: sług narodu ukraińskiego. Otóż słudzy narodu ukraińskiego z jednej strony, a eurofederaści z drugiej strony to właśnie sprawili, że tak jak rolnictwo już latem padało i dusiło się pod ciśnieniem, pod presją – to słynne techniczne zboże ukraińskie – tak też i dzisiaj ściśle analogicznie polscy transportowcy, przewoźnicy, przedsiębiorcy w tej branży padają i zbankrutują, szanowni państwo, bo jedno auto ciężkie do wożenia rozmaitych towarów bardzo nam przydatnych to jest poważna inwestycja, zwłaszcza dla tzw. misiów, małych i średnich przedsiębiorców, to były inwestycje ich życia. Otóż Rzeczpospolita Polska rozrywana była przez wojnę plemion Zjednoczonej łże-Prawicy i totalnej opozycji, z których jedni mniej, a drudzy bardziej chętnie dokonali hurtowej wyprzedaży naszej suwerenności na rzecz eurokołchozu. Polska przedsiębiorczość pada i my posłowie na Sejm Rzeczypospolitej Polskiej – nie tylko z tych okręgów, nie tylko z Podkarpacia, Lubelszczyzny, ale jak Polska długa i szeroka (Dzwonek) – jesteśmy winni przejawić solidarność z tymi, którzy, uwaga, dzisiaj walczą także o nas, bo dziś rolnicy, przewoźnicy, a jutro przyjdą po was, jutro nastąpi ciąg dalszy. Dlatego tam na pograniczu – bardzo dziękuję, panie marszałku, za tolerancję dla nieznacznego przekroczenia czasu mojego oświadczenia – tam na granicy rozstrzygają się większe sprawy. Mam nadzieję, że ta Wysoka Izba niezależnie od podziałów, które nią targają, opowie się za tym, żeby Polak u siebie, na swoim mógł sadzić, wozić niezagrożony nagłą zmianą reguł gry. Bo o te zmiany reguł gry tutaj idzie. Kierowcy, transportowcy, przewoźnicy ukraińscy, tak jak rolnicy czy magnaci produkcji rolno-spożywczej na Ukrainie, nie muszą spełniać tych rozmaitych, skądinąd absurdalnych norm eurokołchozowych, które narzucone zostały przez was, przez tę władzę polskiemu rolnikowi, polskiemu przewoźnikowi poselskie Otóż my nie jesteśmy entuzjastami norm eurokołchozowych – to chyba, panie marszałku, oczywiste – wręcz przeciwnie, radzi byśmy je zakwestionować i ten dyktat znieść, ale póki te reguły gry obowiązują, nie zgodzimy się na to, żeby nasi ludzie, nasi rodacy byli upośledzeni i żeby musieli spełniać bardziej wyśrubowane normy niż ci, którzy pod dowolnym pretekstem są wpuszczani na nasz rynek. Tak jak zaorane zostało już częściowo, w znacznej mierze rolnictwo, tak za chwilę doczeka się tego transport. Bądźmy solidarni z tymi, którzy dzisiaj protestują na granicy. Bardzo dziękuję, panie marszałku. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Głos zabierze pan poseł Tadeusz Tomaszewski z Lewicy.",
                },
                {
                    "speaker": "Poseł Tadeusz Tomaszewski",
                    "content": "Panie Marszałku! Wysoki Sejmie! Moje oświadczenie dotyczy sprawy bezpłatnego przekazania podnośnika hydraulicznego z Komendy Powiatowej Państwowej Straży Pożarnej w Turku do OSP Turek. Od dłuższego czasu media publiczne, władze samorządowe lokalne, ale także ochotnicze straże pożarne zbulwersowane są zamiarem komendanta powiatowego Państwowej Straży Pożarnej w Turku, który zasygnalizował możliwość przekazania podnośnika hydraulicznego do gminy wiejskiej. Ten podnośnik jest bardzo potrzebny na terenie miasta Turek, dlatego że występuje tam zabudowa wielopoziomowa, są takie instytucje publiczne jak szpital, Policja, urzędy, stąd ten podnośnik jest tam bardzo potrzebny. Zgodnie z ustawą o ochronie przeciwpożarowej przypominam komendantowi głównemu Państwowej Straży Pożarnej i komendantom wojewódzkim i powiatowym art. 31: sprzęt w dobrym stanie, ale zbędny w PSP przekazuje się do OSP po zasięgnięciu stosownej opinii oddziału wojewódzkiego Związku Ochotniczych Straży Pożarnych RP. Tę drogę należy wykorzystać. Chcę też przypomnieć, że na zakup tego podnośnika, o którym w tej chwili mówię, składały się również miasto Turek oraz przedsiębiorstwo gospodarki komunalnej i mieszkaniowej. Nieładnie więc, panowie komendanci, że nie macie pamięci historycznej mówiącej o tym, kto dokładał się do tego podnośnika, a w tej chwili chcecie go przekazać gdzie indziej. Mamy też niepokojące informacje, że z okazji Święta Niepodległości w Państwowej Straży Pożarnej działy się nadzwyczajne rzeczy, mianowicie nadzwyczajne awanse po roku, po 2 latach, nadzwyczajne premie, przenoszenie do wyższych grup, tak aby można było z chwilą przejścia na świadczenie emerytalne otrzymać wyższą emeryturę. To wszystko świadczy o tym, że również i tam – co mnie strasznie martwi – zajrzała polityka. Państwowa Straż Pożarna jako służba publiczna nie miała być tą służbą, która jest upolityczniona, i nie była. W tej chwili, za rządów PiS-u, stała się przystawką. Rozwożono samochodami służbowymi materiały wyborcze i używano tejże formacji do akcji wyborczej partii rządzącej. Apeluję do komendanta głównego Państwowej Straży Pożarnej, bo jest z Wielkopolski, aby zainteresował się sprawą z Turku i postępował zgodnie z prawem. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, panie pośle. Teraz oświadczenie wygłosi pan poseł Grzegorz Lorek z Klubu Parlamentarnego Prawo i Sprawiedliwość.",
                },
                {
                    "speaker": "Poseł Grzegorz Lorek",
                    "content": "Panie Marszałku! Panowie Posłowie! Panie, Panowie! Wysoka Izbo! W swoim pierwszym wystąpieniu chciałem podziękować mieszkańcom Piotrkowa Trybunalskiego, powiatu piotrkowskiego, powiatu bełchatowskiego, powiatu radomszczańskiego i powiatu tomaszowskiego za głosy na mnie oddane. Sprawy, które będą procedowane w Wysokiej Izbie X kadencji, szczególnie w zakresie rolnictwa i w zakresie węgla brunatnego, będą dla mnie bardzo ważne i bardzo istotnie będę o nie zabiegał. Szczególnie węgiel brunatny i koncern PGG w Bełchatowie dla Polski są bardzo ważne. To jest 25% wytwarzanego prądu. Nie da się z miesiąca na miesiąc – a niektóre siły polityczne chciałyby z dnia na dzień – doprowadzić do wyłączenia kopalni, elektrowni Bełchatów z systemu energetycznego naszego kraju. Szanowni Państwo! Będę walczył o to, żeby miejsca pracy i rozwój tego koncernu służyły naszej Polsce, żeby węgiel brunatny i energia stamtąd dalej wspierały, dopóki nie powstaną elektrownie atomowe w naszym kraju, naszą gospodarkę energetyczną. Rolnictwo jest bardzo ważną gałęzią gospodarki powiatu piotrkowskiego, szczególnie jeśli chodzi o trzodę chlewną. Trzeba zabiegać o to, żeby polskie mięso było na naszych stołach i żeby nasi rolnicy nie martwili się o przyszłość. Z tego miejsca deklaruję, że te 4 lata będę poświęcał naszej ojczyźnie i regionom piotrkowskiemu, bełchatowskiemu, radomszczańskiemu, tomaszowskiemu, żeby dalej się rozwijały, tak jak było to za rządów Prawa i Sprawiedliwości. Dziękuję poselskie",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję, panie pośle. Jako ostatnia oświadczenie wygłosi pani poseł Anna Wojciechowska z klubu Koalicji Obywatelskiej. Bardzo proszę.",
                },
                {
                    "speaker": "Poseł Anna Wojciechowska",
                    "content": "Panie Marszałku! Wysoka Izbo! Stoję tutaj przed państwem, przed swoimi mieszkańcami, przed swoimi wyborcami – okręg nr 35, województwo warmińsko-mazurskie, od Olsztyna przez całą część wschodnią do Podlasia. Chciałam państwu bardzo podziękować za oddane na mnie głosy. To było niesamowite wydarzenie w naszym regionie. Od bardzo długiego czasu pierwszy raz Koalicja Obywatelska, Platforma Obywatelska, ale również Trzecia Droga i Lewica osiągnęły tak wspaniałe wyniki. I to wszystko dzięki państwu, dzięki państwa uczestnictwu w wyborach. Bardzo państwu dziękuję. To jest dla nas bardzo ważne, że również państwo chcecie żyć w Polsce wolnej, sprawiedliwej, praworządnej, demokratycznej, spokojnej, przyjaznej. Zrobimy wszystko jako opozycja, a więc Koalicja Obywatelska, Trzecia Droga i Lewica, żeby to się stało. Na pewno dotrzymamy obietnic, które państwu złożyliśmy. Jak państwo widzicie, jesteśmy bardzo zdeterminowani. Najważniejszym przykładem, bardzo ważnym, jest to, że od jutra zaczynamy procedować nad projektem ustawy o finansowaniu in vitro. To znaczy, że zmiany już się zaczęły. Jeszcze raz państwu bardzo dziękuję i obiecuję, że przy tych wszystkich problemach naszego kraju, naszego państwa na pewno nie zapomnę o Warmii i Mazurach. Mamy olbrzymie wsparcie. Na pewno zrobimy wszystko, aby nasz region uczynić bardziej atrakcyjnym, aby był bardziej zaopiekowany, również jeśli chodzi o ochronę środowiska, ażeby nasz region był regionem konkurencyjnym dla wszystkich innych, pozostałych części Europy. Dziękuję państwu raz jeszcze i proszę o chwilę cierpliwości. Jesteśmy u państwa na służbie. Dziękuję. (Oklaski)",
                },
                {
                    "speaker": "Marszałek",
                    "content": "Dziękuję bardzo, pani poseł. Na tym zakończyliśmy oświadczenia poselskie. Zarządzam przerwę w posiedzeniu do dnia jutrzejszego, tj. 22 listopada br., do godz. 11.",
                },
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
        self.assertEqual(obj["speaker_senior"], None)
        self.assertEqual(obj["speaker"], None)
        self.assertEqual(obj["vicespeakers"], ["Piotr Zgorzelski", "Dorota Niedziela"])
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
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-28T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "12:05:00")
        self.assertEqual(obj["speaker_senior"], None)
        self.assertEqual(obj["speaker"], "Szymon Hołownia")
        self.assertEqual(
            obj["vicespeakers"],
            [
                "Włodzimierz Czarzasty",
                "Piotr Zgorzelski",
                "Monika Wielichowska",
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
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
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
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 16. porządku dziennego: Pierwsze czytanie przedstawionego przez Prezydium Sejmu projektu uchwały w sprawie powołania i wyboru składu osobowego Komisji Nadzwyczajnej do spraw zmian w kodyfikacjach",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 13. porządku dziennego: Pierwsze czytanie obywatelskiego projektu ustawy o zmianie ustawy o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
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
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-11-29T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "09:04:00")
        self.assertEqual(obj["speaker_senior"], None)
        self.assertEqual(obj["speaker"], "Szymon Hołownia")
        self.assertEqual(
            obj["vicespeakers"],
            [
                "Włodzimierz Czarzasty",
                "Dorota Niedziela",
                "Piotr Zgorzelski",
                "Monika Wielichowska",
                "Krzysztof Bosak",
            ],
        )
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Komunikaty",
                    "speakers": [
                        {"position": "Sekretarz Poseł", "name": "Małgorzata Gromadzka"}
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Włodzimierz Skalik"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 17. porządku dziennego: Sprawozdanie Komisji Gospodarki i Rozwoju o poselskim projekcie ustawy o zmianie ustawy o ograniczeniu handlu w niedziele i święta oraz niektóre inne dni",
                    "speakers": [
                        {
                            "position": "Poseł Sprawozdawca",
                            "name": "Adam Michał Gomoła",
                        },
                        {"position": "Poseł", "name": "Wojciech Michał Zubowski"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Adam Michał Gomoła"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 21. porządku dziennego: Pierwsze czytanie obywatelskiego projektu ustawy o zmianie ustawy o sposobie ustalania najniższego wynagrodzenia zasadniczego niektórych pracowników zatrudnionych w podmiotach leczniczych",
                    "speakers": [
                        {
                            "position": "Przedstawiciel Komitetu Inicjatywy Ustawodawczej",
                            "name": "Krystyna Ptok",
                        },
                        {"position": "Poseł", "name": "Katarzyna Sójka"},
                        {"position": "Poseł", "name": "Elżbieta Gelert"},
                        {"position": "Poseł", "name": "Ewa Szymanowska"},
                        {"position": "Poseł", "name": "Jarosław Rzepa"},
                        {"position": "Poseł", "name": "Joanna Wicha"},
                        {"position": "Poseł", "name": "Marcelina Zawisza"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Jarosław Sachajko"},
                        {"position": "Poseł", "name": "Czesław Hoc"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Wioleta Tomczak"},
                        {"position": "Poseł", "name": "Urszula Nowogórska"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Jarosław Sachajko"},
                        {"position": "Poseł", "name": "Józefa Szczurek-Żelazko"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Bożena Żelazowska"},
                        {"position": "Poseł", "name": "Daria Gosek-Popiołek"},
                        {"position": "Poseł", "name": "Ewa Leniart"},
                        {"position": "Poseł", "name": "Zofia Czernow"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Teresa Pamuła"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Tomasz Zimoch"},
                        {"position": "Poseł", "name": "Dorota Olko"},
                        {"position": "Poseł", "name": "Marcin Porzucek"},
                        {"position": "Poseł", "name": "Marek Rząsa"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Anna Ewa Cicholska"},
                        {"position": "Poseł", "name": "Marek Tomasz Hok"},
                        {"position": "Poseł", "name": "Alicja Chybicka"},
                        {"position": "Poseł", "name": "Ewa Kołodziej"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Katarzyna Anna Lubnauer"},
                        {"position": "Poseł", "name": "Małgorzata Niemczyk"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Henryka Krzywonos-Strycharska"},
                        {"position": "Poseł", "name": "Agnieszka Hanajczyk"},
                        {"position": "Poseł", "name": "Barbara Dolniak"},
                        {"position": "Poseł", "name": "Michał Krawczyk"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Mateusz Bochenek"},
                        {
                            "position": "Podsekretarz Stanu w Ministerstwie Zdrowia",
                            "name": "Piotr Bromber",
                        },
                        {
                            "position": "Zastępca Przedstawiciela Komitetu Inicjatywy Ustawodawczej",
                            "name": "Iwona Borchulska",
                        },
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 22. porządku dziennego: Sprawozdanie Komisji Zdrowia o obywatelskim projekcie ustawy o zmianie ustawy o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych",
                    "speakers": [],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Grzegorz Braun"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 22. porządku dziennego (cd.)",
                    "speakers": [
                        {
                            "position": "Poseł Sprawozdawca",
                            "name": "Bartosz Arłukowicz",
                        },
                        {"position": "Poseł", "name": "Józefa Szczurek-Żelazko"},
                        {"position": "Poseł", "name": "Piotr Uściński"},
                        {"position": "Poseł", "name": "Monika Wielichowska"},
                        {"position": "Poseł", "name": "Agnieszka Pomaska"},
                        {"position": "Poseł", "name": "Barbara Nowacka"},
                        {"position": "Poseł", "name": "Wioleta Tomczak"},
                        {"position": "Poseł", "name": "Agnieszka Maria Kłopotek"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Grzegorz Adam Płaczek"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Andrzej Gawron"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Sławomir Ćwik"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Anna Dąbrowska-Banaszek"},
                        {"position": "Poseł", "name": "Mateusz Bochenek"},
                        {"position": "Poseł", "name": "Marcelina Zawisza"},
                        {"position": "Poseł", "name": "Roman Fritz"},
                        {"position": "Poseł", "name": "Władysław Kurowski"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Kamil Wnuk"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Piotr Paweł Strach"},
                        {"position": "Poseł", "name": "Paweł Szrot"},
                        {"position": "Poseł", "name": "Alicja Chybicka"},
                        {"position": "Poseł", "name": "Barbara Bartuś"},
                        {"position": "Poseł", "name": "Marcin Józefaciuk"},
                        {"position": "Poseł", "name": "Ewa Kołodziej"},
                        {"position": "Poseł", "name": "Krzysztof Ciecióra"},
                        {"position": "Poseł", "name": "Krzysztof Truskolaski"},
                        {"position": "Poseł", "name": "Piotr Kaleta"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Marta Golbik"},
                        {"position": "Poseł", "name": "Kinga Gajewska"},
                        {"position": "Poseł", "name": "Małgorzata Niemczyk"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Monika Rosa"},
                        {"position": "Poseł", "name": "Iwona Małgorzata Krawczyk"},
                        {"position": "Poseł", "name": "Sylwia Bielawska"},
                        {"position": "Poseł", "name": "Anna Wojciechowska"},
                        {"position": "Poseł", "name": "Aleksandra Gajewska"},
                        {"position": "Poseł", "name": "Katarzyna Osos"},
                        {"position": "Poseł", "name": "Joanna Frydrych"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Patryk Gabriel"},
                        {"position": "Poseł", "name": "Patryk Jaskulski"},
                        {"position": "Poseł", "name": "Iwona Maria Kozłowska"},
                        {"position": "Poseł", "name": "Lucjan Marek Pietrzczyk"},
                        {"position": "Poseł", "name": "Franciszek Sterczewski"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Krzysztof Brejza"},
                        {"position": "Poseł", "name": "Michał Krawczyk"},
                        {"position": "Poseł", "name": "Jacek Niedźwiedzki"},
                        {"position": "Poseł", "name": "Jacek Karnowski"},
                        {"position": "Poseł", "name": "Paweł Bliźniuk"},
                        {"position": "Poseł", "name": "Jolanta Niezgodzka"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {
                            "position": "Poseł",
                            "name": "Magdalena Małgorzata Kołodziejczak",
                        },
                        {"position": "Poseł", "name": "Piotr Borys"},
                        {"position": "Poseł", "name": "Łukasz Ściebiorowski"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Elżbieta Anna Polak"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {
                            "position": "Zastępca Przedstawiciela Komitetu Inicjatywy Ustawodawczej",
                            "name": "Małgorzata Rozenek-Majdan",
                        },
                        {
                            "position": "Przedstawiciel Komitetu Inicjatywy Ustawodawczej",
                            "name": "Agnieszka Pomaska",
                        },
                        {"position": "Poseł", "name": "Jacek Karnowski"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 23. porządku dziennego: Informacja Prezesa Rady Ministrów w sprawie protestów polskich transportowców i rolników na granicy polsko-ukraińskiej",
                    "speakers": [
                        {
                            "position": "Minister Rolnictwa i Rozwoju Wsi",
                            "name": "Anna Gembicka",
                        },
                        {
                            "position": "Minister Infrastruktury",
                            "name": "Alvin Gajadhur",
                        },
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Piotr Król"},
                        {"position": "Poseł", "name": "Paweł Kowal"},
                        {"position": "Poseł", "name": "Michał Kołodziejczak"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Dariusz Klimczak"},
                        {"position": "Poseł", "name": "Stefan Krajewski"},
                        {"position": "Poseł", "name": "Andrzej Adamczyk"},
                        {"position": "Poseł", "name": "Jacek Czerniak"},
                        {"position": "Poseł", "name": "Andrzej Tomasz Zapałowski"},
                        {"position": "Poseł", "name": "Witold Tumanowicz"},
                        {"position": "Poseł", "name": "Jarosław Sachajko"},
                        {"position": "Poseł", "name": "Stefan Krajewski"},
                        {"position": "Poseł", "name": "Zbigniew Krzysztof Kuźmiuk"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Andrzej Grzyb"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Jarosław Sachajko"},
                        {"position": "Poseł", "name": "Kazimierz Gwiazdowski"},
                        {"position": "Poseł", "name": "Stefan Krajewski"},
                        {"position": "Poseł", "name": "Artur Jarosław Łącki"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Wiesław Różyński"},
                        {"position": "Poseł", "name": "Paulina Matysiak"},
                        {"position": "Poseł", "name": "Krzysztof Ciecióra"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Ewa Schädler"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Jacek Czerniak"},
                        {"position": "Poseł", "name": "Dorota Marek"},
                        {"position": "Poseł", "name": "Barbara Oliwiecka"},
                        {"position": "Poseł", "name": "Henryk Kiepura"},
                        {"position": "Poseł", "name": "Krzysztof Truskolaski"},
                        {"position": "Poseł", "name": "Sławomir Ćwik"},
                        {"position": "Poseł", "name": "Mirosław Maliszewski"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Adam Dziedzic"},
                        {"position": "Poseł", "name": "Agnieszka Maria Kłopotek"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Alicja Chybicka"},
                        {"position": "Poseł", "name": "Marek Rząsa"},
                        {"position": "Poseł", "name": "Kazimierz Plocke"},
                        {"position": "Poseł", "name": "Joanna Frydrych"},
                        {"position": "Poseł", "name": "Piotr Głowski"},
                        {"position": "Poseł", "name": "Marek Sowa"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Krystyna Sibińska"},
                        {"position": "Poseł", "name": "Zofia Czernow"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Krzysztof Grabczuk"},
                        {"position": "Poseł", "name": "Marta Wcisło"},
                        {"position": "Poseł", "name": "Piotr Borys"},
                        {"position": "Poseł", "name": "Tomasz Piotr Nowak"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Danuta Jazłowiecka"},
                        {"position": "Poseł", "name": "Michał Kołodziejczak"},
                        {"position": "Poseł", "name": "Piotr Kandyba"},
                        {"position": "Poseł", "name": "Sebastian Kaleta"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {
                            "position": "Minister Rolnictwa i Rozwoju Wsi",
                            "name": "Anna Gembicka",
                        },
                        {
                            "position": "Minister Infrastruktury",
                            "name": "Alvin Gajadhur",
                        },
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Infrastruktury",
                            "name": "Rafał Weber",
                        },
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Spraw Zagranicznych",
                            "name": "Paweł Jabłoński",
                        },
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Jacek Ozdoba"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 22. porządku dziennego: Sprawozdanie Komisji Zdrowia o obywatelskim projekcie ustawy o zmianie ustawy o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych (cd.)",
                    "speakers": [
                        {"position": "Poseł Sprawozdawca", "name": "Bartosz Arłukowicz"}
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 23. porządku dziennego: Informacja Prezesa Rady Ministrów w sprawie protestów polskich transportowców i rolników na granicy polsko-ukraińskiej (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 24. porządku dziennego: Odwołanie członków Państwowej Komisji do spraw badania wpływów rosyjskich na bezpieczeństwo wewnętrzne Rzeczypospolitej Polskiej w latach 2007–2022",
                    "speakers": [
                        {"position": "Poseł", "name": "Borys Budka"},
                        {
                            "position": "Prezes Rady Ministrów",
                            "name": "Mateusz Morawiecki",
                        },
                        {
                            "position": "Minister Obrony Narodowej",
                            "name": "Mariusz Błaszczak",
                        },
                        {"position": "Poseł", "name": "Borys Budka"},
                        {"position": "Poseł", "name": "Piotr Kaleta"},
                        {"position": "Poseł", "name": "Tomasz Szymański"},
                        {"position": "Poseł", "name": "Paweł Zalewski"},
                        {"position": "Poseł", "name": "Krzysztof Paszyk"},
                        {"position": "Poseł", "name": "Wiesław Szczepański"},
                        {"position": "Poseł", "name": "Przemysław Wipler"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Paweł Kukiz"},
                        {
                            "position": "Minister Spraw Wewnętrznych i Administracji",
                            "name": "Paweł Szefernaker",
                        },
                        {
                            "position": "Minister – Członek Rady Ministrów",
                            "name": "Jacek Ozdoba",
                        },
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 26. porządku dziennego: Wybór uzupełniający do składu osobowego Komisji do Spraw Unii Europejskiej",
                    "speakers": [
                        {"position": "Poseł", "name": "Marek Suski"},
                        {"position": "Poseł", "name": "Sławomir Nitras"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 25. porządku dziennego: Zmiany w składach osobowych komisji sejmowych",
                    "speakers": [],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Zbigniew Konwiński"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 25. porządku dziennego (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Oświadczenia",
                    "speakers": [
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Szymon Giżyński"},
                        {"position": "Poseł", "name": "Anna Dąbrowska-Banaszek"},
                        {"position": "Poseł", "name": "Anna Wojciechowska"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Adrian Witczak"},
                        {"position": "Poseł", "name": "Zofia Czernow"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Władysław Dajczak"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Waldemar Andzel"},
                        {"position": "Poseł", "name": "Marcin Józefaciuk"},
                        {"position": "Poseł", "name": "Kamil Wnuk"},
                        {"position": "Poseł", "name": "Filip Kaczyński"},
                        {"position": "Poseł", "name": "Łukasz Ściebiorowski"},
                        {"position": "Poseł", "name": "Katarzyna Maria Piekarska"},
                        {"position": "Poseł", "name": "Łukasz Osmalak"},
                        {"position": "Poseł", "name": "Paweł Szrot"},
                        {"position": "Poseł", "name": "Tadeusz Samborski"},
                        {"position": "Poseł", "name": "Włodzimierz Skalik"},
                    ],
                },
                {"type": "BREAK"},
                {
                    "type": "HEADER",
                    "name": "Załącznik – Teksty wystąpień niewygłoszonych",
                    "speakers": [{"position": "Poseł", "name": "Grzegorz Lorek"}],
                },
            ],
        )

    def test_01_g(self):
        file_path = os.path.join("files", "01_g_ksiazka.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-12-06T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "09:03:00")
        self.assertEqual(obj["speaker_senior"], None)
        self.assertEqual(obj["speaker"], "Szymon Hołownia")
        self.assertEqual(
            obj["vicespeakers"],
            [
                "Piotr Zgorzelski",
                "Krzysztof Bosak",
                "Dorota Niedziela",
                "Włodzimierz Czarzasty",
            ],
        )
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Komunikaty",
                    "speakers": [
                        {"position": "Sekretarz Poseł", "name": "Jolanta Niezgodzka"}
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Ryszard Wilk"},
                        {"position": "Poseł", "name": "Zbigniew Krzysztof Kuźmiuk"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Jarosław Sachajko"},
                        {
                            "position": "Minister Rolnictwa i Rozwoju Wsi",
                            "name": "Anna Gembicka",
                        },
                        {"position": "Poseł", "name": "Stefan Krajewski"},
                        {
                            "position": "Minister Rolnictwa i Rozwoju Wsi",
                            "name": "Anna Gembicka",
                        },
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 27. porządku dziennego: Ślubowanie członka Państwowej Komisji do spraw przeciwdziałania wykorzystaniu seksualnemu małoletnich poniżej lat 15",
                    "speakers": [
                        {
                            "position": "Członek Państwowej Komisji do spraw Przeciwdziałania Wykorzystaniu Seksualnemu Małoletnich Poniżej Lat 15",
                            "name": "Karolina Maria Bućko",
                        }
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 28. porządku dziennego: Pierwsze czytanie rządowego projektu ustawy o zmianie ustaw w celu wsparcia odbiorców energii elektrycznej, paliw gazowych i ciepła oraz niektórych innych ustaw",
                    "speakers": [],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 29. porządku dziennego: Pierwsze czytanie poselskiego projektu ustawy o zmianie ustaw w celu wsparcia odbiorców energii elektrycznej, paliw gazowych i ciepła oraz niektórych innych ustaw",
                    "speakers": [
                        {
                            "position": "Minister Klimatu i Środowiska",
                            "name": "Anna Łukaszewska-Trzeciakowska",
                        },
                        {"position": "Poseł", "name": "Krzysztof Gadowski"},
                        {"position": "Poseł", "name": "Waldemar Buda"},
                        {"position": "Poseł", "name": "Janusz Kowalski"},
                        {"position": "Poseł", "name": "Tomasz Piotr Nowak"},
                        {"position": "Poseł", "name": "Krzysztof Gadowski"},
                        {"position": "Poseł", "name": "Ireneusz Zyska"},
                        {"position": "Poseł", "name": "Paulina Hennig-Kloska"},
                        {"position": "Poseł", "name": "Andrzej Grzyb"},
                        {"position": "Poseł", "name": "Dariusz Wieczorek"},
                        {"position": "Poseł", "name": "Krzysztof Mulawa"},
                        {"position": "Poseł", "name": "Zbigniew Krzysztof Kuźmiuk"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Ireneusz Raś"},
                        {"position": "Poseł", "name": "Roman Fritz"},
                        {"position": "Poseł", "name": "Andrzej Gawron"},
                        {"position": "Poseł", "name": "Aleksander Miszalski"},
                        {"position": "Poseł", "name": "Ewa Szymanowska"},
                        {"position": "Poseł", "name": "Jacek Tomczak"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Mariusz Krystian"},
                        {"position": "Poseł", "name": "Ewa Kołodziej"},
                        {"position": "Poseł", "name": "Sławomir Ćwik"},
                        {"position": "Poseł", "name": "Zbigniew Sosnowski"},
                        {"position": "Poseł", "name": "Paweł Rychlik"},
                        {"position": "Poseł", "name": "Karolina Pawliczak"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Andrzej Grzyb"},
                        {"position": "Poseł", "name": "Paweł Hreniak"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Sebastian Kaleta"},
                        {"position": "Poseł", "name": "Małgorzata Gromadzka"},
                        {"position": "Poseł", "name": "Żaneta Cwalina-Śliwowska"},
                        {"position": "Poseł", "name": "Zbigniew Dolata"},
                        {"position": "Poseł", "name": "Iwona Karolewska"},
                        {"position": "Poseł", "name": "Izabela Bodnar"},
                        {"position": "Poseł", "name": "Piotr Müller"},
                        {"position": "Poseł", "name": "Agnieszka Pomaska"},
                        {"position": "Poseł", "name": "Ewa Schädler"},
                        {"position": "Poseł", "name": "Małgorzata Golińska"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Cezary Tomczyk"},
                        {"position": "Poseł", "name": "Piotr Paweł Strach"},
                        {"position": "Poseł", "name": "Robert Gontarz"},
                        {"position": "Poseł", "name": "Michał Kołodziejczak"},
                        {"position": "Poseł", "name": "Rafał Komarewicz"},
                        {"position": "Poseł", "name": "Marcin Porzucek"},
                        {"position": "Poseł", "name": "Jagna Marczułajtis-Walczak"},
                        {"position": "Poseł", "name": "Wioleta Tomczak"},
                        {"position": "Poseł", "name": "Jan Warzecha"},
                        {"position": "Poseł", "name": "Urszula Sara Zielińska"},
                        {"position": "Poseł", "name": "Ireneusz Zyska"},
                        {"position": "Poseł", "name": "Tomasz Piotr Nowak"},
                        {"position": "Poseł", "name": "Radosław Fogiel"},
                        {"position": "Poseł", "name": "Krzysztof Gadowski"},
                        {"position": "Poseł", "name": "Joanna Borowiak"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Paweł Szrot"},
                        {"position": "Poseł", "name": "Artur Jarosław Łącki"},
                        {"position": "Poseł", "name": "Jacek Ozdoba"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Małgorzata Golińska"},
                        {"position": "Poseł", "name": "Lucjan Marek Pietrzczyk"},
                        {"position": "Poseł", "name": "Barbara Bartuś"},
                        {"position": "Poseł", "name": "Henryk Szopiński"},
                        {"position": "Poseł", "name": "Mateusz Bochenek"},
                        {"position": "Poseł", "name": "Piotr Głowski"},
                        {"position": "Poseł", "name": "Marcin Gwóźdź"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Anna Kwiecień"},
                        {"position": "Poseł", "name": "Mirosława Nykiel"},
                        {"position": "Poseł", "name": "Józefa Szczurek-Żelazko"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Paweł Sałek"},
                        {"position": "Poseł", "name": "Patryk Jaskulski"},
                        {"position": "Poseł", "name": "Marek Sowa"},
                        {"position": "Poseł", "name": "Stanisław Lamczyk"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Adrian Witczak"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Marek Suski"},
                        {"position": "Poseł", "name": "Ireneusz Zyska"},
                        {
                            "position": "Minister Klimatu i Środowiska",
                            "name": "Anna Łukaszewska-Trzeciakowska",
                        },
                        {"position": "Poseł", "name": "Krzysztof Gadowski"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Jacek Ozdoba"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 28. porządku dziennego: Pierwsze czytanie rządowego projektu ustawy o zmianie ustaw w celu wsparcia odbiorców energii elektrycznej, paliw gazowych i ciepła oraz niektórych innych ustaw (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 29. porządku dziennego: Pierwsze czytanie poselskiego projektu ustawy o zmianie ustaw w celu wsparcia odbiorców energii elektrycznej, paliw gazowych i ciepła oraz niektórych innych ustaw (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 31. porządku dziennego: Pierwsze czytanie przedstawionego przez Prezydium Sejmu projektu uchwały w sprawie zmiany Regulaminu Sejmu Rzeczypospolitej Polskiej",
                    "speakers": [
                        {"position": "Poseł", "name": "Monika Wielichowska"},
                        {"position": "Poseł", "name": "Kazimierz Smoliński"},
                        {"position": "Poseł", "name": "Jarosław Urbaniak"},
                        {"position": "Poseł", "name": "Łukasz Osmalak"},
                        {"position": "Poseł", "name": "Michał Pyrzyk"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Michał Wawer"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Kazimierz Smoliński"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Andrzej Gawron"},
                        {"position": "Poseł", "name": "Marcin Porzucek"},
                        {"position": "Poseł", "name": "Barbara Bartuś"},
                        {"position": "Poseł", "name": "Sylwester Tułajew"},
                        {"position": "Poseł", "name": "Jarosław Urbaniak"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Marek Jakubiak"},
                        {"position": "Poseł", "name": "Monika Wielichowska"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 31. porządku dziennego (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [
                        {"position": "Marszałek", "name": "Szymon Hołownia"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Kazimierz Smoliński"},
                        {"position": "Poseł", "name": "Bogdan Andrzej Zdrojewski"},
                        {"position": "Poseł", "name": "Łukasz Osmalak"},
                        {"position": "Poseł", "name": "Michał Pyrzyk"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Michał Wawer"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Marek Jakubiak"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Oświadczenia",
                    "speakers": [
                        {"position": "Poseł", "name": "Anna Dąbrowska-Banaszek"},
                        {"position": "Poseł", "name": "Łukasz Kmita"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Patryk Gabriel"},
                        {"position": "Poseł", "name": "Aleksander Mikołaj Mrówczyński"},
                        {
                            "position": "Poseł",
                            "name": "Magdalena Małgorzata Kołodziejczak",
                        },
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Bartosz Zawieja"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Grzegorz Adam Płaczek"},
                        {"position": "Poseł", "name": "Waldemar Andzel"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Szymon Giżyński"},
                        {"position": "Poseł", "name": "Paweł Bliźniuk"},
                        {"position": "Poseł", "name": "Barbara Bartuś"},
                        {"position": "Poseł", "name": "Henryk Szopiński"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Norbert Jakub Kaczmarczyk"},
                        {"position": "Poseł", "name": "Ewa Leniart"},
                        {"position": "Poseł", "name": "Piotr Uruski"},
                        {"position": "Poseł", "name": "Dariusz Matecki"},
                        {"position": "Poseł", "name": "Wioleta Tomczak"},
                        {"position": "Poseł", "name": "Michał Kołodziejczak"},
                        {"position": "Poseł", "name": "Anna Kwiecień"},
                    ],
                },
                {"type": "BREAK"},
                {
                    "type": "HEADER",
                    "name": "Załącznik – Teksty wystąpień niewygłoszonych",
                    "speakers": [{"position": "Poseł", "name": "Grzegorz Lorek"}],
                },
            ],
        )

    def test_01_h(self):
        file_path = os.path.join("files", "01_h_ksiazka.pdf")
        obj = report_to_obj(file_path)
        # print(obj2pretty_json(obj))

        self.assertEqual(obj["term"], "X")
        self.assertEqual(obj["sitting_number"], "1")
        self.assertEqual(obj["session_date"].isoformat(), "2023-12-07T00:00:00")
        self.assertEqual(obj["session_start"].isoformat(), "09:07:00")
        self.assertEqual(obj["speaker_senior"], None)
        self.assertEqual(obj["speaker"], "Szymon Hołownia")
        self.assertEqual(
            obj["vicespeakers"],
            ["Dorota Niedziela", "Monika Wielichowska", "Piotr Zgorzelski"],
        )
        self.assertEqual(
            obj["table_of_contents"],
            [
                {"type": "RESUME POSIEDZENIE"},
                {
                    "type": "HEADER",
                    "name": "Komunikaty",
                    "speakers": [
                        {"position": "Sekretarz Poseł", "name": "Rafał Siemaszko"}
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Marek Suski"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 32. porządku dziennego: Sprawozdanie Komisji Ustawodawczej o poselskim projekcie uchwały w sprawie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego",
                    "speakers": [
                        {"position": "Poseł Sprawozdawca", "name": "Krzysztof Brejza"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Cezary Tomczyk"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Jarosław Rzepa"},
                        {"position": "Poseł", "name": "Joanna Scheuring-Wielgus"},
                        {"position": "Poseł", "name": "Witold Tumanowicz"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Magdalena Sroka"},
                        {"position": "Poseł", "name": "Jacek Czerniak"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Anna Ewa Cicholska"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Elżbieta Jolanta Burkiewicz"},
                        {"position": "Poseł", "name": "Adam Dziedzic"},
                        {"position": "Poseł", "name": "Wanda Nowicka"},
                        {"position": "Poseł", "name": "Marcin Porzucek"},
                        {"position": "Poseł", "name": "Andrzej Szewiński"},
                        {"position": "Poseł", "name": "Ewa Schädler"},
                        {"position": "Poseł", "name": "Robert Gontarz"},
                        {"position": "Poseł", "name": "Marek Krząkała"},
                        {"position": "Poseł", "name": "Piotr Kaleta"},
                        {"position": "Poseł", "name": "Witold Zembaczyński"},
                        {"position": "Poseł", "name": "Sławomir Ćwik"},
                        {"position": "Poseł", "name": "Katarzyna Sójka"},
                        {"position": "Poseł", "name": "Dariusz Joński"},
                        {"position": "Poseł", "name": "Michał Gramatyka"},
                        {"position": "Poseł", "name": "Dariusz Stefaniuk"},
                        {"position": "Poseł", "name": "Sylwia Bielawska"},
                        {"position": "Poseł", "name": "Marcin Skonieczka"},
                        {"position": "Poseł", "name": "Maria Kurowska"},
                        {"position": "Poseł", "name": "Iwona Hartwich"},
                        {"position": "Poseł", "name": "Adam Luboński"},
                        {"position": "Poseł", "name": "Agnieszka Hanajczyk"},
                        {"position": "Poseł", "name": "Małgorzata Niemczyk"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Marcin Józefaciuk"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Krzysztof Grabczuk"},
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Komunikaty",
                    "speakers": [
                        {"position": "Sekretarz Poseł", "name": "Rafał Siemaszko"}
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Sebastian Kaleta"}],
                },
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Punkt 32. porządku dziennego (cd.)",
                    "speakers": [
                        {"position": "Poseł", "name": "Katarzyna Osos"},
                        {"position": "Poseł", "name": "Krzysztof Truskolaski"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Jagna Marczułajtis-Walczak"},
                        {"position": "Poseł", "name": "Adrian Witczak"},
                        {"position": "Poseł", "name": "Jacek Karnowski"},
                        {"position": "Poseł", "name": "Michał Krawczyk"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Sławomir Nitras"},
                        {"position": "Poseł", "name": "Barbara Nowacka"},
                        {"position": "Poseł", "name": "Monika Rosa"},
                        {"position": "Poseł", "name": "Alicja Chybicka"},
                        {"position": "Poseł", "name": "Katarzyna Anna Lubnauer"},
                        {"position": "Poseł", "name": "Elżbieta Anna Polak"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Łukasz Ściebiorowski"},
                        {"position": "Poseł", "name": "Mateusz Bochenek"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Katarzyna Maria Piekarska"},
                        {"position": "Poseł", "name": "Marcin Bosacki"},
                        {"position": "Poseł", "name": "Ewa Szymanowska"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Mariusz Witczak"},
                        {"position": "Poseł", "name": "Marcin Kulasek"},
                        {"position": "Poseł", "name": "Barbara Dolniak"},
                        {"position": "Poseł", "name": "Krystian Łuczak"},
                        {"position": "Poseł", "name": "Paweł Suski"},
                        {"position": "Poseł", "name": "Patryk Jaskulski"},
                        {"position": "Poseł", "name": "Marta Golbik"},
                        {"position": "Poseł", "name": "Michał Kołodziejczak"},
                        {"position": "Poseł", "name": "Kinga Gajewska"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Cezary Tomczyk"},
                        {"position": "Poseł", "name": "Sławomir Nitras"},
                        {"position": "Poseł", "name": "Krzysztof Brejza"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 33. porządku dziennego: Sprawozdanie Komisji do Spraw Energii, Klimatu i Aktywów Państwowych oraz Komisji Finansów Publicznych o poselskim projekcie ustawy o zmianie ustaw w celu wsparcia odbiorców energii elektrycznej, paliw gazowych i ciepła oraz niektórych innych ustaw",
                    "speakers": [
                        {"position": "Poseł Sprawozdawca", "name": "Marek Sowa"},
                        {"position": "Poseł", "name": "Waldemar Buda"},
                        {"position": "Poseł", "name": "Krzysztof Gadowski"},
                        {"position": "Poseł", "name": "Tomasz Piotr Nowak"},
                        {"position": "Poseł", "name": "Waldemar Buda"},
                        {"position": "Poseł", "name": "Andrzej Grzyb"},
                        {"position": "Poseł", "name": "Dariusz Wieczorek"},
                        {"position": "Poseł", "name": "Rafał Komarewicz"},
                        {"position": "Poseł", "name": "Grzegorz Adam Płaczek"},
                        {"position": "Poseł", "name": "Mirosław Suchoń"},
                        {"position": "Poseł", "name": "Zbigniew Krzysztof Kuźmiuk"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Ireneusz Zyska"},
                        {"position": "Poseł", "name": "Michał Szczerba"},
                        {"position": "Poseł", "name": "Barbara Oliwiecka"},
                        {"position": "Poseł", "name": "Maciej Konieczny"},
                        {"position": "Poseł", "name": "Wiesław Krajewski"},
                        {"position": "Poseł", "name": "Małgorzata Pępek"},
                        {"position": "Poseł", "name": "Adam Michał Gomoła"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Paweł Szrot"},
                        {"position": "Poseł", "name": "Ewa Kołodziej"},
                        {"position": "Poseł", "name": "Maria Koc"},
                        {"position": "Poseł", "name": "Krystyna Skowrońska"},
                        {"position": "Poseł", "name": "Małgorzata Golińska"},
                        {"position": "Poseł", "name": "Krzysztof Grabczuk"},
                        {"position": "Poseł", "name": "Anna Wojciechowska"},
                        {"position": "Poseł", "name": "Grzegorz Rusiecki"},
                        {"position": "Poseł", "name": "Mateusz Bochenek"},
                        {"position": "Poseł", "name": "Tomasz Piotr Nowak"},
                        {"position": "Poseł", "name": "Krzysztof Gadowski"},
                        {"position": "Poseł", "name": "Katarzyna Kierzek-Koperska"},
                        {"position": "Poseł", "name": "Michał Kołodziejczak"},
                        {"position": "Poseł", "name": "Elżbieta Anna Polak"},
                        {"position": "Poseł", "name": "Zofia Czernow"},
                        {"position": "Poseł", "name": "Jakub Rutnicki"},
                        {"position": "Poseł", "name": "Stanisław Lamczyk"},
                        {"position": "Poseł", "name": "Konrad Frysztak"},
                        {"position": "Poseł", "name": "Marcin Porzucek"},
                        {"position": "Poseł", "name": "Iwona Małgorzata Krawczyk"},
                        {"position": "Poseł", "name": "Sławomir Ćwik"},
                        {"position": "Poseł", "name": "Marcin Kulasek"},
                        {"position": "Poseł", "name": "Rafał Kasprzyk"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Marek Jakubiak"},
                        {"position": "Poseł", "name": "Stanisław Gorczyca"},
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Klimatu i Środowiska",
                            "name": "Ireneusz Zyska",
                        },
                        {"position": "Poseł", "name": "Krzysztof Gadowski"},
                        {"position": "Poseł", "name": "Michał Kołodziejczak"},
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Klimatu i Środowiska",
                            "name": "Ireneusz Zyska",
                        },
                    ],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Zmiana porządku dziennego",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Witold Tumanowicz"},
                        {"position": "Poseł", "name": "Sebastian Kaleta"},
                        {"position": "Poseł", "name": "Marcin Horała"},
                        {"position": "Poseł", "name": "Krzysztof Mulawa"},
                        {
                            "position": "Prezes Rady Ministrów",
                            "name": "Mateusz Morawiecki",
                        },
                        {"position": "Poseł", "name": "Borys Budka"},
                        {"position": "Poseł", "name": "Łukasz Schreiber"},
                        {"position": "Poseł", "name": "Paulina Hennig-Kloska"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 33. porządku dziennego: Sprawozdanie Komisji do Spraw Energii, Klimatu i Aktywów Państwowych oraz Komisji Finansów Publicznych o poselskim projekcie ustawy o zmianie ustaw w celu wsparcia odbiorców energii elektrycznej, paliw gazowych i ciepła oraz niektórych innych ustaw (cd.)",
                    "speakers": [
                        {"position": "Poseł", "name": "Waldemar Buda"},
                        {"position": "Poseł", "name": "Tomasz Piotr Nowak"},
                        {"position": "Poseł", "name": "Andrzej Grzyb"},
                        {"position": "Poseł", "name": "Grzegorz Adam Płaczek"},
                        {
                            "position": "Sekretarz Stanu w Ministerstwie Klimatu i Środowiska",
                            "name": "Ireneusz Zyska",
                        },
                        {"position": "Poseł", "name": "Marek Sowa"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [{"position": "Poseł", "name": "Mariusz Gosek"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 31. porządku dziennego: Pierwsze czytanie przedstawionego przez Prezydium Sejmu projektu uchwały w sprawie zmiany Regulaminu Sejmu Rzeczypospolitej Polskiej (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 32. porządku dziennego: Sprawozdanie Komisji Ustawodawczej o poselskim projekcie uchwały w spra- wie powołania Komisji Śledczej do zbadania legalności, prawidłowości oraz celowości działań podjętych w celu przygotowania i przeprowadzenia wyborów Prezydenta Rzeczypospolitej Polskiej w 2020 roku w formie głosowania korespondencyjnego (cd.)",
                    "speakers": [],
                },
                {
                    "type": "HEADER",
                    "name": "Sprawy formalne",
                    "speakers": [
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                        {"position": "Poseł", "name": "Cezary Tomczyk"},
                        {"position": "Poseł", "name": "Przemysław Czarnek"},
                    ],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 32. porządku dziennego (cd.)",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 34. porządku dziennego: Wybór Przewodniczącego Państwowej Komisji do spraw przeciwdziałania wykorzystaniu seksualnemu małoletnich poniżej lat 15",
                    "speakers": [
                        {"position": "Poseł", "name": "Włodzimierz Czarzasty"},
                        {"position": "Poseł", "name": "Monika Rosa"},
                        {"position": "Poseł", "name": "Joanna Scheuring-Wielgus"},
                        {"position": "Poseł", "name": "Michał Wójcik"},
                        {"position": "Poseł", "name": "Joanna Scheuring-Wielgus"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                    ],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 39. porządku dziennego: Wybór uzupełniający do składu osobowego Komisji do Spraw Unii Europejskiej",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {
                    "type": "HEADER",
                    "name": "Punkt 35. porządku dziennego: Zmiany w składach osobowych komisji sejmowych",
                    "speakers": [],
                },
                {
                    "type": "VOTING",
                    "speakers": [{"position": "Marszałek", "name": "Szymon Hołownia"}],
                },
                {"type": "BREAK"},
                {"type": "RESUME OBRADY"},
                {
                    "type": "HEADER",
                    "name": "Oświadczenia",
                    "speakers": [
                        {"position": "Poseł", "name": "Anna Dąbrowska-Banaszek"},
                        {"position": "Poseł", "name": "Anna Kwiecień"},
                        {"position": "Poseł", "name": "Łukasz Kmita"},
                        {"position": "Poseł", "name": "Jarosław Wałęsa"},
                        {"position": "Poseł", "name": "Aleksander Mikołaj Mrówczyński"},
                        {"position": "Poseł", "name": "Waldemar Andzel"},
                        {"position": "Poseł", "name": "Klaudia Jachira"},
                        {"position": "Poseł", "name": "Szymon Giżyński"},
                        {"position": "Poseł", "name": "Marcin Józefaciuk"},
                        {"position": "Poseł", "name": "Fryderyk Sylwester Kapinos"},
                        {"position": "Poseł", "name": "Bartosz Romowicz"},
                        {"position": "Poseł", "name": "Mariusz Krystian"},
                        {"position": "Poseł", "name": "Zbigniew Bogucki"},
                        {"position": "Poseł", "name": "Andrzej Tomasz Zapałowski"},
                        {"position": "Poseł", "name": "Norbert Jakub Kaczmarczyk"},
                        {"position": "Poseł", "name": "Tadeusz Tomaszewski"},
                        {"position": "Poseł", "name": "Ewa Leniart"},
                        {"position": "Poseł", "name": "Sylwia Bielawska"},
                        {"position": "Poseł", "name": "Krzysztof Mulawa"},
                        {"position": "Poseł", "name": "Dariusz Matecki"},
                        {"position": "Poseł", "name": "Grzegorz Braun"},
                        {"position": "Poseł", "name": "Henryk Szopiński"},
                        {"position": "Poseł", "name": "Elżbieta Jolanta Burkiewicz"},
                        {"position": "Poseł", "name": "Włodzimierz Skalik"},
                        {"position": "Poseł", "name": "Przemysław Witek"},
                    ],
                },
                {"type": "BREAK"},
                {
                    "type": "HEADER",
                    "name": "Załącznik – Teksty wystąpień niewygłoszonych",
                    "speakers": [{"position": "Poseł", "name": "Grzegorz Lorek"}],
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
