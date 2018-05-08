# author Frenk
from functools import partial

import time

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import astar_search, NailBox, depth_limited_search, breadth_first_tree_search, depth_first_tree_search
import utils

def init():
    statoIniziale = ((0, 0), (1, 0), (2, 'a'), (3, 'b'), (4, 'c'), (5, 0), (6, 0))
    problema = NailBox(statoIniziale)
    alg = astar_search(problema)
    #o in caso breadth_first_graph_search oppure depth_first_graph_search
    pp = alg.path()
    soluzione = alg.solution()
    for i in range(1, len(pp)):
        stato = pp[i].state
        costo = pp[i].path_cost
        azione = soluzione[i-1]
        print(str(azione) + "\t\t\t" + str(stato) + "\t\t\t" + str(costo))

init()
