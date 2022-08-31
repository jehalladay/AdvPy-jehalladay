'''
Assignment - Project 1: Hangman
File: test_game.py
Description: This program will run tests on game.py
James Halladay
Advanced Programming with Python
Date: 8/29/2022


*******************************************************************************

*******************************************************************************
'''

import pytest

from game import Game

def test_game_constructor():
    game = Game("Test", "Test")
    assert game.name == "Test"
    assert game.word == "Test"