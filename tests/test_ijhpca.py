from tests.BaseRunner import BaseRunner


class TestIJHPCA(BaseRunner):

    def setUp(self):
        self.expected_venue = "IJHPCA"

        self.correct_strings = {
            "IJHPCA",  # used by DBLP
            "IJHPCA (1)",  # DBLP
            "{IJHPCA}",
            "The International Journal of High Performance Computing Applications",  # Google Scholar
        }

        self.wrong_strings = {
        }
