import unittest
from city_functions import get_city_country

class LocationsTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country(self):
        """Test if locations like 'Seoul, Korea' work."""
        formatted_location = get_city_country('seoul', 'korea')
        self.assertEqual(formatted_location, 'Seoul, Korea')

    def test_city_country_population(self):
        """Does 'Seoul, Korea - Population 9_967_677' work?"""
        formatted_location = get_city_country('seoul', 'korea', 9_967_677)
        self.assertEqual(
            formatted_location, 'Seoul, Korea - Population 9967677')

if __name__ == '__main__':
    unittest.main()