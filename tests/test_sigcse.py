from tests.BaseRunner import BaseRunner


class TestSIGCSE(BaseRunner):

    def setUp(self):
        self.expected_venue = "SIGCSE"

        self.correct_strings = {
            "SIGSCSE",  # used by DBLP
            "Proceedings of the 17st {SIGCSE} Technical Symposium on Computer Science Education, 1986, Cincinnati, Ohio, USA, February 6-7, 1986",
            "Proceedings of the 49th {ACM} Technical Symposium on Computer Science Education, {SIGCSE} 2018, Baltimore, MD, USA, February 21-24, 2018",
            "Proceedings of the 49th ACM Technical Symposium on Computer Science Education", # Google Scholar
        }

        self.wrong_strings = {
            }
