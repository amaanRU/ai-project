"""
convert the grid into a graph for our search algorithms 

let's convert the grid into a graphical representation 
    what is it?
        - our grid is a 2D list of 101x101 nodes
    our nodes
        - our nodes in the graph are the unblocked cells only, blocked cells are not part of the graphical representation of our grid
    our edges
        - we know that our agent uses the four main compass directions (east, south, west, and north)
        - nodes are connected via their adjacent unblocked cells
    representing the graph
        - utilize an adjacency list to store the data of the graph (look this up if you don't know what an adjacency list is)
    utilizing depth-first-search
        - initially set all cells as unvisited 
        - start from a random cell, mark it as visited and unblocked
        - a cell that has no univisited neighbors is a dead-end
        - when at a dead cell, algorithm must backtrack to parent nodes on the search tree until it reaches a cell with an univisited neighbor

"""

def grid_to_graph(grid):
    graph = {}
    size = len(grid)
    compass_directions = [(0,1), (1,0), (0,-1), (-1,0)]

    for x in range(size):
        for y in range(size):
            if grid[x][y] == 0:
                neighbor_nodes = []
                for dx, dy in compass_directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == 0:
                        neighbor_nodes.append((nx, ny))
                graph[(x, y)] = neighbor_nodes
    
    return graph

def get_neighbors(node, grid):
    x, y = node
    size = len(grid)
    neighbor_nodes = []
    compass_directions = [(0,1), (1,0), (0,-1), (-1,0)]

    for dx, dy in compass_directions:
        nx, ny = x + dx, y + dy
        if 0<= nx < size and 0 <= ny < size and grid[nx][ny] == 0:
            neighbor_nodes.append((nx, ny))
    return neighbor_nodes

