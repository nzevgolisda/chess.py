
from Square import Square
from Piece import Piece

class Board:
    def __init__(self):
        self.deadPieces = []
        self.initBoard()
    def squares(self):
        self.squares = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(Square(self.letters[j]+str(i+1)))
            self.squares.append(row)
        return self.squares
    def pieces(self):
        L = []
        for i in range(8):
            row = []
            for j in range(8):
                piece = Piece(self.squares[i][j])
                row.append(piece)
            L.append(row)
        self.pieces = L
        return self.pieces
    def initBoard(self):
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.squares = self.squares()
        self.pieces = self.pieces()
        
    def __str__(self):
        s = ''
        for i in range(len(self.squares)):
            s += self.letters[i] + ' | '
            for j in range(len(self.squares[i])):
                if self.squares[j][i].piece != None:
                    s += str(self.squares[j][i].piece.name) + ' '
                else:
                    s += str(self.squares[j][i]) + ' '
            s += '\n'
        s += str('    -- -- -- -- -- -- -- --'+'\n')
        s += str('     1  2  3  4  5  6  7  8')
        return s