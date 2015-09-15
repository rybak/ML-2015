from ml import logistic
from ml.data import *

def optimize_regularization(data):
    rc_best, err_best = 0, 1000
    data_train, data_test = split(data)
    p_best = 0
    for p in range(-40, 10):
        # print_time()
        print("2 ** ", p)
        rc = 2 ** p
        theta = logistic.train(data_train, l=rc)
        err = logistic.average_error(data_test, theta)
        if err_best > err:
            rc_best, err_best = rc, err
            p_best = p
    return rc_best, p_best

def main():
    data = dataset_block(load_chips_dataset(), withOnes=False)
    reg_const, p = optimize_regularization(data)
    data_train, data_test = split(data)

    theta = logistic.train(data_train, l=reg_const)
    err = logistic.average_error(data_test, theta)

    print("average error:%6.2f\n" % err)
    print("regularization constant used: %16.10f\n" % reg_const)
    print(" == 2 ** ", p)

if __name__ == '__main__':
    main()
