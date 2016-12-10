import sys
import numpy

def main():
	script = sys.argv[0]
	action = sys.argv[1]
	filenames = sys.argv[2:]
	
	for f in filenames:
		data = numpy.loadtxt(f, delimiter=',')
		
		if action == '--min':
			values = numpy.min(data, axis=1)
		elif action == '--mean':
			values = numpy.mean(data, axis=1)
		elif action == '--max':
			values = numpy.max(data, axis=1)
		
		for m in values:
			print(m)

if __name__ == '__main__':
	main()
