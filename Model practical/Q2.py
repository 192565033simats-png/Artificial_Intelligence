import math
def check_winner(board):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8), # Rows
        (0,3,6), (1,4,7), (2,5,8), # Columns
        (0,4,8), (2,4,6)           # Diagonals
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Draw'
    return None
def alphabeta(board, depth, alpha, beta, is_maximizing):
    result = check_winner(board)
    if result == 'X':
        return 10 - depth
    elif result == 'O':
        return depth - 10
    elif result == 'Draw':
        return 0
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval_score = alphabeta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval_score = alphabeta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval
def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = alphabeta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move
board = [
    'X', 'O', 'X',
    'O', 'O', ' ',
    ' ', ' ', ' '
]
move = find_best_move(board)
print(f"Best move index for AI (X): {move} (Row {move//3 + 1}, Col {move%3 + 1})")
board[move] = 'X'
for r in range(0, 9, 3):
    print(board[r:r+3])