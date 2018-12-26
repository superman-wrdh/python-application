import pandas as pd
from elasticsearch import Elasticsearch

_es = Elasticsearch([{'host': '111.231.132.132', 'port': 9200}])


def init_index():
    _index_mappings = {
        "properties": {
            'id': {"type": "keyword"},
            'fund_id': {"type": "keyword"},
            'fund_full_name': {"type": "text", 'analyzer': 'ik_max_word', 'search_analyzer': 'ik_max_word'},
            'Name': {"type": "text", 'analyzer': 'ik_max_word', 'search_analyzer': 'ik_max_word'},
            'reg_time': {"type": "date"},
            'foundation_date': {"type": "date"},
            'update_time': {"type": "date"},
            'fund_status': {"type": "keyword"},
            'region': {"type": "text"},
            'is_internal': {"type": "short"},
            'is_reg': {"type": "short"},
            'reg_code': {"type": "text"},
            'data_freq': {"type": "keyword"},
            'fund_name_py': {"type": "text"},
            'person_id': {"type": "text"},
            'person_name': {"type": "text", 'analyzer': 'ik_max_word', 'search_analyzer': 'ik_max_word'},
            'org_id': {"type": "keyword"},
            'org_name': {"type": "text", 'analyzer': 'ik_max_word', 'search_analyzer': 'ik_max_word'},

            # 关于类型
            'issuing_way_code': {"type": "integer"},  # 发行方式
            'issuing_way_name': {"type": "keyword"},
            'issuing_way_scode': {"type": "integer"},
            'issuing_way_sname ': {"type": "keyword"},

            'investment_address_code': {"type": "integer"},  # 投资标地方
            'investment_address_name': {"type": "keyword"},
            'investment_address_scode': {"type": "integer"},
            'investment_address_sname': {"type": "keyword"},

            'strategy_code': {"type": "integer"},
            'strategy_name': {"type": "keyword"},
            'strategy_scode': {"type": "integer"},
            'strategy_sname': {"type": "keyword"},

            'structure_code': {"type": "integer"},
            'structure_name': {"type": "keyword"},
            'structure_scode': {"type": "integer"},
            'structure_sname': {"type": "keyword"},

            'nv_date': {"type": "date"},
            'nav': {"type": "float"},
            'added_nav': {"type": "float"},
            'swanav': {"type": "float"},

            'sdate': {"type": "date"},  # 以下指标数据的日期

            'm3_return': {"type": "float"},
            'm6_return': {"type": "float"},
            'y1_return': {"type": "float"},
            'y3_return': {"type": "float"},
            'y5_return': {"type": "float"},
            'year_return': {"type": "float"},
            'total_return': {"type": "float"},

            'm3_return_a': {"type": "float"},
            'm6_return_a': {"type": "float"},
            'y1_return_a': {"type": "float"},
            'y3_return_a': {"type": "float"},
            'y5_return_a': {"type": "float"},
            'year_return_a': {"type": "float"},
            'total_return_a': {"type": "float"},

            'm3_sharp_a': {"type": "float"},
            'm6_sharp_a': {"type": "float"},
            'y1_sharp_a': {"type": "float"},
            'y3_sharp_a': {"type": "float"},
            'y5_sharp_a': {"type": "float"},
            'year_sharp_a': {"type": "float"},
            'total_sharp_a': {"type": "float"},

            'm3_stdev_a': {"type": "float"},
            'm6_stdev_a': {"type": "float"},
            'y1_stdev_a': {"type": "float"},
            'y3_stdev_a': {"type": "float"},
            'y5_stdev_a': {"type": "float"},
            'year_stdev_a': {"type": "float"},
            'total_stdev_a': {"type": "float"},

            'm3_max_retracement': {"type": "float"},
            'm6_max_retracement': {"type": "float"},
            'y1_max_retracement': {"type": "float"},
            'y3_max_retracement': {"type": "float"},
            'y5_max_retracement': {"type": "float"},
            'year_max_retracement': {"type": "float"},
            'total_max_retracement': {"type": "float"},

            'is_collection': {"type": "boolean"},

            'row_num': {"type": "integer"},
            'y1_rank': {"type": "integer"},
            'total_rank': {"type": "integer"},
            'y3_rank': {"type": "integer"},
            'y2_rank': {"type": "integer"},

        }
    }
    # 姓名和地址采用ik分词
    if _es.indices.exists(index='fund_daily_indicator') is not True:
        _es.indices.delete(index='fund_daily_indicator', ignore=[400, 404])
        _es.indices.create(index='fund_daily_indicator', ignore=400)
        result = _es.indices.put_mapping(index='fund_daily_indicator', doc_type='fund', body=_index_mappings)
        print(result)
        print("create index success")
    else:
        print("index already exit ")
