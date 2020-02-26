from tests.BaseRunner import BaseRunner


class TestICFEC(BaseRunner):

    def setUp(self):
        self.expected_venue = "ICFEC"

        self.correct_strings = {
            "ICFEC",  # DBLP
            "1st {IEEE} International Conference on Fog and Edge Computing, {ICFEC} 2017, Madrid, Spain, May 14-15, 2017",
            "Fog and Edge Computing (ICFEC), 2018 IEEE 2nd International Conference on", # Google Scholar
        }

        self.wrong_strings = {
        }
