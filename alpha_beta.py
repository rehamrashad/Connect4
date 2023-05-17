import math
import random

AI1_PIECE = 1
AI2_PIECE = 2
Rows = 6
Cols = 7
WINDOW = 4
EMPTY = 0

def isWin(board, piece):
    # -
    for c in range(Cols - 3):
        for r in range(Rows):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # |
    for c in range(Cols):
        for r in range(Rows - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # /
    for c in range(Cols - 3):
        for r in range(Rows - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # \
    for c in range(Cols - 3):
        for r in range(3, Rows):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def getValidLocation(board):
    valid_locations = []
    for col in range(Cols):
        if isValidLocation(board, col):
            valid_locations.append(col)
    return valid_locations


def isTerminal(board):
    return isWin(board, AI1_PIECE) or isWin(board, AI2_PIECE) or len(getValidLocation(board)) == 0
def score_position(board, piece):
    score = 0

    # Score center column
    center_array = [int(i) for i in list(board[:, Cols // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # -
    for r in range(Rows):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(Cols - 3):
            window = row_array[c:c + WINDOW]
            score += evaluate_window(window, piece)

    # |
    for c in range(Cols):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(Rows - 3):
            window = col_array[r:r + WINDOW]
            score += evaluate_window(window, piece)

    # /
    for r in range(Rows - 3):
        for c in range(Cols - 3):
            window = [board[r + i][c + i] for i in range(WINDOW)]
            score += evaluate_window(window, piece)

    # \
    for r in range(Rows - 3):
        for c in range(Cols - 3):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW)]
            score += evaluate_window(window, piece)
    return score



def isValidLocation(board, col):
    return board[Rows - 1][col] == 0

def putPiece(board, row, col, piece):
    board[row][col] = piece

def nextRow(board, col):
    for r in range(Rows):
        if board[r][col] == 0:
            return r


def evaluate_window(window, piece):
    score = 0
    opp_piece = AI1_PIECE
    if piece == AI1_PIECE:
        opp_piece = AI2_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def AlphaBeta(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = getValidLocation(board)
    is_terminal = isTerminal(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if isWin(board, AI2_PIECE):
                return (None, 100000000000000)
            elif isWin(board, AI1_PIECE):
                return (None, -10000000000000)
            else:  #  no  valid moves
                return (None, 0)
        else:  # depth = zero
            return (None, score_position(board, AI2_PIECE))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = nextRow(board, col)
            b_copy = board.copy()
            putPiece(b_copy, row, col, AI2_PIECE)
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
            row = nextRow(board, col)
            b_copy = board.copy()
            putPiece(b_copy, row, col, AI1_PIECE)
            new_score = AlphaBeta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
