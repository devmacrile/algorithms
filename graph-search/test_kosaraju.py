import unittest
from kosaraju import kosaraju
from directed_graph import DirectedGraph
from directed_graph import Vertex
from directed_graph import Edge

class TestKosaraju(unittest.TestCase):

    def test_all_scc(self):
        G = self.create_graph_from_adj_file('data/no_scc.txt')
        scc = kosaraju(G)
        self.print_info(G, scc)
        self.assertEqual(len(scc.keys()), 4)
    
    def test_single_scc(self):
        G = self.create_graph_from_adj_file('data/single_scc.txt')
        scc = kosaraju(G)
        self.print_info(G, scc)
        self.assertEqual(len(scc.keys()), 1)
        
    def test_two_scc(self):
        G = self.create_graph_from_adj_file('data/two_scc.txt')
        scc = kosaraju(G)
        self.print_info(G, scc)
        self.assertEqual(len(scc.keys()), 2)
        
    def test_three_three_scc(self):
        G = self.create_graph_from_adj_file('data/three_scc.txt')
        scc = kosaraju(G)
        self.print_info(G, scc)
        self.assertEqual(len(scc.keys()), 3)
        
    def print_info(self, G, scc):
        print "\n"
        print "Num vertices: ", G.num_vertices(), ", Num edges: ", G.num_edges()
        print "SCCs found: ", len(scc.keys()) 
        
        
    def create_graph_from_adj_file(self, fname):
        G = DirectedGraph()
        nodes = {}
        with open(fname) as f:
            for line in f:
    	        vals = line.split()
    	        name = 'v' + str(int(vals[0]))
    	        if name not in nodes.keys():
    	            node = Vertex(name)
    	            node.set_label(int(vals[0]))
    	            nodes[name] = node
    	            G.add_vertex(node)
    	        else:
    	            node = nodes[name]
    	        for v in vals[1:]:
    	            nname = 'v' + str(v)
    	            if nname not in nodes.keys():
    	                nnode = Vertex(nname)
    	                nnode.set_label(int(v))
    	                nodes[nname] = nnode
    	                G.add_vertex(nnode)
    	                e = Edge(node, nnode)
    	                G.add_edge(e)
    	            else:
    	                nnode = nodes[nname]
    	                e = Edge(node, nnode)
    	                G.add_edge(e)
    	return G
        
        
if __name__ == '__main__':
    unittest.main()