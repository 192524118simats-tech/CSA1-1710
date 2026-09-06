colors = ["Red", "Green", "Blue"]

neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

assignment = {}

def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve():
    if len(assignment) == len(neighbors):
        return True

    region = next(r for r in neighbors if r not in assignment)

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color

            if solve():
                return True

            del assignment[region]

    return False

if solve():
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution")