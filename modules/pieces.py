import pygame as pg
import os


class chessPieces:
    def __init__(self, type, color, xPos, yPos, firstMoove):
        self.type = type
        self.color = color
        self.xPos = xPos
        self.yPos = yPos
        self.firstMoove = firstMoove
        self.graphic = None

    def isLegalMoove(self, pos = []):
        if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
            return True
        else:
            return False

class king(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        self.possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wking.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bking.png"))
        self.graphic = pg.transform.scale(self.graphic,(85,85))
    def createPossibleMoovements(self, gameBoard = []):
        self.possibleMoovements.clear()
        tempMoovements = []
        tempMoovements.append([self.xPos - 1, self.yPos - 1])
        tempMoovements.append([self.xPos, self.yPos - 1])
        tempMoovements.append([self.xPos + 1, self.yPos - 1])
        tempMoovements.append([self.xPos - 1, self.yPos])
        tempMoovements.append([self.xPos + 1, self.yPos])
        tempMoovements.append([self.xPos - 1, self.yPos + 1])
        tempMoovements.append([self.xPos, self.yPos + 1])
        tempMoovements.append([self.xPos + 1, self.yPos + 1])
        for m in tempMoovements:
            if self.isLegalMoove(m):
                if gameBoard[m[0]][m[1]] == 0:
                    self.possibleMoovements.append(m)
                elif gameBoard[m[0]][m[1]].color != self.color:
                    self.possibleMoovements.append(m)
                else:
                    continue



class queen(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        self.possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wqueen.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bqueen.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
    def createPossibleMoovements(self, gameBoard = []):
        self.possibleMoovements.clear()
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos + i, self.yPos]):
                if gameBoard[self.xPos + i][self.yPos] == 0:
                    self.possibleMoovements.append([self.xPos + i, self.yPos])
                elif gameBoard[self.xPos + i][self.yPos].color != self.color:
                    self.possibleMoovements.append([self.xPos + i, self.yPos])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos - i, self.yPos]):
                if gameBoard[self.xPos - i][self.yPos] == 0:
                    self.possibleMoovements.append([self.xPos - i, self.yPos])
                elif gameBoard[self.xPos - i][self.yPos].color != self.color:
                    self.possibleMoovements.append([self.xPos - i, self.yPos])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos, self.yPos + i]):
                if gameBoard[self.xPos][self.yPos + i] == 0:
                    self.possibleMoovements.append([self.xPos, self.yPos + i])
                elif gameBoard[self.xPos][self.yPos + i].color != self.color:
                    self.possibleMoovements.append([self.xPos, self.yPos + i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos, self.yPos - i]):
                if gameBoard[self.xPos][self.yPos - i] == 0:
                    self.possibleMoovements.append([self.xPos, self.yPos - i])
                elif gameBoard[self.xPos][self.yPos - i].color != self.color:
                    self.possibleMoovements.append([self.xPos, self.yPos - i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos - i, self.yPos - i]):
                if gameBoard[self.xPos - i][self.yPos - i] == 0:
                    self.possibleMoovements.append([self.xPos - i, self.yPos - i])
                elif gameBoard[self.xPos - i][self.yPos - i].color != self.color:
                    self.possibleMoovements.append([self.xPos - i, self.yPos - i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos + i, self.yPos - i]):
                if gameBoard[self.xPos + i][self.yPos - i] == 0:
                    self.possibleMoovements.append([self.xPos + i, self.yPos - i])
                elif gameBoard[self.xPos + i][self.yPos - i].color != self.color:
                    self.possibleMoovements.append([self.xPos + i, self.yPos - i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos + i, self.yPos + i]):
                if gameBoard[self.xPos + i][self.yPos + i] == 0:
                    self.possibleMoovements.append([self.xPos + i, self.yPos + i])
                elif gameBoard[self.xPos + i][self.yPos + i].color != self.color:
                    self.possibleMoovements.append([self.xPos + i, self.yPos + i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos - i, self.yPos + i]):
                if gameBoard[self.xPos - i][self.yPos + i] == 0:
                    self.possibleMoovements.append([self.xPos - i, self.yPos - i])
                elif gameBoard[self.xPos - i][self.yPos + i].color != self.color:
                    self.possibleMoovements.append([self.xPos - i, self.yPos + i])
                    break
                else:
                    break


class rook(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        self.possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wrook.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "brook.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
    def createPossibleMoovements(self, gameBoard = []):
        self.possibleMoovements.clear()
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos + i, self.yPos]):
                if gameBoard[self.xPos + i][self.yPos] == 0:
                    self.possibleMoovements.append([self.xPos + i, self.yPos])
                elif gameBoard[self.xPos + i][self.yPos].color != self.color:
                    self.possibleMoovements.append([self.xPos + i, self.yPos])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos - i, self.yPos]):
                if gameBoard[self.xPos - i][self.yPos] == 0:
                    self.possibleMoovements.append([self.xPos - i, self.yPos])
                elif gameBoard[self.xPos - i][self.yPos].color != self.color:
                    self.possibleMoovements.append([self.xPos - i, self.yPos])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos, self.yPos + i]):
                if gameBoard[self.xPos][self.yPos + i] == 0:
                    self.possibleMoovements.append([self.xPos, self.yPos + i])
                elif gameBoard[self.xPos][self.yPos + i].color != self.color:
                    self.possibleMoovements.append([self.xPos, self.yPos + i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos, self.yPos - i]):
                if gameBoard[self.xPos][self.yPos - i] == 0:
                    self.possibleMoovements.append([self.xPos, self.yPos - i])
                elif gameBoard[self.xPos][self.yPos - i].color != self.color:
                    self.possibleMoovements.append([self.xPos, self.yPos - i])
                    break
                else:
                    break




class bishop(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        self.possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wbishop.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bbishop.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
    def createPossibleMoovements(self, gameBoard = []):
        self.possibleMoovements.clear()
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos - i, self.yPos - i]):
                if gameBoard[self.xPos - i][self.yPos - i] == 0:
                    self.possibleMoovements.append([self.xPos - i, self.yPos - i])
                elif gameBoard[self.xPos - i][self.yPos - i].color != self.color:
                    self.possibleMoovements.append([self.xPos - i, self.yPos - i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos + i, self.yPos - i]):
                if gameBoard[self.xPos + i][self.yPos - i] == 0:
                    self.possibleMoovements.append([self.xPos + i, self.yPos - i])
                elif gameBoard[self.xPos + i][self.yPos - i].color != self.color:
                    self.possibleMoovements.append([self.xPos + i, self.yPos - i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos + i, self.yPos + i]):
                if gameBoard[self.xPos + i][self.yPos + i] == 0:
                    self.possibleMoovements.append([self.xPos + i, self.yPos + i])
                elif gameBoard[self.xPos + i][self.yPos + i].color != self.color:
                    self.possibleMoovements.append([self.xPos + i, self.yPos + i])
                    break
                else:
                    break
        for i in range(1, 8):
            if self.isLegalMoove([self.xPos - i, self.yPos + i]):
                if gameBoard[self.xPos - i][self.yPos + i] == 0:
                    self.possibleMoovements.append([self.xPos - i, self.yPos + i])
                elif gameBoard[self.xPos - i][self.yPos + i].color != self.color:
                    self.possibleMoovements.append([self.xPos - i, self.yPos + i])
                    break
                else:
                    break


class knight(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        self.possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wknight.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bknight.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
    def createPossibleMoovements(self, gameBoard = []):
        self.possibleMoovements.clear()
        tempMoovements = []
        tempMoovements.append([self.xPos - 1, self.yPos - 2])
        tempMoovements.append([self.xPos + 1, self.yPos - 2])
        tempMoovements.append([self.xPos - 2, self.yPos + 1])
        tempMoovements.append([self.xPos - 2, self.yPos - 1])
        tempMoovements.append([self.xPos + 2, self.yPos - 1])
        tempMoovements.append([self.xPos + 2, self.yPos + 1])
        tempMoovements.append([self.xPos - 1, self.yPos + 2])
        tempMoovements.append([self.xPos + 1, self.yPos + 2])
        for m in tempMoovements:
            if self.isLegalMoove(m):
                if gameBoard[m[0]][m[1]] == 0:
                    self.possibleMoovements.append(m)
                elif gameBoard[m[0]][m[1]] != 0 and gameBoard[m[0]][m[1]].color != self.color:
                    self.possibleMoovements.append(m)


class pawn(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        self.possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wpawn.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bpawn.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
    def createPossibleMoovements(self, gameBoard = []):
        self.possibleMoovements.clear()
        if self.color == "white":
            if gameBoard[self.xPos][self.yPos - 1] == 0:
                self.possibleMoovements.append([self.xPos, self.yPos - 1])
                if gameBoard[self.xPos][self.yPos - 2] == 0 and not self.firstMoove:
                    self.possibleMoovements.append([self.xPos, self.yPos - 2])
            elif gameBoard[self.xPos - 1][self.yPos - 1] != 0 and gameBoard[self.xPos - 1][self.yPos - 1].color =="black":
                self.possibleMoovements.append([self.xPos - 1][self.yPos - 1])
            elif gameBoard[self.xPos + 1][self.yPos - 1] != 0 and gameBoard[self.xPos + 1][self.yPos - 1].color =="black":
                self.possibleMoovements.append([self.xPos + 1][self.yPos - 1])
        elif self.color =="black":
            if gameBoard[self.xPos][self.yPos + 1] == 0:
                self.possibleMoovements.append([self.xPos, self.yPos + 1])
                if gameBoard[self.xPos][self.yPos + 2] == 0 and not self.firstMoove:
                    self.possibleMoovements.append([self.xPos, self.yPos + 2])
            elif gameBoard[self.xPos - 1][self.yPos + 1] != 0 and gameBoard[self.xPos - 1][self.yPos + 1].color =="white":
                self.possibleMoovements.append([self.xPos - 1][self.yPos + 1])
            elif gameBoard[self.xPos + 1][self.yPos + 1] != 0 and gameBoard[self.xPos + 1][self.yPos + 1].color =="white":
                self.possibleMoovements.append([self.xPos + 1][self.yPos + 1])

