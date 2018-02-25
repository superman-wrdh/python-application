# -*- encoding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import webbrowser


def fun1():
    """
    clipboard

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


if __name__ == '__main__':
    fun1()