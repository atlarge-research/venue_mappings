from tests.BaseRunner import BaseRunner


class TestIC2E(BaseRunner):

    def setUp(self):
        self.expected_venue = "IC2E"

        self.correct_strings = {
            "IC2E",  # used by DBLP
            "Cloud Engineering (IC2E), 2014 IEEE International Conference on",
            "2013 {IEEE} International Conference on Cloud Engineering, {IC2E} 2013, San Francisco, CA, USA, March 25-27, 2013}",
        }

        self.wrong_strings = {
            "2016 {IEEE} International Conference on Cloud Engineering Workshop, {IC2E} Workshops, Berlin, Germany, April 4-8, 2016",
        }
