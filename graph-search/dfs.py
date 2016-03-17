"""
Depth-first search (DFS) implementation
Common use cases: Compute topological ordering of a directed, acyclic graph; compute 
connected components in directed graphs
O(m+n) time utilizing a stack
"""

def dfs(G, s):
    """ G is a graph object, s is the starting vertex """
    
    l = []  # using a generic list as a stack
    s.set_explored()
    l.append(s)
    while len(l) > 0:
        v = l.pop()
        edges = G.out_edges(v)
        for e in edges:
            w = e[1]
            if not w.is_explored():
                dfs(G, w)