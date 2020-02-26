from tests.BaseRunner import BaseRunner


class TestSIGMETRICS(BaseRunner):

    def setUp(self):
        self.expected_venue = "SIGMETRICS"

        self.correct_strings = {
            "SIGMETRICS",  # used by DBLP
            "SIGMETRICS (Abstracts)",  # used by DBLP
            "Proceedings of the Joint International Conference on Measurements and Modeling of Computer Systems, {SIGMETRICS} 1976, March 29-31, 1976, Cambridge, MA, {USA}",
            "Proceedings of the 1976 ACM SIGMETRICS conference on Computer performance modeling measurement and evaluation",
            "Abstracts of the 2018 {ACM} International Conference on Measurement and Modeling of Computer Systems, {SIGMETRICS} 2018, Irvine, CA, USA, June 18-22, 2018",
        }

        self.wrong_strings = {
            "Proceedings of the 13th Workshop on Economics of Networks, Systems and Computation, NetEcon@SIGMETRICS 2018, Irvine, CA, USA, June 18, 2018",
        }
