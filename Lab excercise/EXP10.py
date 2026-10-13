import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = {}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", g)
            return

        if node in visited and visited[node] <= g:
            continue

        visited[node] = g

        for neighbour, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neighbour]

            heapq.heappush(
                queue,
                (new_f, new_g, neighbour, path + [neighbour])
            )

    print("No path found")

astar('A', 'G')
