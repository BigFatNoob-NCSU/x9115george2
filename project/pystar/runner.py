from __future__ import print_function, division
from graphviz.dot_models import *
__author__ = 'panzer'
from de import DE
from model import Model

def run_de(graph):
  model = Model(graph)
  de = DE(model)
  stat = de.run()
  stat.tiles()

run_de(CSServices())