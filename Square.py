
from Piece import Piece
class Square:
    def __init__(self, pos):
        self.pos = pos
        self.piece = None
    
    def __str__(self):
        return str(self.pos)
    