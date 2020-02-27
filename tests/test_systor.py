from tests.BaseRunner import BaseRunner


class TestSYSTOR(BaseRunner):

    def setUp(self):
        self.expected_venue = "SYSTOR"

        self.correct_strings = {
            r"SYSTOR",  # used by DBLP
            r"Proceedings of of {SYSTOR} 2009: The Israeli Experimental Systems Conference 2009, Haifa, Israel, May 4-6, 2009",  # DBLP
            r"International Conference on Systems and Storage, {SYSTOR} 2014, Haifa, Israel, June 30 - July 02, 2014",
            r"Proceedings of SYSTOR 2009: The Israeli Experimental Systems Conference",
            r"Proceedings of International Conference on Systems and Storage",
            r"Proceedings of the 12th {ACM} International Conference on Systems and Storage, {SYSTOR} 2019, Haifa, Israel, June 3-5, 2019",
            r"Proceedings of the 12th ACM International Conference on Systems and Storage",
        }

        self.wrong_strings = {

        }
