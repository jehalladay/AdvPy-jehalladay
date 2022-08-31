import pytest

from game import Game

def test_game_constructor():
    game = Game("Test", "Test")
    assert game.name == "Test"
    assert game.word == "Test"