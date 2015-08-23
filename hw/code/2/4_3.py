__author__ = 'panzer'
from swampy.TurtleWorld import *
from math import radians, sin

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

def isosceles(t, eq_side, ineq_side, angle):
  """
  Draws an isosceles triangle
  :param t: Turtle object
  :param eq_side: Equal Side
  :param ineq_side: Inequal Side
  :param angle: Angle by the inequal side
  :return: draws isosceles triangle
  """
  fd(t, eq_side)
  lt(t, angle)
  fd(t, ineq_side)
  lt(t, angle)
  fd(t, eq_side)

def pie(t, n, length):
  """
  Draws a pie
  :param t: Turtle object
  :param n: number of sides
  :param length: length of each side
  :return: Draws a Pie(Spiked polygon)
  """
  angle = float(360.0/n)
  eq_side = length/2.0/sin(radians(angle/2.0))
  for _ in range(n):
    isosceles(t, eq_side, length, 180 - (180 - angle)/2.0)
    lt(t, 180)

if __name__ == '__main__':
  # Figure 4.2 a
  pie(initTurtle(), 5, 100)

  # Figure 4.2 a
  pie(initTurtle(), 6, 100)

  # Figure 4.2 a
  pie(initTurtle(), 7, 100)
  wait_for_user()