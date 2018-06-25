from sqlalchemy import create_engine
import pandas as pd
import pymysql

engine = create_engine("mysql+pymysql:://root:wsw@22018@47.98.146.17:8612/user_info")

"""
   col = ['Name', 'CardNo', 'Descriot', 'CtfTp', 'CtfId', 'Gender', 'Birthday', 'Address', 'Zip', 'Dirty', 'District1',
          'District2', 'District3', 'District4', 'District5', 'District6', 'FirstNm', 'LastNm', 'Duty', 'Mobile',
          'Tel', 'Fax', 'EMail', 'Nation', 'Taste', 'Education', 'Company', 'CTel', 'CAddress', 'CZip', 'Family',
          'Version', 'id']
"""


def read_date_from_csv():
    df = pd.read_csv(r"D:\data\2000W开房数据\2000W\1-200W.csv")
    return df


def to_mysql():
    pass
