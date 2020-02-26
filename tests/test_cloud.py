from tests.BaseRunner import BaseRunner


class TestCLOUD(BaseRunner):

    def setUp(self):
        self.expected_venue = "CLOUD"

        self.correct_strings = {
            "CLOUD",  # used by DBLP
            "IEEE CLOUD",  # DBLP
            "{IEEE} International Conference on Cloud Computing, {CLOUD} 2009, Bangalore, India, 21-25 September, 2009",
            "2009 IEEE International Conference on Cloud Computing",
            "2018 IEEE 11th International Conference on Cloud Computing (CLOUD)",
        }

        self.wrong_strings = {
        }
