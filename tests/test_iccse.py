from tests.BaseRunner import BaseRunner


class TestICCSE(BaseRunner):

    def setUp(self):
        self.expected_venue = "ICCSE"

        self.correct_strings = {
            "Proceedings of the 2nd International Conference on Crowd Science and Engineering, {ICCSE} 2017, Beijing, China, July 06 - 09, 2017",
            "Proceedings of the 2nd International Conference on Crowd Science and Engineering",
            }

        self.wrong_strings = {
            }
