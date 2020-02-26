from tests.BaseRunner import BaseRunner


class TestFGCS(BaseRunner):

    def setUp(self):
        self.expected_venue = "FGCS"

        self.correct_strings = {
            "FGCS",  # used by DBLP
            "Future Generation Comp. Syst.",
            "Future Generation Computer Systems",
        }

        self.wrong_strings = {
        }
