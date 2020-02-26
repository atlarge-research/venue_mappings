from tests.BaseRunner import BaseRunner


class TestPPOPP(BaseRunner):

    def setUp(self):
        self.expected_venue = "PPOPP"

        self.correct_strings = {
            "PPOPP",  # used by DBLP
            "Proceedings of the 23rd {ACM} {SIGPLAN} Symposium on Principles and Practice of Parallel Programming, PPoPP 2018, Vienna, Austria, February 24-28, 2018",
            "Proceedings of the {ACM/SIGPLAN} {PPEALS} 1988, Parallel Programming: Experience with Applications, Languages and Systems, New Haven, Connecticut, USA, July 19-21, 1988",
            "Proceedings of the Second {ACM} {SIGPLAN} Symposium on Princiles {\&} Practice of Parallel Programming (PPOPP), Seattle, Washington, USA, March 14-16, 1990",
            "Proceedings of the 23rd ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming",
        }

        self.wrong_strings = {
            "11th Workshop on General Purpose Processing using GPUs, GPGPU@PPoPP 2018, February 25, 2018, Vosendorf (Vienna), Austria",
            "Proceedings of the 4th Workshop on Programming Models for SIMD/Vector Processing, WPMVP@PPoPP 2018, Vienna, Austria, February 24, 2018",
            "Proceedings of the 9th International Workshop on Programming Models and Applications for Multicores and Manycores, PMAM@PPoPP 2018, February 25, 2018, Vienna, Austria",
        }
