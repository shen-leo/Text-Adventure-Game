from unittest import TestCase
from unittest.mock import patch
from game import game_pause


class TestGamePause(TestCase):

    @patch('time.sleep', return_value=None)
    def test_game_pause_2_seconds(self, patched_time_sleep):
        game_pause(2)
        # equal to time.sleep(2)

    @patch('time.sleep', return_value=None)
    def test_game_pause_10_seconds(self, patched_time_sleep):
        game_pause(10)
        # equal to time.sleep(10)

    @patch('time.sleep', return_value=None)
    def test_game_pause_0_seconds(self, patched_time_sleep):
        game_pause(0)
        # equal to time.sleep(0)
