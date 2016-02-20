from merge_sort import *
file = open('IntegerArray.txt')
ints = file.read().split("\n")
print ints
print merge_sort(ints)