import pygame
from gui import GUI
from paddle import Paddle
from ball import Ball
from random import randint
from math import sqrt


def mainLoop():
  global gui
  global paddle_1
  global paddle_2
  global score

  gui = GUI(1200,700,'Pong')

  paddle_1 = Paddle(20, gui.height*0.4,gui)
  paddle_2 = Paddle(gui.width - 40, gui.height*0.4,gui)

  r = 10
  r2 = randint(1,15)

  ball = Ball(gui.width/2,gui.height/2,r,r2,paddle_1,paddle_2,gui)

  done = False

  while not done:
    for e in gui.event():
      if e.type == pygame.QUIT:
        print('ending gui')
        done = True
        break

    if gui.keysDown(pygame.K_w):
      paddle_1.UP()
    if gui.keysDown(pygame.K_s):
      paddle_1.DOWN()
    if gui.keysDown(pygame.K_UP):
      paddle_2.UP()
    if gui.keysDown(pygame.K_DOWN):
      paddle_2.DOWN()


    gui.page.fill((0,0,0))

    ball.calculate()
    paddle_1.draw()
    paddle_2.draw()

    gui.Text(str(ball.score),36)
    gui.showText(gui.width - gui.f.get_width(),0)

    gui.flip(40)


mainLoop()
