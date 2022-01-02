import pygame as pg
import modules.color as col
import modules.welcomeScreen as ws
import modules.game as game

width = 960
height = 680

pg.init()
screen = pg.display.set_mode((width, height))
#w = ws.welcome(screen,width,height)
#pg.display.set_caption("Marmara chess")
FPS = 60
mousePos = (0, 0)
clock = pg.time.Clock()
onContinue = True
isWelcomeScreenShown = False
isGameScreenShown = False

wScreen = ws.welcome(screen, width, height)
gameScreen = game.Game(screen, width, height)

while onContinue:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEBUTTONUP:
            mousePos = pg.mouse.get_pos()
            if not isWelcomeScreenShown and mousePos[0] >= width / 2 - 100 and mousePos[0] <= width / 2 + 100 and mousePos[1] >= height / 2 - 200 and mousePos[1] <= height / 2:
                print("Welcome screen has been shown.")
                isWelcomeScreenShown = True
                screen.fill(col.BLACK)
    if not isWelcomeScreenShown:
        wScreen.createWelcomeScreen()
    elif isGameScreenShown:
        pass
    pg.display.update()


