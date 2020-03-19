#http://www.codeskulptor.org/#user40_FzT1qec2g4_13.py

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 500		# Number of trials to run
SCORE_CURRENT = 1.2	# Score for squares played by the current player
SCORE_OTHER = 1.8	# Score for squares played by the other player

##Player constants and map

EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4
SCORE_MAP = {PLAYERX : {PLAYERX : SCORE_CURRENT, PLAYERO : -SCORE_OTHER}, 
             PLAYERO : {PLAYERO : SCORE_CURRENT, PLAYERX : -SCORE_OTHER}}

STRMAP = {EMPTY: " ",
          PLAYERX: "X",
          PLAYERO: "O"}

#DIM = 3
#main_board = provided.TTTBoard(DIM)

# Add your functions here.

def mc_trial(board, player):
    '''
    Randomly moves for each player
    '''
    empty_list = board.get_empty_squares()
    empty_cells = len(empty_list)
    if empty_cells > 0:
        random.shuffle(empty_list)
        for dummy in range(empty_cells):
            cell = empty_list.pop(0)
            if player == PLAYERX:
                board.move(cell[0], cell[1], PLAYERX)
                player = PLAYERO
            elif player == PLAYERO:
                board.move(cell[0], cell[1], PLAYERO)
                player = PLAYERX
            else:
                print "wrong player, must be PLAYERX or PLAYERO"
            winner = board.check_win()
            if winner == PLAYERX or winner == PLAYERO:
                break

def mc_update_scores(scores, board, player):
    '''
    Scores the grid accordingly to the winner player
    '''
    winner = board.check_win()
    b_dim = board.get_dim()
    if player == PLAYERX:
        other_pl = PLAYERO
    else:
        other_pl = PLAYERX
    if winner == PLAYERX or winner == PLAYERO:
        for row in range(b_dim):
            for col in range(b_dim):
                cell = board.square(row, col)
                if player == winner and (cell == PLAYERO or cell == PLAYERX):
                    scores[row][col] += SCORE_MAP[player][cell]
                elif other_pl == winner and (cell == PLAYERO or cell == PLAYERX):
                    scores[row][col] -= SCORE_MAP[player][cell]

def get_best_move(board, scores):
    '''
    Pick the best move and return the (row, col) as a tuple. If the board is full it shouldn't 
    return anything
    '''
    empty_list = board.get_empty_squares()
    empty_cells = len(empty_list)
    pos_save = list()
    if empty_cells > 0:
        flag = True
        for pos in empty_list:
            if flag:
                top = scores[pos[0]][pos[1]]
                pos_save.append(pos)
                flag = False
            else:
                if scores[pos[0]][pos[1]] >= top:
                    top = scores[pos[0]][pos[1]]
                    pos_save.append(pos)
    return random.choice(pos_save)

def mc_move(board, player, trials):
    '''
    Take the board, and number of trials to determine the best move, and return the (row, col)
    as a tuple
    '''
    dim = board.get_dim()
    scores = [[0 for dummy_row in range(dim)]
          for dummy_col in range(dim)]
    test_board = board.clone()
#    empty_list = board.get_empty_squares()
    for dummy in range(trials):
        mc_trial(test_board, player)
        mc_update_scores(scores, test_board, player)
#    print scores
    pos = get_best_move(board, scores)
    return pos    
        

#print board    
#mc_trial(board, PLAYERX)
#board.move(0,0,2)
#board.move(0,1,2)
#board.move(0,2,3)
#board.move(1,2,3)
#board.move(2,2,3)
#scores = [[0 for row in range(DIM)]
#          for col in range(DIM)]
#print scores
#print "WIN:", board.check_win()
#mc_update_scores(scores, board, PLAYERX)
#print board
#print scores
#pos = get_best_move(board, scores)
#print pos
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
