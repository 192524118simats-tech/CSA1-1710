from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print((x, y))

        if x == 2:   # Goal: 2 liters in Jug A
            print("Goal Reached!")
            return

        next_states = [
            (4, y),                     # Fill Jug A
            (x, 3),                     # Fill Jug B
            (0, y),                     # Empty Jug A
            (x, 0),                     # Empty Jug B
            (x - min(x, 3 - y), y + min(x, 3 - y)),  # A -> B
            (x + min(y, 4 - x), y - min(y, 4 - x))   # B -> A
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

water_jug()