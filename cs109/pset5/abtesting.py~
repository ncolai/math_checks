import scipy.stats as stats
import math
import csv
import numpy as np
import scipy.special as special

def activity(arg):
    if arg == 'activity1':
        return 1
    elif arg == 'activity2':
        return 2
    else:
        return 0

# Helper method: Load True Distribution
# Does what you expect. Expects a header
# line.
def loadLearningOutcomes():
    fileName = 'learningOutcomes.csv'
    outcomes = np.genfromtxt(fileName, delimiter=',', dtype=int, converters={1:activity})
    act_1 = outcomes[outcomes[:,1] == 1]
    act_2 = outcomes[outcomes[:,1] == 2]
    print(sum(act_1)[2]/float(len(act_1)) - sum(act_2)[2]/float(len(act_2)))
    return outcomes

if __name__ == '__main__':
    loadLearningOutcomes()
