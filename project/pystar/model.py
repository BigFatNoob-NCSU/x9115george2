from __future__ import print_function, division
__author__ = 'george'
import sys,os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from template import *
import random

t =  1
f = -1

def coin_toss():
  return random.choice([t, f])

def percent(num, den):
  if den==0:
    return 0
  return round(num*100/den, 2)

def shuffle(lst):
  if not lst:
    return []
  random.shuffle(lst)
  return lst

class Model(O):
  def __init__(self, tree):
    O.__init__(self)
    self._tree = tree
    self.roots = self._tree.get_roots()
    self.bases = self._tree.get_bases()
    self.chain = set()
    self.recursions = 0
    self.costs = []
    self.assign_costs()

  def assign_costs(self):
    rands = range(1,6)
    costs = []
    for _ in self.bases:
      costs.append(random.choice(rands))
    self.costs = costs


  def get_tree(self):
    return self._tree

  def generate(self):
    point_map = {}
    for node in self.bases:
      point_map[node.id] = random.choice([t, f])
    return point_map

  def clear_nodes(self):
    for node in self._tree.nodes:
      node.value = None
      node.is_random = False

  def reset_nodes(self, initial_node_map):
    self.clear_nodes()
    for key in initial_node_map.keys():
      node = self._tree.get_node(key)
      node.value = initial_node_map[key]

  def evaluate_score(self, initial_node_map):
    self.clear_nodes()
    for key in initial_node_map.keys():
      node = self._tree.get_node(key)
      node.value = initial_node_map[key]
    return self.score()

  def evaluate_type(self, node_type, is_percent=False):
    count = 0
    nodes = shuffle(self._tree.get_nodes(node_type=node_type))
    for node in nodes:
      self.chain = set()
      self.eval(node)
      if node.value > 0:
        count += 1
    if is_percent:
      return percent(count, len(nodes))
    else:
      return count

  def evaluate_random(self):
    def check_status():
      for node in self._tree.nodes:
        if node.type in ["goal", "softgoal"] and (not node.value):
          return False
      return True
    for _ in range(len(self._tree.nodes)//2):
      self.chain = set()
      self.eval(random.choice(self._tree.nodes))


  def eval_node(self, node):
    self.chain=set()
    self.eval(node)

  def scores(self, n=1000, seed_val=None):
    """
    Evaluate the graph n times and
    return the average value
    :param n: Number of evals
    :param seed_val: Random seed to be set
    :return: The average score
    """
    from utilities.sk import rdivDemo
    if not seed_val is None:
      random.seed(seed_val)

    final = []
    for _ in xrange(n):
      for node in self._tree.nodes:
        node.value = None
      final.append(self.score())
    final = ["Roots"] + final
    rdivDemo([final])

  def score(self):
    """
    Back Propagation
    Count how many root nodes are covered
    :return: root nodes covered
    """
    count = 0
    for node in self.roots:
      self.chain = set()
      self.recursions = 0
      self.eval(node)
      if node.value > 0:
        count += 1
    return count

  def dep_and_rest(self, edges):
    """
    Split edges into dependencies and the rest
    :param edges:
    :return:
    """
    deps = []
    rest = []
    for edge_id in edges:
      edge = self._tree.get_edge(edge_id)
      if edge.type == "dependency":
        deps.append(edge)
      else:
        rest.append(edge)
    return shuffle(deps), shuffle(rest)

  @staticmethod
  def random_node_val(node):
    """
    Return a random value for a node
    :param node:
    :return:
    """
    if node.type in ["goal", "softgoal"]:
      return t
    return coin_toss()

  def eval(self, node):
    if not (node.value is None):
      return node.value

    if node.id in self.chain:
      node.value = Model.random_node_val(node)
      node.is_random = True
      return
    self.recursions += 1
    self.chain.add(node.id)
    if not node.from_edges:
      node.value = Model.random_node_val(node)
      node.is_random = True
      return
    else:
      # First check for dependencies from the edges and evaluate it
      # Ask @jenhork about it

      deps, rest= self.dep_and_rest(node.from_edges)
      # if rest and rest[0].type == "contribution":
      #   exit()
      # Check if all dependencies are satisfied
      dep_nodes = [self._tree.get_node(dep.source) for dep in deps]


      if not rest:
        node.value = self.eval_and(dep_nodes)
        return

      # Evaluate the rest. We assume the rest are of same kind
      edge_type = rest[0].type
      if edge_type == "decompositions":
        status = self.eval_and(dep_nodes)
        if status < 0:
          node.value = status
          return
        kids = [self._tree.get_node(edge.source) for edge in rest]
        if rest[0].value == "and":
          # Evaluate all children
          status = self.eval_and(kids)
        elif rest[0].value == "or":
          status = self.eval_or(kids)
      elif edge_type == "contribution":
        status = self.eval_contribs(rest, deps)
      else:
        raise Exception("Unexpected edge type %s"%edge_type)
      node.value = status
      return

  def eval_and(self, nodes):
    """
    Evaluate all the nodes in the tree
    :param nodes: Nodes to be evaluated
    :return: status
    """
    status = t
    for node in nodes:
      if status <= 0: break
      self.eval(node)
      status = node.value
    return status

  def eval_or(self, nodes):
    """
    Evaluate all the nodes in the tree
    till a node is evaluated as true
    :param nodes: Nodes to be evaluated
    :return: status
    """
    for node in nodes:
      self.eval(node)
      status = node.value
      if status > 0:
        return status
    return f

  def eval_contribs(self, edges, dependencies=None):
    """
    Evaluate cumulative of contributions
    based on the weight.
    :param edges: Nodes to be evaluated
    :return: status
    """
    kids = []
    for edge in edges:
      if edge.type != "contribution":
        continue
      node = self._tree.get_node(edge.source)
      self.eval(node)
      kids += [Model.soft_goal_val(node.value, edge.value)]
    if dependencies:
      for dep in dependencies:
        dep_node = self._tree.get_node(dep.source)
        self.eval(dep_node)
        kids += [Model.soft_goal_val(dep_node.value, "make")]
    return random.choice(kids)

  @staticmethod
  def soft_goal_val(kid, edge):
    """
    Check out src/img/prop_rules.png
    :param kid:
    :param edge:
    :return:
    """
    if edge in ["someplus", "someminus"]:
      return random.choice([t/2, f/2])
    if kid == t:
      if edge == "make"   : return t
      if edge == "help"   : return t/2
      if edge == "hurt"   : return f/2
      if edge == "break"  : return f
    elif kid == t/2:
      if edge == "make"   : return t/2
      if edge == "help"   : return t/2
      if edge == "hurt"   : return f/2
      if edge == "break"  : return f/2
    elif kid == f/2:
      if edge == "make"   : return f/2
      if edge == "help"   : return f/2
      if edge == "hurt"   : return t/2
      if edge == "break"  : return t/2
    elif kid == f:
      if edge == "make"   : return f
      if edge == "help"   : return f/2
      if edge == "hurt"   : return t/2
      if edge == "break"  : return t/2

    raise RuntimeError("Either node value %s or edge %s is unknown"%(kid, edge))