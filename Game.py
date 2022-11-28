from Board import Board


# When moving, we take as an input a PGN as string, but we calculate position as a vector
def PGNtoList(PGN):
    PGNnum = int(PGN[1])
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    i = -1
    for letter in range(0, len(letters), 1):
        if letters[letter] == PGN[0]:
            i = letter
            break
    if i == -1:
        return "Invalid input"
    if 0 < PGNnum <= 8:
        return i, PGNnum - 1  # [0] es la fila y [1] la columna
    else:
        return "Invalid input"


class Game:
    # IMPORTANT: I use the word PGN with too much liberty, but in here it stands for "algebraic notation"
    # Like: a4 or f5...

    def __init__(self):
        self.board = Board()

    # String currentPos: PGN of the object to move, String newPos: PGN of the new position
    def move(self, currentPos, newPos):
        if PGNtoList(currentPos) == "Invalid input" or PGNtoList(newPos) == "Invalid input":
            return "Invalid input"
        else:
            currentVector_x, currentVector_y = PGNtoList(currentPos)
            newVector_x, newVector_y = PGNtoList(newPos)
        if not isinstance(self.board.board[currentVector_y][currentVector_x], str):
            if self.board.board[currentVector_y][currentVector_x].move([newVector_y, newVector_x], self.board) == True:
                self.makeMove([currentVector_y, currentVector_x], [newVector_y, newVector_x])

    def makeMove(self, previousPos, newPos):
        piece = self.board.board[previousPos[0]][previousPos[1]]
        self.board.board[previousPos[0]][previousPos[1]] = "  "
        self.board.board[newPos[0]][newPos[1]] = piece
        self.board.printBoard()
        print("\n               --------------- \n")

    def check(self):
        pass
