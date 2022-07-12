##############################################################################
# This is a game of tricky triangle (AKA the Cracker Barrel Peg Game)
# It solves a game in 13 moves and shows its progress with each click
# This essentially solves the game really quickly, and takes a 'snapshot' of
# each optimal game state
# Zach Gibby
##############################################################################

import pygame
import peg
from find_optimal_move import find_optimal_move
from pygame.locals import MOUSEBUTTONUP

global mouse_click
mouse_click = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)


# Surface definitions
screen = pygame.display.set_mode((600, 600))
board = pygame.image.load("pegboard.bmp").convert()


# Game definition
class Game:
    global mouse_click
    def __init__(self, fps):
        # initialize the pygame module
        pygame.init()

        self.fps = fps
        self.fps_clock = pygame.time.Clock()

        # create a surface on screen that has the size of 600 x 600
        self.screen = pygame.display.set_mode((600, 600))

    def play(self, pegs):
        # define a variable to control the main loop
        running = True

        # main loop
        while running:
            # event handling, gets all events from the event queue
            for event in pygame.event.get():
                # quit if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                #
                elif event.type == MOUSEBUTTONUP:
                    for p in pegs:
                        if p.rect.collidepoint(event.pos):
                            p.mouse_click_callback(p.id)

                    # Does nothing on the first click
                    screen_callback()

            # redraw the objects on the screen
            self.screen.fill(WHITE)
            screen.blit(board, (170, 170))

            # Check each game snapshot, and only draws a peg if
            # logic dictionary has an 'f' for that spot
            for key, value in logic_dict.items():
                if value == 'f':
                    pegs[key].draw(screen)

            # show the new frame
            pygame.display.flip()

            # wait until time to compute the next frame
            self.fps_clock.tick(self.fps)


    def cleanup(self):
        pygame.quit()


# 1. initialize the game with a frame rate
# -------------------------------------------------------------------------
g = Game(30)

# -------------------------------------------------------------------------
# 2. set up the game pieces
# -------------------------------------------------------------------------


# What the logic does when a peg is clicked
def peg_callback(ID):
    global mouse_click
    if mouse_click == 0:
        for z in pegs:
            if z.id == ID:
                temp = pegs.index(z)
        logic_dict[temp] = 'e'
        snapshots.append(logic_dict)
    else: pass

    mouse_click += 1
    # Finds optimal moves immediately after user selects which peg to get rid of
    find_optimal_move(logic_dict)


# When screen has been clicked, do this
def screen_callback():
    global mouse_click
    # If mouse_click == 0, AKA no pegs have been removed
    if mouse_click == 0:
        pass
    # If peg has been removed, display snapshots on click
    elif mouse_click >= 1:
        for s in snapshots:
            for key, value in s.items():
                if value == 'f':
                    pegs[key].draw


# Game Logic (15 slots in a list that are either empty (e) or filled (f))
logic_dict = {0: 'f', 1: 'f', 2: 'f', 3: 'f', 4: 'f', 5: 'f', 6: 'f', 7: 'f',
              8: 'f', 9: 'f', 10: 'f', 11: 'f', 12: 'f', 13: 'f', 14: 'f'}

# Create multiple peg surfaces to start
pegs = []
for i in range(15):
    if i == 0:
        pegs.append(peg.Peg(i, screen, (290, 205), peg_callback))
    elif 1 <= i <= 2:
        pegs.append(peg.Peg(i, screen, (270 + 41*(i-1), 238), peg_callback))
    elif 3 <= i <= 5:
        pegs.append(peg.Peg(i, screen, (250 + 41*(i-3), 271), peg_callback))
    elif 6 <= i <= 9:
        pegs.append(peg.Peg(i, screen, (230 + 41*(i-6), 304), peg_callback))
    elif 10 <= i <= 14:
        pegs.append(peg.Peg(i, screen, (210 + 41*(i-10), 337), peg_callback))

#######################################################################################
################################################
# Function that solves the game
# Keeps track of moves made
moves_made = []

global is_won
is_won = False

# Keeps track of game states to later print out
# ERROR: Nothing is being appended to the snapshots list other than the first initial move
snapshots = [
                {
                    0: 'f', 1: 'f', 2: 'f', 3: 'f', 4: 'f', 5: 'f', 6: 'f', 7: 'f',
                    8: 'f', 9: 'f', 10: 'f', 11: 'f', 12: 'f', 13: 'f', 14: 'f'
                }

            ]


# List of all legal moves
# ERROR: HOW TO LINK THESE NUMBERS TO LOGIC_DICT
# SO LOGIC_DICT IS ACTUALLY MODIFIED IN FUNCTIONS BELOW
legal_moves = [
    (0, 1, 3),
    (0, 2, 5),
    (1, 3, 6),
    (1, 4, 8),
    (2, 4, 7),
    (2, 5, 9),
    (3, 1, 0),
    (3, 4, 5),
    (3, 6, 10),
    (3, 7, 12),
    (4, 7, 11),
    (4, 8, 13),
    (5, 2, 0),
    (5, 4, 3),
    (5, 8, 12),
    (5, 9, 14),
    (6, 3, 1),
    (6, 7, 8),
    (7, 4, 2),
    (7, 8, 9),
    (8, 4, 1),
    (8, 7, 6),
    (9, 5, 2),
    (9, 8, 7),
    (10, 6, 3),
    (10, 11, 12),
    (11, 7, 4),
    (11, 12, 13),
    (12, 7, 3),
    (12, 8, 5),
    (12, 11, 10),
    (12, 13, 14),
    (13, 8, 4),
    (13, 12, 11),
    (14, 9, 5),
    (14, 13, 12)
]


# If the move is blank in the first slot
# (since in the list of valid moves frontward and backwards are both covered)
# both (0, 1, 3) and (3, 1, 0) are in the list legal_moves
def can_move(move):
    return move[0] == 'e' and move[1] == 'f' and move[2] == 'f'


# Finds current available moves in game state
# (is constantly changing due to make_move and undo functions)
def valid_moves():
    return filter(can_move, legal_moves)


# Executes move
def make_move(move):
    if can_move(move):
        move[0] == 'f'
        move[1] == 'e'
        move[2] == 'e'
        # Adds snapshot of logic and moves_made
        moves_made.append(move)
        snapshots.append(logic_dict)


# Undoes previous move
def undo():
    move = moves_made.pop()
    move[0] = 'e'
    move[1] = 'f'
    move[2] = 'f'
    # Removes snapshot if not optimal
    snapshots.remove()


# Determines how many slots in logic_list are 'f'
def f_count():
    count = 0
    values = logic_dict.values()
    for a in values:
        if a == 'f':
            count += 1

    return count


# Recursive function: Determines which route is the most optimal way to solve Tricky Triangle
# Through brute force
def find_optimal_move(moves_list):
    global is_won
    if is_won:
        return
    # Looks at all available valid moves
    for move in valid_moves():
        # Make the move
        make_move(move)
        # IF WIN OCCURS (Only one peg is left)
        if f_count() == 1:
            is_won = True
        else:
            find_optimal_move()
            undo()


##################################################
#######################################################################################

# -------------------------------------------------------------------------
# 3. operate the game
# -------------------------------------------------------------------------
g.play(pegs)

# -------------------------------------------------------------------------
# 4. shut down the game
# -------------------------------------------------------------------------
#    final processing on completion

#    clean up


# Debugging
for m in moves_made:
    print(m)

for o in snapshots:
    print(o)
