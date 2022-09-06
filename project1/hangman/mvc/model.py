'''
    Assignment - Project 1: Hangman
    File: game.py
    Description: This program will contain the hangman state
    James Halladay
    Advanced Programming with Python
    Date: 8/29/2022


    *******************************************************************************

    *******************************************************************************
'''


from json import load as load_json
from os import path
from random import randint

from hangman.utils.functions import validate_game_input

from hangman.utils.database import (
    check_for_record,
    connect_to_db,
    create_table,
    delete_record,
    insert_into_table
)

from hangman.utils.constants import (
    PLAYER_TABLE,
    PLAYER_TABLE_COLUMNS,
    PLAYER_TABLE_SCHEMA,
    UTILITY_DIR,
    WORD_FILE,
    WORD_LENGTH,
    ColumnNames
)


class Game():
    def __init__(self, name: str, db_name: str, wins: int, losses: int, max_score: int, difficulty: int = 5):
        validate_game_input(name, db_name, wins, losses, max_score, difficulty)

        self.name = name
        self.new_word(difficulty)
        self.guessed_word = ['_' for _ in range(len(self.word))]
        self.wins = wins
        self.losses = losses
        self.max_score = max_score
        self.difficulty = difficulty
        self.guesses = 0
        self.db_name = db_name
        self.letters = []


    def initialize_db(self):
        '''
            This function will initialize the database
        '''

        conn = connect_to_db(self.db_name)
        create_table(conn, PLAYER_TABLE, PLAYER_TABLE_COLUMNS, PLAYER_TABLE_SCHEMA)
        conn.close()


    def save_game(self):
        '''
        This function will save the game
        '''

        conn = connect_to_db(self.db_name)

        if check_for_record(conn, PLAYER_TABLE, ColumnNames.NAME, self.name):
            delete_record(conn, PLAYER_TABLE, ColumnNames.NAME, self.name)

        insert_into_table(
            conn, 
            PLAYER_TABLE, 
            PLAYER_TABLE_COLUMNS, 
            [
                self.name, 
                str(self.wins), 
                str(self.losses)
            ]
        )

        conn.close()


    def load_game(self, name: str):
        '''
            This function will load the wins and losses of the player
        '''

        conn = connect_to_db(self.db_name)
        
        if check_for_record(conn, PLAYER_TABLE, ColumnNames.NAME, name):
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {PLAYER_TABLE} WHERE Name = ?', (name,))
            conn.commit()

            result = cursor.fetchone()
            
            self.name = name
            self.wins = result[1]
            self.losses = result[2]
            self.score = 0
            self.guesses = 0

            status = True
            message = f'Welcome back {name}! Your wins: {self.wins} and losses: {self.losses}'

        else:
            status = False
            message = f'No record found for {name}, please try again'

        conn.close()

        return (status, message)


    def new_word(self, length: int):
        '''
            This function will start a new word
        '''
        
        location = path.join(
            path.dirname(path.abspath(__file__)),
            '..',
            UTILITY_DIR,
            WORD_FILE
        )

        with open(location) as f:
            words = load_json(f)[WORD_LENGTH][str(length)]

        min, max = 0, len(words) - 1
        index = randint(min, max)

        self.word = words[index]


    def new_game(self, difficulty: int or None = None, max_score: int or None = None):
        '''
            This function will start a new game
        '''

        if self.word != self.guessed_word:
            self.losses += 1
        else:   
            self.wins += 1

        if difficulty is not None:
            self.difficulty = difficulty

        if max_score is not None:
            self.max_score = max_score

        self.new_word(self.difficulty)
        self.guessed_word = ['_' for _ in range(len(self.word))]
        
        self.guesses = 0
        self.letters = []


    def new_player(self, name: str):
        '''
            This function will start a new player
        '''

        conn = connect_to_db(self.db_name)
        
        if check_for_record(conn, PLAYER_TABLE, ColumnNames.NAME, name):
            status = False
            message = f'Player {name} already exists, please try again'
                
        else:
            self.name = name
            self.word = self.new_word(5)

            self.wins = 0
            self.losses = 0
            self.max_score = 7
            self.guesses = 0

            status = True
            message = f'Welcome {name}!'

        conn.close()

        return (status, message)



if __name__ == "__main__":
    print("This file is not meant to be run directly.")