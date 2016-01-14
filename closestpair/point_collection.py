"""
Collection representation of Points for closest pair implementation
"""

from point import Point

class PointCollection:

    def __init__(self):
        self.points = []
     
    def add(self, point):
        self.points.append(point)
        
    def remove(self, point):
        for p in self.points:
            if p == point:
                self.points.remove(point)
                
    def num_points(self):
        return len(self.points)
        
    def get_points(self):
        return self.points
        
    def get_x_values(self):
        x_vals = []
        for p in self.points:
            x_vals.append(p.x)
        return x_vals
    
    def get_y_values(self):
        y_vals = []
        for p in self.points:
            y_vals.append(p.y)
        return y_vals
    
    def sort_by_x_value(self):
        get_x = lambda p: p.x
        temp = self.points[:]
        return self.__sort_points(temp, get_x)
        
    def sort_by_y_value(self):
        get_y = lambda p: p.y
        temp = self.points[:]
        return self.__sort_points(temp, get_y)
    
    def __sort_points(self, points, func):
        """ Returns a sorted copy of self.points
            Points is an array of Point objects
            'func' is a function that accesses some member of a Point object (namely, x or y)
        """
        
        # base cases
        if len(points) == 1:
            sorted_points = points
            return sorted_points
        elif len(points) == 2:
            if func(points[0]) > func(points[1]):
                sorted_points = []
                sorted_points.append(points[1])
                sorted_points.append(points[0])
            else:
                return points
                
        # split list into approximate halves
        num_points = len(points)
        lhs = points[num_points/2:]
        rhs = points[:num_points/2]
        
        # recursively sort and merge
        sorted_lhs = self.__sort_points(lhs, func)
        sorted_rhs = self.__sort_points(rhs, func)
        sorted_points = self.__merge(sorted_lhs, sorted_rhs, func)
        
        return sorted_points
        
    def __merge(self, x, y, func):
        """ Merge two sorted arrays of point objects
            'func' is same as defined in __sort()
        """
        
        merged = []
        i = j = 0  # loop through x, y respectively
        for k in range(len(x) + len(y)):
            if i != len(x) and j != len(y):
                if func(x[i]) <= func(y[j]):
                    merged.append(x[i])
                    i += 1
                else:
                    merged.append(y[j])
                    j += 1
            elif i == len(x):
                while j < len(y):
                    merged.append(y[j])
                    j += 1
            elif j == len(y):
                while i < len(x):
                    merged.append(x[i])
                    i += 1
        return merged 
        