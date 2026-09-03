import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 0
}

def astar(start, goal):
    pq = [(heuristic[start], 0, start, [])]

    while pq:
        f, g, node, path = heapq.heappop(pq)
        path = path + [node]

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        for neighbour, cost in graph[node]:
            heapq.heappush(
                pq,
                (g + cost + heuristic[neighbour],
                 g + cost,
                 neighbour,
                 path)
            )

astar('A', 'F')
