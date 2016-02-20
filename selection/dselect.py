""" 
Implementation of the deterministic selection algorithm
i.e. calculating the i-th order statistic
No randomization, but runs O(n)

General algorithm is as follows:
    Break input array A into groups of 5
    Sort each group of 5 (method really does not matter)
    Let C be the n/5 "middle" elements of these groups
    Recursively call dselect on C with order statistic being n/10, call this p
    Partition input array A around p
    Recursively call dselect on the appropriate portion of A
"""

def dselect(A, i):
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
    
    # create n/5 groups from A, sort, and place middle elements in C
    C = []
    n = len(A)
    if n > 5:
        for g in range(n/5):
            a = A[5*g:min(5*(g+1),n)]
            a.sort()  # sorting method irrelevant for length 5
            C.append(a[len(a)/2 + 1])
    else:
        a = A[:]
        a.sort()
        C.append(a[n/2])
    
    # calculate median of C, partition A around this median
    p = dselect(C, n/10 + 1)
    j = __partition(A, p)
    
    # recursive calls
    if j == (i - 1):
        return A[j]
    elif j > (i - 1):
        return dselect(A[:j], i)
    elif j < (i - 1):
        return dselect(A[j+1:], i - (j + 1))
 
 
    
def __partition(A, p):
    """ 
        Modifies A to be partitioned around A[p]
        Returns new index of p
    """
    # TODO: fix this little nugget
    for k in range(len(A)):
        if A[k] == p:
            pidx = k
    
    A[pidx], A[-1] = A[-1], A[pidx]  # swap pivot to be last element
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
        
       