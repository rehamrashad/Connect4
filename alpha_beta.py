import math
import random

AI1 = 1
AI2 = 2
num_row = 6
num_col = 7
window_Ln = 4
empty = 0
def Find_valid_location(board):
    valid_locations = []
    for col in range(num_col):
        if Is_valid(board, col):
            valid_locations.append(col)
    return valid_locations

def Is_valid(board, col):
    return board[num_row - 1][col] == 0

def Find_next_row(board, col):
    for r in range(num_row):
        if board[r][col] == 0:
            return r
        
def Best_move(board, piece):
    # Check horizontal locations for win
    for c in range(num_col - 3):
        for r in range(num_row):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(num_col):
        for r in range(num_row - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(num_col - 3):
        for r in range(num_row - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(num_col - 3):
        for r in range(3, num_row):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def put_piece(board, row, col, piece):
    board[row][col] = piece

def is_terminal_node(board):
    return Best_move(board, AI1) or Best_move(board, AI2) or len(Find_valid_location(board)) == 0

def Find_score_positions(board, piece):
    score = 0
    # Score center column
    center = [int(i) for i in list(board[:, num_col // 2])]
    center_count = center.count(piece)
    score += center_count * 3

    # Score Horizontal
    for r in range(num_row):
        row_positions = [int(i) for i in list(board[r, :])]
        for c in range(num_col - 3):
            window = row_positions[c:c + window_Ln]
            score += Score_window_counter(window, piece)

    # Score Vertical
    for c in range(num_col):
        col_positions = [int(i) for i in list(board[:, c])]
        for r in range(num_row - 3):
            window = col_positions[r:r + window_Ln]
            score += Score_window_counter(window, piece)

    # Score positive sloped diagonal
    for r in range(num_row - 3):
        for c in range(num_col - 3):
            window = [board[r + i][c + i] for i in range(window_Ln)]
            score += Score_window_counter(window, piece)

    for r in range(num_row - 3):
        for c in range(num_col - 3):
            window = [board[r + 3 - i][c + i] for i in range(window_Ln)]
            score += Score_window_counter(window, piece)

    return score

def Score_window_counter(window, piece):
    score = 0
    opposite_player  = AI1
    if piece == AI1:
        opposite_player  = AI2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(empty) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(empty) == 2:
        score += 2

    if window.count(opposite_player ) == 3 and window.count(empty) == 1:
        score -= 4

    return score

def AlphaBeta(board, depth, alpha, beta, MX_player):
    valid_locations = Find_valid_location(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if Best_move(board, AI2):
                return (None, 100000000000000)
            elif Best_move(board, AI1):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, Find_score_positions(board, AI2))
    if MX_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = Find_next_row(board, col)
            b_copy = board.copy()
            put_piece(b_copy, row, col, AI2)
            new_score = AlphaBeta(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = Find_next_row(board, col)
            b_copy = board.copy()
            put_piece(b_copy, row, col, AI1)
            new_score = AlphaBeta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
