""" 
Counting inversions in an array of distinct integers
"""

import time
import random


def sort_and_count(list):
	"""
	Counts inversions in list (an array of distinct integers)
	ith row of the file indicates the ith entry of an array	
	"""
	
	num_inversions = 0
    
	# Checks for base case conditions
	if len(list) == 1:
		return 0
	if len(list) == 2:
		if(list[0] > list[1]):
			tmp = list[0]
			list[0] = list[1]
			list[1] = tmp
			return 1
		else:
			return 0
    
	# Split list into two halves
	lhs = []
	rhs = []
	for i in range(len(list)):
		if i < (len(list)/2):
			lhs.append(list[i])
		else:
			rhs.append(list[i])
			
	# Recursive calls on each half of original list
	lhs_inv = sort_and_count(lhs)
	rhs_inv = sort_and_count(rhs)
	num_inversions += lhs_inv + rhs_inv
	
	# Merge, and add inversions counted in merge step
	splits = merge_and_count(lhs, rhs, list)
	num_inversions += splits
    
	return num_inversions
    

def merge_and_count(list1, list2, biglist):
	"""
	Merge two sorted lists, count cross-inversions between them
	list1, list2 are two sorted lists
	biglist is modified to contain the sorted combination of list1, list2
	"""
	split_inversions = 0
	i = j = 0   # Counters for looping over list1, list2 respectively
	ln1 = len(list1)
	ln2 = len(list2)
	total_len = ln1 + ln2
	for k in range(total_len):
		# Loop until first end of list
		if i != ln1 and j != ln2:  # neither of the lists are finished
			if list1[i] <= list2[j]:
				biglist[k] = list1[i]
				i += 1
			elif list1[i] > list2[j]:
				biglist[k] = list2[j]
				split_inversions += ln1 - i
				j += 1
		elif (i == ln1 and j < ln2):
			biglist[k] = list2[j]
			j += 1
		elif (j == ln2 and i < ln1):
			biglist[k] = list1[i]
			i += 1
	return split_inversions
    
    

if __name__ == "__main__":
	"""
	Run above methods on IntegerArray.txt file (assumed to be in same directory)
	"""
	start = time.time()
	
	file = open('IntegerArray.txt')
	ints = file.read().split("\n")
	ints.pop()
	for i in range(len(ints)):
		ints[i] = int(ints[i])
	inversions = sort_and_count(ints)
	print inversions
	# Answer: 2407905288
	
	elapsed = time.time() - start
	print "Using divide and conquer, found %s inversions in %s seconds." %(inversions, elapsed)
	