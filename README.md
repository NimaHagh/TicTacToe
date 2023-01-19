# Tic Tac Toe AI

This is a Tic Tac Toe program that utilizes the MinMax algorithm to determine the optimal moves for the game. This program was developed as an assignment for the CS50's Introduction to Artificial Intelligence with Python course at Harvard University.

# Getting Started

To run the program, you will need to have Python 3 installed on your computer. You can download it from the official website: https://www.python.org/downloads/

The program includes several functions that work together to play the game of Tic Tac Toe. The initial_state function returns the starting state of the board, where all cells are set to EMPTY. The player function takes the current board state as input and returns which player's turn it is, either X or O. In the initial game state, X gets the first move, and the player alternates with each additional move.

The actions function returns a set of all possible actions that can be taken on a given board. Each action is represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2). The result function takes a board and an action as input and returns a new board state without modifying the original board.

The winner function accepts a board as input, and returns the winner of the board if there is one. The terminal function accepts a board as input and returns a boolean value indicating whether the game is over. The utility function accepts a terminal board as input and outputs the utility of the board.

The minimax function takes a board as input and returns the optimal move for the player to move on that board. For all functions that accept a board as input, it is assumed to be a valid board (namely, it is a list that contains three rows, each with three values of either X, O, or EMPTY). The order and number of arguments to each function should not be modified.

# Acknowledgments
- CS50's Introduction to Artificial Intelligence with Python course at Harvard University
- Inspiration: Tic Tac Toe Game
