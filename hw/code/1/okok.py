"""
# Examples of Unit tests  in Python
"""
import time
from ok import *

print time.strftime("%H:%M:%S\n")

@ok
def _ok1():
  assert 1==1

@ok
def _ok2():
  assert 2==1

@ok
def _ok3():
  assert 3==3 

@ok
def _ok4():
  assert True==1

@ok
def _ok5():
  assert True==2

@ok
def _ok6():
  assert True==(not(not 2))

@ok
def _ok7():
  assert unittest.tries==7
  assert unittest.fails==2
  print unittest.score()
