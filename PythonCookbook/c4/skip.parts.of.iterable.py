from __future__ import print_function

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
from itertools import dropwhile, islice

os.chdir(r'F:/Github/Python/PythonCookbook/c4')
with open('somefile.txt', 'rb') as f:
	for line in dropwhile(lambda line: line.startswith('#'), f):
		print(line, end='')

print('\n', '-'*10)		

# if you happen to know the exact number of items you want to drop
with open('somefile.txt', 'rb') as f:
	for line in islice(f, 3, None):
		print(line, end='')