from __future__ import print_function, division
__author__ = 'george'

from time import strftime
import random, sys, math

class Point:
  def __init__(self, name, hi=1, lo=0):
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

class Schaffer():
  def __init__(self, dec_hi=1, dec_lo=0, obj_hi=1, obj_lo=0):
    """
    Initialize a schaffer model
    :param dec_hi: High for decision
    :param dec_lo: Low for decision
    :param obj_hi: High for objectives
    :param obj_lo: Low for objectives
    :return: Instance of schaffer model
    """
    self.decision = Point("x",dec_hi, dec_lo)
    self.objective = Point("f1+f2", obj_hi, obj_lo)

  def __repr__(self):
    return "#" + strftime("%Y-%m-%d %H:%M:%S") + "\nSchaffer\n"

  @staticmethod
  def get_objectives(decision):
    return decision ** 2, (decision - 2) ** 2

  def eval(self, decision, do_normalize=True):
    """
    Evaluate the schaffer model
    :param decision: Decision value
    :param do_normalize: Optional argument if it needs to be normalized before evaluating
    :return:
    """
    f1, f2 = Schaffer.get_objectives(decision)
    if do_normalize:
      return self.objective.norm(f1+f2)
    else:
      return f1+f2

  def denorm(self, obj):
    """
    Denormalize an objective
    :param obj:
    :return:
    """
    return self.objective.denorm(obj)

  def generate(self):
    """
    Create a random number between the range of decisions
    :return:
    """
    return rand(self.decision.lo, self.decision.hi)

  def neighbor(self, old, prob=0.5):
    """
    Get a neighbor for a point
    :param old: The initial point
    :param prob: Probability to use neighbor
    :return:
    """
    return self.generate() if random.random() < prob else old

  def get_objective_extremes(self, repeats=1000000):
    """
    Get the high and low for objectives
    :param repeats: Number of repeats before termination
    :return:
    """
    lo = sys.maxint
    hi = -lo - 1
    for _ in range(repeats):
      val = self.eval(rand(self.decision.lo, self.decision.hi, 0.01), False)
      if val > hi:
        hi = val
      elif val < lo:
        lo = val
    return hi, lo


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


def simulated_anneal(model, kmax=1000, cooling=5):
  """
  Performs simulated annealing on a model
  :param model: Instance of the model
  :param kmax: Number of iterations before termination
  :param cooling: Annealing factor
  :return: Returns the best decision and denormalized objective
  """
  def anneal(old, new, temp):
    a = math.e**((old - new)/temp)
    b = random.random()
    return  a > b

  def anneal_simple(temp):
    return random.random() > temp

  print(model)
  print("Params    : ")
  print("\tkmax    : " + str(kmax))
  print("\tGradient: " + str(cooling))
  k=0
  this = model.generate()
  e_this = model.eval(this)
  best, e_best = this, e_this
  out = ""
  while k < kmax-1:
    k+=1
    near = model.neighbor(this, 1)
    e_near = model.eval(near)
    key = " ."
    if e_near < e_this :
      key = " +"
      this, e_this = near, e_near
    elif anneal(e_this, e_near, (1-(k/kmax))**cooling):
    #elif anneal_simple(k/kmax):
      key = " ?"
      this, e_this = near, e_near
    if e_this < e_best:
      key = " !"
      best, e_best = this, e_this
    out += key
    if  k % 50 == 0 :
      print(str(model.denorm(e_best)) + out)
      out = ""
  return best, model.denorm(e_best)


def _test():
  """
  Dummy Test method.
  1) Random runs schaffer to get the extremes for objectives
  2) Once objectives are obtained its fed back into another instance of schaffer.
  3) Simulated annealing is used on this model
  :return:
  """
  dec_hi = 10**2
  dec_lo = -dec_hi
  dummy = Schaffer(dec_hi=dec_hi, dec_lo=dec_lo)
  obj_hi, obj_lo = dummy.get_objective_extremes()

  model = Schaffer(dec_hi=dec_hi, dec_lo=dec_lo, obj_hi=obj_hi, obj_lo=obj_lo)
  best, energy = simulated_anneal(model)
  print("\nBest decision     :  ", best)
  print("Best Objectives     :  ", Schaffer.get_objectives(best))
  print("Denormalized Energy :  ", energy)


if __name__ == "__main__":
  _test()


