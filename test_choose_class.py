import io
from unittest.mock import patch
from unittest import TestCase
from game import choose_class


class TestChooseClass(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_select_1(self, _, __):
        actual = choose_class()
        expected = {
            'ATK Level 1': 10,
            'ATK Level 2': 20,
            'ATK Level 3': 30,
            'Accuracy': 0.5,
            'Attack Description': 'Puts on a raincoat and swings a shimmering axe that '
                                  "aims at the enemy's head. This attack has low accuracy "
                                  'but inflicts heavy damage.',
            'Class Name': 'Investment Banker',
            'Description': 'An investment banker who swings an axe wildly, dealing high '
                           'damage with low accuracy. With \n'
                           'their firm health regiment and use of cocaine, this character '
                           'has high durability. The \n'
                           'Investment Banker is a yuppie who hates the banality of their '
                           "peers' opulent lifestyle.\n",
            'EXP Level 2': 150,
            'EXP Level 3': 375,
            'HP Level 2': 250,
            'HP Level 3': 500,
            'Level One': 'Analyst',
            'Level Three': 'Vice President',
            'Level Two': 'Associate',
            'Special Attack': 10,
            'Special Attack Name': 'Axe Swing'}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_select_2(self, _, __):
        actual = choose_class()
        expected = {'ATK Level 1': 10,
                    'ATK Level 2': 20,
                    'ATK Level 3': 30,
                    'Accuracy': 0.8,
                    'Attack Description': 'Puts on a wig and shanks the enemy using a kitchen '
                                          'knife, dealing moderate damage with\n'
                                          'high accuracy.',
                    'Class Name': 'Motel Employee',
                    'Description': 'An awkward motel employee that strikes the enemy precisely, '
                                   'but with moderate durability.\n'
                                   'Their attacks have high accuracy but only deals moderate '
                                   'damage. The Motel Employee seems to\n'
                                   "be a mama's boy.",
                    'EXP Level 2': 150,
                    'EXP Level 3': 375,
                    'HP Level 2': 150,
                    'HP Level 3': 300,
                    'Level One': 'Clerk',
                    'Level Three': 'Motel Owner',
                    'Level Two': 'Motel Manager',
                    'Special Attack': 5,
                    'Special Attack Name': 'Knife Stab'}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_select_3(self, _, __):
        actual = choose_class()
        expected = {'ATK Level 1': 10,
                    'ATK Level 2': 20,
                    'ATK Level 3': 30,
                    'Accuracy': 0.9,
                    'Attack Description': 'Smashes a hand mirror and stabs the enemy with a glass '
                                          'shard. This attack inflicts\n'
                                          'heavy damage but also cuts the user.',
                    'Class Name': 'Ballet Dancer',
                    'Description': 'A nimble ballet dancer that strikes hard, but has low '
                                   'durability. Their attacks harm\n'
                                   'themselves, but strikes the enemy without mercy. The Ballet '
                                   "Dancer's competitive upbringing\n"
                                   'causes them to do anything for success. ',
                    'EXP Level 2': 150,
                    'EXP Level 3': 350,
                    'HP Level 2': 150,
                    'HP Level 3': 250,
                    'Level One': 'Corps de Ballet',
                    'Level Three': 'Principal',
                    'Level Two': 'Soloist',
                    'Special Attack': 9,
                    'Special Attack Name': 'Mirror Strike'}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_select_4(self, _, __):
        actual = choose_class()
        expected = {'ATK Level 1': 10,
                    'ATK Level 2': 20,
                    'ATK Level 3': 30,
                    'Accuracy': 0.7,
                    'Attack Description': 'Fires several missiles of arcane magic that blasts the '
                                          'enemy. Great for casino lovers.',
                    'Class Name': 'Arcane Mage',
                    'Description': 'A powerful mage from another world who strikes the enemy with '
                                   'unwavering magic. Their attacks\n'
                                   'come in multiple bursts and strikes the enemy randomly. The '
                                   'Arcane Mage hears dark whispers\n'
                                   'which guide them towards opening a portal to another world.',
                    'EXP Level 2': 175,
                    'EXP Level 3': 350,
                    'HP Level 2': 125,
                    'HP Level 3': 300,
                    'Level One': 'Apprentice',
                    'Level Three': 'Archmage',
                    'Level Two': 'Enchanter',
                    'Special Attack': 1000,
                    'Special Attack Name': 'Arcane Missiles'}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_select_1(self, _, __):
        actual = choose_class()
        expected = {'ATK Level 1': 10,
                    'ATK Level 2': 20,
                    'ATK Level 3': 30,
                    'Accuracy': 0.7,
                    'Attack Description': 'Fires several missiles of arcane magic that blasts the '
                                          'enemy. Great for casino lovers.',
                    'Class Name': 'Arcane Mage',
                    'Description': 'A powerful mage from another world who strikes the enemy with '
                                   'unwavering magic. Their attacks\n'
                                   'come in multiple bursts and strikes the enemy randomly. The '
                                   'Arcane Mage hears dark whispers\n'
                                   'which guide them towards opening a portal to another world.',
                    'EXP Level 2': 175,
                    'EXP Level 3': 350,
                    'HP Level 2': 125,
                    'HP Level 3': 300,
                    'Level One': 'Apprentice',
                    'Level Three': 'Archmage',
                    'Level Two': 'Enchanter',
                    'Special Attack': 1000,
                    'Special Attack Name': 'Arcane Missiles'}
        self.assertEqual(expected, actual)

