from tests.BaseRunner import BaseRunner


class TestWoWMoM(BaseRunner):

    def setUp(self):
        self.expected_venue = "WOWMOM"

        self.correct_strings = {
            "WoWMoM",
            "WOWMOM",
            "Proceedings of First {ACM} International Workshop on Wireless Mobile Multimedia, {WOWMOM} '98, Dallas, TX, USA, October 30, 1998",
            "Proceedings of the 1st ACM international workshop on Wireless mobile multimedia",
            "2005 International Conference on a World of Wireless, Mobile and Multimedia Networks {(WOWMOM} 2005), 13-16 June 2005, Taormina, Italy, Proceedings",
            "World of Wireless Mobile and Multimedia Networks, 2005. WoWMoM 2005. Sixth IEEE International Symposium on a",
            "19th {IEEE} International Symposium on \"A World of Wireless, Mobile and Multimedia Networks\", WoWMoM 2018, Chania, Greece, June 12-15, 2018",
        }

        self.wrong_strings = {
        }
