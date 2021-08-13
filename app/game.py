import math
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from map2 import Map

class Game:
  done = False
  clock = pygame.time.Clock()
  game_map = Map()
  x = 0
  y = 0
  z = 1
  z_acceleration = 0
  gravity = -9.81
  angle = 0

  def game_input(self):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
      self.angle = self.angle + math.pi / 60
    if pressed[pygame.K_d]:
      self.angle = self.angle - math.pi / 60
    if pressed[pygame.K_w]:
      self.y += (0.1 * math.sin(self.angle))
      self.x += (0.1 * math.cos(self.angle))
    if pressed[pygame.K_s]:
      self.y -= (0.1 * math.sin(self.angle))
      self.x -= (0.1 * math.cos(self.angle))
    if pressed[pygame.K_q]:
      self.y += (0.1 * math.cos(self.angle))
      self.x -= (0.1 * math.sin(self.angle))
    if pressed[pygame.K_e]:
      self.y -= (0.1 * math.cos(self.angle))
      self.x += (0.1 * math.sin(self.angle))
    if pressed[pygame.K_SPACE]:
      self.z_acceleration = 0.5

  def game_update(self):
    self.z_acceleration += self.gravity / 60
    self.z = max(self.z + self.z_acceleration, 1)
    glLoadIdentity()
    gluPerspective(45, (self.width / self.height), 0.1, 40)
    gluLookAt(self.x, self.y, self.z, self.x + 100 * math.cos(self.angle), self.y + 100 * math.sin(self.angle), 0, 0, 0, 1)

  def game_display(self):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    self.game_map.display()

  def __init__(self, width, height):
    pygame.init()
    self.width = width
    self.height = height
    pygame.display.set_mode((width , height), DOUBLEBUF|OPENGL)

    while not self.done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True

      self.game_input()
      self.game_update()
      self.game_display()

      pygame.display.flip()
      self.clock.tick(60)

if __name__ == '__main__':
    game = Game(800, 600)