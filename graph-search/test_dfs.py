import unittest
from dfs import dfs
from graph import Graph
from graph import Vertex
from graph import Edge

class TestDFS(unittest.TestCase):
    
    def test_three_node_one_edge(self):
        G = Graph()
        v1 = Vertex('v1')
        v2 = Vertex('v2')
        v3 = Vertex('v3')
        e = Edge(v1, v2)
        G.add_vertex(v1)
        G.add_vertex(v2)
        G.add_vertex(v3)
        G.add_edge(e)
        dfs(G, v1)
        # TODO
        
if __name__ == '__main__':
    unittest.main()