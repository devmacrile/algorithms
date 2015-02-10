# QuickSort implementation

import random

def quick_sort(A, l, r):
    # requires A an array; l,r are on (0,len(A)-1) with l <= r
    # l,r are indices indicating which part of array A
    # the recursive call should work on
    # effects: sorts array A using QuickSort algorithm
    
    if l >= r:
    	print "fuck"
        return A
    
    # randomly choose pivot    
    #idx = random.randint(l, r)
    #if idx != l:
        #A[l], A[idx] = A[idx], A[l]
    p = A[l]
    
    i = l+1
    for j in range(i+1, r+1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
            
    A[l], A[i] = A[i], A[l]
        
    # recursive calls
    quick_sort(A, l, i) #lhs
    quick_sort(A, i+1, r) #rhs
    
    return A



def choose_pivot(A):
	return 1
