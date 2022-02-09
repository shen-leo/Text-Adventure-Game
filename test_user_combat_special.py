import io
from unittest import TestCase
from unittest.mock import patch
from game import user_combat_special


class TestUserCombatSpecial(TestCase):
    def test_user_combat_special_motel_manager(self):
        character = {"ATK": 10}
        class_info = {
            "Class Name": "Motel Manager",
            "Special Attack": 5,
            "Special Attack Name": "Motel Punch"
        }
        enemy = {"HP": 100, "Max HP": 100}
        user_combat_special(character, class_info, enemy)
        expected_enemy = {
            "HP": 50,
            "Max HP": 100
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)

    def test_user_combat_special_investment_banker(self):
        character = {"ATK": 10}
        class_info = {
            "Class Name": "Investment Banker",
            "Special Attack": 5,
            "Special Attack Name": "Investment Punch"
        }
        enemy = {"HP": 100, "Max HP": 100}
        user_combat_special(character, class_info, enemy)
        expected_enemy = {
            "HP": 50,
            "Max HP": 100
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)

    @patch('game.arcane_missiles', return_value=10)
    def test_user_combat_special_arcane_mage(self, _):
        character = {"ATK": 10}
        class_info = {
            "Class Name": "Arcane Mage",
            "Special Attack": 5,
            "Special Attack Name": "Arcane Missiles"
        }
        enemy = {"HP": 100, "Max HP": 100}
        user_combat_special(character, class_info, enemy)
        expected_enemy = {
            "HP": 90,
            "Max HP": 100
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)

    @patch('game.mirror_strike', return_value=10)
    def test_user_combat_special_ballet_dancer(self, _):
        character = {"ATK": 10, "Current HP": 100, "Level": 1}
        class_info = {
            "Class Name": "Ballet Dancer",
            "Special Attack": 5,
            "Special Attack Name": "Mirror Strike"
        }
        enemy = {"HP": 100, "Max HP": 100}
        user_combat_special(character, class_info, enemy)
        expected_enemy = {
            "HP": 90,
            "Max HP": 100
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_special_motel_manager_print(self, mock_stdout):
        character = {"ATK": 10}
        class_info = {
            "Class Name": "Motel Manager",
            "Special Attack": 5,
            "Special Attack Name": "Motel Punch"
        }
        enemy = {"HP": 100, "Max HP": 100}
        user_combat_special(character, class_info, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """You used Motel Punch, dealing 50 damage.
Enemy HP: 50/100

"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_special_investment_banker_print(self, mock_stdout):
        character = {"ATK": 10}
        class_info = {
            "Class Name": "Investment Banker",
            "Special Attack": 5,
            "Special Attack Name": "Investment Punch"
        }
        enemy = {"HP": 100, "Max HP": 100}
        user_combat_special(character, class_info, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """You used Investment Punch, dealing 50 damage.
Enemy HP: 50/100

"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.arcane_missiles', return_value=10)
    def test_user_combat_special_arcane_mage_print(self, _, mock_stdout):
        character = {"ATK": 10}
        class_info = {
            "Class Name": "Arcane Mage",
            "Special Attack": 5,
            "Special Attack Name": "Arcane Missiles"
        }
        enemy = {"HP": 100, "Max HP": 100}
        user_combat_special(character, class_info, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """You used Arcane Missiles, dealing 10 damage.
Enemy HP: 90/100

"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.mirror_strike', return_value=10)
    def test_user_combat_special_arcane_mage_print(self, _, mock_stdout):
        character = {"ATK": 10}
        class_info = {
            "Class Name": "Ballet Dancer",
            "Special Attack": 5,
            "Special Attack Name": "Mirror Strike"
        }
        enemy = {"HP": 100, "Max HP": 100}
        user_combat_special(character, class_info, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """You used Mirror Strike, dealing 10 damage.
Enemy HP: 90/100

"""
        self.assertEqual(expected_output, function_printed_this)