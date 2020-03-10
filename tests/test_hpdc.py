from tests.BaseRunner import BaseRunner


class TestHPDC(BaseRunner):

    def setUp(self):
        self.expected_venue = "HPDC"

        self.correct_strings = {
            r"HPDC",  # used by DBLP
            r"Proceedings of the 27th International Symposium on High-Performance Parallel and Distributed Computing, {HPDC} 2018, Tempe, AZ, USA, June 11-15, 2018",
            r"Proceedings of the First International Symposium on High Performance Distributed Computing, HPDC '92, Syracuse, NY, USA, September 9-11, 1992",
            r"High-Performance Distributed Computing, 1992.(HPDC-1), Proceedings of the First International Symposium on",
            r"11th {IEEE} International Symposium on High Performance Distributed Computing {(HPDC-11} 2002), 23-26 July 2002, Edinburgh, Scotland, {UK}",
            r"Another: Proceedings of the 16th International Symposium on High-Performance Distributed Computing {(HPDC-16} 2007), 25-29 June 2007, Monterey, California, {USA}",
            r"12th International Symposium on High-Performance Distributed Computing {(HPDC-12} 2003), 22-24 June 2003, Seattle, WA, {USA}",
        }

        self.wrong_strings = {
            r"AI-Science@HPDC", "ScienceCloud@HPDC", "ROSS@HPDC",
            r"Proceedings of the 5th IEEE workshop on Challenges of large applications in distributed environments, CLADE@HPDC 2007, Monterey, California, USA, June 25, 2007",
            r"Proceedings of the 2nd Workshop on the Use of P2P, GRID and Agents for the Development of Content Networks, UPGRADE-CN'07, jointly held with the 16th International Symposium on High-Performance Distributed Computing (HPDC-16 2007), 26 June 2007, Monterey, California, USA."
            r"Proceedings of the 2007 workshop on Grid monitoring, GMW@HPDC 2007, Monterey, California, USA, June 25, 2007",
            r"Proceedings of the 3rd Workshop on the Use of P2P, GRID and Agents for the Development of Content Networks, UPGRADE-CN'08, jointly held with the 17th International Symposium on High-Performance Distributed Computing (HPDC-17 2008), 23 June 2008, Boston, MA, USA",
            r"Proceedings of the 7th International Workshop on Runtime and Operating Systems for Supercomputers, ROSS@HPDC 2017, Washingon, DC, DC, USA, June 27 - 27, 2017.",
            r"Proceedings of the 1st International Workshop on Autonomous Infrastructure for Science, AI-Science@HPDC 2018, Tempe, AZ, USA, June 11, 2018.",
        }
