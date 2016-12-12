from __future__ import print_function

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
from collections import deque

class lineHistory:
	def __init__(self, lines, histlen=3):
		self.lines = lines
		self.history = deque(maxlen=histlen)
		
	def __iter__(self):
		for lineNo, line in enumerate(self.lines, 1):
			self.history.append((lineNo, line) )
			yield line
			
	def clear(self):
		self.history.clear()
		
if __name__ == '__main__':
	os.chdir(r'F:/Github/Python/PythonCookbook/c4')
	with open('somefile.txt', 'rb') as f:
		lines = lineHistory(f)
		for line in lines:
			if 'python' in line:
				for lineNo, hline in lines.history:
					print('{}:{}'.format(lineNo, hline), end='')