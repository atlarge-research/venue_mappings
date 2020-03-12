from tests.BaseRunner import BaseRunner


class TestOSDI(BaseRunner):

    def setUp(self):
        self.expected_venue = "OSDI"

        self.correct_strings = {
            "OSDI",  # used by DBLP
            "Proceedings of the First {USENIX} Symposium on Operating Systems Design and Implementation (OSDI), Monterey, California, USA, November 14-17, 1994",
            "9th {USENIX} Symposium on Operating Systems Design and Implementation, {OSDI} 2010, October 4-6, 2010, Vancouver, BC, Canada, Proceedings",
            "13th $\{$USENIX$\}$ Symposium on Operating Systems Design and Implementation ($\{$OSDI$\}$ 18)",
            "Proceedings of the 1st USENIX conference on Operating Systems Design and Implementation",
        }

        self.wrong_strings = {
            "2010 Workshop on the Economics of Networks, Systems, and Computation, NetEcon@OSDI 2010, Vancouver, BC, Canada, October 3, 2010",
            "4th Workshop on Interactions of NVM/Flash with Operating Systems and Workloads, INFLOW@OSDI 2016, Savannah, GA, USA, November 1, 2016.",
        }
