from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expected = {"Name": "Temp_Name", "Level": 1, "EXP": 0, "EXP Breakpoint": "Temp_Num", "Class": "Temp_Class",
                    "Class Level": "Temp_Class_Level", "Basic Attack": 3, "Max HP": 100, "Current HP": 100, "ATK": 10,
                    "Infamy": 1.0, "X-coordinate": 0, "Y-coordinate": 0,
    }
        actual = make_character()
        self.assertEqual(expected, actual)
