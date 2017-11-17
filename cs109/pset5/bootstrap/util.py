import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def printRow(row):
	s = ''
	for i in range(len(row)):
		if isNumber(row[i]):
			s += '{:.0f}'.format(float(row[i]))
		else:
			s += str(row[i])
		if i != len(row) - 1:
			s += ' '
	print s

def plotHistogram(x, block = False):
	print 'plot'
	# the histogram of the data
	n, bins, patches = plt.hist(x, range(101), facecolor='green', alpha=0.75)

	# add a 'best fit' line
	
	plt.xlabel('Value')
	plt.ylabel('Count')
	plt.grid(True)
	plt.title('Data Histogram')

	plt.show(block)

def load(fileName):
	values = []
	with open(fileName) as f:
		for row in f:
			values.append(float(row))
	return values

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False