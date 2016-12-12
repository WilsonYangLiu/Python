#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Python 中些控制台进度条

from __future__ import division
import sys, time

j = '#'
for i in range(9980):
	if (i+1) % 166 == 0:
		j += '#'
		sys.stdout.write(str(int(((i+1)/9980)*100))+'% ||'+j+'->'+'\r')
		sys.stdout.flush()
		time.sleep(0.5)
print

j = '#'
for i in range(1, 61):
	j += '#'
	sys.stdout.write(str(int((i/60)*100))+'% ||'+j+'->'+'\r')
	sys.stdout.flush()
	time.sleep(0.5)
print

for i in range(1, 61):
	sys.stdout.write('#'+'->'+'\b\b')
	sys.stdout.flush()
	time.sleep(0.5)
print