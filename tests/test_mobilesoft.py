from tests.BaseRunner import BaseRunner


class TestMOBILESoft(BaseRunner):

    def setUp(self):
        self.expected_venue = "MOBILESoft"

        self.correct_strings = {
            "MOBILESoft",  # used by DBLP
            "Proceedings of the 1st International Conference on Mobile Software Engineering and Systems, MOBILESoft 2014, Hyderabad, India, June 2-3, 2014}",
            "Proceedings of the 1st International Conference on Mobile Software Engineering and Systems",
            "Proceedings of the 5th International Conference on Mobile Software Engineering and Systems, MOBILESoft@ICSE 2018, Gothenburg, Sweden, May 27 - 28, 2018",
        }

        self.wrong_strings = {
            }
