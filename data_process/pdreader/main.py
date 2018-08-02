# -*- encoding: utf-8 -*-
import pandas_datareader as pdr


if __name__ == '__main__':
    # 获取数据
    data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
