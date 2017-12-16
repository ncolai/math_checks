import scipy.stats as stats
import math
import csv
import numpy as np
import scipy.special as special
import matplotlib.pyplot as plt
import collections

# Points on the exam add up to 118. Calculations
# should be done based on *percent* score.
MAX_POINTS = 118

# Helper method: Sterling Approximation
# approximate log(n!). Using an approximation
# is useful, but not necessary.
def sterlingApproximate(n):
    return special.gammaln(n + 1)

# Helper method: Get Problems
# Instead of loading the exam data, it
# is inlined :)
def getProblems():
    return [
        (18, 4.0),
        (24, 8.0),
        (20, 4.0),
        (22, 6.7),
        (20, 8.0),
        (14, 5.3)
    ]

# Helper method: Load True Distribution
# Does what you expect. Expects a header
# line.
def loadTrueDistribution():
    fileName = 'trueDistribution.csv'
    reader = csv.reader(open(fileName))
    header = reader.next()
    dist = {}
    for row in reader:
            minRange = int(row[0])
            p = float(row[2])
            dist[minRange] = p
    return dist

def logistic(n):
    return (1 + math.e**-n)**-1

def draw_samples(dist):
    problems = np.array(getProblems())
    student_scores = []
    for i in range(200):
        a_vals = dist.rvs(size=6)
        scores = problems[:,0] * logistic(a_vals - problems[:,1])
        student_scores.append(sum(scores))
    student_hist = np.histogram(student_scores, bins=[i*10 for i in range(11)])
    return student_hist[0]

if __name__ == '__main__':
    average = 0
    abilities = stats.norm(8, 1)
    for i in range(200):
        results = draw_samples(abilities)
        true_dist = loadTrueDistribution()
        true_dist = collections.OrderedDict(sorted(true_dist.items()))
        temp = np.append(results, [0])
        #plt.bar(true_dist.keys(), temp/float(MAX_POINTS), width = 5, color='orange')
        #plt.xlabel('Exam Scores')
        #plt.ylabel('Fraction of Students')
        #plt.show()

        #calculate maximum likelihood estimator
        logged = np.log(true_dist.values())[:-1]
        log_prob = sterlingApproximate(200) + sum(results * logged - sterlingApproximate(results))
        average += log_prob
    print(average / 100)

