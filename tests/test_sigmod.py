from tests.BaseRunner import BaseRunner


class TestSIGMOD(BaseRunner):

    def setUp(self):
        self.expected_venue = "SIGMOD"

        self.correct_strings = {
            "SIGMOD",  # used by DBLP
            "SIGMOD Conference",
            "Proceedings of the 1975 {ACM} {SIGMOD} International Conference on Management of Data, San Jose, California, USA, May 14-16, 1975.",
            "Proceedings of the 1975 ACM SIGMOD international conference on Management of data",
            "SIGMOD'84, Proceedings of Annual Meeting, Boston, Massachusetts, USA, June 18-21, 1984",
            "Proceedings of the Association for Computing Machinery Special Interest Group on Management of Data 1987 Annual Conference, San Francisco, CA, USA, May 27-29, 1987",
            "Proceedings of the {ACM} {SIGMOD} International Conference on Management of Data, {SIGMOD} 2011, Athens, Greece, June 12-16, 2011",
            "Proceedings of the 2018 International Conference on Management of Data",
        }

        self.wrong_strings = {
            "Proceedings of the Workshop on Data Bases for Interactive Design, Canada, September 15-16, 1975.",
            "The Papers of the Fifth Workshop on Computer Architecture for Non-Numeric Processing, Pacific Grove, CA, USA, March 11-14, 1980",
            "Proceedings of the First International Workshop on Performance and Evaluation of Data Management Systems, ExpDB 2006, in cooperation with {ACM} SIGMOD, June 30, 2006, Chicago, Illinois, {USA}",
        }
