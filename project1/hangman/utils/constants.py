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

from typing import (
    Any,
    Dict,
    List,
    Tuple,
)

from enum import Enum

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

# Model constants

DEFAULT_PLAYER_NAME = 'player'

DEFAULT_WINS = 0

DEFAULT_LOSSES = 0

DEFAULT_MAX_SCORE = 7

DEFAULT_DIFFICULTY = 5

Result = Tuple[bool, str]

# word constants

WORD_LENGTH = 'word_length'


# graphql constants

Field = str
Message = str or bool

class ResponseField(Enum):
    '''
        This class contains the response field names
    '''
    
    data       : Field = 'data'
    errors     : Field = 'errors'
    success    : Field = 'success'
    state      : Field = 'state'
    time       : Field = 'time'
    method     : Field = 'method'
    input      : Field = 'input'
    name       : Field = 'name'
    wins       : Field = 'wins'
    losses     : Field = 'losses'
    missed     : Field = 'missed'
    message    : Field = 'message'
    word       : Field = 'word'
    guessedWord: Field = 'guessedWord'

Response = Dict[ResponseField, Any]


class MenuItems(Enum):
    '''
        This class contains the menu item names
    '''

    PLAY_GAME = 'play'
    QUIT_GAME = 'quit'
    NEW_PLAYER = 'new'


class GameStates(Enum):
    '''
        This class contains the different 
    '''

    PLAYING = 'playing'
    WIN = 'win'
    LOSE = 'lose'