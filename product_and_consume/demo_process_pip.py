"""
4、  管道模型：
"""
'''
Created on 2016/11/11
@author: jqy
'''
from multiprocessing import Process
import random
import time
import multiprocessing


def produce(speed, empty, p):
    while True:
        for i in range(speed):
            empty.acquire()
            item = random.random()
            p.send(item)
            print("生产者", speed, ",生产了", str(item))
        time.sleep(1)


def consume(num, empty, p):
    count = 0
    time_start = time.clock()
    while True:
        speed = random.randint(1, 5)
        for i in range(speed):
            item = p.recv()
            print("消费者", " 消费了", item)
            count = count + 1
            if (count == 20):
                time_end = time.clock()
                print("消费 " + str(count) + "个商品所用时间: %f s" % (time_end - time_start))
            empty.release()
        time.sleep(1)


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()

    empty = multiprocessing.Semaphore(5)

    Process(target=produce, args=(1, empty, child_conn)).start()

    Process(target=produce, args=(2, empty, child_conn)).start()

    Process(target=consume, args=(1, empty, parent_conn)).start()
