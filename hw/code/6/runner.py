from __future__ import print_function
__author__ = 'george'

from models.schaffer import Schaffer
from models.osyczka import Osyczka2
from models.kursawe import Kursawe
from algorithms.simulated_annealing import SA
from algorithms.max_walk_sat import MWS

if __name__ == "__main__":
  for model in [Schaffer, Osyczka2, Kursawe]:
    for optimizer in [SA, MWS]:
      print("Optimizer : " + optimizer.__name__)
      o = optimizer(model())
      o.run()
      print("* " * 30)
      print("\n")

