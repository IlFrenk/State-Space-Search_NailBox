# author Frenk
from functools import partial

import time

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import astar_search, NailBox, depth_limited_search, breadth_first_tree_search, depth_first_tree_search
import utils

def init():
    state = ()
    problem = NailBox(state)
    star = astar_search(problem)
    solution = star.solution()
    print("prova")
    path = star.path()
    for i in range(i, len(path)):
        s = path[i].state
        c = path[i].path_cost
        a = solution[i-1]
        #print(str(a) + "\t\t\t" + str(s) + "\t\t\t" + str(c))

init()
