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


if __name__ == '__main__':
    df_process()
