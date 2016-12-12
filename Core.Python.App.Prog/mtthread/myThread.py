#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import threading
from time import ctime, sleep
from atexit import register

class ThreadFunc(object):
	def __init__(self, func, args, name=''):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):
		self.func(*self.args)

class MyThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args

	def getResult(self):
		return self.res

	def run(self):
		print 'starting {} at: {}'.format(self.name, ctime())
		self.res = self.func(*self.args)
		print '{} finished at: {}'.format(self.name, ctime())

def loop(nsec):
	# print 'This is {}'.format(nloop)
	sleep(nsec)

def main():
	print 'starting at: {}'.format(ctime())
	loops = [4, 2]
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		threads.append(MyThread(loop, (loops[i],), ' '.join((loop.__name__, str(i)))))

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()

@register
def _atexit():
	print 'all DONE at: {}'.format(ctime())

if __name__ == '__main__':
	main()



