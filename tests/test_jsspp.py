from tests.BaseRunner import BaseRunner


class TestJSSPP(BaseRunner):

    def setUp(self):
        self.expected_venue = "JSSPP"

        self.correct_strings = {
            "JSSPP",  # used by DBLP
            "Job Scheduling Strategies for Parallel Processing, IPPS'95 Workshop, Santa Barbara, CA, USA, April 25, 1995, Proceedings",
            "Workshop on Job Scheduling Strategies for Parallel Processing",
            "Job Scheduling Strategies for Parallel Processing - 19th and 20th International Workshops, {JSSPP} 2015, Hyderabad, India, May 26, 2015 and {JSSPP} 2016, Chicago, IL, USA, May 27, 2016, Revised Selected Papers",
        }

        self.wrong_strings = {
        }
