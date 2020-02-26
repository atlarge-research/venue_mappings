from tests.BaseRunner import BaseRunner


class TestFAST(BaseRunner):

    def setUp(self):
        self.expected_venue = "FAST"

        self.correct_strings = {
            r"FAST",  # used by DBLP
            r"Proceedings of the {FAST} '02 Conference on File and Storage Technologies, January 28-30, 2002, Monterey, California, {USA}",
            r"17th {USENIX} Conference on File and Storage Technologies, {FAST} 2019, Boston, MA, February 25-28, 2019",
            r"17th $\{$USENIX$\}$ Conference on File and Storage Technologies ($\{$FAST$\}$ 19)",
        }

        self.wrong_strings = {
            r"2007 Linux Storage {\&} Filesystem Workshop, {LSF} 2007, San Jose, CA, USA, February 12-13, 2007",
        }
