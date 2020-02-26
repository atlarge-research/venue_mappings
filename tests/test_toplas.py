from tests.BaseRunner import BaseRunner


class TestTOPLAS(BaseRunner):

    def setUp(self):
        self.expected_venue = "TOPLAS"

        self.correct_strings = {
            "TOPLAS",  # used by DBLP
            "{ACM} Trans. Program. Lang. Syst.",  # DBLP
            "ACM Transactions on Programming Languages and Systems (TOPLAS)",
            }

        self.wrong_strings = {
            }
