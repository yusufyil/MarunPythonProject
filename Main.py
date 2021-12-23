import pygame as pg
import modules.color as col
import modules.welcomeScreen as ws

width = 1280
height = 700

pg.init()
screen = pg.display.set_mode((width,height))
w = ws.welcome(screen,width,height)
#pg.display.set_caption("Marmara chess")

