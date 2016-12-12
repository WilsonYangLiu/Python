#!/etc/bin/env python
# -*- coding: utf-8 -*-

class Node:
	def __init__(self, value):
		self._value = value
		self._children = []
	
	def __repr__(self):
		return 'Node({!r})'.format(self._value)
		
	def add_child(self, other_node):
		self._children.append(other_node)
		
	def __iter__(self):
		return iter(self._children)
	
	def depth_first(self):
		return DepthFirstIterator(self)
		
class DepthFirstIterator(object):
	''' 
	Depth-first traversal
	'''
	def __init__(self, start_node):
		self._node = start_node
		self._children_iter = None
		self._child_iter = None
	
	
	def __iter__(self):
		return self
		
	def __next__(self):
		# Return myself if just started; create an iterator for children
		if self._children_iter is None:
			self._children_iter = iter(self._node)
			return self._node
			
		elif self._child_iter:
			try:
				nextchild = next(self._child_iter)
				return nextchild
			except StopIteration:
				self._child_iter = None
				return next(self)
		
		else:
			self._child_iter = next(self._children_iter).depth_first()
			return next(self)
			
if __name__ == '__main__':
	root = Node(0)
	child11 = Node(1)
	child12 = Node(2)
	child21 = Node(3)
	root.add_child(child11)
	root.add_child(child12)
	child11.add_child(child21)
	child11.add_child(Node(4))
	child12.add_child(Node(5))
	child21.add_child(Node(6))
	
	
	for ch in root.depth_first():	# invokes __next__()
		print(ch)


