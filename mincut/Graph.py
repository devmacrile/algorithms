# Graph class implementation
# Devin Riley, February 2015

"""
	Implement a graph as a dictionary of dictionaries
"""

class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""
    
    def __init__(self, vs = [], es = []):
        """create a new graph. (vs) is a list of vertices; (es) list of edges"""
        for v in vs:
            self.add_vertex(v)
        
        for e in es:
            self.add_edge(e)
        
    def add_vertex(self, v):
        """add v to the graph"""
        self[v] = {}
            
    def add_edge(self, e):
        """add (e) to the graph by adding entry in both directions. 
        If already an edge connecting nodes, new edge replaces it. """
        v,w = e
        self[v][w] = e
        self[w][v] = e
    
    def get_edge(self, v1, v2):
        """returns edge between v1, v2 if there is one, otherwise returns None"""
        if v2 in self[v1]:
            return self[v1][v2]
        else:
            return None
    
    def remove_edge(self, e):
        """removes all references to edge e"""
        del self[e[0]][e[1]]
        del self[e[1]][e[0]]
        
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
        
    def add_all_edges(self):
        """makes current instance a complete graph, adding edge between each pair of nodes"""
        for node in self:  
        	# this seems like a bad way of doing this
        	# so may need more thought later
            for vertex in self:
                if node != vertex and self.get_edge(node, vertex) == None:
                    new_edge = Edge(node, vertex)  # cross dependency on Edge.. bad?
                    self.add_edge(new_edge)
    
    def clear_all_edges(self):
        """removes reference to all edges in graph, leaving vertices intact"""
        edges = self.edges()
        for edge in edges:
            self.remove_edge(edge)





class Vertex(object):
    def __init__(self, label = ''):
        self.label = label
    
    def __repr__(self):
        #returns a string representation of node
        return 'Vertex(%s)' % repr(self.label)    

    __str__ = __repr__
    
  
   
class Edge(tuple):
    def __new__(cls, v1, v2):#overriding new (python invokes 'new' then 'init')
        """tuple immutable; for immutable objects, 
        common to override __new__, as can't modify elements in __init"""
        return tuple.__new__(cls, (v1, v2))
        
    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))
        
    __str__ = __repr__