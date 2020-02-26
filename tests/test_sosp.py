from tests.BaseRunner import BaseRunner


class TestSOSP(BaseRunner):

    def setUp(self):
        self.expected_venue = "SOSP"

        self.correct_strings = {
            "SOSP",  # used by DBLP
            "Proceedings of the Second Symposium on Operating Systems Principles, {SOSP} 1969, Princeton, NJ, USA, October 20-22, 1969",
            "Proceedings of the second symposium on Operating systems principles",
            }

        self.wrong_strings = {
            "Proceedings of the 6th Workshop on Programming Languages and Operating Systems, PLOS@SOSP 2011, Cascais, Portugal, October 23, 2011",

            }
