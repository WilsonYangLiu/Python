#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import heapq
from threading import Thread, Lock, Condition, Event
from Queue import Queue
from time import sleep, ctime
from random import randint
from atexit import register

# Can be replaced by the Queue.task_done() used by consumer thread
_sentinel = object()
lock = Lock()

# Build my own data structure for thread communication like Queue
class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._count = 0
		self._cv = Condition()

	def put(self, item, priority):
		with self._cv:
			heapq.heappush(self._queue, (-priority, self._count, item))
			self._count += 1
			self._cv.notify()

	def get(self):
		with self._cv:
			while len(self._queue) == 0:
				print 'Currently the Queue contain nothing, waiting for put item by other thread...'
				self._cv.wait()
		
		return heapq.heappop(self._queue)[-1]

def producer(out_q, loops):
	for i in range(loops):
		with lock:
			print '[{}] producing object data for Queue...'.format(ctime()),

		evt = Event()		
		out_q.put(('xxx', evt), 1)

		with lock:		
			print 'size now: {}'.format(out_q.qsize())
		sleep(randint(2, 3))

		#evt.wait()

	with lock:
		print '[{}] producing sentinel for Queue...'.format(ctime()),

	out_q.put((_sentinel, evt))

	with lock:	
		print 'size now: {}'.format(out_q.qsize())


def consumer(in_q, loops):
	while True:
		val, evt = in_q.get(1)
		with lock:
			print '[{}] consumed object from Queue...size now: {}'.format(ctime(), in_q.qsize())

		if val is _sentinel:
			in_q.put(_sentinel)
			break
		
		sleep(randint(3, 5))

		#evt.set()
		#in_q.task_done()

funcs = [producer, consumer]
nfuncs = range(len(funcs))

def main():
	nloops = randint(3, 6)
	q = Queue()
	threads = []

	for i in nfuncs:
		t = Thread(target=funcs[i], args=(q, nloops), name=funcs[i].__name__)
		threads.append(t)

	for i in nfuncs:
		threads[i].start()

	#q.join()

@register
def _atexit():
	print 'all DONE at: {}'.format(ctime())

if __name__ == '__main__':
	main()





