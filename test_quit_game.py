import io
from unittest.mock import patch
from unittest import TestCase
from game import quit_game


class TestQuitGame(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_game_input_1(self, _, __):
        with self.assertRaises(SystemExit) as cm:
            quit_game()
        self.assertEqual(cm.exception.code, None)

    @patch('builtins.input', side_effect=["a", "b", "c", "d", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_game_input_incorrect_values_then_1(self, _, __):
        with self.assertRaises(SystemExit) as cm:
            quit_game()
        self.assertEqual(cm.exception.code, None)