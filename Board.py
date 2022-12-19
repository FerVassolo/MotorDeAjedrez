from Pawn import Pawn
from Rook import Rook
from Bishop import Bishop
from Knight import Knight

class Board:

    def __init__(self):
        self.board = [["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"],
                      ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                      ["bR", "bN", "bB", "bK", "bQ", "bB", "bN", "bR"]]
        self.auxiliaryBoard = [["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]]
        self.whiteMoves = True
        self.updateBoard()

    def updateBoard(self):
        i = 0
        j = 0
        for element in self.board:
            for elm in element:
                if elm[0] == "w":
                    color = "white"
                else:
                    color = "black"
                if elm[1] == "P":
                    pawn = Pawn([i, j], color)
                    self.board[i][j] = pawn
                elif elm[1] == "R":
                    rook = Rook([i, j], color)
                    self.board[i][j] = rook
                elif elm[1] == "B":
                    bishop = Bishop([i, j], color)
                    self.board[i][j] = bishop
                elif elm[1] == "N":
                    knight = Knight([i, j], color)
                    self.board[i][j] = knight
                j +=1
            j =0
            i +=1
        i = 0

    def drawBoard(self):
        # in pygame
        pass

    def printBoard(self):
        # C/java-styled for loop
        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board), 1):
                self.auxiliaryBoard[i][j] = "  "
                if isinstance(self.board[i][j], Pawn):
                    if self.board[i][j].color == "white":
                        self.auxiliaryBoard[i][j] = "wP"
                    else:
                        self.auxiliaryBoard[i][j] = "bP"
                if isinstance(self.board[i][j], Rook):
                    if self.board[i][j].color == "white":
                        self.auxiliaryBoard[i][j] = "wR"
                    else:
                        self.auxiliaryBoard[i][j] = "bR"
                if isinstance(self.board[i][j], Bishop):
                    if self.board[i][j].color == "white":
                        self.auxiliaryBoard[i][j] = "wB"
                    else:
                        self.auxiliaryBoard[i][j] = "bB"
                if isinstance(self.board[i][j], Knight):
                    if self.board[i][j].color == "white":
                        self.auxiliaryBoard[i][j] = "wN"
                    else:
                        self.auxiliaryBoard[i][j] = "bN"
        for elm in self.auxiliaryBoard:
            print(elm)
