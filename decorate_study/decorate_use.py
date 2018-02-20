# -*- coding:utf-8 -*-
"""
不带参数装饰器使用
"""


# 斐波拉数列 最简单递归算法 缺点 存在重复计算 速度慢
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# 斐波拉数列 使用缓存 速度快
def fibonacci_use_cache(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = fibonacci_use_cache(n - 1, cache) + fibonacci_use_cache(n - 2, cache)
    return cache[n]


# 将缓存功能写入到装饰器
def use_cache(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


# 使用装饰器
@use_cache
def fibonacci_use_decorate(n):
    if n <= 1:
        return 1
    return fibonacci_use_decorate(n - 1) + fibonacci_use_decorate(n - 2)


if __name__ == '__main__':
    # fibonacci(50) 短时间内计算不出来
    print(fibonacci_use_cache(100))
    print(fibonacci_use_decorate(100))