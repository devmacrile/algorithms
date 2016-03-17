""" 
Simple directed graph implementation 
TODO: Inheritance with original Graph class
"""

import random

class DirectedGraph(dict):
    
    def __init__(self, vs = [], es = []):
        """create a new graph. (vs) is a list of vertices; (es) list of edges"""
        for v in vs:
            self.add_vertex(v)
        
        for e in es:
            self.add_edge(e)
            
    def num_vertices(self):
        return len(self)
        
    def num_edges(self):
        es = 0
        for v in self:
            es += len(self[v])
        return es
        
    def add_vertex(self, v):
        self[v] = {}
            
    def add_edge(self, e):
        """add (e) to the graph by adding entry in both directions. 
        If already an edge connecting nodes, new edge replaces it. """
        v,w = e
        self[v][w] = e
    
    def get_edge(self, v1, v2):
        """returns edge between v1, v2 if there is one, otherwise returns None"""
        if v2 in self[v1]:
            return self[v1][v2]
        else:
            return None
    
    def remove_vertex(self, v):
        """ removes vertex v from graph"""
        out_edges = self.out_edges(v)
        for e in out_edges:
            self.remove_edge(e)
        del self[v]
    
    def remove_edge(self, e):
        """removes all references to edge e"""
        del self[e[0]][e[1]]
        
    def vertices(self):
        """returns nodes of graph"""
        nodes = []
        for vertex in self:
            nodes.append(vertex)
        return nodes
        
    def edges(self):
        """returns list of edges of graph"""
        edges = []
        nodes = self.vertices()
        for vertex in self:
            if len(self[vertex]) > 0:
                for node in nodes:
                    e = self.get_edge(vertex, node)
                    if e != None and e not in edges:
                        edges.append(e)
        return edges
        
    def out_vertices(self, v):
        """returns list of vertices to which v is connected"""
        neighbors = []
        for node in self[v]:
            if self.get_edge(v, node) != None:
                neighbors.append(node)
        return neighbors
        
    def out_edges(self, v):
        """returns list of edges to which v is connected"""
        edges = []
        for node in self[v]:
            e = self.get_edge(v, node)
            if e != None:
                edges.append(e)
        return(edges)
    
    def clear_all_edges(self):
        """removes reference to all edges in graph, leaving vertices intact"""
        edges = self.edges()
        for edge in edges:
            self.remove_edge(edge)
    
    def num_explored_vertices(self):
        count = 0
        for node in self:
            if node.is_explored():
                count += 1
        return count
        
class Vertex(object):
    def __init__(self, name = ''):
        self.name = name
        self.explored = False
        self.label = -1
        
    def is_explored(self):
        return self.explored
        
    def set_explored(self):
        self.explored = True
    
    def set_unexplored(self):
        self.explored = False
    
    def set_label(self, i):
        self.label = i
    
    def __repr__(self):
        return 'Vertex(%s, %s, %s)' % (repr(self.name), self.explored, self.label)    

    __str__ = __repr__
    
  
   
class Edge(tuple):
    def __new__(cls, v1, v2):  # overriding new (python invokes 'new' then 'init')
        """tuple immutable; for immutable objects, 
        common to override __new__, as can't modify elements in __init"""
        return tuple.__new__(cls, (v1, v2))
        
    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))
        
    __str__ = __repr__