#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from atexit import register
from re import compile as rcompile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGEX = rcompile(r'#([\d,]+) in Books ')
AMZN = 'https://amazon.com/db/'
ISBNs = {
		'0132269937': 'Core Python Programming',
		'0132356139': 'Python Web Development with Django', 
		'0137143419': 'Python Fundamentals'}

def getRanking(isbn):
	page = uopen('{0}{1}'.format(AMZN, isbn))
	data = page.read()
	page.close()
	return REGEX.findall(data)[0]

def _showRanking(isbn):
	print '- {!r} ranked {}'.format(ISBNs[isbn], getRanking(isbn))

def _main():
	print 'At {} on Amazon...'
	for isbn in ISBNs:
		Thread(target=_showRanking, args=(isbn,)).start()

@register
def _atexit():
	print 'all DONE at: {}'.format(ctime())

if __name__ == '__main__':
	_main()

