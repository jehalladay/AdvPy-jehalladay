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


def clear_screan() -> None:
    '''
    This function will clear the screen
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

    
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


def validate_game_input(name: str, db_name: str, wins: int, losses: int, difficulty: int) -> None:
    '''
        This function will validate the game input
            Invalid inputs will populate a list of error messages
            If the list is not empty, the messages ill print and the program will exit
    '''
    messages = []

    # Validate types
    messages = validate_type_message(messages, name, str, f"Name must be a string: {name}")
    messages = validate_type_message(messages, db_name, str, f"Db_name must be a string: {db_name}")
    messages = validate_type_message(messages, wins, int, f"Wins must be an integer: {wins}")
    messages = validate_type_message(messages, losses, int, f"Losses must be an integer: {losses}")
    messages = validate_type_message(messages, difficulty, int, f"Difficulty must be an integer: {difficulty}")

    # Validate values
    if name == '' or db_name == '':
        messages.append("Name and Db_name cannot be empty")
        messages.append(f"Name: {name}; Db_name: {db_name}")

    if wins < 0 or losses < 0:
        messages.append("Wins and losses cannot be negative")
        messages.append(f"Wins: {wins}, Losses: {losses}")

    if difficulty < 1 or difficulty > 10:
        messages.append("Difficulty must be between 1 and 10")
        messages.append(f"Difficulty: {difficulty}")

    for m in messages:
        print(m, file=sys.stderr)

    assert len(messages) == 0, "Invalid game input"

