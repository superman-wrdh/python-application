# -*- encoding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import webbrowser


def fun1():
    """
    clipboard data

        Feb 2018	Feb 2017	Change	Programming Language	Ratings	Change
    1	1		Java	14.988%	-1.69%
    2	2		C	11.857%	+3.41%
    3	3		C++	5.726%	+0.30%
    4	5	change	Python	5.168%	+1.12%
    5	4	change	C#	4.453%	-0.45%
    6	8	change	Visual Basic .NET	4.072%	+1.25%
    7	6	change	PHP	3.420%	+0.35%
    8	7	change	JavaScript	3.165%	+0.29%
    9	9		Delphi/Object Pascal	2.589%	+0.11%
    10	11	change	Ruby	2.534%	+0.38%
    :return:
    """
    # link = "https://www.tiobe.com/tiobe-index/"
    # webbrowser.open(link)
    df = pd.read_clipboard()
    print(type(df))


def api_description():
    data = [1, 2, 3]
    index = ['a', 'b', 'c']
    s = pd.Series(data=data, index=index)
    # s
    """
        a    1
        b    2
        c    3
        dtype: int64
    """
    s[1]  # scalar, 返回一个值
    # 2

    s[0:2]  # 范围，左闭右开，返回Series切片
    """
    a 1

    b 2

    dtype: int64
    """

    s[[0, 2]]  # 列表，返回Series切片
    """
    a 1

    c 3

    dtype: int64
    """

    mask = [False, True, False]  # mask，类似于列表，只是长度必须和Series相同，返回Series切片
    s[mask]
    """
    b 2

    dtype: int64
    """

    s.loc['b']  # 单索引，返回一个值 2

    s.loc['a':'c']  # 范围，注意：左闭右闭，返回Series切片
    """
    a 1
    b 2
    c 3
    dtype: int64
    """

    s.loc[['a', 'c']]  # 列表，返回Series切片
    """
    a 1
    c 3
    dtype: int64
    """

    mask = [False, True, False]  # mask，和iloc[]效果等同，返回Series切片
    s.loc[mask]
    """
    b 2
    dtype: int64
    """

    s.iloc[1]  # scalar, 返回一个值
    # Out[5]:
    # 2

    s.iloc[0:2]  # 范围，左闭右开，返回Series切片
    # Out[6]:
    # a 1
    # b 2
    # dtype: int64


def data_frame_api():
    # 创建dataframe

    # 二维数组
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df = pd.DataFrame(data=array, columns=['A', 'B', 'C'], index=None)

    """
       A  B  C
    0  1  2  3
    1  4  5  6
    2  7  8  9
    """
    # 一维数组
    arr = [{"A": 1, "B": 2, "C": 3}, {"A": 1, "B": 2, "C": 3}, {"A": 1, "B": 2, "C": 3}]
    pd.DataFrame(data=arr, columns=['A', 'B', 'C'], index=None)

    # 从字典
    kw = {"A": [1, 4, 7], "B": [2, 5, 6], "C": [3, 6, 9]}
    df = pd.DataFrame(data=array, columns=['A', 'B', 'C'], index=None)

    # 取数据相关

    df.values

    for index, row in df.iterrows():
        # row 为series
        print(index, row)
    df.index


if __name__ == '__main__':
    data_frame_api()
