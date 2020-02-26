from tests.BaseRunner import BaseRunner


class TestIPDPS(BaseRunner):

    def setUp(self):
        self.expected_venue = "IPDPS"

        self.correct_strings = {
            "IPDPS",  # used by DBLP
            "2018 {IEEE} International Parallel and Distributed Processing Symposium, {IPDPS} 2018, Vancouver, BC, Canada, May 21-25, 2018",
            "18th International Parallel and Distributed Processing Symposium {(IPDPS} 2004), {CD-ROM} / Abstracts Proceedings, 26-30 April 2004, Santa Fe, New Mexico, {USA}",
            "Parallel and Distributed Processing Symposium, 2004. Proceedings. 18th International",
        }

        self.wrong_strings = {
            "The Fifth International Parallel Processing Symposium, Proceedings, Anaheim, California, USA, April 30 - May 2, 1991.",
            "11th International Parallel Processing Symposium {(IPPS} '97), 1-5 April 1997, Geneva, Switzerland, Proceedings",
            "Job Scheduling Strategies for Parallel Processing, IPPS/SPDP'99 Workshop, JSSPP'99, San Juan, Puerto Rico, April 16, 1999, Proceedings",
        }
