from tests.BaseRunner import BaseRunner


class TestCCGrid(BaseRunner):

    def setUp(self):
        self.expected_venue = "CCGrid"

        self.correct_strings = {
            r"CCGrid",
            r"CCGRID",
            r"18th IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing, CCGRID 2018, Washington, DC, USA, May 1-4, 2018.",
            r"15th {IEEE/ACM} International Symposium on Cluster, Cloud and Grid Computing, CCGrid 2015, Shenzhen, China, May 4-7, 2015",
            r"First IEEE International Symposium on Cluster Computing and the Grid (CCGrid 2001), May 15-18, 2001, Brisbane, Australia.",
            r"Proceedings of the 2011 11th IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing",
            r"Cluster Computing and the Grid, 2005. CCGrid 2005. IEEE International Symposium on",
            r"10th {IEEE/ACM} International Conference on Cluster, Cloud and Grid Computing, CCGrid 2010, 17-20 May 2010, Melbourne, Victoria, Australia",
            r"Cluster, Cloud and Grid Computing (CCGrid), 2013 13th IEEE/ACM International Symposium on",
        }

        self.wrong_strings = {
            r"The First International Workshop on Advances in High-Performance Algorithms Middleware and Applications (AHPAMA 2018)",
            r"3rd IEEE/ACM International Workshop on Distributed Big Data Management (DBDM 2018)",
        }
