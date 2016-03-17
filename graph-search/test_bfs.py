import unittest
import random
from bfs import bfs
from graph import Graph
from graph import Vertex
from graph import Edge
from test_helper import *

class TestBFS(unittest.TestCase):
    
    def test_two_node(self):
        G = Graph()
        v1 = Vertex('v1')
        v2 = Vertex('v2')
        v3 = Vertex('v3')
        e = Edge(v1, v2)
        G.add_vertex(v1)
        G.add_vertex(v2)
        G.add_vertex(v3)
        G.add_edge(e)
        bfs(G, v1)
        self.assertTrue(v2.is_explored())
        self.assertTrue(v3.is_explored() == False)
        self.assertEqual(G.num_explored_vertices(), 2)
        
    def test_random_graph(self):
        G = create_random_graph(100)
        self.assertEqual(G.num_vertices(), 100)
        
    def test_complete_graph(self):
        n = 25
        G = create_complete_graph(n)
        s = random.choice(G.vertices())
        bfs(G, s)
        self.assertEqual(G.num_explored_vertices(), n)
        
    def test_unconnected_graph(self):
        G = create_unconnected_graph(100)
        s = random.choice(G.vertices())
        bfs(G, s)
        self.assertTrue(G.num_explored_vertices() == 1)
        
    def test_two_component_graph(self):
        n = 100
        v1 = Vertex('Dirk')
        v2 = Vertex('Nowitzki')
        G = create_two_component_graph(n, v1, v2)
        bfs(G, v1)
        self.assertTrue(v2.is_explored() == False)
        self.assertTrue(G.num_explored_vertices >= 50)
        
if __name__ == '__main__':
    unittest.main()
        