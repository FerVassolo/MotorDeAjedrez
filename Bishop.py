from Piece import Piece

class Bishop(Piece):

    def __init__(self, pos, color):
        super().__init__(pos, color)

    def isValidMove(self, vectorPos, board):

        if (board.whiteMoves and self.color != "white") or (board.whiteMoves == False and self.color == "white"):
            return False
        if vectorPos[0] - self.pos_y == 0 or vectorPos[1] - self.pos_x == 0:
            return False
        elif abs(vectorPos[0] - self.pos_y) != abs(vectorPos[1] - self.pos_x):
            return False
        if self.newPosInBounds(vectorPos) == False:
            print("mesi")
            return False

        # if direction[0] > 0 --> going upwards, direction[1] > 0 --> going right
        direction = [vectorPos[0] - self.pos_y, vectorPos[1] - self.pos_x]
        dir_y = direction[0]
        dir_x = direction[1]
        initialPos_y = self.pos_y
        initialPos_x = self.pos_x

        for i in range(min(vectorPos[0], self.pos_y), max(vectorPos[0], self.pos_y), 1):
            if dir_y > 0:
                if dir_x > 0:
                    if board.board[initialPos_y + 1][initialPos_x + 1] != "  ":
                        return False
                    else:
                        initialPos_y = initialPos_y + 1
                        initialPos_x = initialPos_x + 1
                elif dir_x < 0:
                    if board.board[initialPos_y + 1][initialPos_x - 1] != "  ":
                        return False
                    else:
                        initialPos_y = initialPos_y + 1
                        initialPos_x = initialPos_x - 1
            elif dir_y < 0:
                if dir_x > 0:
                    if board.board[initialPos_y - 1][initialPos_x + 1] != "  ":
                        return False
                    else:
                        initialPos_y = initialPos_y - 1
                        initialPos_x = initialPos_x + 1
                elif dir_x < 0:
                    if board.board[initialPos_y - 1][initialPos_x - 1] != "  ":
                        return False
                    else:
                        initialPos_y = initialPos_y - 1
                        initialPos_x = initialPos_x - 1

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


