'''
    Assignment - Project 1: Hangman
    File: test_words.py
    Description: This program will run tests on words.json
    James Halladay
    Advanced Programming with Python
    Date: 8/29/2022

    *******************************************************************************
        We will test the length of the words in words.json using pytest
    *******************************************************************************
'''

from json import load as load_json
from os import path

from hangman.utils.constants import (
    UTILITY_DIR,
    WORD_FILE,
    WORD_LENGTH
)
        

def test_word_length():
    '''
        Test the length of the words used for game
    '''
    
    location = path.join(
        path.dirname(path.abspath(__file__)),
        '..',
        UTILITY_DIR,
        WORD_FILE
    )

    with open(location) as f:
        word_set = load_json(f)[WORD_LENGTH]

    for length in word_set:
        words = word_set[length]
        assert len(word_set) == 10
        assert len(word_set[length]) > 0

        for word in words:
            assert len(word) == int(length)

