from __future__ import print_function, division
from utils.lib import *

__author__ = 'george'


class Decision(O):
  def __init__(self, name, low, high):
    self.name = name
    self.low  = low
    self.high = high

  def norm(self, val):
    return norm(val, self.low, self.high)

  def de_norm(self, val):
    return de_norm(val, self.low, self.high)

class Objective(O):
  def __init__(self, name, low=None, high=None, to_minimize=True):
    self.name = name
    self.low = low
    self.high = high
    self.to_minimize = to_minimize

  def norm(self, val):
    return norm(val, self.low, self.high)

  def de_norm(self, val):
    return de_norm(val, self.low, self.high)

class Constraint(O):
  def __init__(self, name):
    self.name = name
    self.value = None
    self.status = True

class Model(O):
  def __init__(self):
    self.name         = None
    self.decisions    = []
    self.objectives   = []
    self.constraints  = []
    self.population   = []

  def generate(self, generator=uniform):
    while True:
      one = [generator(d.low, d.high) for d in self.decisions]
      status = self.evaluate_constraints(one)[0]
      if status: return one

  def evaluate(self, one):
    """
    Evaluate one based on the models
    :param one: Set of decisions to evaluate
    :return: Evaluated set of objectives
    """
    pass

  def evaluate_constraints(self, one):
    """
    Evaluate constraints for set
    of decisions
    :param one: List of decisions
    :return: Status of evaluation and value of offset if constraint fails
    """
    return True, None

  def check_constraints(self, one):
    return True

  def norm_objectives(self, one):
    """
    Normalize objectives
    :param one: Objectives
    :return: Normalized objectives
    """
    return [self.objectives[i].norm(o) for i, o in enumerate(one)]

  def norm_decisions(self, one):
    """
    Normalize decisions
    :param one: Decisions
    :return: Normalized Decisions
    """
    return [self.decisions[i].norm(o) for i, o in enumerate(one)]
