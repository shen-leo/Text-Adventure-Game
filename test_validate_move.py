from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):

    def test_validate_move_one_by_one(self):
        board = {(0, 0): 'Empty Room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "2"
        output = validate_move(board, character, direction)
        self.assertFalse(output)

    def test_validate_move_in_board(self):
        board = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "2"
        output = validate_move(board, character, direction)
        self.assertTrue(output)

    def test_validate_move_not_in_board(self):
        board = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "4"
        output = validate_move(board, character, direction)
        self.assertFalse(output)

    def test_validate_move_in_board_negative_x_coordinates(self):
        # negative coordinates are not applicable to this assignment, but can be possible with this function
        board = {(-1, 0): 'Room One', (-1, 1): 'Room Two', (0, 0): 'Room Three', (0, 1): 'Room Four'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "3"
        output = validate_move(board, character, direction)
        self.assertTrue(output)

    def test_validate_move_not_in_board_negative_x_coordinates(self):
        # negative coordinates are not applicable to this assignment, but can be possible with this function
        board = {(-1, 0): 'Room One', (-1, 1): 'Room Two', (0, 0): 'Room Three', (0, 1): 'Room Four'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "1"
        output = validate_move(board, character, direction)
        self.assertFalse(output)

    def test_validate_move_in_board_negative_y_coordinates(self):
        # negative coordinates are not applicable to this assignment, but can be possible with this function
        board = {(0, -1): 'Room One', (1, -1): 'Room Two', (0, 0): 'Room Three', (1, 0): 'Room Four'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "1"
        output = validate_move(board, character, direction)
        self.assertTrue(output)

    def test_validate_move_not_in_board_negative_y_coordinates(self):
        # negative coordinates are not applicable to this assignment, but can be possible with this function
        board = {(0, -1): 'Room One', (1, -1): 'Room Two', (0, 0): 'Room Three', (1, 0): 'Room Four'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "3"
        output = validate_move(board, character, direction)
        self.assertFalse(output)

    def test_validate_move_arguments_unchanged(self):
        board = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "2"
        expected_board = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        expected_direction = "2"
        validate_move(board, character, direction)
        self.assertEqual(expected_board, board)
        self.assertEqual(expected_character, character)
        self.assertEqual(expected_direction, direction)

    def test_validate_move_hp_unchanged(self):
        board = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        direction = "1"
        validate_move(board, character, direction)
        post_move_hp = character['Current HP']
        expected_hp = 5
        self.assertEqual(expected_hp, post_move_hp)
