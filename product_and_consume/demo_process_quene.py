"""
3、  消息队列模型
"""
'''
@author: jqy
'''
from multiprocessing import Process
import random
import time
import multiprocessing


def produce(speed, q):
    while True:
        for i in range(speed):
            item = random.random()
            q.put(item)
            print("生产者", speed, "生产了", str(item))
        time.sleep(1)


def consume(num, q):
    count = 0
    time_start = time.clock()
    while True:
        speed = random.randint(1, 5)
        for i in range(speed):
            item = q.get()
            print("消费者", "消费了", item)
            count = count + 1
            if (count == 20):
                time_end = time.clock()
                print("消费 " + str(count) + "个商品所用时间: %f s" % (time_end - time_start))
        time.sleep(1)


if __name__ == '__main__':
    q = multiprocessing.Queue(maxsize=5)

    Process(target=produce, args=(1, q)).start()

    Process(target=produce, args=(2, q)).start()

    Process(target=consume, args=(1, q)).start()
