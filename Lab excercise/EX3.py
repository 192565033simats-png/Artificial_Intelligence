from collections import deque

def water_jug():
    jug1 = 4
    jug2 = 3
    goal = 2

    q = deque([(0, 0, [])])
    visited = set()

    while q:
        a, b, path = q.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == goal or b == goal:
            print("Solution:")
            for state in path:
                print(state)
            return

        states = [
            (jug1, b),                 # Fill Jug 1
            (a, jug2),                 # Fill Jug 2
            (0, b),                    # Empty Jug 1
            (a, 0),                    # Empty Jug 2

            # Pour Jug 1 -> Jug 2
            (a - min(a, jug2 - b),
             b + min(a, jug2 - b)),

            # Pour Jug 2 -> Jug 1
            (a + min(b, jug1 - a),
             b - min(b, jug1 - a))
        ]

        for state in states:
            if state not in visited:
                q.append((state[0], state[1], path))


water_jug()
