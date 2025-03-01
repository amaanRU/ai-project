def grid_to_graph(grid):
    graph = {} # using a dict to store the adjaceny list
    size = len(grid) # 101x101 grid size
    compass_directions = [(0,1), (1,0), (0,-1), (-1,0)] # our agent can move in 4 directions 

    for x in range(size):
        for y in range(size):
            # checking for if the grid[cell] is blocked 
            if grid[x][y] == 0: 
                neighbor_nodes = []
                for dx, dy in compass_directions:
                    # our calculation for our neighbor_nodes
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == 0:
                        neighbor_nodes.append((nx, ny)) # appending our unblocked neighbor nodes
                graph[(x, y)] = neighbor_nodes # adding these neighbor nodes to our adjaceny list
    
    return graph

def get_neighbors(node, grid):
    x, y = node # getting our coordinates for the node
    size = len(grid) # getting the size of the grid
    neighbor_nodes = [] # this is where we will store our neighbor_nodes that are unblocked
    compass_directions = [(0,1), (1,0), (0,-1), (-1,0)]

    for dx, dy in compass_directions:
        nx, ny = x + dx, y + dy # calculating coordinates for the neighbor_nodes again
        if 0<= nx < size and 0 <= ny < size and grid[nx][ny] == 0: # if the node is unlbokced, append it to neighbor_nodes
            neighbor_nodes.append((nx, ny))
    return neighbor_nodes

