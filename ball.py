from math import floor
from random import randint

class Ball(object):
  def __init__(self, x, y, vx, vy, p1, p2, gui):
    self.x = x
    self.y = y
    self.vel_x = vx
    self.vel_y = vy

    self.score = {'Player1':0,'Player2':0}

    self.paddle_1 = p1
    self.paddle_2 = p2
    self.gui = gui

  def calculate(self):
    if self.y > self.gui.height or self.y < 0:
      self.vel_y *= -1
    if self.paddle_1.y < self.y < (self.paddle_1.y + self.gui.height*0.2) and self.paddle_1.x < self.x < (self.paddle_1.x + 20):
      self.vel_x *= -1
    if self.paddle_2.y < self.y < (self.paddle_2.y + self.gui.height*0.2) and self.paddle_2.x < self.x < (self.paddle_2.x + 20):
      self.vel_x *= -1

    if self.x < 0:
      self.score['Player2'] += 1
      self.x = self.gui.width/2
      self.y = self.gui.height/2

      self.vel_x = randint(6,12)
      self.vel_y = (self.vel_x**2 - 25)**(0.5)

    elif self.x > self.gui.width:
      self.score['Player1'] += 1
      self.x = self.gui.width/2
      self.y = self.gui.height/2

      self.vel_x = randint(6,12)
      self.vel_x *= -1
      self.vel_y = (self.vel_x**2 - 25)**(0.5)

    self.gui.Color('ffffff')
    self.x += self.vel_x
    self.y += self.vel_y
    self.gui.circle(int(floor(self.x)),int(floor(self.y)),10)
