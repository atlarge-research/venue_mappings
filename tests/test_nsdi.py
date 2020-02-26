from tests.BaseRunner import BaseRunner


class TestNSDI(BaseRunner):

    def setUp(self):
        self.expected_venue = "NSDI"

        self.correct_strings = {
            "NSDI",  # used by DBLP
            "1st Symposium on Networked Systems Design and Implementation {(NSDI} 2004), March 29-31, 2004, San Francisco, California, USA, Proceedings",
            "15th {USENIX} Symposium on Networked Systems Design and Implementation, {NSDI} 2018, Renton, WA, USA, April 9-11, 2018",
            "USENIX Symposium on Networked Systems Design and Implementation",  # Google Scholar
        }

        self.wrong_strings = {
        }
