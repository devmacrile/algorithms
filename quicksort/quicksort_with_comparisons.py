# Counting quicksort comparisons for different pivot values:
# First element, last element, 'median-of-three' element
# Average running time of quicksort is O(nlogn)
# which => E[C] = O(nlogn), where C is the number
# of comparisons made by the quicksort algorithm


def quicksort_with_comparisons(A, l, r, method, num_comparisons):
	# Requires A list of unique integers
	# l,r are indices indicating range of elements to sort
	# method is one of 'first', 'last', 'median-of-three'
	# Returns count of comparisons made during sort
	
	if l < r:
		pivotIndex = choose_pivot(A, l, r, method)
		if pivotIndex == -1:
			print "Invalid pivot type."
			return
		pivot = A[pivotIndex]
		A[pivotIndex], A[l] = A[l], A[pivotIndex]
		
		# partition
		i = l + 1
		for j in range(l+1, r+1):
			if A[j] < pivot:
				A[j], A[i] = A[i], A[j]
				i += 1
		A[i-1], A[l] = A[l], A[i-1]
		
		# increment comparison count, recursive calls
		num_comparisons[0] += r-l
		quicksort_with_comparisons(A, l, i - 2, method, num_comparisons)
		quicksort_with_comparisons(A, i, r, method, num_comparisons)
	
	return num_comparisons
    


def choose_pivot(A, l, r, method):
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
		
		
		
def main():
	import time
	pivots = ["first", "last", "median-of-three"]
    	
    # count comparisons for each pivot type	
	for piv in pivots:
		# build list of integers from file
		file = open('data/QuickSort.txt')
		ints = file.read().strip().split("\n")
		for i in range(len(ints)):
			ints[i] = int(ints[i])
		
		start = time.time()
		comps = [0]
		quicksort_with_comparisons(ints, 0, len(ints)-1, piv, comps) 
		elapsed = time.time() - start
		print "Pivot type: ", piv
		print comps, " comparisons made, sorted in ", elapsed, " seconds.\n"


		
if __name__ == "__main__":
	print "Running quicksort comparisons..."
	main()
		
