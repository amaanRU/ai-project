import heapq
import numpy as np
from astar_search import heuristic
from graph import get_neighbors

def repeated_forward_astar(grid, start=(0,0), target=(100,100), tie_breaking="small_g"):
    size = len(grid)
    
    agent_grid = np.zeros_like(grid)  
    agent_grid[start] = 0  
    agent_grid[target] = 0  
    
    g_values = {start: 0}
    search_values = {}
    tree_pointers = {}

    current_cell = start
    expanded_nodes = 0
    total_path = []
    timesteps = 0
    counter = 0  
    while current_cell != target:
        counter += 1
        
        for x in range(size):
            for y in range(size):
                if (x, y) not in search_values:
                    search_values[(x, y)] = 0

        search_values[current_cell] = counter
        g_values[current_cell] = 0
        search_values[target] = counter
        g_values[target] = float('inf')

        open_heap = []
        closed_set = set()
        heapq.heappush(open_heap, (heuristic(current_cell, target), g_values[current_cell], current_cell))

        while open_heap:
            _, g_value, node = heapq.heappop(open_heap)
            if node in closed_set:
                continue  

            closed_set.add(node)
            expanded_nodes += 1

            if node == target:
                break 

            for neighbor in get_neighbors(node, agent_grid):
                if neighbor in closed_set:
                    continue
                
                if grid[neighbor] == 1:
                    agent_grid[neighbor] = 1
                    continue  
                
                if search_values[neighbor] < counter:
                    g_values[neighbor] = float("inf")
                    search_values[neighbor] = counter

                new_g_value = g_values[node] + 1
                if new_g_value < g_values[neighbor]:
                    g_values[neighbor] = new_g_value
                    tree_pointers[neighbor] = node
                    f_value = g_values[neighbor] + heuristic(neighbor, target)

                    if tie_breaking == "large_g":
                        priority = (f_value, -g_values[neighbor], neighbor)
                    else:
                        priority = (f_value, g_values[neighbor], neighbor)
                    
                    heapq.heappush(open_heap, priority)
        
        if target not in tree_pointers:
            print("agent being a dummy!! cannot find path!")
            return None, expanded_nodes, timesteps
        
        planned_path = []
        step = target
        while step in tree_pointers:
            planned_path.append(step)
            step = tree_pointers[step]
        planned_path.reverse()

        for step in planned_path:
            x, y = step
            timesteps += 1

            if grid[x, y] == 1:
                agent_grid[x, y] = 1
                break

            current_cell = step
            total_path.append(step)

            if current_cell == target:
                print(f"made it to the target in {timesteps} timesteps")
                return total_path, expanded_nodes, timesteps
    
    return total_path, expanded_nodes, timesteps



def repeated_backward_astar(grid, start, target, tie_breaking="large_g"):    
    def heuristic(s, goal):
        return abs(s[0] - goal[0]) + abs(s[1] - goal[1])
    
    compass_directions = [(0,1), (1,0), (0,-1), (-1,0)]
    open_set = []
    closed_set = set()
    g_values = {target: 0}
    parent_nodes = {}
    nodes_expanded = 0
    timesteps = 0
    
    f_start = heuristic(target, start)
    heapq.heappush(open_set, (f_start, 0, target))
    
    while open_set:
        f, g, current = heapq.heappop(open_set)
        
        if current in closed_set:
            continue
            
        closed_set.add(current)
        nodes_expanded += 1
        
        if current == start:
            path = []
            while current in parent_nodes:
                path.append(current)
                current = parent_nodes[current]
            path.append(target) 
            path.reverse()     
            return path, nodes_expanded, timesteps
        
        for dx, dy in compass_directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if (0 <= neighbor[0] < len(grid) and 
                0 <= neighbor[1] < len(grid[0]) and 
                grid[neighbor[0]][neighbor[1]] == 0):
                
                new_g = g_values[current] + 1
                
                if neighbor not in g_values or new_g < g_values[neighbor]:
                    g_values[neighbor] = new_g
                    parent_nodes[neighbor] = current
                    
                    f = new_g + heuristic(neighbor, start)
                    
                    tiebreaker = new_g if tie_breaking == "large_g" else -new_g
                    
                    heapq.heappush(open_set, (f, tiebreaker, neighbor))
        
        timesteps += 1
    
    return None, nodes_expanded, timesteps