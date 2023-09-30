import heapq

# Define a grid (0 represents empty, 1 represents obstacles)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

# Define the start and goal positions
start = (0, 0)
goal = (4, 4)


# Define a heuristic function (Manhattan distance)
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# A* algorithm
def astar(grid, start, goal):
    open_list = [(0.0, start)]  # Priority queue (f-score, node)
    came_from = {}  # Dictionary to store the parent node of each node

    # Initialize g_score with all nodes set to infinity
    g_score = {
        (x, y): float("inf") for x in range(len(grid)) for y in range(len(grid[0]))
    }
    g_score[start] = 0

    f_score = {node: float("inf") for node in g_score}
    f_score[start] = heuristic(start, goal)

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current[0] + neighbor[0], current[1] + neighbor[1]

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[(x, y)]:
                    came_from[(x, y)] = current
                    g_score[(x, y)] = tentative_g_score
                    f_score[(x, y)] = tentative_g_score + heuristic((x, y), goal)
                    heapq.heappush(open_list, (f_score[(x, y)], (x, y)))

    return None  # No path found


# Find the path
path = astar(grid, start, goal)

if path:
    print("Path found:")
    for node in path:
        print(node)
else:
    print("No path found.")
