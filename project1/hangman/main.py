'''
    Assignment - Project 1: Hangman
    File: main.py
    Description: This program will launch the hangman game
    James Halladay
    Advanced Programming with Python
    Date: 8/29/2022


    *******************************************************************************
        Here we are building a hangman game.  The game will use a MVC design pattern 
            where the model is in ./game.py, the view is in ./display.py, and the controller
            is in ./controller.py.
    *******************************************************************************
'''

from utils.import_path import *

from hangman.mvc.model import Model
from hangman.mvc.controller import Controller

from hangman.utils.constants import (
    DB_NAME,
    DEFAULT_DIFFICULTY, 
    DEFAULT_LOSSES,
    DEFAULT_MAX_SCORE,
    DEFAULT_PLAYER_NAME,
    DEFAULT_WINS
)


def main():
    model = Model(
        DEFAULT_PLAYER_NAME,
        DB_NAME,
        DEFAULT_WINS,
        DEFAULT_LOSSES,
        difficulty = DEFAULT_DIFFICULTY
    )
    controller = Controller(__name__, model)
    controller.run()


if __name__ == "__main__":
    main()