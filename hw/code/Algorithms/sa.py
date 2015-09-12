from __future__ import print_function, division
import math, random
__author__ = 'george'



def simulated_anneal(model, kmax=1500, cooling=1):
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
    return  a < b
  print(model)
  print("Params    : ")
  print("\tkmax    : " + str(kmax))
  print("\tGradient: " + str(cooling))
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
    #elif anneal(e_this, e_near, 1 - k/kmax):
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
