from tests.BaseRunner import BaseRunner


class TestHiPC(BaseRunner):

    def setUp(self):
        self.expected_venue = "HiPC"

        self.correct_strings = {
            "HiPC",  # Used by DBLP
            "23rd {IEEE} International Conference on High Performance Computing, HiPC 2016, Hyderabad, India, December 19-22, 2016",
            "2016 IEEE 23rd International Conference on High Performance Computing (HiPC)",
            "3rd International Conference on High Performance Computing, {HIPC} 1996, Proceedings, Trivandrum, India, 19-22 December, 1996",
            "High Performance Computing - HiPC'99, 6th International Conference, Calcutta, India, December 17-20, 1999, Proceedings",
        }

        self.wrong_strings = {
        }
