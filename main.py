import sys
import time

import numpy as np
import pygame

from alpha_beta import *
from gui import draw_board
from minmax import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1
#
# EMPTY = 0
# PLAYER_PIECE = 1
# AI_PIECE = 2
#
# WINDOW_LENGTH = 4

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False

pygame.init()

SQUARE_SIZE = 80
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 40)

turn = random.randint(PLAYER, AI)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if turn == PLAYER and not game_over:
        col = random.randint(0, 6)
        #col, minimax_score = minimax(board, 5, True)
        if is_valid_location(board, col):
            # pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_PIECE)

            if winning_move(board, PLAYER_PIECE):
                label = myfont.render("Player 1 wins!!", 1, RED)
                screen.blit(label, (40, 10))
                game_over = True

            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2
            time.sleep(1)
    # # Ask for Player 2 Input
    if turn == AI and not game_over:

        col, minimax_score = AlphaBeta(board, 5, -math.inf, math.inf, True)
        #col = random.randint(0, 6)
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)

            if winning_move(board, AI_PIECE):
                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(3000)