from tests.BaseRunner import BaseRunner


class TestNDSS(BaseRunner):

    def setUp(self):
        self.expected_venue = "NDSS"

        self.correct_strings = {
            "NDSS",  # used by DBLP
            "1995 Symposium on Network and Distributed System Security, {(S)NDSS} '95, San Diego, California, USA, February 16-17, 1995",
            "Network and Distributed System Security, 1995., Proceedings of the Symposium on",
            "5th Annual Network and Distributed System Security Symposium, {NDSS} 2018, San Diego, California, USA, February 18-21, 2018",
            "Proc. Network and Distributed Systems Symposium (NDSS)",
        }

        self.wrong_strings = {
        }
