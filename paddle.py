class Paddle(object):
  def __init__(self,x,y,gui):
    self.x = x
    self.y = y
    self.gui = gui

  def UP(self):
    if self.y < 0:
      pass
    else:
      self.y -= 6

  def DOWN(self):
    if self.y + self.gui.height*0.2 > self.gui.height:
      pass
    else:
      self.y += 6

  def reset(self,x,y):
    self.x = x
    self.y = y

  def draw(self):
    self.gui.Color('ffffff')
    self.gui.rect(self.x,self.y,20,self.gui.height*0.2)
