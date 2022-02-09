import io
from unittest import TestCase
from unittest.mock import patch
from game import user_combat_turn


class TestUserCombatTurn(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_turn_input_1(self, _, __):
        class_info = {"Special Attack Name": "Special Attack"}
        actual = user_combat_turn(class_info)
        expected_output = '1'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_turn_input_2(self, _, __):
        class_info = {"Special Attack Name": "Special Attack"}
        actual = user_combat_turn(class_info)
        expected_output = '2'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_turn_input_3(self, _, __):
        class_info = {"Special Attack Name": "Special Attack"}
        actual = user_combat_turn(class_info)
        expected_output = '3'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_turn_input_4(self, _, __):
        class_info = {"Special Attack Name": "Special Attack"}
        actual = user_combat_turn(class_info)
        expected_output = '4'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["a", "b", "c", "d", "0", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_turn_input_incorrect_values_then_1(self, _, __):
        class_info = {"Special Attack Name": "Special Attack"}
        actual = user_combat_turn(class_info)
        expected_output = '1'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_combat_turn_class_info_argument_unchanged(self, _, __):
        class_info = {"Special Attack Name": "Special Attack"}
        user_combat_turn(class_info)
        expected_class_info = {"Special Attack Name": "Special Attack"}
        actual_class_info = class_info
        self.assertEqual(expected_class_info, actual_class_info)