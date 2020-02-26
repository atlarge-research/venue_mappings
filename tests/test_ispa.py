from tests.BaseRunner import BaseRunner


class TestISPA(BaseRunner):

    def setUp(self):
        self.expected_venue = "ISPA"

        self.correct_strings = {
            "Parallel and Distributed Processing and Applications, International Symposium, {ISPA} 2003, Aizu, Japan, July 2-4, 2003, Proceedings",
            "12th {IEEE} International Conference on Trust, Security and Privacy in Computing and Communications, TrustCom 2013 / 11th {IEEE} International Symposium on Parallel and Distributed Processing with Applications, {ISPA-13} / 12th {IEEE} International Conference on Ubiquitous Computing and Communications, IUCC-2013, Melbourne, Australia, July 16-18, 2013",
            "2017 {IEEE} International Symposium on Parallel and Distributed Processing with Applications and 2017 {IEEE} International Conference on Ubiquitous Computing and Communications (ISPA/IUCC), Guangzhou, China, December 12-15, 2017",
            "Ubiquitous Computing and Communications (ISPA/IUCC), 2017 IEEE International Symposium on Parallel and Distributed Processing with Applications and 2017 IEEE International Conference on",
        }

        self.wrong_strings = {
            "2011 IEEE Ninth International Symposium on Parallel and Distributed Processing with Applications Workshops"
        }
