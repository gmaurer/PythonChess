import numpy as np

class Board:
    def __init__(self):
        self.board = self.createBoard()


    def createBoard(self):
        return np.zeros((8,8))



class Pieces(Board):
    def __init__(self):
        self.data = []


class WKing(Board):
    def __init__(self):
        self.color = "White"
        self.positionX = 0
        self.positionY = 3
        self.sets = self.moveSet()

    def moveSet(self):
        sets = {}
        sets[self.positionX+1] = self.positionY+1
        sets[self.positionX] = self.positionY+1
        sets[self.positionX+1] = self.positionY
        sets[self.positionX-1] = self.positionY-1
        sets[self.positionX-1] = self.positionY+1
        sets[self.positionX+1] = self.positionY-1
        sets[self.positionX-1] = self.positionY
        sets[self.positionX] = self.positionY-1

        print(sets)
        return sets



class Go(Board):
    def test(self):
        piece = input("Piece to move: ")
        if piece == "WKing":
            move(self,"WKing")
        else:
            print("wrong piece")

    def __init__(self):

        WKing.__init__(self)
        Pieces.__init__(self)
        super().__init__()

def move(self,piece):
    while True:
        try:
            #print(self.board[xPos,yPos])
            xPos = input("Put x position in: ")
            yPos = input("Put y position in: ")
            if self.board[int(xPos),int(yPos)] == 0:
                self.positionX = int(xPos)
                self.positionY = int(yPos)
                print("fair move")
                break

        except:
            print("Try a valid move")

go = Go()
go.test()
