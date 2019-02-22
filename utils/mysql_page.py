from utils.cache_iml import get_cache, to_cache
import pandas as pd
import hashlib
import pickle


class Pagination:
    def __init__(self, **kwargs):
        self.kw = kwargs or {}
        self.page = self.kw.get('page', 1)  # first page 1
        self.page_size = self.kw.get('page_size', 10)
        self.sql = self.kw.get("sql")
        self.engine = self.kw.get("engine")
        self.use_cache = self.kw.get("user_cache", False)  # 是否使用缓存
        self.cache_time = self.kw.get("cache_time", 3600)  # 缓存时间
        if self.cache_time is None:
            self.cache_time = 3600

    def _check(self):
        if self.sql is None or self.engine is None:
            raise Exception("un-init params [sql] or [db engine] ")
        if self.page is None:
            self.page = 1
        if self.page_size is None:
            self.page_size = 10
        if isinstance(self.page, str):
            self.page = int(self.page)
        if isinstance(self.page_size, str):
            self.page_size = int(self.page_size)

    @property
    def hash_key(self):
        return hashlib.md5(pickle.dumps((self.sql,))).hexdigest()

    def get_count(self):
        if self.use_cache:
            cache_count = get_cache(db="mysql_cache", key=self.hash_key + "count")
            if cache_count:
                print("get cache count")
                return cache_count
        sql = """ select count(1) as c
                          from ({}) as tb """.format(self.sql)
        count = pd.read_sql(sql, self.engine)['c'][0]
        if self.use_cache:
            print("cache count")
            to_cache(db="mysql_cache", key=self.hash_key + "count", data=count, expire=self.cache_time)
        return count

    def execute_sql(self, sql):
        sql_hash_key = hashlib.md5(pickle.dumps((sql,))).hexdigest()
        if self.use_cache:
            df = get_cache(db="mysql_cache", key=sql_hash_key + "db")
            if isinstance(df, pd.DataFrame):
                print("get cache data")
                return df

        df = pd.read_sql(sql, self.engine)
        if self.use_cache:
            print("cache data")
            to_cache(db="mysql_cache", key=sql_hash_key + "db", data=df, expire=self.cache_time)
        return df

    def __call__(self, *args, **kwargs):
        self._check()

        count = self.get_count()

        # 分页设置 不能整除加1 能整除不加1
        start_page, end_page = 1, int(count / int(self.page_size)) if int(
            count % int(self.page_size)) == 0 and count != 0 else int(count / int(self.page_size)) + 1
        if self.page < start_page:
            self.page = 1
        elif self.page > end_page:
            self.page = end_page
        self.sql = self.sql + "limit {start},{page_size}".format(start=(self.page - 1) * self.page_size,
                                                                 page_size=self.page_size)
        page_info = {
            "current_page": self.page,
            "total_page": end_page,
            "page_size": self.page_size,
            "data_size": count
        }

        return self.execute_sql(self.sql), page_info


if __name__ == '__main__':
    # mysql 通用分页查询 可选择是否使用缓存
    from time import time

    sql = "select * from asset_info "
    from sqlalchemy import create_engine

    test = create_engine("db config")

    page = 1
    page_size = 10
    p = Pagination(page=page, page_size=page_size, sql=sql, engine=test(), user_cache=True)
    s1 = time()
    data = p()
    s2 = time()
    print(s2 - s1)
    pass
