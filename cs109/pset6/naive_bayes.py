import numpy as np
import math
import re

# Helper method: Load Data
# Does what you expect. Expects a header
# line.
def loadData(filenames):
    datasets = []
    for name in filenames:
        temp = open(name, 'r')
        input_file = [line for line in temp]
        features, points = map(int, input_file[:2])
        data = [map(int, re.split(': | ', line)) for line in input_file[2:]]
        datasets.append(np.array(data))
        temp.close()
    return datasets + [features + 1]

#a_i = P(X_i = 0|Y = y)
#b_i = P(X_i = 1|Y = y)
#weights returned is counts rather than probabilities
def trainData(data, n_features):
    [output, priors, n1, n2] = [[], [], 0,0]
    priors = map(float, [len(data[data[:,-1] == 0]),len(data[data[:,-1] == 1])])
    for y in [0,1]:
        weights = []
        sample_y = data[data[:,-1] == y, :]
        for feature in range(n_features - 1):
            match0 = sample_y[sample_y[:,feature] == 0, :]
            match1 = sample_y[sample_y[:,feature] == 1, :]
            weights.append([float(len(match0)), float(len(match1))])
        output.append(np.array(weights))
    return np.array(output), np.array(priors)

#p, priors, represent our prior knowledge of Y = 0 and Y = 1.
#weights converted to cond probs using priors
def testData(weights, p, data, n_features, isLaplace):
    correct = [0,0]
    found = [0,0]
    [num, denom] = [0,0] #used for adjusting with Laplace MAP
    if isLaplace:
        [num, denom] = [1,2]
    for d,line in enumerate(data):
        counts = [1.0,1.0]
        for i in range(n_features - 1):
            counts[0] += np.log(float(num + weights[0,i,line[i]])/float(denom + p[0]) )
            counts[1] += np.log(float(num + weights[1,i,line[i]])/float(denom + p[1]) ) 
        counts[0] += np.log(p[0])
        counts[1] += np.log(p[1])

        #found[line[-1]] += 1
        if counts[0] > counts[1] and line[-1] == 0:
            correct[0] += 1
        if counts[0] < counts[1] and line[-1] == 1:
            correct[1] += 1
    found = [np.sum(data[:,-1] == 0), np.sum(data[:,-1] == 1)]

    for c in [0,1]:
        print('Class {}: tested {}, correctly classified {}'.format \
                (c, found[c],correct[c]))
    print('Overall: tested {}, correctly classified {}'.format(sum(found),sum(correct)))
    print('Accuracy = {}%'.format(100*sum(correct)/float(sum(found))))

def print_weights(weights, priors, y):
    for ind, w in enumerate(weights[y]):
        print('P($X_{%d}$ = 1 \\textbar Y = %d) & %f & %f\\\\' % \
        (ind + 1, y, float(w[1])/priors[y], float(w[1] + 1)/(priors[y] + 2)))

def weight_ratios(weights):
    print((weights[1, :, 1]) * 1.0 / weights[0,:,1])

def run_naive_bayes(dataset_name, training_set, test_set):
    print('\n' + dataset_name + '\n')
    train, test, n_features = loadData([training_set, test_set])
    for laplace_setting in [False, True]:
        weights, priors = trainData(train, n_features)
        testData(weights, priors, test, n_features, laplace_setting)
        if dataset_name == 'netflix dataset':
            print_weights(weights, priors, 1)
            print(priors)
            weight_ratios(weights)

#the main routine
if __name__ == '__main__':
    run_naive_bayes('simple dataset', 'datasets/simple-train.txt', 'datasets/simple-test.txt')
    run_naive_bayes('netflix dataset', 'datasets/netflix-train.txt', 'datasets/netflix-test.txt')
    run_naive_bayes('ancestry dataset', 'datasets/ancestry-train.txt', 'datasets/ancestry-test.txt')
    run_naive_bayes('heart dataset', 'datasets/heart-train.txt', 'datasets/heart-test.txt')

