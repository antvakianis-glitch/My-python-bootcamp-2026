# Tic Tac Toe (Command Line)

A text-based Tic Tac Toe game built in Python as part of the
100 Days of Code bootcamp (Day 84).

## Features
- Play as X or O against the computer
- X always moves first, so choosing O lets the computer start
- Input validation (only numbers 1-9, taken spots are rejected)
- Detects wins and draws
- Option to play again after each game

## Requirements
Python 3. No extra packages needed.

## How to run
In a terminal, run:

    python main.py

Choose X or O, then pick a position from 1 to 9:

    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9

## How it works
- The board is a list of 9 spaces.
- `WINNING_LINES` holds all 8 winning combinations.
- `get_move` handles the human player.
- `computer_move` picks a random free spot.

## Possible improvements
- Smarter computer that wins and blocks
- Two-player mode
- A graphical version with tkinter