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
        if(pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7):
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
    def createPossibleMoovements(self):
        self.possibleMoovements.append([self.xPos - 1, self.yPos - 1])
        self.possibleMoovements.append([self.xPos, self.yPos - 1])
        self.possibleMoovements.append([self.xPos + 1, self.yPos - 1])
        self.possibleMoovements.append([self.xPos - 1, self.yPos])
        self.possibleMoovements.append([self.xPos + 1, self.yPos])
        self.possibleMoovements.append([self.xPos - 1, self.yPos + 1])
        self.possibleMoovements.append([self.xPos, self.yPos + 1])
        self.possibleMoovements.append([self.xPos + 1, self.yPos + 1])
        self .possibleMoovements = list(filter(self.isLegalMoove(), self.possibleMoovements))
        print(self.possibleMoovements)

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
    def createPossibleMoovements(self):
        for i in range(8):
            self.possibleMoovements.append([self.xPos - i, self.yPos - i])
            self.possibleMoovements.append([self.xPos + i, self.yPos - i])
            self.possibleMoovements.append([self.xPos - i, self.yPos + i])
            self.possibleMoovements.append([self.xPos + i, self.yPos + 1])
            self.possibleMoovements.append([self.xPos + i, self.yPos])
            self.possibleMoovements.append([self.xPos - i, self.yPos])
            self.possibleMoovements.append([self.xPos, self.yPos + i])
            self.possibleMoovements.append([self.xPos, self.yPos - i])
        self.possibleMoovements = list(filter(self.isLegalMoove(), self.possibleMoovements))


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
    def createPossibleMoovements(self):
        for i in range(8):
            self.possibleMoovements.append([self.xPos + i, self.yPos])
            self.possibleMoovements.append([self.xPos - i, self.yPos])
            self.possibleMoovements.append([self.xPos, self.yPos + i])
            self.possibleMoovements.append([self.xPos, self.yPos - i])
        self.possibleMoovements = list(self.isLegalMoove(), self.possibleMoovements)
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
    def createPossibleMoovements(self):
        for i in range(8):
            self.possibleMoovements.append([self.xPos - i, self.yPos - i])
            self.possibleMoovements.append([self.xPos + i, self.yPos - i])
            self.possibleMoovements.append([self.xPos - i, self.yPos + i])
            self.possibleMoovements.append([self.xPos + i, self.yPos + 1])
        self.possibleMoovements = list(filter(self.isLegalMoove(), self.possibleMoovements))
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
    def createPossibleMoovements(self):
        self.possibleMoovements.append([self.xPos - 3, self.yPos - 1])
        self.possibleMoovements.append([self.xPos - 3, self.yPos + 1])
        self.possibleMoovements.append([self.xPos + 3, self.yPos - 1])
        self.possibleMoovements.append([self.xPos + 3, self.yPos + 1])
        self.possibleMoovements.append([self.xPos - 1, self.yPos - 3])
        self.possibleMoovements.append([self.xPos - 1, self.yPos + 3])
        self.possibleMoovements.append([self.xPos + 1, self.yPos - 3])
        self.possibleMoovements.append([self.xPos + 1, self.yPos + 3])

        self.possibleMoovements = list(filter(self.isLegalMoove(), self.possibleMoovements))
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
    def createPossibleMoovements(self):
        if(self.color == "white"):
            self.possibleMoovements.append([self.xPos, self.yPos - 1])
            if(not self.firstMoove):
                self.possibleMoovements.append([self.xPos, self.yPos - 2])
        elif(self.color == "black"):
            self.possibleMoovements.append(self.xPos, self.yPos + 1)
            if(not self.firstMoove):
                self.possibleMoovements.append([self.xPos, self.yPos + 2])
        self.possibleMoovements = list(filter(self.isLegalMoove(), self.possibleMoovements))