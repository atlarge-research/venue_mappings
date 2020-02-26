from tests.BaseRunner import BaseRunner


class TestISC(BaseRunner):

    def setUp(self):
        self.expected_venue = "ISC"

        self.correct_strings = {
            "ISC",  # used by DBLP
            "Supercomputer'89: Anwendungen, Architekturen, Trends, Seminar, Mannheim, 8.-10. Juni 1989, Proceedings",
            "Supercomputing - 28th International Supercomputing Conference, {ISC} 2013, Leipzig, Germany, June 16-20, 2013. Proceedings}",
            "International Supercomputing Conference",
            "Supercomputer'89",
            "High Performance Computing - 33rd International Conference, {ISC} High Performance 2018, Frankfurt, Germany, June 24-28, 2018, Proceedings",
        }

        self.wrong_strings = {
            "High Performance Computing - {ISC} High Performance 2017 International Workshops, DRBSD, ExaComm, HCPM, HPC-IODC, IWOPH, IXPUG, P{\^{}}3MA, VHPC, Visualization at Scale, WOPSSS, Frankfurt, Germany, June 18-22, 2017, Revised Selected Papers",
        }
