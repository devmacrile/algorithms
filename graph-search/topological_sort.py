""" 
Computing a topological sort of a directed graph using DFS 

A topological sort of a directed graph G is a labeling F of the nodes of G
such that: (1) the f(v)'s are the set {1,2,....,n}, and (2) (u,v) in G implies
that f(u) < f(v).
"""

from directed_graph import DirectedGraph

class TopologicalSort:
    """ Methods for creating a topological ordering of given DAG G """
    
    def __init__(self, G):
        self.G = G
        self.current_label = G.num_vertices()
        
    def run(self):
        self.dfs_loop()

    def dfs_loop(self):
        # Mark all nodes to be unexplored
        for v in self.G.vertices():
            v.set_unexplored()
        for v in self.G.vertices():
            if not v.is_explored():
                self.dfs(v)
    
    
    def dfs(self, s):
        """ s is the starting vertex """
        s.set_explored()
        for v in self.G.out_vertices(s):
            if not v.is_explored():
                self.dfs(v)
        s.set_label(self.current_label)
        self.current_label =  self.current_label - 1
    