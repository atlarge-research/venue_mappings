from tests.BaseRunner import BaseRunner


class TestICDCS(BaseRunner):

    def setUp(self):
        self.expected_venue = "ICDCS"

        self.correct_strings = {
            "ICDCS",  # used by DBLP
            "38th {IEEE} International Conference on Distributed Computing Systems, {ICDCS} 2018, Vienna, Austria, July 2-6, 2018",
            "Proceedings of the 2nd International Conference on Distributed Computing Systems, Paris, France, 1981",
            "29th {IEEE} International Conference on Distributed Computing Systems {(ICDCS} 2009), 22-26 June 2009, Montreal, Qu{\'{e}}bec, Canada",
            "Distributed Computing Systems, 2009. ICDCS'09. 29th IEEE International Conference on",
        }

        self.wrong_strings = {
            "37th {IEEE} International Conference on Distributed Computing Systems Workshops, {ICDCS} Workshops 2017, Atlanta, GA, USA, June 5-8, 2017",

        }
