from tests.BaseRunner import BaseRunner


class TestEDBT(BaseRunner):

    def setUp(self):
        self.expected_venue = "EDBT"

        self.correct_strings = {
            "EDBT",  # used by DBLP
            "Advances in Database Technology - EDBT'88, Proceedings of the International Conference on Extending Database Technology, Venice, Italy, March 14-18, 1988",
            "International Conference on Extending Database Technology",
            "Proceedings of the Workshops of the {EDBT/ICDT} 2018 Joint Conference {(EDBT/ICDT} 2018), Vienna, Austria, March 26, 2018.",
            "Workshops of the EDBT/ICDT 2017 Joint Conference (EDBT/ICDT 2017)",
        }

        self.wrong_strings = {
        }
