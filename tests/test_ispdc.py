from tests.BaseRunner import BaseRunner


class TestISPDC(BaseRunner):

    def setUp(self):
        self.expected_venue = "ISPDC"

        self.correct_strings = {
            "ISPDC",  # used by DBLP
            "16th International Symposium on Parallel and Distributed Computing, {ISPDC} 2017, Innsbruck, Austria, July 3-6, 2017",
            "2nd International Symposium on Parallel and Distributed Computing {(ISPDC} 2003), 13-14 October 2003, Ljubljana, Slovenia",
            "2018 17th International Symposium on Parallel and Distributed Computing (ISPDC)",  # Google Scholar
        }

        self.wrong_strings = {
            }
