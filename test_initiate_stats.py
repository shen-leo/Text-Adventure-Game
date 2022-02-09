from unittest import TestCase
from game import initiate_stats


class TestInitiateStats(TestCase):
    def test_initiate_stats(self):
        character = {
            "Name": "Leo",
            "EXP Breakpoint": "Temp_Num",
            "Class Level": "Temp_Class_Level",
            "ATK": 10,
        }
        class_info = {
            "Class Name": "Investment Banker",
            "Level One": "Analyst",
            "EXP Level 2": 150,
            "ATK Level 1": 10,
        }
        expected_character = {
            "Name": "Leo",
            "EXP Breakpoint": 150,
            "Class Level": "Analyst",
            "ATK": 10,
        }
        initiate_stats(character, class_info)
        actual_character = character
        self.assertEqual(expected_character, actual_character)

    def test_initiate_stats_class_info_argument_unchanged(self):
        character = {
            "Name": "Leo",
            "EXP Breakpoint": "Temp_Num",
            "Class Level": "Temp_Class_Level",
            "ATK": 10,
        }
        class_info = {
            "Class Name": "Investment Banker",
            "Level One": "Analyst",
            "EXP Level 2": 150,
            "ATK Level 1": 10,
        }
        initiate_stats(character, class_info)
        expected_class_info = {
            "Class Name": "Investment Banker",
            "Level One": "Analyst",
            "EXP Level 2": 150,
            "ATK Level 1": 10,
        }
        actual_class_info = class_info
        self.assertEqual(expected_class_info, actual_class_info)