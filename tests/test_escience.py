from tests.BaseRunner import BaseRunner


class TestEScience(BaseRunner):

    def setUp(self):
        self.expected_venue = "e-Science"

        self.correct_strings = {
            "e-Science and Grid Computing, 2005. First International Conference on",
            "First International Conference on e-Science and Grid Technologies (e-Science 2005), 5-8 December 2005, Melbourne, Australia",
            "14th {IEEE} International Conference on e-Science, e-Science 2018, Amsterdam, The Netherlands, October 29 - November 1, 2018",
            "First International Conference on e-Science and Grid Computing (e-Science'05)",
            "Third International Conference on e-Science and Grid Computing, e-Science 2007, 10-13 December 2007, Bangalore, India",
            "2015 IEEE 11th International Conference on e-Science",
        }

        self.wrong_strings = {
            "10th {IEEE} International Conference on e-Science, eScience Workshops 2014, Sao Paulo, Brazil, October 20-24, 2014"
        }
