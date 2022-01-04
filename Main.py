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
possibleCoords = []

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
            xSquare = mousePos[0] // 85
            ySquare = mousePos[1] // 85
            if not isWelcomeScreenShown and mousePos[0] >= width / 2 - 100 and mousePos[0] <= width / 2 + 100 and mousePos[1] >= height / 2 - 200 and mousePos[1] <= height / 2:
                print("Welcome screen has been shown.")
                isWelcomeScreenShown = True
                screen.fill(col.BLACK)
            elif not isGameScreenShown and mousePos[0] <= 680:
                #gameScreen.selectedPos = [xSquare, ySquare]
                #print(gameScreen.selectedPos)
                if gameScreen.boardCoordinate[xSquare][ySquare] == 0:
                    pass
                elif whiteTurn and gameScreen.boardCoordinate[xSquare][ySquare].color == "white":
                    gameScreen.selectedPos = [xSquare, ySquare]
                    isPieceSelected = True
                elif blackTurn and gameScreen.boardCoordinate[xSquare][ySquare].color == "black":
                    gameScreen.selectedPos = [xSquare, ySquare]
                    isPieceSelected = True
                else:
                    pass
            #now coding the moovements
            if [xSquare, ySquare] in possibleCoords:
                print("change turn")
                gameScreen.boardCoordinate[xSquare][ySquare] = gameScreen.boardCoordinate[gameScreen.selectedPos[0]][gameScreen.selectedPos[1]]
                gameScreen.boardCoordinate[gameScreen.selectedPos[0]][gameScreen.selectedPos[1]] = 0
                gameScreen.boardCoordinate[xSquare][ySquare].xPos = xSquare
                gameScreen.boardCoordinate[xSquare][ySquare].yPos = ySquare
                isPieceSelected = False
                changeTurn()



    if not isWelcomeScreenShown:
        wScreen.createWelcomeScreen()
    elif not isGameScreenShown:
        gameScreen.createBoard()
        #drawing pieces and current positions
        if not isPieceSelected:
            gameScreen.blitBoard()
        else:
            gameScreen.drawSelected()
            gameScreen.blitBoard()
            selectedPiece = gameScreen.boardCoordinate[gameScreen.selectedPos[0]][gameScreen.selectedPos[1]]
            selectedPiece.createPossibleMoovements(gameScreen.boardCoordinate)
            possibleCoords = selectedPiece.possibleMoovements
            gameScreen.drawPossibleMoovements(selectedPiece.possibleMoovements)

    pg.display.update()


