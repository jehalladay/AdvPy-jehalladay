'''
    Assignment - Project 2: Kattis
    File: import_path.py
    Description: This program assures all files are reachable from pytest and main.py
    James Halladay
    Advanced Programming with Python
    Date: 9/22/2022
'''

import sys

from pathlib import Path

file = Path(__file__).resolve()
root = file.parents[1]

sys.path.append(str(root))
