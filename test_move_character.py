from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):

    def test_move_character_1_direction(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = "1"
        move_character(character, direction)
        actual_x_coordinate = character["X-coordinate"]
        actual_y_coordinate = character["Y-coordinate"]
        expected_x_coordinate = 1
        expected_y_coordinate = 0
        self.assertEqual(expected_x_coordinate, actual_x_coordinate)
        self.assertEqual(expected_y_coordinate, actual_y_coordinate)

    def test_move_character_2_direction(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = "2"
        move_character(character, direction)
        actual_x_coordinate = character["X-coordinate"]
        actual_y_coordinate = character["Y-coordinate"]
        expected_x_coordinate = 1
        expected_y_coordinate = 2
        self.assertEqual(expected_x_coordinate, actual_x_coordinate)
        self.assertEqual(expected_y_coordinate, actual_y_coordinate)

    def test_move_character_3_direction(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = "3"
        move_character(character, direction)
        actual_x_coordinate = character["X-coordinate"]
        actual_y_coordinate = character["Y-coordinate"]
        expected_x_coordinate = 0
        expected_y_coordinate = 1
        self.assertEqual(expected_x_coordinate, actual_x_coordinate)
        self.assertEqual(expected_y_coordinate, actual_y_coordinate)

    def test_move_character_4_direction(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = "4"
        move_character(character, direction)
        actual_x_coordinate = character["X-coordinate"]
        actual_y_coordinate = character["Y-coordinate"]
        expected_x_coordinate = 2
        expected_y_coordinate = 1
        self.assertEqual(expected_x_coordinate, actual_x_coordinate)
        self.assertEqual(expected_y_coordinate, actual_y_coordinate)

    def test_move_character_1_direction_negative(self):
        # negative coordinates are not applicable to this assignment, but can be possible with this function
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "1"
        move_character(character, direction)
        actual_x_coordinate = character["X-coordinate"]
        actual_y_coordinate = character["Y-coordinate"]
        expected_x_coordinate = 0
        expected_y_coordinate = -1
        self.assertEqual(expected_x_coordinate, actual_x_coordinate)
        self.assertEqual(expected_y_coordinate, actual_y_coordinate)

    def test_move_character_2_direction_negative(self):
        # negative coordinates are not applicable to this assignment, but can be possible with this function
        character = {'X-coordinate': 0, 'Y-coordinate': -2}
        direction = "2"
        move_character(character, direction)
        actual_x_coordinate = character["X-coordinate"]
        actual_y_coordinate = character["Y-coordinate"]
        expected_x_coordinate = 0
        expected_y_coordinate = -1
        self.assertEqual(expected_x_coordinate, actual_x_coordinate)
        self.assertEqual(expected_y_coordinate, actual_y_coordinate)

    def test_move_character_3_direction_negative(self):
        # negative coordinates are not applicable to this assignment, but can be possible with this function
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "3"
        move_character(character, direction)
        actual_x_coordinate = character["X-coordinate"]
        actual_y_coordinate = character["Y-coordinate"]
        expected_x_coordinate = -1
        expected_y_coordinate = 0
        self.assertEqual(expected_x_coordinate, actual_x_coordinate)
        self.assertEqual(expected_y_coordinate, actual_y_coordinate)

    def test_move_character_4_direction_negative(self):
        # negative coordinates are not applicable to this assignment, but can be possible with this function
        character = {'X-coordinate': -2, 'Y-coordinate': 0}
        direction = "4"
        move_character(character, direction)
        actual_x_coordinate = character["X-coordinate"]
        actual_y_coordinate = character["Y-coordinate"]
        expected_x_coordinate = -1
        expected_y_coordinate = 0
        self.assertEqual(expected_x_coordinate, actual_x_coordinate)
        self.assertEqual(expected_y_coordinate, actual_y_coordinate)

    def test_move_character_hp_unchanged(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = "1"
        move_character(character, direction)
        post_move_hp = character['Current HP']
        expected_hp = 5
        self.assertEqual(expected_hp, post_move_hp)
