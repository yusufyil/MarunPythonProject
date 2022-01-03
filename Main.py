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
whiteTurn = True
blackTurn = False
isPieceSelected = False

def changeTurn():
    global whiteTurn
    global blackTurn
    if whiteTurn:
        whiteTurn = False
        blackTurn = True
    else:
        whiteTurn = True
        blackTurn = False

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
            elif not isGameScreenShown and mousePos[0] <= 680:
                xSquare = mousePos[0] // 85
                ySquare = mousePos[1] // 85
                gameScreen.selectedPos = [xSquare, ySquare]
                print(gameScreen.selectedPos)



    if not isWelcomeScreenShown:
        wScreen.createWelcomeScreen()
    elif not isGameScreenShown:
        gameScreen.createBoard()
        #drawing pieces and current positions
        if not isPieceSelected:

            gameScreen.blitBoard()
        else:
            pass
    pg.display.update()


