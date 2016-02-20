from graph import Graph
from graph import Vertex
from graph import Edge
from rcontraction import rcontraction

def test_rcontraction():
    g = Graph()
    for i in range(10):
        v = Vertex(i)
        g.add_vertex(v)
    g.add_all_edges()
    g2 = rcontraction(g)
    
if __name__ == '__main__':
    test_rcontraction()