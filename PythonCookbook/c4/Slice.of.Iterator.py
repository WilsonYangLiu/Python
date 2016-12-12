from __future__ import print_function

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
from itertools import islice

def myCount(n):
	while True:
		yield n
		n += 1
		
os.chdir(r'F:/Github/Python/PythonCookbook/c4')
c = myCount(0)
for x in islice(c, 10, 20):
	print(x)
	
# islice() will consume data on the supplied iterater
next(c)
