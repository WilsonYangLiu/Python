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
		
	def breadth_first(self):
		return BreadthFirstIterator(self)
		
class DepthFirstIterator(object):
	''' 
	Depth-first traversal
	'''
	def __init__(self, start_node):
		self._node = start_node
		self._children_iter = None
		self._child_iter = None
		
	def __repr__(self):
		self._children = []
		while True:
			try:
				self._children.append(self._dfs())
			except StopIteration:
				break
		return '{!r}'.format(self._children)
		
	def _dfs(self):
		# Return myself if just started; create an iterator for children
		if self._children_iter is None:
			self._children_iter = iter(self._node)
			return self._node
			
		# If processing a child, return its next item
		elif self._child_iter:
			try:
				nextchild = self._child_iter._dfs()
				return nextchild
			except StopIteration:
				self._child_iter = None
				return self._dfs()
		
		# Advance to the next child and start its iteration
		else:
			self._child_iter = next(self._children_iter).depth_first()
			return self._dfs()
			
class BreadthFirstIterator(object):
	'''
	Depth-first traversal
	'''
	def __init__(self, start_node):
		self._queue = [start_node]
		self._order = [start_node]
		self._children_iter = None
		
	def __repr__(self):
		return '{!r}'.format(self._bfs())
		
	def _bfs(self):
		while len(self._queue) > 0:
			self._children_iter = iter(self._queue.pop(0))
			for child in self._children_iter:
				self._queue.append(child)
				self._order.append(child)
				
		return self._order
			
if __name__ == '__main__':
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)
	root.add_child(child1)
	root.add_child(child2)
	child1.add_child(Node(3))
	child1.add_child(Node(4))
	child2.add_child(Node(5))
	
	print root.depth_first()
	print root.breadth_first()
