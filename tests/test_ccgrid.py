from tests.BaseRunner import BaseRunner


class TestCCGrid(BaseRunner):

    def setUp(self):
        self.expected_venue = "CCGrid"

        self.correct_strings = {
            "CCGrid",
            "CCGRID",
            "18th IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing, CCGRID 2018, Washington, DC, USA, May 1-4, 2018.",
            "15th {IEEE/ACM} International Symposium on Cluster, Cloud and Grid Computing, CCGrid 2015, Shenzhen, China, May 4-7, 2015",
            "First IEEE International Symposium on Cluster Computing and the Grid (CCGrid 2001), May 15-18, 2001, Brisbane, Australia.",
            "Proceedings of the 2011 11th IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing",
            }

        self.wrong_strings = {
            "The First International Workshop on Advances in High-Performance Algorithms Middleware and Applications (AHPAMA 2018)",
            "3rd IEEE/ACM International Workshop on Distributed Big Data Management (DBDM 2018)",
            }
