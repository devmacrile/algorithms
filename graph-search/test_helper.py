""" Helper functions for test creation """
import random
from graph import Graph
from graph import Vertex
from graph import Edge

def create_random_graph(num_nodes):
    vs = create_vertices(num_nodes)   
    es = []
    num_edges = random.randint(1, num_nodes * num_nodes)
    for j in range(num_edges):
        v1 = random.choice(vs)
        v2 = random.choice(vs)
        if v1 != v2:
            e = Edge(v1, v2)
            es.append(e)
    G = Graph(vs, es)
    return G
    
    
def create_complete_graph(num_nodes):
    G = Graph()
    vs = create_vertices(num_nodes)
    for v in vs:
        G.add_vertex(v)
    for v in vs:
        for v2 in vs:
            if v != v2:
                e = Edge(v, v2)
                G.add_edge(e)
    return G

def create_unconnected_graph(num_nodes):
    G = Graph()
    vs = create_vertices(num_nodes)
    for v in vs:
        G.add_vertex(v)
    return G
    
def create_two_component_graph(num_nodes, v1, v2):
    """ Returns a multi-component graph s.t. there does not exist a path from v1 to v2 """
    G = Graph()
    vs = create_vertices(num_nodes)
    for v in vs:
        G.add_vertex(v)
    G.add_vertex(v1)
    G.add_vertex(v2)
    split_idx = len(vs)/2
    for v in vs[:split_idx]:
        G.add_edge(Edge(v1, v))
    for v in vs[split_idx:]:
        G.add_edge(Edge(v2, v))
    return G
    
    
def create_vertices(n):
    vs = []
    for i in range(n):
        v = Vertex(i)
        vs.append(v)
    return vs

    