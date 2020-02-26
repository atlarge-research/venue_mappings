from tests.BaseRunner import BaseRunner


class TestINFOCOM(BaseRunner):

    def setUp(self):
        self.expected_venue = "INFOCOM"

        self.correct_strings = {
            "INFOCOM",  # used by DBLP
            "Proceedings {IEEE} {INFOCOM} '91, The Conference on Computer Communications, Tenth Annual Joint Conference of the {IEEE} Computer and Communications Societies, Networking in the 90s, Bal Harbour, Florida, USA, April 7-11, 1991",
            "[Proceedings] IEEE INFOCOM'92: The Conference on Computer Communications",  # Google Scholar
            "IEEE INFOCOM 2019-IEEE Conference on Computer Communications",  # Used by Google Scholar
        }

        self.wrong_strings = {
            "INFOCOM Workshop",
            "{IEEE} {INFOCOM} 2018 - {IEEE} Conference on Computer Communications Workshops, {INFOCOM} Workshops 2018, Honolulu, HI, USA, April 15-19, 2018",
            "IEEE INFOCOM 2018-IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS)",
            }
