from tests.BaseRunner import BaseRunner


class TestIMC(BaseRunner):

    def setUp(self):
        self.expected_venue = "IMC"

        self.correct_strings = {
            r"IMC",  # used by DBLP
            r"Internet Measurement Workshop",  # used by DBLP
            r"Internet Measurement Conference",  # used by DBLP
            r"Proceedings of the 1st {ACM} {SIGCOMM} Internet Measurement Workshop, {IMW} 2001, San Francisco, California, USA, November 1-2, 2001",
            r"Proceedings of the 2nd {ACM} {SIGCOMM} Internet Measurement Workshop, {IMW} 2002, Marseille, France, November 6-8, 2002",
            r"Proceedings of the 1st ACM SIGCOMM Workshop on Internet Measurement",
            r"Proceedings of the 2nd ACM SIGCOMM Workshop on Internet measurment",  # Notice the typo? It's in Google Scholar like that :)
            r"Proceedings of the 3rd {ACM} {SIGCOMM} Internet Measurement Conference, {IMC} 2003, Miami Beach, FL, USA, October 27-29, 2003",
            r"Proceedings of the 3rd ACM SIGCOMM conference on Internet measurement",
            r"Proceedings of the 5th Internet Measurement Conference, {IMC} 2005, Berkeley, California, USA, October 19-21, 2005",
        }

        self.wrong_strings = {

        }
