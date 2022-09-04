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

from MVC.game import Game
from MVC.display import Display
from MVC.controller import Controller


def main():
    game = Game()
    display = Display()
    controller = Controller(game, display)
    controller.run()


if __name__ == "__main__":
    main()