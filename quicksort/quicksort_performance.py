# Script to count QuickSort comparisons for varying input lengths
# Devin Riley

import time
import csv
from quicksort_with_comparisons import *

sizes = [10000*x for x in range(1, 100 + 1)]
results = {}  # Store quick sort comparison counts for each array size

start = time.time()
for i in sizes:

	if i/10000 % 10 == 0:
		print "progress: ", i
	
	fname = "data/QuickSort-" + str(i) + ".txt"
	pivots = ["first", "last", "median-of-three"]
	counts = []
    
    # count comparisons for each pivot type	
	for piv in pivots:
		# build list of integers from file
		file = open(fname)
		ints = file.read().strip().split("\n")
		for j in range(len(ints)):
			ints[j] = int(ints[j])
		
		comps = [0]
		quicksort_with_comparisons(ints, 0, len(ints)-1, piv, comps)
		counts.append(comps[0])
	results[str(i)] = counts
	
		
elapsed = time.time() - start
print "Finished in ", elapsed, "seconds."

# Write results to file
w = csv.writer(open("data/results.csv", "w"))
for key, val in results.items():
    w.writerow([str(key), ','.join(map(repr, results[key]))])
    