'''
Assignment - Project 1: Hangman
File: test_game.py
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

from ..MVC.game import Game

from ..utils.constants import (
    PLAYER_TABLE, 
    ColumnNames
)

from ..utils.database import (
    check_for_record, 
    connect_to_db
)

from .constants import (
    SAMPLE_DB_NAMES,
    SAMPLE_PLAYER_NAMES
)



def test_game_constructor():
    '''
        Test the constructor of the Game class
    '''
    wins, losses = 1, 2

    game = Game(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        wins, 
        losses
    )
    
    assert game.name == SAMPLE_PLAYER_NAMES[0]
    assert game.db_name == SAMPLE_DB_NAMES[0]
    assert game.wins == wins
    assert game.losses == losses


def test_game_db_save():
    '''
        Test the successful saving of a game to the database
    '''
    right_wins, right_losses = 1, 2
    wrong_wins, wrong_losses = 3, 4

    game = Game(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        right_wins, 
        right_losses
    )
    
    game.initialize_db()
    game.save_game()

    assert check_for_record(
        connect_to_db(game.db_name),
        PLAYER_TABLE,
        ColumnNames.NAME,
        game.name
    )


def test_game_db_save_and_load():
    '''
        Test the successful saving and loading of a game from the database
    '''
    right_wins, right_losses = 1, 2
    wrong_wins, wrong_losses = 3, 4

    game = Game(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        right_wins, 
        right_losses
    )
    
    game.initialize_db()
    game.save_game()
    
    game.wins = wrong_wins
    game.losses = wrong_losses

    game.load_game(game.name)

    assert game.wins == right_wins
    assert game.losses == right_losses


def test_game_db_save_and_reload():
    '''
        Test the successful saving of a game and reloading from a different game
    '''
    right_wins, right_losses = 1, 2
    wrong_wins, wrong_losses = 3, 4

    game_1 = Game(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        right_wins, 
        right_losses
    )
    
    game_1.initialize_db()
    game_1.save_game()
    
    game_2 = Game(
        SAMPLE_PLAYER_NAMES[1],
        SAMPLE_DB_NAMES[0],
        wrong_wins,
        wrong_losses
    )

    game_2.load_game(SAMPLE_PLAYER_NAMES[0])

    assert game_2.name == game_1.name
    assert game_2.wins == right_wins
    assert game_2.losses == right_losses


def test_game_db_no_record():
    '''
        Test that load_game doesn't crash if there is no record in the database
    '''
    right_wins, right_losses = 1, 2
    wrong_wins, wrong_losses = 3, 4

    game = Game(
        SAMPLE_PLAYER_NAMES[2], 
        SAMPLE_DB_NAMES[0],
        right_wins, 
        right_losses
    )
    
    game.initialize_db()

    game.wins = wrong_wins
    game.losses = wrong_losses

    game.load_game(game.name)

    assert game.wins == wrong_wins
    assert game.losses == wrong_losses


def test_get_word():
    '''
        Test that the get_word method returns the correct word
    '''
    game = Game(
        SAMPLE_PLAYER_NAMES[0], 
        SAMPLE_DB_NAMES[0],
        0, 
        0
    )

    for i in range(10):
        game.new_word(i+1)
        assert len(game.word) == i+1


