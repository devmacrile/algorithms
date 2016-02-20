"""
Implementation of a union-find (or disjoint set) data structure
http://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""
	
class UnionFind:
    def __init__(self, n):
        self.size = n
        if self.size <= 1:
            raise Exception("IllegalArgumentException: make size greater than 1 to be useful")
        self.id = range(n)
        self.size = [1] * n
        self.num_sets = n
        
    def root(self, p):
        """
        Return the root set of element p
        """
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]] # Path compression to limit tree depth
            p = self.id[p]
        return p
            
    def find(self, p, q):
        """
        Determine if two elements belong to the same set
        """
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        """
        Join sets p,q together
        """
        i = self.root(p)
        j = self.root(q)
        if self.size[p] < self.size[q]:
            self.id[i] = j
            self.size[i] += self.size[j]
        else:
            self.id[j] = i
            self.size[j] += self.size[i]
            
        # Decrement set count
        self.num_sets = self.num_sets - 1
        
    def set_count(self):
        """
        Return the number of unique root values
        """
        return self.num_sets
            