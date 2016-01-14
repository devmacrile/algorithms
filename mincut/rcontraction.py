""" 
Random contraction implementation for finding minimum cut of a graph
@author Devin Riley
March 2015
"""

import random
import UnionFind

def mincut(uf):
	# Takes a union-find object
	while uf.group_count > 2:
		e = random.choice(G.edges())
		v1 = e[0]
		v2 = e[1]
		v1v = G.out_vertices(v1)
		for v in G.out_vertices(v2):
			if v not in v1v and v != v1:
				G.add_edge(v1, v)
		for edge in G.out_edges(v2):
			G.remove_edge(edge)
	return G
				