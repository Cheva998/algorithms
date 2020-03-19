#http://www.codeskulptor.org/#user42_4cjyPGxH1P_14.py


"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
        
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for idx in self._zombie_list:
            yield idx

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for idx in self._human_list:
            yield idx
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [[self._grid_height * self._grid_width 
                           for dummyx in range(self._grid_width)]
                          for dummy in range(self._grid_height)]
        if entity_type == HUMAN:
            que_list = self._human_list
        elif entity_type == ZOMBIE:
            que_list = self._zombie_list
        else:
            return
        boundary = poc_queue.Queue()
        for item_list in que_list:
            boundary.enqueue(item_list)
        for item in boundary:
            visited.set_full(item[0], item[1])
            distance_field[item[0]][item[1]] = 0
            
        # BFS search
        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            neighbors = self.four_neighbors(current_cell[0], current_cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]) \
                    and self._cells[neighbor[0]][neighbor[1]] == EMPTY:
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1

        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        idx = 0
        for human in self.humans():
            pos_moves = self.eight_neighbors(human[0], human[1])
            pos_moves.append(human)
            best_move = 0
            list_moves = []
            
            for move in pos_moves:
                if self._cells[move[0]][move[1]] == EMPTY and zombie_distance_field[move[0]][move[1]] > best_move:
                    list_moves = [move]
                    best_move = zombie_distance_field[move[0]][move[1]]
                elif self._cells[move[0]][move[1]] == EMPTY and zombie_distance_field[move[0]][move[1]] == best_move:
                    list_moves.append(move)
            self._human_list[idx] = random.choice(list_moves)
            idx += 1
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        idx = 0
        for zombie in self.zombies():
            pos_moves = self.four_neighbors(zombie[0], zombie[1])
            pos_moves.append(zombie)
            best_move = self._grid_height * self._grid_width
            list_moves = []
            for move in pos_moves:
                if self._cells[move[0]][move[1]] == EMPTY and human_distance_field[move[0]][move[1]] < best_move:
                    list_moves = [move]
                    best_move = human_distance_field[move[0]][move[1]]
                elif self._cells[move[0]][move[1]] == EMPTY and human_distance_field[move[0]][move[1]] == best_move:
                    list_moves.append(move)
            self._zombie_list[idx] = random.choice(list_moves)
            idx += 1

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
#poc_zombie_gui.run_gui(Apocalypse(20, 22, [(0,1)], [(2,2)], [(0,2), (2,0)]))


#######TESTING############
#grid_height = 30
#grid_width = 40
#obstacle_list = [(0,1)]
#zombie_list = [(2,2)]
#human_list = [(0,2), (2,0)]
#Apoc = Apocalypse(grid_height, grid_width, obstacle_list, zombie_list, human_list)
#dis_fi = Apoc.compute_distance_field(HUMAN)
#Apoc.move_humans(dis_fi)

#Apoc.clear()
#Apoc.add_zombie(0,1)
#Apoc.add_zombie(0,2)
#
#Apoc.add_human(1,0)
#Apoc.add_human(2,0)
#print Apoc.num_humans()
#
#hum = Apoc.humans()
#print hum.next()
#print hum.next()

