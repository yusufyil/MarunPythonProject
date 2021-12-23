import pygame as pg
import modules.color as col
import modules.welcomeScreen as ws
import modules.game as game

width = 960
height = 680

pg.init()
screen = pg.display.set_mode((width,height))
#w = ws.welcome(screen,width,height)
#pg.display.set_caption("Marmara chess")
FPS = 60
mousePos = (0,0)
clock = pg.time.Clock()
onContinue = True
isWelcomeScreenShown = False
isGameScreenShown = False

wScreen = ws.welcome(screen,width,height)
gameScreen = game.Game(screen,width,height)

while onContinue:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEBUTTONUP:
            mousePos = pg.mouse.get_pos()
            if (not isWelcomeScreenShown and mousePos[0] >= width / 2 - 100 and mousePos[0]<= width / 2 + 100 and mousePos[1] >= height / 2 - 200 and mousePos[1] <= height / 2 ):
                isWelcomeScreenShown = True
            elif(not isGameScreenShown and mousePos[0] <=680):
                xSquare = mousePos[0] // 85
                ySquare = mousePos[1] // 85
                if(gameScreen.boardCoordinate[xSquare][ySquare] == 0):
                    pass
                else:
                    gameScreen.selectedPos = [xSquare, ySquare]

    #showing welcomeScreen
    if (not isWelcomeScreenShown):
        wScreen.createWelcomeScreen()
    elif (not isGameScreenShown):
        screen.fill(col.BLACK)
        gameScreen.createBoard()
        if (gameScreen.selectedPos != []):
            gameScreen.drawSelected(gameScreen.selectedPos)
        gameScreen.blitBoard()
    pg.display.update()


