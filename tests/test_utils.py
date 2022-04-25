import unittest
from datetime import date
from utils.utils import check_status_doc, is_valid_fiscal_code


class TestUtils(unittest.TestCase):
    def test_check_status_doc(self):
        example_dates = {
            'valid': date(2022, 12, 20),
            'expiring': date(2022, 5, 2),
            'expired': date(2022, 4, 1),
            'error': '1234',
            'bool': True
        }

        valid = check_status_doc(example_dates['valid'])
        expiring = check_status_doc(example_dates['expiring'])
        expired = check_status_doc(example_dates['expired'])

        self.assertEqual(valid, 'Valid')
        self.assertEqual(expiring, 'Expiring')
        self.assertEqual(expired, 'Expired')
        self.assertRaises(TypeError, check_status_doc, example_dates['error'])
        self.assertRaises(TypeError, check_status_doc, example_dates['bool'])

    def test_is_valid_fiscal_code(self):
        examples = {
            'valid': 'DBLFNC69P52D994G',
            'invalid': 'BLFNC69P52994',
        }

        self.assertTrue(is_valid_fiscal_code(examples['valid']))
        self.assertFalse(is_valid_fiscal_code(examples['invalid']))
