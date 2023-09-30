def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)

        for neigh in graph[start]:
            dfs(graph, start, visited)


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": []}  # TODO incomplete
    visited = set()
    print("DFS")
    dfs(graph, "A", visited)
