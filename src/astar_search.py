import heapq
from graph import get_neighbors

# function to calculate manhattan distance between the points (a,b)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  

# TESTING FOR TIE BREAKING, DOES NOT NEED TO BE IN FINAL IMPLEMENTATION

# we are using a min-heap (prio queue) to expand nodes efficiently 
# a star finds the shortest path from agent to target
# this will use the manhattan distance as our heuristic
# function expands the best possible node that has the lowest f-value first
# using a closed set to avoid going through the same node again

def astar_search(grid, start, target, tie_breaking="small_g"):
    open_heap = [] # our prio queue
    heapq.heappush(open_heap, (heuristic(start, target), 0, start)) # pushing the starting node
    
    g_score = {start: 0} # g score is the cost from the start to current position
    parent_nodes = {} # for storing path
    closed = set()
    expanded_nodes = 0 # for performance benchmarks

    while open_heap:
        # pop the node with the lowest f score
        current_f, g_value, current = heapq.heappop(open_heap)
        # continue if the node is one we have already visited
        if current in closed:
            continue

        # marking the node as visited
        closed.add(current)
        expanded_nodes += 1
        
        # if our current node reached the target, return the path
        if current == target:
            # Reconstruct path
            path = []
            while current in parent_nodes:
                path.append(current)
                current = parent_nodes[current]
            return path[::-1], expanded_nodes

        
        for neighbor_node in get_neighbors(current, grid): # exploring all valid neighbor nodes which are unblocked cells
            x, y = neighbor_node
            if grid[x, y] == 1:
                continue
            if neighbor_node in closed:
                continue # if the neighbor node has been expanded then skip
            
            # computing our new g score which is the cost from start to current neighbor node
            new_gscore = g_score[current] + 1

            # updating neighbor_nodes g score if new path is shorter
            if neighbor_node not in g_score or new_gscore < g_score[neighbor_node]:
                parent_nodes[neighbor_node] = current # storing the parent node for reconstructing path
                g_score[neighbor_node] = new_gscore # updating new g score cost
                f_score = new_gscore + heuristic(neighbor_node, target) # computing f score
                # heapq.heappush(open_heap, (f_score, neighbor_node))  # pushing neighbor node with priority

                if tie_breaking == "large_g":
                    priority = (f_score, -new_gscore, neighbor_node)
                else:
                    priority = (f_score, new_gscore, neighbor_node)
                heapq.heappush(open_heap, priority)
    
    # in case no path
    return None, expanded_nodes