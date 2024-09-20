import pygame
from game import TicTacToe
import json

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (192, 192, 192)

board_size = 500
cell_size = board_size // 3
start_x = (width - board_size) // 2
start_y = (height - board_size) // 2

game = TicTacToe()

font = pygame.font.SysFont(None, 60)

def draw_board():
    screen.fill(WHITE)

    board = json.loads(game.get_board())
    print(board)

    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (start_x + i * cell_size, start_y), 
                         (start_x + i * cell_size, start_y + board_size), 5)
        pygame.draw.line(screen, BLACK, (start_x, start_y + i * cell_size), 
                         (start_x + board_size, start_y + i * cell_size), 5)

    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                pygame.draw.line(screen, RED, 
                                 (start_x + c * cell_size + 20, start_y + r * cell_size + 20),
                                 (start_x + (c + 1) * cell_size - 20, start_y + (r + 1) * cell_size - 20), 5)
                pygame.draw.line(screen, RED, 
                                 (start_x + (c + 1) * cell_size - 20, start_y + r * cell_size + 20),
                                 (start_x + c * cell_size + 20, start_y + (r + 1) * cell_size - 20), 5)
            elif board[r][c] == "O":
                pygame.draw.circle(screen, BLUE, 
                                   (start_x + c * cell_size + cell_size // 2, start_y + r * cell_size + cell_size // 2),
                                   cell_size // 2 - 20, 5)

def get_cell(pos):
    x, y = pos
    if start_x <= x <= start_x + board_size and start_y <= y <= start_y + board_size:
        return (y - start_y) // cell_size, (x - start_x) // cell_size  
    return None

def display_message(message, color):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, GRAY, background_rect)
    screen.blit(text, text_rect)

running = True
game_over = False
message = ""

while running:
    draw_board()

    if game_over:
        display_message(message, RED)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            cell = get_cell(pygame.mouse.get_pos())
            if cell:
                row, col = cell  
                if game.player_move(row, col): 
                    game.pc_move()
                    if game.check_winner('X'):
                        message = "¡Ganaste!"
                        game_over = True
                    elif game.check_winner('O'):
                        message = "Perdiste"
                        game_over = True
                    elif all(cell != "" for row in game.board for cell in row):
                        message = "Empate"
                        game_over = True

    pygame.display.update()

pygame.quit()
