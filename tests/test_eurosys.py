from tests.BaseRunner import BaseRunner


class TestEuroSys(BaseRunner):

    def setUp(self):
        self.expected_venue = "EuroSys"

        self.correct_strings = {
            "EuroSys",  # used by DBLP
            "Proceedings of the 2006 EuroSys Conference, Leuven, Belgium, April 18-21, 2006",
            "ACM SIGOPS Operating Systems Review",
            "European Conference on Computer Systems, Proceedings of the 5th European conference on Computer systems, EuroSys 2010, Paris, France, April 13-16, 2010",
            "Proceedings of the Tenth European Conference on Computer Systems",
        }

        self.wrong_strings = {
            "Proceedings of the 1st workshop on Middleware-Application Interaction, {MAI} 2007, in conjunction with Euro-Sys 2007, Lisbon, Portugal, March 20, 2007",
            "Proceedings of the Fourth International Workshop on Cloud Data and Platforms, CloudDP@EuroSys 2014, Amsterdam, The Netherlands, April 13, 2014",
        }
