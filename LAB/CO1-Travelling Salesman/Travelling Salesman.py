from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
cities = list(range(1, n))

min_cost = float('inf')

for perm in permutations(cities):
    cost = 0
    current = 0

    for city in perm:
        cost += graph[current][city]
        current = city

    cost += graph[current][0]

    if cost < min_cost:
        min_cost = cost

print("Minimum Cost:", min_cost)