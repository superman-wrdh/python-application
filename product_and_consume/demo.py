import time
from multiprocessing import Pool, cpu_count
import random
from datetime import datetime


def product(size=10):
    p = list(range(0, size))
    print("生成了", len(p), "物品")
    return p


def consumer(p):
    pid = random.randint(1000, 9999)
    print('\n', pid, '开始消费')
    time.sleep(2)
    print(pid, '消费', p, '成功', '\n')
    time.sleep(2)


if __name__ == '__main__':
    pool = Pool(processes=cpu_count())
    p = product()
    start = datetime.now()
    try:
        pool.map(consumer, p)
    except Exception as e:
        print(str(e))
    end = datetime.now()
    print("花费时间", (end - start).seconds)
