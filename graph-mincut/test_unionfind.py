import unittest
from unionfind import UnionFind

class TestUnionFind(unittest.TestCase):
    
    def test_initialize_unionfind(self):
        U = UnionFind(100)
        self.assertEqual(len(U.id), 100)
        
    def test_bad_initialize(self):
        e = Exception("IllegalArgumentException: make size greater than 1 to be useful")
        with self.assertRaises(Exception):
          UnionFind(1)
        with self.assertRaises(Exception):
            UnionFind(-1)
        
    def test_union(self):
        U = UnionFind(5)
        U.union(0,4)
        self.assertTrue(U.root(0) == U.root(4))
        
    def test_find(self):
        U = UnionFind(10)
        U.union(0,4)
        U.union(4,7)
        self.assertTrue(U.find(0,4))
        self.assertTrue(U.find(0,7))
        self.assertTrue(U.find(4,7))
        
    def test_root(self):
        U = UnionFind(10)
        U.union(0,4)
        self.assertTrue(U.root(4) == 0)
        self.assertTrue(U.root(0) == 0)
        self.assertTrue(U.root(1) != 0)
        
    def test_set_counter(self):
        U = UnionFind(100)
        U.union(10, 33)
        U.union(11, 22)
        U.union(12, 68)
        self.assertTrue(U.set_count() == 97)
        
        U = UnionFind(5)
        U.union(0, 3)
        U.union(0, 4)
        self.assertTrue(U.set_count() == 3)
             
if __name__ == '__main__':
    unittest.main()
