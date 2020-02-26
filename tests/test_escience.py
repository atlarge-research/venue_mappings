from tests.BaseRunner import BaseRunner


class TestEScience(BaseRunner):

    def setUp(self):
        self.expected_venue = "e-Science"

        self.correct_strings = {
            "e-Science and Grid Computing, 2005. First International Conference on",
            "First International Conference on e-Science and Grid Technologies (e-Science 2005), 5-8 December 2005, Melbourne, Australia",
            "14th {IEEE} International Conference on e-Science, e-Science 2018, Amsterdam, The Netherlands, October 29 - November 1, 2018",
        }

        self.wrong_strings = {
            "10th {IEEE} International Conference on e-Science, eScience Workshops 2014, Sao Paulo, Brazil, October 20-24, 2014"
        }
