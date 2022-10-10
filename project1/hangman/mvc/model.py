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
from typing import Tuple

from hangman.utils.functions import (
    validate_model_input
)

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
    ColumnNames,
    GameStates,
    Result
)


class Model():
    def __init__(self, name: str, db_name: str, wins: int, losses: int, difficulty: int = 5):
        validate_model_input(name, db_name, wins, losses, difficulty)

        self.name = name
        self.new_word(difficulty)
        self.guessed_word: list = ['_' for _ in range(len(self.word))]
        self.wins = wins
        self.losses = losses
        self.difficulty = difficulty
        self.missed = 0
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
        This function will save the game after deleting any old records for the player
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


    def load_game(self, name: str) -> Result:
        '''
            This function will load the wins and losses of the player if they exist
        '''

        conn = connect_to_db(self.db_name)
        
        if check_for_record(conn, PLAYER_TABLE, ColumnNames.NAME, name):
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {PLAYER_TABLE} WHERE Name = ?', (name,))
            conn.commit()

            result = cursor.fetchone()
            
            self.name = name
            self.wins = int(result[1])
            self.losses = int(result[2])
            self.missed = 0

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


    def new_game(self, difficulty: int or None = None):
        '''
            This function will start a new game
        '''

        print(f'Word: {self.word.lower()}')
        print(f'Guessed Word: {"".join(self.guessed_word)}')
        print(self.word.lower() == ''.join(self.guessed_word))

        if self.word.lower() == ''.join(self.guessed_word):
            self.wins += 1
        else:   
            self.losses += 1

        if difficulty is not None:
            self.difficulty = difficulty

        self.new_word(self.difficulty)
        self.guessed_word = ['_' for _ in range(len(self.word))]
        
        self.missed = 0
        self.letters = []


    def new_player(self, name: str) -> Result:
        '''
            This function will start a new player
        '''

        conn = connect_to_db(self.db_name)
        
        if check_for_record(conn, PLAYER_TABLE, ColumnNames.NAME, name):
            status = False
            message = f'Player {name} already exists, please try again'
                
        else:
            self.name = name
            self.new_word(5)
            self.letters = []
            self.guessed_word = ['_' for _ in range(len(self.word))]

            self.wins = 0
            self.losses = 0
            self.missed = 0

            status = True
            message = f'Welcome {name}!'

        conn.close()

        return (status, message)


    def current_guessed_word(self):
        '''
            This function will change the current guessed_word based on the
                current letters guessed
        '''
        guessed_word = []
            
        for i in self.word.lower():
            if i in self.letters:
                guessed_word.append(i)
            else:
                guessed_word.append('_') 

        self.guessed_word = guessed_word


    def guess(self, char: str) -> bool:
        '''
            This function will guess a letter
        '''

        new_letter = True

        if char in self.letters:
            new_letter = False
        else:
            self.letters.append(char)
            if char not in self.word.lower():
                self.missed += 1

        self.current_guessed_word()

        return new_letter
        
    def can_guess(self) -> bool:
        '''
            This function will check if the player can guess again
        '''

        return self.missed < 6 and self.word.lower() != ''.join(self.guessed_word)

    
    def game_state(self) -> GameStates:
        '''
            This function will return the current game state
        '''

        if self.word.lower() == ''.join(self.guessed_word):
            return GameStates.WIN
        elif self.missed >= 6:
            return GameStates.LOSE
        else:
            return GameStates.PLAYING


if __name__ == "__main__":
    print("This file is not meant to be run directly.")