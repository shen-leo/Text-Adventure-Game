import io
from unittest import TestCase
from unittest.mock import patch
from game import gain_exp


class TestGainExp(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_under_level_3(self, mock_stdout):
        character = {"EXP": 0, "EXP Breakpoint": 100}
        class_info = {"EXP Level 3": 300}
        enemy = {"EXP Given": 15}
        gain_exp(character, class_info, enemy)
        expected_output = """You gained 15 EXP, you have 15/100 EXP.
\n"""
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_past_level_3(self, mock_stdout):
        character = {"EXP": 300, "EXP Breakpoint": 300}
        class_info = {"EXP Level 3": 300}
        enemy = {"EXP Given": 15}
        gain_exp(character, class_info, enemy)
        expected_output = """You gained 15 EXP, you have 300/300 EXP.
\n"""
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_zero_gained(self, mock_stdout):
        character = {"EXP": 0, "EXP Breakpoint": 100}
        class_info = {"EXP Level 3": 300}
        enemy = {"EXP Given": 0}
        gain_exp(character, class_info, enemy)
        expected_output = """You gained 0 EXP, you have 0/100 EXP.
\n"""
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    def test_gain_exp_arguments_unchanged(self):
        character = {"EXP": 0, "EXP Breakpoint": 100}
        class_info = {"EXP Level 3": 300}
        enemy = {"EXP Given": 15}
        gain_exp(character, class_info, enemy)
        expected_class_info = {"EXP Level 3": 300}
        expected_enemy = {"EXP Given": 15}
        self.assertEqual(expected_class_info, class_info)
        self.assertEqual(expected_enemy, enemy)
