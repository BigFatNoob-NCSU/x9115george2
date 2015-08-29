from __future__ import print_function, division
__author__ = 'george'

import random, sys, math

class Point():
  def __init__(self, name, hi=1, lo=0):
    self.name = name
    self.hi = hi
    self.lo = lo

  def norm(self, value):
    return (value - self.lo) / (self.hi - self.lo)

  def denorm(self, value):
    return (self.hi - self.lo)*value + self.lo

class Schaffer():
  def __init__(self, dec_hi=1, dec_lo=0, obj_hi=1, obj_lo=0):
    self.decision = Point("x",dec_hi, dec_lo)
    self.objective = Point("f1+f2", obj_hi, obj_lo)

  def eval(self, decision, do_normalize=True):
    f1 = decision ** 2
    f2 = (decision - 2) ** 2
    if do_normalize:
      return self.objective.norm(f1+f2)
    else:
      return f1+f2

  def denorm(self, obj):
    return self.objective.denorm(obj)

  def generate(self):
    return rand(self.decision.lo, self.decision.hi)

  def neighbor(self, old, prob=0.5):
    return self.generate() if random.random() < prob else old

  def get_objective_extremes(self, repeats=1000000):
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
  mul = int(1/step)
  return random.randrange(start*mul, stop*mul, 1) * step


def simulated_anneal(model, kmax=1000, cooling=0.5):
  def anneal(old, new, temp):
    a = math.e**((old - new)/temp)
    b = random.random()
    return  a < b
  k=0
  this = model.generate()
  e_this = model.eval(this)
  best, e_best = this, e_this
  out = ""
  while k < kmax:
    k+=1
    near = model.neighbor(this, 1)
    e_near = model.eval(near)
    key = " ."
    if e_near < e_this :
      key = " +"
      this, e_this = near, e_near
    elif anneal(e_this, e_near, (k/kmax)**cooling):
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
  dec_hi = 10**2
  dec_lo = -dec_hi
  dummy = Schaffer(dec_hi=dec_hi, dec_lo=dec_lo)
  obj_hi, obj_lo = dummy.get_objective_extremes()

  model = Schaffer(dec_hi=dec_hi, dec_lo=dec_lo, obj_hi=obj_hi, obj_lo=obj_lo)
  print(simulated_anneal(model))

if __name__ == "__main__":
  _test()


