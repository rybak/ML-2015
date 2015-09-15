import numpy as np
from numpy.linalg import norm
import scipy.optimize as opt
import main
import math

def dist(x1, x2, p = 2):
    di = (x1[0] - x2[0]) ** p  + (x1[1] - x2[1]) ** p
    return di

def mysort(d):
    n = len(d)
    for i in range(n):
        for j in range(n - 1):
            if d[j][0] > d[j + 1][0]:
                d[j], d[j + 1] = np.array(d[j + 1]), np.array(d[j])
    return d

def KNN(train, x, k):
    n = len(train)
    d = np.zeros((n, 2))
    for i in range(n):
        d[i] = np.array([dist(train[i][:-1], x)] + [train[i][-1]])
    
    mysort(d)

    res = 0.0
    for i in range(k):
        res += d[i][-1]

    return 1 if res >= 0 else -1

def testing(train, test, k = 5):
    stats = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}
    result = {'pre': 0.0, 'rec': 0.0, 'er': 0.0, 'f1': 0.0}
    x, y = test[:, :-1], test[:, -1]
    for i in range(len(y)):
        res = KNN(train, x[i], k)
        if res == 1 and y[i] == 1.0:
            stats['tp'] += 1
        elif res == 1 and y[i] == -1.0:
            stats['fp'] += 1
        elif res == -1 and y[i] == 1.0:
            stats['fn'] += 1
        else:
            stats['tn'] += 1

    
    result['pre'] = stats['tp'] / (stats['tp'] + stats['fp'])
    result['rec'] = stats['tp'] / (stats['tp'] + stats['fn'])
    result['er'] = (stats['fp'] + stats['fn']) / len(y)
    result['f1'] = 2 * result['rec'] * result['pre'] / (result['rec'] + result['pre'])
    return result
