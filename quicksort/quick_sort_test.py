from quick_sort import *
import time

file = open('simple.txt')
ints = file.read().strip().split("\n")
for i in range(len(ints)):
    ints[i] = int(ints[i])

print ints  
start = time.time()
#quick_sort(ints, 0, len(ints)-1)    
elapsed = time.time() - start


for i in range(len(ints)):
	print ints[i]
print "elapsed: ", elapsed 