from tests.BaseRunner import BaseRunner


class TestSERVICES(BaseRunner):

    def setUp(self):
        self.expected_venue = "SERVICES"

        self.correct_strings = {
            "SERVICES",  # used by DBLP
            "SERVICES I",  # DBLP
            "SERVICES II",
            "2008 {IEEE} Congress on Services, Part I, {SERVICES} {I} 2008, Honolulu, Hawaii, USA, July 6-11, 2008",
            "Services-Part I, 2008. IEEE Congress on",
            "2018 {IEEE} World Congress on Services, {SERVICES} 2018, San Francisco, CA, USA, July 2-7, 2018",
            "2018 IEEE World Congress on Services (SERVICES)",
            "IEEE SCW",  # DBLP at it again
        }

        self.wrong_strings = {
            "Services with a fake name to test the regex lookahead",
            }
