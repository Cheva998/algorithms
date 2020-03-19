#http://www.codeskulptor.org/#user40_W04mJuLkXz_0.py

#2048
#http://www.codeskulptor.org/#user40_3iNKBL9L8d_8.py

#Merge
#http://www.codeskulptor.org/#user40_7GIhTQ6lat_0.py

"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
import poc_simpletest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = [0] * len(line)
    count = 0
    state = 1
    flag = False
    for ite in range(len(line)):
        if line[ite] > 0:
            new_line[count] = line[ite]
            flag = True
        if state == 1:
            if count > 0 and new_line[count - 1] == new_line[count]:
                new_line[count - 1] += new_line[count]
                new_line[count] = 0
                count -= 1
                state = 2
        elif state == 2 and new_line[count] > 0:
            state = 1
        if flag:
            count += 1
            flag = False
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.reset()
        self.initial_tile = dict()
        self.initial_tile[UP] = [(0, col) for col in range(grid_width)]
        self.initial_tile[DOWN] = [(grid_height - 1, col) for col in range(grid_width)]
        self.initial_tile[LEFT] = [(row, 0) for row in range(grid_height)]
        self.initial_tile[RIGHT] = [(row, grid_width - 1) for row in range(grid_height)]
        self.num_iter = {UP: grid_height, DOWN: grid_height, LEFT: grid_width, RIGHT: grid_width}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_x in range(self.width)] 
                     for dummy_y in range(self.height)]
#        self.new_tile()
#        self.new_tile()
        return self.grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        merged_grid = [[0 for dummy_x in range(self.width)] 
                     for dummy_y in range(self.height)]
        for line in self.initial_tile[direction]:
            merge_line = list()
            for step in range(self.num_iter[direction]):
                row = line[0] + step * OFFSETS[direction][0]
                col = line[1] + step * OFFSETS[direction][1]
                merge_line.append(self.grid[row][col])
            merge_line = merge(merge_line)
            for step in range(len(merge_line)):
                row = line[0] + step * OFFSETS[direction][0]
                col = line[1] + step * OFFSETS[direction][1]
                merged_grid[row][col] = merge_line[step]
        if self.grid != merged_grid:
            self.grid = list(merged_grid)
            self.new_tile()
        

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        ran_num = random.random()
        if ran_num <= 0.9:
            num = 2
        else:
            num = 4
        pick_list = [[row, col] for row in range(self.height)
                     for col in range(self.width) 
                      if self.grid[row][col] == 0 ]
        pos = random.choice(pick_list)
        self.set_tile(pos[0], pos[1], num)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        return self.grid

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

DIM = 2
board = TwentyFortyEight(DIM,DIM)
testes = poc_simpletest.TestSuite()
y =  str(board)
print y
testes.run_test(y, "[[0, 0], [0, 0]]", "initial")
board.set_tile(0,0,2)
y =  str(board)
print y
testes.run_test(y, "[[2, 0], [0, 0]]", "1 tile")
board.set_tile(0,1,4)
y =  str(board)
print y
testes.run_test(y, "[[2, 4], [0, 0]]", "2 tile")
board.set_tile(1,0,2)
y =  str(board)
print y
testes.run_test(y, "[[2, 4], [2, 0]]", "3 tile")
board.set_tile(1,1,4)
y =  str(board)
print y
testes.run_test(y, "[[2, 4], [2, 4]]", "4 tile")
testes.report_results()

#print board
#print "board after reset", board
#for x in range(DIM):
#    ndf = [board.get_tile(x,y) for y in range(DIM)]
#    print ndf
#print

#print ( board.get_tile(0,0),  board.get_tile(0,1))
#print ( board.get_tile(1,0),  board.get_tile(1,1))
#for dummy in range (7):
#    board.new_tile()
#print "board after 7 more", board
#board.move(RIGHT)
#for x in range(3):
#    ndf = [board.get_tile(x,y) for y in range(3)]
#    print ndf
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))



