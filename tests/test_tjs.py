from tests.BaseRunner import BaseRunner


class TestTJS(BaseRunner):

    def setUp(self):
        self.expected_venue = "TJS"

        self.correct_strings = {
            "TJS",
            "The Journal of Supercomputing",
        }

        self.wrong_strings = {
            "Proceedings of the {ACM/IEEE} Conference on Supercomputing, {SC} 1999, November 13-19, 1999, Portland, Oregon, {USA}",
        }
