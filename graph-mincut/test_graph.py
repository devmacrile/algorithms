import unittest
from graph import Graph
from graph import Vertex
from graph import Edge

class TestGraph(unittest.TestCase):
        
    def test_add_vertex(self):
        graph = Graph()
        v = Vertex('dmr')
        graph.add_vertex(v)
        self.assertEqual(graph.num_vertices(), 1)
        
    def test_remove_vertex(self):
        graph = Graph()
        v = Vertex('dmr')
        v2 = Vertex('ees')
        graph.add_vertex(v)
        graph.add_vertex(v2)
        self.assertEqual(graph.num_vertices(), 2)
        e = Edge(v, v2)
        graph.add_edge(e)
        self.assertEqual(graph.num_edges(), 1)
        graph.remove_vertex(v)
        self.assertEqual(graph.num_vertices(), 1)
        self.assertEqual(graph.num_edges(), 0)
    
    def test_add_edge(self):
        graph = Graph()
        v1 = Vertex('dmr')
        v2 = Vertex('ees')
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_edge(Edge(v1, v2))
        self.assertEqual(graph.num_vertices(), 2)
        self.assertEqual(graph.num_edges(), 1)
        
    def test_remove_edge(self):
        graph = Graph()
        v1 = Vertex('dmr')
        v2 = Vertex('ees')
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        edge = Edge(v1, v2)
        graph.add_edge(edge)
        self.assertEqual(graph.num_edges(), 1)
        graph.remove_edge(edge)
        self.assertEqual(graph.num_edges(), 0)
        
    def test_add_all_edges(self):
        graph = Graph()
        n = 10
        for i in range(1,n+1):
            v = Vertex('v' + str(i))
            graph.add_vertex(v)
        self.assertEqual(graph.num_vertices(), n)
        graph.add_all_edges()
        self.assertEqual(graph.num_edges(), (n * (n-1))/2)
        
if __name__ == '__main__':
    unittest.main()