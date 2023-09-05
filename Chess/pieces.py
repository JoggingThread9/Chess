import copy


class King:
    def __init__(self):
        self.moves_type = [[1, 0],
                           [-1, 0],

                           [0, 1],
                           [0, -1],

                           [1, 1],
                           [-1, -1],

                           [1, -1],
                           [-1, 1]]

        self.moves = []
        self.valid_moves = []

    def find_all_moves(self, row, col, color, game_board):
        self.moves = []
        for move in self.moves_type:
            if row + move[0] in range(len(game_board)):
                if col + move[1] in range(len(game_board[0])):
                    if color == 'white':
                        if game_board[row + move[0]][col + move[1]] == '0':
                            self.moves.append([row + move[0], col + move[1]])
                        if 'b' in game_board[row + move[0]][col + move[1]]:
                            self.moves.append([row + move[0], col + move[1]])
                    if color == 'black':
                        if game_board[row + move[0]][col + move[1]] == '0':
                            self.moves.append([row + move[0], col + move[1]])
                        if 'w' in game_board[row + move[0]][col + move[1]]:
                            self.moves.append([row + move[0], col + move[1]])

    def find_valid_moves(self, row, col, color, game_board):
        from board import in_check
        self.find_all_moves(row, col, color, game_board)
        self.valid_moves = []

        for move in self.moves:
            temp_board = copy.deepcopy(game_board)

            newr = move[0]
            newc = move[1]

            if color == 'white':
                piece = 'wK'
            else:
                piece = 'bK'

            temp_board[row][col] = '0'
            temp_board[newr][newc] = piece
            if not in_check(color, temp_board):
                self.valid_moves.append(move)


class Queen:
    def __init__(self):
        self.moves_type = [[1, 0],
                           [-1, 0],
                           [0, 1],
                           [0, -1],
                           [1, 1],
                           [-1, -1],
                           [1, -1],
                           [-1, 1]]

        self.moves = []
        self.valid_moves = []

    def find_all_moves(self, row, col, color, game_board):
        self.moves = []
        start_row = row
        start_col = col
        for move in self.moves_type:
            row = start_row
            col = start_col
            while True:
                row = row+move[0]
                col = col+move[1]
                if row in range(len(game_board)):
                    if col in range(len(game_board[0])):
                        if color == 'white':
                            if game_board[row][col] == '0':
                                self.moves.append([row, col])
                            elif 'b' in game_board[row][col]:
                                self.moves.append([row, col])
                                break
                            else:
                                break
                        else:
                            if game_board[row][col] == '0':
                                self.moves.append([row, col])
                            elif 'w' in game_board[row][col]:
                                self.moves.append([row, col])
                                break
                            else:
                                break
                    else:
                        break
                else:
                    break

    def find_valid_moves(self, row, col, color, game_board):
        from board import in_check
        self.find_all_moves(row, col, color, game_board)
        self.valid_moves = []

        for move in self.moves:
            temp_board = copy.deepcopy(game_board)

            newr = move[0]
            newc = move[1]

            if color == 'white':
                piece = 'wQ'
            else:
                piece = 'bQ'

            temp_board[row][col] = '0'
            temp_board[newr][newc] = piece
            if not in_check(color, temp_board):
                self.valid_moves.append(move)


class Rook:
    def __init__(self):
        self.moves_types = [[1, 0],
                      [0, 1],
                      [-1, 0],
                      [0, -1]]

        self.moves = []
        self.valid_moves = []

    def find_all_moves(self, row, col, color, game_board):
        self.moves = []
        start_row = row
        start_col = col
        for move in self.moves_types:
            row = start_row
            col = start_col
            while True:
                row = row+move[0]
                col = col+move[1]
                if row in range(len(game_board)):
                    if col in range(len(game_board[0])):
                        if color == 'white':
                            if game_board[row][col] == '0':
                                self.moves.append([row, col])
                            elif 'b' in game_board[row][col]:
                                self.moves.append([row, col])
                                break
                            else:
                                break
                        if color == 'black':
                            if game_board[row][col] == '0':
                                self.moves.append([row, col])
                            elif 'w' in game_board[row][col]:
                                self.moves.append([row, col])
                                break
                            else:
                                break
                    else:
                        break
                else:
                    break

    def find_valid_moves(self, row, col, color, game_board):
        from board import in_check
        self.find_all_moves(row, col, color, game_board)
        self.valid_moves = []

        for move in self.moves:
            temp_board = copy.deepcopy(game_board)

            newr = move[0]
            newc = move[1]

            if color == 'white':
                piece = 'wR'
            else:
                piece = 'bR'

            temp_board[row][col] = '0'
            temp_board[newr][newc] = piece
            if not in_check(color, temp_board):
                self.valid_moves.append(move)


class Bishop:
    def __init__(self):
        self.moves_types = [[1, 1],
                      [-1, 1],
                      [1, -1],
                      [-1, -1]]

        self.moves = []
        self.valid_moves = []

    def find_all_moves(self, row, col, color, game_board):
        self.moves = []
        start_row = row
        start_col = col
        for move in self.moves_types:
            row = start_row
            col = start_col
            while True:
                row = row+move[0]
                col = col+move[1]
                if row in range(len(game_board)):
                    if col in range(len(game_board[0])):
                        if color == 'white':
                            if game_board[row][col] == '0':
                                self.moves.append([row, col])
                            elif 'b' in game_board[row][col]:
                                self.moves.append([row, col])
                                break
                            else:
                                break
                        if color == 'black':
                            if game_board[row][col] == '0':
                                self.moves.append([row, col])
                            elif 'w' in game_board[row][col]:
                                self.moves.append([row, col])
                                break
                            else:
                                break
                    else:
                        break
                else:
                    break

    def find_valid_moves(self, row, col, color, game_board):
        from board import in_check
        self.find_all_moves(row, col, color, game_board)
        self.valid_moves = []

        for move in self.moves:
            temp_board = copy.deepcopy(game_board)

            newr = move[0]
            newc = move[1]

            if color == 'white':
                piece = 'wB'
            else:
                piece = 'bB'

            temp_board[row][col] = '0'
            temp_board[newr][newc] = piece
            if not in_check(color, temp_board):
                self.valid_moves.append(move)


class Knight:
    def __init__(self):
        self.moves_types = [[2, 1],  # down 2, 1 right
                      [2, -1],  # down 2, 1 left

                      [-2, 1],  # up 2, 1 right
                      [-2, -1],  # up 2, 1 left

                      [1, 2],  # up 1, right 2
                      [-1, 2],  # down 1, right 2

                      [1, -2],  # up 1, left 2
                      [-1, -2]]  # down 1, left 2

        self.moves = []
        self.valid_moves = []

    def find_all_moves(self, row, col, color, game_board):
        self.moves = []
        for move in self.moves_types:
            if row + move[0] in range(len(game_board)):
                if col + move[1] in range(len(game_board[0])):
                    if color == 'white':
                        if game_board[row + move[0]][col + move[1]] == '0':
                            self.moves.append([row + move[0], col + move[1]])

                        if 'b' in game_board[row + move[0]][col + move[1]]:
                            self.moves.append([row + move[0], col + move[1]])

                    if color == 'black':
                        if game_board[row + move[0]][col + move[1]] == '0':
                            self.moves.append([row + move[0], col + move[1]])
                        if 'w' in game_board[row + move[0]][col + move[1]]:
                            self.moves.append([row + move[0], col + move[1]])

    def find_valid_moves(self, row, col, color, game_board):
        from board import in_check
        self.find_all_moves(row, col, color, game_board)
        self.valid_moves = []

        for move in self.moves:
            temp_board = copy.deepcopy(game_board)

            newr = move[0]
            newc = move[1]

            if color == 'white':
                piece = 'wN'
            else:
                piece = 'bN'

            temp_board[row][col] = '0'
            temp_board[newr][newc] = piece
            if not in_check(color, temp_board):
                self.valid_moves.append(move)


class Pawn:
    def __init__(self):
        self.moves = []
        self.valid_moves = []

    def find_all_moves(self, row, col, color, game_board):
        self.moves = []
        if color == 'white':
            if row == 6:
                if game_board[row - 2][col] == '0':
                    self.moves.append([row - 2, col])
            if row - 1 in range(len(game_board)):
                if col - 1 in range(len(game_board[0])):
                    if 'b' in game_board[row - 1][col - 1]:
                        self.moves.append([row - 1, col - 1])
                if col + 1 in range(len(game_board[0])):
                    if 'b' in game_board[row - 1][col + 1]:
                        self.moves.append([row - 1, col + 1])
                if game_board[row-1][col] == '0':
                    self.moves.append([row - 1, col])

        if color == 'black':
            if row == 1:
                if game_board[row + 2][col] == '0':
                    self.moves.append([row + 2, col])

            if row + 1 in range(len(game_board)):
                if col + 1 in range(len(game_board[0])):
                    if 'w' in game_board[row + 1][col - 1]:
                        self.moves.append([row + 1, col - 1])
                if col + 1 in range(len(game_board[0])):
                    if 'w' in game_board[row + 1][col + 1]:
                        self.moves.append([row + 1, col + 1])
                if game_board[row+1][col] == '0':
                    self.moves.append([row + 1, col])

    def find_valid_moves(self, row, col, color, game_board):
        from board import in_check
        self.find_all_moves(row, col, color, game_board)
        self.valid_moves = []

        for move in self.moves:
            temp_board = copy.deepcopy(game_board)

            newr = move[0]
            newc = move[1]

            if color == 'white':
                piece = 'wP'
            else:
                piece = 'bP'

            temp_board[row][col] = '0'
            temp_board[newr][newc] = piece
            if not in_check(color, temp_board):
                self.valid_moves.append(move)


King = King()
Queen = Queen()
Rook = Rook()
Bishop = Bishop()
Knight = Knight()
Pawn = Pawn()
