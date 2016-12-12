from threading import Thread, Event
from time import sleep

def countDown(n, started_evt):
	print 'countDown starting'
	started_evt.set()
	while n > 0:
		print 'T-minus {}'.format(n)
		n -= 1
		sleep(2)

started_evt = Event()

print 'Launching countDown'
t = Thread(target=countDown, args=(10, started_evt))
t.start()

started_evt.wait()
print 'countDown is running'
