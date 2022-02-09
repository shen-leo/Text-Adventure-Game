import io
from unittest import TestCase
from unittest.mock import patch
from game import enemy_combat_turn


class TestEnemyCombatTurn(TestCase):

    @patch('random.random', side_effect=[0.1])
    def test_enemy_combat_turn_special_attack(self, _):
        character = {
            "Current HP": 100,
            "Max HP": 100
        }
        enemy = {
            "Special Attack": 5,
            "ATK": 5,
            "Special Attack Name": "Special Attack!",
            "Name": "Monster",
            "Basic Attack": 2,
            "Basic Attack Name": "Basic Attack!",
            "Special Attack Quote": "Here's my special attack!",
            "Basic Attack Quote": "Here's my normal attack!"
        }
        enemy_combat_turn(character, enemy)
        expected_character = {
            "Current HP": 75,
            "Max HP": 100
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('random.random', side_effect=[0.7])
    def test_enemy_combat_turn_basic_attack(self, _):
        character = {
            "Current HP": 100,
            "Max HP": 100
        }
        enemy = {
            "Special Attack": 5,
            "ATK": 5,
            "Special Attack Name": "Special Attack!",
            "Name": "Monster",
            "Basic Attack": 2,
            "Basic Attack Name": "Basic Attack!",
            "Special Attack Quote": "Here's my special attack!",
            "Basic Attack Quote": "Here's my normal attack!"
        }
        enemy_combat_turn(character, enemy)
        expected_character = {
            "Current HP": 90,
            "Max HP": 100
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('random.random', side_effect=[0.5])
    def test_enemy_combat_turn_randomizer_on_fifty(self, _):
        character = {
            "Current HP": 100,
            "Max HP": 100
        }
        enemy = {
            "Special Attack": 5,
            "ATK": 5,
            "Special Attack Name": "Special Attack!",
            "Name": "Monster",
            "Basic Attack": 2,
            "Basic Attack Name": "Basic Attack!",
            "Special Attack Quote": "Here's my special attack!",
            "Basic Attack Quote": "Here's my normal attack!"
        }
        enemy_combat_turn(character, enemy)
        expected_character = {
            "Current HP": 90,
            "Max HP": 100
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('random.random', side_effect=[0.1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_combat_turn_special_attack_print(self, mock_stdout, _):
        character = {
            "Current HP": 100,
            "Max HP": 100
        }
        enemy = {
            "Special Attack": 5,
            "ATK": 5,
            "Special Attack Name": "Special Attack!",
            "Name": "Monster",
            "Basic Attack": 2,
            "Basic Attack Name": "Basic Attack!",
            "Special Attack Quote": "Here's my special attack!",
            "Basic Attack Quote": "Here's my normal attack!"
        }
        enemy_combat_turn(character, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """Here's my special attack!
Monster attacked you with Special Attack!! You took 25 damage, your HP is now 75/100.

"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('random.random', side_effect=[0.7])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_combat_turn_basic_attack_print(self, mock_stdout, _):
        character = {
            "Current HP": 100,
            "Max HP": 100
        }
        enemy = {
            "Special Attack": 5,
            "ATK": 5,
            "Special Attack Name": "Special Attack!",
            "Name": "Monster",
            "Basic Attack": 2,
            "Basic Attack Name": "Basic Attack!",
            "Special Attack Quote": "Here's my special attack!",
            "Basic Attack Quote": "Here's my normal attack!"
        }
        enemy_combat_turn(character, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """Here's my normal attack!
Monster attacked you with a Basic Attack! You took 10 damage, your HP is now 90/100.

"""
        self.assertEqual(expected_output, function_printed_this)

    def test_enemy_combat_turn_enemy_unchanged(self):
        character = {
            "Current HP": 100,
            "Max HP": 100
        }
        enemy = {
            "Special Attack": 5,
            "ATK": 5,
            "Special Attack Name": "Special Attack!",
            "Name": "Monster",
            "Basic Attack": 2,
            "Basic Attack Name": "Basic Attack!",
            "Special Attack Quote": "Here's my special attack!",
            "Basic Attack Quote": "Here's my normal attack!"
        }
        enemy_combat_turn(character, enemy)
        expected_enemy = {
            "Special Attack": 5,
            "ATK": 5,
            "Special Attack Name": "Special Attack!",
            "Name": "Monster",
            "Basic Attack": 2,
            "Basic Attack Name": "Basic Attack!",
            "Special Attack Quote": "Here's my special attack!",
            "Basic Attack Quote": "Here's my normal attack!"
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)