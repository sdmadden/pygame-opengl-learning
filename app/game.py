import math
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from map2 import Map
from thing import Thing

class Game:
  done = False
  clock = pygame.time.Clock()
  game_map = Map()
  thing = Thing([
    (50, 50, 50), (60, 50, 50), (60, 60, 50), (50, 60, 50),
    (50, 50, 60), (60, 50, 60), (60, 60, 60), (50, 60, 60)
  ], [
    (0,1), (1,2), (2,3), (3,0),
    (0,4), (1,5), (2,6), (3,7),
    (4,5), (5,6), (6,7), (7,4)
  ])
  x = 0
  y = 0
  z = 5
  z_base = z
  z_acceleration = 0
  gravity = -9.81
  angle = 0
  z_angle = 0
  far_away = 100
  max_distance = 10000
  fps = 60
  min_z_down = -math.pi / 2
  max_z_up = math.pi / 2

  def game_input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.done = True
      if event.type == pygame.MOUSEMOTION:
        dx, dy = event.rel
        self.angle = self.angle - math.pi * dx / (self.fps * 15)
        self.z_angle = max(self.min_z_down, min(self.z_angle - math.pi * dy / (self.fps * 15), self.max_z_up))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
      self.angle = self.angle + math.pi / self.fps
    if pressed[pygame.K_e]:
      self.angle = self.angle - math.pi / self.fps
    if pressed[pygame.K_w]:
      self.y += math.sin(self.angle)
      self.x += math.cos(self.angle)
    if pressed[pygame.K_s]:
      self.y -= math.sin(self.angle)
      self.x -= math.cos(self.angle)
    if pressed[pygame.K_a]:
      self.y += math.cos(self.angle)
      self.x -= math.sin(self.angle)
    if pressed[pygame.K_d]:
      self.y -= math.cos(self.angle)
      self.x += math.sin(self.angle)
    if pressed[pygame.K_SPACE]:
      self.z_acceleration = 0.5
    if pressed[pygame.K_ESCAPE]:
      self.done = True

  def game_update(self):
    self.z_acceleration += self.gravity / self.fps
    self.z = max(self.z + self.z_acceleration, self.z_base)
    glLoadIdentity()
    gluPerspective(45, (self.width / self.height), 0.1, self.max_distance)
    gluLookAt(self.x, self.y, self.z, self.x + self.far_away * math.cos(self.angle), self.y + self.far_away * math.sin(self.angle), self.z + self.far_away * math.sin(self.z_angle), 0, 0, 1)

  def game_display(self):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    self.game_map.display()
    self.thing.display()

  def __init__(self, width, height):
    pygame.init()
    self.width = width
    self.height = height
    pygame.display.set_mode((width , height), DOUBLEBUF|OPENGL)
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)

    while not self.done:
      self.game_input()
      self.game_update()
      self.game_display()

      pygame.display.flip()
      self.clock.tick(self.fps)

if __name__ == '__main__':
    game = Game(800, 600)