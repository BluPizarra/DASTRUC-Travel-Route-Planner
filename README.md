# Travel Route Planner (DASTRUC Final Task)

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Dijkstra's%20Shortest%20Path-4B8BBE?style=for-the-badge)](https://github.com/BluPizarra/DASTRUC-Travel-Route-Planner)
[![Data Structure](https://img.shields.io/badge/Data%20Structure-Weighted%20Graph-FFD43B?style=for-the-badge&logoColor=black)](https://github.com/BluPizarra/DASTRUC-Travel-Route-Planner)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Academic](https://img.shields.io/badge/APC-DASTRUC%20Final%20Task-B3665B?style=for-the-badge)](https://www.apc.edu.ph/)

An interactive CLI-based route navigation system in Python demonstrating graph data structures and shortest-path calculation using **Dijkstra's Algorithm**.

Developed by **Bludylan Cyrus A. Pizarra** for the **Data Structures and Algorithms (DASTRUC)** course final requirement:
> *"Efficient Route Planning Using Graph-Based Algorithms"*

---

## Features

- **Adjacency List Graph Representation**: Dynamically model locations (vertices) and bidirectional roads with weights/distances (edges).
- **Dijkstra's Algorithm with Priority Queue**: Computes the optimal, lowest-distance route between any two locations using Python's `heapq` module ($O((V + E) \log V)$ time complexity).
- **Persistence (JSON Serialization)**: Easily save and reload road networks to/from `routes.json`.
- **Interactive Terminal UI**: Intuitive menu interface enhanced with ANSI color formatting for clear feedback and readability.

---

## Repository Structure

```text
DASTRUC-Travel-Route-Planner/
├── travel_route_planner.py           # Main application script (clean entry point)
├── [DASTRUC]PIZARRA_CODE_FINAL TASK.py # Original submitted script
├── routes.json                       # Sample pre-configured graph (Metro Manila routes)
├── .gitignore                        # Git ignore patterns for Python & IDEs
└── README.md                         # Project documentation
```

---

## Requirements & Setup

- **Python 3.7+**
- No external packages required (uses Python standard library: `json`, `heapq`).

### Clone the Repository
```bash
git clone https://github.com/BluPizarra/DASTRUC-Travel-Route-Planner.git
cd DASTRUC-Travel-Route-Planner
```

### Run the Application
```bash
python travel_route_planner.py
```
*(Or run `python "[DASTRUC]PIZARRA_CODE_FINAL TASK.py"`)*

---

## How It Works

### Menu Options
1. **Add Location**: Register a new location/node in the graph.
2. **Add Road**: Connect two existing locations with a specified distance (bidirectional edge).
3. **Find Shortest Path**: Compute and display the shortest path sequence and total distance between a start and destination using Dijkstra's Algorithm.
4. **List Locations**: List all saved locations in the graph.
5. **Show Graph**: Display the full adjacency list and connection weights.
6. **Save Data**: Export the current graph to `routes.json`.
7. **Load Data**: Import a graph configuration from `routes.json`.
0. **Exit**: Save current state and exit the program.

### Sample Preloaded Graph (`routes.json`)
The included `routes.json` file contains sample Metro Manila routes:
- **Manila** $\leftrightarrow$ **Quezon City** (10.0 units)
- **Quezon City** $\leftrightarrow$ **Makati** (8.0 units)
- **Makati** $\leftrightarrow$ **Taguig** (5.0 units)
- **Taguig** $\leftrightarrow$ **Manila** (20.0 units)

Finding the shortest path from **Manila** to **Taguig**:
- Manila $\rightarrow$ Quezon City $\rightarrow$ Makati $\rightarrow$ Taguig (Distance: 23.0) vs Direct (Distance: 20.0)
- Optimal Path: `Manila -> Taguig` (Distance: 20.0)

---

## Author

**Bludylan Cyrus A. Pizarra**  
GitHub: [@BluPizarra](https://github.com/BluPizarra)
