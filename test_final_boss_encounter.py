import io
from unittest import TestCase
from unittest.mock import patch
from game import final_boss_encounter


class TestFinalBossEncounter(TestCase):

    @patch('random.random', side_effect=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    def test_final_boss_encounter_stats_all_hit(self, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "ATK": 1
        }
        final_boss_encounter(enemy, character)
        expected_character = {
            "Current HP": 182,
            "Max HP": 200
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('random.random', side_effect=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
    def test_final_boss_encounter_stats_all_miss(self, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "ATK": 1
        }
        final_boss_encounter(enemy, character)
        expected_character = {
            "Current HP": 200,
            "Max HP": 200
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('random.random', side_effect=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    def test_final_boss_encounter_stats_all_on_fifty_percent(self, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "ATK": 1
        }
        final_boss_encounter(enemy, character)
        expected_character = {
            "Current HP": 200,
            "Max HP": 200
        }
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    @patch('random.random', side_effect=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_boss_encounter_all_hit_print(self, mock_stdout, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "ATK": 1
        }
        final_boss_encounter(enemy,character)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """The enemy successfully struck you with 1 tentacle(s)
The enemy successfully struck you with 2 tentacle(s)
The enemy successfully struck you with 3 tentacle(s)
The enemy successfully struck you with 4 tentacle(s)
The enemy successfully struck you with 5 tentacle(s)
The enemy successfully struck you with 6 tentacle(s)
The enemy successfully struck you with 7 tentacle(s)
The enemy successfully struck you with 8 tentacle(s)
Your HP is 182/200.

"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('random.random', side_effect=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_boss_encounter_all_miss_print(self, mock_stdout, _):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "ATK": 1
        }
        final_boss_encounter(enemy,character)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """Your HP is 200/200.

"""
        self.assertEqual(expected_output, function_printed_this)

    def test_final_boss_encounter_enemy_unchanged(self):
        character = {
            "Current HP": 200,
            "Max HP": 200
        }
        enemy = {
            "ATK": 1
        }
        final_boss_encounter(enemy, character)
        expected_enemy = {
            "ATK": 1
        }
        actual_enemy = enemy
        self.assertEqual(expected_enemy, actual_enemy)