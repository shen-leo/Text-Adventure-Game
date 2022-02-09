from unittest import TestCase
from game import special_coordinates


class TestSpecialCoordinates(TestCase):
    def test_special_coordinates(self):
        expected = {'The Apothecary': (12, 12), 'Bates Motel': (1, 23), 'Pierce & Pierce': (23, 1),
                    'Lincoln Center': (23, 23)}
        actual = special_coordinates()
        self.assertEqual(expected, actual)


