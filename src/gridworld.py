""""
**generating gridworld, saving, and loading gridworld**

**OUTLINE**
-----------

defining the gridworld structure
        - grid is 101x101 size
        - individual cells are marked as 0 for unblocked and 1 for blocked
        - A starts at (0,0) and T is located at fixed position (100,100)
        - A assumes that cells are unblocked unless it has already observed them to be blocked until they are discovered

creating the blocked cells in the grid
        - 30% of cells are blocked (1)
        - 70% of cells are unblocked (0)
        - start and target nodes must be unblocked

creating the grids
        - create 50 different grids
        - save each grid as grid_(num).txt (e.g. grid_1.txt grid_2.txt grid_3.txt etc etc lmk if you need help understanding this)
        - each grid must be formatted with rows of unblocked (0's) and blocked (1's) cells

reading the grid
        - you'll have to create a function to read the grid_1.txt file and convert those rows of cells into a 2D structure (use a list)

"""

import random
import os
from astar_search import astar_search

def create_grid(size = 101, block_probability = 0.3):
    grid = [[0 if random.random() > block_probability else 1 for _ in range(size)] for _ in range(size)]

    # define start coordinate and target coordinate to be 0
    grid[0][0] = 0           # (0,0) agent's starting position
    grid[size-1][size-1] = 0 # (100,100) fixed position

    # carve paths in the grid
    # random.shuffle(compass_directions) random tie breaking
    def dfs(x, y):  
        compass_directions = [(0,2), (2,0), (0,-2), (-2,0)]
        random.shuffle(compass_directions)

        for dx, dy in compass_directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == 1:
                grid[nx // 2][ny // 2] = 0
                grid[nx][ny] = 0  # visited nodes
                dfs(ny, ny)
        grid[0][0] = 0
        dfs(0,0)
        grid[size-1][size-1] = 0

    return grid



def save_grid(grid, filename):
    with open(filename, "w") as f:
        for row in grid:
            f.write(" ".join(map(str, row)) + "\n")

def load_grid(filename):
    with open(filename, "r") as f:
        grid = [list(map(int, line.strip().split())) for line in f]
        return grid

def create_50_grids(num = 50, folder = "grids"):
    os.makedirs(folder, exist_ok = True)

    for i in range(1, num + 1):
        grid = create_grid()
        filename = f"{folder}/grid_{i}.txt"
        save_grid = (grid, filename)
        print(f"File : {filename} has been saved")

create_50_grids()
    


