from Piece import Piece

class Pawn(Piece):

    def __init__(self, pos, color):
        super().__init__(pos, color)
        #front: weather the pawn is facing forward (if white) or backwards (if black)
        self.possibleEnPassant = False # TODO
        self.inStartingPos = True

    def upgradeToQueen(self): # TODO
        pass

    def isValidMove(self, vectorPos, board):
        if self.color == "white":
            if 0 >= vectorPos[0] - self.pos[0] < 2:
                return False
        else:
            if 0 >= self.pos[0] - vectorPos[0] < 2:
                return False
        if -1 > vectorPos[1] - self.pos[1] < 1:
            return False
        if self.possibleCheck():
            return False

        if self.color == "white" and board.whiteMoves:
            if self.inStartingPos == True:
                if vectorPos[0] - self.pos[0] == 2:
                    if board.board[vectorPos[0]][vectorPos[1]] == "  " and board.board[vectorPos[0]-1][vectorPos[1]] == "  ":
                        self.inStartingPos = False
                        board.whiteMoves = False
                        return True
            if vectorPos[0] - self.pos[0] == 1:
                if board.board[vectorPos[0]][vectorPos[1]] == "  ":
                    if vectorPos[0] == 7:
                        self.upgradeToQueen()
                    self.inStartingPos = False
                    board.whiteMoves = False
                    return True

                if vectorPos[1] - self.pos[1] == 1 or vectorPos[1] - self.pos[1] == -1:
                    if board.board[vectorPos[0]][vectorPos[1]] != "  ":
                        if board.board[vectorPos[0]][vectorPos[1]].color == "black":
                            self.inStartingPos = False
                            board.whiteMoves = False
                            return True

        if self.color == "black" and board.whiteMoves == False:
            if self.inStartingPos == True:
                if self.pos[0] - vectorPos[0] == 2:
                    if board.board[vectorPos[0]][vectorPos[1]] == "  " and board.board[vectorPos[0]+1][vectorPos[1]] == "  ":
                        self.inStartingPos = False
                        board.whiteMoves = True
                        return True
            if self.pos[0] - vectorPos[0] == 1:
                if board.board[vectorPos[0]][vectorPos[1]] == "  ":
                        self.inStartingPos = False
                        board.whiteMoves = True
                        return True
                if vectorPos[1] - self.pos[1] == 1 or vectorPos[1] - self.pos[1] == -1:
                    if board.board[vectorPos[0]][vectorPos[1]] != "  ":
                        if board.board[vectorPos[0]][vectorPos[1]].color == "white":
                            self.inStartingPos = False
                            board.whiteMoves = True
                            return True

