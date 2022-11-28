from abc import ABC, abstractmethod
class Piece(ABC):

    def __init__(self, pos, color):
        # position as a vector (x, y)
        self.pos = pos
        self.color = color
        self.pos_y = pos[0] # decimos que y es la fila (1, ..., 8) o altura
        self.pos_x = pos[1] # decimos que x es la columna (a, b, ..., h)

    # as of now, black king is at line 8 and white king in line 1.

    def kingIsChecked(self, board):
        pass

    def makeMove(self, board, previousPos, newPos, piece):
        board[previousPos[0]][previousPos[1]] = "  "
        board[newPos[0]][newPos[1]] = piece

    def move(self, vectorPGN, board):
        if self.isValidMove(vectorPGN, board) == True:
            self.pos = vectorPGN
            return True
        else:
            return "Invalid input"

    def possibleCheck(self):
        pass

    @abstractmethod
    def isValidMove(self, vectorPos, board):
        pass

    def newPosInBounds(self, vectorPGN):
        if 0 > vectorPGN[0] <=8 or 0 > vectorPGN[1] <=8:
            return False
