from tests.BaseRunner import BaseRunner


class TestICPP(BaseRunner):

    def setUp(self):
        self.expected_venue = "ICPP"

        self.correct_strings = {
            "ICPP",  # used by DBLP
            "ICPP (1)",  # DBLP
            "International Conference on Parallel Processing, ICPP'82, August 24-27, 1982, Bellaire, Michigan, {USA}",
            "Proceedings of the International Conference on Parallel Processing, {ICPP} '88, The Pennsylvania State University, University Park, PA, USA, August 1988. Volume 2: Software.",
            "Proceedings of the 47th International Conference on Parallel Processing",
            "Proceedings of the 1994 International Conference on Parallel Processing, North Carolina State University, NC, USA, August 15-19, 1994. Volume {I:} Architecture.",
        }

        self.wrong_strings = {
            "32nd International Conference on Parallel Processing Workshops {(ICPP} 2003 Workshops), 6-9 October 2003, Kaohsiung, Taiwan",
            "The 47th International Conference on Parallel Processing, {ICPP} 2018, Workshop Proceedings, Eugene, OR, USA, August 13-16, 2018",
            "Proceedings of the 47th International Conference on Parallel Processing Companion",
        }
