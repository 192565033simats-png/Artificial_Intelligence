from collections import deque

start = (3, 3, 0)
goal = (0, 0, 1)

def valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (3-m == 0 or 3-m >= 3-c))

def solve():
    q = deque([(start, [])])
    visited = {start}
    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    while q:
        state, path = q.popleft()
        m, c, b = state

        if state == goal:
            print(path + [state])
            return

        for x, y in moves:
            if b == 0:
                new = (m-x, c-y, 1)
            else:
                new = (m+x, c+y, 0)

            if (valid(new[0], new[1]) and
                    new not in visited and
                    0 <= new[0] <= 3 and
                    0 <= new[1] <= 3):
                visited.add(new)
                q.append((new, path + [state]))

solve()
