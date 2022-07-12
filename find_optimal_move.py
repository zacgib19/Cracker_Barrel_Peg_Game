import pygame

# Keeps track of moves made
moves_made = []

# Keeps track of game states to later print out
optimal_path = []

legal_moves = [
    [0, 1, 3],
    [0, 2, 5],
    [1, 3, 6],
    [1, 4, 8],
    [2, 4, 7],
    [2, 5, 9],
    [3, 1, 0],
    [3, 4, 5],
    [3, 6, 10],
    [3, 7, 12],
    [4, 7, 11],
    [4, 8, 13],
    [5, 4, 3],
    [5, 8, 12],
    [5, 9, 14],
    [6, 3, 1],
    [6, 7, 8],
    [7, 4, 2],
    [7, 8, 9],
    [8, 4, 1],
    [8, 7, 6],
    [9, 5, 2],
    [9, 8, 7],
    [10, 6, 3],
    [10, 11, 12],
    [11, 7, 4],
    [11, 12, 13],
    [12, 7, 3],
    [12, 8, 5],
    [12, 11, 10],
    [12, 13, 14],
    [13, 8, 4],
    [13, 12, 11],
    [14, 9, 5],
    [14, 13, 12]
]


# If the move is blank in the first slot
# (since in the list of valid moves frontward and backwards are both covered)
# both (0, 1, 3) and (3, 1, 0) are in the list legal_moves
def can_move(move):
    return move[0] == 'e' and move[1] == 'f' and move.index(2) == 'f'


# Finds current available moves in game state
def valid_moves():
    filter(can_move(), legal_moves)


def undo():
    pass


# recursive function
def find_optimal_move():
    pass
