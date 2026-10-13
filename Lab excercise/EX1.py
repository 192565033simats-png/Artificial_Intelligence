from collections import deque

def solve_puzzle(start, goal):
    q = deque([(start, [])])
    visited = set()

    while q:
        state, path = q.popleft()

        if state == goal:
            print("Solution:")
            for p in path:
                print(p)
            print(state)
            return

        visited.add(state)

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)

                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited:
                    q.append((new_state, path + [state]))

# 0 represents blank space
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solve_puzzle(start, goal)
