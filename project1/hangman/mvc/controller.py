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
import os

from flask import (
    Flask, 
    send_from_directory, 
    render_template
)

from hangman.mvc.model import Game

class Controller:
    def __init__(self, name: str, game: Game):

        self.game = game
        self.app = Flask(
            name, 
            template_folder = os.path.abspath('mvc/view/build'),
            static_folder = os.path.abspath('mvc/view/build')
        )

        @self.app.route('/')
        def index():

            return render_template('index.html')


        @self.app.route('/static/<path:path>') 
        def serve_file(path): 

            file_name = path.split('/')[-1]
            dir_end = '/'.join(['static', *path.split('/')[:-1]])
            dir_name = os.path.join(self.app.static_folder, dir_end)

            return send_from_directory(dir_name, file_name)


        @self.app.route('/<path:path>')
        def serve_public_file(path):

            file_name = path.split('/')[-1]
            dir_end = '/'.join(path.split('/')[:-1])
            dir_name = os.path.join(self.app.static_folder, dir_end)

            return send_from_directory(dir_name, file_name)


    def run(self):
        self.app.run(port = '4999', debug = True)


if __name__ == "__main__":
    print('This file is not meant to be run directly.')

