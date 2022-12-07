import unittest
from project.celebrities_births_amy import Date

class DateTest(unittest.TestCase):
    
    def setUp(self):
        self.new_date = Date(32, 10, 2021)

    def test_date_valid(self):
        self.assertRaises(ValueError)


t=(1)
