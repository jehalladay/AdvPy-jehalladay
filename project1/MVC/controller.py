'''
Assignment - Project 1: Hangman
File: controller.py
Description: This program will control the game and manages passing the game state
    to the view in display.py.
James Halladay
Advanced Programming with Python
Date: 8/29/2022


*******************************************************************************
Here we are building a hangman game.  The game will use a MVC design pattern 
    where the model is in ./game.py, the view is in ./display.py, and this file
    is the controller.




*******************************************************************************
'''

from .game import Game
from .display import Display

class Controller:
    def __init__(self, game: Game, display: Display):
        self.game = game
        self.display = display

    def run(self):
        while not self.game.is_over():
            self.display.draw(self.game)
            self.game.guess(input("Guess a letter: "))

        self.display.draw(self.game)