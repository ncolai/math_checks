import population
import numpy as np
import random
import util
import math
import matplotlib.pyplot as plt

NPOP = 10000
NSAMPLE = 15

def main():
	print '\nTesting Sample Variance\n'

	# Get a random population
	pop = population.makeModalPopulation(NPOP)
	util.plotHistogram(means)
	
	means = []
	for i in range(10000):
		subsample = random.sample(pop, NSAMPLE)
		mean = np.mean(subsample)
		means.append(mean)

	util.plotHistogram(means)

	

# This is the definition of the variance of an
# entire population.
def calcSampleVariance(data):
	sampleMean = np.mean(data)
	n = len(data)
	total = 0
	for i in range(n):
		d = data[i]
		total += math.pow(d - sampleMean, 2)
	return float(total)/ (n-1)

# This is the definition of the variance of an
# entire population.
def calcVariance(data):
	sampleMean = np.mean(data)
	n = len(data)
	total = 0
	for i in range(n):
		d = data[i]
		total += math.pow(d - sampleMean, 2)
	return float(total)/ (n)

def printRow(row):
	util.printRow(row)

if __name__ == '__main__':
	main()
	plt.show()