# -*- coding:utf-8 -*-
import numpy as np


def array():
    """
    1 2 3
    3 4 5
    :return:
    """
    arr = np.array([[1, 2, 0], [4, 5, 6]])
    print(np.shape(arr))
    nonzero = np.nonzero(arr)
    ravel = np.ravel(arr)
    trace = np.trace(arr)
    diagonal = np.diagonal(arr)
    diagonal = np.squeeze(arr)


if __name__ == '__main__':
    array()

