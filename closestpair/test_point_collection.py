import unittest
import random
from point import Point
from point_collection import PointCollection


class PointCollectionTest(unittest.TestCase):

    def test_point_adding(self):
        points = PointCollection()
        point = Point(0, 1, 1)
        points.add(point)
        self.assertEquals(points.num_points(), 1)
        
    def test_point_removal(self):
        points = PointCollection()
        point = Point(0, 1, 1) 
        points.add(point)
        self.assertEquals(points.num_points(), 1)
        points.remove(point)
        self.assertEquals(points.num_points(), 0)
        
    def test_number_of_points_getter(self):
        points = PointCollection()
        for i in range(10):
            new_point = Point(i, random.random(), random.random())
            points.add(new_point)
        self.assertEquals(points.num_points(), 10)
        
    def test_sort_by_x_value(self):
        points = PointCollection()
        for i in range(100):
            point = Point(i, random.random(), random.random())
            points.add(point)
        sorted = points.sort_by_x_value()
        cur_x = 0
        for i in range(100):
            new_x = sorted[i].x
            self.assertTrue(new_x >= cur_x)
            cur_x = new_x
            
    def test_sort_by_y_value(self):
        points = PointCollection()
        for i in range(100):
            point = Point(i, random.random(), random.random())
            points.add(point)
        sorted = points.sort_by_y_value()
        cur_y = 0
        for i in range(100):
            new_y = sorted[i].y
            self.assertTrue(new_y >= cur_y)
            cur_y = new_y

    
if __name__ == '__main__':
    unittest.main()
    
    