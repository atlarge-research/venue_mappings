from tests.BaseRunner import BaseRunner


class TestICPE(BaseRunner):

    def setUp(self):
        self.expected_venue = "ICPE"

        self.correct_strings = {
            "ICPE",  # used by DBLP
            "{WOSP}",  # DBLP
            "Proceedings of the 1st international workshop on Software and performance",
            "Proceedings of the first joint {WOSP/SIPEW} International Conference on Performance Engineering, San Jose, California, USA, January 28-30, 2010",
            "ICPE'11 - Second Joint {WOSP/SIPEW} International Conference on Performance Engineering, Karlsruhe, Germany, March 14-16, 2011",
            "Proceedings of the 2018 {ACM/SPEC} International Conference on Performance Engineering, {ICPE} 2018, Berlin, Germany, April 09-13, 2018",
        }

        self.wrong_strings = {
            "Proceedings of the 2013 international workshop on Hot topics in cloud services, HotTopiCS 2013, co-located with ICPE'13, Czech Republic, April 20-21, 2013",
            "Proceedings of the 2015 Workshop on Challenges in Performance Methods for Software Development, WOSP-C'15, Austin, TX, USA, January 31, 2015",
            "Companion of the 2018 {ACM/SPEC} International Conference on Performance Engineering, {ICPE} 2018, Berlin, Germany, April 09-13, 2018",
            "Power Electronics and ECCE Asia (ICPE-ECCE Asia), 2015 9th International Conference on",
            "ICPE Companion",  # Semantic Scholar
        }
