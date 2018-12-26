import pandas as pd
from elasticsearch import Elasticsearch
import platform

"""
    if platform.system() == "Windows":
        host = '192.168.199.179'
        port = 9200
    elif platform.system() == "Linux":
        host = '127.0.0.1'
        port = 9200
    else:
        host = '66super.com'
        port = 10200

"""


def init():
    if platform.system() == "Windows":
        host = '192.168.199.179'
        port = 9200
    elif platform.system() == "Linux":
        host = '127.0.0.1'
        port = 9200
    else:
        host = '66super.com'
        port = 10200
    _es = Elasticsearch([{'host': host, 'port': port}])
    return _es


def search_by_name(name):
    _es = init()
    dsl = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"Name": name}},
                ]
            }
        },
        "from": 0, "size": 100
    }

    result = _es.search(index='user_index', body=dsl)
    print('query dsl', dsl)
    d = result['hits']['hits']
    content = []
    for i in d:
        tmp = i['_source']
        tmp['id'] = i['_id']
        content.append(tmp)
    df = pd.DataFrame(data=content)
    if df.empty:
        return None
    df = df[["Name", "Address", "id"]]
    df = df.fillna("-")
    return df.to_dict(orient='records')


def get_by_id(id):
    _es = init()
    dsl = {

        "query": {
            "terms": {
                "_id": [
                    id
                ]
            }
        }
    }
    result = _es.search(index='user_index', body=dsl)
    print('query dsl', dsl)
    r = result['hits']['hits']
    if r:
        return r[0]['_source']
    else:
        return None


if __name__ == '__main__':
    # search_by_name("何超")
    print(get_by_id("7509473"))
