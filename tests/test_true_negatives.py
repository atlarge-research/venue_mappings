from tests.BaseRunner import BaseRunner


class TestTrueNegatives(BaseRunner):

    def setUp(self):
        self.expected_venue = None

        self.correct_strings = {
            "",
            " ",
            "fake conference",
            "?",
            "none",
            "null",
        }

        self.wrong_strings = {
            }
