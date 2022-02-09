from unittest import TestCase
from game import make_keys


class TestMakeKeys(TestCase):
    def test_make_character(self):
        expected = {"Odile Key": False, "Mother Key": False, "Paul Key": False, "Final Boss": False}
        actual = make_keys()
        self.assertEqual(expected, actual)

