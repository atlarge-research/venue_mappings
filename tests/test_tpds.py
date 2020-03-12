from tests.BaseRunner import BaseRunner


class TestTPDS(BaseRunner):

    def setUp(self):
        self.expected_venue = "TPDS"

        self.correct_strings = {
            "IEEE Trans. Parallel Distrib. Syst.",  # used by DBLP
            "{IEEE} Trans. Parallel Distrib. Syst.",
            "IEEE Transactions on parallel and distributed systems",  # Google Scholar
            "IEEE transactions on parallel and distributed systems",
        }

        self.wrong_strings = {
        }
