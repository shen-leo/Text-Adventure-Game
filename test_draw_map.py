import io
from unittest import TestCase
from unittest.mock import patch
from game import draw_map


class TestDrawMap(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_map_5_by_5(self, mock_stdout):
        x_coord = 5
        y_coord = 5
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        draw_map(character, x_coord, y_coord, special_locations, width=3)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """#  .  .  .  .  
.  .  .  .  .  
.  .  .  .  .  
.  .  .  .  .  
.  .  .  .  .  
"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_map_1_by_1(self, mock_stdout):
        x_coord = 1
        y_coord = 1
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        draw_map(character, x_coord, y_coord, special_locations, width=3)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """#  
"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_map_25_by_25(self, mock_stdout):
        x_coord = 25
        y_coord = 25
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        draw_map(character, x_coord, y_coord, special_locations, width=3)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """#  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  X  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
.  X  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  X  .  
.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  
"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_map_more_columns_than_rows(self, mock_stdout):
        x_coord = 5
        y_coord = 3
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        draw_map(character, x_coord, y_coord, special_locations, width=3)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """#  .  .  .  .  
.  .  .  .  .  
.  .  .  .  .  
"""
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_map_more_rows_than_columns(self, mock_stdout):
        x_coord = 3
        y_coord = 5
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        special_locations = {
            "The Apothecary": (12, 12),
            "Bates Motel": (1, 23),
            "Pierce & Pierce": (23, 1),
            "Lincoln Center": (23, 23)
        }
        draw_map(character, x_coord, y_coord, special_locations, width=3)
        function_printed_this = mock_stdout.getvalue()
        expected_output = """#  .  .  
.  .  .  
.  .  .  
.  .  .  
.  .  .  
"""
        self.assertEqual(expected_output, function_printed_this)
