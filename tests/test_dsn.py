from tests.BaseRunner import BaseRunner


class TestDSN(BaseRunner):

    def setUp(self):
        self.expected_venue = "DSN"

        self.correct_strings = {
            r"DSN",  # used by DBLP
            r"2000 International Conference on Dependable Systems and Networks {(DSN} 2000) (formerly {FTCS-30} and DCCA-8), 25-28 June 2000, New York, NY, {USA}",
            r"Proceeding International Conference on Dependable Systems and Networks. DSN 2000",
            r"49th Annual {IEEE/IFIP} International Conference on Dependable Systems and Networks, {DSN} (Industry Track) 2019, Portland, OR, USA, June 24-27, 2019",
            r"2006 International Conference on Dependable Systems and Networks {(DSN} 2006), 25-28 June 2006, Philadelphia, Pennsylvania, USA, Proceedings",
        }

        self.wrong_strings = {
            r"DSN Workshops",
            r"49th Annual {IEEE/IFIP} International Conference on Dependable Systems and Networks Workshops, {DSN} Workshops 2019, Portland, OR, USA, June 24-27, 2019",
            r""
        }
