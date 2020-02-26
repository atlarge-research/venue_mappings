from tests.BaseRunner import BaseRunner


class TestISWC(BaseRunner):

    def setUp(self):
        self.expected_venue = "ISWC"

        self.correct_strings = {
            "ISWC",  # used by DBLP
            "First International Symposium on Wearable Computers {(ISWC} 1997), Cambridge, Massachusetts, USA, 13-14 October 1997, Proceedings.",
            "Wearable Computers, 1997. Digest of Papers., First International Symposium on",
            "Proceedings of the 2015 {ACM} International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2015 {ACM} International Symposium on Wearable Computers, UbiComp/ISWC Adjunct 2015, Osaka, Japan, September 7-11, 2015",
            "Adjunct Proceedings of the 2017 {ACM} International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2017 {ACM} International Symposium on Wearable Computers, UbiComp/ISWC 2017, Maui, HI, USA, September 11-15, 2017",
            "Proceedings of the 2017 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2017 ACM International Symposium on Wearable Computers",
        }

        self.wrong_strings = {
        }
