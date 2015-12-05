from __future__ import division, print_function
import sys, random, json, sk
from prettytable import PrettyTable

t = +1
f = -1

"""
Default class which everything extends.
"""
class O():
  def __init__(self,**d): self.has().update(**d)
  def has(self): return self.__dict__
  def update(self,**d): self.has().update(d); return self
  def __repr__(self)   :
    def _name(val):
      if isinstance(val, list):
        return [_name(v) for v in val]
      if hasattr(val, '__call__'):
        return val.__name__
      return val
    show=[':%s %s' % (k,_name(self.has()[k]))
      for k in sorted(self.has().keys() )
      if k[0] is not "_"]
    txt = ' '.join(show)
    if len(txt) > 60:
      show=map(lambda x: '\t'+x+'\n',show)
    return '{'+' '.join(show)+'}'
  def __getitem__(self, item):
    return self.has().get(item)
  def to_json(self):
    def dflt(obj):
      if isinstance(obj, set): return list(obj)
      return obj.__dict__
    return json.dumps(self, default=dflt, sort_keys=True, indent=4)
  def clone(self):
    cloned = O()
    for key, val in self.has().iteritems():
      cloned.__dict__[key] = val
    return cloned

"""
An accumulator for reporting on numbers.
"""
class N():
  "Add/delete counts of numbers."
  def __init__(self,inits=[]):
    self.zero()
    map(self.__iadd__,inits)
  def zero(self):
    self.n = self.mu = self.m2 = 0
    self.cache= Cache()
  def sd(self)  :
    if self.n < 2:
      return 0
    else:
      return (max(0,self.m2)/(self.n - 1))**0.5
  def __iadd__(self,x):
    self.cache += x
    self.n     += 1
    delta       = x - self.mu
    self.mu    += delta/(1.0*self.n)
    self.m2    += delta*(x - self.mu)
    return self
  def __isub__(self,x):
    self.cache = Cache()
    if self.n < 2: return self.zero()
    self.n  -= 1
    delta = x - self.mu
    self.mu -= delta/(1.0*self.n)
    self.m2 -= delta*(x - self.mu)
    return self

CACHE_SIZE=128
class Cache:
  "Keep a random sample of stuff seen so far."
  def __init__(self, inits=[]):
    self.all,self.n,self._has = [],0,None
    map(self.__iadd__,inits)
  def __iadd__(self,x):
    self.n += 1
    if len(self.all) < CACHE_SIZE: # if not full
      self._has = None
      self.all += [x]               # then add
    else: # otherwise, maybe replace an old item
      if random.random() <= CACHE_SIZE/self.n:
        self._has=None
        self.all[int(random.random()*CACHE_SIZE)] = x
    return self
  def has(self):
    if self._has == None:
      lst  = sorted(self.all)
      med,iqr = median_iqr(lst,ordered=True)
      self._has = O(
        median = med,      iqr = iqr,
        lo     = self.all[0], hi  = self.all[-1])
    return self._has

def median_iqr(lst, ordered=False):
  if not ordered:
    lst = sorted(lst)
  n = len(lst)
  q = n//4
  iqr = lst[q*3] - lst[q]
  if n % 2:
    return lst[q*2],iqr
  else:
    p = max(0,q-1)
    return (lst[p] + lst[q]) * 0.5,iqr

def choice(lst):
  return random.choice(lst)

def sample(lst, k):
  return random.sample(lst, k)

def rand():
  return random.random()

def seed(val=None):
  random.seed(val)

def gt(a, b):
  return a > b

def lt(a, b):
  return a < b

def shuffle(lst):
  if not lst:
    return []
  random.shuffle(lst)
  return lst

def sign(num):
  if num > 0:
    return 1
  else:
    return -1

def printm(matrix):
  s = [[str(e) for e in row] for row in matrix]
  lens = [max(map(len, col)) for col in zip(*s)]
  fmt = ' | '.join('{{:{}}}'.format(x) for x in lens)
  for row in [fmt.format(*row) for row in s]:
    print(row)

def say(*lst):
  print(*lst, end="")
  sys.stdout.flush()

def percent(num, den):
  if den==0:
    return 0
  return round(num*100/den, 2)

class Statistics(O):
  @staticmethod
  def default_settings():
    return O(
      gen_step = 20
    )
  def __init__(self, settings=None):
    O.__init__(self)
    self.generations = []
    self.runtime = 0
    if not settings:
      settings = Statistics.default_settings()
    self.settings = settings

  def insert(self, pop):
    self.generations.append(pop)
    return self

  def tiles(self):
    num_obs = len(self.generations[0][0].objectives)
    for i in range(num_obs):
      obj_gens=[]
      for gen, pop in enumerate(self.generations):
        if gen % self.settings.gen_step != 0:
          continue
        objs = ["gen"+str(gen)+"_f"+str(i+1)]
        for point in pop:
          objs.append(point.objectives[i])
        obj_gens.append(objs)
      sk.rdivDemo(obj_gens)

  def median_spread(self):
    num_obs = len(self.generations[0][0].objectives)
    data  = []
    for i in range(num_obs):
      data_map = {}
      meds = []
      iqrs = []
      for gen, pop in enumerate(self.generations):
        objs = [pt.objectives[i] for pt in pop]
        med, iqr = median_iqr(objs)
        meds.append(med)
        iqrs.append(iqr)
      data_map["meds"] = meds
      data_map["iqrs"] = iqrs
      data.append(data_map)
    return data

  def spit_objectives(self):
    objectives = []
    for point in self.generations[-1]:
      objectives.append(point.objectives)
    return objectives

  def tabulate(self, columns, pt):
    tab = PrettyTable(columns)
    tab.align["name"] = "l"
    nodes = pt.get_nodes()
    for node in nodes:
      row = []
      for key in columns:
        row.append(node.has()[key])
      tab.add_row(row)
    print(tab)