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

import utils


class Game():
    def __init__(self, name: str, word: str, wins: int, losses: int, score: int, guesses: int, history_file: str):
        utils.validate_game_input(name, word, wins, losses, score, guesses, history_file),
        
        self.name = name
        self.word = word
        self.wins = wins
        self.losses = losses
        self.score = score
        self.guesses = guesses
        self.file = history_file