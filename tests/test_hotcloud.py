from tests.BaseRunner import BaseRunner


class TestTJS(BaseRunner):

    def setUp(self):
        self.expected_venue = "HotCloud"

        self.correct_strings = {
            "HotCloud",  # Google Scholar
            "Workshop on Hot Topics in Cloud Computing, HotCloud'09, San Diego, CA, USA, June 15, 2009",
            "8th {USENIX} Workshop on Hot Topics in Cloud Computing, HotCloud 2016, Denver, CO, USA, June 20-21, 2016.",
        }

        self.wrong_strings = {
        }
