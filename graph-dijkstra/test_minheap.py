import unittest
import random
from minheap import MinHeap

class TestMinHeap(unittest.TestCase):
    
    def test_insert(self):
        h = MinHeap()
        h.insert((3.76, 1))
        h.insert((1.2, 2))
        h.insert((1.7, 3))
        h.insert((2.3, 4))
        h.insert((9.3, 5))
        self.assertTrue(h.size == 5)
        print h.extract()
        print h.extract()
        print h.extract()
        print h.extract()
        print h.extract()
        
        
if __name__ == '__main__':
    unittest.main()