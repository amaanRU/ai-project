import random
import os
from astar_search import astar_search
from visualizer import grid_visualized
import numpy as np
from collections import deque
import time
from repeated_astar_search import repeated_forward_astar, repeated_backward_astar
from adaptive_astar_search import adaptive_astar



def create_grid(size=101, block_probability=0.3):
    
    # starting our grid off completely blocked
    grid = np.ones((size, size), dtype=int) 
    visited = set() # tracking cells that will be visited in a set
    stack = [(0,0)] # our stack for when we perform dfs
    visited.add((0,0)) # our starting coordinate (0,0) adding to visited set
    grid[0,0] = 0 # making sure that our starting coordinate is unblocked
    
    compass_directions = [(0,2), (2,0), (0, -2), (-2,0)] # movement

    while stack:
        cx, cy = stack[-1] # getting our current position (the c means current, im lazy, will refactor later)

        neighbor_nodes = []
        for dx, dy in compass_directions: # d for delta
            nx, ny = cx + dx, cy + dy # n for next
            if 0 <= nx < size and 0 <= ny < size and (nx,ny) not in visited:
                neighbor_nodes.append((nx, ny, dx, dy))
        # need random neighbor to remove the corridor between
        if neighbor_nodes:
            nx, ny, dx, dy = random.choice(neighbor_nodes)

            wall_x, wall_y = cx + dx//2, cy + dy//2
            grid[wall_x, wall_y] = 0

            grid[nx, ny] = 0
            visited.add((nx, ny))
            stack.append((nx, ny))
        else: 
            # this will backtrack if there are no unvisited neighbor nodes
            stack.pop()
    """
    for x in range(1, size, 2):
        for y in range(1, size, 2):
            if (x,y) not in visited:
                stack.append((x, y))
                visited.add((x, y))
                grid[x,y] = 0
    
    for x in range(size):
        for y in range(size):
            if grid[x,y] == 0 and random.random() < block_probability:
                grid[x,y] = 1
    grid[0,0] = 0
    """

    # making sure our target is unblocked
    grid[size-1, size-1] = 0
    if astar_search(grid, (0,0), (100,100)):
        return grid


# ACTUAL PATHFINDER

def astar_pathfinding(grid, start=(0,0), target=(100,100)):
    return astar_search(grid, start, target)

# IGNORE BFS_PATHFINDING STRICTLY FOR TESTING PURPOSES

"""
def bfs_pathfinding(grid, start=(0,0), target=(100,100)):
    size = len(grid)
    if grid[start[0], start[1]] == 1 or grid[target[0], target[1]] == 1:
        print("Start or target is blocked")
        return None
    queue = deque([start])
    visited = {start}
    parent_nodes = {start: None}
    compass_directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == target:
            path = []
            while (x, y) is not None:
                path.append((x, y))
                if parent_nodes[(x, y)] is None:
                    break
                x, y = parent_nodes[(x, y)]
            print(f"individual len of path: {len(path)}")
            return path [::-1]
        
        for dx, dy in compass_directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < size and 0 <= ny < size and grid[nx, ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent_nodes[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    print("No path found")
    solved_path = path(grid)
    grid_visualized(grid, path=solved_path)
    return None
"""

def save_grid(grid, filename):
    with open(filename, "w") as f:
        for row in grid:
            f.write(" ".join(map(str, row)) + "\n")

def load_grid(filename):
    with open(filename, "r") as f:
        grid = [list(map(int, line.strip().split())) for line in f if line.strip()]
        return grid

def create_50_grids(num = 50, folder = "grids"):
    os.makedirs(folder, exist_ok = True)

    for i in range(1, num + 1):
        grid = create_grid()
        filename = f"{folder}/grid_{i}.txt"
        save_grid(grid, filename)
        print(f"File : {filename} has been saved")

def save_results(filename, results):
    output_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
    os.makedirs(output_directory, exist_ok=True)
    file_path = os.path.join(output_directory, os.path.basename(filename))
    with open(file_path, "a") as f:
        f.write(results + "\n")

grid = create_grid()
# create_50_grids()

results = []
for i in range(1, 51):
    grid_file = f"grids/grid_{i}.txt"
    print(f"Running repeated a* on {grid_file}...")

    with open(grid_file, "r") as f:
        grid = np.array([list(map(int, line.strip().split())) for line in f if line.strip()])

    
    # repeated forward a*

    start_time = time.time()
    path_small, expanded_nodes_small, timesteps_small = repeated_forward_astar(grid, (0,0), (100,100), tie_breaking="small_g")
    time_small = time.time() - start_time
    result_small = f"{grid_file}, small_g, {len(path_small) if path_small else 'no path'}, {time_small:.6f}, {expanded_nodes_small}"

    start_time = time.time()
    path_large, expanded_nodes_large, timesteps_large = repeated_forward_astar(grid, (0,0), (100,100), tie_breaking="large_g")
    time_large = time.time() - start_time
    result_large = f"{grid_file}, large_g, {len(path_large) if path_large else 'no path'}, {time_large:.6f}, {expanded_nodes_large}"

    # repeated backward a*

    start_time = time.time()
    path_backward_small, expanded_nodes_backward_small, timesteps_backward_small = repeated_backward_astar(grid, (0,0), (100,100), tie_breaking="small_g")
    time_backward_small = time.time() - start_time
    result_backward_small = f"{grid_file}, backward_small_g, {len(path_backward_small) if path_backward_small else 'no path'}, {time_backward_small:.6f}, {expanded_nodes_backward_small}"

    start_time = time.time()
    path_backward_large, expanded_nodes_backward_large, timesteps_backward_large = repeated_backward_astar(grid, (0,0), (100,100), tie_breaking="large_g")
    time_backward_large = time.time() - start_time
    result_backward_large = f"{grid_file}, backward_large_g, {len(path_backward_large) if path_backward_large else 'no path'}, {time_backward_large:.6f}, {expanded_nodes_backward_large}"

    # adaptive a* 

    start_time = time.time()
    adaptive_path, expanded_nodes_adaptive, timesteps_adaptive = adaptive_astar(grid, (0,0), (100,100), tie_breaking="large_g")
    time_adaptive = time.time() - start_time
    result_adaptive = f"{grid_file}, adaptive, {len(adaptive_path) if adaptive_path else 'no path'}, {time_adaptive:.6f}, {expanded_nodes_adaptive}"


    print(result_small)
    print(result_large)
    print(result_backward_small)
    print(result_backward_large)
    print(result_adaptive)

    save_results("outputs/statistics.txt", result_small)
    save_results("outputs/statistics.txt", result_large)
    save_results("outputs/statistics.txt", result_backward_small)
    save_results("outputs/statistics.txt", result_backward_large)
    save_results("outputs/statistics.txt", result_adaptive)

    

    results.append(result_small)
    results.append(result_large)
    results.append(result_backward_small)
    results.append(result_backward_large)
    results.append(result_adaptive)

print("data collection complete.")


    

# TESTING SPEEDS AND COMPARING ASTAR WITH BFS

"""
start_time = time.time()
bfs_path = bfs_pathfinding(grid)
bfs_time = time.time() - start_time
bfs_expanded_nodes = len(bfs_path) if bfs_path else 0
print(f"BFS path length : {len(bfs_path) if bfs_path else 'no path'} || Time: {bfs_time:.6f} seconds || Expanded Nodes: {bfs_expanded_nodes}")
"""
"""
false_maze = false_maze_testing()
if path(false_maze) is not None:
    print("wrong bozo")
else:
    print("not solvable")
"""

"""

start_time = time.time()
astar_path_small, astar_expanded_nodes_small = astar_search(grid, (0,0), (100,100), tie_breaking="small_g")
astar_time_small = time.time() - start_time
astar_path_small_results = (f"A* (small g) path length {len(astar_path_small) if astar_path_small else 'no path'} || Time: {astar_time_small:.6f} seconds || Expanded Nodes: {astar_expanded_nodes_small}")


start_time = time.time()
astar_path_large, astar_expanded_nodes_large = astar_search(grid, (0,0), (100,100), tie_breaking="large_g")
astar_time_large = time.time() - start_time
astar_path_large_results = (f"A* (big g) path length {len(astar_path_large) if astar_path_large else 'no path'} || Time: {astar_time_large:.6f} seconds || Expanded Nodes: {astar_expanded_nodes_large}")

grid_visualized(grid, path=astar_path_small)
print("visual complete")
save_results("outputs/statistics.txt", astar_path_small_results)
save_results("outputs/statistics.txt", astar_path_large_results)
"""

"""
if astar_time < bfs_time: 
    print("A* star is faster than BFS")
else: 
    print("A* star is slower than BFS")
"""

"""
print(astar_path_small_results)
print(astar_path_large_results)


start_time = time.time()
repeated_path, expanded_nodes, timesteps = repeated_forward_astar(grid, (0,0), (100,100), tie_breaking="small_g")
repeated_time = time.time() - start_time
repeated_astar_search_results = (f"Repeated A* path length {len(repeated_path) if repeated_path else 'no path'} || Time: {repeated_time:.6f} seconds || Expanded Nodes: {expanded_nodes}")
print(repeated_astar_search_results)

save_results("outputs/statistics.txt", repeated_astar_search_results)


if repeated_path:
    grid_visualized(grid, path=repeated_path)
"""

path_forward_astar, _, _ = repeated_forward_astar(grid, (0,0), (100,100))
grid_visualized(grid, path=path_forward_astar, path_label="Repeated A*", algorithm_name="Repeated A*")

path_backward_astar, _, _ = repeated_backward_astar(grid, (0,0), (100,100))
grid_visualized(grid, path=path_backward_astar, path_label="Backward A*", algorithm_name="Repeated Backward A*")

path_adaptive_astar, _, _ = adaptive_astar(grid, (0,0), (100,100))
grid_visualized(grid, path=path_adaptive_astar, path_label="Adaptive A*", algorithm_name="Adaptive A*")


