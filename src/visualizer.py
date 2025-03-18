import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def grid_visualized(grid, agent_grid=None, start=(0,0), target=(100,100), save_as=None, path=None, path_label="Path", animate=False, algorithm_name="Algorithm"):
    size = len(grid)
    grid_array = np.array(grid)

    plt.figure(figsize=(10,10))
    plt.xticks([])
    plt.yticks([])
    plt.title(f"{algorithm_name}")
    plt.imshow(grid_array, cmap="binary", origin="upper")
    plt.scatter(start[1], start[0], color="green", s=100, label="Start")
    plt.scatter(target[1], target[0], color="red", s=100, label="Target")
    agent_dot, = plt.plot([], [], "bo", markersize=10, label="Agent")
    visited_x, visited_y = [], []
    visited_scatter = plt.scatter([], [], color="orange", s=10)
    reconstructed_path, = plt.plot([], [], color="darkred", linewidth=2, label="Reconstructed Path")


    """
    if path is not None and len(path) > 1:
        #print("Drawing path on the grid...")
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, color="blue", linewidth=2, label="path")
        """
    def update(frame):
        if frame < len(path):
            x, y = path[frame]
            visited_x.append(y)
            visited_y.append(x)
            agent_dot.set_data([y],[x])
            visited_scatter.set_offsets(np.column_stack((visited_x, visited_y )))
        if frame == len(path) - 1:
            path_x, path_y = zip(*path)
            reconstructed_path.set_data(path_y, path_x)
        return agent_dot, visited_scatter, reconstructed_path
    ani = FuncAnimation(plt.gcf(), update, frames=len(path), interval=10, blit=True, repeat=False)
    plt.legend(loc="upper right")
    plt.show()
            
        

    

