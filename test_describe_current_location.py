import io
from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location


class TestDescribeCurrentLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_one_by_one_room(self, mock_stdout):
        board = {(0, 0): 'Shrouded Street'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        describe_current_location(board, character)
        function_printed_this = mock_stdout.getvalue()
        expected_output = 'Your coordinates are (0, 0), your location is: Shrouded Street.\n\n'
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_two_by_two_room(self, mock_stdout):
        board = {(0, 0): 'The Clinic', (0, 1): 'Creepy Crosswalk', (1, 0): 'Malicious Mall', (1, 1): 'Busy Bus Stop'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        describe_current_location(board, character)
        function_printed_this = mock_stdout.getvalue()
        expected_output = 'Your coordinates are (1, 1), your location is: Busy Bus Stop.\n\n'
        self.assertEqual(expected_output, function_printed_this)

    def test_describe_current_location_arguments_unchanged(self):
        board = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        expected_board = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        describe_current_location(board, character)
        self.assertEqual(expected_board, board)
        self.assertEqual(expected_character, character)

    def test_describe_current_location_hp_unchanged(self):
        board = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        describe_current_location(board, character)
        post_move_hp = character['Current HP']
        expected_hp = 5
        self.assertEqual(expected_hp, post_move_hp)