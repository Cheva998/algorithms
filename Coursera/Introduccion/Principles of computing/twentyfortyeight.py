#2048
#http://www.codeskulptor.org/#user40_osxIOY5opz_5.py

#Merge
#http://www.codeskulptor.org/#user40_7GIhTQ6lat_0.py


"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
#import poc_simpletest

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
        self.indices = {}
        self.indices[UP] = [[0, col] for col in range(self.width)]
        self.indices[DOWN] =  [[self.height-1, col] for col in range(self.width)]
        self.indices[LEFT] = [[row, 0] for row in range(self.height)]
        self.indices[RIGHT] = [[row, self.width-1] for row in range(self.height)]
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_x in range(self.width)] 
                     for dummy_y in range(self.height)]
        self.new_tile()
        self.new_tile()
        return self.grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        self.strin = str(self.grid)
        return self.strin

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
        direc = OFFSETS[direction]
        flag = False
        for start in self.indices[direction]:
            if direction == UP or  direction == DOWN:
                line = [0 for dummy in range(self.height)]
                count = 0
                for step in range(self.height):
                    row = start[0] + step * direc[0]
                    col = start[1] + step * direc[1]
                    line[count] = self.grid[row][col]
                    count += 1
                merged_line = merge(line)
                if line != merged_line:
                    flag = True
                count = 0
                for step in range(self.height):
                    row = start[0] + step * direc[0]
                    col = start[1] + step * direc[1]
                    self.grid[row][col] = merged_line[count]
                    count += 1
            elif direction == LEFT or direction == RIGHT:
                line = [0 for dummy in range(self.width)]
                count = 0
                for step in range(self.width):
                    row = start[0] + step * direc[0]
                    col = start[1] + step * direc[1]
                    line[count] = self.grid[row][col]
                    count += 1
                merged_line = merge(line)
                if line != merged_line:
                    flag = True
                count = 0
                for step in range(self.width):
                    row = start[0] + step * direc[0]
                    col = start[1] + step * direc[1]
                    self.grid[row][col] = merged_line[count]
                    count += 1
        if flag:
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

board = TwentyFortyEight(3,3)
#print "board after reset", board

#for x in range(3):
#    ndf = [board.get_tile(x,y) for y in range(3)]
#    print ndf
    
#print ( board.get_tile(0,0),  board.get_tile(0,1))
#print ( board.get_tile(1,0),  board.get_tile(1,1))
board.new_tile()
#print "board after 1 more", board
#for x in range(3):
#    ndf = [board.get_tile(x,y) for y in range(3)]
#    print ndf
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#Test for the merge function 
#test_merge = poc_simpletest.TestSuite()
#test_merge.run_test(merge([2, 0, 0, 0]), [2, 0, 0, 0], "Prueba 1")
#test_merge.run_test(merge([2, 2, 0, 0]), [4, 0, 0, 0], "Prueba 2")
#test_merge.run_test(merge([2, 0, 2, 0]), [4, 0, 0, 0], "Prueba 3")
#test_merge.run_test(merge([2, 0, 0, 2]), [4, 0, 0, 0], "Prueba 4")
#test_merge.run_test(merge([0, 2, 0, 2]), [4, 0, 0, 0], "Prueba 5")
#test_merge.run_test(merge([0, 0, 2, 2]), [4, 0, 0, 0], "Prueba 6")
#test_merge.run_test(merge([4, 0, 0, 2]), [4, 2, 0, 0], "Prueba 7")
#test_merge.run_test(merge([4, 2, 0, 0]), [4, 2, 0, 0], "Prueba 8")
#test_merge.run_test(merge([4, 2, 2, 0]), [4, 4, 0, 0], "Prueba 9")
#test_merge.run_test(merge([8, 4, 0, 2]), [8, 4, 2, 0], "Prueba 10")
#test_merge.run_test(merge([8, 4, 2, 8]), [8, 4, 2, 8], "Prueba 11")
#test_merge.run_test(merge([0, 4, 2, 8]), [4, 2, 8, 0], "Prueba 12")
#test_merge.run_test(merge([8, 0, 0, 8]), [16, 0, 0, 0], "Prueba 13")
#test_merge.report_results()

