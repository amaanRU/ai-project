import heapq
import numpy as np

def adaptive_astar(grid, start, target, tie_breaking="large_g"):
    def heuristic(s, target):
        return abs(s[0] - target[0]) + abs(s[1] - target[1])
    
    size = len(grid)
    open_set = []
    g_values = {start: 0}
    h_values = {start: heuristic(start, target)}
    parent_nodes = {}
    expanded_nodes = 0
    timesteps = 0

    heapq.heappush(open_set, (h_values[start], 0, start))

    while open_set:
        _, g, current = heapq.heappop(open_set)
        expanded_nodes += 1

        if current == target:
            break

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor_node = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor_node[0] < size and 0 <= neighbor_node[1] < size and grid[neighbor_node[0]][neighbor_node[1]] == 0:
                new_g = g + 1
                if neighbor_node not in g_values or new_g < g_values[neighbor_node]:
                    g_values[neighbor_node] = new_g
                    parent_nodes[neighbor_node] = current
                    h_values[neighbor_node] = heuristic(neighbor_node, target)
                    f = new_g + h_values[neighbor_node]

                    priority = (f, new_g if tie_breaking == "large_g" else -new_g)
                    heapq.heappush(open_set, (priority, new_g, neighbor_node))

        timesteps += 1

    if target not in parent_nodes:
        return None, expanded_nodes, timesteps
    
    g_target = g_values[target]
    for node in g_values:
        h_values[node] = g_target - g_values[node]

    path = []
    step = target
    while step in parent_nodes:
        path.append(step)
        step = parent_nodes[step]
    path.append(start)

    return path[::-1], expanded_nodes, timesteps