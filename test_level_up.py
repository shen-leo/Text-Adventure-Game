import io
from unittest import TestCase
from unittest.mock import patch
from game import level_up


class TestLevelUp(TestCase):

    def test_level_up_at_level_2_breakpoint_stats(self):
        character = {
            "Level": 1,
            "EXP": 20,
            "EXP Breakpoint": 20,
            "ATK": 10,
            "Current HP": 100,
            "Max HP": 100,
            "Class Level": "Year 1"
        }
        class_info = {
            "EXP Level 2": 20,
            "ATK Level 2": 20,
            "HP Level 2": 200,
            "Level Two": "Year 2",
            "EXP Level 3": 30,
            "ATK Level 3": 30,
            "HP Level 3": 300,
            "Level Three": "Year 3"
        }
        expected_stats = {
            "Level": 2,
            "EXP": 20,
            "EXP Breakpoint": 30,
            "ATK": 20,
            "Current HP": 200,
            "Max HP": 200,
            "Class Level": "Year 2"
        }
        level_up(character, class_info)
        actual_stats = character
        self.assertEqual(expected_stats, actual_stats)

    def test_level_up_at_level_3_breakpoint_stats(self):
        character = {
            "Level": 2,
            "EXP": 30,
            "EXP Breakpoint": 30,
            "ATK": 20,
            "Current HP": 200,
            "Max HP": 200,
            "Class Level": "Year 2"
        }
        class_info = {
            "EXP Level 2": 20,
            "ATK Level 2": 20,
            "HP Level 2": 200,
            "Level Two": "Year 2",
            "EXP Level 3": 30,
            "ATK Level 3": 30,
            "HP Level 3": 300,
            "Level Three": "Year 3"
        }
        expected_stats = {
            "Level": 3,
            "EXP": 30,
            "EXP Breakpoint": 30,
            "ATK": 30,
            "Current HP": 300,
            "Max HP": 300,
            "Class Level": "Year 3"
        }
        level_up(character, class_info)
        actual_stats = character
        self.assertEqual(expected_stats, actual_stats)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_at_level_2_breakpoint_print(self, mock_stdout):
        character = {
            "Level": 1,
            "EXP": 20,
            "EXP Breakpoint": 20,
            "ATK": 10,
            "Current HP": 100,
            "Max HP": 100,
            "Class Level": "Year 1"
        }
        class_info = {
            "EXP Level 2": 20,
            "ATK Level 2": 20,
            "HP Level 2": 200,
            "Level Two": "Year 2",
            "EXP Level 3": 30,
            "ATK Level 3": 30,
            "HP Level 3": 300,
            "Level Three": "Year 3"
        }
        expected_output = "You are a now Level 2! Your Class Rank is Year 2.\n"
        level_up(character, class_info)
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_past_level_2_breakpoint_print(self, mock_stdout):
        character = {
            "Level": 1,
            "EXP": 25,
            "EXP Breakpoint": 20,
            "ATK": 10,
            "Current HP": 100,
            "Max HP": 100,
            "Class Level": "Year 1"
        }
        class_info = {
            "EXP Level 2": 20,
            "ATK Level 2": 20,
            "HP Level 2": 200,
            "Level Two": "Year 2",
            "EXP Level 3": 30,
            "ATK Level 3": 30,
            "HP Level 3": 300,
            "Level Three": "Year 3"
        }
        expected_output = "You are a now Level 2! Your Class Rank is Year 2.\n"
        level_up(character, class_info)
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_at_level_3_breakpoint_print(self, mock_stdout):
        character = {
            "Level": 2,
            "EXP": 30,
            "EXP Breakpoint": 30,
            "ATK": 20,
            "Current HP": 200,
            "Max HP": 200,
            "Class Level": "Year 2"
        }
        class_info = {
            "EXP Level 2": 20,
            "ATK Level 2": 20,
            "HP Level 2": 200,
            "Level Two": "Year 2",
            "EXP Level 3": 30,
            "ATK Level 3": 30,
            "HP Level 3": 300,
            "Level Three": "Year 3"
        }
        expected_output = "You are a now Level 3! Your Class Rank is Year 3.\n"
        level_up(character, class_info)
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_past_level_3_breakpoint_print(self, mock_stdout):
        character = {
            "Level": 2,
            "EXP": 35,
            "EXP Breakpoint": 30,
            "ATK": 20,
            "Current HP": 200,
            "Max HP": 200,
            "Class Level": "Year 2"
        }
        class_info = {
            "EXP Level 2": 20,
            "ATK Level 2": 20,
            "HP Level 2": 200,
            "Level Two": "Year 2",
            "EXP Level 3": 30,
            "ATK Level 3": 30,
            "HP Level 3": 300,
            "Level Three": "Year 3"
        }
        expected_output = "You are a now Level 3! Your Class Rank is Year 3.\n"
        level_up(character, class_info)
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    def test_level_up_class_info_unchanged(self):
        character = {
            "Level": 2,
            "EXP": 35,
            "EXP Breakpoint": 30,
            "ATK": 20,
            "Current HP": 200,
            "Max HP": 200,
            "Class Level": "Year 2"
        }
        class_info = {
            "EXP Level 2": 20,
            "ATK Level 2": 20,
            "HP Level 2": 200,
            "Level Two": "Year 2",
            "EXP Level 3": 30,
            "ATK Level 3": 30,
            "HP Level 3": 300,
            "Level Three": "Year 3"
        }
        expected_class_info = {
            "EXP Level 2": 20,
            "ATK Level 2": 20,
            "HP Level 2": 200,
            "Level Two": "Year 2",
            "EXP Level 3": 30,
            "ATK Level 3": 30,
            "HP Level 3": 300,
            "Level Three": "Year 3"
        }
        level_up(character, class_info)
        actual_class_info = class_info
        self.assertEqual(expected_class_info, actual_class_info)