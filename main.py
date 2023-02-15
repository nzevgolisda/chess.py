       
class Square:
    def __init__(self, sq):
        self.value = sq
        self.piece = []
    def __str__(self):
        s = ''
        p = self.piece
        if len(p) == 0:
            s = str(self.value)+'|'
        else:
            L = self.piece
            p = L[0]
            s = '|'+str(p)+'|'
        return s
class Piece:
    def __init__(self, sq, name):
        self.square = sq
        self.name = name
        self.symbols = ['p', 'R', 'N', 'B', 'Q', 'K']
        self.piece = []
        if self.name in self.symbols:
            if self.name == 'p':
                self.value = 1
            elif self.name == 'R':
                self.value = 5
            elif self.name == 'N':
                self.value = 2.9
            elif self.name == 'B':
                self.value = 3
            elif self.name == 'Q':
                self.value = 9
            elif self.name == 'K':
                self.value = 60
    def __str__(self):
        return str(self.name)
class Board:
    def __init__(self, L = 'abcdefgh'):
        self.board = []
        self.Letters = list(L)
        self.n = len(self.Letters)
        self.m = self.n
        for i in range(self.m-1, -1, -1):
            row = [] # Black top
            for j in range(self.n):
                sq = str(self.Letters[j]) + str(i+1)
                square = Square(sq)
                row.append(square)
            self.board.append(row)
    def createPieces(self):
        self.white = []
        self.black = []
        self.blackView = ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R']
        for i in range(self.n):
            # WHITE
            #  Pawns
            name = 'p'
            square = str(self.Letters[i]) + str('2')
            self.white.append(Piece(square, name))
            #  Pieces
            square = str(self.Letters[i]) + str('1')
            name = self.blackView[i]
            self.white.append(Piece(square, name))
            # BLACK
            #  Pawns
            name = 'p'
            square = str(self.Letters[i]) + str('7')
            self.black.append(Piece(square, name))
            #  Pieces
            name = self.blackView[i]
            square = str(self.Letters[i]) + str('8')
            self.black.append(Piece(square, name))
    def importPieces(self):
        for p in self.white + self.black:
            sq = p.square
            i = int(sq[1])-1
            j = self.Letters.index(sq[0])
            square = self.board[self.n-i-1][self.m-j-1]
            square.piece.append(p)
        print(self)
    def move(self):
        sq1 = str(input('Starting square: '))
        letter = sq1[0]
        j = self.Letters.index(letter)
        i = int(sq1[1])-1
        square = self.board[self.n-i-1][j]
        p = square.piece.pop()

        sq2 = str(input('Ending square: '))
        letter = sq2[0]
        j = self.Letters.index(letter)
        i = int(sq2[1])-1
        square = self.board[self.n-i-1][j]
        square.piece.append(p)
        print(self)
    def __str__(self):
        s = 2*'\n'
        for i in range(self.m):
            row = ''
            for j in range(self.n):
                square = self.board[i][j]
                row += str(square)
            s += row + 2*'\n'
        return s
        
b = Board()
b.createPieces()
b.importPieces()
for i in range(3):
    b.move()
