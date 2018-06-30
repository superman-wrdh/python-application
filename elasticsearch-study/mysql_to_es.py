import traceback
import pandas as pd
from elasticsearch import Elasticsearch
from datetime import datetime
from sqlalchemy.engine import create_engine


def engine():
    _engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
        'root',
        'wsw@2018',
        '127.0.0.1',  # 47.98.146.17   172.16.17.201    127.0.0.1
        '8612',
        'user_info',
    ), connect_args={"charset": "utf8"})
    return _engine


page_size = 10000
_es = Elasticsearch([{'host': '172.16.17.200', 'port': 9200}])
table = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']


def get_table_count(table):
    sql = "select count(*)  as num from {}".format(table)
    df = pd.read_sql(sql, engine())
    num = df.to_dict(orient='records')[0]['num']
    return num


def get_mysql_data(table, s, e):
    print('read table {} start {},end {}'.format(table, s, e))
    sql = "select *  from {} limit {} ,{}".format(table, s, e)
    df = pd.read_sql(sql, engine())
    df = df.where(df.notnull(),None)
    print('read finished')
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
    if _es.indices.exists(index='person') is not True:
        _es.indices.create(index='person', body=_index_mappings)


def add(data):
    try:
        _es.index(index='person', doc_type='user', refresh=True, body=data)
    except Exception as e:
        print("Exception", str(e))


def to_es(df):
    print('start to insert ')
    for _, rows in df.iterrows():
        todict = rows.to_dict()
        add(todict)
    print('insert a piece success')


def synchronize():
    init_index()
    for t in table:
        num = get_table_count(t)
        # assume page_size is 10 ,data num is 23 ,page is 3 or data num is 20,page is 2
        page = num / page_size if num % page_size == 0 else num / page_size + 1
        page = int(page)
        print(datetime.now(), 'table {} data count ,page size is {} ,page is '.format(t, page_size, page))
        # page 3
        for p in list(range(1, page + 1)):
            # p is 1 2 3
            if p < page:
                s, e = (p - 1) * page_size, p * page_size
                print(datetime.now(), 'table {} start {} end {}'.format(t, s, e))
                df = get_mysql_data(t, s, e)
                to_es(df)
            else:
                s, e = p * page_size, num
                print(datetime.now(), 'table {} start {} end {}'.format(t, s, e))
                df = get_mysql_data(t, s, e)
                to_es(df)


if __name__ == '__main__':
    synchronize()
