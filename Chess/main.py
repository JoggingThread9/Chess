import sys
from board import *
import copy

pygame.init()

yellow = (240, 240, 0)
white = (215, 211, 186)
black = (0, 0, 0)
grey = (125, 125, 125)
red = (250, 20, 20)

cols = 8
rows = 8

size = 90

display = pygame.display.set_mode((cols * size, rows * size))

clock = pygame.time.Clock()

font = pygame.font.Font(None, 100)

def print_array(array):
    for i in array:
        print(i)


def get_clicked_pos(pos, size):
    gap = size
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


highlight_square = False

turn = 1

current = False

start_state = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
              ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
              ['0', '0', '0', '0', '0', '0', '0', '0'],
              ['0', '0', '0', '0', '0', '0', '0', '0'],
              ['0', '0', '0', '0', '0', '0', '0', '0'],
              ['0', '0', '0', '0', '0', '0', '0', '0'],
              ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
              ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]

game_board = copy.deepcopy(start_state)

white_in_check = False
black_in_check = False

stalemate = False
win = False

while True:
    wk_pos = find_king_pos('white', game_board)
    bk_pos = find_king_pos('black', game_board)

    display.fill(white)
    draw_squares(display)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # checks if the uses quits the game
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col, row = get_clicked_pos(pos, size)
            highlight_square = True
            selected_piece = get_selected_piece(row, col, game_board)

            if current:
                if [row, col] in current.valid_moves:
                    game_board[current_row][current_col] = '0'
                    game_board[row][col] = '0'
                    game_board[row][col] = current_piece

                    current = False
                    highlight_square = False
                    selected_piece = False

                    white_in_check = in_check('white', game_board)
                    black_in_check = in_check('black', game_board)

                    turn += 1

    if not white_in_check:
        if checkmate('white', game_board):
            stalemate = True

    elif not black_in_check:
        if checkmate('black', game_board):
            stalemate = True

    if white_in_check:
        pygame.draw.rect(display, red, (wk_pos[1]*size, wk_pos[0]*size, size, size))
        if checkmate('white', game_board):
            win = True
            winner = 'black'

    elif black_in_check:
        pygame.draw.rect(display, red, (bk_pos[1]*size, bk_pos[0]*size, size, size))
        if checkmate('black', game_board):
            win = True
            winner = 'white'

    draw_pieces(display, game_board)

    if win:
        if winner == 'white':
            display.fill(black)
            text = font.render(winner, True, white)
            display.blit(display, ((cols*size)/2, (rows*size)/2))


    if highlight_square:
        if turn % 2 != 0:
            if 'w' in selected_piece:
                if selected_piece == 'wK':
                    current = King
                elif selected_piece == 'wQ':
                    current = Queen
                elif selected_piece == 'wR':
                    current = Rook
                elif selected_piece == 'wB':
                    current = Bishop
                elif selected_piece == 'wN':
                    current = Knight
                elif selected_piece == 'wP':
                    current = Pawn
                pygame.draw.rect(display, yellow, (col * size, row * size, size, size))
                draw_pieces(display, game_board)
                current.find_valid_moves(row, col, 'white', game_board)
                for i in current.valid_moves:
                    pygame.draw.circle(display, grey, center=((i[1] * size) + size / 2, (i[0] * size) + size / 2), radius=10)

                current_piece = selected_piece
                current_row = row
                current_col = col

        else:
            if 'b' in selected_piece:
                if selected_piece == 'bK':
                    current = King
                elif selected_piece == 'bQ':
                    current = Queen
                elif selected_piece == 'bR':
                    current = Rook
                elif selected_piece == 'bB':
                    current = Bishop
                elif selected_piece == 'bN':
                    current = Knight
                elif selected_piece == 'bP':
                    current = Pawn

                pygame.draw.rect(display, yellow, (col * size, row * size, size, size))
                draw_pieces(display, game_board)
                current.find_valid_moves(row, col, 'black', game_board)
                for i in current.valid_moves:
                    pygame.draw.circle(display, grey, center=((i[1] * size) + size / 2, (i[0] * size) + size / 2), radius=10)

                current_piece = selected_piece
                current_row = row
                current_col = col

    pygame.display.update()
    clock.tick(120)

# todo: make a material counter by going over every square and seeing how much of each piece is on the game_board
# todo: make it so you can castle
# todo: make pawn promotion
# make en passent

# todo: make an engine
