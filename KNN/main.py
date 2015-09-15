import numpy as np
import random
import sys
import knn


def load_data():
    
    lines = open("chips.txt").readlines()
    n = len(lines)
    x = np.zeros((n, 3))
    
    for i in range(n):
        line = lines[i].split(',')
#        print(line)
        x[i] = np.array([float(f) for f in line[:-1]] + [1 if line[2][0] == '1' else -1])
    return x

def split(data, fraction=0.2):
    np.random.shuffle(data)
    point = int(len(data) * fraction)
    return data[point:], data[:point]

def main():
    sys.stdout = open('result', 'w')
    data = load_data()
    train, test = split(data)
    best = 0
    best_k = 0
    for k in range(2, 15):
        result = knn.testing(train, data, k)
        print("k: ", k)
        print("Total error: %.5f" % result['er'])
        print("Precision: %.5f" % result['pre'])
        print("Recall: %.5f" % result['rec'])
        print("F1-metric: %.5f" % result['f1'])

        if (result['f1'] > best):
            best = result['f1']
            best_k = k

    result = knn.testing(train, data, best_k)
    print("Best k:", best_k)
    print("Total error: %.5f" % result['er'])
    print("Precision: %.5f" % result['pre'])
    print("Recall: %.5f" % result['rec'])
    print("F1-metric: %.5f" % result['f1'])


if __name__ == '__main__':
    main()


