""" 
Implementation of Karger's random contraction for finding minimum cut of a graph
"""

import random
from graph import Graph
from graph import Vertex
from graph import Edge
from unionfind import UnionFind

def mincut():
    nodes = []
    edges = []

    fname = "data/kargerMinCut.txt"
    with open(fname) as f:
        for line in f:
    	    vals = line.split()
    	    node = vals[0] - 1
    	    nodes.append(node)
    	    for v in vals[1:]:
    	        node2 = v - 1
    	        edges.append[(node, node2)]
    uf = contract(nodes, edges)
    cut = get_cut(uf, edges)
    return cut  

def contract(nodes, edges):
    """
    nodes: list from 0 to n-1 where n is the number of nodes
    edges: list of tupes (x, y) where x,y are both in set of node ids
    """
    
    uf = UnionFind(len(nodes))
    while uf.num_sets() > 2:
        e = random.choice(edges)
        if not uf.find(e[0], e[1]):
            uf.union(e[0], e[1])
            edges.remove(e)
    
    return uf
    
def get_cut(uf, edges):
    """
    Use computed union find structure to determine cut of graph
    """
    cut = []
    for e in edges:
        if not uf.find(e[0], e[1]):
            cut.append(e)
    return cut
			