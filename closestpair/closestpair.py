"""
Implementation of closest-pair divide & conquer algorithm for 2D points
"""

def closestpair(points):
    """ points is a PointCollection object """
    
    # detect input return conditions
    if points.num_points() <= 1:
        print "PointCollection must have more than 1 point."
    elif points.num_points() == 2:
        print "You got 'em."

    # preprocessing step: make copies of points sorted by x, y
    px = points.sort_by_x_value()
    py = points.sort_by_y_value()
    
    return __closest_pair(px, py)
       

def __closest_pair(px, py):

    if len(px) <= 3:
        return __brute(px, py)
    
    # let q = left half of p, r = right half of p
    qx = px[:len(px)/2]
    rx = px[len(px)/2:]
    qy = px[:len(py)/2]
    ry = px[len(py)/2:]
    
    # recursive calls, and split pair (i.e. one in q one in r) check
    pair1 = __closest_pair(qx, qy)
    pair2 = __closest_pair(rx, ry)
    delta = min(pair1[0].distance_from(pair1[1]), pair2[0].distance_from(pair2[1]))
    pair3 = __closest_split_pair(px, py, delta)
    
    # take pair with minimum distance of the three
    # recall pair3 could be an empty tuple()
    if len(pair3) > 0:
        if pair3[0].distance_from(pair3[1]) < delta:
            return pair3
    else:
        if pair1[0].distance_from(pair1[1]) < pair2[0].distance_from(pair2[1]):
            return pair1
        else:
            return pair2
 
 
def __brute(px, py):
    """Requires: only called when len(px), len(py) <= 3"""
    best = -1
    best_pair = ()
    for x in px:
        for y in py:
            if x == y:
                continue
            elif x.distance_from(y) < best or best == -1:
                best = x.distance_from(y)
                best_pair = (x, y)
    return best_pair
                           
    
def __closest_split_pair(px, py, delta):
    """ 
        Points that would have distance less than delta are at most 7 points away in 'sy'
        Returns a blank tuple if no split pair is closer than delta
    """
    x_hat = px[len(px)/2].x  # largest x-coordinate in left half of p
    sy = __create_sy(py, x_hat, delta)
    best = delta
    best_pair = ()
    for i in range(len(sy) - 1):
        for j in range(min(7, len(sy) - i)):
            p = sy[i]
            q = sy[i+j]
            if p != q:
                dist = p.distance_from(q)
                if dist < best:
                    best_pair = (p, q)
                    best = dist
    return best_pair
                
def __create_sy(py, x_hat, delta):
    """sy defined as all points s.t. (x_hat +- x) <= delta"""
    sy = []
    for pt in py:
        if abs(x_hat - pt.x) < delta:
            sy.append(pt)
    return sy
    