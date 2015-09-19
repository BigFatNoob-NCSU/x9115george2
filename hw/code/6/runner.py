from __future__ import print_function
__author__ = 'george'

from models.schaffer import Schaffer

if __name__ == "__main__":
  o = Schaffer()
  print(o.evaluate([1]))
