import unittest
import random
from topological_sort import TopologicalSort
from directed_graph import DirectedGraph
from directed_graph import Vertex
from directed_graph import Edge

class TestTopologicalSort(unittest.TestCase):
    
    def test_diamond(self):
        G = DirectedGraph()
        v1 = Vertex('v1')
        v2 = Vertex('v2')
        v3 = Vertex('v3')
        v4 = Vertex('v4')
        e12 = Edge(v1, v2)
        e13 = Edge(v1, v3)
        e24 = Edge(v2, v4)
        e34 = Edge(v3, v4)
        G.add_vertex(v1)
        G.add_vertex(v2)
        G.add_vertex(v3)
        G.add_vertex(v4)
        G.add_edge(e12)
        G.add_edge(e13)
        G.add_edge(e24)
        G.add_edge(e34)
        T = TopologicalSort(G)
        T.run()
        self.assertTrue(v1.label <  v2.label)
        self.assertTrue(v1.label < v3.label)
        self.assertTrue(v2.label < v4.label)
        self.assertTrue(v3.label < v4.label)
        
    def test_random_acyclic_graph(self):
        n = 10
        G = DirectedGraph()
        for i in range(n):
            v = Vertex(i)
            G.add_vertex(v)
        for v in G.vertices():
            for j in range(n/2):
                v2 = random.choice(G.vertices())
                if int(v.name) < int(v2.name):
                    e = Edge(v, v2)
                    G.add_edge(e)
        T = TopologicalSort(G)
        T.run()
        # TODO: Confirm results
            
        
if __name__ == '__main__':
    unittest.main()