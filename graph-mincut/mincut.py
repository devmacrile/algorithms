""" 
Implementation of Karger's random contraction for finding the minimum cut of a graph
"""

import random
import time
from math import log
from unionfind import UnionFind

def mincut(nodes, edges):
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
    
if __name__ == "__main__":
    
    start = time.time()
    min_cut = 100000
    nodes = []
    edges = []
    fname = "data/kargerMinCut.txt"
    with open(fname) as f:
        for line in f:
    	    vals = line.split()
    	    node = int(vals[0]) - 1
    	    nodes.append(node)
    	    for v in vals[1:]:
    	        if node < int(v):
    	        # Doing this to only add the (undirected) edge once to the list
    	            edges.append((node, int(v) - 1))
    	        
    # Karger's min cut is a random algorithm, so need to run multiple times to achieve
    # certain probabilistic guarantees (i.e. n*lg(n) for 1/n failure probability, 
    # where n is the number of nodes)       
    n = len(nodes)
    trials = 100 # n * log(n)
    print "Estimated processing time is ", float(trials) * .0325, " seconds..."
    for i in range(trials):
        cut = mincut(nodes[:], edges[:])
        if len(cut) < min_cut:
            best_cut = cut
            min_cut = len(cut)
        
    print "Elapsed: ", time.time() - start
    print "Min cut: ", min_cut
    if min_cut < 50:
        print "Best cut: ", best_cut
			