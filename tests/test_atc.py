from tests.BaseRunner import BaseRunner


class TestATC(BaseRunner):

    def setUp(self):
        self.expected_venue = "ATC"

        self.correct_strings = {
            "USENIX Annual Technical Conference",  # used by DBLP
            "Proceedings of the {USENIX} Summer Conference, Altanta, GA, USA, June 1986",
            "Proceedings of the Usenix Winter 1993 Technical Conference, San Diego, California, USA, January 1993",
            "Proceedings of the {USENIX} Annual Technical Conference, San Diego, California, USA, January 22-26, 1996",
            "Proceedings of the {FREENIX} Track: 1999 {USENIX} Annual Technical Conference, June 6-11, 1999, Monterey, California, {USA}",
            "2017 {USENIX} Annual Technical Conference, {USENIX} {ATC} 2017, Santa Clara, CA, USA, July 12-14, 2017.",
            "Proc. of ATC", # Used by Google Scholar
        }

        self.wrong_strings = {
            }
