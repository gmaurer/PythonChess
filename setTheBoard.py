import numpy as np

class Board:
    def __init__(self):
        self.board = self.createBoard()


    def createBoard(self):
        npBoard = np.zeros((8,8))
        setPieces(npBoard)
        return npBoard



class Pieces(Board):
    def __init__(self):
        self.data = []


class WKing(Board):
    def __init__(self):
        self.color = "White"
        self.character = 6
        self.positionX = 7
        self.positionY = 3
        self.set = self.moveSet()
        self.checked = False


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
            move(self,self.wKing)
            checkLocation(self,self.wKing.positionX,self.wKing.positionY)

        else:
            print("wrong piece")

    def __init__(self):

        self.wKing = WKing()
        self.pieces = Pieces()
        super().__init__()
def setPieces(b):#will do this cleaner
    b[7,3] = 6
    b[0,3] = 6 #Kings

def move(self,piece):
    while True:
        try:

            xPos = input("Put x position in: ")
            yPos = input("Put y position in: ")
            tupleCheck = (int(xPos),int(yPos))

            if self.board[int(xPos),int(yPos)
                        ] == 0 and tupleCheck in piece.set:

                tempX = piece.positionX
                tempY = piece.positionY
                piece.positionX = int(xPos)
                piece.positionY = int(yPos)
                self.board[piece.positionX,piece.positionY] = piece.character
                self.board[tempX,tempY] = 0
                print(self.board)
                print("fair move")
                break
            else:
                print("Invalid move or piece in the way")

        except:
            print("Try valid moves")

def checkLocation(self,X,Y):
    if self.board[X,Y] != 0:
        print("taken Piece at: ", X, Y)
    else:
        print("Moved to space: ", X, Y)


go = Go()
go.test()
