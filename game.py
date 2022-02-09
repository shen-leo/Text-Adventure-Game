"""
Your name: Leo Shen
Your student number: A01267947

All of your code must go in this file.
"""

import random
import sys
import time
from itertools import cycle
from typing import Union


def game_pause(seconds: Union[int, float]) -> None:
    """
    Suspends the execution of the Python program for number of seconds equal to function argument.

    :param seconds: a number (integer or float)
    :precondition: seconds argument must be a positive integer or float number
    :postcondition: suspends the python program for seconds equal to seconds argument
    :return: None
    """

    time.sleep(seconds)


def special_coordinates() -> dict:
    """
    Defines a dictionary containing coordinates of specific locations.

    :postcondition: defines and returns a dictionary containing a string as key and a two integer tuple as values
    :return: a dictionary

    >>> special_coordinates()
    {'The Apothecary': (12, 12), 'Bates Motel': (1, 23), 'Pierce & Pierce': (23, 1), 'Lincoln Center': (23, 23)}
    """

    special_locations = {
        "The Apothecary": (12, 12),
        "Bates Motel": (1, 23),
        "Pierce & Pierce": (23, 1),
        "Lincoln Center": (23, 23)
    }

    return special_locations


def make_board(rows: int, columns: int, special_locations: dict) -> dict:
    """
    Generate a dictionary containing coordinates with randomized rooms that are rows by columns in size; set specific
    coordinates' location name to a value.

    :param rows: a number (integer)
    :param columns: a number (integer)
    :param special_locations: a dictionary
    :precondition: row and columns arguments must be positive non-zero integers
    :precondition: special_locations argument must be a dictionary with string keys and two integer tuple as values
    :postcondition: generates a dictionary of key-value pairs with coordinates (key) and random locations (value)
    :postcondition: sets pre-determined names to values in the generated dictionary according to special_locations'
                    coordinate values
    :return: a dictionary containing coordinates as keys and location name as values
    """

    rooms = ["Shrouded Street", "Busy Bus Stop", "Creepy Crosswalk", "Malicious Mall", "Secluded Skyscraper"]

    board = {(x_axis, y_axis): random.choice(rooms) for x_axis in range(rows) for y_axis in range(columns)}

    board[(0, 0)] = "The Clinic"

    board[special_locations["The Apothecary"]] = "The Apothecary"

    board[special_locations["Bates Motel"]] = "Bates Motel"

    board[special_locations["Pierce & Pierce"]] = "Pierce & Pierce"

    board[special_locations["Lincoln Center"]] = "Lincoln Center"

    return board


def play_intro() -> bool:
    """
    Asks the user whether they have played the game before continually, then returns False for "Yes" and True for "No".

    :postcondition: continually ask the user for an input until they enter "1" or "2", then return False for "1" and T
                    rue for "2"
    :return: a boolean value, True or False
    """

    played_game = None

    while played_game not in ("1", "2"):
        played_game = input("""
        1: Yes
        2: No
        
        Have you played this game before?:
        """)

    if played_game == "1":
        return False
    elif played_game == "2":
        return True


def make_character() -> dict:
    """
    Creates a dictionary containing user's stats.

    :postcondition: defines and returns a dictionary containing user stats
    :return: a dictionary

    >>> make_character()
    {'Name': 'Temp_Name', 'Level': 1, 'EXP': 0, 'EXP Breakpoint': 'Temp_Num', 'Class': 'Temp_Class', 'Class Level': \
'Temp_Class_Level', 'Basic Attack': 3, 'Max HP': 100, 'Current HP': 100, 'ATK': 10, 'Infamy': 1.0, 'X-coordinate': \
0, 'Y-coordinate': 0}
    """

    player = {
        "Name": "Temp_Name",
        "Level": 1,
        "EXP": 0,
        "EXP Breakpoint": "Temp_Num",
        "Class": "Temp_Class",
        "Class Level": "Temp_Class_Level",
        "Basic Attack": 4,
        "Max HP": 100,
        "Current HP": 100,
        "ATK": 10,
        "X-coordinate": 0,
        "Y-coordinate": 0,
    }

    return player


def game_intro(character: dict) -> None:
    """
    Prints out narrative story for the game.

    :param character: a dictionary
    :precondition: character argument must have a key named 'Name"
    :postcondition: prints out descriptive text
    :postcondition: character argument must be unchanged
    """

    print("""
    Darkness surrounds you. Your body is numb from the feeling of emptiness. You raise your heavy eyelids to 
    see a bright, shining light. All around you is white, a bright sterile color that blinds you. 
    
    You sit up from the bed and stare across the windowless room to see a variety of medical posters. It is completely 
    quiet except for the buzzing noises of bright fluorescent lights. You wonder... why are you here? You have no 
    recollection of how you ended up in this room. Is this Hell?""")

    game_pause(12)

    print("""
    Suddenly, the door to your right creaks open. A tall slender man with brown curls steps into the room. He 
    is draped in the color white, blending in with the blinding room. He seems to be a learned man... a doctor... or 
    perhaps a physician. Nevertheless, his presence provides you with relief as you can now be certain that these four
    walls are not the epilogue to your mortal coil.""")

    game_pause(12)

    print(f"""
    Doctor: Hey {character['Name']}! How are you feeling? You came to my office asking for me to do a check-up
    on you, but you passed right out! 
    
    Doctor: Who am I? I'm Dr. Charles, we've already met earlier today! Why do I look like Paul Bettany? Why you're very
    flattering aren't you.""")

    game_pause(10)

    print(f"""
    Dr. Charles: You know, when I was young, I actually studied literature! It seems my affinity for the arts and
    classics really helped paint the image of someone talented like Paul Bettany. In fact, I studied literature at 
    Princeton... but that doesn't pay the bills unfortunately, so I had to settle on being a doctor. My roommate at the
    time was actually John Nash. Boy, that guy sure had a beautiful mind. May he rest in peace.""")

    game_pause(12)

    print(f"""
    Dr. Charles: Enough about me, lets go over your examination results.
    
    Dr. Charles: Oh... it looks like you have some sort of mysterious illness. This will need to be treated right away.
    You need to head to the pharmacy in the middle of New York. Once you make it there, you can buy the cure to this 
    problem. It'll probably cost you around $12,000 for medication, but it will save your life.""")

    game_pause(10)

    print(f"""
    Dr. Charles: What? You don't have any money? This is the United States of America, you're not getting that 
    medication for free...
    
    Dr. Charles: Hmmm... Maybe we can work something out. The pharmacy has a few employees that seem to hang out around
    New York. I hate those guys... You could try stealing their keys and sneak into the pharmacy to get your 
    medication.""")

    game_pause(10)

    print(f"""
    DR. Charles: Explore New York and try to find those pharmacy employees. Remember, the pharmacy or the apothecary as 
    the kids call it these days, rests in the middle of New York. X's on the map will be places of interest, make your
    way there.""")

    game_pause(8)


def draw_map(character: dict, x_coord: int, y_coord: int, special_locations: dict, width=3) -> None:
    """
    Prints out an ASCII map with the user's location and special locations.

    :param character: a dictionary
    :param x_coord: a number (integer)
    :param y_coord: a number (integer)
    :param special_locations: a dictionary
    :param width: a default number (integer)
    :precondition: character dictionary must have keys "X-coordinate" and "Y-coordinate"
    :precondition: special_locations argument must have keys "The Apothecary", "Bates Motel", "Pierce & Pierce", and
                    "Lincoln Center"
    :precondition: x_coord and y_coord arguments must be non-negative integers
    :postcondition: prints out an ASCII map relative to board size, user location, and special landmarks
    :postcondition: character and special locations arguments must be unchanged

        >>> x_coordinate = 1
    >>> y_coordinate = 1
    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> locations = {"The Apothecary": (12, 12),"Bates Motel": (1, 23),\
    "Pierce & Pierce": (23, 1),"Lincoln Center": (23, 23)}
    >>> draw_map(player, x_coordinate, y_coordinate, locations, width=3) # doctest: +NORMALIZE_WHITESPACE
    #

    >>> x_coordinate = 5
    >>> y_coordinate = 5
    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> locations = {"The Apothecary": (12, 12),"Bates Motel": (1, 23),\
    "Pierce & Pierce": (23, 1),"Lincoln Center": (23, 23)}
    >>> draw_map(player, x_coordinate, y_coordinate, locations, width=3) # doctest: +NORMALIZE_WHITESPACE
        #  .  .  .  .
    .  .  .  .  .
    .  .  .  .  .
    .  .  .  .  .
    .  .  .  .  .
    """

    for rise in range(y_coord):
        for run in range(x_coord):
            if (run, rise) == (character["X-coordinate"], character["Y-coordinate"]):
                print("%%-%ds" % width % '#', end="")
            elif (run, rise) in ((special_locations["The Apothecary"], special_locations["Bates Motel"],
                                  special_locations["Pierce & Pierce"], special_locations["Lincoln Center"])):
                print("%%-%ds" % width % 'X', end="")
            else:
                print("%%-%ds" % width % '.', end="")
        print()


def make_keys() -> dict:
    """
    Creates a dictionary containing key-value pairs containing booleans.

    :postcondition: defines and returns a dictionary with a string as key and a boolean as value
    :return: a dictionary

    >>> make_keys()
    {'Odile Key': False, 'Mother Key': False, 'Paul Key': False, 'Final Boss': False}
    """

    keys = {
        "Odile Key": False,
        "Mother Key": False,
        "Paul Key": False,
        "Final Boss": False
    }

    return keys


def validate_keys(keys: dict) -> bool:
    """
    Evaluates whether certain values in the keys argument are True; outputs True if they all are, False otherwise.

    :param keys: a dictionary
    :precondition: keys argument must be a dictionary with keys "Odile Key", "Mother Key", and "Paul Key"
    :postcondition: returns True if "Odile Key", "Mother Key", and "Paul Key" key-values are all True, otherwise False
    :postcondition: keys argument must be unchanged
    :return: a boolean value, True or False

    >>> keys_dict = {"Odile Key": True, "Mother Key": True, "Paul Key": True,}
    >>> validate_keys(keys_dict)
    True

    >>> keys_dict = {"Odile Key": True, "Mother Key": False, "Paul Key": False,}
    >>> validate_keys(keys_dict)
    False
    """

    if keys["Odile Key"] and keys["Mother Key"] and keys["Paul Key"] is True:
        return True
    else:
        return False


def get_name(character: dict) -> None:
    """
    Asks the user to input a name and saves it in the character dictionary.

    :param character: a dictionary
    :precondition: character argument must be a dictionary with "Name" key
    :postcondition: continually asks the user for an input until they enter something that is not an empty string, then
                    set the "Name" key's value to the input
    """

    inputted_name = ""

    while inputted_name == "":
        inputted_name = input("What is your name?: ")

    character["Name"] = inputted_name


def choose_class() -> dict:
    """
    Asks the user for an input continually until they select something from the options, then returns a dictionary.

    :postcondition: continually asks the user to input a value until they enter "1", "2", "3", or "4", then returns a
                    dictionary depending on their inputted value
    :return: a dictionary
    """

    investment_banker = {
        "Class Name": "Investment Banker",
        "Level One": "Analyst",
        "Level Two": "Associate",
        "Level Three": "Vice President",
        "Special Attack Name": "Axe Swing",
        "Special Attack": 10,
        "Attack Description": "Puts on a raincoat and swings a shimmering axe that aims at the enemy's head. This "
                              "attack has low accuracy but inflicts heavy damage.",
        "Accuracy": 0.5,
        "EXP Level 2": 150,
        "EXP Level 3": 375,
        "ATK Level 1": 10,
        "ATK Level 2": 20,
        "ATK Level 3": 30,
        "HP Level 2": 250,
        "HP Level 3": 500,
        "Description": "An investment banker who swings an axe wildly, dealing high damage with low accuracy. With \n"
                       "their firm health regiment and use of cocaine, this character has high durability. The \n"
                       "Investment Banker is a yuppie who hates the banality of their peers' opulent lifestyle.\n"
    }

    motel_employee = {
        "Class Name": "Motel Employee",
        "Level One": "Clerk",
        "Level Two": "Motel Manager",
        "Level Three": "Motel Owner",
        "Special Attack Name": "Knife Stab",
        "Special Attack": 7,
        "Attack Description": "Puts on a wig and shanks the enemy using a kitchen knife, dealing moderate damage with\n"
                              "high accuracy.",
        "Accuracy": 0.8,
        "EXP Level 2": 150,
        "EXP Level 3": 375,
        "ATK Level 1": 10,
        "ATK Level 2": 20,
        "ATK Level 3": 30,
        "HP Level 2": 150,
        "HP Level 3": 400,
        "Description": "An awkward motel employee that strikes the enemy precisely, but with moderate durability.\n"
                       "Their attacks have high accuracy but only deals moderate damage. The Motel Employee seems to\n"
                       "be a mama's boy."
    }

    ballet_dancer = {
        "Class Name": "Ballet Dancer",
        "Level One": "Corps de Ballet",
        "Level Two": "Soloist",
        "Level Three": "Principal",
        "Special Attack Name": "Mirror Strike",
        "Special Attack": 9,
        "Attack Description": "Smashes a hand mirror and stabs the enemy with a glass shard. This attack inflicts\n"
                              "heavy damage but also cuts the user.",
        "Accuracy": 0.9,
        "EXP Level 2": 150,
        "EXP Level 3": 350,
        "ATK Level 1": 10,
        "ATK Level 2": 20,
        "ATK Level 3": 30,
        "HP Level 2": 150,
        "HP Level 3": 300,
        "Description": "A nimble ballet dancer that strikes hard, but has low durability. Their attacks harm\n"
                       "themselves, but strikes the enemy without mercy. The Ballet Dancer's competitive upbringing\n"
                       "causes them to do anything for success. "
    }

    arcane_mage = {
        "Class Name": "Arcane Mage",
        "Level One": "Apprentice",
        "Level Two": "Enchanter",
        "Level Three": "Archmage",
        "Special Attack Name": "Arcane Missiles",
        "Special Attack": 1000,
        "Attack Description": "Fires several missiles of arcane magic that blasts the enemy. Great for casino lovers.",
        "Accuracy": 0.7,
        "EXP Level 2": 175,
        "EXP Level 3": 350,
        "ATK Level 1": 10,
        "ATK Level 2": 20,
        "ATK Level 3": 30,
        "HP Level 2": 125,
        "HP Level 3": 350,
        "Description": "A powerful mage from another world who strikes the enemy with unwavering magic. Their attacks\n"
                       "come in multiple bursts and strikes the enemy randomly. The Arcane Mage hears dark whispers\n"
                       "which guide them towards opening a portal to another world."
    }

    select_a_class = ""

    while select_a_class not in ("1", "2", "3", "4"):
        select_a_class = input("""
    1: Investment Banker - works on Wall Street, seems to have a keen eye for stationary
    2: Motel Employee - an awkward but kind person, seems to have a great relationship with their mom
    3: Ballet Dancer - passionate about dance, seems to hate Mila Kunis for some reason...
    4: Arcane Mage - w...wh...what are you doing here in New York? Go back to Karazhan!
        
    Please select a class: """)

    if select_a_class == "1":
        return investment_banker
    if select_a_class == "2":
        return motel_employee
    if select_a_class == "3":
        return ballet_dancer
    if select_a_class == "4":
        return arcane_mage


def describe_current_location(board: dict, character: dict) -> None:
    """
    Describe the character's current coordinates and its associated location name.

    :param board: a dictionary containing key-value pairs representing coordinates and random location names
    :param character: a dictionary containing the character's coordinates and current HP
    :precondition: board parameter must be dictionary with a two integer tuple as keys and a string for the values
    :precondition: character parameter must be dictionary with 'X-coordinate' and 'Y-coordinate' keys with integer value
    :postcondition: prints a string displaying the character's current X and Y coordinates and location name
    :postcondition: board argument is unchanged
    :postcondition: character argument is unchanged

    >>> location = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> describe_current_location(location, player)
    Your coordinates are (0, 0), your location is: Empty Room.
    <BLANKLINE>
    """

    coordinate_key = (character.get('X-coordinate'), character.get('Y-coordinate'))
    current_location = board[coordinate_key]
    print(f"Your coordinates are {coordinate_key}, your location is: {current_location}.\n")


def quit_game() -> None:
    """
    Asks user for input continually until they enter "1" or "2", then raises SystemExit exception if "1" was inputted.

    :postcondition: continually asks the user for input until they enter "1" or "2", then invokes sys.exit if "1"
                    inputted, causing a SystemExit exception
    """

    print("\nLooks like you're giving up...\n")

    response = ""

    while response not in ("1", "2"):
        response = input("1 - Quit Game.\n"
                         "2 - Cancel\n"
                         "\n"
                         "Would you like to quit the game?: ")

    if response == "1":
        sys.exit()


def get_user_choice() -> str:
    """
    Show user a list of possible commands and repeatedly asks them for an input until a value 1-4 or quit is entered,
    entering quit will invoke the quit_game function.

    :postcondition: prints possible directions and repeatedly asks for an input until "1", "2", "3", "4", or any form of
                    "QUIT" is inputted. If a number 1-4 is inputted, return that number as a string. If "QUIT" is
                    inputted, invoke the quit_game function
    :return: a string value ("1", "2", "3", or "4")
    """

    menu_items = ["Up", "Down", "Left", "Right"]

    for count, item in enumerate(menu_items, 1):
        print(count, item)

    print("-------------\n"
          "S - Status\n"
          "A - Abilities\n"
          "I - Inventory\n"
          "Quit - Exit Game\n")

    command = ""

    while command not in ("1", "2", "3", "4", "S", "A", "I", "QUIT"):
        command = input("Input a command: ")
        command = command.upper()

    if command == "QUIT":
        quit_game()

    return command


def menu(character: dict, class_info: dict, command: str, keys: dict) -> None:
    """
    Prints information Character, Ability, and Keys information for the user depending on command argument.

    :param character: a dictionary
    :param class_info: a dictionary
    :param command: a string ("S", "A", or "I")
    :param keys: a dictionary
    :precondition: character argument must be a dictionary containing "Name", "Current HP", "Max HP", "Level", "EXP",
                    "EXP Breakpoint", "Class Level", "ATK", and "Basic Attack" keys
    :precondition: class_info argument must ba a dictionary containing "Class Name", "Description", "Special Attack",
                    "Special Attack Name", "Attack Description", and "Accuracy" keys
    :precondition: command argument must be an "S", "A", or "I" string value
    :precondition: keys argument must be a dictionary whose values are booleans
    :postcondition: if command is "S", prints out information about the user's character statistics
    :postcondition: if command is "A", prints out information about the user's abilities
    :postcondition: if command is "I", prints out information about the user's inventory

    >>> player = {"Name": "Leo", "Current HP": 10, "Max HP": 10, "Level": 1, "EXP": 10, "EXP Breakpoint": 20,\
    "Class Level": "Year 1", "ATK": 10, "Basic Attack": 10}
    >>> class_information = {"Class Name": "Student","Description": "A student named Leo.", "Special Attack": 5,\
    "Special Attack Name": "Punch", "Attack Description": "The student punches.", "Accuracy": 1.0}
    >>> game_keys = {"Odile Key": False, "Mother Key": False, "Paul Key": False, "Final Boss": False}
    >>> input_command = "S"
    >>> menu(player, class_information, input_command, game_keys) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
        Character Statistics
        --------------------
        Name: Leo
        HP: 10/10
        Level: 1
        EXP: 10/20
        Class: Student
        Rank: Year 1
        Attack: 10
    <BLANKLINE>
        A student named Leo.
    <BLANKLINE>

    >>> input_command = "A"
    >>> menu(player, class_information, input_command, game_keys) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
        Character Abilities
        --------------------
        Basic Attack:
        Description - Performs a simple punch that does little damage but never seems to miss.
        Damage - 100
        Accuracy - 100%
    <BLANKLINE>
        Special Attack:
        Name - Punch
        Description - The student punches.
        Damage - 50
        Accuracy - 100%
    <BLANKLINE>

    >>> input_command = "I"
    >>> menu(player, class_information, input_command, game_keys) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
        Keys
        --------------------
        You have 0 keys.
    <BLANKLINE>
    """

    key_count = 0

    for key in keys:
        if keys[key] is True:
            key_count += 1

    if command == "S":
        print(f"""
        Character Statistics
        --------------------
        Name: {character['Name']}
        HP: {character['Current HP']}/{character['Max HP']}
        Level: {character['Level']}
        EXP: {character['EXP']}/{character['EXP Breakpoint']}
        Class: {class_info['Class Name']}
        Rank: {character['Class Level']}
        Attack: {character['ATK']}
        
{class_info['Description']}
        """)

    if class_info["Class Name"] == "Arcane Mage":
        special_attack_damage = f"Randomly fires 0-5 magic missiles that do {1 * character['ATK']}, " \
                                f"{2 * character['ATK']}, {3 * character['ATK']}, {4 * character['ATK']}, " \
                                f"and {5 * character['ATK']} damage."
    else:
        special_attack_damage = class_info['Special Attack'] * character['ATK']

    if command == "A":
        print(f"""
        Character Abilities
        --------------------
        Basic Attack:
        Description - Performs a simple punch that does little damage but never seems to miss.
        Damage - {character["Basic Attack"] * character["ATK"]}
        Accuracy - 100%
              
        Special Attack:
        Name - {class_info['Special Attack Name']}
        Description - {class_info['Attack Description']}
        Damage - {special_attack_damage}
        Accuracy - {int(class_info['Accuracy'] * 100)}%""")

    if command == "I":
        print(f"\n"
              "Keys\n"
              "--------------------\n"
              f"You have {key_count} keys.\n")


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Validate whether the new coordinates of the character reside within the coordinate keys from board argument.

    :param board: a dictionary containing key-value pairs representing coordinates and random location names
    :param character: a dictionary containing the character's coordinates and current HP
    :param direction: a string ("1", "2", "3", or "4")
    :precondition: board parameter must be dictionary with a two integer tuple as keys and a string for the values
    :precondition: character parameter must be dictionary with 'X-coordinate' and 'Y-coordinate' keys with integer value
    :precondition: direction parameter must be a string value equal to "1", "2", "3", or "4"
    :postcondition: calculates the new coordinates of character and evaluates True if it's in board and False if not
    :postcondition: board argument is unchanged
    :postcondition: character argument is unchanged
    :postcondition: direction argument is unchanged
    :return: a boolean value, True or False

    >>> location = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> movement = "2"
    >>> validate_move(location, player, movement)
    True

    >>> location = {(0, 0): 'Empty Room', (0, 1): 'Empty Room'}
    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> movement = "1"
    >>> validate_move(location, player, movement)
    False
    """

    x_scalar = 0
    y_scalar = 0

    if direction == "1":
        y_scalar = character["Y-coordinate"] - 1
    if direction == "2":
        y_scalar = character["Y-coordinate"] + 1
    if direction == "3":
        x_scalar = character["X-coordinate"] - 1
    if direction == "4":
        x_scalar = character["X-coordinate"] + 1

    new_coordinate = (x_scalar, y_scalar)

    if new_coordinate in board:
        return True
    else:
        return False


def move_character(character: dict, direction: str) -> None:
    """
    Modify the character's X or Y coordinate depending on the value of direction argument.

    :param character: a dictionary containing the character's coordinates and current HP
    :param direction: a string ("1", "2", "3", or "4")
    :precondition: character parameter must be dictionary with 'X-coordinate' and 'Y-coordinate' keys with integer value
    :precondition: direction parameter must be a string value equal to "1", "2", "3", or "4"
    :postcondition: evaluates the value of direction and adds or subtracts 1 to character's X or Y coordinate

    >>> player = {'X-coordinate': 1, 'Y-coordinate': 1}
    >>> movement = "2"
    >>> move_character(player, movement)
    >>> player['Y-coordinate'] == 2
    True

    >>> player = {'X-coordinate': 1, 'Y-coordinate': 1}
    >>> movement = "4"
    >>> move_character(player, movement)
    >>> player['X-coordinate'] == 2
    True
    """

    if direction == "1":
        character["Y-coordinate"] -= 1
    if direction == "2":
        character["Y-coordinate"] += 1
    if direction == "3":
        character["X-coordinate"] -= 1
    if direction == "4":
        character["X-coordinate"] += 1


def check_for_boss(character: dict, special_locations: dict) -> bool:
    """
    Evaluates whether the character's current coordinates exist within the special_locations dictionary.

    :param character: a dictionary
    :param special_locations: a dictionary
    :precondition: character argument must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: checks whether the characters current "X-coordinate" and "Y-coordinate" values as a tuple exists
                    inside the special_locations dictionary
    :postcondition: character and special_locations arguments must be unchanged
    :return: a boolean value, True or False

    >>> player = {"X-coordinate": 12,"Y-coordinate": 12}
    >>> locations = {"The Apothecary": (12, 12),"Bates Motel": (1, 23),"Pierce & Pierce": (23, 1),\
    "Lincoln Center": (23, 23)}
    >>> check_for_boss(player, locations)
    True

    >>> player = {"X-coordinate": 10,"Y-coordinate": 10}
    >>> locations = {"The Apothecary": (12, 12),"Bates Motel": (1, 23),"Pierce & Pierce": (23, 1),\
    "Lincoln Center": (23, 23)}
    >>> check_for_boss(player, locations)
    False
    """

    if (character['X-coordinate'], character["Y-coordinate"]) in list(special_locations.values()):
        return True
    else:
        return False


def check_for_foes() -> bool:
    """
    Random probability check that returns True 20% of the time.

    :postcondition: rolls a random number between [0, 1), returns True if the number is less than 0.20 (not inclusive)
    :return: a boolean value, True or False
    """

    randomizer = random.random()

    if randomizer < 0.20:
        return True
    else:
        return False


def make_enemy(character):
    """
    Defines three dictionaries containing enemy information, then randomly returns one of them.

    :param character: a dictionary
    :precondition: character argument must have "Level" key
    :postcondition: creates three dictionaries containing enemy stats, then returns one of the three
    :postcondition: if character is Level 2 or 3, modify the statistics of each enemy dictionary
    :postcondition: character argument must be unchanged
    :return: a randomly selected dictionary
    """

    enemy1 = {
        "Name": "Anxious Apparition",
        "Rank": "1",
        "HP": 100,
        "Max HP": 100,
        "Level": 1,
        "ATK": 1,
        "Basic Attack": 2,
        "Special Attack": 3,
        "Special Attack Name": "Deathly Wail",
        "EXP Given": 25,
        "Encounter Quote": "Anxious Apparition: Stop... your soul is mine...",
        "Basic Attack Quote": "Anxious Apparition: Begone...",
        "Special Attack Quote": "Anxious Apparition: DON'T LEAVE ME ALONE",
        "Victory Quote": "Anxious Apparition: Finally, it's over...",
        "Death Quote": "Anxious Apparition: NO PLEASE DON'T KILL ME!"
    }

    enemy2 = {
        "Name": "Sneaky Shadow",
        "Rank": "1",
        "HP": 100,
        "Max HP": 100,
        "Level": 1,
        "ATK": 1,
        "Basic Attack": 1,
        "Special Attack": 4,
        "Special Attack Name": "Sinister Strike",
        "EXP Given": 25,
        "Encounter Quote": "Sneaky Shadow: Empty your wallets!",
        "Basic Attack Quote": "Sneaky Shadow: Take this!",
        "Special Attack Quote": "Sneaky Shadow: I'll decorate your back... with steel.",
        "Victory Quote": "Sneaky Shadow: Gold... for a pound of flesh.",
        "Death Quote": "Sneaky Shadow: NO LET ME GO, PLEASE!"
    }

    enemy3 = {
        "Name": "Puzzled Phantom",
        "Rank": "1",
        "HP": 100,
        "Max HP": 100,
        "Level": 1,
        "ATK": 1,
        "Basic Attack": 2,
        "Special Attack": 2,
        "Special Attack Name": "Spectral Rend",
        "EXP Given": 25,
        "Encounter Quote": "Puzzled Phantom: Who are you? Who am I?",
        "Basic Attack Quote": "Puzzled Phantom: Answer me...",
        "Special Attack Quote": "Puzzled Phantom: LEAVE ME ALONE",
        "Victory Quote": "Puzzled Phantom: This answers nothing...",
        "Death Quote": "Puzzled Phantom: WHAT HAVE YOU DONE?"
    }

    selected_enemy = random.choice([enemy1, enemy2, enemy3])

    if character["Level"] == 2:
        selected_enemy["Level"] = 2
        selected_enemy["ATK"] = 2
        selected_enemy["HP"] = 200
        selected_enemy["Max HP"] = 200
    elif character["Level"] == 3:
        selected_enemy["Level"] = 3
        selected_enemy["ATK"] = 4
        selected_enemy["HP"] = 350
        selected_enemy["Max HP"] = 350

    return selected_enemy


def gain_exp(character: dict, class_info: dict, enemy: dict) -> None:
    """
    Adds a value to the character's EXP equal to the given EXP of an enemy, then prints the characters EXP status.

    :param character: a dictionary
    :param class_info: a dictionary
    :param enemy: a dictionary
    :precondition: character argument must be a dictionary with "EXP" and "EXP Breakpoint" keys
    :precondition: class_info argument must be a dictionary with "EXP Level 3" key
    :precondition: enemy argument must be a dictionary with "EXP Given" key
    :postcondition: adds the value of "EXP Given" from the enemy dictionary to the character dictionary's "EXP" value
    :postcondition: if the character's EXP exceeds the maximum value at level three, set it to the maximum value
    :postcondition: class_info and enemy arguments should be unchanged

    >>> player = {"EXP": 0, "EXP Breakpoint": 100}
    >>> class_information = {"EXP Level 3": 300}
    >>> enemy_stats = {"EXP Given": 15}
    >>> gain_exp(player, class_information, enemy_stats)
    You gained 15 EXP, you have 15/100 EXP.
    <BLANKLINE>

    >>> player = {"EXP": 300, "EXP Breakpoint": 300}
    >>> class_information = {"EXP Level 3": 300}
    >>> enemy_stats = {"EXP Given": 15}
    >>> gain_exp(player, class_information, enemy_stats)
    You gained 15 EXP, you have 300/300 EXP.
    <BLANKLINE>
    """

    character["EXP"] += enemy["EXP Given"]
    if character["EXP"] >= class_info["EXP Level 3"]:
        character["EXP"] = class_info["EXP Level 3"]
    print(f"You gained {enemy['EXP Given']} EXP, you have {character['EXP']}/{character['EXP Breakpoint']} EXP.\n")


def level_up(character: dict, class_info: dict) -> None:
    """
    Levels up the character and modifies their stats according to their level.

    :param character: a dictionary
    :param class_info: a dictionary
    :precondition: character argument must be a dictionary with "Level", "EXP", "ATK", "Max HP", "Class Level",
                    "EXP Breakpoint", "Current HP" keys
    :precondition: class_info argument must be a dictionary with "EXP Level 2", "ATK Level 2", "HP Level 2", "Level Two"
                    "EXP Level 3", "ATK Level 3", "HP Level 3", and "Level 3" keys
    :postcondition: modifies the characters statistics depending on their level and current EXP, then prints out a level
                    up message
    :postcondition: class_info argument must be unchanged

    >>> player = {"Level": 1, "EXP": 20, "EXP Breakpoint": 20, "ATK": 10, "Current HP": 100,\
     "Max HP": 100, "Class Level": "Year 1"}
    >>> class_information = {"EXP Level 2": 20, "ATK Level 2": 20, "HP Level 2": 200, "Level Two": "Year 2",\
      "EXP Level 3": 30, "ATK Level 3": 30, "HP Level 3": 300, "Level Three": "Year 3"}
    >>> level_up(player, class_information)
    You are a now Level 2! Your Class Rank is Year 2.

    >>> player = {"Level": 2, "EXP": 30, "EXP Breakpoint": 30, "ATK": 20, "Current HP": 200,\
     "Max HP": 200, "Class Level": "Year 2"}
    >>> class_information = {"EXP Level 2": 20, "ATK Level 2": 20, "HP Level 2": 200, "Level Two": "Year 2",\
      "EXP Level 3": 30, "ATK Level 3": 30, "HP Level 3": 300, "Level Three": "Year 3"}
    >>> level_up(player, class_information)
    You are a now Level 3! Your Class Rank is Year 3.
    """

    if character["Level"] == 1 and character["EXP"] >= class_info["EXP Level 2"]:
        character["Level"] = 2
        character["ATK"] = class_info["ATK Level 2"]
        character["Max HP"] = class_info["HP Level 2"]
        character["Class Level"] = class_info["Level Two"]
        character["EXP Breakpoint"] = class_info["EXP Level 3"]
        character["Current HP"] = character["Max HP"]
        print(f"You are a now Level {character['Level']}! Your Class Rank is {character['Class Level']}.")

    if character["Level"] == 2 and character["EXP"] >= class_info["EXP Level 3"]:
        character["Level"] = 3
        character["ATK"] = class_info["ATK Level 3"]
        character["Max HP"] = class_info["HP Level 3"]
        character["Class Level"] = class_info["Level Three"]
        character["Current HP"] = character["Max HP"]
        print(f"You are a now Level {character['Level']}! Your Class Rank is {character['Class Level']}.")


def initiate_stats(character: dict, class_info: dict) -> None:
    """
    Initializes the starting stats for the character using the class_info dictionary.

    :param character: a dictionary
    :param class_info: a dictionary
    :precondition: character argument must be a dictionary with "Class Level", "EXP Breakpoint", "ATK", and "Name" keys
    :precondition: class_info argument must be a dictionary with "Level One", "EXP Level 2", "ATK Level 1", and
                    "Class Name" keys
    :postcondition: sets the characters default starting stats to information help in the class_info dictionary
    :postcondition: prints out a greeting for the user with the character's Name and Class Name
    :post_condition: class_info argument is unchanged
    """

    character["Class Level"] = class_info["Level One"]
    character["EXP Breakpoint"] = class_info["EXP Level 2"]
    character["ATK"] = class_info["ATK Level 1"]
    print(f"\nGreetings, {character['Name']} the {class_info['Class Name']}.\n")


def user_combat_turn(class_info: dict) -> str:
    """
    Outputs a string of options then asks the user for an input until they enter "1", "2", "3", or "4".

    :param class_info: a dictionary
    :precondition: class_info is a dictionary containing "Special Attack Name" key
    :postcondition: continually asks the user for input until they enter "1", "2", "3", or "4", then returns the value
    :postcondition: class_info argument is unchanged
    :return: a string ("1", "2", "3", or "4")
    """

    user_choice = ""

    while user_choice not in ("1", "2", "3", "4"):
        user_choice = input(f"""
        1: Basic Attack
        2: {class_info["Special Attack Name"]}
        3: Block
        4: Run\n
        Select a move: """)
        print("\n")

    return user_choice


def user_combat_basic(character: dict, enemy: dict) -> None:
    """
    Character attacks the enemy with a basic attack, deducting damage from the enemy's HP.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: character argument is a dictionary with "Basic Attack" and "ATK" keys
    :precondition: enemy argument is a dictionary with "HP" and "Max HP" keys
    :postcondition: calculates the character's basic attack damage and subtracts it from the enemy's HP
    :postcondition: prints messages with information about the user's attack and the enemy's HP status
    :postcondition: character argument is unchanged

    >>> player = {"Basic Attack": 10, "ATK": 10}
    >>> enemy_info = {"HP": 100, "Max HP": 100}
    >>> user_combat_basic(player, enemy_info)
    You used Basic Attack, dealing 100 damage.
    Enemy HP: 0/100
    <BLANKLINE>
    >>> player = {"Basic Attack": 0, "ATK": 10}
    >>> enemy_info = {"HP": 100, "Max HP": 100}
    >>> user_combat_basic(player, enemy_info)
    You used Basic Attack, dealing 0 damage.
    Enemy HP: 100/100
    <BLANKLINE>
    """

    damage = character["Basic Attack"] * character["ATK"]
    enemy["HP"] -= damage

    if enemy["HP"] < 0:
        enemy["HP"] = 0

    print(f"You used Basic Attack, dealing {damage} damage.")
    print(f"Enemy HP: {enemy['HP']}/{enemy['Max HP']}\n")

    game_pause(1)


def user_combat_special(character: dict, class_info: dict, enemy: dict) -> None:
    """
    Character attacks the enemy with a special attack, deducting damage from the enemy's HP.

    :param character: a dictionary
    :param class_info: a dictionary
    :param enemy: a dictionary
    :precondition: character argument is a dictionary with the "ATK" key
    :precondition: class_info argument is a dictionary with "Class Name", "Special Attack", "Special Attack Name" keys
    :precondition: enemy argument is a dictionary with "HP" and "Max HP" keys
    :postcondition: calculates the character's special attack damage and subtracts it from the enemy's HP
    :postcondition: if character's Class Name is Arcane Mage, the arcane_missiles function will be invoked
    :postcondition: if character's Class Name is Ballet Dancer, the mirror_strike function will be invoked
    :postcondition: prints messages with information about the user's attack and the enemy's HP status
    :postcondition: class_info arguments is unchanged

    >>> player = {"ATK": 10}
    >>> class_information = {"Class Name": "Motel Manager","Special Attack": 5,"Special Attack Name": "Motel Punch"}
    >>> enemy_info = {"HP": 100, "Max HP": 100}
    >>> user_combat_special(player, class_information, enemy_info)
    You used Motel Punch, dealing 50 damage.
    Enemy HP: 50/100
    <BLANKLINE>

    >>> player = {"ATK": 10}
    >>> class_information = {"Class Name": "Investment Banker","Special Attack": 5,\
    "Special Attack Name": "Investment Punch"}
    >>> enemy_info = {"HP": 100, "Max HP": 100}
    >>> user_combat_special(player, class_information, enemy_info)
    You used Investment Punch, dealing 50 damage.
    Enemy HP: 50/100
    <BLANKLINE>

    # cannot test the Arcane Mage class in doctests due to invoking a random function
    """

    damage = class_info["Special Attack"] * character["ATK"]

    if class_info["Class Name"] == "Arcane Mage":
        damage = arcane_missiles(character)
    if class_info["Class Name"] == "Ballet Dancer":
        damage = mirror_strike(character, class_info)

    enemy["HP"] -= damage

    if enemy["HP"] < 0:
        enemy["HP"] = 0

    print(f"You used {class_info['Special Attack Name']}, dealing {damage} damage.")
    print(f"Enemy HP: {enemy['HP']}/{enemy['Max HP']}\n")

    game_pause(1)


def mirror_strike(character: dict, class_info: dict) -> int:
    """
    Subtracts HP from character's current HP then returns damage equal to attack x special attack.

    :param character: a dictionary
    :param class_info: a dictionary
    :precondition: character argument must be a dictionary with "Current HP", "Level", and "ATK" keys
    :precondition: class_info argument must be a dictionary with "Special Attack" key
    :postcondition: subtracts 5 x character's level from current HP
    postcondition: calculates and returns damage dealt as character's attack x the special attack damage
    :postcondition: class_info argument is unchanged
    :return: an integer

    >>> player = {"ATK": 10, "Current HP": 100, "Level": 2}
    >>> class_information = {"Special Attack": 5}
    >>> mirror_strike(player, class_information)
    You cut yourself with the mirror's edge, inflicting 10 damage to yourself.
    50

    >>> player = {"ATK": 0, "Current HP": 100, "Level": 2}
    >>> class_information = {"Special Attack": 5}
    >>> mirror_strike(player, class_information)
    You cut yourself with the mirror's edge, inflicting 10 damage to yourself.
    0
    """

    character["Current HP"] -= 5 * character["Level"]

    if character["Current HP"] < 0:
        character["Current HP"] = 0

    print(f"You cut yourself with the mirror's edge, inflicting {5 * character['Level']} damage to yourself.")

    return character["ATK"] * class_info["Special Attack"]


def arcane_missiles(character: dict) -> int:
    """
    Cycles through numbers 1-5, with each value having 50% chance to deal damage equal to it times character's attack.

    :param character: a dictionary
    :precondition: character argument is a dictionary with "ATK" key value
    :postcondition: each number in 1-5 (5 inclusive) has a 50% chance to deal damage equal to itself times character's
                    attack. The function sums the individual damages and returns the total damage calculated
    :postcondition: tracks and prints the number of successful hits
    :postcondition: character argument is unchanged
    :return: an integer
    """

    missiles_fired = 0
    total_damage = 0
    successful_hits = 0
    for possible_damage in cycle([1, 2, 3, 4, 5]):
        randomizer = random.random()
        missiles_fired += 1

        if randomizer < 0.5:
            total_damage += possible_damage * character["ATK"]
            successful_hits += 1
        if missiles_fired == 5:
            print(f"You channeled {successful_hits} Arcane Missiles!")
            return total_damage


def combat_accuracy(class_info: dict) -> bool:
    """
    Rolls a random number between 0.0 and 1.0 (1 not inclusive), returns True if less than accuracy, False otherwise.

    :param class_info: a dictionary
    :precondition: class_info argument is a dictionary with "Accuracy" key
    :postcondition: rolls a random float between [0, 1) and returns True if the random number is less than accuracy,
                    False otherwise
    :postcondition: class_info argument is unchanged
    :return: a boolean value, True or False
    """

    randomizer = random.random()

    if randomizer < class_info["Accuracy"]:
        return True
    else:
        return False


def enemy_combat_turn(character: dict, enemy: dict) -> None:
    """
    Roll a random number in [0.0, 1.0), if outcome is less than 0.5, perform a special attack, otherwise basic attack.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: character argument must be a dictionary with "Current HP" and "Max HP" keys
    :precondition: enemy argument must be a dictionary with "Special Attack", "ATK", "Special Attack Quote", "Name",
                    "Basic Attack", and "Basic Attack Quote" keys
    :postcondition: subtracts HP from the user depending on whether the randomizer is less than 0.5 (Special Attack)
                    or more (Basic Attack).
    :postcondition: enemy argument is unchanged
    """

    randomizer = random.random()

    if randomizer < 0.5:
        character["Current HP"] -= enemy["Special Attack"] * enemy["ATK"]
        if character["Current HP"] < 0:
            character["Current HP"] = 0
        print(f"{enemy['Special Attack Quote']}")
        print(
            f"{enemy['Name']} attacked you with {enemy['Special Attack Name']}! You took \
{enemy['Special Attack'] * enemy['ATK']} damage, your HP is now \
{character['Current HP']}/{character['Max HP']}.\n")
    else:
        character["Current HP"] -= enemy["Basic Attack"] * enemy["ATK"]
        if character["Current HP"] < 0:
            character["Current HP"] = 0
        print(f"{enemy['Basic Attack Quote']}")
        print(
            f"{enemy['Name']} attacked you with a Basic Attack! You took \
{enemy['Basic Attack'] * enemy['ATK']} damage, your HP is now \
{character['Current HP']}/{character['Max HP']}.\n")

    if character["Current HP"] < 0:
        character["Current HP"] = 0

    game_pause(1)


def final_boss_encounter(enemy: dict, character: dict) -> None:
    """
    Final Boss randomly deals damage equal to numbers each number from 1-8 multiplied by attack divided by two.

    :param enemy: a dictionary
    :param character: a dictionary
    :precondition: enemy argument is a dictionary with "ATK" key
    :precondition: character argument is a dictionary with "Current HP" and "Max HP" keys
    :postcondition: streams through values 1-8, each with 50% change to deal damage equal to the value multiplied by
                    enemy's attack divided by 2
    :postcondition: enemy argument is unchanged
    """

    possible_damage = (1, 2, 3, 4, 5, 6, 7, 8)

    def boss_encounter_damage_hits(attack_damage):
        randomizer = random.random()
        if randomizer < 0.5:
            print(f"The enemy successfully struck you with {attack_damage} tentacle(s)")
            game_pause(0.5)
            return attack_damage
        else:
            attack_damage = 0
            return attack_damage

    damage = sum(map(boss_encounter_damage_hits, possible_damage))

    character["Current HP"] -= int(damage * enemy["ATK"] / 2)

    print(f"Your HP is {character['Current HP']}/{character['Max HP']}.\n")


def escape_damage(character: dict, enemy: dict) -> None:
    """
    Enemy deals damage to equal to their basic attack x ATK to the user 20% of the time when the player runs away.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: character argument must be a dictionary with "Current HP" and "Max HP" keys
    :precondition: enemy argument must be a dictionary  with "Basic Attack" and "ATK" keys
    :postcondition: rolls a random number between [0.0, 1.0), if it's less than 0.2, the enemy will deal damage equal
                    to Basic Attack multiplied by their attack
    :postcondition: prints a message indicating how much damage the enemy deal and a safe escape message
    :postcondition: enemy argument is not changed
    """

    randomizer = random.random()
    if randomizer < 0.20:
        character["Current HP"] -= enemy["Basic Attack"] * enemy["ATK"]
        if character["Current HP"] < 0:
            character["Current HP"] = 0
        print(
            f"The enemy struck you as you ran! \
You lost {enemy['Basic Attack'] * enemy['ATK']} \
HP, your HP is now {character['Current HP']}/{character['Max HP']}.\n")
    else:
        print(f"You got away safely! Your HP is {character['Current HP']}/{character['Max HP']}\n")


def enemy_flee(enemy: dict) -> bool:
    """
    Random roll that hits 20% of the time to determines whether the enemy will run away.

    :param enemy: a dictionary
    :precondition: enemy argument must be a dictionary with "Rank" key
    :postcondition: rolls a random number between [0.0, 1.0), if it's less than 0.2 and they enemy is not a boss,
                    they flee and True is returned Otherwise, combat persists and return False
    :return: a boolean value, True or False
    """

    randomizer = random.random()

    if randomizer < 0.2 and enemy['Rank'] != "Boss":
        print("The enemy fled!")
        game_pause(1)
        return True
    else:
        return False


def post_combat(character: dict, class_info: dict, enemy: dict) -> None:
    """
    Triggers character EXP gain and initiates the level_up function.

    :param character: a dictionary
    :param class_info: a dictionary
    :param enemy: a dictionary
    :precondition: character argument must be a dictionary with "Current HP", "Max HP", and "Level" keys
    :precondition: class_info argument must be a dictionary with "EXP Level 2", "ATK Level 2", "HP Level 2", "Level Two"
                    "EXP Level 3", "ATK Level 3", "HP Level 3", and "Level 3" keys
    :precondition: enemy argument must be a dictionary with "Name" and "EXP Given" keys
    :postcondition: if enemy HP is less than or equal to zero, invokes the gain_exp function
    :postcondition: invokes the level-up function
    :postcondition: prints messages informing user of enemy defeat and current HP status

    >>> player = {"Level": 1, "EXP": 20, "EXP Breakpoint": 20, "ATK": 10, "Current HP": 100, "Max HP": 100,\
    "Class Level": "Year 1"}
    >>> class_information = {"EXP Level 2": 20, "ATK Level 2": 20, "HP Level 2": 200, "Level Two": "Year 2",\
    "EXP Level 3": 30, "ATK Level 3": 30, "HP Level 3": 300, "Level Three": "Year 3"}
    >>> enemy_info = {"Name": "Monster", "HP": 10, "EXP Given": 15}
    >>> post_combat(player, class_information, enemy_info)
    You are a now Level 2! Your Class Rank is Year 2.
    Your HP is 200/200, your Level is 2.

    >>> player = {"Level": 1, "EXP": 10, "EXP Breakpoint": 20, "ATK": 10, "Current HP": 100, "Max HP": 100,\
    "Class Level": "Year 1"}
    >>> class_information = {"EXP Level 2": 20, "ATK Level 2": 20, "HP Level 2": 200, "Level Two": "Year 2",\
    "EXP Level 3": 30, "ATK Level 3": 30, "HP Level 3": 300, "Level Three": "Year 3"}
    >>> enemy_info = {"Name": "Monster", "HP": 0, "EXP Given": 15}
    >>> post_combat(player, class_information, enemy_info)
    The enemy writhes in agony and vanishes. You defeated Monster!
    You gained 15 EXP, you have 25/20 EXP.
    <BLANKLINE>
    You are a now Level 2! Your Class Rank is Year 2.
    Your HP is 200/200, your Level is 2.

    """

    if enemy["HP"] <= 0:
        print(f"The enemy writhes in agony and vanishes. You defeated {enemy['Name']}!")
        gain_exp(character, class_info, enemy)
    level_up(character, class_info)
    print(f"Your HP is {character['Current HP']}/{character['Max HP']}, your Level is {character['Level']}.")

    game_pause(2)


def combat(character: dict, class_info: dict, enemy: dict) -> None:
    """
    Drives the combat system.

    :param character: a dictionary
    :param class_info: a dictionary
    :param enemy: a dictionary
    :precondition: character argument must be a dictionary that contains "Name", "Level", "EXP", "EXP Breakpoint"
                    "Class", "Class Level", "Basic Attack", "Max HP", "Current HP", "ATK" keys
    :precondition: class_info argument must be a dictionary that contains "Class Name", "Level One", "Level Two"
                    "Level Three", "Special Attack Name", "Special Attack", "Accuracy", "EXP Level 2", "EXP Level 3"
                    "ATK Level 1", "ATK Level 2", "ATK Level 3", "HP Level 2", "HP Level 3"
    :precondition: enemy argument must be a dictionary that contains "Name", "Rank", "HP", "Max HP", "Level", "ATK"
                    "Basic Attack", "Special Attack", "Special Attack Name", "EXP Given","Encounter Quote"
                    "Basic Attack Quote", "Special Attack Quote", "Victory Quote", "Death Quote"
    :postcondition: while the character and enemy is alive and has not fled, the user and enemy will engage in combat
    """

    print(f"You encountered {enemy['Name']} (Level {enemy['Level']}), it prepares to attack!")
    enemy_escaped = False
    while character["Current HP"] > 0 and enemy["HP"] > 0 and enemy_escaped is False:
        user_choice = user_combat_turn(class_info)
        accuracy = combat_accuracy(class_info)
        if user_choice == "1":
            user_combat_basic(character, enemy)
        elif user_choice == "2":
            if accuracy:
                user_combat_special(character, class_info, enemy)
            else:
                print("You missed!")
        elif user_choice == "3":
            print("You blocked the enemy's attack.")
            enemy_escaped = enemy_flee(enemy)
            continue
        elif user_choice == "4":
            if enemy["Rank"] == "Boss":
                print("Can't run away!")
            else:
                escape_damage(character, enemy)
                break

        if enemy["HP"] > 0:
            enemy_escaped = enemy_flee(enemy)
        if enemy_escaped is False and enemy["HP"] > 0:
            enemy_combat_turn(character, enemy)

    if enemy["HP"] <= 0:
        print(f"{enemy['Name']}: {enemy['Death Quote']}\n")
    elif character["Current HP"] <= 0:
        print(f"{enemy['Name']}: {enemy['Victory Quote']}\n")
    post_combat(character, class_info, enemy)


def battle_odile(character: dict, class_info: dict, keys: dict) -> None:
    """
    Initiates combat with one of the game's sub-bosses, Odile.

    :param character: a dictionary
    :param class_info: a dictionary
    :param keys: a dictionary
    :precondition: character argument must be a dictionary that contains "Name", "Level", "EXP", "EXP Breakpoint"
                    "Class", "Class Level", "Basic Attack", "Max HP", "Current HP", "ATK" keys
    :precondition: class_info argument must be a dictionary that contains "Class Name", "Level One", "Level Two"
                    "Level Three", "Special Attack Name", "Special Attack", "Accuracy", "EXP Level 2", "EXP Level 3"
                    "ATK Level 1", "ATK Level 2", "ATK Level 3", "HP Level 2", "HP Level 3"
    :precondition: keys argument must be a dictionary with "Odile Key" as a key
    :postcondition: prints an encounter quote then initiates battle with Odile, if her HP becomes less than or equal to
                    zero, set "Odile's Key" in the keys dictionary to True
    """

    odile = {
        "Name": "Odile, the Black Swan",
        "HP": 320,
        "Max HP": 320,
        "Level": 75,
        "Rank": "Boss",
        "ATK": 4,
        "Basic Attack": 3,
        "Special Attack": 6,
        "Special Attack Name": "Feather Strike",
        "EXP Given": 50,
        "Encounter Quote": "Odile: How about I dance the Black Swan? I shall make your final moment beautiful.\n",
        "Basic Attack Quote": "Odile: My feathers cut like blades.",
        "Special Attack Quote": "Odile: HA HA HA! DIE DIE DIE",
        "Victory Quote": "Odile: What are you going to do? Run home to mommy?",
        "Death Quote": "Odile: NO, THE HUMILIATION!"
    }

    print(odile["Encounter Quote"])
    combat(character, class_info, odile)

    if odile["HP"] <= 0:
        keys["Odile Key"] = True
        print("You obtained Odile's Key.\n")


def battle_mother(character: dict, class_info: dict, keys: dict) -> None:
    """
     Initiates combat with one of the game's sub-bosses, Norma Bates.

    :param character: a dictionary
    :param class_info: a dictionary
    :param keys: a dictionary
    :precondition: character argument must be a dictionary that contains "Name", "Level", "EXP", "EXP Breakpoint"
                    "Class", "Class Level", "Basic Attack", "Max HP", "Current HP", "ATK" keys
    :precondition: class_info argument must be a dictionary that contains "Class Name", "Level One", "Level Two"
                    "Level Three", "Special Attack Name", "Special Attack", "Accuracy", "EXP Level 2", "EXP Level 3"
                    "ATK Level 1", "ATK Level 2", "ATK Level 3", "HP Level 2", "HP Level 3"
    :precondition: keys argument must be a dictionary with "Mother Key" as a key
    :postcondition: prints an encounter quote then initiates battle with Norma Bates, if her HP becomes less than or
                    equal to zero, set "Mother Key" in the keys dictionary to True
    """

    mother = {
        "Name": "Norma Bates",
        "HP": 240,
        "Max HP": 240,
        "Level": 50,
        "Rank": "Boss",
        "ATK": 3,
        "Basic Attack": 2,
        "Special Attack": 6,
        "Special Attack Name": "Mother's Wrath",
        "EXP Given": 50,
        "Encounter Quote": "Mother: A boy's best friend is his mother.",
        "Basic Attack Quote": "Mother: Leave my boy alone!",
        "Special Attack Quote": "Mother: You wanna play with the big kids, honey, you gotta act like the big kids.",
        "Victory Quote": "Mother: It's sad, when a mother has to speak the words that condemn her own son.",
        "Death Quote": "Mother: NO, I WILL NOT HIDE IN THE FRUIT CELLAR!"
    }

    print(mother["Encounter Quote"])
    combat(character, class_info, mother)

    if mother["HP"] <= 0:
        keys["Mother Key"] = True
        print("You obtained Mother's Key.\n")


def battle_paul(character: dict, class_info: dict, keys: dict) -> None:
    """
     Initiates combat with one of the game's sub-bosses, Paul Allen.

    :param character: a dictionary
    :param class_info: a dictionary
    :param keys: a dictionary
    :precondition: character argument must be a dictionary that contains "Name", "Level", "EXP", "EXP Breakpoint"
                    "Class", "Class Level", "Basic Attack", "Max HP", "Current HP", "ATK" keys
    :precondition: class_info argument must be a dictionary that contains "Class Name", "Level One", "Level Two"
                    "Level Three", "Special Attack Name", "Special Attack", "Accuracy", "EXP Level 2", "EXP Level 3"
                    "ATK Level 1", "ATK Level 2", "ATK Level 3", "HP Level 2", "HP Level 3"
    :precondition: keys argument must be a dictionary with "Paul Key" as a key
    :postcondition: prints an encounter quote then initiates battle with Norma Bates, if his HP becomes less than or
                    equal to zero, set "Paul Key" in the keys dictionary to True
    """

    paul = {
        "Name": "Paul Allen",
        "HP": 250,
        "Max HP": 250,
        "Level": 50,
        "Rank": "Boss",
        "ATK": 4,
        "Basic Attack": 2,
        "Special Attack": 4,
        "Special Attack Name": "Brutal Punch",
        "EXP Given": 50,
        "Encounter Quote": "Paul Allen: Well, I could tell you... but then I'd have to kill ya.",
        "Basic Attack Quote": "Paul Allen: I went to Yale.",
        "Special Attack Quote": "Paul Allen: You're just my shadow.",
        "Victory Quote": "Paul Allen: This is why I get to handle the Fisher Account.",
        "Death Quote": "Paul Allen: Is that a rain coat?"
    }

    print(paul["Encounter Quote"])
    combat(character, class_info, paul)

    if paul["HP"] <= 0:
        keys["Paul Key"] = True
        print("You obtained Paul's Key.\n")


def battle_final_boss(character: dict, class_info: dict, valid_keys: bool, keys: dict) -> None:
    """
    Initiates combat with the game's final boss, Kozilek.

    :param character: a dictionary
    :param class_info: a dictionary
    :param valid_keys: a boolean value, True or False
    :param keys: a dictionary
    :precondition: character argument must be a dictionary that contains "Name", "Level", "EXP", "EXP Breakpoint"
                    "Class", "Class Level", "Basic Attack", "Max HP", "Current HP", "ATK" keys
    :precondition: class_info argument must be a dictionary that contains "Class Name", "Level One", "Level Two"
                    "Level Three", "Special Attack Name", "Special Attack", "Accuracy", "EXP Level 2", "EXP Level 3"
                    "ATK Level 1", "ATK Level 2", "ATK Level 3", "HP Level 2", "HP Level 3"
    :precondition: keys argument must be a dictionary with "Paul Key" as a key
    :postcondition: evaluates whether the character is Level 3 and has all the keys, invokes the final_boss_encounter
                    function then initiates combat with Kozilek.
    :postcondition: if character is not Level 3 and does not have all the keys, a message will be printed to tell the
                    user to come back later
    :postcondition" if Kozilek's HP is zero or less, the Final Boss key-value pair in the keys dictionary is set to True
    """

    final_boss = {
        "Name": "Kozilek, The Great Distortion",
        "HP": 1300,
        "Max HP": 1300,
        "Level": 100,
        "Rank": "Boss",
        "ATK": 8,
        "Basic Attack": 2,
        "Special Attack": 4,
        "Special Attack Name": "Consume the Meek",
        "EXP Given": 50,
        "Encounter Quote": "You shrivel as you feel something not of this world.\n",
        "Basic Attack Quote": "Kozilek strikes you with its sweeping tentacles.",
        "Special Attack Quote": "Kozilek distorts the space around you, crushing your body.",
        "Victory Quote": "Kozilek shatters your mind. Now all must witness the end.",
        "Death Quote": "Kozilek withers away and vanishes."
    }

    if character["Level"] == 3 and valid_keys:
        print(final_boss["Encounter Quote"])
        game_pause(2)
        print("You unlock the pharmacy doors and enter to claim your medicine... except you are faced with an endless\n"
              "sea of darkness. Shadows spill forth from the vast space in the room and the ground quakes. Ethereal\n"
              "tentacles erupt from the ground to grab you. You attempt to dodge them...\n")
        game_pause(3)
        final_boss_encounter(final_boss, character)
        combat(character, class_info, final_boss)
    if valid_keys is False:
        print("You don't have all the keys yet, come back later.")
    if character["Level"] < 3:
        print("You are not Level 3. Come back when you are stronger.")

    if final_boss["HP"] <= 0:
        keys["Final Boss"] = True


def encounter_boss(character: dict, class_info: dict, special_locations: dict, keys: dict, valid_keys: bool) -> None:
    """
    Evaluates whether the character coordinates match the bosses' locations and whether they dont have the bosses' key.

    :param character: a dictionary
    :param class_info: a dictionary
    :param special_locations: a dictionary
    :param keys: a dictionary
    :param valid_keys: a boolean value, True or False
    :precondition: character argument must be a dictionary that contains "Name", "Level", "EXP", "EXP Breakpoint"
                    "Class", "Class Level", "Basic Attack", "Max HP", "Current HP", "ATK" keys
    :precondition: class_info argument must be a dictionary that contains "Class Name", "Level One", "Level Two"
                    "Level Three", "Special Attack Name", "Special Attack", "Accuracy", "EXP Level 2", "EXP Level 3"
                    "ATK Level 1", "ATK Level 2", "ATK Level 3", "HP Level 2", "HP Level 3"
    :precondition: keys argument must be a dictionary with "Mother Key", "Paul Key", and "Odile Key" as a keys
    :precondition: special_locations argument is a dictionary with string keys and two integer tuples as values
    :postcondition: if character's coordinates match with Bates Motel's coordinates, invoke battle_mother if Mother Key
                    is False
    :postcondition: if character's coordinates match with Pierce & Pierce's coordinates, invoke battle_paul if Paul Key
                    is False
    :postcondition: if character's coordinates match with Lincoln Center's coordinates, invoke battle_odile if Odile Key
                    is False
    :postcondition: if character's coordinates match The Apothecary's coordinates, invoke battle_final_boss function
    """

    if (character['X-coordinate'], character["Y-coordinate"]) == \
            special_locations["Bates Motel"] and keys["Mother Key"] is False:
        battle_mother(character, class_info, keys)

    elif (character['X-coordinate'], character["Y-coordinate"]) == \
            special_locations["Pierce & Pierce"] and keys["Paul Key"] is False:
        battle_paul(character, class_info, keys)

    elif (character['X-coordinate'], character["Y-coordinate"]) == \
            special_locations["Lincoln Center"] and keys["Odile Key"] is False:
        battle_odile(character, class_info, keys)

    elif (character['X-coordinate'], character["Y-coordinate"]) == \
            special_locations["The Apothecary"]:
        battle_final_boss(character, class_info, valid_keys, keys)


def hp_regen(character: dict) -> None:
    """
    Regenerates 1% of character's Max HP then prints the status of the character's HP.

    :param character: a dictionary
    :precondition: character argument must be a dictionary with "Current HP" and "Max HP"
    :postcondition: if the character's HP is not equal to Max HP, add 1% of character's Max HP to their Current HP
    :postcondition: outputs print messages to update the character's HP status

    >>> player = {"Current HP": 90, "Max HP": 100}
    >>> hp_regen(player)
    You regenerated 1 HP.
    Your HP is now 91/100.
    <BLANKLINE>

    >>> player = {"Current HP": 100, "Max HP": 100}
    >>> hp_regen(player)

    """

    health_regained = int(round(character["Max HP"] * 0.01))

    if character["Current HP"] < character["Max HP"]:
        print(f"You regenerated {health_regained} HP.")
        character["Current HP"] += health_regained
        if character["Current HP"] >= character["Max HP"]:
            character["Current HP"] = character["Max HP"]
        print(f"Your HP is now {character['Current HP']}/{character['Max HP']}.\n")


def is_alive(character: dict) -> bool:
    """
    Evaluates whether the character's Current HP is greater than zero.

    :param character: a dictionary
    :precondition: character parameter is a dictionary with "Current HP" as a key
    :postcondition: checks if the character's current HP is greater than zero, return True if greater or False otherwise
    :postcondition: character argument is unchanged
    :return: a boolean value, True or False

    >>> player = {'Current HP': 5}
    >>> is_alive(player)
    True

    >>> player = {'Current HP': 0}
    >>> is_alive(player)
    False
    """

    if character["Current HP"] > 0:
        return True
    else:
        return False


def victory_sequence() -> None:
    """
    Prints the victory sequence once the player defeats the final boss.

    :postcondition: prints several lines of strings for narrative exposition
    """

    print("""
    The Cosmic Entity Kozilek and its servants have been vanquished. The shadows recede to the corners of the room, 
    brightening the room with a familiar white light. Once again, you are faced with four walls and silence. Your
    medicine sits atop the shelf in front of you.""")

    game_pause(12)

    print("""
    You read the prescription that Dr. Charles gave to you. Chlorpromazine... an exact match. Although you are unsure 
    what this medicine does, you swallow the pills without hesitation, hoping for it to cure your ailment.""")

    print(r"""
                 {_________}
                  )=======(
                 /         \
                | _________ |
                ||   _     ||
                ||  |_)    ||
                ||  | \/   ||
          __    ||    /\   ||
     __  (_|)   |'---------'|
    (_|)        `-.........-'""")

    game_pause(10)

    print("""
    As you unclench the medicine bottle from your hands, you turn it around to read the other side of the label.
    This name is more familiar... Thorazine, a common drug used to treat psychotic disorders such as schizophrenia.""")

    game_pause(8)

    print("""
    The room no longer looks a sterile white. Instead, the pharmacy appears to be run down and abandoned. The walls are 
    painted a bright red color. You look down to see your hands stained with blood. Behind you, a trail of red paints 
    the path you've taken. Reality looks dull and filthy.""")

    game_pause(10)

    print("""
    The room no longer looks a sterile white. Instead, the pharmacy appears to be run down and abandoned. The walls are 
    painted a bright red color. You look down to see your hands stained with blood. Behind you, a trail of red paints 
    the path you've taken to reach the pharmacy. The streets are littered with the corpses of your victims. 
    Reality looks dull and filthy.""")

    game_pause(10)

    print("""
    You hear sirens in the distance echoing through the streets. Perhaps Hell will treat you better than reality.""")

    game_pause(5)

    print("""
    THE END""")


def game():
    """
     Drive the main game loop.
    """

    rows = 25
    columns = 25
    special_locations = special_coordinates()
    board = make_board(rows, columns, special_locations)
    character = make_character()
    get_name(character)
    class_info = choose_class()
    initiate_stats(character, class_info)
    play_game_intro = play_intro()
    if play_game_intro:
        game_intro(character)
    keys = make_keys()
    final_boss_dead = False

    while is_alive(character) and not final_boss_dead:
        draw_map(character, rows, columns, special_locations)
        describe_current_location(board, character)
        hp_regen(character)
        command = ""
        while command not in ("1", "2", "3", "4"):
            command = get_user_choice()
            menu(character, class_info, command, keys)
        valid_move = validate_move(board, character, command)
        if valid_move:
            move_character(character, command)
            there_is_a_boss = check_for_boss(character, special_locations)

            if there_is_a_boss:
                valid_keys = validate_keys(keys)
                encounter_boss(character, class_info, special_locations, keys, valid_keys)
                if keys["Final Boss"]:
                    break
                else:
                    continue

            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                enemy = make_enemy(character)
                combat(character, class_info, enemy)
        else:
            print("You can't go that way!")
        if character["Current HP"] <= 0:
            break

    if character["Current HP"] <= 0:
        print("Sorry, you died a slow, painful, gruesome death. There's no respite for the weak.")
    else:
        victory_sequence()


def main():
    """
    Drive the program.
    """

    game()


if __name__ == "__main__":
    main()
