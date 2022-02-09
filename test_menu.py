import io
from unittest import TestCase
from unittest.mock import patch
from game import menu


class TestMenu(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_stats_command(self, mock_stdout):
        character = {
            "Name": "Leo",
            "Current HP": 10,
            "Max HP": 10,
            "Level": 1,
            "EXP": 10,
            "EXP Breakpoint": 20,
            "Class Level": "Year 1",
            "ATK": 10,
            "Basic Attack": 10}
        class_info = {
            "Class Name": "Student",
            "Description": "A student named Leo.",
            "Special Attack": 5,
            "Special Attack Name": "Punch",
            "Attack Description": "The student punches.",
            "Accuracy": 1.0}

        command = "S"

        keys = {
            "Odile Key": False,
            "Mother Key": False,
            "Paul Key": False,
            "Final Boss": False}

        menu(character, class_info, command, keys)

        expected_output = """
        Character Statistics
        --------------------
        Name: Leo
        HP: 10/10
        Level: 1
        EXP: 10/20
        Class: Student
        Rank: Year 1
        Attack: 10
        
        A student named Leo.
        
"""
        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_abilities_command(self, mock_stdout):
        character = {
            "Name": "Leo",
            "Current HP": 10,
            "Max HP": 10,
            "Level": 1,
            "EXP": 10,
            "EXP Breakpoint": 20,
            "Class Level": "Year 1",
            "ATK": 10,
            "Basic Attack": 10}
        class_info = {
            "Class Name": "Student",
            "Description": "A student named Leo.",
            "Special Attack": 5,
            "Special Attack Name": "Punch",
            "Attack Description": "The student punches.",
            "Accuracy": 1.0}

        command = "A"

        keys = {
            "Odile Key": False,
            "Mother Key": False,
            "Paul Key": False,
            "Final Boss": False}

        menu(character, class_info, command, keys)

        expected_output = f"""
        Character Abilities
        --------------------
        Basic Attack:
        Description - Performs a simple punch that does little damage but never seems to miss.
        Damage - 100
        Accuracy - 100%
              
        Special Attack:
        Name - Punch
        Description - The student punches.
        Damage - 50
        Accuracy - 100%\n"""

        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_inventory_command_zero_keys(self, mock_stdout):
        character = {
            "Name": "Leo",
            "Current HP": 10,
            "Max HP": 10,
            "Level": 1,
            "EXP": 10,
            "EXP Breakpoint": 20,
            "Class Level": "Year 1",
            "ATK": 10,
            "Basic Attack": 10}
        class_info = {
            "Class Name": "Student",
            "Description": "A student named Leo.",
            "Special Attack": 5,
            "Special Attack Name": "Punch",
            "Attack Description": "The student punches.",
            "Accuracy": 1.0}

        command = "I"

        keys = {
            "Odile Key": False,
            "Mother Key": False,
            "Paul Key": False,
            "Final Boss": False}

        menu(character, class_info, command, keys)

        expected_output = ("\n"
                           "Keys\n"
                           "--------------------\n"
                           f"You have 0 keys.\n\n")

        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_inventory_command_four_keys(self, mock_stdout):
        character = {
            "Name": "Leo",
            "Current HP": 10,
            "Max HP": 10,
            "Level": 1,
            "EXP": 10,
            "EXP Breakpoint": 20,
            "Class Level": "Year 1",
            "ATK": 10,
            "Basic Attack": 10}
        class_info = {
            "Class Name": "Student",
            "Description": "A student named Leo.",
            "Special Attack": 5,
            "Special Attack Name": "Punch",
            "Attack Description": "The student punches.",
            "Accuracy": 1.0}

        command = "I"

        keys = {
            "Odile Key": True,
            "Mother Key": True,
            "Paul Key": True,
            "Final Boss": True}

        menu(character, class_info, command, keys)

        expected_output = ("\n"
                           "Keys\n"
                           "--------------------\n"
                           f"You have 4 keys.\n\n")

        function_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected_output, function_printed_this)
