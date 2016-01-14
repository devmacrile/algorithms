"""
Testing union-find data-structure
Devin Riley
March 2015
"""

from UnionFind import UnionFind

def union_test():
	uf = UnionFind(10)
	uf.union(3,4)
	assert uf.same_component(3,4)
	print "Passed 'union' test..."
	
def group_size_test():
	uf = UnionFind(10)
	uf.union(3,4)
	assert uf.group_count == (uf.size - 1)
	print "Passed group size test..."
	
def find_test():
	uf = UnionFind(10)
	assert uf.find(uf.group[3]) == uf.group[3]
	uf.union(3,4)
	assert uf.find(uf.group[3]) == uf.group[4]
	print "Passed 'find' test..."
	
def multi_union_test():
	uf = UnionFind(10)
	uf.union(3, 4)
	uf.union(7, 3)
	uf.union(1, 2)
	uf.union(7, 1)
	assert uf.group_count == 6
	print "Passed multi union test..."	
	
	
if __name__ == '__main__':
	union_test()
	group_size_test()
	find_test()
	multi_union_test()