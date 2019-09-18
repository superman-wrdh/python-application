from cache.redis_engine import RedisCache
from cache.memory_engine import MemoryCache


class RedisEngineConfig:
    def __init__(self, redis_conn):
        self.r = redis_conn


class MemoryEngineConfig:
    def __init__(self, cap=None, memory_limit=None):
        self.cap = cap
        self.memory_limit = memory_limit


class Cache:
    def __init__(self, engine_config=None):
        self._engine_config = engine_config
        self._engine = None
        self._init_engine()

    def _init_engine(self):
        if isinstance(self._engine_config, RedisEngineConfig):
            self._engine = RedisCache(self._engine_config.r)
        elif isinstance(self._engine_config, MemoryEngineConfig):
            self._engine = MemoryCache()
        else:
            self._engine = MemoryCache()

    def cache_data(self, db="", ex=None):
        return self._engine.cache_data(db=db, ex=ex)

    def get(self, db, key):
        return self._engine.get(db, key)

    def mget(self):
        pass

    def set(self, db, key, data, expire):
        return self._engine.set(db, key, data, expire)

    def mset(self, **kwargs):
        pass

    def expire(self, db, key):
        pass

    def incr(self, db, key):
        pass

    def decr(self, db, key):
        pass

    def is_exit(self, db, key):
        pass

    def remove(self, db, key):
        self._engine.remove(db, key)

    def flush(self):
        pass

    def start_gc(self):
        pass

