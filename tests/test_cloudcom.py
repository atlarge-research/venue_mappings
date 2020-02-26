from tests.BaseRunner import BaseRunner


class TestCloudCom(BaseRunner):

    def setUp(self):
        self.expected_venue = "CloudCom"

        self.correct_strings = {
            "CloudCom",  # used by DBLP
            "CloudCom (1)",  # DBLP
            "Cloud Computing, First International Conference, CloudCom 2009, Beijing, China, December 1-4, 2009. Proceedings",
            "Cloud Computing, Second International Conference, CloudCom 2010, November 30 - December 3, 2010, Indianapolis, Indiana, USA, Proceedings",
            "{IEEE} 3rd International Conference on Cloud Computing Technology and Science, CloudCom 2011, Athens, Greece, November 29 - December 1, 2011",
            "IEEE} 5th International Conference on Cloud Computing Technology and Science, CloudCom 2013, Bristol, United Kingdom, December 2-5, 2013, Volume 2",
            "2018 {IEEE} International Conference on Cloud Computing Technology and Science, CloudCom 2018, Nicosia, Cyprus, December 10-13, 2018",
            "2018 IEEE International Conference on Cloud Computing Technology and Science (CloudCom)",

        }

        self.wrong_strings = {
        }
