from Piece import Piece

class Knight(Piece):
    def __init__(self, pos, color):
        super().__init__(pos, color)

    def isValidMove(self, vectorPos, board):
        if (board.whiteMoves and self.color != "white") or (board.whiteMoves == False and self.color == "white"):
            return False
        if self.newPosInBounds(vectorPos) == False:
            return False

        direction = [vectorPos[0] - self.pos_y, vectorPos[1] - self.pos_x]
        dir_y = direction[0]
        dir_x = direction[1]
        if (abs(vectorPos[0]-self.pos_y) + abs(vectorPos[1]-self.pos_x)) != 3:
            return False
        # since the sum of the absolute value of both is 3, I'm assuring that the only possible sum is 1 + 2 = 3 or 2 + 1 = 3
        elif dir_y == 0 or dir_x == 0:
            return False

        if board.board[vectorPos[0]][vectorPos[1]] == "  ":
            board.whiteMoves = not board.whiteMoves
            self.pos_y = vectorPos[0]
            self.pos_x = vectorPos[1]
            return True
        elif board.board[vectorPos[0]][vectorPos[1]].color != self.color:
            board.whiteMoves = not board.whiteMoves
            self.pos_y = vectorPos[0]
            self.pos_x = vectorPos[1]
            return True
        else:
            return False
