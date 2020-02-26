from tests.BaseRunner import BaseRunner


class TestNOSSDAV(BaseRunner):

    def setUp(self):
        self.expected_venue = "NOSSDAV"

        self.correct_strings = {
            "NOSSDAV",  # used by DBLP
            "Network and Operating System Support for Digital Audio and Video, Second International Workshop, Heidelberg, Germany, November 18-19, 1991, Proceedings",
            "International Workshop on Network and Operating System Support for Digital Audio and Video",
            }

        self.wrong_strings = {
            }
