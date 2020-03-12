from tests.BaseRunner import BaseRunner


class TestSC(BaseRunner):

    def setUp(self):
        self.expected_venue = "SC"

        self.correct_strings = {
            "SC",  # used by DBLP
            "Proceedings of the {ACM/IEEE} {SC2005} Conference on High Performance Networking and Computing, November 12-18, 2005, Seattle, WA, USA, CD-Rom",
            "Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, {SC} 2015, Austin, TX, USA, November 15-20, 2015",
            "Proceedings Supercomputing '88, Orlando, FL, USA, November 12-17, 1988",
            "Proceedings of the {ACM/IEEE} Conference on Supercomputing, {SC} 1999, November 13-19, 1999, Portland, Oregon, {USA}",
            "SC State of the Practice Reports",  # DBLP
            "International Conference on Supercomputing",
            "Conference on High Performance Computing Networking, Storage and Analysis, {SC} 2011, Seattle, WA, USA, November 12-18, 2011",
            "Proceedings of the Conference on High Performance Computing Networking, Storage and Analysis",
        }

        self.wrong_strings = {
            "{IEEE/ACM} 8th Workshop on Fault Tolerance for {HPC} at eXtreme Scale, FTXS@SC 2018, Dallas, TX, USA, November 16, 2018"
            "WHPCF'11, Proceedings of the Fourth Workshop on High Performance Computational Finance, co-located with SC11, Seattle, WA, USA, November 13, 2011",
        }
