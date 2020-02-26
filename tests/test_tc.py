from tests.BaseRunner import BaseRunner


class TestTC(BaseRunner):

    def setUp(self):
        self.expected_venue = "TC"

        self.correct_strings = {
            "TC",
            "{IEEE} Trans. Computers",
            "IEEE Transactions on Computers",
        }

        self.wrong_strings = {

        }
