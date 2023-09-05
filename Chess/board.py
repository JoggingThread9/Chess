import pygame
from pieces import *

cols = 8
rows = 8

size = 90
green = (32, 125, 57)


def draw_squares(display):
    alternate = False
    for row in range(rows):
        if not alternate:
            for col in range(1, cols, 2):
                pygame.draw.rect(display, green, (col * size, row * size, size, size))
            alternate = True
        elif alternate:
            for col in range(0, cols, 2):
                pygame.draw.rect(display, green, (col * size, row * size, size, size))
            alternate = False


pieces = {'bB': pygame.transform.scale(pygame.image.load('assets/bB.svg'), (size, size)),
          'bK': pygame.transform.scale(pygame.image.load('assets/bK.svg'), (size, size)),
          'bN': pygame.transform.scale(pygame.image.load('assets/bN.svg'), (size, size)),
          'bP': pygame.transform.scale(pygame.image.load('assets/bP.svg'), (size, size)),
          'bQ': pygame.transform.scale(pygame.image.load('assets/bQ.svg'), (size, size)),
          'bR': pygame.transform.scale(pygame.image.load('assets/bR.svg'), (size, size)),
          'wB': pygame.transform.scale(pygame.image.load('assets/wB.svg'), (size, size)),
          'wK': pygame.transform.scale(pygame.image.load('assets/wK.svg'), (size, size)),
          'wN': pygame.transform.scale(pygame.image.load('assets/wN.svg'), (size, size)),
          'wP': pygame.transform.scale(pygame.image.load('assets/wP.svg'), (size, size)),
          'wQ': pygame.transform.scale(pygame.image.load('assets/wQ.svg'), (size, size)),
          'wR': pygame.transform.scale(pygame.image.load('assets/wR.svg'), (size, size))}


def draw_pieces(display, game_board):
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            piece = game_board[row][col]
            if piece != '0':
                display.blit(pieces[piece], (col * size, row * size))


def get_selected_piece(row, col, game_board):
    return str(game_board[row][col])


def in_check(color, game_board):
    if color == 'white':
        king_pos = find_king_pos('white', game_board)
    if color == 'black':
        king_pos = find_king_pos('black', game_board)

    if color == 'white':
        for r in range(len(game_board)):
            for c in range(len(game_board[r])):
                if 'bQ' == game_board[r][c]:
                    Queen.find_all_moves(r, c, 'black', game_board)
                    if king_pos in Queen.moves:
                        return True
                elif 'bR' == game_board[r][c]:
                    Rook.find_all_moves(r, c, 'black', game_board)
                    if king_pos in Rook.moves:
                        return True
                elif 'bB' == game_board[r][c]:
                    Bishop.find_all_moves(r, c, 'black', game_board)
                    if king_pos in Bishop.moves:
                        return True
                elif 'bK' == game_board[r][c]:
                    Knight.find_all_moves(r, c, 'black', game_board)
                    if king_pos in Knight.moves:
                        return True
                elif 'bP' == game_board[r][c]:
                    Pawn.find_all_moves(r, c, 'black', game_board)
                    if king_pos in Pawn.moves:
                        return True

    else:
        for r in range(len(game_board)):
            for c in range(len(game_board[r])):
                if 'wQ' == game_board[r][c]:
                    Queen.find_all_moves(r, c, 'white', game_board)
                    if king_pos in Queen.moves:
                        return True
                elif 'wR' == game_board[r][c]:
                    Rook.find_all_moves(r, c, 'white', game_board)
                    if king_pos in Rook.moves:
                        return True
                elif 'wB' == game_board[r][c]:
                    Bishop.find_all_moves(r, c, 'white', game_board)
                    if king_pos in Bishop.moves:
                        return True
                elif 'wN' == game_board[r][c]:
                    Knight.find_all_moves(r, c, 'white', game_board)
                    if king_pos in Knight.moves:
                        return True
                elif 'wP' == game_board[r][c]:
                    Pawn.find_all_moves(r, c, 'white', game_board)
                    if king_pos in Pawn.moves:
                        return True
    return False


def find_king_pos(color, game_board):
    if color == 'white':
        for r in range(len(game_board)-1, 0, -1):
            for c in range(len(game_board)-1, 0, -1):
                if game_board[r][c] == 'wK':
                    return [r, c]

    if color == 'black':
        for r in range(len(game_board)):
            for c in range(len(game_board[r])):
                if game_board[r][c] == 'bK':
                    return [r, c]


def checkmate(color, game_board):
    moves = []
    for r in range(len(game_board)):
        for c in range(len(game_board[r])):
            if game_board[r][c] != '0':
                if color == 'white':
                    if 'w' in game_board[r][c]:
                        if 'wK' == game_board[r][c]:
                            King.find_valid_moves(r, c, color, game_board)
                            moves.append(King.valid_moves)
                        elif 'wQ' == game_board[r][c]:
                            Queen.find_valid_moves(r, c, color, game_board)
                            moves.append(Queen.valid_moves)
                        elif 'wR' == game_board[r][c]:
                            Rook.find_valid_moves(r, c, color, game_board)
                            moves.append(Rook.valid_moves)
                        elif 'wB' == game_board[r][c]:
                            Bishop.find_valid_moves(r, c, color, game_board)
                            moves.append(Bishop.valid_moves)
                        elif 'wN' == game_board[r][c]:
                            Knight.find_valid_moves(r, c, color, game_board)
                            moves.append(Knight.valid_moves)
                        elif 'wP' == game_board[r][c]:
                            Pawn.find_valid_moves(r, c, color, game_board)
                            moves.append(Pawn.valid_moves)
                else:
                    if 'b' in game_board[r][c]:
                        if 'bK' == game_board[r][c]:
                            King.find_valid_moves(r, c, color, game_board)
                            moves.append(King.valid_moves)
                        elif 'bQ' == game_board[r][c]:
                            Queen.find_valid_moves(r, c, color, game_board)
                            moves.append(Queen.valid_moves)
                        elif 'bR' == game_board[r][c]:
                            Rook.find_valid_moves(r, c, color, game_board)
                            moves.append(Rook.valid_moves)
                        elif 'bB' == game_board[r][c]:
                            Bishop.find_valid_moves(r, c, color, game_board)
                            moves.append(Bishop.valid_moves)
                        elif 'bN' == game_board[r][c]:
                            Knight.find_valid_moves(r, c, color, game_board)
                            moves.append(Knight.valid_moves)
                        elif 'bP' == game_board[r][c]:
                            Pawn.find_valid_moves(r, c, color, game_board)
                            moves.append(Pawn.valid_moves)

    for i in moves:
        if len(i) != 0:
            return False

    return True



