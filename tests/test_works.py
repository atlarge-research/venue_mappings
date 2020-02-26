from tests.BaseRunner import BaseRunner


class TestWORKS(BaseRunner):

    def setUp(self):
        self.expected_venue = "WORKS"

        self.correct_strings = {
            "SC-WORKS",
            "Proceedings of the 11th Workshop on Workflows in Support of Large-Scale Science co-located with The International Conference for High Performance Computing, Networking, Storage and Analysis {(SC} 2016), Salt Lake City, Utah, USA, November 14, 2016.",
            "Proceedings of the 4th Workshop on Workflows in Support of Large-Scale Science, {WORKS} 2009, November 16, 2009, Portland, Oregon, {USA}",
            "Workflows in support of large-scale science",  # DBLP
            "Proceedings of the 2nd workshop on Workflows in support of large-scale science",  # Google Scholar
        }

        self.wrong_strings = {
        }
