"""
Brute force inversion counter
Used for comparison of efficiency and correctness with merge-sort implementation
"""

def count_inversions(list):
    num_inversions = 0
    for i in range(len(list)-1):
        for j in range(i+i, len(list)):
            if list[i] > list[j]:
                num_inversions += 1
    return num_inversions
    
import time 
start = time.time()

file = open('IntegerArray.txt')
ints = file.read().split("\n")
inversions = count_inversions(ints)
print inversions

elapsed = time.time() - start
print "The brute force inversion count took %s seconds." %(elapsed)
            
		