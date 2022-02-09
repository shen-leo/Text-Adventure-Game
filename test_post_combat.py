import io
from unittest import TestCase
from unittest.mock import patch
from game import post_combat


class TestPostCombat(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_post_combat_enemy_HP_not_zero(self, mock_stdout):
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
        enemy = {
            "Name": "Monster",
            "HP": 10,
            "EXP Given": 15
        }
        post_combat(character, class_info, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """You are a now Level 2! Your Class Rank is Year 2.
Your HP is 200/200, your Level is 2.
"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_post_combat_enemy_HP_zero_no_level_up(self, mock_stdout):
        character = {
            "Level": 1,
            "EXP": 10,
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
        enemy = {
            "Name": "Monster",
            "HP": 0,
            "EXP Given": 5
        }
        post_combat(character, class_info, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """The enemy writhes in agony and vanishes. You defeated Monster!
You gained 5 EXP, you have 15/20 EXP.

Your HP is 100/100, your Level is 1.
"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_post_combat_enemy_HP_zero_level_up(self, mock_stdout):
        character = {
            "Level": 1,
            "EXP": 10,
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
        enemy = {
            "Name": "Monster",
            "HP": 0,
            "EXP Given": 15
        }
        post_combat(character, class_info, enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """The enemy writhes in agony and vanishes. You defeated Monster!
You gained 15 EXP, you have 25/20 EXP.

You are a now Level 2! Your Class Rank is Year 2.
Your HP is 200/200, your Level is 2.
"""
        self.assertEqual(expected_output, function_printed_this)