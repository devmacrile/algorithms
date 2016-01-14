"""
Union-find (or disjoint set) data structure implementation
http://en.wikipedia.org/wiki/Disjoint-set_data_structure
Devin Riley
March 2015
"""

class UnionFind(dict):
	def __init__(self, size):
		self.size = size
		self.group_count = size
		self.group = [i for i in range(size)]
		
	def union(self, child, parent):
		if self.group[child] == self.group[parent]:
			return
		
		self.group = [self.group[parent] if self.group[i] == self.group[child] else self.group[i] for i in range(self.size)]
		self.group_count = self.group_count - 1
		
	def find(self, e):
		return self.group[e]
		
	def get_group_count(self):
		return self.group_count
		
	def same_component(self, e1, e2):
		if self.group[e1] == self.group[e2]:
			return True
		return False
		
