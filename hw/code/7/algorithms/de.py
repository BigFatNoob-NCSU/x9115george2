from __future__ import print_function, division
__author__ = 'george'

from utils.lib import *
from algorithm import *

def default():
  return O(
    gens = 100,
    candidates = 50,
    f = 0.75,
    cr = 0.3,
    seed = 1,
    better = lt,
    verbose = True
  )


class DE(Algorithm):
  def __init__(self, model, settings=None):
    if not settings:
      settings = default()
    Algorithm.__init__(self, model, settings)

  def dominates(obj1, obj2):
    """
    Static method to check if one objective
    dominate the other.
    :param obj1: List of points A
    :param obj2: List of points B
    :param better: greater/lesser function that used for domination
    """
    at_least = False
    for a, b in zip(obj1, obj2):
      if self.settings.better(a,b):
        at_least = True
      elif a == b:
        continue
      else:
        return False
    return at_least


  def dominates_single(self, obj1, obj2):
    """
    Static method that uses fromHell to check
    :param obj1: Objectives1
    :param obj2: Objectives2
    :param hells: List of worst values for each objective
    :return: boolean indicating if obj1 dominates obj2
    """
    hells=self.model.hells()
    def from_hell(obj):
      norms = [self.model.objectives[i].norm(val) for i, val in enumerate(obj)]
      return [abs(i-j) for i,j in zip(norms, hells)]
    def energy(obj):
      return 1-(sum(from_hell(obj))/len(obj))**0.5
    return self.settings.better(energy(obj1), energy(obj2))


  @staticmethod
  def three_others(one, pop):
    """
    Return three other points from population
    :param one: Point not to consider
    :param pop: Population to look in
    :return: two, three, four
    """
    def one_other():
      while True:
        x = choice(pop)
        if not x.id in seen:
          seen.append(x.id)
          return x
    seen = [one.id]
    two = one_other()
    three = one_other()
    four = one_other()
    return two, three, four

  def generate(self, size):
    """
    Generate a population of size "size"
    :param size: Size of population to generate
    """
    pop = list()
    while len(pop) < size:
      point = Point(self.model.generate())
      if not point in pop:
        pop.append(point)
    return pop

  def mutate(self, one, pop):
    """
    Function to mutate point using
    DE mutation strategy and return it
    :param one: Point to be mutated
    :param pop: Population to mutate from
    :return: Mutated point
    """
    two, three, four = DE.three_others(one, pop)
    r = choice(range(len(one.decisions)))
    mutated_decs = one.decisions[:]
    for i in range(len(one.decisions)):
      if (rand() < self.settings.cr) or (r == i):
        mutated_decs[i] = self.model.decisions[i].limit(
          two.decisions[i] + self.settings.f * (three.decisions[i] - four.decisions[i]))
    return Point(mutated_decs)

  def run(self):
    """
    Runner function to run the
    Differential Evolution algorithm
    :return: Best solution, Objectives and number of evals
    """
    model = self.model
    settings = self.settings
    if settings.verbose:
      print(model)
      print(settings)
    front = Front()
    evals = 0
    pop = self.generate(settings.candidates)
    evals += settings.candidates
    for _ in range(self.settings.gens):
      say(".")
      clones = pop[:]
      for point in pop:
        original_obj = point.evaluate(model)
        mutant = self.mutate(point, pop)
        if not model.check_constraints(mutant.decisions):
          continue
        mutated_obj = mutant.evaluate(model)
        evals += 1
        if self.dominates_single(mutated_obj, original_obj) and (not mutant in clones):
        #if DE.dominates(mutated_obj, original_obj, better=settings.better):
          clones.remove(point)
          clones.append(mutant)
      pop = clones
    front.points = pop
    front.evals = evals
    print("")
    return front


