# Fast Trajectory Replanning
### Developed by Amaan Dar

This project visualizes different A* search variants in a grid environment. The agent dynamically explores the grid using Repeated Forward A* search, Repeated Backward A* search, and Adaptive A* search.

## Visualizations of A* Search Variants

### Repeated Forward A*
<div align="center">
  <table>
    <tr>
      <th>Traversal</th>
      <th>Reconstructed Path</th>
    </tr>
    <tr>
      <td><img src="assets/Repeated%20Forward%20A*.gif" width="90%"></td>
      <td><img src="assets/Repeated%20Forward%20A*%20Path.png" width="90%"></td>
    </tr>
  </table>
</div>

### Repeated Backward A*
<div align="center">
  <table>
    <tr>
      <th>Traversal</th>
      <th>Reconstructed Path</th>
    </tr>
    <tr>
      <td><img src="assets/Repeated%20Backward%20A*.gif" width="90%"></td>
      <td><img src="assets/Repeated%20Backward%20A*%20Path.png" width="90%"></td>
    </tr>
  </table>
</div>

### Adaptive A*
<div align="center">
  <table>
    <tr>
      <th>Traversal</th>
      <th>Reconstructed Path</th>
    </tr>
    <tr>
      <td><img src="assets/Adaptive%20A*.gif" width="90%"></td>
      <td><img src="assets/Adaptive%20A*%20Path.png" width="90%"></td>
    </tr>
  </table>
</div>

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
