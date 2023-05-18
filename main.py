import sys
import time

import numpy as np
from alpha_beta import *
from gui import *
from minmax import *
from gui2 import *

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROWS = 6
COLS = 7
SQUARE = 80

AI1 = 0
AI2 = 1

width = COLS * SQUARE
height = (ROWS + 1) * SQUARE
size = (width, height)


def initBoard():
    board = np.zeros((ROWS, COLS))
    return board


def chooseDifficulty(level):
    if level == "Easy":
        return 1
    elif level == "Medium":
        return 3
    else:
        return 5


def main():
    app.mainloop()
    root.withdraw()
    board = initBoard()
    gameOver = False
    pygame.init()
    screen = pygame.display.set_mode(size)
    drawBoard(board)
    pygame.display.update()
    font = pygame.font.SysFont("Tahoma", 40)
    turn = AI1

    while not gameOver:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if turn == AI1 and not gameOver:
            difficulty = chooseDifficulty(AI1_Level)
            if AI1_Option == "MinMax":
                col, minimax_score = minimax(board, difficulty, True)
            elif AI1_Option == "AlphaBeta":
                col, minimax_score = AlphaBeta(board, difficulty, -math.inf, math.inf, True)
            else:
                col = random.randint(0, 6)
            if isValidLocation(board, col):
                row = nextRow(board, col)
                putPiece(board, row, col, AI1_PIECE)

                if isWin(board, AI1_PIECE):
                    label = font.render("The Winner is Player 1 ", True, RED)
                    screen.blit(label, (40, 10))
                    gameOver = True

                drawBoard(board)
                turn += 1
                turn = turn % 2
                time.sleep(1)
            else:
                label = font.render("Draw!! GAME OVER", True, WHITE)
                screen.blit(label, (40, 10)),
                gameOver = True
                drawBoard(board)

        if turn == AI2 and not gameOver:
            difficulty = chooseDifficulty(AI2_Level)
            if AI2_Option == "MinMax":
                col, minimax_score = minimax(board, difficulty, True)
            elif AI2_Option == "AlphaBeta":
                col, minimax_score = AlphaBeta(board, difficulty, -math.inf, math.inf, True)
            else:
                col = random.randint(0, 6)

            if isValidLocation(board, col):
                row = nextRow(board, col)
                putPiece(board, row, col, AI2_PIECE)

                if isWin(board, AI2_PIECE):
                    label = font.render("The Winner is Player 2 ", True, YELLOW)
                    screen.blit(label, (40, 10))
                    gameOver = True

                drawBoard(board)

                turn += 1
                turn = turn % 2
            else:
                label = font.render("Draw!! GAME OVER", True, WHITE)
                screen.blit(label, (40, 10)),
                gameOver = True
                drawBoard(board)

        if gameOver:
            pygame.time.wait(5000)


main()
