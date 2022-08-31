'''
Assignment - Project 1: Hangman
File: utils.py
Description: This file contains all of the utility functions used in the game
James Halladay
Advanced Programming with Python
Date: 8/29/2022


*******************************************************************************

*******************************************************************************
'''

import os, sys


def validate_type(value: any, type: any) -> bool:
    '''
    This function will validate the type of a value
    '''
    return isinstance(value, type)

def validate_type_message(messages: list, value: any, type: any, message: str) -> list:
    '''
    This function will validate the type of a value
    '''

    if not isinstance(value, type):
        messages.append(message)

    return messages


def validate_game_input(name: str, word: str, wins: int, losses: int, score: int, guesses: int, history_file: str) -> None:
    '''
    This function will validate the game input
    '''
    messages = []


    # Validate types
    messages = validate_type_message(messages, name, str, "Name must be a string")
    messages = validate_type_message(messages, word, str, "Word must be a string")
    messages = validate_type_message(messages, wins, int, "Wins must be an integer")
    messages = validate_type_message(messages, losses, int, "Losses must be an integer")
    messages = validate_type_message(messages, score, int, "Score must be an integer")
    messages = validate_type_message(messages, guesses, int, "Guesses must be an integer")
    messages = validate_type_message(messages, history_file, str, "History file must be a string")
    
    # Validate values
    if name == '' or word == '':
        messages.append("Name and word cannot be empty")
    if wins < 0 or losses < 0 or score < 0 or guesses < 0:
        messages.append("Wins, losses, score, and guesses cannot be negative")

    for m in messages:
        print(m, file=sys.stderr)

    assert(len(messages) == 0, "Invalid game input")