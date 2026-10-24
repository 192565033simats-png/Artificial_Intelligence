# Alpha-Beta Pruning Algorithm

def alphabeta(depth, index, maximizing, values, alpha, beta):
    if depth == 2:
        return values[index]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            value = alphabeta(
                depth + 1, index * 2 + i,
                False, values, alpha, beta
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alphabeta(
                depth + 1, index * 2 + i,
                True, values, alpha, beta
            )
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alphabeta(
    0, 0, True, values,
    float('-inf'), float('inf')
)

print("Best value:", result)
