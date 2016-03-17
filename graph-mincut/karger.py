""" 
Implementation of Karger's random contraction for finding the minimum cut of a graph
"""

import random
from math import log
from unionfind import UnionFind

def karger(nodes, edges):
    uf, edges = contract(nodes, edges)
    cut = get_cut(uf, edges)
    return cut  

def contract(nodes, edges):
    """
    nodes: list from 0 to n-1 where n is the number of nodes
    edges: list of tupes (x, y) where x,y are both in set of node ids
    """
    uf = UnionFind(len(nodes))
    while uf.set_count() > 2:
        e = random.choice(edges)
        if not uf.find(e[0], e[1]):
            uf.union(e[0], e[1])
        edges.remove(e)
    
    return uf, edges
    
def get_cut(uf, edges):
    """
    Use computed union find structure to determine cut of graph
    """
    cut = []
    for e in edges:
        if not uf.find(e[0], e[1]):
            cut.append(e)
    return cut