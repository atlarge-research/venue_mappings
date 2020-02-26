from tests.BaseRunner import BaseRunner


class TestGCC(BaseRunner):

    def setUp(self):
        self.expected_venue = "GCC"

        self.correct_strings = {
            "GCC",  # used by DBLP
            "GCC (1)",  # DBLP
            "Grid and Cooperative Computing, Second International Workshop, {GCC} 2003, Shanghai, China, December 7-10, 2003, Revised Papers, Part {II}",
            "International Conference on Grid and Cooperative Computing",
            "{GCC} 2010, The Ninth International Conference on Grid and Cloud Computing, Nanjing, Jiangsu, China, 1-5 November 2010",
            "Grid and Cooperative Computing, Second International Workshop, {GCC} 2003, Shanghai, China, December 7-10, 2003, Revised Papers, Part {II}",
            }

        self.wrong_strings = {
            "Grid and Cooperative Computing - {GCC} 2004 Workshops: {GCC} 2004 International Workshops, IGKG, SGT, GISS, AAC-GEVO, and VVS, Wuhan, China, October 21-24, 2004. Proceedings",
        }
