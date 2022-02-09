import io
from unittest import TestCase
from unittest.mock import patch
from game import escape_damage


class TestEscapeDamage(TestCase):

    @patch('random.random', side_effect=[0.1])
    def test_escape_damage_hit(self, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "Basic Attack": 5,
            "ATK": 1
        }
        escape_damage(character, enemy)
        expected_character = {
            "Current HP": 195,
            "Max HP": 200
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('random.random', side_effect=[0.7])
    def test_escape_damage_miss(self, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "Basic Attack": 5,
            "ATK": 1
        }
        escape_damage(character, enemy)
        expected_character = {
            "Current HP": 200,
            "Max HP": 200
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('random.random', side_effect=[0.1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_escape_damage_hit_print(self, mock_stdout, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "Basic Attack": 5,
            "ATK": 1
        }
        escape_damage(character, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """The enemy struck you as you ran! You lost 5 HP, your HP is now 195/200.

"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('random.random', side_effect=[0.7])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_escape_damage_miss_print(self, mock_stdout, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "Basic Attack": 5,
            "ATK": 1
        }
        escape_damage(character, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """You got away safely! Your HP is 200/200

"""
        self.assertEqual(expected_output, function_printed_this)

    def test_escape_damage_enemy_unchanged(self):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "Basic Attack": 5,
            "ATK": 1
        }
        escape_damage(character, enemy)
        expected_enemy = {
            "Basic Attack": 5,
            "ATK": 1
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)
