from tests.BaseRunner import BaseRunner


class TestJPDC(BaseRunner):

    def setUp(self):
        self.expected_venue = "JPDC"

        self.correct_strings = {
            "Journal of Parallel and Distributed Computing",  # Google Scholar
            "J. Parallel Distrib. Comput.",  # DBLP
        }

        self.wrong_strings = {
        }
