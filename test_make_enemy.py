from unittest import TestCase
from unittest.mock import patch
from game import make_enemy


class TestMakeEnemy(TestCase):
    enemy1 = {
        "Name": "Anxious Apparition",
        "Rank": "1",
        "HP": 100,
        "Max HP": 100,
        "Level": 1,
        "ATK": 1,
        "Basic Attack": 2,
        "Special Attack": 3,
        "Special Attack Name": "Deathly Wail",
        "EXP Given": 25,
        "Encounter Quote": "Anxious Apparition: Stop... your soul is mine...",
        "Basic Attack Quote": "Anxious Apparition: Begone...",
        "Special Attack Quote": "Anxious Apparition: DON'T LEAVE ME ALONE",
        "Victory Quote": "Anxious Apparition: Finally, it's over...",
        "Death Quote": "Anxious Apparition: NO PLEASE DON'T KILL ME!"
    }

    enemy2 = {
        "Name": "Sneaky Shadow",
        "Rank": "1",
        "HP": 100,
        "Max HP": 100,
        "Level": 1,
        "ATK": 1,
        "Basic Attack": 1,
        "Special Attack": 4,
        "Special Attack Name": "Sinister Strike",
        "EXP Given": 25,
        "Encounter Quote": "Sneaky Shadow: Empty your wallets!",
        "Basic Attack Quote": "Sneaky Shadow: Take this!",
        "Special Attack Quote": "Sneaky Shadow: I'll decorate your back... with steel.",
        "Victory Quote": "Sneaky Shadow: Gold... for a pound of flesh.",
        "Death Quote": "Sneaky Shadow: NO LET ME GO, PLEASE!"
    }

    enemy3 = {
        "Name": "Puzzled Phantom",
        "Rank": "1",
        "HP": 100,
        "Max HP": 100,
        "Level": 1,
        "ATK": 1,
        "Basic Attack": 2,
        "Special Attack": 2,
        "Special Attack Name": "Spectral Rend",
        "EXP Given": 25,
        "Encounter Quote": "Puzzled Phantom: Who are you? Who am I?",
        "Basic Attack Quote": "Puzzled Phantom: Answer me...",
        "Special Attack Quote": "Puzzled Phantom: LEAVE ME ALONE",
        "Victory Quote": "Puzzled Phantom: This answers nothing...",
        "Death Quote": "Puzzled Phantom: WHAT HAVE YOU DONE?"
    }

    @patch('random.choice', side_effect=[enemy1])
    def test_make_enemy_enemy1(self, _):
        character = {"Level": 1}
        actual = make_enemy(character)
        expected = {
            "Name": "Anxious Apparition",
            "Rank": "1",
            "HP": 100,
            "Max HP": 100,
            "Level": 1,
            "ATK": 1,
            "Basic Attack": 2,
            "Special Attack": 3,
            "Special Attack Name": "Deathly Wail",
            "EXP Given": 25,
            "Encounter Quote": "Anxious Apparition: Stop... your soul is mine...",
            "Basic Attack Quote": "Anxious Apparition: Begone...",
            "Special Attack Quote": "Anxious Apparition: DON'T LEAVE ME ALONE",
            "Victory Quote": "Anxious Apparition: Finally, it's over...",
            "Death Quote": "Anxious Apparition: NO PLEASE DON'T KILL ME!"
        }
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[enemy2])
    def test_make_enemy_enemy2(self, _):
        character = {"Level": 1}
        actual = make_enemy(character)
        expected = {
            "Name": "Sneaky Shadow",
            "Rank": "1",
            "HP": 100,
            "Max HP": 100,
            "Level": 1,
            "ATK": 1,
            "Basic Attack": 1,
            "Special Attack": 4,
            "Special Attack Name": "Sinister Strike",
            "EXP Given": 25,
            "Encounter Quote": "Sneaky Shadow: Empty your wallets!",
            "Basic Attack Quote": "Sneaky Shadow: Take this!",
            "Special Attack Quote": "Sneaky Shadow: I'll decorate your back... with steel.",
            "Victory Quote": "Sneaky Shadow: Gold... for a pound of flesh.",
            "Death Quote": "Sneaky Shadow: NO LET ME GO, PLEASE!"
        }
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[enemy3])
    def test_make_enemy_enemy3(self, _):
        character = {"Level": 1}
        actual = make_enemy(character)
        expected = {
            "Name": "Puzzled Phantom",
            "Rank": "1",
            "HP": 100,
            "Max HP": 100,
            "Level": 1,
            "ATK": 1,
            "Basic Attack": 2,
            "Special Attack": 2,
            "Special Attack Name": "Spectral Rend",
            "EXP Given": 25,
            "Encounter Quote": "Puzzled Phantom: Who are you? Who am I?",
            "Basic Attack Quote": "Puzzled Phantom: Answer me...",
            "Special Attack Quote": "Puzzled Phantom: LEAVE ME ALONE",
            "Victory Quote": "Puzzled Phantom: This answers nothing...",
            "Death Quote": "Puzzled Phantom: WHAT HAVE YOU DONE?"
        }
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[enemy1])
    def test_make_enemy_enemy1_level_two(self, _):
        character = {"Level": 2}
        actual = make_enemy(character)
        expected = {
            "Name": "Anxious Apparition",
            "Rank": "1",
            "HP": 150,
            "Max HP": 150,
            "Level": 2,
            "ATK": 2,
            "Basic Attack": 2,
            "Special Attack": 3,
            "Special Attack Name": "Deathly Wail",
            "EXP Given": 25,
            "Encounter Quote": "Anxious Apparition: Stop... your soul is mine...",
            "Basic Attack Quote": "Anxious Apparition: Begone...",
            "Special Attack Quote": "Anxious Apparition: DON'T LEAVE ME ALONE",
            "Victory Quote": "Anxious Apparition: Finally, it's over...",
            "Death Quote": "Anxious Apparition: NO PLEASE DON'T KILL ME!"
        }
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[enemy1])
    def test_make_enemy_enemy1_level_three(self, _):
        character = {"Level": 3}
        actual = make_enemy(character)
        expected = {
            "Name": "Anxious Apparition",
            "Rank": "1",
            "HP": 200,
            "Max HP": 200,
            "Level": 3,
            "ATK": 3,
            "Basic Attack": 2,
            "Special Attack": 3,
            "Special Attack Name": "Deathly Wail",
            "EXP Given": 25,
            "Encounter Quote": "Anxious Apparition: Stop... your soul is mine...",
            "Basic Attack Quote": "Anxious Apparition: Begone...",
            "Special Attack Quote": "Anxious Apparition: DON'T LEAVE ME ALONE",
            "Victory Quote": "Anxious Apparition: Finally, it's over...",
            "Death Quote": "Anxious Apparition: NO PLEASE DON'T KILL ME!"
        }
        self.assertEqual(expected, actual)

    def test_make_enemy_arguments_unchanged(self):
        character = {"Level": 3}
        make_enemy(character)
        expected = {"Level": 3}
        self.assertEqual(expected, character)
