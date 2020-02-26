from tests.BaseRunner import BaseRunner


class TestP2P(BaseRunner):

    def setUp(self):
        self.expected_venue = "P2P"

        self.correct_strings = {
            "P2P",
            "1st International Conference on Peer-to-Peer Computing {(P2P} 2001), 27-29 August 2001, Link{\"{o}}ping, Sweden",
            "2015 {IEEE} International Conference on Peer-to-Peer Computing, {P2P} 2015, Boston, MA, USA, September 21-25, 2015",
            "Peer-to-Peer Computing (P2P), 2011 IEEE International Conference on",
            "{IEEE} Tenth International Conference on Peer-to-Peer Computing, {P2P} 2010, Delft, The Netherlands, 25-27 August 2010",
            "Peer-to-Peer Computing",  # DBLP
        }

        self.wrong_strings = {
        }
