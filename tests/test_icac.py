from tests.BaseRunner import BaseRunner


class TestICAC(BaseRunner):

    def setUp(self):
        self.expected_venue = "ICAC"

        self.correct_strings = {
            "ICAC",
            "1st International Conference on Autonomic Computing {(ICAC} 2004), 17-19 May 2004, New York, NY, {USA}",
            "International Conference on Autonomic Computing, 2004. Proceedings.",
            "2018 {IEEE} International Conference on Autonomic Computing, {ICAC} 2018, Trento, Italy, September 3-7, 2018",
        }

        self.wrong_strings = {
        }
