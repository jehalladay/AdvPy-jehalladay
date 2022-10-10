'''
    Assignment - Project 1: Hangman
    File: test_model.py
    Description: This program will run tests on game.py
    James Halladay
    Advanced Programming with Python
    Date: 8/29/2022

    *******************************************************************************
        Here we use the pytest framework to test the game.py file.  
        We will test the following:
            - Constructor
            - Database Handling
            - Word Generation

        To run tests, execute pytest in the terminal under the project1 directory
    *******************************************************************************
'''

import pytest

from ..mvc.model import Model

from ..utils.constants import (
    PLAYER_TABLE, 
    ColumnNames
)

from ..utils.database import (
    check_for_record, 
    connect_to_db
)

from .constants import (
    ALPHABET,
    SAMPLE_DB_NAMES,
    SAMPLE_GUESS_WORDS,
    SAMPLE_PLAYER_NAMES
)



def test_model_constructor():
    '''
        Test the constructor of the Game class
    '''
    wins, losses = 1, 2
    max_score, difficulty = 7, 9

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wins, 
        losses,
        difficulty = difficulty
    )
    
    assert model.name == SAMPLE_PLAYER_NAMES[0]
    assert model.db_name == SAMPLE_DB_NAMES[0]
    assert model.wins == wins
    assert model.losses == losses
    assert model.difficulty == difficulty


def test_model_db_save():
    '''
        Test the successful saving of a game to the database
    '''
    wins, losses = 1, 2
    difficulty = 9

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wins, 
        losses,
        difficulty = difficulty
    )
    
    model.initialize_db()
    model.save_game()

    assert check_for_record(
        connect_to_db(model.db_name),
        PLAYER_TABLE,
        ColumnNames.NAME,
        model.name
    )


def test_model_db_save_and_load():
    '''
        Test the successful saving and loading of a game from the database
    '''
    right_wins, right_losses = 1, 2
    wrong_wins, wrong_losses = 3, 4
    difficulty = 9

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        right_wins, 
        right_losses,
        difficulty = difficulty
    )
    
    model.initialize_db()
    model.save_game()
    
    model.wins = wrong_wins
    model.losses = wrong_losses

    loaded = model.load_game(model.name)

    assert model.name == SAMPLE_PLAYER_NAMES[0]
    assert model.wins == right_wins
    assert model.losses == right_losses
    assert loaded[0]
    assert loaded[1] == f'Welcome back {SAMPLE_PLAYER_NAMES[0]}! Your wins: {model.wins} and losses: {model.losses}'


def test_model_db_save_and_reload():
    '''
        Test the successful saving of a game and reloading from a different game
    '''
    right_wins, right_losses = 1, 2
    wrong_wins, wrong_losses = 3, 4
    difficulty = 9

    model_1 = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        right_wins, 
        right_losses,
        difficulty = difficulty
    )
    
    model_1.initialize_db()
    model_1.save_game()
    
    model_2 = Model(
        SAMPLE_PLAYER_NAMES[1],
        SAMPLE_DB_NAMES[0],
        wrong_wins,
        wrong_losses,
        difficulty = difficulty
    )

    loaded = model_2.load_game(SAMPLE_PLAYER_NAMES[0])

    assert model_2.name == model_1.name
    assert model_2.wins == right_wins
    assert model_2.losses == right_losses
    assert loaded[0]
    assert loaded[1] == f'Welcome back {SAMPLE_PLAYER_NAMES[0]}! Your wins: {model_2.wins} and losses: {model_2.losses}'


def test_model_db_no_record():
    '''
        Test that load_game doesn't crash if there is no record in the database 
    '''
    right_wins, right_losses = 1, 2
    wrong_wins, wrong_losses = 3, 4
    difficulty = 9

    model = Model(
        SAMPLE_PLAYER_NAMES[2], 
        SAMPLE_DB_NAMES[0],
        right_wins, 
        right_losses,
        difficulty = difficulty
    )
    
    model.initialize_db()

    model.wins = wrong_wins
    model.losses = wrong_losses

    loaded = model.load_game(model.name)

    assert model.wins == wrong_wins
    assert model.losses == wrong_losses
    assert not loaded[0]
    assert loaded[1] == f'No record found for {SAMPLE_PLAYER_NAMES[2]}, please try again'


def test_get_word():
    '''
        Test that the get_word method returns the correct word
    '''
    wins, losses = 0, 0
    difficulty = 9

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wins, 
        losses,
        difficulty = difficulty
    )

    for i in range(10):
        model.new_word(i+1)
        assert len(model.word) == i+1


def test_new_player():
    '''
        Test that the new_player method creates a new player
    '''
    right_wins, right_losses = 0, 0
    wrong_wins, wrong_losses = 1, 2
    difficulty = 9

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wrong_wins, 
        wrong_losses,
        difficulty = difficulty
    )

    model.new_player(SAMPLE_PLAYER_NAMES[1])
    assert model.name == SAMPLE_PLAYER_NAMES[1]
    assert model.wins == right_wins
    assert model.losses == right_losses


def test_new_game():
    '''
        Test that the new_game method creates a new game
    '''

    right_wins, right_losses = 1, 3
    wrong_wins, wrong_losses = 1, 2
    difficulty = 9

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wrong_wins, 
        wrong_losses,
        difficulty = difficulty
    )

    model.new_game()
    
    assert model.letters == []
    assert model.wins == right_wins
    assert model.losses == right_losses
    assert model.difficulty == difficulty
    assert len(model.word) == difficulty


def test_new_game_with_difficulty():
    '''
        Test new game with different difficulty
    '''

    right_wins, right_losses, right_difficulty = 1, 3, 8
    wrong_wins, wrong_losses, wrong_difficulty = 1, 2, 9

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wrong_wins, 
        wrong_losses,
        difficulty = wrong_difficulty
    )

    model.new_game(difficulty = right_difficulty)
    
    assert model.letters == []
    assert model.wins == right_wins
    assert model.losses == right_losses
    assert model.difficulty == right_difficulty
    assert len(model.word) == right_difficulty


def test_model_current_guessed_word_with_correct_letters():
    '''
        Test that the current_guessed_word method returns the correct word
    '''
    wins, losses = 0, 0
    difficulty = 9

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wins, 
        losses,
        difficulty = difficulty
    )

    model.word = SAMPLE_GUESS_WORDS[0]
    model.letters = list(model.word)

    model.current_guessed_word()

    guessed_word = ''.join(model.guessed_word)

    assert guessed_word == model.word


def test_model_current_guessed_word_with_no_letters():
    '''
        Test that the current_guessed_word method returns the correct word
    '''
    wins, losses = 0, 0
    difficulty = len(SAMPLE_GUESS_WORDS[0])

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wins, 
        losses,
        difficulty = difficulty
    )

    model.word = SAMPLE_GUESS_WORDS[0]
    model.letters = []

    model.current_guessed_word()

    guessed_word = ''.join(model.guessed_word)

    assert guessed_word == '_' * difficulty


def test_model_current_guessed_word_with_all_incorrect_letters():
    '''
        Test that the current_guessed_word method returns the correct word
    '''
    wins, losses = 0, 0
    difficulty = len(SAMPLE_GUESS_WORDS[0])

    model = Model(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wins, 
        losses,
        difficulty = difficulty
    )

    model.word = SAMPLE_GUESS_WORDS[0]

    model.letters = [l for l in ALPHABET if l not in model.word]

    model.current_guessed_word()

    guessed_word = ''.join(model.guessed_word)
    # guessed_word = ''.join(model.letters)
    # guessed_word = ''.join(ALPHABET)

    assert guessed_word == '_' * difficulty