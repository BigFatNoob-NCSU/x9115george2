from __future__ import print_function, division
__author__ = 'george'

import random, sys, math


def rand(start, stop, step=1):
  """
  Generate a random number between a range
  :param start: start value
  :param stop: stop value
  :param step: increment value
  :return:
  """
  mul = int(1/step)
  return random.randrange(start*mul, stop*mul, 1) * step

class Point:
  def __init__(self, name, hi=1, lo=0, step = 0.01):
    """
    Create a point
    :param name: Name of the point
    :param hi: Max value of the point
    :param lo: Min value of the point
    :return: Instance of Point
    """
    self.name = name
    self.hi = hi
    self.lo = lo
    self.step = step

  def norm(self, value):
    """
    Normalize a value as (value - lo)/(hi - lo)
    :param value:Value to be normalized
    :return:
    """
    return (value - self.lo) / (self.hi - self.lo)

  def denorm(self, value):
    """
    Denormalizes a value as (hi-lo)*value _ lo
    :param value:
    :return:
    """
    return (self.hi - self.lo)*value + self.lo

class Osyczka2():
  def __init__(self, dec_hi, dec_lo, obj_hi=1, obj_lo=0):
    """
    Initialize an osyczka2 model
    :param dec_lo: Array of upper bounds for decisions
    :param dec_hi: Array of lower bounds for decisions
    :param obj_hi: Upper bound for objective
    :param obj_lo: Lower bound for objective
    :return:
    """
    decisions = []
    pts = 100
    for i in range(6):
      decisions.append(Point("x"+str(i+1),
                             dec_hi[i], dec_lo[0],
                             (dec_hi[i]-dec_lo[i])/pts))
    self.decisions = decisions
    self.objectives = [Point("f1 + f2", obj_hi, obj_lo)]

  @staticmethod
  def get_objectives(decisions):
    f1 = -(25*(decisions[0] - 2)**2 +
           (decisions[1] - 2)**2 +
           (decisions[2] - 1)**2 * (decisions[3]-4)**2 +
           (decisions[4] - 1)**2)
    f2 = sum([d**2 for d in decisions])
    return f1, f2

  @staticmethod
  def check_constraints(decisions):
    #g1(x)
    status = decisions[0] + decisions[1] - 2 >= 0
    #g2(x)
    status = status and (6 - decisions[0] - decisions[1] >= 0)
    #g3(x)
    status = status and (2 - decisions[1] + decisions[0] >= 0)
    #g4(x)
    status = status and (2 - decisions[0] + 3*decisions[1] >= 0)
    #g5(x)
    status = status and (4 - (decisions[2] - 3)**2 - decisions[3] >= 0)
    #g6(x)
    status = status and ((decisions[4] - 3)**3 + decisions[5] - 4 >= 0)
    return status

  def eval(self, decisions, do_normalize = True):
    """
    Evaluate the Osyczka2 model
    :param decisions: Decisions value
    :param do_normalize: Optional argument if it needs to be normalized before evaluating
    :return:
    """
    status = Osyczka2.check_constraints(decisions)
    if status:
      f1, f2 = Osyczka2.get_objectives(decisions)
      ret_val = f1 + f2
      if do_normalize:
        ret_val = self.objectives[0].norm(ret_val)
      return status, ret_val
    else:
      return status, None

  def generate(self):
    """
    Create a random number between the range of decisions
    :return:
    """
    generated = []
    for dec in self.decisions:
      generated.append(rand(dec.lo, dec.hi, dec.step))
    return generated

  def get_objective_extremes(self, repeats = 1000):
    """
    get the high and low for objectives
    :param repeats: Number of repeats before termination
    :return:
    """
    lo = sys.maxint
    hi = -lo - 1
    for _ in range(repeats):
      f1, f2 = Osyczka2.get_objectives(self.generate())
      val = f1 + f2
      if val > hi:
        hi = val
      elif val < lo:
        lo = val
    return hi, lo


def _test():
  """
  Dummy Test method.
  1) Random runs schaffer to get the extremes for objectives
  2) Once objectives are obtained its fed back into another instance of schaffer.
  3) Simulated annealing is used on this model
  :return:
  """
  dec_hi = [10, 10, 5, 6, 6, 10]
  dec_lo = [0, 0, 1, 0, 1, 0]
  dummy = Osyczka2(dec_hi, dec_lo)
  obj_hi, obj_lo = dummy.get_objective_extremes()
  print(obj_hi, obj_lo)


if __name__ == "__main__":
  _test()