import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class MapEdge:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def display(self):
    glVertex3f(self.start[0], self.start[1], self.start[2])
    glVertex3f(self.end[0], self.end[1], self.end[2])

class MapNode:
  def __init__(self, coord, width, height, depth, edges):
    self.coord = coord
    self.width = width
    self.height = height
    self.depth = depth
    self.edges = edges

  def display(self):
    for edge in self.edges:
      edge.display()

class Map:
  node_width = 1
  node_height = 1
  node_columns = 10
  node_rows = 10
  grid = []

  def __init__(self):
    for i in range(self.node_rows):
      for j in range(self.node_columns):
        edges = [
          MapEdge((i, j, 0), (i, j + self.node_height, 0)),
          MapEdge((i, j, 0), (i + self.node_width, j, 0))
        ]

        if(i == self.node_rows - 1):
          edges.append(
            MapEdge((i + self.node_width, j, 0), (i + self.node_width, j + self.node_height, 0))
          )

        if(j == self.node_columns - 1):
          edges.append(
            MapEdge((i, j + self.node_height, 0), (i + self.node_width, j + self.node_height, 0))
          )
        self.grid.append(MapNode((i, j, 0), self.node_width, self.node_height, 0, edges))

  def display(self):
    glColor3f(0, 1, 1)
    glBegin(GL_LINES)
    for x in self.grid:
      x.display()
    glEnd()