from tests.BaseRunner import BaseRunner


class TestPSI(BaseRunner):

    def setUp(self):
        self.expected_venue = "PSI"

        self.correct_strings = {
            "Perspectives of System Informatics - 9th International Ershov Informatics Conference, {PSI} 2014, St. Petersburg, Russia, June 24-27, 2014. Revised Selected Papers",
            "International Sympoisum on Theoretical Programming, Novosibirsk, Russia, August 7-11, 1972, Proceedings",
            "International Symposium on Theoretical Programming",  # Google Scholar
            "International Andrei Ershov Memorial Conference on Perspectives of System Informatics", # Google Scholar
            "Ershov Memorial Conference", # DBLP
        }

        self.wrong_strings = {
        }
