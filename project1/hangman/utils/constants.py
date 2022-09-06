'''
    Assignment - Project 1: Hangman
    File: constants.py
    Description: This file contains all of the constants used in the game
    James Halladay
    Advanced Programming with Python
    Date: 8/29/2022


    *******************************************************************************

    *******************************************************************************
'''

# database constants

DB_NAME = "hangman.db"

PLAYER_TABLE = "Players"

class ColumnNames():
    '''
    This class contains the column names for the player table
    '''
    NAME = 'Name'
    WINS = 'Wins'
    LOSSES = 'Losses'


PLAYER_TABLE_COLUMNS = [
    'Name', 
    'Wins', 
    'Losses'
]

PLAYER_TABLE_SCHEMA = [
    'TEXT',
    'INTEGER',
    'INTEGER'
]

# file constants

UTILITY_DIR = 'utils'

WORD_FILE = 'words.json'

# game constants

DEFAULT_PLAYER_NAME = 'player'

DEFAULT_WINS = 0

DEFAULT_LOSSES = 0

DEFAULT_MAX_SCORE = 7

DEFAULT_DIFFICULTY = 5

# menu constants

WELCOME_MESSAGE = '''
Welcome to Hangman!
'''


OPTION_POS = 0

OPTION_DESC = 1

PLAY = (
    'a',
    'Play a new game'
)

QUIT = (
    'b',
    'Quit the game'
)

STATUS = (
    'c',
    'Display status of the current player'
)

CREATE = (
    'd',
    'Create a new player'
)

# word constants

WORD_LENGTH = 'word_length'
