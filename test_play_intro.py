import io
from unittest import TestCase
from unittest.mock import patch
from game import play_intro


class TestPlayIntro(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_intro_input_yes(self, _, __):
        actual = play_intro()
        expected_output = False
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_intro_input_no(self, _, __):
        actual = play_intro()
        expected_output = True
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["a", "b", "c", "d", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_intro_input_values_not_in_array_then_input_1(self, _, __):
        actual = play_intro()
        expected_output = False
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["a", "b", "c", "d", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_intro_input_values_not_in_array_then_input_2(self, _, __):
        actual = play_intro()
        expected_output = True
        self.assertEqual(expected_output, actual)

