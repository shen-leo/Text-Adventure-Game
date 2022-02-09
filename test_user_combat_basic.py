import io
from unittest import TestCase
from unittest.mock import patch
from game import user_combat_basic


class TestUserCombatBasic(TestCase):

    def test_user_combat_basic_positive_damage(self):
        character = {
            "Basic Attack": 5,
            "ATK": 10
        }
        enemy = {
            "HP": 100,
            "Max HP": 100
        }
        user_combat_basic(character, enemy)
        expected_enemy = {
            "HP": 50,
            "Max HP": 100
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)

    def test_user_combat_basic_zero_damage(self):
        character = {
            "Basic Attack": 0,
            "ATK": 10
        }
        enemy = {
            "HP": 100,
            "Max HP": 100
        }
        user_combat_basic(character, enemy)
        expected_enemy = {
            "HP": 100,
            "Max HP": 100
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_basic_positive_damage_print(self, mock_stdout):
        character = {
            "Basic Attack": 5,
            "ATK": 10
        }
        enemy = {
            "HP": 100,
            "Max HP": 100
        }
        user_combat_basic(character, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """You used Basic Attack, dealing 50 damage.
Enemy HP: 50/100

"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_basic_zero_damage_print(self, mock_stdout):
        character = {
            "Basic Attack": 0,
            "ATK": 10
        }
        enemy = {
            "HP": 100,
            "Max HP": 100
        }
        user_combat_basic(character, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """You used Basic Attack, dealing 0 damage.
Enemy HP: 100/100

"""
        self.assertEqual(expected_output, function_printed_this)

    def test_user_combat_basic_character_unchanged(self):
        character = {
            "Basic Attack": 10,
            "ATK": 10
        }
        enemy = {
            "HP": 100,
            "Max HP": 100
        }
        user_combat_basic(character, enemy)
        expected_character = {
            "Basic Attack": 10,
            "ATK": 10
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)
