from tests.BaseRunner import BaseRunner


class TestSPIRE(BaseRunner):

    def setUp(self):
        self.expected_venue = "SPIRE"

        self.correct_strings = {
            "SPIRE",  # used by DBLP
            "International symposium on string processing and information retrieval",
            "international symposium on string processing and information retrieval",
            "String Processing and Information Retrieval: {A} South American Symposium, {SPIRE} 1998, Santa Cruz de la Sierra Bolivia, September 9-11, 1998",
            "Proceedings. String Processing and Information Retrieval: A South American Symposium (Cat. No. 98EX207)",
            "Sixth International Symposium on String Processing and Information Retrieval and Fifth International Workshop on Groupware, {SPIRE/CRIWG} 1999, Cancun, Mexico, September 21-24, 1999",
            "6th International Symposium on String Processing and Information Retrieval. 5th International Workshop on Groupware (Cat. No. PR00268)",
        }

        self.wrong_strings = {
        }
