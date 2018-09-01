import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("oracle://ddscd:pass@192.168.199.115:1521/orcl, echo=True")


def read(path):
    df = pd.read_excel(path)
    return df


if __name__ == '__main__':
    df = read("indicator.xlsx")
    df.to_sql("DDS_ALL_INDICATORS", engine)
