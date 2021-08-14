from OpenGL.GL import *
from OpenGL.GLU import *

class Thing:
  nodes = []
  edges = []

  def __init__(self, nodes, edges):
    self.nodes = nodes
    self.edges = edges

  def display(self):
    glColor3f(1, 0, 1)
    glBegin(GL_LINES)
    for edge in self.edges:
      glVertex3f(self.nodes[edge[0]][0], self.nodes[edge[0]][1], self.nodes[edge[0]][2])
      glVertex3f(self.nodes[edge[1]][0], self.nodes[edge[1]][1], self.nodes[edge[1]][2])
    glEnd()