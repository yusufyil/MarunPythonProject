import pygame as pg
import os
import modules.pieces as pc
import modules.color as col
class Game:
    def __init__(self, screen, screenWidth, screenHeight):
        self.screen = screen
        self.width = screenWidth
        self.height = screenHeight
        self.gameBoard = pg.image.load(os.path.join("assets", "chessboard.png"))
        self.gameBoard = pg.transform.scale(self.gameBoard, (680, 680))
        self.cross = pg.image.load(os.path.join("assets", "crosshair.png"))
        self.cross = pg.transform.scale(self.cross, (85, 85))
        self.selectedPos = []
        self.createBoard()
        self.boardCoordinate = [[0 for i in range(8)] for j in range(8)]
        self.initializeBoard()

    def createBoard(self):
        pg.display.set_caption("Marmara Chess <3")
        self.screen.blit(self.gameBoard, (0, 0))

    def initializeBoard(self):
        for i in range(8):
            self.boardCoordinate[i][1] = pc.pawn("pawn", "black", i, 1, False)
            self.boardCoordinate[i][6] = pc.pawn("pawn", "white", i, 6, False)
        self.boardCoordinate[0][0] = pc.rook("rook", "black", 0, 0, False)
        self.boardCoordinate[7][0] = pc.rook("rook", "black", 7, 0, False)
        self.boardCoordinate[1][0] = pc.knight("knight", "black", 1, 0, False)
        self.boardCoordinate[6][0] = pc.knight("knight", "black", 6, 0, False)
        self.boardCoordinate[2][0] = pc.bishop("bishop", "black", 2, 0, False)
        self.boardCoordinate[5][0] = pc.bishop("bishop", "black", 5, 0, False)
        self.boardCoordinate[3][0] = pc.queen("queen", "black", 3, 0, False)
        self.boardCoordinate[4][0] = pc.king("king", "black", 4, 0, False)

        self.boardCoordinate[0][7] = pc.rook("rook", "white", 0, 7, False)
        self.boardCoordinate[7][7] = pc.rook("rook", "white", 7, 7, False)
        self.boardCoordinate[1][7] = pc.knight("knight", "white", 1, 7, False)
        self.boardCoordinate[6][7] = pc.knight("knight", "white", 6, 7, False)
        self.boardCoordinate[2][7] = pc.bishop("bishop", "white", 2, 7, False)
        self.boardCoordinate[5][7] = pc.bishop("bishop", "white", 5, 7, False)
        self.boardCoordinate[3][7] = pc.queen("queen", "white", 3, 7, False)
        self.boardCoordinate[4][7] = pc.king("king", "white", 4, 7, False)

    def blitBoard(self):
        for i in range(8):
            for j in range(8):
                if(self.boardCoordinate[i][j] != 0):
                    self.screen.blit(self.boardCoordinate[i][j].graphic, (85 * self.boardCoordinate[i][j].xPos, 85 * self.boardCoordinate[i][j].yPos))

    def drawSelected(self):
        selectedSquare = pg.image.load(os.path.join("assets", "selected.png"))
        selectedSquare = pg.transform.scale(selectedSquare, (85, 85))
        self.screen.blit(selectedSquare, (self.selectedPos[0] * 85 + 1, self.selectedPos[1] * 85 + 1))

    def drawPossibleMoovements(self, coords = [0, 0]):
        for coord in coords:
            self.screen.blit(self.cross, (coord[0] * 85, coord[1] * 85))

    def showGameInfo(self, white, black):
        turn = ""
        if white:
            turn = "Beyaz"
        elif black:
            turn = "Siyah"
        font = pg.font.Font('freesansbold.ttf', 18)
        text = font.render("Sıra" + " " + turn + " " + "oyuncuda", True, col.WHITE)
        textRect = text.get_rect()
        textRect.center = (800, 300)
        self.screen.blit(text, textRect)

    def checkForWinner(self):
        isWhiteKingFound = False
        isBlackKingFound = False
        for row in self.boardCoordinate:
            for piece in row:
                if piece == 0:
                    pass
                elif piece.type == "king":
                    if piece.color == "black":
                        isBlackKingFound = True
                    elif piece.color == "white":
                        isWhiteKingFound = True
        if isWhiteKingFound and isBlackKingFound:
            return False
        elif isWhiteKingFound:
            return "white"
        else:
            return "black"

