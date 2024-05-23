from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

def bfs(graph, start, goal):
    """Perform BFS to find the shortest path from start to goal."""
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for neighbor in graph.adjacency_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # If no path is found

