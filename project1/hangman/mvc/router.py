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
from os import path as os_path

from flask import Flask, render_template, redirect, url_for, send_from_directory

def router(app: Flask):

    @app.route('/')
    def index():
        return render_template('index.html')

    # @app.route("/favicon.ico")
    # def favicon():
    #     """ 
    #         Route will serve the browser tab icon
    #     """

    #     # return(redirect(url_for("static", filename="favicon.ico")))
    #     return send_from_directory(
    #         os_path.join(app.root_path, 'mvc', 'view', 'build'), 
    #         'favicon.ico', 
    #         mimetype = 'image/vnd.microsoft.icon'
    #     )

    # @app.route('/manifest.json')
    # def manifest():
    #     return send_from_directory(
    #         os_path.join(app.root_path, 'mvc', 'view', 'build'), 
    #         'manifest.json', 
    #         mimetype = 'application/json'
    #     )

    # @app.route('/logo192.png')
    # def logo192():
    #     print('hello from logo192')
    #     print(f'root: {app.root_path}')
    #     location = os_path.join(app.root_path, 'mvc', 'view', 'build') 
    #     print(f'location: {location}')
    #     return send_from_directory(
    #         location,
    #         'logo192.png', 
    #         mimetype = 'image/png'
    #     )

    @app.route('/static/<path:path>') 
    def serve_file(path): 


        file_name = path.split('/')[-1]
        dir_end = '/'.join(['static', *path.split('/')[:-1]])
        dir_name = os_path.join(app.static_folder, dir_end)

        return send_from_directory(dir_name, file_name)

    @app.route('/<path:path>')
    def serve_public_file(path):
        file_name = path.split('/')[-1]
        dir_end = '/'.join(path.split('/')[:-1])
        dir_name = os_path.join(app.static_folder, dir_end)

        return send_from_directory(dir_name, file_name)


    # @app.route('/game') 
    # def game():
    #     return render_template('game.html')

    # @app.route('/game/<int:game_id>')
    # def game_id(game_id):
    #     return render_template('game.html')

    # @app.route('/game/<int:game_id>/guess', methods=['POST'])
    # def guess(game_id):
    #     return render_template('game.html')