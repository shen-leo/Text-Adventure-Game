import io
from unittest import TestCase
from unittest.mock import patch
from game import hp_regen


class TestHpRegen(TestCase):

    def test_hp_regen_not_full(self):
        character = {
            "Current HP": 90,
            "Max HP": 100
        }
        hp_regen(character)
        expected_character = {
            "Current HP": 91,
            "Max HP": 100
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    def test_hp_regen_full(self):
        character = {
            "Current HP": 100,
            "Max HP": 100
        }
        hp_regen(character)
        expected_character = {
            "Current HP": 100,
            "Max HP": 100
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hp_regen_not_full_print_statement(self, mock_stdout):
        character = {
            "Current HP": 90,
            "Max HP": 100
        }
        hp_regen(character)
        expected_output = """You regenerated 1 HP.
Your HP is now 91/100.

"""
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hp_regen_full_print_statement(self, mock_stdout):
        character = {
            "Current HP": 100,
            "Max HP": 100
        }
        hp_regen(character)
        expected_output = ""
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)