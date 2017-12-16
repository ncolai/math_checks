import numpy as np
import math
import re

#calculates the sigmoid value of a number
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

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
        datasets.append(np.hstack(( np.ones((points,1)), data)) )
        temp.close()
    return datasets + [features + 1]

#train data using gradient descent
def trainData(data, n_features, rate):
    thetas = np.zeros(n_features)
    for step in range(3000):
        new_thetas = [0.0 for i in range(n_features)]
        diffs = [0.0 for line in data]
        diffs = data[:,-1] - \
                sigmoid(np.sum(np.multiply(data[:,:-1], thetas), axis =1))
        for j in range(n_features):
            new_thetas[j] = thetas[j] + rate * np.dot(diffs, data[:,j])
        thetas = new_thetas
    return thetas

#test data by comparing against actual input
def testData(thetas, data):
    correct = [0,0]
    for line in data:
        logistic_0 = 1 - sigmoid(np.dot(thetas, line[:-1]))
        logistic_1 = sigmoid(np.dot(thetas, line[:-1]))
        if logistic_0 > logistic_1 and line[-1] == 0:
            correct[0] += 1
        elif logistic_0 < logistic_1 and line[-1] == 1:
            correct[1] += 1
    found = [np.sum(data[:,-1] == 0), np.sum(data[:,-1] == 1)]

    for c in [0,1]:
        print('Class {}: tested {}, correctly classified {}'.format \
                (c, found[c],correct[c]))
    print('Overall: tested {}, correctly classified {}'.format(sum(found),sum(correct)))
    print('Accuracy = {}%'.format(100*sum(correct)/float(sum(found))))

#calculates the log of the likelihood that our data set would occur with 
#model governed by thetas
def log_likelihood(data, thetas, n_features):
    log_likelihood = 0
    for i,line in enumerate(data):
        y_hat = sigmoid(np.dot(thetas, line[:-1]))
        point_likelihood = line[-1] * np.log(y_hat) + \
                (1-line[-1]) * np.log(1 - y_hat)
        log_likelihood += point_likelihood
    print(log_likelihood)

#Given a training set, creates parameters for model and tests on test set
def run_logistic_regression(dataset_name, training_set, test_set):
    print('\n' + dataset_name + '\n')
    train, test, n_features = loadData([training_set, test_set])
    thetas = np.zeros(n_features)
    log_likelihood(train, thetas, n_features)
    thetas = trainData(train, n_features, 0.0001)
    log_likelihood(train, thetas, n_features)
    print(thetas)
    testData(thetas, test)

#the main routine
if __name__ == '__main__':
    run_logistic_regression('simple dataset', 'datasets/simple-train.txt', 'datasets/simple-test.txt')
    run_logistic_regression('netflix dataset', 'datasets/netflix-train.txt', 'datasets/netflix-test.txt')
    run_logistic_regression('ancestry dataset', 'datasets/ancestry-train.txt', 'datasets/ancestry-test.txt')
    run_logistic_regression('heart dataset', 'datasets/heart-train.txt', 'datasets/heart-test.txt')
