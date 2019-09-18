# -*- encoding: utf-8 -*-
import hashlib
import pickle
from functools import wraps
from cache.base import BaseCache


class RedisCache(BaseCache):
    """
    redis_connection = redis.Redis(host=HOST, port=PORT, password=PASSWORD, db=6, socket_connect_timeout=10, socket_timeout=10)
    """

    def __init__(self, redis_connection, debug=None, **kwargs):
        super().__init__()
        self.r = redis_connection
        self.REDIS_TIME = None
        self.DEBUG = debug

    def set(self, db, key, data, expire=None):
        try:
            r_key = db + ":" + key
            p_data = pickle.dumps(data)
            self.r.set(name=r_key, value=p_data)
            if expire and isinstance(expire, int):
                self.r.expire(name=r_key, time=expire)
            return True
        except Exception as e:
            print(str(e))
            return False

    def get_raw(self, db, key):
        try:
            r_key = db + ":" + key
            v = self.r.get(name=r_key)
            if v:
                return v
            else:
                return None
        except Exception as e:
            print(str(e))
            return None

    def get(self, db, key):
        try:
            r_key = db + ":" + key
            v = self.r.get(name=r_key)
            if v:
                return pickle.loads(v)
            else:
                return None
        except Exception as e:
            print(str(e))
            return None

    def remove(self, db, key):
        try:
            r_key = db + ":" + key
            self.r.delete(r_key)
            return True
        except Exception as e:
            print(str(e))
            return False

    def cache_data(self, db="", ex=None):
        def _cache(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                hash_key = hashlib.md5(pickle.dumps((func.__name__, args, kwargs))).hexdigest()
                cache = self.get_raw(db=db, key=hash_key)
                if cache:
                    # get cache successful
                    if self.DEBUG:
                        print('get cache')
                    return pickle.loads(cache)
                else:
                    # not fund cache,return data will be cache
                    if self.DEBUG:
                        print('cache data')
                    d = func(*args, **kwargs)
                    self.set(db=db, key=hash_key, data=d, expire=ex)
                    return d

            return wrapper

        return _cache