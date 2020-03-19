#http://www.codeskulptor.org/#user40_2639NXK1RS_6.py



"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]# for dummy in range(7)]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        dimen = len(configuration)
        self._board = [0] * dimen
        for col in range(dimen):
            self._board[-col-1] = configuration[col]
            
    def __str__(self):
        """
        Return string representation for Mancala board
        """
#        charac = "H6| H5| H4| H3| H2| H1| S\n"
#        for col in range(len(self.board)):
#            charac += str(self.board[col])
#            if col < len(self.board) - 1 :
#                charac += " | "
        charac = str(self._board)
        return charac
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        indic = -1 * house_num -1
        return self._board[indic]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        won = True
        for col in range(len(self._board)):
            if self.get_num_seeds(col) > 0:
                won = False
                break
        return won
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        seeds_num = self.get_num_seeds(house_num)
        if house_num == 0:
            legal_move = False
        elif seeds_num == house_num:
            legal_move = True
        else:
            legal_move = False
        return legal_move

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        indic = -1 * house_num -1
        if self.is_legal_move(house_num):
            self._board[indic] -=  self._board[indic]
            for col in range(indic+1, 0, 1):
                self._board[col] += 1
            

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        shor_move = 0
        for col in range(1, len(self._board)):
            if self.is_legal_move(col):
                shor_move = col
                break
        return shor_move
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        moves = []
        set_test = list(self._board)
        set_test.reverse()
        test = SolitaireMancala()
        test.set_board(set_test)
        next_move = 1
#        count = 0 
        while next_move > 0:
            next_move = test.choose_move()
            if next_move > 0:
                moves.append(next_move)
                test.apply_move(next_move)
#            count += 1
        return moves
 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

# add more tests here
#main_board = SolitaireMancala()
#main_board.set_board([0, 0, 1, 1, 3, 5, 0])
#print main_board
#print main_board.get_num_seeds(0), main_board.get_num_seeds(1), main_board.get_num_seeds(2) 
#main_board.apply_move(1)
#moves = main_board.plan_moves()
#print moves
#print main_board
#moves_ = main_board.choose_move()
#main_board.apply_move(moves_)
#print main_board
#moves_ = main_board.choose_move()
#main_board.apply_move(moves_)
#print main_board
#moves_ = main_board.choose_move()
#main_board.apply_move(moves_)
#print main_board
#moves_ = main_board.choose_move()
#main_board.apply_move(moves_)
#print main_board


#test_mancala()


# Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())
