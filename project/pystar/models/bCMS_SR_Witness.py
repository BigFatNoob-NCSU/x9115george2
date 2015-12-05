import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from template import *
__author__ = 'george'

N = Many()
# Nodes
n1 = N + SoftGoal(
  name = "Provide accurate Information",
)
n2 = N + SoftGoal(
  name = "To know what to do",
)
n3 = N + Task(
  name = "Follow instructions from firemen",
)
n4 = N + Task(
  name = "Provide crisis related info",
)
n5 = N + Task(
  name = "Provide to fireman",
)
n6 = N + Task(
  name = "Provide info to police",
)
n7 = N + HardGoal(
  name = "Receive instructions",
)
n8 = N + Resource(
  name = "Crisis-related information(Fire)",
)
n9 = N + Resource(
  name = "Instructions(Fire)",
)
n10 = N + Resource(
  name = "Instructions(Police)",
)
n11 = N + Task(
  name = "Crisis-related information(Police)",
)

E = Many()
#Edges
e1 = E + SomePlus(
  source = n7,
  target = n2
)
e2 = E + Or(
  source = n7,
  target = n3
)
e3 = E + And(
  source = n5,
  target = n4
)
e4 = E + And(
  source = n6,
  target = n4
)
e5 = E + Dep(
  source = n5,
  target = n8
)
e6 = E + Dep(
  source = n9,
  target = n7
)
e7 = E + Dep(
  source = n10,
  target = n7
)
e8 = E + Dep(
  source = n6,
  target = n11
)

graph = Graph(name="bCMS_SR_Witness", nodes=N.all, edges=E.all)