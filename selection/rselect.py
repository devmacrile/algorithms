""" 
Implementation of the randomized selection algorithm
i.e. calculating the i-th order statistic
Average running time (over random pivot choices) is O(n)
"""
import random

def rselect(A, i):
    """
        A is a list of distinct integers
        i is the order statistic desired
    """
    # detect error conditions
    assert len(A) > 0
    assert i > 0
    assert i <= len(A)
    
    # base case
    if len(A) == 1:
        return A[0]
    
    # choose pivot uniformly at random and partition
    p = random.randint(0, len(A) - 1)
    j = __partition(A, p)
    
    if j == (i - 1):
        return A[j]
    elif j > (i - 1):
        return rselect(A[:j], i)
    elif j < (i - 1):
        return rselect(A[j+1:], i - (j + 1))
        
        
def __partition(A, p):
    """ 
        Modifies A to be partitioned around A[p]
        Returns new index of p
    """
    A[p], A[-1] = A[-1], A[p]  # swap pivot to be last element
    i = 0  # left 'pointer' to be first index
    j = len(A) - 2  # right 'pointer' at second to last index
    while i != j:
        while A[i] < A[-1] and i != j:
            i += 1
        while A[j] > A[-1] and j != i:
            j -= 1
        A[i], A[j] = A[j], A[i]
    if A[j] > A[-1]:
        A[j], A[-1] = A[-1], A[j]  # swap pivot to rightful position
    return j
    