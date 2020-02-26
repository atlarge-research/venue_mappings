from tests.BaseRunner import BaseRunner


class TestPC(BaseRunner):

    def setUp(self):
        self.expected_venue = "PC"

        self.correct_strings = {
            "PC",  # Used by DBLP
            "Parallel Computing",
        }

        self.wrong_strings = {
        }
