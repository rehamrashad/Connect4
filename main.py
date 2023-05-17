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

num_row = 6
num_col = 7

PLAYER = 0
AI = 1
#
# EMPTY = 0
# PLAYER_PIECE = 1
# AI_PIECE = 2
#
# WINDOW_LENGTH = 4

def create_board():
    board = np.zeros((num_row, num_col))
    return board

def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False

pygame.init()

SQUARE_SIZE = 80
width = num_col * SQUARE_SIZE
height = (num_row + 1) * SQUARE_SIZE
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
        if Is_valid(board, col):
            # pygame.time.wait(500)
            row = Find_next_row(board, col)
            put_piece(board, row, col, AI1)

            if Best_move(board, AI1):
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
        if Is_valid(board, col):
            row = Find_next_row(board, col)
            put_piece(board, row, col, AI2)

            if Best_move(board, AI2):
                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(3000)