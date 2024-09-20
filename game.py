import json

class TicTacToe:
    def __init__(self):
        self.__board = [["", "", ""],
                        ["", "", ""],
                        ["", "", ""]]

        self.__binary = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]

        self.__magic_square = [[2, 9, 4],
                               [7, 5, 3],
                               [6, 1, 8]]

    def __update_binary(self, row, column, player):
        self.__binary[row][column] = 1 if player == "X" else 2

    def check_winner(self, symbol):
        for r in range(3):
            if sum(self.__magic_square[r][c] for c in range(3) if self.__board[r][c] == symbol) == 15 or \
               sum(self.__magic_square[c][r] for c in range(3) if self.__board[c][r] == symbol) == 15:
                return f"Jugador {symbol} gana"

        if sum(self.__magic_square[r][r] for r in range(3) if self.__board[r][r] == symbol) == 15 or \
           sum(self.__magic_square[r][2-r] for r in range(3) if self.__board[r][2-r] == symbol) == 15:
            return f"Jugador {symbol} gana"

        if all(cell != "" for row in self.__board for cell in row):
            return "Es un empate"

        return None 


    def __win_if_possible(self):
        for r in range(3):
            for c in range(3):
                if self.__board[r][c] == "":
                    if sum(self.__magic_square[r][c] for r, c in [(i, j) for i in range(3) for j in range(3) if self.__binary[i][j] == 2]) + self.__magic_square[r][c] == 15:
                        self.__board[r][c] = "O"
                        self.__update_binary(r, c, "O")
                        return True
        return False

    def __dont_lose(self):
        for r in range(3):
            for c in range(3):
                if self.__board[r][c] == "":
                    self.__board[r][c] = "X"
                    if self.__check_winner("X"):
                        self.__board[r][c] = "O"
                        self.__update_binary(r, c, "O")
                        return True
                    self.__board[r][c] = ""

        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        opponent_corners = [corner for corner in corners if self.__board[corner[0]][corner[1]] == "X"]
        if len(opponent_corners) == 2 and self.__board[1][1] == "O":
            for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]:
                if self.__board[r][c] == "":
                    self.__board[r][c] = "O"
                    self.__update_binary(r, c, "O")
                    return True

        if self.__board[1][1] == "":
            self.__board[1][1] = "O"
            self.__update_binary(1, 1, "O")
            return True

        for r, c in corners:
            if self.__board[r][c] == "":
                self.__board[r][c] = "O"
                self.__update_binary(r, c, "O")
                return True

        for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if self.__board[r][c] == "":
                self.__board[r][c] = "O"
                self.__update_binary(r, c, "O")
                return True

        return False

    def pc_move(self):
        if self.__dont_lose():
            return
        
        if self.__win_if_possible():
            return
        
        best_move = None
        best_value = -1
        for r in range(3):
            for c in range(3):
                if self.__board[r][c] == "" and self.__magic_square[r][c] > best_value:
                    best_move = (r, c)
                    best_value = self.__magic_square[r][c]
        if best_move:
            r, c = best_move
            self.__board[r][c] = "O"
            self.__update_binary(r, c, "O")

    def player_move(self, row, col):
        if self.__board[row][col] == "":
            self.__board[row][col] = 'X'
            self.__update_binary(row, col, "X")
            return True
        return False 

    def get_board(self):
        return json.dumps(self.__board)

    def set_board(self, board_json):
        self.__board = json.loads(board_json)
