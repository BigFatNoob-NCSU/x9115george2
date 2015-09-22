from __future__ import print_function
__author__ = 'george'

from models.schaffer import Schaffer
from algorithms.simulated_annealing import SA
from algorithms.max_walk_sat import MWS

if __name__ == "__main__":
  o = Schaffer()
  a = SA(o)
  print(a.run())
