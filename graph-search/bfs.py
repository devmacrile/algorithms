"""
Breadth-first search (BFS) implementation
Typical use-cases are computing shortest paths, computing connected components of undirected graph
O(m+n) time utilizing a queue
"""

from collections import deque

def bfs(G, s):
    """ G is a graph object, s is the starting vertex """
    
    q = deque()
    s.set_explored()
    q.append(s)
    while len(q) > 0:
        v = q.popleft()
        neighbors = G.out_vertices(v)
        for w in neighbors:
            if not w.is_explored():
                w.set_explored()
                q.append(w)
    