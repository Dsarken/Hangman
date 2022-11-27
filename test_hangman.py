import pytest
from hangman import *


def test_win_loss_tracker():
    assert win_loss_tracker("win") == 1
    assert win_loss_tracker("loss") == 1


def test_hangman_pieces():
    assert hangman_pieces(6) == """
             _______
            |/      |
            |
            |
            |
            |
            |
        jgs_|___
        """
    assert hangman_pieces(5) == """
             _______
            |/      |
            |       |
            |
            |
            |
            |
        jgs_|___
        """
    assert hangman_pieces(4) == """
             _______
            |/      |
            |       |
            |      (_)
            |
            |
            |
        jgs_|___
        """
    assert hangman_pieces(3) == """
             _______
            |/      |
            |       |
            |      (_)
            |      \|/
            |
            |
        jgs_|___
        """
    assert hangman_pieces(2) == """
             _______
            |/      |
            |       |
            |      (_)
            |      \|/
            |       |
            |
        jgs_|___
        """
    assert hangman_pieces(1) == """
             _______
            |/      |
            |       |
            |      (_)
            |      \|/
            |       |
            |      / \\
        jgs_|___
        """


def test_word_list_difficulty():
    length_3_to_5 = word_list_choice(1)
    length_6_to_8 = word_list_choice(2)
    length_10_to_12 = word_list_choice(3)
    length_15_to_20 = word_list_choice(4)
    assert 3 <= len(length_3_to_5) <= 5
    assert 6 <= len(length_6_to_8) <= 8
    assert 10 <= len(length_10_to_12) <= 12
    assert 15 <= len(length_15_to_20) <= 20
