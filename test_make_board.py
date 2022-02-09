from unittest import TestCase
from unittest.mock import patch

from game import make_board


class TestMakeBoard(TestCase):
    @patch('random.choice', side_effect=["Shrouded Street", "Busy Bus Stop", "Creepy Crosswalk", "Malicious Mall",
                                         "Secluded Skyscraper", "Shrouded Street", "Busy Bus Stop", "Creepy Crosswalk",
                                         "Malicious Mall", "Secluded Skyscraper", "Shrouded Street", "Busy Bus Stop",
                                         "Creepy Crosswalk", "Malicious Mall", "Secluded Skyscraper",
                                         "Shrouded Street", "Busy Bus Stop", "Creepy Crosswalk", "Malicious Mall",
                                         "Secluded Skyscraper", "Shrouded Street", "Busy Bus Stop", "Creepy Crosswalk",
                                         "Malicious Mall", "Secluded Skyscraper"])
    def test_make_board_5_by_5(self, _):
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        actual = make_board(5, 5, special_locations)
        expected = {(0, 0): 'The Clinic', (0, 1): 'Busy Bus Stop', (0, 2): 'Creepy Crosswalk', (0, 3): 'Malicious Mall',
                    (0, 4): 'Secluded Skyscraper', (1, 0): 'Shrouded Street', (1, 1): 'Busy Bus Stop',
                    (1, 2): 'Creepy Crosswalk', (1, 3): 'Malicious Mall', (1, 4): 'Secluded Skyscraper',
                    (1, 23): 'Bates Motel', (2, 0): 'Shrouded Street', (2, 1): 'Busy Bus Stop',
                    (2, 2): 'Creepy Crosswalk', (2, 3): 'Malicious Mall', (2, 4): 'Secluded Skyscraper',
                    (3, 0): 'Shrouded Street', (3, 1): 'Busy Bus Stop', (3, 2): 'Creepy Crosswalk',
                    (3, 3): 'Malicious Mall', (3, 4): 'Secluded Skyscraper', (4, 0): 'Shrouded Street',
                    (4, 1): 'Busy Bus Stop', (4, 2): 'Creepy Crosswalk', (4, 3): 'Malicious Mall',
                    (4, 4): 'Secluded Skyscraper', (12, 12): 'The Apothecary',
                    (23, 1): 'Pierce & Pierce', (23, 23): 'Lincoln Center'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["Shrouded Street"])
    def test_make_board_one_by_one(self, _):
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        actual = make_board(1, 1, special_locations)
        expected = {(0, 0): 'The Clinic', (1, 23): 'Bates Motel', (12, 12): 'The Apothecary',
                    (23, 1): 'Pierce & Pierce', (23, 23): 'Lincoln Center'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["Shrouded Street", "Shrouded Street", "Shrouded Street", "Shrouded Street"])
    def test_make_board_two_by_two(self, _):
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        actual = make_board(2, 2, special_locations)
        expected = {(0, 0): 'The Clinic', (0, 1): 'Shrouded Street', (1, 0): 'Shrouded Street',
                    (1, 1): 'Shrouded Street', (1, 23): 'Bates Motel', (12, 12): 'The Apothecary',
                    (23, 1): 'Pierce & Pierce', (23, 23): 'Lincoln Center'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["Shrouded Street", "Shrouded Street"])
    def test_make_board_rows_greater_than_columns(self, _):
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        actual = make_board(2, 1, special_locations)
        expected = {(0, 0): 'The Clinic', (1, 0): 'Shrouded Street', (1, 23): 'Bates Motel', (12, 12): 'The Apothecary',
                    (23, 1): 'Pierce & Pierce', (23, 23): 'Lincoln Center'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["Shrouded Street", "Shrouded Street"])
    def test_make_board_columns_greater_than_rows(self, _):
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        actual = make_board(1, 2, special_locations)
        expected = {(0, 0): 'The Clinic', (0, 1): 'Shrouded Street', (1, 23): 'Bates Motel', (12, 12): 'The Apothecary',
                    (23, 1): 'Pierce & Pierce', (23, 23): 'Lincoln Center'}
        self.assertEqual(expected, actual)
