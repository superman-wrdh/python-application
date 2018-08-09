# -*- encoding: utf-8 -*-
import pandas as pd
from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch([{'host': '192.168.199.139', 'port': 9200}])


def init():
    # 初始化
    mapping = {
        'properties': {
            'title': {
                'type': 'text',
                'analyzer': 'ik_max_word',
                'search_analyzer': 'ik_max_word'
            }
        }
    }
    es.indices.delete(index='news', ignore=[400, 404])
    es.indices.create(index='news', ignore=400)
    result = es.indices.put_mapping(index='news', doc_type='politics', body=mapping)


def index_data():
    datas = [
        {
            'title': '美国留给伊拉克的是个烂摊子吗',
            'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
            'date': '2011-12-16'
        },
        {
            'title': '公安部：各地校车将享最高路权',
            'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
            'date': '2011-12-16'
        },
        {
            'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
            'url': 'https://news.qq.com/a/20111216/001044.htm',
            'date': '2011-12-17'
        },
        {
            'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
            'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
            'date': '2011-12-18'
        }
    ]
    print("#### " * 10, "索引数据", "####" * 10)
    for data in datas:
        es.index(index='news', doc_type='politics', body=data)
    print("#### " * 10, "查询数据数据", "####" * 10)
    result = es.search(index='news', doc_type='politics')
    print(result)


def chinese_analysis():
    """
    中文分词
    :return:
    """
    dsl = {
        'query': {
            'match': {
                'title': '中国 领事馆'
            }
        }
    }
    result = es.search(index='news', doc_type='politics', body=dsl)
    pprint(result)


if __name__ == '__main__':
    from pprint import pprint

    pprint(chinese_analysis())
