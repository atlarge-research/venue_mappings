from tests.BaseRunner import BaseRunner


class TestIC(BaseRunner):

    def setUp(self):
        self.expected_venue = "IC"

        self.correct_strings = {
            "IC",  # used by DBLP
            "IEEE Internet Computing",
            "{IEEE} Internet Computing",
        }

        self.wrong_strings = {
        }
