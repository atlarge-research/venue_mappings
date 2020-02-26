from tests.BaseRunner import BaseRunner


class TestEuroPar(BaseRunner):

    def setUp(self):
        self.expected_venue = "Euro-Par"

        self.correct_strings = {
            "Euro-Par",  # used by DBLP
            "Euro-Par (1)",
            "Euro-Par '95 Parallel Processing, First International Euro-Par Conference, Stockholm, Sweden, August 29-31, 1995, Proceedings",
            "European Conference on Parallel Processing",
            "Euro-Par 2018: Parallel Processing - 24th International Conference on Parallel and Distributed Computing, Turin, Italy, August 27-31, 2018, Proceedings"
        }

        self.wrong_strings = {
            "Euro-Par 2012: Parallel Processing Workshops - BDMC, CGWS, HeteroPar, HiBB, OMHI, Paraphrase, PROPER, Resilience, UCHPC, VHPC, Rhodes Islands, Greece, August 27-31, 2012. Revised Selected Papers",
            "Euro-Par 2016: Parallel Processing Workshops - Euro-Par 2016 International Workshops, Grenoble, France, August 24-26, 2016, Revised Selected Papers",
            "Seventh International Conference on Parallel and Distributed Computing, Applications and Technologies {(PDCAT} 2006), 4-7 December 2006, Taipei, Taiwan",
        }
