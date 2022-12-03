import unittest
from project.celebrities_births import Date

class DateTestCase(unittest.TestCase):
    def setUp(self):
        self.date = Date(12, 4, 1995)
        
    def test_str_(self):
        expected_string = '12-4-1995'
        actual_string = self.date.__str__()
        self.assertEqual(expected_string, actual_string)

    # def test_is_date_valid(self):
    #     actual_date_bool = self.date.is_date_valid()
    #     self.assertTrue(actual_date_bool)

    def test_to_wiki_format(self):
        expected_date = 'April_12'
        actual_date = self.date.to_wiki_format()
        self.assertEqual(expected_date, actual_date)

unittest.main(argv=[''], verbosity=2, exit=False)