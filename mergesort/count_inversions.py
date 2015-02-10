# Counting inversions in an array of integers

import random

def sort_and_count(list):
    # counts inversions in the list given, where the ith row of the file indicates the ith entry of an array
    num_inversions = 0  # tracking the number of inversions
    
    if len(list) == 1:  # base case
        return 0
        
    if len(list) == 2:  # base case for recursion
        if(list[0] > list[1]):
            tmp = list[0]
            list[0] = list[1]
            list[1] = tmp
            return 1
        else:
            return 0
    
    #split list into halves
    lhs = []
    rhs = []
    for i in range(len(list)):
        if i < (len(list)/2):
            lhs.append(list[i])
        else:
            rhs.append(list[i])
    
    #recursive calls
    lhs_inv = sortAndCount(lhs)
    rhs_inv = sortAndCount(rhs)
    num_inversions += lhs_inv + rhs_inv

    #merge and count
    splts = merge_and_count(lhs, rhs, list)
    num_inversions += splts
    
    return num_inversions
    

def merge_and_count(list1, list2, biglist):
    # requires two sorted lists
    # returns sorted list
    split_inversions = 0
    i = j = 0   #to iterate through lhs, rhs
    ln1 = len(list1)
    ln2 = len(list2)
    total_len = ln1 + ln2
    for k in range(total_len):
        # loop until first end of list
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
    
    

# Test of above methods
# Read in a list of integers from a file and count number of inversions
# IntegerArray.txt
import time
start = time.time()

file = open('../data/IntegerArray.txt')
ints = file.read().split("\n")
ints.pop()
for i in range(len(ints)):
    ints[i] = int(ints[i])
inversions = sort_and_count(ints)
print inversions
# Answer: 2407905288

elapsed = time.time() - start
print "Using divide and conquer, found %s inversions in %s seconds." %(inversions, elapsed)



 







