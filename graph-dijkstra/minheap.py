"""
Binary min-heap implementation
Conceptually a binary tree, with the invariant that for a given node n, key[n] <= [key[x]
for all x children of n].
"""

class MinHeap:
    """ 
    Array implementation of a min-heap data structure.
    Array elements are tuples of key-value pairs (key, object)
    """

    def __init__(self, objs = None):
        if objs != None:
            self.heapify(objs)
        else:
            self.heapArr = []
            self.size = 0
    
    def insert(self, k):
        """ Inserts k into heap, bubbling-up to maintain heap invariant """
        self.heapArr.append(k)
        self.size += 1
        self._bubble_up(self.size - 1)
        
    def extract(self):
        """ Extracts the root node from the heap (min value by the invariant) """
        k = self.heapArr[0]
        self.heapArr[0] = self.heapArr[self.size - 1]
        del self.heapArr[-1]
        self.size = self.size - 1
        self._bubble_down(0)  # bubble the new root down
        return k
        
    def delete(self, obj):
        """ Deletes object from heap, swapping as necessary to maintain heap invariant """
        pass
        
    def heapify(self, objs):
        """ Initializes a heap from a list of objects.
            O(n) where n is the number of objects.
        """
        pass
        
    def _bubble_up(self, i):
        while self.heapArr[i // 2][0] > self.heapArr[i][0]:
            temp = self.heapArr[i // 2]
            self.heapArr[i // 2] = self.heapArr[i]
            self.heapArr[i] = temp
            i = i // 2
           
    def _bubble_down(self, i):
        if self.size == 1:
            return
        while (2*i) < self.size:
            p = self.heapArr[i]
            c_idx = self._min_child(i)
            ch = self.heapArr[c_idx]
            if p[0] > ch[0]:
                self._swap(i, c_idx)
            i = c_idx
                       
    def _min_child(self, i):
        """ Return the child with the smaller key value.  Only called when >=1 child. """
        if (2*i + 1) >= self.size:
            return 2*i
        else:
            if self.heapArr[2*i][0] < self.heapArr[(2*i) + 1][0]:
                return 2*i
            else:
                return (2*i + 1)    
    
    def _swap(self, i, j):
        temp = self.heapArr[i]
        self.heapArr[i] = self.heapArr[j]
        self.heapArr[j] = temp
                
            
        