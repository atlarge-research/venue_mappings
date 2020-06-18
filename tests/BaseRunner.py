import unittest

from venue_mapper.venue_mapper import VenueMapper


class BaseRunner(unittest.TestCase):
    expected_venue = ""
    correct_strings = {}
    wrong_strings = {}

    def runTest(self):
        venue_mapper = VenueMapper()
        for string in self.correct_strings:
            self.assertEqual(self.expected_venue, venue_mapper.get_abbreviation(string), "{0} failed.".format(string))

        for string in self.wrong_strings:
            self.assertNotEqual(self.expected_venue, venue_mapper.get_abbreviation(string),
                                "Didn't expect {0} for string {1}".format(venue_mapper.get_abbreviation(string), string))
