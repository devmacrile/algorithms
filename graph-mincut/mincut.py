""" 
Running Karger's random contraction algorithm on a graph defined by the 
adjacency list in data/kargerMinCut.txt

Karger's min cut is a random algorithm, so need to run multiple times to achieve
certain probabilistic guarantees (i.e. n*lg(n) for 1/n failure probability, 
where n is the number of nodes)   
"""

import time
from karger import karger


def find_mincut(): 
    start = time.time()
    min_cut = 100000  # arbitrarily high
    nodes = []
    edges = []
    with open("data/kargerMinCut.txt") as f:
        for line in f:
    	    vals = line.split()
    	    node = int(vals[0]) - 1
    	    nodes.append(node)
    	    for v in vals[1:]:
    	        if node < int(v):
    	        # only add the (undirected) edge once to the list
    	            edges.append((node, int(v) - 1))
    	          
    n = len(nodes)
    trials = 100  # proper is n*log(n)
    print "Estimated processing time is ", float(trials) * .0325, " seconds..."
    for i in range(trials):
        cut = karger(nodes[:], edges[:])
        if len(cut) < min_cut:
            best_cut = cut
            min_cut = len(cut)
        
    print "Elapsed: ", time.time() - start
    print "Min cut: ", min_cut
    if min_cut < 50:
        print "Best cut: ", best_cut
    
if __name__ == "__main__":
    find_mincut()
			