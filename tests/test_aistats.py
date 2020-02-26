from tests.BaseRunner import BaseRunner


class TestAISTATS(BaseRunner):

    def setUp(self):
        self.expected_venue = "AISTATS"

        self.correct_strings = {
            "AISTATS",  # used by DBLP
            "Learning from Data - Fifth International Workshop on Artificial Intelligence and Statistics, {AISTATS} 1995, Key West, Florida, USA, January, 1995. Proceedings.",
            "Learning from Data",  # Google Scholar
            "International Conference on Artificial Intelligence and Statistics",  # Google Scholar
        }
        self.wrong_strings = {
            }
