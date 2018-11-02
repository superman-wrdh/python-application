# -*- encoding: utf-8 -*-
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    df = pd.DataFrame(data={"X": [1, 2, 3, 4],
                            "Y": [1, 2, 4, 5]})
    # 通过pandas读取为DataFrame，回归用的是矩阵数据而不是列表，数据为n个样品点和m个特征值，这里特征值只有一个因此换证nx1的矩阵
    dataSet_x = df.loc[:, 'X'].as_matrix(columns=None)  # T为矩阵转置把1xn变成nx1
    dataSet_x = np.array([dataSet_x]).T
    dataSet_y = df.loc[:, 'Y'].as_matrix(columns=None)
    dataSet_y = np.array([dataSet_y]).T  # regr为回归过程，fit(x,y)进行回归
    regr = LinearRegression().fit(dataSet_x, dataSet_y)
    # 输出R的平方print(regr.score(dataSet_x, dataSet_y))
    plt.scatter(dataSet_x, dataSet_y, color='black')
    # 用predic预测，这里预测输入x对应的值，进行画线
    plt.plot(dataSet_x, regr.predict(dataSet_x), color='red', linewidth=1)
    plt.show()
