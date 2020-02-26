from tests.BaseRunner import BaseRunner


class TestSoCC(BaseRunner):

    def setUp(self):
        self.expected_venue = "SoCC"

        self.correct_strings = {
            "SoCC",  # used by DBLP
            "Proceedings of the 1st {ACM} Symposium on Cloud Computing, SoCC 2010, Indianapolis, Indiana, USA, June 10-11, 2010",
            "Proceedings of the 1st ACM symposium on Cloud computing",
            "Proceedings of the {ACM} Symposium on Cloud Computing, SoCC 2018, Carlsbad, CA, USA, October 11-13, 2018",
        }

        self.wrong_strings = {
            }
