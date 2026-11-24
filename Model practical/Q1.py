from collections import deque
def water_jug_bfs(cap1=5, cap2=3, target=4):
    start = (0, 0)
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == target or y == target:
            return path
        next_states = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            # Pour 5L -> 3L
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            # Pour 3L -> 5L
            (x + min(y, cap1 - x), y - min(y, cap1 - x))
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(path + [state])
    return None
solution = water_jug_bfs()
print("Solution Path (5L, 3L):")
for step in solution:
    print(step)