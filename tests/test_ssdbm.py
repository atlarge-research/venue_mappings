from tests.BaseRunner import BaseRunner


class TestSSDBM(BaseRunner):

    def setUp(self):
        self.expected_venue = "SSDBM"

        self.correct_strings = {
            "SSDBM",  # used by DBLP
            "Proceedings of the First {LBL} Workshop on Statistical Database Management, Melno Park, California, USA, December 2-4, 1981",
            "Proceedings of the Second International Workshop on Statistical Database Management, Los Altos, California, USA, September 27-29, 1983",
            "Proceedings of the Third International Workshop on Statistical and Scientific Database Management, July 22-24, 1986, Grand Duchy of Luxembourg, Luxembourg",
            "Proceedings of the 15th International Conference on Scientific and Statistical Database Management {(SSDBM} 2003), 9-11 July 2003, Cambridge, MA, {USA}",
        }

        self.wrong_strings = {
        }
