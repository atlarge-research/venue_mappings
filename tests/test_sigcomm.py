from tests.BaseRunner import BaseRunner


class TestSIGCOMM(BaseRunner):

    def setUp(self):
        self.expected_venue = "SIGCOMM"

        self.correct_strings = {
            "SIGCOMM",  # used by DBLP
            "{SIGCOMM} '81, Proceedings of the seventh symposium on Data communications, 1981",
            "ACM SIGCOMM Computer Communication Review",  # Google Scholar
            "Proceedings of the {ACM} {SIGCOMM} conference on Communications architectures {\&} protocols, 1986, Stowe, Vermont, United States, August 5-7, 1986",
            "Proceedings of the {ACM} {SIGCOMM} 1995 Conference on Applications, Technologies, Architectures, and Protocols for Computer Communication, Cambridge, MA, USA, August 28 - September 1, 1995.",
            "Proceedings of the 2018 Conference of the {ACM} Special Interest Group on Data Communication, {SIGCOMM} 2018, Budapest, Hungary, August 20-25, 2018",
            "Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication",
        }

        self.wrong_strings = {
            "Proceedings of the first workshop on Hot topics in software defined networks, HotSDN@SIGCOMM 2012, Helsinki, Finland, August 13, 2012",
            "Proceedings of the first edition of the {MCC} workshop on Mobile cloud computing, MCC@SIGCOMM 2012, Helsinki, Finland, August 17, 2012",
            "Proceedings of the 2013 {ACM} {SIGCOMM} workshop on Future human-centric multimedia networking, FhMN@SIGCOMM 2013, Hong Kong, China, August 16, 2013",
            "Proceedings of the 5th {ACM} workshop on Hot topics in planet-scale measurement, HotPlanet@SIGCOMM 2013, Hong Kong, China, August 12-16, 2013",
        }
