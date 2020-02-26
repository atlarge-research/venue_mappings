from tests.BaseRunner import BaseRunner


class TestHPCC(BaseRunner):

    def setUp(self):
        self.expected_venue = "HPCC"

        self.correct_strings = {
            "HPCC",  # used by DBLP
            "HPCC-ICESS",  # DBLP
            "HPCC/CSS/ICESS",  # DBLP
            "HPCC/SmartCity/DSS",  # DBLP
            "HPCC/EUC",  # DBLP
            "High Performance Computing and Communications, First International Conference, {HPCC} 2005, Sorrento, Italy, September 21-23, 2005, Proceedings",
            "International Conference on High Performance Computing and Communications",
            "14th {IEEE} International Conference on High Performance Computing and Communication {\&} 9th {IEEE} International Conference on Embedded Software and Systems, {HPCC-ICESS} 2012, Liverpool, United Kingdom, June 25-27, 2012",
            "High Performance Computing and Communication \& 2012 IEEE 9th International Conference on Embedded Software and Systems (HPCC-ICESS), 2012 IEEE 14th International Conference on",
            "17th {IEEE} International Conference on High Performance Computing and Communications, {HPCC} 2015, 7th {IEEE} International Symposium on Cyberspace Safety and Security, {CSS} 2015, and 12th {IEEE} International Conference on Embedded Software and Systems, {ICESS} 2015, New York, NY, USA, August 24-26, 2015",
            "10th {IEEE} International Conference on High Performance Computing and Communications, {HPCC} 2008, 25-27 Sept. 2008, Dalian, China",
        }


        self.wrong_strings = {
        }
