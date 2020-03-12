from tests.BaseRunner import BaseRunner


class TestGRID(BaseRunner):

    def setUp(self):
        self.expected_venue = "GRID"

        self.correct_strings = {
            "GRID",  # used by DBLP
            "Grid Computing - {GRID} 2000, First {IEEE/ACM} International Workshop, Bangalore, India, December 17, 2000, Proceedings",
            "International Workshop on Grid Computing",
            "Proceedings of the 2010 11th {IEEE/ACM} International Conference on Grid Computing, Brussels, Belgium, October 25-29, 2010",
            "Grid Computing (GRID), 2010 11th IEEE/ACM International Conference on",
            "Proceedings of the 7th IEEE/ACM International Conference on Grid Computing",
        }

        self.wrong_strings = {
        }
