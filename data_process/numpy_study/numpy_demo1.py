# -*- encoding: utf-8 -*-
import numpy as np


def created_data():
    """
    numpy 生成数据
    :return:
    """
    zeros = np.zeros((2, 3))
    ones = np.ones((2, 3))
    full = np.full((2, 3), 6)
    arange = np.arange(1, 10)
    linspace = np.linspace(1, 10, 100)
    random = np.random.random((3, 3))


def shape_operation():
    # 数组形状改变
    random = np.random.random(10)
    reshape = random.reshape(5, 2)
    transpose = reshape.transpose()
    ravel = reshape.ravel()


def numpy_concat():
    # 拼接
    A = np.ones((3, 3))
    B = np.zeros((3, 3))
    vstack = np.vstack((A, B))
    hstack = np.hstack((A, B))
    pass


def numpy_calculate():
    A = np.full((3, 3), 5)
    B = np.full((3, 3), 2)

    # 元素级别乘法
    AB = A * B

    # 矩阵乘法
    ABdot = np.dot(A, B)

    # 通用计算
    sqrt_A = np.sqrt(A)

    A_sum = np.sum(A)
    A_sum = A.sum()

    A_mean = np.mean(A)

    A_std = np.std(A)


if __name__ == '__main__':
    pass
