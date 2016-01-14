import unittest
from point import Point
from math import sqrt

class PointTest(unittest.TestCase):

    def test_distance_from_origin(self):
        point = Point(0, 1, 0)
        self.assertEquals(point.distance_from_origin(), 1)
        
        point2 = Point(1, 2, 2)
        self.assertEquals(point2.distance_from_origin(), sqrt(8))
        
        point3 = Point(2, 0, 0)
        self.assertEquals(point3.distance_from_origin(), 0)
        
    def test_distance_from_other_point(self):
        point1 = Point(0, 1, 1)
        point2 = Point(1, 1, 2)
        self.assertEquals(point1.distance_from(point2), 1)
        
        point3 = Point(2, 0, 0)
        self.assertEquals(point3.distance_from(point1), sqrt(2))
        
if __name__ == '__main__':
    unittest.main()