import io
from unittest import TestCase
from unittest.mock import patch
from game import get_name


class TestGetName(TestCase):

    @patch('builtins.input', side_effect=["Leo"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_name_single_input(self, _, __):
        character = {"Name": "X"}
        get_name(character)
        expected_output = {"Name": "Leo"}
        actual = character
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=["", "", "", "Leo"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_name_multiple_empty_string_then_correct_input(self, _, __):
        character = {"Name": "X"}
        get_name(character)
        expected_output = {"Name": "Leo"}
        actual = character
        self.assertEqual(expected_output, actual)
