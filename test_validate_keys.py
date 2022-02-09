from unittest import TestCase
from game import validate_keys


class TestValidateKeys(TestCase):
    def test_validate_keys_all_True(self):
        keys_dict = {
            "Odile Key": True,
            "Mother Key": True,
            "Paul Key": True,
        }
        self.assertTrue(validate_keys(keys_dict))

    def test_validate_keys_all_False(self):
        keys_dict = {
            "Odile Key": False,
            "Mother Key": False,
            "Paul Key": False,
        }
        self.assertFalse(validate_keys(keys_dict))

    def test_validate_keys_True_and_False(self):
        keys_dict = {
            "Odile Key": True,
            "Mother Key": False,
            "Paul Key": False,
        }
        self.assertFalse(validate_keys(keys_dict))

    def test_validate_keys_values_unchanged(self):
        keys_dict = {
            "Odile Key": True,
            "Mother Key": True,
            "Paul Key": True,
        }
        expected_keys_dict = {
            "Odile Key": True,
            "Mother Key": True,
            "Paul Key": True,
        }
        validate_keys(keys_dict)
        self.assertEqual(expected_keys_dict, keys_dict)
