import pygame as pg
import os
import modules.color as col



class endingScreen:
    def __init__(self, screen, screenWidth, screenHeight):
        self.screen = screen
        self.width = screenWidth
        self.height = screenHeight

    def createEndingScreen(self, winner = ""):
        self.screen.fill(col.BLACK)
        self.logo = pg.image.load(os.path.join("assets", "MarunLogo.png"))
        self.logo = pg.transform.scale(self.logo, (200, 200))
        self.screen.blit(self.logo, (self.width / 2 - 100, self.height / 2 - 200))
        font = pg.font.Font('freesansbold.ttf', 32)
        text = font.render("Maçın kazananı " + winner.title() + " Oyuncu", True, col.WHITE)
        textRect = text.get_rect()
        textRect.center = (self.width / 2, 100 + self.height / 2)
        self.screen.blit(text, textRect)
        pg.display.update()

