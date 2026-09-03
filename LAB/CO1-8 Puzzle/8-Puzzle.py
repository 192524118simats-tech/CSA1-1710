from collections import deque

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

def get_neighbors(state):
    neighbors = []
    index = state.index(0)

    moves = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
    }

    for move in moves[index]:
        new_state = state[:]
        new_state[index], new_state[move] = new_state[move], new_state[index]
        neighbors.append(new_state)

    return neighbors

def solve():
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        if state == goal:
            print("Solution Found:")
            for step in path + [state]:
                print(step)
            return

        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))

solve()