def dfs(graph, start, goal):
    """Perform DFS to find the shortest path from start to goal."""
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in graph.adjacency_list[current]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    
    return None  # If no path is found
