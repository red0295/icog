from graph import Graph, read_cities
from bfs import bfs
from dfs import dfs

# Example usage
if __name__ == "__main__":
    # Create graph from file
    file_path = 'cities.txt'  # Path to the file containing city connections
    graph = read_cities(file_path)

    # Print the graph using the __str__ method
    print("Graph representation (adjacency list):")
    print(graph)

    # Perform BFS to find the shortest path
    start_city = "New York"
    goal_city = "Miami"
    bfs_path = bfs(graph, start_city, goal_city)

    if bfs_path:
        print(f"BFS shortest path from {start_city} to {goal_city}: {bfs_path}")
        graph.draw(path=bfs_path, title=f"BFS Shortest Path from {start_city} to {goal_city}")
    else:
        print(f"No path found from {start_city} to {goal_city} using BFS")

    # Perform DFS to find a path
    dfs_path = dfs(graph, start_city, goal_city)

    if dfs_path:
        print(f"DFS path from {start_city} to {goal_city}: {dfs_path}")
        graph.draw(path=dfs_path, title=f"DFS Path from {start_city} to {goal_city}")
    else:
        print(f"No path found from {start_city} to {goal_city} using DFS")

   
