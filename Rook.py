from Piece import Piece

class Rook(Piece):
    # FINISHED, I believe
    def __init__(self, pos, color):
        super().__init__(pos, color)


    def isValidMove(self, vectorPos, board):
        if (board.whiteMoves and self.color != "white") or (board.whiteMoves == False and self.color == "white"):
            return False
        # if it is not moving vertically nor horizontally
        if vectorPos[0] - self.pos_y != 0 and vectorPos[1] - self.pos_x != 0:
            return False
        if self.newPosInBounds(vectorPos) == False:
            return False

        if vectorPos[0] - self.pos_y > 0:
            for i in range(self.pos_y, vectorPos[0], 1):
                if board.board[i][self.pos_x] != "  ":
                    return False
        elif vectorPos[0] - self.pos_y < 0:
            for i in range(vectorPos[0], self.pos_y, 1):
                if board.board[i][self.pos_x] != "  ":
                    return False
        elif vectorPos[1] - self.pos_x > 0:
            for i in range(self.pos_x + 1, vectorPos[1], 1):
                if board.board[self.pos_y][i] != "  ":
                    return False
        elif vectorPos[1] - self.pos_x < 0:
            for i in range(vectorPos[1], self.pos_x, 1):
                if board.board[self.pos_y][i] != "  ":
                    return False
        else:
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
