import matplotlib.pyplot as plt
import numpy as np

def grid_visualized(grid, agent_grid=None, start=(0,0), target=(100,100), save_as=None, path=None, path_color="blue", path_label="Path"):
    size = len(grid)
    grid_array = np.array(grid)

    plt.figure(figsize=(10,10))
    plt.imshow(grid_array, cmap="binary", origin="upper")

    if agent_grid is not None:
        for x in range(size):
            for y in range(size):
                if agent_grid[x, y] == 1:
                    plt.scatter(y, x, color="gray", s=3)

    plt.scatter(start[1], start[0], color="green", s=100, label="Start")
    plt.scatter(target[1], target[0], color="red", s=100, label="Target")

    """
    if path is not None and len(path) > 1:
        #print("Drawing path on the grid...")
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, color="blue", linewidth=2, label="path")
        """
    
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, color=path_color, linewidth=2, label=path_label)
    #else:
        #print("no path displayed")

    plt.legend(loc="upper right")
    plt.title("Grid generated")
    plt.axis("off")

    if save_as:
        plt.savefig(save_as)
        print(f"Visualized grad saved as {save_as}")
    else:
        plt.show()
        plt.pause(0.001)
        input("Press enter to continue: ")
        plt.close()

