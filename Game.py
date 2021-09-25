
from Square import Square
from Piece import Piece
from Board import Board
from Player import Player

class Game:
    def __init__(self, wP, bP):
        self.player1 = wP
        self.player2 = bP
        self.board = Board()
        self.createPlayers()
        self.createPlayersPieces()
    def createPawns(self):
        for i in range(8):
            square = self.board.squares[1][i]
            piece = Piece(square)
            piece.playerOwner = self.player1
            square.piece = piece
            self.board.pieces.append(piece)
        for i in range(8):
            square = self.board.squares[6][i]
            piece = Piece(square)
            piece.playerOwner = self.player2
            square.piece = piece
            self.board.pieces.append(piece)
    def createPieces(self):
        for j in range(8):
            square = self.board.squares[0][j]
            piece = Piece(square)
            piece.playerOwner = self.player1
            square.piece = piece
            self.board.pieces.append(piece)
        for j in range(8):
            square = self.board.squares[7][j]
            piece = Piece(square)
            piece.playerOwner = self.player2
            square.piece = piece
            self.board.pieces.append(piece)
    def createPlayers(self):
        self.player1.side = 'W'
        self.player2.side = 'B'
    def createPlayersPieces(self):
        self.pawns = self.createPawns()
        self.pieces = self.createPieces()

    def __str__(self):
        return '\n'+'         > '+self.player1.name+' VS '+self.player2.name+' <'+2*'\n'+str(self.board)
    