#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Iterate in reverse/forword over a sequence

class Countdown:
	def __init__(self, start):
		self._start = start
		
	# Forward iteration
	def __iter__(self):
		n = self._start
		while n > 0:
			yield n
			n -= 1
	
	# Reverse iteration
	def __reversed__(self):
		n = 1
		while n <= self._start:
			yield n
			n += 1
			
if __name__ == '__main__':
	cd = Countdown(10)
	for item in cd:
		print item

