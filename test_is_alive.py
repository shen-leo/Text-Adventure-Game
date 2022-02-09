from unittest import TestCase
from game import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_hp_above_zero(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertTrue(is_alive(character))

    def test_is_alive_hp_is_zero(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 0}
        self.assertFalse(is_alive(character))

    def test_is_alive_negative_hp(self):
        # negative HP values are not applicable to this assignment, but can be possible with this function
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': -5}
        self.assertFalse(is_alive(character))

    def test_is_alive_coordinates_unchanged(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        is_alive(character)
        post_function_x_coordinate = character['X-coordinate']
        post_function_y_coordinate = character['Y-coordinate']
        expected_x_coordinate = 1
        expected_y_coordinate = 1
        self.assertEqual(expected_x_coordinate, post_function_x_coordinate)
        self.assertEqual(expected_y_coordinate, post_function_y_coordinate)

    def test_is_alive_hp_unchanged(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        is_alive(character)
        post_function_hp = character['Current HP']
        expected_hp = 5
        self.assertEqual(expected_hp, post_function_hp)
