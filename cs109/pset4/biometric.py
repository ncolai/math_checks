import numpy as np
import csv
from scipy.stats import norm

if __name__ == '__main__':
    X = np.genfromtxt('personKeyTimingA.txt',delimiter=',')
    Y = np.genfromtxt('personKeyTimingB.txt',delimiter=',')

    #expectation of X and Y
    print('{:.3f}'.format(X[len(X)-1][0]/len(X)))
    print('{:.3f}'.format(Y[len(Y)-1][0]/len(Y)))

    #expectation of X squared and Y squared
    X_indiv = X[1:,0] - X[:len(X) - 1, 0]
    Y_indiv = Y[1:,0] - Y[:len(Y) - 1, 0]
    print(sum(X_indiv) / len(X))
    print(sum(Y_indiv) / len(Y))
    print(sum(X_indiv * X_indiv) / len(X))
    print(sum(Y_indiv * Y_indiv) / len(Y))

    #ratio of probabilities of keystroke times of unknown emails
    unknown = np.genfromtxt('email.txt',delimiter=',')
    unknown_indiv = unknown[1:,0] - unknown[:len(unknown)-1,0]
    A = norm(7.407,3.938**0.5)
    B = norm(8.031,3.620**0.5)
    ratios = A.pdf(unknown_indiv)/B.pdf(unknown_indiv);
    print(np.prod(ratios))
