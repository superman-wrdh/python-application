# -*- encoding: utf-8 -*-

import redis
import pickle
import hashlib
from functools import wraps

REDIS_PARAMS = {
    'host': "192.168.11.11",
    'port': 6379,
    'password': 'password',
    'time': 3600 * 4,
    'is_use_cache': True
}
REDIS_TIME = REDIS_PARAMS.get("time", 3600 * 8)
HOST = REDIS_PARAMS.get('host')
PORT = REDIS_PARAMS.get('port')
PASSWORD = REDIS_PARAMS.get('password')
r = redis.Redis(host=HOST, port=PORT, password=PASSWORD)
"""
redis + pickle缓存python任何对象
TODO 待实现缓存装饰器,思路:用户指定name,key为函数名字加参数,name+key 构成redis的 key
TODO 可能遇到的问题，不相同的函数有同样的函数名字和参数，数据会友覆盖问题(低概率事件)
"""


def to_cache(db, key, data, expire=REDIS_TIME):
    try:
        r_key = db + ":" + key
        p_data = pickle.dumps(data)
        r.set(name=r_key, value=p_data)
        r.expire(name=r_key, time=expire)
        return True
    except Exception as e:
        print(str(e))
        return False


def get_cache(db, key):
    try:
        r_key = db + ":" + key
        v = r.get(name=r_key)
        if v:
            return pickle.loads(v)
        else:
            return None
    except Exception as e:
        print(str(e))
        return None


def get_raw_cache(db, key):
    try:
        r_key = db + ":" + key
        v = r.get(name=r_key)
        if v:
            return v
        else:
            return None
    except Exception as e:
        print(str(e))
        return None


def redis_cache(db="", ex=REDIS_TIME):
    """
    @author superman-wrdh  see https://github.com/superman-wrdh
    @date 2018-8-27
    :param db: redis db
    :param ex: cache expire time
    :return:
    """

    def _cache(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            hash_key = hashlib.md5(pickle.dumps((func.__name__, args, kwargs))).hexdigest()
            cache = get_raw_cache(db=db, key=hash_key)
            if cache:
                # get cache successful
                print('get cache')
                return pickle.loads(cache)
            else:
                # not fund cache,return data will be cache
                print('cache data')
                d = func(*args, **kwargs)
                to_cache(db=db, key=hash_key, data=d, expire=ex)
                return d

        return wrapper

    return _cache


@redis_cache(db='test', ex=60)
def cache_test(a, b):
    return a + b


def obj_cache():
    import pandas as pd

    d = pd.DataFrame(data={"A": [1, 2, 3], "B": [4, 5, 6]})
    to_cache(db='test', key='1', data=d)
    c = get_cache(db='test', key='1')
    print(c)


if __name__ == '__main__':
    import time

    s = time.time()
    print(cache_test(6, 8))
    e = time.time()
    print(e - s)
