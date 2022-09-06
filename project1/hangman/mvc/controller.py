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

from flask import Flask
from os import path

from hangman.mvc.model import Game
from hangman.mvc.router import router

class Controller:
    def __init__(self, name: str, game: Game):

        self.game = game
        self.app = Flask(
            name, 
            template_folder = path.abspath('mvc/view/build'),
            static_folder = path.abspath('mvc/view/build')
        )

        router(self.app)

    def run(self):
        self.app.run(port = '4999', debug = True)


if __name__ == "__main__":
    print('This file is not meant to be run directly.')

