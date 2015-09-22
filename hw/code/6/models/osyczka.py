from __future__ import print_function, division
__author__ = 'george'

from model import *

class Osyczka2(Model):
  def __init__(self):
    Model.__init__(self)
    self.name = Osyczka2.__name__
    self.decisions = []
    self.decisions.append(Decision("x1", 0, 10))
    self.decisions.append(Decision("x2", 0, 10))
    self.decisions.append(Decision("x3", 1,  5))
    self.decisions.append(Decision("x4", 0,  6))
    self.decisions.append(Decision("x5", 1,  5))
    self.decisions.append(Decision("x6", 0, 10))
    self.objectives = []
    self.objectives.append(Objective("f1", -1920, -4, to_minimize=True))
    self.objectives.append(Objective("f2", 2, 386, to_minimize=True))


  @staticmethod
  def check_constraints(one):
    """
    Check if the constraints are satisfied for a set of decisions
    :param decisions:
    :return:
    """
    #g1(x)
    status = one[0] + one[1] - 2 >= 0
    #g2(x)
    status = status and (6 - one[0] - one[1] >= 0)
    #g3(x)
    status = status and (2 - one[1] + one[0] >= 0)
    #g4(x)
    status = status and (2 - one[0] + 3*one[1] >= 0)
    #g5(x)
    status = status and (4 - (one[2] - 3)**2 - one[3] >= 0)
    #g6(x)
    status = status and ((one[4] - 3)**3 + one[5] - 4 >= 0)
    return status

  def evaluate(self, one):
    return [Osyczka2.f1(one), Osyczka2.f2(one)]

  @staticmethod
  def f1(d):
    return -(25*(d[0]-2)**2 +
             (d[1]-2)**2 +
             (d[2]-1)**2 * (d[3]-4)**2 +
             (d[4]-1)**2)

  @staticmethod
  def f2(ds):
    return sum([d**2 for d in ds])

  @staticmethod
  def get_extreme_objectives():
    o = Osyczka2()
    f1s = []
    f2s = []
    for i in range(6):
      s = [0,0,1,0,1,0]
      for j in range(i+1):
        dec = o.decisions[j]
        for val in range(dec.low, dec.high+1, 1):
          s[j] = val
          f1s.append(Osyczka2.f1(s))
          f2s.append(Osyczka2.f2(s))
    print(min(f1s), max(f1s))
    print(min(f2s), max(f2s))



