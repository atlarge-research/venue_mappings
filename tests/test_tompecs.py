from tests.BaseRunner import BaseRunner


class TestTOMPECS(BaseRunner):

    def setUp(self):
        self.expected_venue = "TOMPECS"

        self.correct_strings = {
            "TOMPECS",  # used by DBLP
            "{TOMPECS}",
            "ACM Transactions on Modeling and Performance Evaluation of Computing Systems (TOMPECS)",
        }

        self.wrong_strings = {
            }
