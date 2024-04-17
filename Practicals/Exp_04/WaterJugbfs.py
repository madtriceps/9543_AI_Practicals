from collections import deque

def water_jug_bfs(X, Y, Z):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()
        if x == Z or y == Z:
            return path

        visited.add((x, y))

        # Fill jug 1
        if (X, y) not in visited:
            queue.append(((X, y), path + [(X, y)]))

        # Fill jug 2
        if (x, Y) not in visited:
            queue.append(((x, Y), path + [(x, Y)]))

        # Empty jug 1
        if (0, y) not in visited:
            queue.append(((0, y), path + [(0, y)]))

        # Empty jug 2
        if (x, 0) not in visited:
            queue.append(((x, 0), path + [(x, 0)]))

        # Pour water from jug 1 to jug 2
        pour_amount = min(x, Y - y)
        if (x - pour_amount, y + pour_amount) not in visited:
            queue.append(((x - pour_amount, y + pour_amount), path + [(x - pour_amount, y + pour_amount)]))

        # Pour water from jug 2 to jug 1
        pour_amount = min(X - x, y)
        if (x + pour_amount, y - pour_amount) not in visited:
            queue.append(((x + pour_amount, y - pour_amount), path + [(x + pour_amount, y - pour_amount)]))

    return None

# Example usage:
X = 4
Y = 3
Z = 2
solution_path = water_jug_bfs(X, Y, Z)

if solution_path:
    print("Steps to measure", Z, "gallons:")
    for i, (x, y) in enumerate(solution_path):
        print("Step", i + 1, ": Jug 4:", x, "gallons, Jug 3:", y, "gallons")
else:
    print("No solution found.")
