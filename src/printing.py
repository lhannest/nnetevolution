import sys
import time

class printer(object):
	def __init__(self, wait_time):
		self.wait_time = wait_time
		self.t = time.time()
	def reprint(self, message):
		if time.time() - self.t >= self.wait_time:
			sys.stdout.write('\r')
			sys.stdout.flush()
			sys.stdout.write(message)
			sys.stdout.flush()
			self.t = time.time()
	def clear(self):
		sys.stdout.write('\r')
		sys.stdout.flush()
		sys.stdout.write('                                                             ')
		sys.stdout.flush()
		sys.stdout.write('\r')
		sys.stdout.flush()