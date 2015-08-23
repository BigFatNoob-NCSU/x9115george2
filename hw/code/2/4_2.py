__author__ = 'panzer'
from swampy.TurtleWorld import *
from math import pi


def initTurtle(delay = 0.01):
  """
  Initializes a turtle object
  :param delay: Delay before each action of the turtle. Lower it is the faster the turtle moves.
  :return: turtle object
  """
  TurtleWorld()
  t = Turtle()
  t.delay = delay
  return t

def polyline(t, n, length, angle):
  """
  Draws a polyline turning left.
  :param t: Turtle object
  :param n: number of sides
  :param length: length of a side
  :param angle: angle to turn
  :return: draws polyline
  """
  for _ in range(n):
    fd(t, length)
    lt(t, angle)


def polygon(t, n, length):
  """
  Draws a polygon
  :param t: Turtle Object
  :param n: number of sides
  :param length: length of each side
  :return: draws polygon
  """
  angle = 360.0 / n
  polyline(t, n, length, angle)


def arc(t, radius, angle):
  """
  Draws an arc
  :param t: Turtle object
  :param radius: radius of the arc
  :param angle: angle of the arc
  :return: draws arc
  """
  arc_length = 2 * pi * radius * angle / 360.0
  n = int(arc_length / 3) + 1
  step_length = arc_length / n
  step_angle = float(angle) / n
  polyline(t, n, step_length, step_angle)


def circle(t, radius):
  """
  Draws a circle
  :param t: Turtle object
  :param radius: radius of circle
  :return: draws circle
  """
  arc(t, radius, 360)


def petal(t, radius, angle):
  """
  Draws a petal for the flower
  :param t: Turtle object
  :param radius: Radius of the petal's arc
  :param angle: Angle subtended by petal's arc
  :return: draws petal
  """
  for  _ in range(2):
    arc(t, radius, angle)
    lt(t, 180 - angle)


def flower(t, n, radius, angle):
  """
  Draws a flower
  :param t: Turtle Object
  :param n: Number of petals
  :param radius: Radius of each petal's arc
  :param angle: angle subtended by petal's arc
  :return: draws flower
  """
  for _ in range(n):
    petal(t, radius, angle)
    lt(t, float(360.0/n))


if __name__ == "__main__":
  # Figure 4.1 a
  flower(initTurtle(), 7, 100, 60)

  # Figure 4.1 b
  flower(initTurtle(), 10, 100, 80)

  # Figure 4.1 c
  flower(initTurtle(), 20, 300, 20)
  wait_for_user()