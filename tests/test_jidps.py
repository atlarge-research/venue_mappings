from tests.BaseRunner import BaseRunner


class TestJIDPS(BaseRunner):

    def setUp(self):
        self.expected_venue = "JIDPS"

        self.correct_strings = {
            "JIDPS",  # Not observed in the wild, just to be safe.
            "J. Integrated Design {\&} Process Science",  # DBLP
            "Transactions of the {SDPS}",
            "Journal of Integrated Design and Process Science",  # Google Scholar
        }

        self.wrong_strings = {
        }
