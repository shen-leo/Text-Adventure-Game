from unittest import TestCase
from unittest.mock import patch
from game import combat_accuracy


class TestCombatAccuracy(TestCase):

    @patch('random.random', side_effect=[0.1])
    def test_combat_accuracy_hit(self, _):
        class_info = {"Accuracy": 0.8}
        actual = combat_accuracy(class_info)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.random', side_effect=[0.9])
    def test_combat_accuracy_miss(self, _):
        class_info = {"Accuracy": 0.8}
        actual = combat_accuracy(class_info)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.random', side_effect=[0.8])
    def test_combat_accuracy_equal_to_accuracy(self, _):
        class_info = {"Accuracy": 0.8}
        actual = combat_accuracy(class_info)
        expected = False
        self.assertEqual(expected, actual)

    def test_combat_accuracy_class_info_unchanged(self):
        class_info = {"Accuracy": 0.8}
        combat_accuracy(class_info)
        expected_class_info = {"Accuracy": 0.8}
        actual_class_info = class_info
        self.assertEqual(expected_class_info, actual_class_info)
