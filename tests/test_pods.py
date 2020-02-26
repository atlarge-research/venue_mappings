from tests.BaseRunner import BaseRunner


class TestPODS(BaseRunner):

    def setUp(self):
        self.expected_venue = "PODS"

        self.correct_strings = {
            "Proceedings of the {ACM} Symposium on Principles of Database Systems, March 29-31, 1982, Los Angeles, California, {USA}",
            "Proceedings of the 31st {ACM} {SIGMOD-SIGACT-SIGART} Symposium on Principles of Database Systems, {PODS} 2012, Scottsdale, AZ, USA, May 20-24, 2012",
            "Proceedings of the 31st ACM SIGMOD-SIGACT-SIGAI symposium on Principles of Database Systems",
        }

        self.wrong_strings = {

        }
