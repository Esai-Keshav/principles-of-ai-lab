# Define a depth-first search (DFS) function that traverses a graph.
# Parameters:
# - 'graph': The graph represented as an adjacency list.
# - 'start': The starting vertex for the DFS traversal.
# - 'visited': A set to keep track of visited vertices.


def dfs(graph, start, visited):
    # Check if the 'start' vertex has not been visited.
    if start not in visited:
        # Print the current 'start' vertex as part of the traversal.
        print(start, end=" ")
        # Mark the 'start' vertex as visited by adding it to the 'visited' set.
        visited.add(start)
        # Explore neighbors of the current 'start' vertex using recursion.
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)


# Example usage:
if __name__ == "__main__":
    # Define a sample graph as an adjacency list where letters represent vertices.
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    # Create an empty set 'visited' to keep track of visited vertices during DFS.
    visited = set()

    # Print a message indicating the start of the DFS traversal.
    print("Depth-First Traversal (starting from vertex 'A'):")

    # Call the 'dfs' function with the sample graph, starting vertex 'A', and the 'visited' set.
    dfs(graph, "A", visited)
