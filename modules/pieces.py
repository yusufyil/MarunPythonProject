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
class king(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wking.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bking.png"))
        self.graphic = pg.transform.scale(self.graphic,(85,85))

class queen(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wqueen.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bqueen.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
class rook(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wrook.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "brook.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
class bishop(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wbishop.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bbishop.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
class knight(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wknight.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bknight.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))
class pawn(chessPieces):
    def __init__(self, type, color, xPos, yPos, firstMoove):
        super().__init__(type, color, xPos, yPos, firstMoove)
        possibleMoovements = []
        self.loadImage()
    def loadImage(self):
        if(self.color == "white"):
            self.graphic = pg.image.load(os.path.join("assets", "wpawn.png"))
        elif((self).color == "black"):
            self.graphic = pg.image.load(os.path.join("assets", "bpawn.png"))
        self.graphic = pg.transform.scale(self.graphic, (85, 85))

