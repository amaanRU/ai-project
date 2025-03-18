# Fast Trajectory Replanning
### Developed by Amaan Dar

This project visualizes different A* search variants in a grid environment. The agent dynamically explores the grid using Repeated Forward A* search, Repeated Backward A* search, and Adaptive A* search.

## Visualizations of A* Search Variants

### Repeated Forward A*
**Animation:**
![Repeated Forward A*](assets/Repeated%20Forward%20A*.gif)

**Reconstructed Path:**
![Repeated Forward A* Reconstructed Path](assets/Repeated%20Forward%20A*%20Path.png)

### Repeated Backward A*
**Animation:**
![Repeated Backward A*](assets/Repeated%20Backward%20A*.gif)

**Reconstructed Path:**
![Repeated Backward A* Reconstructed Path](assets/Repeated%20Backward%20A*%20Path.png)

### Adaptive A*
**Animation:**
![Adaptive A*](assets/Adaptive%20A*.gif)

**Reconstructed Path:**
![Adaptive A* Reconstructed Path](assets/Adaptive%20A*%20Path.png)

---

## Running the project

### Clone the repo
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Setup a virtual environment
```bash
python -m venv venv
source venv/bin/activate # for windows peeps, use venv/Scripts/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Running the program on a random grid
```bash
python3 gridworld.py
```

### Generating and saving 50 random grids
```bash
python3 gridworld.py --generate
```

### Running the algorithms on a specific grid
```bash
python3 gridworld.py --grid grids/grid_1.txt
```
