from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat_position):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_position = boat_position

    def is_valid(self):
        if (
            0 <= self.missionaries <= 3
            and 0 <= self.cannibals <= 3
            and 0 <= self.boat_position <= 1
        ):
            if (
                self.missionaries == 0
                or self.missionaries == 3
                or self.missionaries >= self.cannibals
            ):
                return True
        return False

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat_position == 0

def generate_next_states(current_state):
    next_states = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for m, c in moves:
        if current_state.boat_position == 1:
            new_state = State(
                current_state.missionaries - m,
                current_state.cannibals - c,
                0,
            )
        else:
            new_state = State(
                current_state.missionaries + m,
                current_state.cannibals + c,
                1,
            )

        if new_state.is_valid():
            next_states.append(new_state)

    return next_states

def missionaries_cannibals_bfs():
    start_state = State(3, 3, 1)

    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state.is_goal():
            return path

        next_states = generate_next_states(current_state)
        for next_state in next_states:
            queue.append((next_state, path + [current_state]))

    return None

# Example usage:
solution_path = missionaries_cannibals_bfs()

if solution_path:
    print("Solution Path:")
    for i, state in enumerate(solution_path):
        print("Step", i + 1, ":")
        print(state.missionaries, "Missionaries and", state.cannibals, "Cannibals on the Left Shore,", 3 - state.missionaries, "Missionaries and", 3 - state.cannibals, "Cannibals on the Right Shore")
        print("")
else:
    print("No solution found.")
