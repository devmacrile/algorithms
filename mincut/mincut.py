# Calculate mincut on data/kargerMinCut.txt graph
# Devin Riley

import random
from Graph import Graph, Vertex, Edge

G = Graph()  # instantiate graph object
fname = "data/kargerMinCut.txt"
with open(fname) as f:
    for line in f:
    	vals = line.split()
    	v = Vertex(vals[0])
    	G.add_vertex(v)
    	for j in vals[1:]:
    		v2 = Vertex(j)
    		G.add_vertex(v2)
    		e = Edge(v, v2)
    		G.add_edge(e)
    		

print random.choice(G.edges())

    		
    	
    