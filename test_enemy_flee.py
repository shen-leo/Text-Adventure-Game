import io
from unittest import TestCase
from unittest.mock import patch
from game import enemy_flee


class TestEnemyFlee(TestCase):

    @patch('random.random', side_effect=[0.1])
    def test_enemy_flee_success_not_boss(self, _):
        enemy = {
            "Rank": 1
        }
        self.assertTrue(enemy_flee(enemy))

    @patch('random.random', side_effect=[0.7])
    def test_enemy_flee_fail_not_boss(self, _):
        enemy = {
            "Rank": 1
        }
        self.assertFalse(enemy_flee(enemy))

    @patch('random.random', side_effect=[0.1])
    def test_enemy_flee_success_is_boss(self, _):
        enemy = {
            "Rank": "Boss"
        }
        self.assertFalse(enemy_flee(enemy))

    @patch('random.random', side_effect=[0.7])
    def test_enemy_flee_fail_is_boss(self, _):
        enemy = {
            "Rank": "Boss"
        }
        self.assertFalse(enemy_flee(enemy))

    @patch('random.random', side_effect=[0.1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flee_success_print(self, mock_stdout, _):
        enemy = {
            "Rank": 1
        }
        enemy_flee(enemy)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """The enemy fled!
"""
        self.assertEqual(expected_output, function_printed_this)

    def test_enemy_flee_enemy_unchanged(self):
        enemy = {
            "Rank": 1
        }
        enemy_flee(enemy)
        expected_enemy = {
            "Rank": 1
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)
