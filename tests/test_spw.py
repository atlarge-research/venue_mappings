from tests.BaseRunner import BaseRunner


class TestSPW(BaseRunner):

    def setUp(self):
        self.expected_venue = "SPW"

        self.correct_strings = {
            "SPW",
            "Security Protocols Workshop",  # DBLP
            "Security Protocols, International Workshop, Cambridge, United Kingdom, April 10-12, 1996, Proceedings",
            "International Workshop on Security Protocols",
            "Security Protocols {XXVI} - 26th International Workshop, Cambridge, UK, March 19-21, 2018, Revised Selected Papers",
            "Cambridge International Workshop on Security Protocols",
        }

        self.wrong_strings = {
        }
