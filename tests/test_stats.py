import unittest

from  apirestful.api.SimpleStats import SimpleStats

NORMAL_DATA = "/home/malle/proj/py/mxresto/data/normal/"
csvRatings = NORMAL_DATA+"rating_final.csv"
csvPlaces  = NORMAL_DATA+"geoplaces2.csv"
stat = SimpleStats(csvRatings,csvPlaces)

class TestStatsClasses(unittest.TestCase):

    def test_simple_stats(self):
        self.assertGreater(stat.get_places_count(),50)
