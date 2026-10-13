from itertools import permutations

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
cities = list(range(1, n))
min_cost = float('inf')
best_path = []

for p in permutations(cities):
    path = [0] + list(p) + [0]
    cost = 0

    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Best Path:", best_path)
print("Minimum Distance:", min_cost)
