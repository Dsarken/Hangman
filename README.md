# Hangman
    #### Video Demo:  https://youtu.be/uP2Y8z45Xq8
    #### Description:
    This is an implementation of the word game Hangman with some minor additional features:
    there are 4 difficulty levels: Easy, Medium, Hard, and Nightmare as the difficulty increases so does
    the length of the word that is randomly chosen.

    The player has 6 guesses and can either guess a single letter or guess the entire word correctly
    at once, the program also keeps track of the players wins and losses directly above the hangman symbol
    with every mistake another part of the body is added gradually and once the body is complete the game
    is over and counted as a loss, there are a total of 6 guesses.
    
    The program itself is composed of 4 functions: a main function, one to handle the tracking of wins
    and losses, one to return the proper state of the hangman given the number of guesses left, and finally
    one to choose the correct set of words given the difficulty input and return a randomly chosen word from 
    that set.
    
    #### How to run:
    To run the program simply type: python hangman.py
    once a game is finished and whether you have lost or won, if you wish to play again type either 'y'
    or 'n' and a new word will randomly be chosen of the same difficulty. If you wish to play again with
    a new difficulty of choice you must exit the program with Ctrl + C and retype the same command above to begin
    playing.
    
