import pygame as pg
import os
import modules.color as col
class welcome:
    def __init__(self,screen,screenWidth,screenHeight):
        self.screen = screen
        self.width = screenWidth
        self.height = screenHeight
        self.createWelcomeScreen()
    def createWelcomeScreen(self):
        onWelcomeScreen = True
        FPS = 60
        clock = pg.time.Clock()
        mousePos = (0,0)
        while onWelcomeScreen:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEBUTTONUP:
                    mousePos = pg.mouse.get_pos()
                    if (mousePos[0] >= self.width / 2 - 100 and mousePos[0]<= self.width / 2 + 100 and mousePos[1] >= self.height / 2 - 200 and mousePos[1] <= self.height / 2 ):
                        print(mousePos)

            self.screen.fill(col.BLACK)
            self.logo = pg.image.load(os.path.join("assets", "MarunLogo.png"))
            self.logo = pg.transform.scale(self.logo, (200, 200))
            self.screen.blit(self.logo, (self.width / 2 - 100, self.height / 2 - 200))
            font = pg.font.Font('freesansbold.ttf', 32)
            text = font.render("Maça başlamak için Marmara logosuna tıklayınız", True, col.WHITE)
            textRect = text.get_rect()
            textRect.center = (self.width / 2, 100 + self.height / 2)
            self.screen.blit(text, textRect)
            pg.display.update()
