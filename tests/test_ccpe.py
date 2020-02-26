from tests.BaseRunner import BaseRunner


class TestCCPE(BaseRunner):

    def setUp(self):
        self.expected_venue = "CCPE"

        self.correct_strings = {
            "CCPE",  # used by DBLP
            "Concurrency - Practice and Experience",
            "Concurrency: practice and experience",
            "Concurrency and Computation: Practice and Experience",
        }

        self.wrong_strings = {
        }
