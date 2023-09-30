def bfs(graph, start):
    visited = set()
    queue = []
    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end="\t")

        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

    print("BFS starting from 2")
    bfs(graph, 2)
