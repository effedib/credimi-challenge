import unittest
import datetime as d
from datetime import datetime
from db.fake_data import create_fake_data


class TestCreateFakeData(unittest.TestCase):
    def test_create_fake_data(self):
        result = create_fake_data(2)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result[0][0]), 16)
        self.assertIs(type(result[0][1]), int)
        self.assertEqual(len(result[0][2]), 2)
        self.assertIs(type(datetime.strptime(result[0][3], '%Y-%m-%d')), datetime)
        self.assertIsInstance(result[0][4], d.date)
