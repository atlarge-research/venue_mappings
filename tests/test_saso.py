from tests.BaseRunner import BaseRunner


class TestDSN(BaseRunner):

    def setUp(self):
        self.expected_venue = "SASO"

        self.correct_strings = {
            r"SASO",  # used by DBLP
            r"13th {IEEE} International Conference on Self-Adaptive and Self-Organizing Systems, {SASO} 2019, Umea, Sweden, June 16-20, 2019",
            r"2019 IEEE 13th International Conference on Self-Adaptive and Self-Organizing Systems (SASO)",
            r"Proceedings of the First International Conference on Self-Adaptive and Self-Organizing Systems, {SASO} 2007, Boston, MA, USA, July 9-11, 2007",
        }

        self.wrong_strings = {
            r"SASO Workshops",
            r"{IEEE} 4th International Workshops on Foundations and Applications of Self* Systems, FAS*W@SASO/ICCAC 2019, Umea, Sweden, June 16-20, 2019",
            r"2019 IEEE 4th International Workshops on Foundations and Applications of Self* Systems (FAS* W)",
        }
