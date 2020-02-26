from tests.BaseRunner import BaseRunner


class TestCloudComp(BaseRunner):

    def setUp(self):
        self.expected_venue = "CloudComp"

        self.correct_strings = {
            "CloudComp",
            "Cloud Computing - First International Conference, CloudComp 2009, Munich, Germany, October 19-21, 2009 Revised Selected Papers",
            "Cloud Computing - 6th International Conference, CloudComp 2015, Daejeon, South Korea, October 28-29, 2015, Proceedings",
            "International Conference on Cloud Computing", # Google Scholar
        }

        self.wrong_strings = {
            }
