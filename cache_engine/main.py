from cache import RedisEngineConfig
from cache import MemoryEngineConfig
from cache import Cache


def use_redis_engine():
    import redis
    import time
    r = redis.Redis(host="127.0.0.1", port=6379, db=1, socket_connect_timeout=10, socket_timeout=10)

    config = RedisEngineConfig(redis_conn=r)
    cache = Cache(engine_config=config)
    cache.set(db="1", key="test", data={"a": 1}, expire=5)

    for i in range(10):
        print(cache.get(db="1", key="test"))
        time.sleep(1)

    @cache.cache_data(db="fun")
    def fun(a, b):
        return a + b

    print(fun(1, 2))
    print(fun(1, 2))
    print(fun(1, 2))


def user_memory_engine():
    import time
    config = MemoryEngineConfig()
    cache = Cache(engine_config=config)
    cache.set(db="1", key="test", data={"a": 1}, expire=5)

    for i in range(10):
        print(cache.get(db="1", key="test"))
        time.sleep(1)

    @cache.cache_data(db="fun")
    def fun(a, b):
        return a + b

    print(fun(1, 2))
    print(fun(1, 2))
    print(fun(1, 2))


if __name__ == '__main__':
    # use_redis_engine()
    user_memory_engine()
