from tests.BaseRunner import BaseRunner


class TestUCC(BaseRunner):

    def setUp(self):
        self.expected_venue = "UCC"

        self.correct_strings = {
            "UCC",  # used by DBLP
            "{IEEE} 4th International Conference on Utility and Cloud Computing, {UCC} 2011, Melbourne, Australia, December 5-8, 2011"
            "Utility and Cloud Computing (UCC), 2011 Fourth IEEE International Conference on",
            "Proceedings of the 7th {IEEE/ACM} International Conference on Utility and Cloud Computing, {UCC} 2014, London, United Kingdom, December 8-11, 2014",
            "2018 IEEE/ACM 11th International Conference on Utility and Cloud Computing (UCC)",
            "Proceedings of the 9th International Conference on Utility and Cloud Computing",
        }

        self.wrong_strings = {
            "2018 {IEEE/ACM} International Conference on Utility and Cloud Computing Companion, {UCC} Companion 2018, Zurich, Switzerland, December 17-20, 2018",
            "Companion Proceedings of the 10th International Conference on Utility and Cloud Computing, {UCC} 2017, Austin, TX, USA, December 5-8, 2017",
        }
