import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice
from game import quit_game


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_1(self, _, __):
        actual = get_user_choice()
        expected_output = '1'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_2(self, _, __):
        actual = get_user_choice()
        expected_output = '2'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_3(self, _, __):
        actual = get_user_choice()
        expected_output = '3'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_4(self, _, __):
        actual = get_user_choice()
        expected_output = '4'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["s"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_s_lower(self, _, __):
        actual = get_user_choice()
        expected_output = 'S'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["S"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_s_upper(self, _, __):
        actual = get_user_choice()
        expected_output = 'S'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["a"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_a_lower(self, _, __):
        actual = get_user_choice()
        expected_output = 'A'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["A"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_a_upper(self, _, __):
        actual = get_user_choice()
        expected_output = 'A'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["i"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_i_lower(self, _, __):
        actual = get_user_choice()
        expected_output = 'I'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["I"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_i_upper(self, _, __):
        actual = get_user_choice()
        expected_output = 'I'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["5", "5", "5", "5", "4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_values_not_in_array_then_input_4(self, _, __):
        actual = get_user_choice()
        expected_output = '4'
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["quit", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_quit_lower(self, _, __):
        with self.assertRaises(SystemExit) as cm:
            quit_game()
        self.assertEqual(cm.exception.code, None)

    @patch('builtins.input', side_effect=["QUIT", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_quit_upper(self, _, __):
        with self.assertRaises(SystemExit) as cm:
            quit_game()
        self.assertEqual(cm.exception.code, None)
