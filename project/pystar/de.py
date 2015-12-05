from __future__ import print_function, division
import sys
__author__ = 'george'
sys.dont_write_bytecode = True
from lib import *
import time

MIN_FRONTIER_SIZE=10

def default():
  return O(
    gens = 100,
    candidates = 50,
    f = 0.75,
    cr = 0.3,
    seed = 1,
    better = [gt, gt, lt],
    obj_funcs = [eval_softgoals, eval_goals, eval_costs],
    evaluation = Point.evaluate,
    is_percent = True,
    binary = True
  )

def eval_roots(model):
  return model.evaluate_score()

def eval_goals(model):
  return model.evaluate_type(node_type="goal", is_percent=default().is_percent)

def eval_softgoals(model):
  return model.evaluate_type(node_type="softgoal", is_percent=default().is_percent)

def eval_all_goals(model):
  return model.evaluate_type(node_type=["softgoal", "goal"], is_percent=default().is_percent)

def eval_coverage(model):
  covered = len(model.get_tree().get_nodes_covered())
  if default().is_percent:
    return percent(covered, len(model.get_tree().get_nodes()))
  else:
    return len(model.get_tree().get_nodes_covered())

def eval_costs(model):
  total_cost = 0
  for node, cost in zip(model.bases, model.costs):
    if node.value and node.value > 0:
      total_cost += cost
  return total_cost


class Point(O):
  id = 0
  def __init__(self, decisions, objectives=None):
    O.__init__(self)
    Point.id += 1
    self.id = Point.id
    self.decisions = decisions
    self.objectives = objectives
    self._nodes = None

  def get_nodes(self):
    return self._nodes

  def get_randomness(self):
    count = 0
    for node in self._nodes:
      if node.is_random: count+=1
    return percent(count, len(self._nodes))

  def __hash__(self):
    if type(self.decisions) == dict:
      return hash(frozenset(self.decisions.items()))
    return hash(frozenset(self.decisions))

  def __eq__(self, other):
    return cmp(self.decisions, other.decisions) == 0

  @staticmethod
  def evaluate(point, model, obj_funcs):
    if not point.objectives:
      model.reset_nodes(point.decisions)
      point.objectives = [func(model) for func in obj_funcs]
      point._nodes = [node.clone() for node in model.get_tree().get_nodes()]
    return point.objectives

  @staticmethod
  def evaluate_random(point, model, obj_funcs):
    if point.objectives:
      return point.objectives
    model.reset_nodes(point.decisions)
    model.evaluate_random()
    point.objectives = [func(model) for func in obj_funcs]
    point._nodes = [node.clone() for node in model.get_tree().get_nodes()]
    return point.objectives


  @staticmethod
  def trim(val):
    if val > 0:
      return t
    else:
      return f


class DE(O):
  def __init__(self, model, **settings):
    O.__init__(self)
    self.model = model
    self.settings = default().update(candidates=self.assign_frontier_size()).update(**settings)
    seed(self.settings.seed)

  def assign_frontier_size(self):
    num_decs = len(self.model.generate().keys())
    return min(int(2**num_decs), default().candidates)

  def generate(self, size):
    population = list()
    while len(population) < size:
      point = Point(self.model.generate())
      if not point in population:
        population.append(point)
    return population

  def run(self):
    """
    Runner function to run differential evolution
    :return: Optimal population
    """
    settings = self.settings
    #print(settings)
    stat = Statistics()
    start = time.time()
    if settings.candidates < MIN_FRONTIER_SIZE:
      raise RuntimeError(500, "Cannot generate %s candidates with %s leaves"
                %(settings.candidates, len(self.model.roots)))
    population = self.generate(settings.candidates)
    stat.insert(population)
    for _ in range(self.settings.gens):
      clones = population[:]
      for point in population:
        original_obj = settings.evaluation(point, self.model, settings.obj_funcs)
        mutant = self.mutate(point, population)
        mutated_obj = settings.evaluation(mutant, self.model, settings.obj_funcs)
        if self.dominates(mutated_obj, original_obj) and (not mutant in clones):
          clones.remove(point)
          clones.append(mutant)
      population = clones
      stat.insert(population)
    stat.runtime = time.time() - start
    return stat

  def dominates(self, obj1, obj2):
    at_least = False
    for i,(a, b) in enumerate(zip(obj1, obj2)):
      if self.settings.better[i](a,b):
        at_least = True
      elif a == b:
        continue
      else:
        return False
    return at_least

  def mutate(self, one, pop):
    """
    Function to mutate point using
    DE mutation strategy and return it
    :param one: Point to be mutated
    :param pop: Population to mutate from
    :return: Mutated point
    """
    if self.settings.binary:
      return self.mutate_binary(one, pop)
    else:
      return self.mutate_real(one, pop)

  def mutate_real(self, one, pop):
    """
    Function to perform real mutation to
    compute real values
    :param one: Point to be mutated
    :param pop: Population to selected from
    :return: mutant
    """
    two, three, four = DE.three_others(one, pop)
    random_key = choice(one.decisions.keys())
    mutated_decs = one.decisions.copy()
    for key in one.decisions.keys():
      if (rand() < self.settings.cr) or (key == random_key):
        mutated_decs[key] = Point.trim(two.decisions[key] + self.settings.f * (three.decisions[key] - four.decisions[key]))
    return Point(mutated_decs)

  def mutate_binary(self, one, pop):
    two, three, four = DE.three_others(one, pop)
    random_key = choice(one.decisions.keys())
    mutated_decs = one.decisions.copy()
    crossover_vector = [t if rand() < self.settings.f else f for _ in mutated_decs]
    for i, key in enumerate(one.decisions.keys()):
      if (rand() < self.settings.cr) or (key == random_key):
        mutated_decs[key] = OR(two.decisions[key], AND(crossover_vector[i], XOR(three.decisions[key], four.decisions[key])))
    return Point(mutated_decs)


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

def XOR(a, b):
  if (a==t and b==f) or (a==f and b==t):
    return t
  return f

def OR(a, b):
  if a==t or b==t:
    return t
  return f

def AND(a, b):
  if a==t and b==t:
    return t
  return f
