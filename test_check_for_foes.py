from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes


class TestCheckForFoes(TestCase):

    @patch('random.random', return_value=0.1)
    def test_check_for_foes_true(self, _):
        self.assertTrue(check_for_foes())

    @patch('random.random', return_value=0.8)
    def test_check_for_foes_false(self, _):
        self.assertFalse(check_for_foes())

    @patch('random.random', return_value=0.2)
    def test_check_for_foes_exactly_zero_point_two(self, _):
        self.assertFalse(check_for_foes())