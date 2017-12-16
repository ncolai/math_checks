import scipy.stats as stats
import math
import csv
import numpy as np
import scipy.special as special
import random

def activity(arg):
    mydict = {'activity1':1, 'activity2':2}
    return mydict[arg]

def behavior(arg):
    mydict = {'less':-1, 'average':0, 'more':1}
    return mydict[arg]

#takes in a data set and returns sample mean and size of people in activity1 and activity2
def getStats(data):
    act_1 = data[data[:,1] == 1]
    act_2 = data[data[:,1] == 2]
    sample_mean = np.mean(act_1[:,2]) - np.mean(act_2[:,2])
    return len(act_1), len(act_2), sample_mean

# Helper method: Load True Distribution
# Does what you expect. Expects a header
# line.
def loadLearningOutcomes():
    fileName = 'learningOutcomes.csv'
    return np.genfromtxt(fileName, delimiter=',', dtype=int, converters={1:activity, 2:int, 3:behavior})

#p1 and p2 are the number of elements in each segment
def bootstrap(p1, p2, pop, test_mean):
    n_more_extreme = 0
    samples_to_draw = 10000
    for i in range(samples_to_draw):
        resample1 = pop[np.random.randint(len(pop), size=100)]
        resample2 = pop[np.random.randint(len(pop), size=100)]
        if abs(np.mean(resample1) - np.mean(resample2)) > abs(test_mean):
            n_more_extreme += 1
    #estimate overall stat
    return float(n_more_extreme) / samples_to_draw

if __name__ == '__main__':
    outcomes = loadLearningOutcomes()
    behaviors = [outcomes[outcomes[:,3] == i] for i in [-1,0,1]]
    behaviors.append(outcomes)
    for data in behaviors:
        p1, p2, test_mean = getStats(data)
        print(p1, p2, test_mean)
        print(bootstrap(p1, p2, data, test_mean))
