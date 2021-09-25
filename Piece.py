
class Piece:
    def __init__(self, square):
        self.playerOwner = None
        self.square = square
        self.initPiece()
    def initPiece(self):
        self.value = None
        self.type = None
        self.name = None
        if self.playerOwner == None:    
            position = self.square.pos
            if position[1] in ['2', '7']:
                self.value = 1
                self.type = 'p'
                if position[1] == '2':
                    self.name = 'p '
                elif position[1] == '7':
                    self.name = ' p'
            elif position in ['A1', 'H1', 'A8', 'H8']:
                self.value = 5
                self.canCastle = True
                self.type = 'P'
                if position in ['A1', 'H1']:
                    self.name = 'R '
                elif position in ['A8', 'H8']:
                    self.name = ' R'
            elif position in ['B1', 'G1', 'B8', 'G8']:
                self.value = 2.9
                self.name = 'Kn'
                self.type = 'P'
            elif position in ['C1', 'F1', 'C8', 'F8']:
                self.value = 3
                self.type = 'P'
                if position in ['C1', 'F1']:
                    self.name = 'B '
                elif position in ['C8', 'F8']:
                    self.name = ' B'
            elif position in ['D1', 'D8']:
                self.value = 9
                self.type = 'P'
                if position == 'D1':
                    self.name = 'Q '
                elif position == 'D8':
                    self.name = ' Q'
            elif position in ['E1', 'E8']:
                self.value = 30
                self.canCastle = True
                self.type = 'P'
                if position == 'E1':
                    self.name = 'K '
                elif position == 'E8':
                    self.name = ' K'
        else:
            pass
        return self