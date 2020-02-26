from tests.BaseRunner import BaseRunner


class TestIBMRD(BaseRunner):

    def setUp(self):
        self.expected_venue = "IBMRD"

        self.correct_strings = {
            "{IBM} Journal of Research and Development",
            "IBM Journal of Research and Development", # Google Scholar
        }

        self.wrong_strings = {
            }
