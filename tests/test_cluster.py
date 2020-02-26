from tests.BaseRunner import BaseRunner


class TestCLUSTER(BaseRunner):

    def setUp(self):
        self.expected_venue = "CLUSTER"

        self.correct_strings = {
            "CLUSTER",  # used by DBLP
            "2000 {IEEE} International Conference on Cluster Computing {(CLUSTER} 2000), November 28th - December 1st, 2000, Technische Universit{\"{a}}t Chemnitz, Saxony, Germany",
            "Cluster Computing, 2000. Proceedings. IEEE International Conference on",
            "{IEEE} International Conference on Cluster Computing, {CLUSTER} 2018, Belfast, UK, September 10-13, 2018",
            }

        self.wrong_strings = {
            }
