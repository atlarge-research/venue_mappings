from tests.BaseRunner import BaseRunner


class TestPOPL(BaseRunner):

    def setUp(self):
        self.expected_venue = "POPL"

        self.correct_strings = {
            "POPL",  # used by DBLP
            "Conference Record of the {ACM} Symposium on Principles of Programming Languages, Boston, Massachusetts, USA, October 1973",
            "Proceedings of the 44th {ACM} {SIGPLAN} Symposium on Principles of Programming Languages, {POPL} 2017, Paris, France, January 18-20, 2017",
            "Proceedings of the 1st annual ACM SIGACT-SIGPLAN symposium on Principles of programming languages", # Google Scholar
        }

        self.wrong_strings = {
            "Proceedings of the {POPL} 2005 Workshop on Issues in the Theory of Security, {WITS} 2005, Long Beach, California, USA, January 10-11, 2005",
        }
