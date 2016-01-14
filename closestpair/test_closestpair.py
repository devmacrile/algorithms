import unittest
import random
from point import Point
from point_collection import PointCollection
from closestpair import closestpair

def setup():
    points = PointCollection()
    for i in range(10):
        point = Point(i, 1000*random.random(), 1000*random.random())
        points.add(point)
    return points

def brute_force(points):
    min = -1
    best_pair = ()
    pts = points.get_points()
    for i in range(len(pts)):
        for j in range(len(pts)):
            if i != j:
                p = pts[i]
                q = pts[j]
                dist = p.distance_from(q)
                if dist < min or min == -1:
                    best_pair = (p,q)
                    min = dist
    return best_pair
    
def test():
    pts = setup()
    cp = closestpair(pts)
    brute = brute_force(pts)
    if cp == brute or (cp[1], cp[0]) == brute:
        print "Success! Divide and conquer matched brute force."
        print "Minimum distance is ", cp[0].distance_from(cp[1])
    else:
        print "Test failure!"
        print "D&C gave ", cp
        print "Brute force gave ", brute
        
            
if __name__ == "__main__":
    test()
    