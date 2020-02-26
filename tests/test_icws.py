from tests.BaseRunner import BaseRunner


class TestICWS(BaseRunner):

    def setUp(self):
        self.expected_venue = "ICWS"

        self.correct_strings = {
            "ICWS",  # used by DBLP
            "ICWS Computer Society",
            "ICWS-Europe",
            "Proceedings of the {IEEE} International Conference on Web Services (ICWS'04), June 6-9, 2004, San Diego, California, {USA}",
            "Web Services, 2004. Proceedings. IEEE International Conference on",
        }

        self.wrong_strings = {
            "2011 7th International Conference on Next Generation Web Services Practices",
        }
