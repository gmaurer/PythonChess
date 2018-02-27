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
        self.set = self.moveSet()

    def moveSet(self):
        #use sets instead
        x = self.positionX
        y = self.positionY
        sets = set()
        sets.add((x+1,y))
        sets.add((x-1,y))
        sets.add((x,y+1))
        sets.add((x,y-1))
        sets.add((x+1,y+1))
        sets.add((x+1,y-1))
        sets.add((x-1,y+1))
        sets.add((x-1,y-1))

        return sets



class Go(Board):
    def test(self):
        piece = input("Piece to move: ")
        if piece == "WKing":
            move(self,"WKing")
        else:
            print("wrong piece")

    def __init__(self):

        self.wKing = WKing()
        self.pieces = Pieces()
        super().__init__()

def move(self,piece):
    while True:
        try:
            xPos = input("Put x position in: ")
            yPos = input("Put y position in: ")
            tupleCheck = (int(xPos),int(yPos))

            if self.board[int(xPos),int(yPos)
                        ] == 0 and tupleCheck in self.wKing.set:

                self.positionX = int(xPos)
                self.positionY = int(yPos)
                print("fair move")
                break

        except:
            print("Try a valid move")

go = Go()
go.test()
