'''
    Assignment - Project 1: Hangman
    File: import_path.py
    Description: This program assures all files are reachable from pytest and main.py
    James Halladay
    Advanced Programming with Python
    Date: 8/29/2022
'''

import sys

from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[2]

sys.path.append(str(root))
