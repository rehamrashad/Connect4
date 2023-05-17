import pygame

SQUARE = 80
Rows = 6
Cols = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

EMPTY = 0
AI1_PIECE = 1
AI2_PIECE = 2


RADIUS = int(SQUARE / 2 - 5)
width = Cols * SQUARE
height = (Rows + 1) * SQUARE
size = (width, height)

screen = pygame.display.set_mode(size)

def drawBoard(board):
    for c in range(Cols):
        for r in range(Rows):
            pygame.draw.rect(screen, BLUE, (c * SQUARE, r * SQUARE + SQUARE, SQUARE, SQUARE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARE + SQUARE / 2), int(r * SQUARE + SQUARE + SQUARE / 2)), RADIUS)

    for c in range(Cols):
        for r in range(Rows):
            if board[r][c] == AI1_PIECE:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARE + SQUARE / 2), height - int(r * SQUARE + SQUARE / 2)), RADIUS)
            elif board[r][c] == AI2_PIECE:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARE + SQUARE / 2), height - int(r * SQUARE + SQUARE / 2)), RADIUS)
    pygame.display.update()
