from unittest import TestCase
from game import check_for_boss


class TestCheckForBoss(TestCase):
    def test_check_for_boss_positive(self):
        character = {
            "X-coordinate": 12,
            "Y-coordinate": 12
        }
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        self.assertTrue(check_for_boss(character, special_locations))

    def test_check_for_boss_negative(self):
        character = {
            "X-coordinate": 10,
            "Y-coordinate": 10
        }
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        self.assertFalse(check_for_boss(character, special_locations))

    def test_check_for_boss_arguments_unchanged(self):
        character = {
            "X-coordinate": 10,
            "Y-coordinate": 10
        }
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        expected_character = {
            "X-coordinate": 10,
            "Y-coordinate": 10
        }

        expected_special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        check_for_boss(character, special_locations)
        self.assertEqual(expected_character, character)
        self.assertEqual(expected_special_locations, special_locations)

