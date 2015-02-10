from quicksort import *
import time

file = open('data/QuickSort.txt')
ints = file.read().strip().split("\n")
for i in range(len(ints)):
    ints[i] = int(ints[i])
 
start = time.time()
quicksort(ints, 0, len(ints)-1, "last")    
elapsed = time.time() - start

for i in range(len(ints)):
	print ints[i]
print "elapsed: ", elapsed 