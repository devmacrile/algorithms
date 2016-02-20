import random
import unittest
from dselect import dselect

class TestRselect(unittest.TestCase):

    def test_simple_median(self):
        a = [1,2,3]
        result = dselect(a, 1)
        self.assertEqual(result, 1)
        
        result = dselect(a, 3)
        self.assertEqual(result, 3)
        
    def test_get_min_value(self):
        random.seed(41)
        a = random.sample(range(1, 10), 9)
        result = dselect(a, 1)
        self.assertEqual(result, 1)
        
    def test_get_max_value(self):
        random.seed(41)
        a = random.sample(range(1, 10), 9)
        result = dselect(a, 9)
        self.assertEqual(result, 9)
        
    def test_101(self):
        random.seed(41)
        a = random.sample(range(1,102), 101)
        result = dselect(a, 51)
        self.assertEqual(result, 51)
        
    def test_long_input(self):
        random.seed(42)
        a = random.sample(range(1,10000), 1001)
        median_order_statistic = len(a)/2 + 1
        result = dselect(a, median_order_statistic)
        b = a[:]
        b.sort()
        median = b[len(b)/2]
        self.assertEqual(result, median)
        
    def test_single_input(self):
        a = [4]
        result = dselect(a, 1)
        self.assertEqual(result, 4)
        
    def test_bad_order_statistic(self):
        a = [1,2,3,4,5]
        with self.assertRaises(AssertionError):
            dselect(a,6)
            
        with self.assertRaises(AssertionError):
            dselect(a, -1)
            
    def test_bad_input_length(self):
        a = []
        with self.assertRaises(AssertionError):
            dselect(a, 1)
        
if __name__ == '__main__':
    unittest.main()