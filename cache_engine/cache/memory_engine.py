import time
from cache.base import BaseCache
import pickle
import hashlib
from functools import wraps


class Data:
    def __init__(self, value, expire=None):
        self._value = value
        self._expire_time = expire + time.time() if expire else None

    def set_expire(self, expire):
        self._expire_time = expire + time.time() if expire else None

    def get(self):
        is_expire = False
        if self._expire_time:
            if time.time() > self._expire_time:
                self._value = None
                is_expire = True
        return self._value, is_expire


class MemoryCache(BaseCache):
    def __init__(self, db=0, *args, **kwargs):
        super().__init__()
        self._db = db if db is None else 0
        self._cache = {}
        self._cap = 0

    def get(self, db, key):
        key = db + ":" + key
        data_obj = self._cache.get(key)
        if data_obj:
            data, is_expire = data_obj.get()
            if is_expire:
                self.remove(db="", key=key)
                self._cap -= 1
            return data
        return None

    @property
    def length(self):
        return self._cap

    def cache_data(self, db, ex):
        def _cache(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                hash_key = hashlib.md5(pickle.dumps((func.__name__, args, kwargs))).hexdigest()
                cache = self.get(db=db, key=hash_key)
                if cache:
                    # get cache successful
                    return cache
                else:
                    # not fund cache,return data will be cache
                    d = func(*args, **kwargs)
                    self.set(db=db, key=hash_key, data=d, expire=ex)
                    return d

            return wrapper

        return _cache

    def set(self, db, key, data, expire=None):
        key = db + ":" + key
        data_obj = Data(data, expire=expire)
        self._cap += 1
        self._cache[key] = data_obj

    def remove(self, db, key):
        key = db + ":" + key
        if key in self._cache:
            self._cap -= 1
            return self._cache.pop(key)
        return None

    def expire(self, db, key, expire):
        key = db + ":" + key
        if key in self._cache:
            data_obj = self._cache.get(key)
            data_obj.set_expire(expire)
            return True
        return False

    def start_gc(self):
        pass
