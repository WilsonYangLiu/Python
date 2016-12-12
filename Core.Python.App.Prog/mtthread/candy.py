#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread, _Semaphore
from time import ctime, sleep

class _mySemaphore(_Semaphore):
	def __init__(self, value=1, verbose=None):
		_Semaphore.__init__(self, value, verbose)
		self._initial_value = value

	def __len__(self):
		return self._Semaphore__value

	def release(self):
		with self._Semaphore__cond:
			if self._Semaphore__value >= self._initial_value:
				raise ValueError("Semaphore released too many times")
			self._Semaphore__value += 1
			self._Semaphore__cond.notify()

def mySemaphore(*args, **kwargs):
    return _mySemaphore(*args, **kwargs)

lock = Lock()
MAX = 5
candytray = mySemaphore(MAX)

def refill():
	with lock:
		print 'Refilling candy...',
		try:
			candytray.release()
		except ValueError:
			print 'full, skipping'
		else:
			print 'OK, {}'.format(len(candytray))

def buy():
	with lock:
		print 'Buying candy...',
		if candytray.acquire(False):
			print 'OK, {}'.format(len(candytray))
		else:
			print 'empty, skipping'

def producer(loops):
	for i in xrange(loops):
		refill()
		sleep(randrange(3))

def consumer(loops):
	for i in xrange(loops):
		buy()
		sleep(randrange(3))

def _main():
	print 'starting at: {}'.format(ctime())
	nloops = randrange(2, 6)
	print 'THE CANDY MECHINE (full with {} bars)!'.format(MAX)
	Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2), )).start()
	Thread(target=producer, args=(nloops, )).start()

@register
def _atexit():
	print 'all DONE at: {}'.format(ctime())

if __name__ == '__main__':
	_main()


