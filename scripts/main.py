import pygame
import sys
import time
import tictactoeBot as tttb

# CONSTANTS
SIZE = WIDTH, HEIGHT = 600, 400
# Colors
BG_COLOR = (0, 173, 181)
LINE_COLOR = (57, 62, 70)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 99, 99)
GREY = (34, 40, 49)
YELLOW = (238, 238, 23)
pygame.init()
# Fonts
FONT_PATH = r'assets\font\Comfortaa-Regular.ttf'
MEDIUM_FONT = pygame.font.Font(FONT_PATH, 28)
LARGE_FONT = pygame.font.Font(FONT_PATH, 40)
MOVE_FONT = pygame.font.Font(FONT_PATH, 60)

user = None
board = tttb.initial_state()
ai_turn = False
screen = pygame.display.set_mode(SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BG_COLOR)

    # Let user choose a player.
    if user is None:
        # Draw title
        title = LARGE_FONT.render("Play Tic-Tac-Toe", True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((WIDTH / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((WIDTH / 8), (HEIGHT / 2), WIDTH / 4, 50)
        playX = MEDIUM_FONT.render("Play as X", True, BLACK)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, RED, playXButton)
        screen.blit(playX, playXRect)
        playOButton = pygame.Rect(5 * (WIDTH / 8), (HEIGHT / 2), WIDTH / 4, 50)
        playO = MEDIUM_FONT.render("Play as O", True, BLACK)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, RED, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = tttb.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = tttb.O
    else:
        # Draw game board
        tile_size = 80
        tile_origin = (WIDTH / 2 - (1.5 * tile_size),
                       HEIGHT / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, LINE_COLOR, rect, 3)
                if board[i][j] != tttb.EMPTY:
                    move = MOVE_FONT.render(board[i][j], True, YELLOW)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)
        game_over = tttb.terminal(board)
        player = tttb.player(board)

        # Show title
        if game_over:
            winner = tttb.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = LARGE_FONT.render(title, True, GREY)
        titleRect = title.get_rect()
        titleRect.center = ((WIDTH / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = tttb.minimax(board)
                board = tttb.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == tttb.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = tttb.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(WIDTH / 3, HEIGHT - 65, WIDTH / 3, 50)
            again = MEDIUM_FONT.render("Play Again", True, BLACK)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, WHITE, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = tttb.initial_state()
                    ai_turn = False

    pygame.display.flip()
