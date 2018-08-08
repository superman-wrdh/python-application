# -*- encoding: utf-8 -*-
import numpy as np
import pandas as pd
from pprint import pprint


def df_process():
    """
    最近项目中需求
    """
    db_data = [{"A": 1, "B": 7, "C": 3}, {"A": 2, "B": 2, "C": 3}, {"A": 3, "B": 2, "C": 3}]
    df = pd.DataFrame(data=db_data)
    query_data_from_other_db = [1, 2]
    print("--------- raw data-----------")
    print(df)

    df["is_in"] = df.apply(lambda x: x['A'] in query_data_from_other_db, axis=1)
    print("---------- after process--------------")
    print(df)
    print("----------------------")
    db_data = [row.to_dict() for _, row in df.iterrows()]
    for i in db_data:
        pprint(i)
    print("---------------")


def df_fill_null():
    """
     过滤空数据
    """
    data = [{'A': 1, 'B': 7, 'C': 3},
            {'A': 2, 'B': None, 'C': 3},
            {'A': 3, 'B': 2, 'C': 3},
            {'A': None, 'B': 7, 'C': 3}]
    df = pd.DataFrame(data=data)  # dict None 变成DataFrame 之后会变成NaN

    df.notnull()
    df.notna()

    df.isna()
    df.isnull()

    # 过滤控制
    df.where(df.notnull(), None)  # 将df里面的 '空NaN' 变成 None
    df.where(df.notnull(), 'x')   #
    df.where(pd.notnull(df), 'y')  #


if __name__ == '__main__':
    # df_process()
    df_fill_null()
