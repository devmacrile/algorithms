"""
Implementation of the QuickSort sorting algorithm
"""

import random

def quicksort(A, l, r, method):
    """
    Requires A an array; l,r are on (0,len(A)-1) with l <= r
    l,r are indices indicating which part of array A on which the recursive call should work
    Effects: sorts array A using QuickSort algorithm
    """
    if l < r:
		pivotIndex = choose_pivot(A, l, r, method)
		if pivotIndex == -1:
			print "Invalid pivot type."
			return
		pivot = A[pivotIndex]
		A[pivotIndex], A[l] = A[l], A[pivotIndex]
		i = l + 1
		for j in range(l+1, r+1):
			if A[j] < pivot:
				A[j], A[i] = A[i], A[j]
				i += 1
		A[i-1], A[l] = A[l], A[i-1]
		quicksort(A, l, i - 2, method)
		quicksort(A, i, r, method)

    return A
	

def choose_pivot(A, l, r, method):
    """
    Method to choose pivot type at run type based on parameter 'method'
    """
	if method == "first":
		return l
	elif method == "last":
		return r
	elif method == "median-of-three":
		mid = (r + l)/2
		vals = [A[l], A[mid], A[r]]
		mn = min(vals)
		mx = max(vals)
		for i in [l, mid, r]:
			if A[i] != mn and A[i] != mx:
				return i
		return mid  # this covers the case where r-l == 1
	else:
		return -1
		
