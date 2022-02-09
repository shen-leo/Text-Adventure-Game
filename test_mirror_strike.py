import io
from unittest import TestCase
from unittest.mock import patch
from game import mirror_strike


class TestMirrorStrike(TestCase):

    def test_mirror_strike_damage_dealt(self):
        character = {
            "ATK": 10,
            "Current HP": 100,
            "Level": 2}
        class_info = {
            "Special Attack": 5
        }
        actual = mirror_strike(character, class_info)
        expected = 50
        self.assertEqual(expected, actual)

    def test_mirror_strike_damage_dealt_to_self(self):
        character = {
            "ATK": 10,
            "Current HP": 100,
            "Level": 2
        }
        class_info = {
            "Special Attack": 5
        }
        mirror_strike(character, class_info)
        expected_character = {
            "ATK": 10,
            "Current HP": 90,
            "Level": 2
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    def test_mirror_strike_zero_damage_dealt(self):
        character = {
            "ATK": 0,
            "Current HP": 100,
            "Level": 2}
        class_info = {
            "Special Attack": 5
        }
        actual = mirror_strike(character, class_info)
        expected = 0
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mirror_strike_damage_to_self_print_statement(self, mock_stdout):
        character = {
            "ATK": 10,
            "Current HP": 100,
            "Level": 2
        }
        class_info = {
            "Special Attack": 5
        }
        mirror_strike(character, class_info)
        function_printed_this = mock_stdout.getvalue()
        expected_output = "You cut yourself with the mirror's edge, inflicting 10 damage to yourself.\n"
        self.assertEqual(expected_output, function_printed_this)

    def test_mirror_strike_class_info_unchanged(self):
        character = {
            "ATK": 5,
            "Current HP": 100,
            "Level": 2}
        class_info = {
            "Special Attack": 5
        }
        mirror_strike(character, class_info)
        expected_class_info = {
            "Special Attack": 5
        }
        actual_class_info = class_info
        self.assertEqual(expected_class_info, actual_class_info)
