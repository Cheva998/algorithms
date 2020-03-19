#http://www.codeskulptor.org/#user42_Kt26R0Bcek_2.py

"""
An example of creating a distance field using Manhattan distance
"""

GRID_HEIGHT = 6
GRID_WIDTH = 8


def manhattan_distance(row0, col0, row1, col1):
    """
    Compute the Manhattan distance between the cells
    (row0, col0) and (row1, col1)
    """
    return abs(row0 - row1) + abs(col0 - col1)
        

def create_distance_field(entity_list):
        """
        Create a Manhattan distance field that contains the minimum distance to 
        each entity (zombies or humans) in entity_list
        Each entity is represented as a grid position of the form (row, col) 
        """
        dist_field = [[0 for idx in range(0,GRID_WIDTH)] for idy in range(0,GRID_HEIGHT)]
        for idx in range(0,GRID_HEIGHT):
            for idy in range(0,GRID_WIDTH):
                dist = 10 ** 100
                for dummy in entity_list:
                    x = dummy[0]
                    y = dummy[1]
#                    print "x", x, "y", y, "idx", idx, "idy", idy
                    distance = manhattan_distance(x,y,idx,idy)
#                    print distance
                    if distance < dist:
                        dist = distance
#                print "dist", dist, "field", dist_field
                dist_field[idx][idy] = dist
        return dist_field
        
    
def print_field(field):
    """
    Print a distance field in a human readable manner with 
    one row per line
    """
    for idx in field:
        print idx

def run_example():
    """
    Create and print a small distance field
    """
    field = create_distance_field([[4, 0],[2, 5]])
    print_field(field)
    
run_example()
#print manhattan_distance(4, 6, 1, 1)
#field = create_distance_field([[4, 0],[2, 5]])
#print_field(field)

# Sample output for the default example
#[4, 5, 5, 4, 3, 2, 3, 4]
#[3, 4, 4, 3, 2, 1, 2, 3]
#[2, 3, 3, 2, 1, 0, 1, 2]
#[1, 2, 3, 3, 2, 1, 2, 3]
#[0, 1, 2, 3, 3, 2, 3, 4]
#[1, 2, 3, 4, 4, 3, 4, 5]
    
    

