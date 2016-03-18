""" 
Implementation of Kosaraju's two-pass algorithm for computing SCCs of
a directed graph.  An SCC is a strongly-connected component, which are the
equivalence classes of the relation:
     u~v => there exists a path u -> v and a path v -> u in G
Or, basically areas of the graph where you can get anywhere from anywhere.
Runs in linear time, O(m+n), where m = # of edges, n = number of nodes
"""

from directed_graph import DirectedGraph
from directed_graph import Edge

class Tracker(object):
    """ Class to maintain state of 'global' variables required by algorithm """
    def __init__(self):
        self.current_time = 0  # finishing time in first pass
        self.current_source = None  # for leader assignment in second pass
        
    def reset(self):
        self.current_time = 0
        self.current_source = None
        
def kosaraju(G):
    """ 
    Determine SCCs of graph object G 
    Returns a dictionary of SCCs from 'leader' vertex -> member vertices
    """
    t = Tracker()
    
    # First pass, calculate the topological ordering ('finish times')
    reverse_edges(G)  # flip edge directions, no copy
    dfs_loop(G, t)
    
    # Second pass to calculate components
    reverse_edges(G)  # restore edge directions
    t.reset()
    dfs_loop(G, t)
    
    return group_by_scc(G)
    
def dfs_loop(G, t):
    """ G is a graph object, t is a Tracker """
    reset_vertices_explored(G)
    n = G.num_vertices()
    for v in G.vertices_by_label():
        if not v.is_explored():
            t.current_source = v
            dfs(G, v, t)
            
def dfs(G, v, t):
    v.set_explored()
    v.set_leader(t.current_source)
    for w in G.out_vertices(v):
        if not w.is_explored():
            dfs(G, w, t)
    t.current_time += 1
    v.set_label(t.current_time)
    
def group_by_scc(G):
    """ Return dictionary from 'leader' vertex to SCC member vertices """
    scc = {}
    for v in G.vertices():
        if v.leader in scc.keys():
            scc[v.leader].append(v)
        else:
            scc[v.leader] = [v]
    return scc
    
def reset_vertices_explored(G):
    for v in G.vertices():
        v.set_unexplored()
               
def reverse_graph(G):
    """ Makes a copy of G, with each of the edges reversed (i.e. (u,v) becomes (v,u))"""
    Grev = G.copy()
    reverse_edges(Grev)
    return Grev

def reverse_edges(G):
    """ Reverses edges of directed graph G without making a copy """
    for e in G.edges():
        v,w = e
        G.remove_edge(e)
        new_edge = Edge(w,v)
        G.add_edge(new_edge)
    return G
    