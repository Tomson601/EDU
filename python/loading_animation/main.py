import sys
import time


for i in range(98):
	sys.stdout.write('=')
	sys.stdout.flush()
	time.sleep(0.01)

sys.stdout.write('>')
sys.stdout.flush()
print('\nDone!')
