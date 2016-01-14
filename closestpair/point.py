"""
Class for two-dimensional for testing closest-pair implementation
"""

class Point:
    """ Class to represent x,y values of a two dimensional point"""
    
    def __init__(self, id, x = 0, y = 0):
        """ Create a new point at x,y """
        self.id = id
        self.x = x
        self.y = y
        
    def distance_from_origin(self):
        """ Compute Euclidean distance between this point and (0,0) """
        return ((self.x ** 2) + (self.y ** 2)) ** .5
        
    def distance_from(self, point2):
        """ Compute Euclidean distance between this point and 'point2' """
        return (((self.x - point2.x) ** 2) + ((self.y - point2.y) ** 2)) ** .5
                
    def __str__(self):
        return "Point(id={0}, {1}, {2})".format(self.id, self.x, self.y)

        