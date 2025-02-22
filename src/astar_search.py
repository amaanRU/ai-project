"""
goal of this file is to compute the shortest path from start to target

priority queue (min - heap)

refactor this file after implementing binary heap from scratch

create separate file for binary heap implementation?

using manhattan distances to track h - values

bidirectional dfs implementation alternate navigation? 
    if bidirectional:
        - make sure to account for lowest f - values when backtracking from intersection point between the two paths created

for manhattan distance
    - create a linked list to store heuristic values dynamically

"""

from binary_heap import BinaryHeap
from graph import get_neighbors


# this function will calculate the manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar_search(grid, start, target):
    # priority queue
    open_list = BinaryHeap()
    open_list.push((0, start))

    # parent nodes for reconstructing path
    came_from = {}
    # g values, cost from starting point to each node
    g_score = {start: 0}                  
    # f values, f = g - values + h - values         
    f_score = {start: heuristic(start, target)}     

    while not open_list.is_empty():
        # retrieving the node with the lowest f-score
        _, current = open_list.pop()

        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            # returning the path from start to target reversed
            return path[::-1]
        
        for neighbor_node in get_neighbors(current, grid):
            untried_g_score = g_score[current] + 1
        
        if neighbor_node not in g_score or untried_g_score < g_score[neighbor_node]:
            came_from[neighbor_node] = current
            g_score[neighbor_node] = untried_g_score
            f_score[neighbor_node] = untried_g_score + heuristic(neighbor_node, target)

            open_list.push((f_score[neighbor_node], neighbor_node))

        # path was not found
        return None 
            
