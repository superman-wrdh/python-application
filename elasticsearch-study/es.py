import traceback
import pandas as pd
from elasticsearch import Elasticsearch
from datetime import datetime

_es = Elasticsearch([{'host': '192.168.199.139', 'port': 9200}])


def read_date_from_csv():
    df = pd.read_csv(r"D:\data\2000W\2000W\1-200W.csv")
    return df


def init_index():
    _index_mappings = {
        "mappings": {
            "user": {
                "properties": {
                    'Name': {"type": "text"}, 'CardNo': {"type": "text"}, 'Descriot': {"type": "text"},
                    'CtfTp': {"type": "text"}, 'CtfId': {"type": "text"}, 'Gender': {"type": "text"},
                    'Birthday': {"type": "text"}, 'Address': {"type": "text"}, 'Zip': {"type": "text"},
                    'Dirty': {"type": "text"}, 'District1': {"type": "text"},
                    'District2': {"type": "text"}, 'District3': {"type": "text"}, 'District4': {"type": "text"},
                    'District5': {"type": "text"}, 'District6': {"type": "text"}, 'FirstNm': {"type": "text"},
                    'LastNm': {"type": "text"}, 'Duty': {"type": "text"}, 'Mobile': {"type": "text"},
                    'Tel': {"type": "text"}, 'Fax': {"type": "text"}, 'EMail': {"type": "text"},
                    'Nation': {"type": "text"}, 'Taste': {"type": "text"}, 'Education': {"type": "text"},
                    'Company': {"type": "text"}, 'CTel': {"type": "text"}, 'CAddress': {"type": "text"},
                    'CZip': {"type": "text"}, 'Family': {"type": "text"},
                    'Version': {"type": "text"}, 'id': {"type": "text"}
                }
            }
        }
    }
    if _es.indices.exists(index='user_index') is not True:
        _es.indices.create(index='user_index', body=_index_mappings)


def add(data):
    try:
        _es.index(index='user_index', doc_type='user', refresh=True, body=data)
    except Exception as e:
        print("Exception", str(e))


def col_format():
    """
    col = ['Name', 'CardNo', 'Descriot', 'CtfTp', 'CtfId', 'Gender', 'Birthday', 'Address', 'Zip', 'Dirty', 'District1',
           'District2', 'District3', 'District4', 'District5', 'District6', 'FirstNm', 'LastNm', 'Duty', 'Mobile',
           'Tel', 'Fax', 'EMail', 'Nation', 'Taste', 'Education', 'Company', 'CTel', 'CAddress', 'CZip', 'Family',
           'Version', 'id']
    """


def main():
    init_index()
    df = read_date_from_csv()
    df = df.where(df.notnull(), None)
    df = df.loc[140672:]
    count = 0
    insert_start = datetime.now()
    print('start insert index')
    for _, rows in df.iterrows():
        todict = rows.to_dict()
        add(todict)
        count = count + 1
        if count % 10000 == 0:
            print("insert data rows ", count, " take times ", ((datetime.now()) - insert_start).seconds)
    print('finished', count)


if __name__ == '__main__':
    main()
