import numpy as np
from os.path import exists
import time

import sys
def load_chips_dataset():
    data = open("chips.txt", "r")
    lines = data.readlines()
    n, d = len(lines), len(lines[0].split(',')) - 1
    x, y = np.empty((n, d)), np.empty(n)

    for i in range(n):
        line = lines[i].split(',')
        x[i] = np.array([float(f) for f in line[:-1]])
        y[i] = 1 if int(line[-1]) == 1 else -1
    return x, y

def split(data, fraction=0.2, shuffle=True):
    if shuffle:
        np.random.shuffle(data)
    point = int(len(data) * fraction)
    return data[point:], data[:point]

def split_xy(data):
    return data[:, :-1], data[:, -1]

def join_xy(data_x, data_y):
    return np.concatenate((data_x, data_y), axis=1)

def scale_features(data):
    return data / abs(np.outer(np.ones(len(data)), data.max(axis=0)))

def dataset_block(dataset, withOnes=True):
    x, y = dataset
    if withOnes:
        ones = np.empty((len(x), 1))
        ones.fill(1.0)
        x = join_xy(x, ones)
    return join_xy(x, y.reshape((len(y), 1)))


def print_time():
    localtime = time.asctime( time.localtime(time.time()))
    print("Time :", localtime, file = sys.stderr)


