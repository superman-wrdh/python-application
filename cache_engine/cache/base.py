class BaseCache:

    def __init__(self, *args, **kwargs):
        pass

    def get(self, db, key):
        pass

    def set(self, db, key, data, expire=None):
        pass

    def expire(self, db, key, expire):
        pass

    def remove(self, db, key):
        pass
