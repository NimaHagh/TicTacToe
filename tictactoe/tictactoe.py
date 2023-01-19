"""
Tic Tac Toe Player
"""

from asyncio.windows_events import NULL
import math
from queue import Empty

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


"""
As X always go first we check if cunt x == count o, 
 Returns player who has the next turn on a board.
"""


def player(board):
    Xcounter = 0  # a counter for x
    Ocounter = 0  # a counter for o

    # Looking thorugh the 2d array
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == X:
                Xcounter = Xcounter+1
            elif board[i][j] == O:
                Ocounter = Ocounter+1
    if Xcounter == Ocounter:  # if count x is eq to count O it is x players turn
        return X
    else:
        return O


"""
    Returns set of all possible actions (i, j) available on the board.
"""


def actions(board):
    PosMoves = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                PosMoves.add((i, j))
    return PosMoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    (i, j) = action
    # check if action is whitin the board
    if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
        raise IndexError()  # if not raise and index error

    newBoard = [x[:] for x in board]  # deep copy format
    newBoard[i][j] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == O or winner(board) == X:
        return True
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == O:
        return -1
    elif winner(board) == X:
        return 1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board)==True: # if the game is over return nothing
        return None

    elif (terminal(board)==False):     # if the game isnt over use the max and min values functions to make a move 
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

    else:             # an else statement that does nothing
        return NULL



def max_value(board):

    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    best_move = None
    for action in actions(board):
        hypothetical_value = min_value(result(board, action))[0]
        if hypothetical_value > v:
            v = hypothetical_value
            best_move = action
    return [v, best_move]


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
