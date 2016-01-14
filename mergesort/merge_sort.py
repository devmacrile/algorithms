"""
Implementation of the merge-sort sorting algorithm
Devin Riley
"""

import random

def merge_sort(list):
    """Merge sort implementation
    Split list in half, sort recursively, merge results
    Upper bound: 6nlog(n) + 6n
    At each level j: 2^j subproblems of size 6*n/(2^j), const 6 coming from merge step
    2^j cancel to get 6n as an upperbound per level (of recursion tree)
    """
    
    result = []  # for storing the sorted list
    
    # Checks for base cases
    if len(list) == 1:
        return list
    if len(list) == 2:
        if(list[0] > list[1]):
            result.append(list[1])
            result.append(list[0])
            return result
        else:
            return list
    
    # Split 'list' into two halves
    lhs = []
    rhs = []
    for i in range(len(list)):
        if i < (len(list)/2):
            lhs.append(list[i])
        else:
            rhs.append(list[i])
    
    # Recursive calls on each half of original 'list'
    sorted_lhs = merge_sort(lhs)
    sorted_rhs = merge_sort(rhs)
    
    # Merge step to combine recursive calls
    result = merge(sorted_lhs, sorted_rhs)
    
    return result
    
    
 
def merge(list1, list2):
    """
    Combines two sorted lists into a single sorted list
    """
    result = []
    i = j = 0   # to iterate through lhs, rhs
    ln1 = len(list1)
    ln2 = len(list2)
    total_len = ln1 + ln2
    for k in range(total_len):
        # loop until one of lists reaches the end
        if i != ln1 and j != ln2:  # neither of the lists are finished
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            elif list1[i] > list2[j]:
                result.append(list2[j])
                j += 1
        elif (i == ln1):
            while(j < ln2):
                result.append(list2[j])
                j += 1
        elif (j == ln2):
            while(i < ln1):
                result.append(list1[i])
                i += 1
    return result
            