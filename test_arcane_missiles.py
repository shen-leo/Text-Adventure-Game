from unittest import TestCase
from unittest.mock import patch
from game import arcane_missiles


class TestArcaneMissiles(TestCase):

    @patch('random.random', side_effect=[0.1, 0.1, 0.1, 0.1, 0.1])
    def test_arcane_missiles_all_hit(self, _):
        character = {"ATK": 1}
        actual = arcane_missiles(character)
        expected = 15
        self.assertEqual(expected, actual)

    @patch('random.random', side_effect=[0.6, 0.6, 0.6, 0.6, 0.6])
    def test_arcane_missiles_all_miss(self, _):
        character = {"ATK": 1}
        actual = arcane_missiles(character)
        expected = 0
        self.assertEqual(expected, actual)

    @patch('random.random', side_effect=[0.5, 0.5, 0.5, 0.5, 0.5])
    def test_arcane_missiles_prob_equal_to_50(self, _):
        character = {"ATK": 1}
        actual = arcane_missiles(character)
        expected = 0
        self.assertEqual(expected, actual)

    def test_arcane_missiles_character_unchanged(self):
        character = {"ATK": 2}
        arcane_missiles(character)
        expected_character = {"ATK": 2}
        actual_character = character
        self.assertEqual(expected_character, actual_character)
