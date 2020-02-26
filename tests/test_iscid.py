from tests.BaseRunner import BaseRunner


class TestISCID(BaseRunner):

    def setUp(self):
        self.expected_venue = "ISCID"

        self.correct_strings = {
            "ISCID",  # used by DBLP
            "ISCID (1)",  # DBLP
            "ISCID (2)",  # DBLP
            "2009 Second International Symposium on Computational Intelligence and Design, {ISCID} 2009, Changsha, Hunan, China, 12-14 December 2009, 2 Volumes",
            "Computational Intelligence and Design, 2009. ISCID'09. Second International Symposium on",
            "2011 Fourth International Symposium on Computational Intelligence and Design",
        }

        self.wrong_strings = {
        }
