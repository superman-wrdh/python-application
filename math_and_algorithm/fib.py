# -*- encoding: utf-8 -*-
import time


def fib_n(n):
    if n <= 2:
        return 1
    else:
        content = [1, 1, 1]  # 从1开始
        for i in range(3, n + 1):
            content.append(content[i - 1] + content[i - 2])
    return content[n]


def fib_n_v2(n):
    if n <= 2:
        return 1
    else:
        content = [1, 1, 2]
        for i in range(3, n + 1):
            r = sum(content[0:2])
            l = content[1]
            content = [l, r]
        return content[1]


if __name__ == '__main__':
    # for i in [10, 100, 1000, 10000, 100000, 1000000][0:3]:
    #     s = time.clock()
    #     # fib_n(i)
    #     print(fib_n_v2(i))
    #     e = time.clock()
    #     print("n is {}, time {}".format(i, e - s), "\n")
    s = time.time()
    n = 10
    print(fib_n_v2(1000000))
    e = time.time()
    print("n is {}, time {}".format(n, e - s), "\n")
