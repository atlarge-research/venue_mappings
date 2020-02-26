from tests.BaseRunner import BaseRunner


class TestFiCloud(BaseRunner):

    def setUp(self):
        self.expected_venue = "FiCloud"

        self.correct_strings = {
            "FiCloud",  # used by DBLP
            "5th {IEEE} International Conference on Future Internet of Things and Cloud, FiCloud 2017, Prague, Czech Republic, August 21-23, 2017",
            "Future Internet of Things and Cloud (FiCloud), 2017 IEEE 5th International Conference on",
            "2014 International Conference on Future Internet of Things and Cloud, FiCloud 2014, Barcelona, Spain, August 27-29, 2014",
        }

        self.wrong_strings = {
        }
